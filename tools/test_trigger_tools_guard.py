#!/usr/bin/env python3
"""Both-directions suite for `.claude/hooks/trigger_tools_guard.py`.

fm #831 measured the lesson this file is built around: a hook tested only
against its motivating defect and that defect's absence still shipped seven
real bugs, because the tests covered none of the **traffic the hook would
actually sit in**. For a `PreToolUse` guard that traffic is *every tool call the
session makes*, so the silence cases below outnumber the fire cases on purpose —
a guard that denies a legitimate call is worse than no guard, because the owner
is away and cannot wave it through.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
HOOK = REPO / ".claude" / "hooks" / "trigger_tools_guard.py"

passed = failed = 0


def run(event: dict, *, allow: bool = False, session: str | None = None) -> dict:
    env = dict(os.environ)
    env["TMPDIR"] = TMP
    if allow:
        env["FM_ALLOW_TRIGGER_DELETE"] = "1"
    else:
        env.pop("FM_ALLOW_TRIGGER_DELETE", None)
    event = {**event, "session_id": session or f"test-{uuid.uuid4()}"}
    p = subprocess.run(
        [sys.executable, str(HOOK)], input=json.dumps(event),
        capture_output=True, text=True, env=env, timeout=20,
    )
    if p.returncode != 0:
        return {"__exit__": p.returncode}
    try:
        return json.loads(p.stdout) if p.stdout.strip() else {}
    except json.JSONDecodeError:
        return {"__raw__": p.stdout}


def decision(out: dict) -> str:
    """'deny' | 'warn' | 'silent' — the only three outcomes that matter."""
    h = out.get("hookSpecificOutput") or {}
    if h.get("permissionDecision") == "deny":
        return "deny"
    if h.get("additionalContext"):
        return "warn"
    return "silent"


def check(name: str, actual: str, expected: str) -> None:
    global passed, failed
    if actual == expected:
        passed += 1
        print(f"  PASS {name}")
    else:
        failed += 1
        print(f"  FAIL {name}   [{actual}, wanted {expected}]")


TMP = tempfile.mkdtemp(prefix="trigger-guard-test-")

print("== the call that caused this: delete_trigger, any server spelling ==")
for tool in (
    "mcp__Claude_Code_Remote__delete_trigger",
    "mcp__claude-code-remote__delete_trigger",
    "mcp__CCR__delete_trigger",
):
    check(f"{tool} denied", decision(run({"tool_name": tool, "tool_input": {}})), "deny")

print("== the emergency stop must stay open ==")
# A denied delete with no alternative is a trap: an unattended session facing a
# runaway recurring trigger could neither stop it nor reach the owner. The answer
# is `update_trigger(enabled=false)` — stops firing at once, no approval prompt,
# reversible. These two cases pin that the escape exists AND that the deny
# message names it, because a path nobody is told about is not a path.
check("update_trigger (the disable path) is never blocked",
      decision(run({"tool_name": "mcp__Claude_Code_Remote__update_trigger",
                    "tool_input": {"trigger_id": "t", "enabled": False}})), "silent")
_deny = run({"tool_name": "mcp__Claude_Code_Remote__delete_trigger", "tool_input": {}})
_msg = (_deny.get("hookSpecificOutput") or {}).get("permissionDecisionReason", "")
check("the deny message names the disable path",
      "yes" if ("update_trigger" in _msg and "enabled" in _msg) else "no", "yes")

print("== the deliberate override ==")
check("FM_ALLOW_TRIGGER_DELETE=1 lets it through",
      decision(run({"tool_name": "mcp__Claude_Code_Remote__delete_trigger",
                    "tool_input": {}}, allow=True)), "silent")

print("== send_later warns, does not block ==")
check("send_later warns",
      decision(run({"tool_name": "mcp__Claude_Code_Remote__send_later",
                    "tool_input": {"message": "x"}})), "warn")
sess = f"test-{uuid.uuid4()}"
run({"tool_name": "mcp__Claude_Code_Remote__send_later", "tool_input": {}}, session=sess)
check("send_later warns ONCE per session",
      decision(run({"tool_name": "mcp__Claude_Code_Remote__send_later",
                    "tool_input": {}}, session=sess)), "silent")

print("== the route around the tools — WARNS, deliberately not deny ==")
# Downgraded from deny on measurement: 2 false positives, 0 true positives, both
# of them this hook blocking its own authorship. Command text cannot be judged by
# regex — `python3 -c "requests.delete(u+'/triggers/'+t)"` must fire and
# `python3 -c "print('curl -X DELETE /triggers/x')"` must not, and they differ
# only in whether a string is executed or printed.
check("curl -X DELETE .../triggers/<id> warns", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "curl -X DELETE https://api.example.com/v1/triggers/trig_01AB"}})), "warn")
check("python requests.delete on a trigger warns", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "python3 -c \"import requests; requests.delete(url + '/triggers/' + tid)\""}})), "warn")
check("path-then-verb ordering also warns", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "TID=/triggers/trig_9; curl -X DELETE \"$BASE$TID\""}})), "warn")
check("the API warning fires on a first match", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "curl -X DELETE $B/triggers/t2"}},
    session=(_s := f"test-{uuid.uuid4()}"))), "warn")
# Dedup is per-COMMAND, not per-session: a DIFFERENT command must warn again.
# This assertion used to demand silence here, which is precisely the defect
# Codex found — one false positive would consume the session's only warning and
# a later real deletion would pass unremarked.
check("  ...a DIFFERENT command warns again (dedup is per-command)", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "curl -X DELETE $B/triggers/t3"}}, session=_s)), "warn")
check("  ...the SAME command repeated is deduped", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "curl -X DELETE $B/triggers/t2"}}, session=_s)), "silent")
check("REAL PR-comment text that false-fired mid-session no longer denies", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "python3 -c \"print('does --request DELETE or -X DELETE hit the /triggers/ path?')\""}})), "warn")

print("== SILENCE on the traffic this hook actually sits in ==")
SILENT_TOOLS = [
    ("mcp__Claude_Code_Remote__create_trigger", {"name": "n", "prompt": "p"}),
    ("mcp__Claude_Code_Remote__list_triggers", {}),
    ("mcp__Claude_Code_Remote__update_trigger", {"trigger_id": "t"}),
    ("mcp__Claude_Code_Remote__fire_trigger", {"trigger_id": "t"}),
    ("mcp__Claude_Code_Remote__subscribe_pr_activity", {"owner": "o"}),
    ("mcp__github__merge_pull_request", {"pullNumber": 1}),
    ("Read", {"file_path": "x.md"}),
    ("Edit", {"file_path": "x.md", "new_string": "y"}),
    ("Write", {"file_path": "x.md", "content": "y"}),
    ("Grep", {"pattern": "delete_trigger"}),
]
for tool, ti in SILENT_TOOLS:
    check(f"{tool} silent", decision(run({"tool_name": tool, "tool_input": ti})), "silent")

print("== SILENCE on Bash that merely mentions triggers ==")
SILENT_CMDS = [
    "curl -sS https://api.example.com/v1/triggers | jq .",          # list, not delete
    "git log --oneline -1",                                          # unrelated
    "curl -X DELETE https://api.github.com/repos/o/r/git/refs/heads/x",  # delete, no trigger
    "grep -rn 'delete_trigger' docs/",                               # documenting it
    "echo 'do not use delete_trigger' >> docs/x.md",                 # writing the rule
]
for cmd in SILENT_CMDS:
    check(f"silent: {cmd[:48]}", decision(run({"tool_name": "Bash",
                                               "tool_input": {"command": cmd}})), "silent")

print("== WRITING about the pattern is not DOING it ==")
# The first version of this guard blocked the very commit that documents it: a
# `cat >> README <<'MDEOF'` heredoc carrying the worked example
# `curl -X DELETE $B/triggers/trig_1`. Measured, not imagined — the deny text
# came back as a tool error mid-session.
HEREDOC = (
    "cat >> .claude/hooks/README.md <<'MDEOF'\n"
    "# denied — the route around it\n"
    "echo 'x' | curl -X DELETE $B/triggers/trig_1\n"
    "MDEOF\n"
)
check("heredoc documenting the pattern is silent",
      decision(run({"tool_name": "Bash", "tool_input": {"command": HEREDOC}})), "silent")
# This case used to expect silence — encoding the bug. An UNQUOTED delimiter
# expands $() and backticks before the file is written, so the body is not
# guaranteed inert and must stay inspectable. Only <<'EOF' is literal.
check("unquoted heredoc is NOT treated as inert",
      decision(run({"tool_name": "Bash", "tool_input": {"command":
          "cat > d.md <<EOF\ncurl -X DELETE $B/triggers/t1\nEOF\n"}})), "warn")
check("Write of a doc containing the pattern is silent",
      decision(run({"tool_name": "Write", "tool_input": {
          "file_path": "docs/x.md",
          "content": "never run: curl -X DELETE /triggers/trig_1"}})), "silent")
# ...and the real thing must still be caught AFTER a heredoc elsewhere in the
# same command, or stripping would become a bypass.
check("real delete AFTER an unrelated heredoc still warns",
      decision(run({"tool_name": "Bash", "tool_input": {"command":
          "cat > note.md <<'EOF'\nhello\nEOF\ncurl -X DELETE $B/triggers/trig_1\n"}})), "warn")

print("== fail-open: malformed input must never trap the session ==")
for bad in ({}, {"tool_name": None}, {"tool_name": "Bash", "tool_input": "notadict"}):
    check(f"malformed {str(bad)[:34]} silent", decision(run(bad)), "silent")

print("== Codex round 1 on #834 — regressions pinned ==")
check("curl --request DELETE is caught (long-form flag)", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "curl --request DELETE https://api.x/v1/triggers/trig_1"}})), "warn")
check("bash <<EOF that EXECUTES a deletion is not stripped", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "bash <<'EOF'\ncurl -X DELETE $B/triggers/trig_1\nEOF\n"}})), "warn")
check("piping a heredoc into sh is not stripped", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "cat <<'EOF' | sh\ncurl -X DELETE $B/triggers/t\nEOF\n"}})), "warn")
check("python3 <<EOF that executes is not stripped", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "python3 <<'EOF'\nimport requests; requests.delete(u+'/triggers/'+t)\nEOF\n"}})), "warn")
# ...and the inert case must STILL be silent, or the fix is just a revert.
check("cat > file <<EOF (inert) is still silent", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "cat > d.md <<'EOF'\ncurl -X DELETE $B/triggers/t1\nEOF\n"}})), "silent")
check("state is per-session via the EVENT, not an env var", decision(run({
    "tool_name": "mcp__Claude_Code_Remote__send_later", "tool_input": {}},
    session="codex-a")), "warn")
check("  ...a DIFFERENT session still gets its own warning", decision(run({
    "tool_name": "mcp__Claude_Code_Remote__send_later", "tool_input": {}},
    session="codex-b")), "warn")

print()
print("== Codex round 2 on #834 — regressions pinned ==")
# P2a: only a QUOTED delimiter is literal. `<<EOF` expands $() before writing.
check("unquoted heredoc with $(...) is NOT stripped", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "cat > note <<EOF\n$(curl --request DELETE $B/triggers/t)\nEOF\n"}})), "warn")
check("unquoted heredoc with backticks is NOT stripped", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "cat > note <<EOF\n`curl -X DELETE $B/triggers/t`\nEOF\n"}})), "warn")
check("QUOTED heredoc (literal) is still silent", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "cat > d.md <<'EOF'\ncurl -X DELETE $B/triggers/t1\nEOF\n"}})), "silent")

# P2d: a known false positive must not consume the session's only warning.
_s2 = f"test-{uuid.uuid4()}"
check("a false-positive doc command warns first", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "python3 -c \"print('curl -X DELETE /triggers/x is banned')\""}},
    session=_s2)), "warn")
check("  ...and a LATER REAL deletion still warns (dedup not burned)", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "curl -X DELETE https://api.x/v1/triggers/trig_real"}},
    session=_s2)), "warn")
check("  ...but the SAME command twice is still deduped", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "curl -X DELETE https://api.x/v1/triggers/trig_real"}},
    session=_s2)), "silent")

# P2c: the deny must not promise more than is established.
_d = run({"tool_name": "mcp__Claude_Code_Remote__delete_trigger", "tool_input": {}})
_m = (_d.get("hookSpecificOutput") or {}).get("permissionDecisionReason", "")
check("deny states the in-flight bound rather than promising immediacy",
      "yes" if ("UNVERIFIED" in _m and "IN FLIGHT" in _m) else "no", "yes")
check("deny no longer claims it stops firing immediately",
      "yes" if "stops firing immediately" not in _m else "no", "yes")

print()
print(f"{passed}/{passed + failed} passed")
sys.exit(1 if failed else 0)
