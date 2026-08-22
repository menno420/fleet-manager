#!/usr/bin/env python3
"""Executable contract suite for Fleet Manager's Codex hook adapters."""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
import uuid
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
ROUTE = REPO / ".codex" / "hooks" / "route_docs.py"
OWNER = REPO / ".codex" / "hooks" / "owner_review.py"
CONFIG = REPO / ".codex" / "hooks.json"
failures: list[str] = []


def check(label: str, condition: bool, detail: str = "") -> None:
    mark = "PASS" if condition else "FAIL"
    print(f"{mark:4}  {label}" + (f" — {detail}" if detail else ""))
    if not condition:
        failures.append(label)


def invoke(script: Path, event: dict, env: dict | None = None) -> subprocess.CompletedProcess:
    return subprocess.run(
        [sys.executable, str(script)],
        input=json.dumps(event),
        text=True,
        capture_output=True,
        cwd=REPO,
        env=env,
        timeout=12,
        check=False,
    )


def decoded(result: subprocess.CompletedProcess) -> dict:
    try:
        return json.loads(result.stdout)
    except Exception:
        return {}


with tempfile.TemporaryDirectory(prefix="fm-codex-hooks-") as state:
    env = dict(os.environ, TMPDIR=state, TEMP=state, TMP=state)
    session = "route-" + uuid.uuid4().hex
    prompt = {
        "session_id": session,
        "hook_event_name": "UserPromptSubmit",
        "prompt": "This session is for spider-swing.",
        "cwd": str(REPO),
    }
    first = invoke(ROUTE, prompt, env)
    first_json = decoded(first)
    specific = first_json.get("hookSpecificOutput") or {}
    check("prompt route exits zero", first.returncode == 0)
    check("prompt route keeps stderr silent", not first.stderr.strip())
    check(
        "prompt route injects the Layer 2 entry point",
        "docs/repos/spider-swing/README.md" in specific.get("additionalContext", ""),
    )
    check("prompt route declares the Codex event", specific.get("hookEventName") == "UserPromptSubmit")
    check("unsupported suppressOutput is removed", "suppressOutput" not in first_json)

    second = invoke(ROUTE, prompt, env)
    check("prompt route fires once per session", not second.stdout.strip())

    wrong_event = invoke(ROUTE, {"hook_event_name": "PreToolUse", "prompt": "spider-swing"}, env)
    check("adapter is silent on unregistered events", not wrong_event.stdout.strip())

long_reply = (
    "The implementation is complete and verified from the repository root. "
    "The load-bearing conclusion is based on the executable contract suite and "
    "the exact Windows command path, both of which returned zero. " * 4
)
review = invoke(
    OWNER,
    {
        "session_id": "review-" + uuid.uuid4().hex,
        "hook_event_name": "Stop",
        "last_assistant_message": long_reply,
        "stop_hook_active": False,
    },
)
review_json = decoded(review)
check("owner review exits zero", review.returncode == 0)
check("owner review keeps stderr silent", not review.stderr.strip())
check("owner review blocks a claim-bearing reply", review_json.get("decision") == "block")
check("owner review reuses the canonical fixed question", "What made you draw that conclusion?" in review_json.get("reason", ""))
check("owner review has no model enrichment dependency", "And specifically:" not in review_json.get("reason", ""))

guarded = invoke(OWNER, {"stop_hook_active": True, "last_assistant_message": long_reply})
check("Stop loop guard is silent", not guarded.stdout.strip())
short = invoke(OWNER, {"stop_hook_active": False, "last_assistant_message": "Done."})
check("short replies stay silent", not short.stdout.strip())

malformed = subprocess.run(
    [sys.executable, str(OWNER)],
    input="not-json",
    text=True,
    capture_output=True,
    cwd=REPO,
    timeout=12,
    check=False,
)
check("malformed events fail open", malformed.returncode == 0 and not malformed.stdout.strip())

config = json.loads(CONFIG.read_text(encoding="utf-8"))
hooks = config.get("hooks") or {}
check("UserPromptSubmit is registered", len(hooks.get("UserPromptSubmit") or []) == 1)
check("Stop is registered", len(hooks.get("Stop") or []) == 1)
commands = [
    hook
    for event in ("UserPromptSubmit", "Stop")
    for group in hooks.get(event, [])
    for hook in group.get("hooks", [])
]
check("all registrations are command hooks", len(commands) == 2 and all(h.get("type") == "command" for h in commands))
check("all registrations include Windows commands", all(h.get("commandWindows") for h in commands))
check("registration contains no machine-specific repo path", all("C:\\\\dev" not in json.dumps(h) for h in commands))

windows_command = hooks["UserPromptSubmit"][0]["hooks"][0]["commandWindows"]
nested_event = {
    "session_id": "nested-" + uuid.uuid4().hex,
    "hook_event_name": "UserPromptSubmit",
    "prompt": "Please inspect spider-swing.",
}
nested = subprocess.run(
    ["powershell", "-NoProfile", "-Command", windows_command],
    input=json.dumps(nested_event),
    text=True,
    capture_output=True,
    cwd=REPO / "docs",
    timeout=15,
    check=False,
)
nested_json = decoded(nested)
nested_context = (nested_json.get("hookSpecificOutput") or {}).get("additionalContext", "")
check("exact Windows command resolves a nested worktree", nested.returncode == 0 and "spider-swing/README.md" in nested_context, nested.stderr.strip())

print()
if failures:
    print(f"Codex hooks: {len(failures)} failure(s): " + ", ".join(failures))
    raise SystemExit(1)
print("Codex hooks: all contracts passed")
