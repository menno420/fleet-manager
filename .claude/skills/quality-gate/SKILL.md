---
name: quality-gate
description: "Run the project's full verification before pushing and report what must be fixed."
---

# quality-gate

Prove a change is good before pushing fleet-manager.

1. Run `python3 bootstrap.py check --strict` — doc + session-log hygiene, real exit code.
2. Run `python3 tools/check_no_false_walls.py --strict` — the false-wall guard, to read its
   findings in isolation. (Coverage note, corrected 2026-08-11: this checker ALSO runs inside
   step 1's `scripts/preflight.py` fan-out and in CI's required `substrate-gate` — a finding
   here blocks the merge; this step is a closer look, not the only enforcement.)
3. Report every failure with the exact command to reproduce it.
4. Do NOT push on red — green here should mean green in CI.

Declared capabilities: run.
