# 2026-07-13 — Trigger-health I1 absent-enabled fix (coordinator-dispatched worker)

> **Status:** `in-progress`

Intent: Slice A — close the `check_trigger_health.py` I1 absent-`enabled` blind spot (records with the `enabled` key ABSENT are skipped by I1 entirely; observed live: `trig_011XAWqPeksS8LBrS5G9RvVc`, next_run frozen 2026-07-02T03:07Z) by surfacing them as a distinct report class matching the checker's grammar, WARN on ambiguous+frozen, with before/after runs against the committed snapshot @ `f09ba87`. Slice B — record the Q-0264 relay consumption sweep (baton item 1 follow-up).

📊 Model: Fable 5

## Work record

- **Slice A shipped:** `scripts/check_trigger_health.py` gains **I1b
  AMBIGUOUS-ENABLED** — records with the `enabled` key ABSENT (not False) were
  skipped by every invariant; I1b splits them into explained remnants (carry an
  `ended_reason`; counted, not listed — 1199 in the committed snapshot) vs
  AMBIGUOUS (no `ended_reason`; listed, liveness never guessed), and an
  ambiguous standing cron with `next_run_at` frozen > grace in the past is a
  **WARN** (truthy status — never affects the exit code; remnants are expected
  history). Before: 7/7 PASS, `trig_011XAWqPeksS8LBrS5G9RvVc` (next_run frozen
  2026-07-02T03:07Z) invisible. After: 7/8 green + 1 WARN, exit 0, the frozen
  dispatch cron listed with the live-verify remedy; second ambiguous record
  surfaced too (`trig_01MWHvQFnRF1dVdZFSP6SM5L`, sentinel next_run, no frozen
  signal). Test pattern: the script's own `--selfcheck` (the PR #133 harness) —
  7 new assertions, PASS. Verifies: roster-freshness OK · owner-queue CLEAN ·
  `bootstrap.py check --strict` red ONLY on this card's designed born-red hold.
