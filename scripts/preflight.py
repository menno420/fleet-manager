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
4. **`tools/check_pipe_exit_code.py --strict`** — TRAP-002's deterministic half:
   an exit code read after a pipe, in executable surfaces only (workflows, shell
   scripts). Prose is not scanned; the doc-route covers command-authoring time.

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
    lines = (p.stdout + p.stderr).strip().splitlines()
    # Prefer the line that states the verdict over the literal last line: a
    # failing `check` ends on the guard-fires telemetry note, so the tail
    # describes bookkeeping while the finding sits above it.
    tail = next((l for l in reversed(lines) if "finding(s)" in l), lines[-1] if lines else "")
    print(f"preflight: {label} -> exit {p.returncode}  ({tail.strip()[:120]})")
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
    failing: list[str] = []

    for card in added_cards():
        rc = run(
            f"added-card lane ({card})",
            [sys.executable, "bootstrap.py", "check", "--strict",
             "--session-log", ".sessions/__born-red-card-added__.md",
             "--added-card", card],
            env=inner)
        if rc != 0:
            failing.append(f"added-card lane ({card}) — born-red HOLD if the "
                           "card is still in-progress; a real finding otherwise")
        failed |= rc != 0

    for label, argv in (
        ("doc routes", [sys.executable, "tools/check_doc_routes.py", "--strict"]),
        ("false walls", [sys.executable, "tools/check_no_false_walls.py", "--strict"]),
        ("pipe exit code", [sys.executable, "tools/check_pipe_exit_code.py", "--strict"]),
    ):
        rc = run(label, argv)
        if rc != 0:
            failing.append(label)
        failed |= rc != 0

    # The LAST line must name the cause: bootstrap surfaces only this line in
    # its `[preflight-script]` finding, and on 2026-08-08 that made a born-red
    # hold read as a failure of `false walls`, the leg that had just passed.
    # An instrument that attributes a red to the wrong leg is worse than none.
    if failing:
        print("preflight: FAILED — " + " · ".join(failing))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
