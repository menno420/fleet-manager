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
MATCHER = "Bash|WebFetch|Read|Glob|Grep|Edit|Write|MultiEdit"

# Every hook this repo installs, and the events each one serves. Keyed by script
# name because that is how an existing registration is recognised — see merge_event.
HOOKS = {
    # doc routing: probe-time on tool input, and prompt-time so naming a repo
    # pulls its Layer 2 README before the work starts.
    "route_docs.py": (("PreToolUse", MATCHER), ("UserPromptSubmit", None)),
    # read-before-write: records reads and flags prose about unopened files,
    # plus the closed-vocabulary fields (Status badges, Model-line task class).
    # One event; the same matcher covers both halves (read tools record,
    # Edit/Write check).
    "read_before_write.py": (("PreToolUse", MATCHER),),
    # git-state guard: squash-stacked branch, force-push tree comparison, and
    # reset --hard over a dirty tree — the facts the 2026-08-08 git failures
    # were missing at the moment of the command.
    "git_state_guard.py": (("PreToolUse", MATCHER),),
    # trigger-tools guard: the ONLY denying hook, and the one whose absence is
    # silently expensive. A multi-root session that loses this can call
    # `delete_trigger`, raise an approval prompt on the owner's screen, and stall
    # until he is physically back — the exact failure the guard exists to stop,
    # in the exact environment where nobody is watching. Its own matcher, because
    # MATCHER covers only the built-in tools and this must also see the MCP
    # trigger tools by name. Codex, fm #834 (P1) — this table was written without
    # it, which left the rescue path rescuing three hooks out of four.
    "trigger_tools_guard.py": (
        ("PreToolUse", "Bash|mcp__.*__delete_trigger|mcp__.*__send_later"),
    ),
    # change guard: kit-named skill amendments, broken tables, un-propagated
    # edits — before the write AND after it lands (propagation is only knowable
    # post-edit). Absent from this table until 2026-08-11 (the full-read
    # audit's D28): the same three-of-four class fm #834 fixed, recurring — the
    # rescue path silently restored 4 of 6 hooks and printed a clean install.
    "change_guard.py": (
        ("PreToolUse", "Write|Edit|MultiEdit"),
        ("PostToolUse", "Edit|MultiEdit"),
    ),
    # owner-review Stop hook: reviews the reply the owner reads, blocks once.
    # Also absent until 2026-08-11 — losing it silently removes the estate's
    # CLAIM-layer instrument. Stop has no tool to match on.
    "owner_review.py": (("Stop", None),),
    # session-start orientation: the six mandatory reads, delivered at the one
    # moment the cold-orientation contract applies. No matcher — SessionStart
    # matchers filter on `source` values, and this hook branches on source
    # itself so that a value nobody anticipated still gets the cold block
    # rather than silence.
    #
    # Worth stating plainly, because it is the one hook in this table whose
    # rescue case is self-defeating: when root has moved, THIS hook did not fire
    # either, so the session that most needs the orientation is the one that
    # never got it. Installing it here does not fix that boot — nothing can,
    # from inside a session that already started. It fixes every session after
    # the operator runs --apply, which is the same bargain every other row makes.
    "session_start.py": (("SessionStart", None),),
}

# Per-hook timeout for NEW registrations (seconds; merge_event leaves existing
# entries' timeouts alone). owner_review calls a model and the repo-local
# registration gives it 120s — installing it with the 10s default would kill
# the review mid-flight while still reporting "installed".
TIMEOUTS = {"owner_review.py": 120}
DEFAULT_TIMEOUT = 10


def command_for(root: Path, script: str) -> str:
    """Portable inside the repo, absolute outside it — and never fatal."""
    if root == REPO:
        base = ('"${CLAUDE_PROJECT_DIR:-$(git rev-parse --show-toplevel)}"'
                f"/.claude/hooks/{script}")
    else:
        base = f'"{REPO / ".claude/hooks" / script}"'
    return f"[ -f {base} ] && python3 {base} || true"


def merge_event(settings: dict, command: str, event: str, matcher: str | None,
                script: str) -> bool:
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
            if script not in h.get("command", ""):
                continue
            if h.get("command") == command and entry.get("matcher") == matcher:
                return False
            h["command"] = command
            if matcher is None:
                entry.pop("matcher", None)
            else:
                entry["matcher"] = matcher
            return True
    timeout = TIMEOUTS.get(script, DEFAULT_TIMEOUT)
    entry = {"hooks": [{"type": "command", "command": command,
                        "timeout": timeout}]}
    if matcher is not None:
        entry["matcher"] = matcher
    entries.append(entry)
    return True


def merge(settings: dict, root: Path) -> tuple[dict, bool]:
    """Register every hook on every event it serves.

    Driven by the HOOKS table rather than hardcoded, because the rescue path is
    exactly where a half-installed apparatus is invisible: a session that runs
    this after landing on the wrong root has no other signal that a hook is
    missing. Adding a hook above is the whole change.
    """
    changed = False
    for script, events in HOOKS.items():
        if not (REPO / ".claude/hooks" / script).is_file():
            print(f"WARN   skipping {script} — not present in this repo")
            continue
        command = command_for(root, script)
        for event, matcher in events:
            changed |= merge_event(settings, command, event, matcher, script)
    return settings, changed


def main() -> int:
    apply = "--apply" in sys.argv
    root = Path(os.environ.get("CLAUDE_PROJECT_DIR") or Path.cwd()).resolve()
    target = root / ".claude/settings.json"

    print(f"session root : {root}")
    print(f"is this repo : {'yes' if root == REPO else 'NO — root moved above the repo'}")
    print(f"target       : {target}")

    present = [s for s in HOOKS if (REPO / ".claude/hooks" / s).is_file()]
    if not present:
        print(f"ERROR  no hook scripts found under {REPO / '.claude/hooks'}")
        return 1
    print(f"hooks        : {', '.join(present)}")

    settings: dict = {}
    if target.is_file():
        try:
            settings = json.loads(target.read_text())
        except Exception as exc:
            print(f"ERROR  {target} does not parse — refusing to overwrite: {exc}")
            return 1

    settings, changed = merge(settings, root)
    if not changed:
        print("\nalready installed — nothing to do")
        return 0

    if not apply:
        print("\nwould write (re-run with --apply):\n")
        hooks = settings.get("hooks", {})
        events = sorted({e for evs in HOOKS.values() for e, _ in evs})
        print(json.dumps({e: hooks.get(e, []) for e in events}, indent=2))
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
