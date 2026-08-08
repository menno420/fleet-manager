#!/usr/bin/env python3
"""Install this repo's hooks into whichever directory is actually the session root.

Claude Code loads `<root>/.claude/settings.json`, where root is the session's
working directory — and root is not always a repo. Measured 2026-08-05 in this
container:

  · single-source session  → root = /home/user/fleet-manager   (the repo)
  · multi-repo session     → root = /home/user                 (owner-observed)

`/home/user` holds all four clones, is not a git repo, and has no `.claude/`.
So in a multi-repo session every repo's `.claude/` goes quiet at once —
settings, hooks, skills and the auto-loaded CLAUDE.md — with no error anywhere.
superbot's seven hooks, including its hard-fail Stop gate, disappear exactly
that way.

This script writes the hook registration to the root that is live right now,
merging into any existing settings rather than replacing them. Run it once per
session when root is not a repo; it is idempotent, so running it again is free.

    python3 tools/install_root_hooks.py            # show what would change
    python3 tools/install_root_hooks.py --apply    # write it

The repo-local `.claude/settings.json` already carries the same registration
for the ordinary single-source case, so this is only needed when root moved.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
HOOK = REPO / ".claude/hooks/route_docs.py"
MATCHER = "Bash|WebFetch|Read|Glob|Grep|Edit|Write"


def command_for(root: Path) -> str:
    """Portable inside the repo, absolute outside it — and never fatal."""
    if root == REPO:
        base = '"${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel)}"/.claude/hooks/route_docs.py'
    else:
        base = f'"{HOOK}"'
    return f"[ -f {base} ] && python3 {base} || true"


def merge_event(settings: dict, command: str, event: str, matcher: str | None) -> bool:
    """Register the hook on one event. Returns True if anything changed.

    Find our own registration by the script it runs, not by the matcher.
    Keying on the matcher would append a duplicate every time the matcher
    changes — which it does whenever a new tool becomes routable.

    `matcher=None` is the no-matcher form (UserPromptSubmit has no tool to
    match on), and an existing entry's stale matcher is cleared rather than
    left behind.
    """
    entries = settings.setdefault("hooks", {}).setdefault(event, [])
    for entry in entries:
        for h in entry.get("hooks") or []:
            if "route_docs.py" not in h.get("command", ""):
                continue
            if h.get("command") == command and entry.get("matcher") == matcher:
                return False
            h["command"] = command
            if matcher is None:
                entry.pop("matcher", None)
            else:
                entry["matcher"] = matcher
            return True
    entry = {"hooks": [{"type": "command", "command": command, "timeout": 10}]}
    if matcher is not None:
        entry["matcher"] = matcher
    entries.append(entry)
    return True


def merge(settings: dict, command: str) -> tuple[dict, bool]:
    """Register on both events the hook serves.

    UserPromptSubmit is what makes naming a repo pull its Layer 2 README in
    before the session starts working (route_docs.py docstring). Installing
    only PreToolUse here would leave the rescue path — the case-three
    `--apply` run — silently carrying half the retrieval.
    """
    changed = merge_event(settings, command, "PreToolUse", MATCHER)
    changed |= merge_event(settings, command, "UserPromptSubmit", None)
    return settings, changed


def main() -> int:
    apply = "--apply" in sys.argv
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path.cwd()).resolve()
    target = root / ".claude/settings.json"

    print(f"session root : {root}")
    print(f"is this repo : {'yes' if root == REPO else 'NO — root moved above the repo'}")
    print(f"target       : {target}")

    if not HOOK.is_file():
        print(f"ERROR  hook script missing: {HOOK}")
        return 1

    settings: dict = {}
    if target.is_file():
        try:
            settings = json.loads(target.read_text())
        except Exception as exc:
            print(f"ERROR  {target} does not parse — refusing to overwrite: {exc}")
            return 1

    settings, changed = merge(settings, command_for(root))
    if not changed:
        print("\nalready installed — nothing to do")
        return 0

    if not apply:
        print("\nwould write (re-run with --apply):\n")
        hooks = settings.get("hooks", {})
        print(json.dumps({e: hooks.get(e, []) for e in ("PreToolUse", "UserPromptSubmit")}, indent=2))
        return 0

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps(settings, indent=2) + "\n")
    print(f"\ninstalled into {target}")
    if root != REPO:
        print(
            "NOTE  this root is outside any repo, so the file is not version "
            "controlled and dies with the container. Re-run once per session."
        )
    return 0


if __name__ == "__main__":
    sys.exit(main())
