# 2026-07-19 · fm roster-regen cron resilience (second cron line + hub-merge ask)

> **Status:** `in-progress`

About to happen (declared born-red): fix-slice for the roster-regen scheduler-drop
diagnosis (this hour, read-only pass by the coordinator seat). GitHub's best-effort
scheduler is dropping `roster-regen.yml`'s `40 */2 * * *` windows — run objects were
never created for 00:40Z three nights running, plus 02:40Z tonight; the workflow
itself is healthy (state active, 30/30 recent runs green, chronic +45–140m start
delay). Remedy in this PR: add a second cron line `40 1-23/2 * * *` (odd hours) for
net hourly coverage — regen exits clean when nothing changed, so extra fires cost
~30s each. This PR touches `.github/workflows/**`, so merge-on-green deliberately
skips it: it is opened READY with the blocker named and the merge is queued as
owner-queue item `OQ-FM-ROSTER-CRON-SECOND-LINE` (VENUE:hub). Also: annotate the
`OQ-FM-ROSTER-CRON-RELIABILITY` watch item (verdict reached) and refresh
`control/status.md`.

- **📊 Model:** fable-5 · high · ci+docs — fix slice (workflow cron line + owner-queue + heartbeat)
