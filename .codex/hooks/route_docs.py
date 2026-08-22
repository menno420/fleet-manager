#!/usr/bin/env python3
"""Codex UserPromptSubmit adapter for the canonical Claude document router.

The event's useful fields are compatible, so run the existing matcher and
normalize only the host-specific response. This keeps one route table and one
matching implementation. It also replaces the legacy ``/tmp`` fallback with
the actual operating-system temporary directory on Windows.
"""

from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CLAUDE_HOOK = REPO / ".claude" / "hooks" / "route_docs.py"
EVENT = "UserPromptSubmit"


def main() -> int:
    raw = sys.stdin.read()
    try:
        event = json.loads(raw or "{}")
    except Exception:
        return 0
    if event.get("hook_event_name") != EVENT:
        return 0
    if not CLAUDE_HOOK.is_file():
        return 0

    env = dict(os.environ)
    # tempfile observes TMPDIR/TEMP/TMP, so tests and managed environments can
    # still isolate state. The assigned value is always a directory that exists
    # on this host; unlike the canonical script's POSIX-only fallback.
    env["TMPDIR"] = tempfile.gettempdir()
    try:
        result = subprocess.run(
            [sys.executable, str(CLAUDE_HOOK)],
            input=raw,
            text=True,
            capture_output=True,
            cwd=REPO,
            env=env,
            timeout=8,
            check=False,
        )
    except Exception:
        return 0
    if result.returncode != 0 or not result.stdout.strip():
        return 0

    try:
        payload = json.loads(result.stdout)
        specific = payload.get("hookSpecificOutput")
        if not isinstance(specific, dict):
            return 0
        if specific.get("hookEventName") != EVENT:
            return 0
        # Parsed but unsupported by Codex today; leaving it in makes the hook
        # fail instead of injecting the route context.
        payload.pop("suppressOutput", None)
    except Exception:
        return 0

    json.dump(payload, sys.stdout)
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException:
        raise SystemExit(0)  # advisory and fail-open, including native defects
