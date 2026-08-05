#!/usr/bin/env python3
"""PreToolUse hook: surface the estate's own doc before a session probes blind.

The failure this exists to stop, measured 2026-08-05: a session wanted a
multi-turn Gemini conversation, fetched the `generativelanguage` discovery
document, found no `interactions` endpoint, and wrote "unavailable" into the
capability ledger — while `docs/providers/gemini.md:151` carried the working
recipe the whole time. Prose did not prevent it; the same session had authored
the rule it broke, three hours earlier.

So this is a mechanism, not another rule. When a tool call mentions something
the estate has already written down, the hook injects the doc path and one
sentence of what it says.

Design constraints, in priority order:

1. **Never block.** Advisory only, exit 0 on every path including a crash. A
   hook that can stop work will eventually stop the wrong work.
2. **Silence is the default.** It fires only when a route matches AND the doc
   exists AND that route has not already fired this session. An agent tries to
   satisfy whatever appears in its feedback channel, so a channel that is
   usually empty is the only kind worth writing to.
3. **No repo writes.** Session state lives in /tmp, keyed by session id, so
   running the hook never dirties the tree the session is trying to keep clean.

Wired by tools/install_root_hooks.py, which installs into whichever directory
is actually the session root — see .claude/hooks/README.md for why that is not
always this repo.
"""

from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
ROUTES = Path(__file__).resolve().parent / "doc-routes.json"
STATE_DIR = Path(os.environ.get("TMPDIR", "/tmp")) / "claude-doc-routes"

# Where each tool hides the text worth matching against. Anything not listed
# falls back to a bounded JSON dump of the whole input.
FIELDS = {
    "Bash": ("command",),
    "WebFetch": ("url", "prompt"),
    "Read": ("file_path",),
    "Glob": ("pattern", "path"),
    "Grep": ("pattern", "path", "glob"),
    # Write/Edit match on what is being WRITTEN, not on the path — the route
    # that matters here is "you are recording a wall", and that lives in the
    # prose. Kept off the default tool set below so a doc edit that merely
    # quotes a hostname does not trip every probe route.
    "Write": ("file_path", "content"),
    "Edit": ("file_path", "new_string"),
}

# A route with no `tools` key is a probe route: it fires when a session is
# about to go ask a vendor something. Content routes opt in explicitly.
DEFAULT_TOOLS = ("Bash", "WebFetch", "Read", "Glob", "Grep")


def haystack(tool: str, payload: dict) -> str:
    keys = FIELDS.get(tool)
    if keys:
        return "\n".join(str(payload.get(k, "")) for k in keys)
    return json.dumps(payload)[:4000]


def already_fired(session: str) -> set[str]:
    try:
        return set(json.loads((STATE_DIR / f"{session}.json").read_text()))
    except Exception:
        return set()


def remember(session: str, fired: set[str]) -> None:
    try:
        STATE_DIR.mkdir(parents=True, exist_ok=True)
        (STATE_DIR / f"{session}.json").write_text(json.dumps(sorted(fired)))
    except Exception:
        pass  # advisory state; losing it costs one duplicate line


def main() -> int:
    try:
        event = json.loads(sys.stdin.read() or "{}")
    except Exception:
        return 0

    tool = event.get("tool_name", "")
    text = haystack(tool, event.get("tool_input") or {})
    if not text.strip():
        return 0

    try:
        routes = json.loads(ROUTES.read_text())["routes"]
    except Exception:
        return 0

    session = str(event.get("session_id") or "nosession")
    fired = already_fired(session)
    hits = []

    for route in routes:
        rid = route.get("id", "")
        if rid in fired:
            continue
        if tool not in tuple(route.get("tools") or DEFAULT_TOOLS):
            continue
        docs = [d for d in route.get("docs", []) if (REPO / d).is_file()]
        if not docs:
            continue
        # Already opening one of these docs? Then the hook has nothing to add.
        # Probe routes only: a content route fires ON the edit to its own doc,
        # which is the entire point of the wall-recording route below.
        if not route.get("tools") and any(d in text for d in docs):
            fired.add(rid)
            continue
        try:
            if not any(re.search(p, text, re.I) for p in route.get("when", [])):
                continue
        except re.error:
            continue  # a bad pattern silences its own route, never the hook
        fired.add(rid)
        hits.append((docs, route.get("says", "")))

    if not hits:
        return 0
    remember(session, fired)

    lines = [
        "This estate has already written down how this works. Read the "
        "doc before deriving the behaviour from a probe — a probe that fails "
        "tells you about one call, not about what is possible."
    ]
    for docs, says in hits:
        lines.append("")
        lines.append("· " + " + ".join(f"`{d}`" for d in docs))
        if says:
            lines.append("  " + says)

    json.dump(
        {
            "hookSpecificOutput": {
                "hookEventName": "PreToolUse",
                "additionalContext": "\n".join(lines),
            },
            "suppressOutput": True,
        },
        sys.stdout,
    )
    return 0


if __name__ == "__main__":
    try:
        sys.exit(main())
    except Exception:
        sys.exit(0)  # fail open, always
