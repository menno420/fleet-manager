#!/usr/bin/env python3
"""PreToolUse guard for the one tool class that can stall a session outright.

**Owner-stated, 2026-08-09 (live):** *"Delete triggers are the only thing that
gives me an approval prompt in automode, this will stall your session untill I
get back. Always prevent using them."*

That makes `delete_trigger` categorically different from every other call this
estate makes. A successful call returns, a failed one raises, and a denied one
says so in writing — all three leave the session working. `delete_trigger`
**pauses and waits for a human**, and the session cannot see that it is waiting.
The owner is away by design during implementation, so the cost is not one prompt,
it is the remainder of the session.

Two behaviours, and the split is deliberate:

* **`delete_trigger` → DENY.** Every other advisory in this directory is advisory
  because it involves judgement — is this text a wall, is this claim propagated,
  is this table malformed. This one involves none: a tool name is an exact
  string, and the owner has stated there is no legitimate agent use. That is the
  shape `findings/2026-08-09-error-to-mechanism.md` § 2 calls ideal — the Edit
  tool's exact-match, which cannot be argued with — rather than a checker whose
  false positives have to be traded off. Escape hatch for the case where he asks
  for one directly: `FM_ALLOW_TRIGGER_DELETE=1`.
* **`send_later` → WARN.** It has a legitimate use (waiting on something genuinely
  external that will not notify), so denying it would be the mandatory-
  infrastructure-everywhere move the promotion rule rejects. But it was the wrong
  tool for the job it kept getting used for: **polling a PR.**
  `subscribe_pr_activity` is the owner's stated preference — push rather than
  poll, free while idle, and it never arms a trigger that later needs deleting.
  It does NOT deliver CI-success or new-push events, though (`CAPABILITIES.md`,
  MEASURED 2026-07-14), so it answers "did something happen" and never "is it
  green yet" — re-check the PR when you next act instead of waiting. fm #833 armed five `send_later` check-ins to watch one PR and then
  had to delete one, which is the whole failure in miniature: **the cleanup that
  stalls him was created by the polling that was not needed.**

Also covers the **direct-API route around the tools** — a `curl`/`requests` call
to `DELETE .../triggers/...`. A guard that only knows tool names is one `curl`
away from irrelevant, and this repo reaches GitHub and the CCR API over direct
egress constantly, so that route is not hypothetical.

**Why the Bash leg only warns, when the tool leg denies.** It was written as a
deny and downgraded the same hour, on evidence: **2 false positives, 0 true
positives.** Both false positives were this hook blocking its own authorship —
first the README section carrying a worked `curl -X DELETE .../triggers/...`
example, then the PR comment *asking a reviewer to check that very regex*, whose
text necessarily contained both halves of the pattern. Heredoc stripping fixed
the first and not the second, because the second sat inside a `python3 -c "..."`
string.

The general problem is undecidable by regex: `python3 -c "requests.delete(u +
'/triggers/' + t)"` must fire and `python3 -c "print('curl -X DELETE
/triggers/x')"` must not, and the two differ only in whether a string is
*executed* or *printed*. So the two legs are split by how much judgement they
need: **the tool name needs none** — it is an exact string with a stated rule, so
it denies. **The command text needs a lot** — so it warns, puts the rule in front
of the session at the moment of the call, and leaves the decision where the
judgement is. A guard that blocks its own documentation twice in one hour has
demonstrated its false-positive rate, and the promotion rule says that is the
number that decides.

Contract, as with every hook here: the process exits 0 on every path; a
deliberate deny is carried by ``permissionDecision: deny`` in the hook JSON. It
is silent unless it matches. ``send_later`` warns once per session, while each
distinct direct-API command gets its own warning slot so an earlier false
positive cannot silence a later real deletion. It matches on names and command
text only — it never inspects intent.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import sys
from pathlib import Path

STATE_DIR = Path(os.environ.get("TMPDIR", "/tmp")) / "claude-trigger-guard"

# Server prefix is deliberately loose: the same tool is exposed as
# `mcp__Claude_Code_Remote__…` here and `mcp__claude-code-remote__…` elsewhere,
# and a guard keyed to one spelling is silent for the other.
DELETE_TOOL_RE = re.compile(r"^mcp__.*__delete_trigger$", re.I)
SEND_LATER_RE = re.compile(r"^mcp__.*__send_later$", re.I)

# The route around the tools. Requires BOTH a delete verb and a trigger path, so
# an ordinary `curl` to any other endpoint stays silent.
_DELETE_VERB = (
    r"(?:-X\s*DELETE|--request[= ]\s*DELETE|\.delete\s*\(|"
    r"\.request\s*\(\s*[\"']DELETE[\"']|"
    r"method\s*[:=]\s*[\"']DELETE[\"'])"
)
API_DELETE_RE = re.compile(
    _DELETE_VERB + r"[\s\S]{0,400}?/triggers?/|"
    r"/triggers?/[\s\S]{0,400}?" + _DELETE_VERB,
    re.I,
)

DENY_MSG = (
    "BLOCKED — `delete_trigger` raises an approval prompt on the owner's screen "
    "in automode, and the session STALLS until he is physically back to click it. "
    "He stated this live on 2026-08-09 and asked that it always be prevented: "
    "\"Delete triggers are the only thing that gives me an approval prompt in "
    "automode, this will stall your session untill I get back.\"\n"
    "\n"
    "There is no agent-side reason to delete a trigger. A stale one-shot trigger "
    "has already fired and is inert (`ended_reason: run_once_fired`); leaving it "
    "costs nothing.\n"
    "\n"
    "**IF A TRIGGER IS ACTUALLY MISBEHAVING — firing repeatedly, misconfigured, "
    "burning quota — DISABLE IT, do not delete it:** call `update_trigger` with "
    "`enabled: false`. It is NOT blocked by this guard, it raises NO approval "
    "prompt, and it is reversible — the routine stays stored and can be "
    "re-enabled. Deleting is never the emergency stop; disabling is.\n"
    "\n"
    "STATE THE BOUND HONESTLY WHEN YOU REPORT IT. What is established is that "
    "**FUTURE firings stop** — the schema says 'Disabled Routines stay stored "
    "but never fire'. Whether it cancels a run ALREADY IN FLIGHT is UNVERIFIED "
    "here. So report 'further firings disabled', never 'the incident is "
    "contained', unless you have watched the in-flight run end. Deleting would "
    "not have given you that guarantee either — it would have given you a "
    "stalled session on top of the runaway.\n"
    "\n"
    "If it then genuinely needs removing rather than silencing, say so in your "
    "reply — he removes it in seconds, without a stalled session.\n"
    "\n"
    "Do NOT route around this with a direct API call — that produces the same "
    "prompt and the same stall. If he has explicitly asked you to delete one in "
    "this conversation, re-run with FM_ALLOW_TRIGGER_DELETE=1 set."
)

WARN_MSG = (
    "`send_later` is usually not the tool you want. If you are watching a PR, "
    "`subscribe_pr_activity` is the owner's stated preference — 2026-08-09: "
    "\"send later is also not necessary, if you want to check in on a PR you can "
    "subscribe to them.\" It is push rather than poll, free while idle, and it "
    "never arms a trigger that a later session feels tempted to clean up — and "
    "that cleanup is the call that stalls him.\n"
    "\n"
    "KNOW WHAT IT DELIVERS, THOUGH. `docs/CAPABILITIES.md` records a MEASURED "
    "limit (2026-07-14): PR subscriptions deliver comments, reviews and CI "
    "FAILURES, but **not CI-success or new-push events**. So a subscription will "
    "never wake you to say the PR went green.\n"
    "\n"
    "THE ANSWER IS NOT A TRIGGER — IT IS TO NOT END THE TURN. If you are waiting "
    "for green in order to merge, POLL TO A TERMINAL STATE INSIDE THE TURN: loop "
    "on `/repos/{o}/{r}/commits/{sha}/check-runs` until every run reports "
    "`status == completed`, then act. Measured on fm #833: a bounded loop "
    "(12 × 15 s) caught the transition on the 2nd iteration. Arms nothing, "
    "cannot strand you, and needs no wake at all.\n"
    "\n"
    "'Re-check when you next act' is NOT sufficient on its own and saying it was "
    "is the mistake this paragraph corrects: if nothing wakes you, there is no "
    "next act, and a session that ends waiting for a green event is simply "
    "stopped. Either poll to terminal inside the turn, or end the turn having "
    "said plainly that the PR is still pending and why.\n"
    "\n"
    "`send_later` is still right for a genuinely external wait that will not "
    "notify you at all (a deploy, a quota window, a human elsewhere). It is NOT "
    "the fallback for PR CI: if bounded in-turn polling cannot reach a terminal "
    "state, end the turn saying plainly that the PR is still pending and why."
)


def _fingerprint(text: str) -> str:
    """Short stable digest, so each distinct command gets its own dedup slot.

    The Bash leg is KNOWN to false-fire on prose that merely quotes the pattern.
    Keying dedup on a constant let the first such false positive consume the
    session's single warning, leaving a later REAL deletion silent at exactly
    the moment the warning matters. Codex, fm #834 (P2).
    """
    return hashlib.sha256(text.encode("utf-8", "replace")).hexdigest()[:12]


def once(key: str, session: str = "nosession") -> bool:
    """True the first time `key` is seen this session.

    The id comes from the EVENT (`session_id`), which the hook protocol always
    supplies and every other hook here already uses (`git_state_guard.py:177`).
    An earlier version read `CLAUDE_SESSION_ID` from the environment, which the
    host does not export: every session would have shared one `nosession.json`,
    so the first session to see a warning would have silenced it for all the
    rest. The suite hid this by manufacturing the variable itself — a test
    encoding the bug it should have caught. Codex, fm #834 (P2).
    """
    try:
        f = STATE_DIR / f"{session}.json"
        seen = set(json.loads(f.read_text())) if f.exists() else set()
        if key in seen:
            return False
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        f.write_text(json.dumps(sorted(seen | {key})))
        return True
    except Exception:
        return True  # losing state costs a duplicate line, never a silence


# A heredoc body is CONTENT being written, not a command being run. Stripping it
# before matching is what separates "delete a trigger" from "document that you
# must not delete a trigger" — and the two are otherwise byte-identical.
#
# This is not hypothetical: the first version of this guard BLOCKED THE COMMIT
# THAT DOCUMENTS IT. The README append below was a `cat >> … <<'MDEOF'` heredoc
# containing the worked example `curl -X DELETE $B/triggers/trig_1`, and the
# guard fired on its own documentation. The suite had a case for grepping the
# string and none for writing it — tested against the motivating case, not
# against the traffic the hook actually sits in, which is fm #831's lesson
# arriving for the third time.
_HEREDOC_RE = re.compile(r"<<-?\s*(['\"]?)([A-Za-z_][A-Za-z0-9_]*)\1[\s\S]*?^\2$",
                         re.M)

# A heredoc is only inert if its CONSUMER writes it somewhere. `bash <<'EOF'`,
# `sh <<EOF`, `python3 <<EOF` all EXECUTE the body, so stripping those would turn
# the guard off for the most obvious hiding place there is. Codex caught this on
# fm #834 (P2) — the first version stripped every heredoc, and the suite pinned
# that behaviour as correct, which is a test encoding a bug.
_SHELL_COMMAND_START = r"(?:^\s*|[;&|()]\s*|\b(?:then|do|else)\s+)"
_SHELL_PATH_PREFIX = r"(?:[^\s;&|()]*/)?"
_SHELL_PREFIX_TOKEN = (
    r"(?:[A-Za-z_][A-Za-z0-9_]*=(?:\"[^\"\n]*\"|'[^'\n]*'|[^\s;&|()]+)|"
    r"command|builtin|" + _SHELL_PATH_PREFIX
    + r"env|time|!|--?[A-Za-z0-9_-]+)"
)
_HEREDOC_EXECUTOR_WORD = (
    r"(?:(?:ba|z|k|da)?sh|python3?|perl|ruby|node|deno|eval|source)(?=[\s<])"
)
_HEREDOC_EXECUTOR_RE = re.compile(
    _SHELL_COMMAND_START
    + rf"(?:{_SHELL_PREFIX_TOKEN}\s+)*{_SHELL_PATH_PREFIX}"
    + rf"(?:{_HEREDOC_EXECUTOR_WORD}|\.(?=\s))"
    + r"[^\n<]*<<|"
    + r"\|\s*(?:ba|z)?sh(?=\s|$)",
    re.I | re.M,
)


def _strip_written_content(cmd: str) -> str:
    """Remove heredoc bodies — but ONLY when nothing executes them.

    Writing a doc that quotes a deletion must stay silent; piping the same text
    into a shell must not. When any interpreter-fed heredoc appears in the
    command, nothing is stripped — the safe direction, since over-matching here
    costs one advisory line and under-matching costs the whole guard.
    """
    if _HEREDOC_EXECUTOR_RE.search(cmd):
        return cmd
    return _HEREDOC_RE.sub(_strip_if_quoted, cmd)


def _strip_if_quoted(m: "re.Match[str]") -> str:
    """Strip only heredocs whose delimiter is QUOTED — those alone are literal.

    `cat > f <<EOF` expands `$(curl ...)` and backticks BEFORE writing, so an
    unquoted body is executable regardless of how inert the consumer looks.
    Only `<<'EOF'` / `<<"EOF"` guarantee the text is never interpreted. Codex,
    fm #834 (P2), on the tree that had already "fixed" heredocs once.
    """
    return " " if m.group(1) else m.group(0)


def _command_text(event: dict) -> str:
    ti = event.get("tool_input") or {}
    if not isinstance(ti, dict):
        return ""
    cmd = _strip_written_content(str(ti.get("command", "")))
    # `content` / `new_string` are file bodies by definition — never executed, so
    # they are excluded entirely rather than stripped. A doc that explains the
    # rule must be writable, or the rule cannot be recorded.
    return " ".join([cmd, str(ti.get("code", ""))])


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
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": text,
            },
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

    tool = str(event.get("tool_name") or "")
    session = str(event.get("session_id") or "nosession")
    allowed = os.environ.get("FM_ALLOW_TRIGGER_DELETE") == "1"

    if DELETE_TOOL_RE.match(tool):
        if allowed:
            return 0
        return deny(DENY_MSG)

    if SEND_LATER_RE.match(tool):
        return note(WARN_MSG) if once("send_later", session) else 0

    # The route around the tools, via direct egress. WARNS, does not deny — see
    # the module docstring's § "Why the Bash leg only warns".
    if tool in ("Bash", "BashOutput") and API_DELETE_RE.search(_command_text(event)):
        if allowed:
            return 0
        return note(
            "This command matches the shape of a trigger deletion over the direct "
            "API, which would produce the same owner approval prompt and the same "
            "stall as the `delete_trigger` tool.\n\n"
            "If that is what it does: **don't**. " + DENY_MSG + "\n\n"
            "If you are merely WRITING ABOUT the pattern — documentation, a PR "
            "comment, a test fixture — carry on; this warning cannot tell the two "
            "apart, which is exactly why it does not block."
        ) if once(f"api_delete:{_fingerprint(_command_text(event))}", session) else 0

    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException:
        sys.exit(0)  # fail open, always — a guard must never trap the session
