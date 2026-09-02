#!/usr/bin/env python3
"""Both-directions suite for `.claude/hooks/codex_round_guard.py`.

Same shape as `test_trigger_tools_guard.py`, for the same reason (fm #831): a
`PreToolUse` guard sits in every tool call the session makes, so the silence
cases outnumber the fire cases on purpose. The motivating case is fm #1010 —
17 `@codex review` requests in one session — and the suite walks that exact
sequence: three counted rounds, the fourth denied, the override honoured, a
retry not double-counted, and a second PR counted on its own.
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
HOOK = REPO / ".claude" / "hooks" / "codex_round_guard.py"

passed = failed = 0


def run(event: dict, *, allow: bool = False, session: str | None = None) -> dict:
    env = dict(os.environ)
    env["TMPDIR"] = TMP
    if allow:
        env["FM_ALLOW_CODEX_ROUND"] = "1"
    else:
        env.pop("FM_ALLOW_CODEX_ROUND", None)
    event = {"hook_event_name": "PreToolUse", **event,
             "session_id": session or f"test-{uuid.uuid4()}"}
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
    """'deny' | 'note' | 'silent' — the only three outcomes that matter."""
    h = out.get("hookSpecificOutput") or {}
    if h.get("permissionDecision") == "deny":
        return "deny"
    if h.get("additionalContext"):
        return "note"
    return "silent"


def check(name: str, actual: str, expected: str) -> None:
    global passed, failed
    if actual == expected:
        passed += 1
        print(f"  PASS {name}")
    else:
        failed += 1
        print(f"  FAIL {name}   [{actual}, wanted {expected}]")


TMP = tempfile.mkdtemp(prefix="codex-round-guard-test-")


def mcp(pr: int, body: str, tool: str = "mcp__github__add_issue_comment") -> dict:
    return {"tool_name": tool,
            "tool_input": {"owner": "menno420", "repo": "fleet-manager",
                           "issue_number": pr, "body": body}}


def bash(cmd: str) -> dict:
    return {"tool_name": "Bash", "tool_input": {"command": cmd}}


print("silence — the traffic the guard sits in")
check("ordinary command", decision(run(bash("git status --short"))), "silent")
check("grep for the phrase is reading, not requesting",
      decision(run(bash("grep -rn '@codex review' docs/ | head"))), "silent")
check("commit message mentioning the phrase",
      decision(run(bash('git commit -m "Ask @codex review on the flip head"'))), "silent")
check("doc written via quoted heredoc that quotes a curl POST of the phrase",
      decision(run(bash("cat >> docs/x.md <<'EOF'\ncurl -X POST $API/issues/12/comments "
                        "-d '{\"body\":\"@codex review\"}'\nEOF"))), "silent")
check("GET of the comments endpoint mentioning the phrase in a comment",
      decision(run(bash("curl -sS $API/issues/12/comments  # looking for '@codex review'"))),
      "silent")
check("POST to a comments endpoint WITHOUT the phrase",
      decision(run(bash("curl -X POST $API/issues/12/comments -d '{\"body\":\"landed\"}'"))),
      "silent")
check("MCP comment without the phrase", decision(run(mcp(1010, "Fixed in 76834c8."))), "silent")
check("MCP '@codex address that feedback' is a different command",
      decision(run(mcp(1010, "@codex address that feedback"))), "silent")
check("a non-comment MCP tool carrying the phrase",
      decision(run({"tool_name": "mcp__github__pull_request_read",
                    "tool_input": {"pullNumber": 1010, "method": "get_comments",
                                   "body": "@codex review"}})), "silent")
check("Edit tool writing the phrase into a doc",
      decision(run({"tool_name": "Edit",
                    "tool_input": {"file_path": "docs/x.md",
                                   "new_string": "post `@codex review`"}})), "silent")
check("non-PreToolUse event", decision(run({"hook_event_name": "PostToolUse",
                                            **mcp(1010, "@codex review")})), "silent")
check("garbage input", decision(run({"tool_name": "Bash", "tool_input": "not a dict"})),
      "silent")

print("the fm #1010 sequence — three counted, the fourth denied")
s = f"seq-{uuid.uuid4()}"
r1 = run(mcp(1010, "@codex review\n\nFlip-readiness request."), session=s)
check("round 1 allowed and counted", decision(r1), "note")
check("round 1 says 1 of 3",
      "1 of 3" in (r1.get("hookSpecificOutput") or {}).get("additionalContext", ""),
      True)
check("retry of the SAME body is not a new round",
      decision(run(mcp(1010, "@codex review\n\nFlip-readiness request."), session=s)), "silent")
r2 = run(mcp(1010, "@codex review\n\nRe-request on 76834c8."), session=s)
check("round 2 allowed", decision(r2), "note")
r3 = run(mcp(1010, "@codex review\n\nRe-request on d49d437."), session=s)
check("round 3 allowed and marked as the last", decision(r3), "note")
check("round 3 warns it is the last",
      "LAST" in (r3.get("hookSpecificOutput") or {}).get("additionalContext", ""), True)
r4 = run(mcp(1010, "@codex review\n\nRe-request on 1965aa9."), session=s)
check("round 4 DENIED", decision(r4), "deny")
check("denial names the cap and the exit",
      all(w in (r4.get("hookSpecificOutput") or {}).get("permissionDecisionReason", "")
          for w in ("cap is 3", "Gemini", "hand off", "FM_ALLOW_CODEX_ROUND")), True)
check("round 4 via the Bash route is denied the same",
      decision(run(bash("curl -X POST $API/repos/menno420/fleet-manager/issues/1010/comments "
                        "-d '{\"body\":\"@codex review on 1965aa9\"}'"), session=s)), "deny")
check("round 4 via pull_request_review_write is denied the same",
      decision(run(mcp(1010, "@codex security review",
                       tool="mcp__github__pull_request_review_write"), session=s)), "deny")
check("a DIFFERENT PR in the same session starts its own count",
      decision(run(mcp(1011, "@codex review"), session=s)), "note")
check("a different session starts at zero",
      decision(run(mcp(1010, "@codex review\n\nRe-request on 1965aa9."))), "note")
r5 = run(mcp(1010, "@codex review\n\nOwner asked for one more."), session=s, allow=True)
check("override allows the fourth and says so", decision(r5), "note")
check("override note names the override",
      "FM_ALLOW_CODEX_ROUND" in (r5.get("hookSpecificOutput") or {}).get("additionalContext", ""),
      True)

print("the Bash leg — counts only a visible POST of the phrase")
s2 = f"bash-{uuid.uuid4()}"
check("curl -X POST to issues/N/comments with the phrase counts",
      decision(run(bash("curl -sS -X POST $API/repos/o/r/issues/77/comments "
                        "-d '{\"body\":\"@codex review please\"}'"), session=s2)), "note")
check("python requests.post through an executed heredoc counts",
      decision(run(bash("python3 - <<'EOF'\nimport requests\nrequests.post(f'{API}/issues/77/"
                        "comments', json={'body': '@codex review'})\nEOF"), session=s2)), "note")
check("curl --data to pulls/N/reviews with the phrase counts",
      decision(run(bash("curl --request POST $API/repos/o/r/pulls/77/reviews "
                        "--data '{\"body\":\"@codex review\",\"event\":\"COMMENT\"}'"),
                   session=s2)), "note")
check("the fourth Bash-leg request on the same PR is denied",
      decision(run(bash("curl -X POST $API/repos/o/r/issues/77/comments "
                        "-d '{\"body\":\"@codex review again\"}'"), session=s2)), "deny")

print()
print(f"{passed} passed, {failed} failed")
sys.exit(1 if failed else 0)
