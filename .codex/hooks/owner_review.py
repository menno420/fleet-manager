#!/usr/bin/env python3
"""Codex Stop adapter for Fleet Manager's fixed owner-review questions.

Codex gives Stop hooks the final reply as ``last_assistant_message``. Claude's
hook instead parses a Claude-specific transcript and optionally calls Gemini.
This adapter uses the native Codex field and imports only the literal FIXED and
REASON strings from the canonical Claude source. No model, network or credential
path is part of the Codex mechanism.

Contract: block once for a claim-bearing reply, fail open on every defect, and
write telemetry only to the operating system's temporary directory.
"""

from __future__ import annotations

import ast
import json
import tempfile
import time
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CLAUDE_HOOK = REPO / ".claude" / "hooks" / "owner_review.py"
LOG = Path(tempfile.gettempdir()) / "codex-owner-review" / "log.jsonl"
MIN_CHARS = 400


def _canonical_copy() -> tuple[str, str]:
    """Read FIXED and REASON without importing or executing the Claude hook."""
    tree = ast.parse(CLAUDE_HOOK.read_text(encoding="utf-8"))
    found: dict[str, str] = {}
    for node in tree.body:
        if not isinstance(node, ast.Assign):
            continue
        for target in node.targets:
            if isinstance(target, ast.Name) and target.id in {"FIXED", "REASON"}:
                value = ast.literal_eval(node.value)
                if isinstance(value, str):
                    found[target.id] = value
    return found["FIXED"], found["REASON"]


def _log(data: dict, **fields: object) -> None:
    try:
        LOG.parent.mkdir(parents=True, exist_ok=True)
        record = {
            "ts": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "session": data.get("session_id"),
            **fields,
        }
        with LOG.open("a", encoding="utf-8") as handle:
            handle.write(json.dumps(record) + "\n")
    except Exception:
        pass


def main() -> int:
    try:
        data = json.loads(__import__("sys").stdin.read() or "{}")
    except Exception:
        return 0

    if data.get("stop_hook_active"):
        return 0

    text = data.get("last_assistant_message")
    if not isinstance(text, str):
        _log(data, skip="no-last-assistant-message")
        return 0
    if len(text) < MIN_CHARS:
        _log(data, skip="reply-too-short", reply_chars=len(text))
        return 0

    try:
        fixed, reason = _canonical_copy()
    except Exception as exc:
        _log(data, skip="canonical-copy-unavailable", error=type(exc).__name__)
        return 0

    _log(data, reply_chars=len(text), blocked=True, enriched=False)
    print(json.dumps({"decision": "block", "reason": reason.format(q=fixed)}))
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except (KeyboardInterrupt, SystemExit):
        raise
    except BaseException:
        # A defective Stop hook must never trap a turn.
        raise SystemExit(0)
