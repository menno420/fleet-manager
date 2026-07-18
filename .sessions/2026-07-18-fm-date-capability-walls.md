# 2026-07-18 · date the undated capability walls (clear S9 advisory)

> **Status:** `in-progress`

About to happen: add evidence-based ledger-recorded dates to the 5 `docs/CAPABILITIES.md`
WALL entries that `scripts/check_capabilities_wall_age.py` (S9) reports as `[undated-wall]`
notes — an undated wall carries no freshness data, so it can never be aged for re-probe and
silently hardens into assumed-permanent. Dates are sourced from `git blame` (the commit that
recorded each finding), not invented, so each wall becomes an age-trackable re-probe candidate.

- **📊 Model:** opus-4.8 · high · docs-only
