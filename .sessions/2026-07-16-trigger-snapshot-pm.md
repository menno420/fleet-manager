# 2026-07-16 — trigger-snapshot-pm (R26 snapshot refresh wake)

> **Status:** `in-progress`

Intent: refresh `telemetry/triggers-snapshot.json` from a fresh full
`list_triggers` export to clear the stale I6 SNAPSHOT-FRESH FAIL (snapshot
was ~8h stale at the 06:47Z capture), re-run `check_trigger_health.py`,
verify the ~15:05Z FM failsafe cutover appears in the export (old
`trig_01UNjDKaaiGuUTvyfQGLKLrn` gone / replacement
`trig_01An9YmU3KC1kLhB5c9cv4Ax` present), and record the verdicts on the
heartbeat. Oversight only — no trigger created/modified/fired/deleted; no
sibling ids touched.
