#!/usr/bin/env python3
"""PreToolUse guard: at most THREE Codex review rounds per PR per session.

**Owner-stated, 2026-09-02 (live), after reading the night session's PR:**
*"For some reason it thought it was necessary to have 17 rounds of codex
reviews. I thought there was a rule to prevent this from happening. Apparently
not a good rule. I think there should be a maximum of 3 review rounds at most,
never more than that."*

There was a rule — [D-0019], 2026-08-29: *"lets keep the codex reviews until the
PR is ready to flip to green. I don't think It's necessary to review after every
push, that just wastes the usage limits."* It was prose, in the boot file and the
decision ledger, and fm #1010 requested a round after **every** push anyway:
17 rounds, 91 findings, 03:00Z → 06:30Z, on one 931-line report. Nothing in the
session's feedback channel ever said *stop*; the harness's own drive-to-green
text says the opposite (*"there is no round limit"*), and the session quoted
that line back in its round-13 comment. A rule that is only stated has never
bound anything here (`docs/findings/2026-08-08-why-rules-dont-bind.md`: 116
statements, 0 catches) — so this is the mechanism, delivered at the one moment
it applies: the call that would post the next `@codex review`.

Two legs, and the split follows `trigger_tools_guard.py`'s reasoning exactly:

* **MCP comment tools → count, then DENY the fourth.** `add_issue_comment`,
  `pull_request_review_write`, `add_reply_to_pull_request_comment` carry the
  comment body as a named field, so "this call posts `@codex review` on PR #N"
  is an exact string match with no judgement in it — the shape a deny needs.
  Rounds 1–3 are allowed and *counted out loud* (one line each), so the wall is
  never a surprise. Round 4+ is denied with the exit the owner wants instead:
  fix what the last round found, disclose the residue, flip or hand off.
* **Bash → the same, but only when the command visibly POSTS a comment.** A
  `curl … /issues/N/comments -d '…@codex review…'` is the route around the tools
  and this repo uses it constantly. It counts only when the phrase, a comment
  endpoint and a POST verb all appear in the executed text; a `grep` for the
  phrase, a doc written through a quoted heredoc, or a commit message that
  mentions it stay silent. The heredoc discipline is imported from the trigger
  guard rather than re-derived — that file paid for it twice.

**What the count is, honestly.** Session-local, per PR number, keyed by the
event's `session_id` like every other hook here. A PR another session already
reviewed starts at zero here — fm #1010's 17 rounds were one session, so this
guard would have stopped it at 04:00Z instead of 06:30Z, but a PR passed across
sessions is not fully covered. A retried call is not a new round: an identical body
**on the same checked-out head** is deduplicated. The head is part of the key
because the body alone is not one — a session that posts the literal
`@codex review` on every fix commit is running new rounds, and keying on the
text alone would have counted fm #1010's seventeen as one (Codex, fm #1011
round 1, the first thing it found). The count never reads GitHub: a hook has
ten seconds and no promise of network, and a guard that sometimes cannot count
is worse than one that counts a smaller, honest thing.

**Deliberate override:** `FM_ALLOW_CODEX_ROUND=1`, for the case where he asks
for another round himself. A guard with no escape becomes a wall someone edits
out (the trigger guard's lesson, kept).

Contract, as with every hook here: exits 0 on every path; a deny is carried by
``permissionDecision: deny`` in the hook JSON; silent unless it matches.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path

try:
    import fcntl
except ImportError:  # pragma: no cover — non-POSIX: run unlocked, never fail
    fcntl = None

try:  # sibling module; sys.path[0] is this directory when run as a script
    from trigger_tools_guard import _strip_written_content
except Exception:  # pragma: no cover — never let an import trap the session

    def _strip_written_content(cmd: str) -> str:  # type: ignore[misc]
        return cmd


CAP = 3  # owner, live, 2026-09-02: "a maximum of 3 review rounds at most, never more"

STATE_DIR = Path(os.environ.get("TMPDIR", "/tmp")) / "claude-codex-rounds"
REPO = Path(__file__).resolve().parents[2]

# The phrase Codex's own About-block documents as the trigger. `@codex address
# that feedback` is a different command and is not a round.
REQUEST_RE = re.compile(r"@codex\s+(?:security\s+)?review\b", re.I)

COMMENT_TOOL_RE = re.compile(
    r"^mcp__.*__(?:add_issue_comment|pull_request_review_write|"
    r"add_reply_to_pull_request_comment)$",
    re.I,
)

# Bash leg: the executed text must show all three — the phrase, a comment
# endpoint, and something that sends a body. Any one alone is prose.
ENDPOINT_RE = re.compile(
    r"(?:repos/(?P<repo>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+))?/(?:issues|pulls)/(?P<pr>\d+)/(?:comments|reviews)\b"
)
# The GitHub CLI posts without a literal endpoint or verb (Codex, fm #1011 round
# 2, P1): `gh pr comment 77 --body '@codex review'`, `gh pr review 77 --comment
# -b '…'`, and `gh api repos/o/r/issues/77/comments -f body='…'` (a field flag
# switches gh's method to POST, per `gh api --help`).
# `gh pr comment [<number> | <url> | <branch>]` — the URL form carries the
# repository and the number (Codex, fm #1011 round 3); a branch target leaves
# the number unknown, written `?`.
GH_PR_RE = re.compile(
    r"\bgh\s+pr\s+(?:comment|review)\s+"
    r"(?:(?P<pr>\d+)|(?P<url>https?://github\.com/(?P<urepo>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)/pull/(?P<upr>\d+))|\S+)"
    r"(?P<rest>[^\n|;&]*)",
    re.I,
)
GH_REPO_FLAG_RE = re.compile(r"(?:^|\s)(?:-R|--repo)[= ]\s*(?P<repo>[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+)")
GH_API_RE = re.compile(r"\bgh\s+api\b(?P<rest>[^\n|;&]*)", re.I)
GH_API_POST_RE = re.compile(r"(?:\s-[fF]\s|\s--(?:raw-)?field[= ]|\s--input[= ]|-X\s*POST|--method[= ]\s*POST)", re.I)
# `gh api --method GET … -f k=v` sends the fields as a query string (`gh api
# --help`); an explicit GET is a read whatever fields it carries (Codex, fm #1011
# round 3).
GH_API_GET_RE = re.compile(r"(?:-X|--method)[= ]?\s*GET\b", re.I)
POST_RE = re.compile(
    r"(?:-X\s*POST|--request[= ]\s*POST|\s-d\s|\s--data(?:-raw|-binary)?[= ]|"
    r"\s--json[= ]|requests\.post\s*\(|\.post\s*\(|method\s*[:=]\s*[\"']POST[\"'])",
    re.I,
)

DENY_MSG = (
    "BLOCKED — this would be Codex review round {n} on {pr} in this session, "
    "and the cap is {cap}. Owner, live, 2026-09-02, after fm #1010 ran 17 rounds "
    "overnight: \"I think there should be a maximum of 3 review rounds at most, "
    "never more than that.\"\n"
    "\n"
    "WHY THE LOOP DOES NOT CONVERGE ON ITS OWN: every fix is a new head, every "
    "new head 'needs' a review, and a reviewer shown a long prose document "
    "returns a P2 almost every time — on fm #1010, a third of all 88 findings "
    "were drift a previous round's own fix had caused, and three rounds (5, 16, "
    "17) found nothing else. 'One clean round' is not a reachable exit "
    "condition; the cap is.\n"
    "\n"
    "WHAT TO DO INSTEAD, in this order:\n"
    "1. Fix what the last round found. Verify each finding against the raw "
    "source before accepting it — never on the reviewer's word alone.\n"
    "2. Verify your own fix without Codex: the free-key Gemini route "
    "(`gemini-3.6-flash`, one call with the findings + the diff — [D-0019]), or "
    "a direct re-check against the source. That fully discharges the "
    "verification owed on a non-flip head.\n"
    "3. Disclose whatever stays unfixed, in the PR comment and the session "
    "card, marked as such.\n"
    "4. Then flip the card and land — or, if you judge the residue too large to "
    "ship, hand off: write the state down and end the turn saying plainly what "
    "is open. Merging with a known error hidden is not an option; a fourth "
    "round is not either.\n"
    "\n"
    "Do NOT route around this with a direct API call — same cap, same reason. "
    "If the owner has asked for another round in THIS conversation, re-run with "
    "FM_ALLOW_CODEX_ROUND=1 set."
)

COUNT_MSG = (
    "Codex review round {n} of {cap} on {pr} this session (cap: owner, "
    "2026-09-02, after fm #1010's 17 rounds). [D-0019]: intermediate fixes are "
    "verified on the free-key Gemini route or directly against source; Codex is "
    "for the head that flips. A fourth request will be denied."
)

LAST_MSG = (
    "Codex review round {n} of {cap} on {pr} this session — THE LAST ONE THE "
    "CAP ALLOWS (owner, 2026-09-02). Whatever it returns: verify each finding "
    "against source, fix, disclose the residue in the PR comment and the card, "
    "then flip or hand off. A fourth request will be denied."
)


def _head(event: dict) -> str:
    """The checked-out commit the request is made from, or "" if unreadable.

    Read from the event's ``cwd`` (the session root), this file's repo as the
    fallback. "" makes ``main`` skip deduplication entirely — the safe direction
    is to count, so an unreadable head never turns a new round into a retry.
    """
    cwd = str(event.get("cwd") or REPO)
    try:
        p = subprocess.run(["git", "-C", cwd, "rev-parse", "HEAD"],
                           capture_output=True, text=True, timeout=3)
        return p.stdout.strip() if p.returncode == 0 else ""
    except Exception:
        return ""


def _fingerprint(head: str, text: str) -> str:
    return hashlib.sha256((head + "\n" + text).encode("utf-8", "replace")).hexdigest()[:12]


def _load(session: str) -> dict:
    try:
        f = STATE_DIR / f"{session}.json"
        return json.loads(f.read_text()) if f.exists() else {}
    except Exception:
        return {}


def _save(session: str, state: dict) -> None:
    try:
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        (STATE_DIR / f"{session}.json").write_text(json.dumps(state))
    except Exception:
        pass  # losing state costs one uncounted round, never a stalled session


def _key(repo: str | None, pr: str | None) -> str:
    """`owner/repo#N` — the repository is part of the identity (Codex, fm #1011
    round 2, P2): a session working two repositories must not let `a#42` and
    `b#42` share one allowance. Unknown halves are spelled out, never guessed."""
    return f"{repo or '?'}#{pr or '?'}"


def _pr_from_input(ti: dict) -> str:
    for key in ("pullNumber", "pull_number", "issue_number", "issueNumber", "number"):
        v = ti.get(key)
        if v not in (None, ""):
            return _key(f"{ti.get('owner')}/{ti.get('repo')}" if ti.get("owner") and ti.get("repo") else None, str(v))
    return _key(None, None)


def _mcp_request(event: dict) -> tuple[str, str] | None:
    """(pr, body) when an MCP comment tool is about to post a review request."""
    ti = event.get("tool_input") or {}
    if not isinstance(ti, dict):
        return None
    body = " ".join(str(ti.get(k, "")) for k in ("body", "text", "comment", "event"))
    if not REQUEST_RE.search(body):
        return None
    return _pr_from_input(ti), body


def _bash_request(event: dict) -> tuple[str, str] | None:
    """(pr, text) when a shell command visibly POSTs a review request."""
    ti = event.get("tool_input") or {}
    if not isinstance(ti, dict):
        return None
    text = _strip_written_content(str(ti.get("command", "")))
    if not REQUEST_RE.search(text):
        return None
    m = ENDPOINT_RE.search(text)
    if m and (POST_RE.search(text) or GH_API_RE.search(text)):
        if not POST_RE.search(text):  # gh api: a field flag or an explicit method is the POST
            api = GH_API_RE.search(text)
            rest = " " + (api.group("rest") if api else "") + " "
            if not api or GH_API_GET_RE.search(rest) or not GH_API_POST_RE.search(rest):
                return None
        return _key(m.group("repo"), m.group("pr")), text
    g = GH_PR_RE.search(text)
    if g:
        flag = GH_REPO_FLAG_RE.search(text)
        repo = g.group("urepo") or (flag.group("repo") if flag else None)
        return _key(repo, g.group("pr") or g.group("upr")), text
    return None


def deny(reason: str) -> int:
    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "permissionDecision": "deny",
                "permissionDecisionReason": reason,
            }
        },
        sys.stdout,
    )
    return 0


def note(text: str) -> int:
    json.dump(
        {
            "hookSpecificOutput": {"hookEventName": "PreToolUse", "additionalContext": text},
            "suppressOutput": True,
        },
        sys.stdout,
    )
    return 0


def main() -> int:
    try:
        event = json.loads(sys.stdin.read() or "{}")
    except Exception:
        return 0
    if str(event.get("hook_event_name") or "PreToolUse") != "PreToolUse":
        return 0

    tool = str(event.get("tool_name") or "")
    if COMMENT_TOOL_RE.match(tool):
        hit = _mcp_request(event)
    elif tool in ("Bash", "BashOutput"):
        hit = _bash_request(event)
    else:
        hit = None
    if hit is None:
        return 0

    pr, text = hit
    session = str(event.get("session_id") or "nosession")
    # One hook process per tool call, and a parallel tool batch runs several at
    # once: without a lock every one of them reads count=0 and passes as round 1
    # (Codex, fm #1011 round 3: 12 parallel requests, all allowed). The whole
    # load → decide → save transaction runs under a per-session lock; if the
    # lock cannot be taken the guard still counts, unlocked — fail open, never
    # fail silent.
    lock = None
    try:
        if fcntl is not None:
            STATE_DIR.mkdir(parents=True, exist_ok=True)
            lock = open(STATE_DIR / f"{session}.lock", "a+")
            fcntl.flock(lock, fcntl.LOCK_EX)
    except Exception:
        lock = None
    try:
        return _decide(event, pr, text, session)
    finally:
        if lock is not None:
            try:
                fcntl.flock(lock, fcntl.LOCK_UN)
                lock.close()
            except Exception:
                pass


def _decide(event: dict, pr: str, text: str, session: str) -> int:
    state = _load(session)
    entry = state.get(pr) or {"count": 0, "seen": []}
    head = _head(event)
    fp = _fingerprint(head, text)
    if head and fp in entry["seen"]:
        return 0  # the same request on the same head (a retry) is not a new round
    n = int(entry["count"]) + 1
    allowed = os.environ.get("FM_ALLOW_CODEX_ROUND") == "1"

    if n > CAP and not allowed:
        return deny(DENY_MSG.format(n=n, pr=pr, cap=CAP))

    entry["count"] = n
    entry["seen"] = (entry["seen"] + [fp])[-50:]
    state[pr] = entry
    _save(session, state)

    if n > CAP:  # override in effect — say so, keep counting
        return note(
            f"FM_ALLOW_CODEX_ROUND=1 override: Codex round {n} on {pr}, past the "
            f"cap of {CAP}. Name the owner's ask that authorised it in the card."
        )
    if n == CAP:
        return note(LAST_MSG.format(n=n, pr=pr, cap=CAP))
    return note(COUNT_MSG.format(n=n, pr=pr, cap=CAP))


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException:
        sys.exit(0)  # fail open, always — a guard must never trap the session
