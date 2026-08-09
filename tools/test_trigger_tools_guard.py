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
    env["CLAUDE_SESSION_ID"] = session or f"test-{uuid.uuid4()}"
    env["TMPDIR"] = TMP
    if allow:
        env["FM_ALLOW_TRIGGER_DELETE"] = "1"
    else:
        env.pop("FM_ALLOW_TRIGGER_DELETE", None)
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

print("== the route around the tools ==")
check("curl -X DELETE .../triggers/<id> denied", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "curl -X DELETE https://api.example.com/v1/triggers/trig_01AB"}})), "deny")
check("python requests.delete on a trigger denied", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "python3 -c \"import requests; requests.delete(url + '/triggers/' + tid)\""}})), "deny")
check("path-then-verb ordering also denied", decision(run({
    "tool_name": "Bash",
    "tool_input": {"command": "TID=/triggers/trig_9; curl -X DELETE \"$BASE$TID\""}})), "deny")

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
check("unquoted heredoc delimiter also stripped",
      decision(run({"tool_name": "Bash", "tool_input": {"command":
          "cat > d.md <<EOF\ncurl -X DELETE $B/triggers/t1\nEOF\n"}})), "silent")
check("Write of a doc containing the pattern is silent",
      decision(run({"tool_name": "Write", "tool_input": {
          "file_path": "docs/x.md",
          "content": "never run: curl -X DELETE /triggers/trig_1"}})), "silent")
# ...and the real thing must still be caught AFTER a heredoc elsewhere in the
# same command, or stripping would become a bypass.
check("real delete AFTER an unrelated heredoc still denied",
      decision(run({"tool_name": "Bash", "tool_input": {"command":
          "cat > note.md <<'EOF'\nhello\nEOF\ncurl -X DELETE $B/triggers/trig_1\n"}})), "deny")

print("== fail-open: malformed input must never trap the session ==")
for bad in ({}, {"tool_name": None}, {"tool_name": "Bash", "tool_input": "notadict"}):
    check(f"malformed {str(bad)[:34]} silent", decision(run(bad)), "silent")

print()
print(f"{passed}/{passed + failed} passed")
sys.exit(1 if failed else 0)
