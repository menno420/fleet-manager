---
name: quality-gate
description: "Run the project's full verification before pushing and report what must be fixed."
---

# quality-gate

Prove a change is good before pushing fleet-manager.

1. Run `python3 bootstrap.py check --strict` — doc + session-log hygiene, real exit code.
2. Run `python3 tools/check_no_false_walls.py --strict` — the false-wall guard (nothing in CI runs it for you).
3. Report every failure with the exact command to reproduce it.
4. Do NOT push on red — green here should mean green in CI.

Declared capabilities: run.
