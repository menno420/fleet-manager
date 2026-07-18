# 2026-07-18 · fm verify-routine-state (new tool: one-command routine-state proof)

> **Status:** `in-progress`

Build `scripts/verify_routine_state.py` — a stdlib one-command proof that the heartbeat's
claimed routine state (armed failsafe id/cron, deleted predecessors) matches a real
`list_triggers` export, born from today's hung-arm + 6.1h-stale-snapshot friction where
proving chain state took a 20-page hand pagination.
