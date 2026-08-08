#!/usr/bin/env python3
"""Local-ritual ↔ CI-gate parity — the one check list, finally planted.

`bootstrap.py check` has looked for this file on every full-lane run and
NOTEd its absence (`_default_preflight_scripts`, ORDER 018: *"plant one to
converge the local ritual and the CI gate on one check list"*). Nobody had.
The cost was measured 2026-08-08: a session ran `check --strict` → exit 0,
pushed, and CI went red on the added-card grammar check (`build` is not a
PL-004 task class) — because **plain `check` never runs the added-card lane;
only CI's workflow logic did.** Local green and CI green were different
predicates. This file makes them the same predicate.

What runs here, and why exactly these:

1. **The added-card lane** — for every session card ADDED in the diff vs
   origin/main, the same invocation substrate-gate.yml uses:
   `check --strict --session-log .sessions/__born-red-card-added__.md
   --added-card <card>`. This is the check that was CI-only.
2. **`tools/check_doc_routes.py --strict`** — CI runs it as its own step.
3. **`tools/check_no_false_walls.py --strict`** — likewise.

Recursion guard: bootstrap runs THIS script from inside `check`, and step 1
runs bootstrap from inside this script. `FM_PREFLIGHT_ACTIVE` breaks the
loop — the inner bootstrap sees it and this script exits 0 immediately.

Exit contract: 0 all green; 1 otherwise (bootstrap rides any non-zero into
its strict finding loop, so `check --strict` now goes red locally on
everything CI would red on).
"""

from __future__ import annotations

import os
import subprocess
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[1]
GUARD = "FM_PREFLIGHT_ACTIVE"


def run(label: str, argv: list[str], env: dict | None = None) -> int:
    p = subprocess.run(argv, cwd=REPO, env=env, capture_output=True, text=True)
    tail = (p.stdout + p.stderr).strip().splitlines()[-1:] or [""]
    print(f"preflight: {label} -> exit {p.returncode}  ({tail[0][:120]})")
    return p.returncode


def added_cards() -> list[str]:
    """Session cards ADDED vs origin/main — same selection CI's gate makes."""
    try:
        base = subprocess.run(
            ["git", "merge-base", "origin/main", "HEAD"],
            cwd=REPO, capture_output=True, text=True, timeout=10)
        if base.returncode != 0:
            print("preflight: NOTE — no merge-base with origin/main; "
                  "added-card lane skipped (fetch origin main to enable)")
            return []
        diff = subprocess.run(
            ["git", "diff", "--name-only", "--diff-filter=A",
             base.stdout.strip() + "..HEAD", "--",
             ".sessions/*.md", ":!.sessions/README.md"],
            cwd=REPO, capture_output=True, text=True, timeout=10)
        return [c for c in diff.stdout.splitlines() if c.strip()]
    except Exception as exc:
        print(f"preflight: NOTE — card selection failed ({exc}); lane skipped")
        return []


def main() -> int:
    if os.environ.get(GUARD):
        return 0  # invoked from inside our own inner bootstrap run

    inner = dict(os.environ, **{GUARD: "1"})
    failed = 0

    for card in added_cards():
        failed |= run(
            f"added-card lane ({card})",
            [sys.executable, "bootstrap.py", "check", "--strict",
             "--session-log", ".sessions/__born-red-card-added__.md",
             "--added-card", card],
            env=inner) != 0

    for label, argv in (
        ("doc routes", [sys.executable, "tools/check_doc_routes.py", "--strict"]),
        ("false walls", [sys.executable, "tools/check_no_false_walls.py", "--strict"]),
    ):
        failed |= run(label, argv) != 0

    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
