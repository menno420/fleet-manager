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
sessions is not fully covered. Identical bodies are one request (a retried call
is not a new round). The count never reads GitHub: a hook has ten seconds and no
promise of network, and a guard that sometimes cannot count is worse than one
that counts a smaller, honest thing.

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
import sys
from pathlib import Path

try:  # sibling module; sys.path[0] is this directory when run as a script
    from trigger_tools_guard import _strip_written_content
except Exception:  # pragma: no cover — never let an import trap the session

    def _strip_written_content(cmd: str) -> str:  # type: ignore[misc]
        return cmd


CAP = 3  # owner, live, 2026-09-02: "a maximum of 3 review rounds at most, never more"

STATE_DIR = Path(os.environ.get("TMPDIR", "/tmp")) / "claude-codex-rounds"

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
ENDPOINT_RE = re.compile(r"/(?:issues|pulls)/(\d+)/(?:comments|reviews)\b")
POST_RE = re.compile(
    r"(?:-X\s*POST|--request[= ]\s*POST|\s-d\s|\s--data(?:-raw|-binary)?[= ]|"
    r"\s--json[= ]|requests\.post\s*\(|\.post\s*\(|method\s*[:=]\s*[\"']POST[\"'])",
    re.I,
)

DENY_MSG = (
    "BLOCKED — this would be Codex review round {n} on PR #{pr} in this session, "
    "and the cap is {cap}. Owner, live, 2026-09-02, after fm #1010 ran 17 rounds "
    "overnight: \"I think there should be a maximum of 3 review rounds at most, "
    "never more than that.\"\n"
    "\n"
    "WHY THE LOOP DOES NOT CONVERGE ON ITS OWN: every fix is a new head, every "
    "new head 'needs' a review, and a reviewer shown a long prose document "
    "returns a P2 almost every time — on fm #1010, 5 of 17 rounds found only "
    "drift the previous round's own fix had caused. 'One clean round' is not a "
    "reachable exit condition; the cap is.\n"
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
    "Codex review round {n} of {cap} on PR #{pr} this session (cap: owner, "
    "2026-09-02, after fm #1010's 17 rounds). [D-0019]: intermediate fixes are "
    "verified on the free-key Gemini route or directly against source; Codex is "
    "for the head that flips. A fourth request will be denied."
)

LAST_MSG = (
    "Codex review round {n} of {cap} on PR #{pr} this session — THE LAST ONE THE "
    "CAP ALLOWS (owner, 2026-09-02). Whatever it returns: verify each finding "
    "against source, fix, disclose the residue in the PR comment and the card, "
    "then flip or hand off. A fourth request will be denied."
)


def _fingerprint(text: str) -> str:
    return hashlib.sha256(text.encode("utf-8", "replace")).hexdigest()[:12]


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


def _pr_from_input(ti: dict) -> str:
    for key in ("pullNumber", "pull_number", "issue_number", "issueNumber", "number"):
        v = ti.get(key)
        if v not in (None, ""):
            return str(v)
    return "unknown"


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
    if not m or not POST_RE.search(text):
        return None
    return m.group(1), text


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
    state = _load(session)
    entry = state.get(pr) or {"count": 0, "seen": []}
    fp = _fingerprint(text)
    if fp in entry["seen"]:
        return 0  # the same request again (a retry) is not a new round
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
            f"FM_ALLOW_CODEX_ROUND=1 override: Codex round {n} on PR #{pr}, past the "
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
