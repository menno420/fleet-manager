# 2026-07-12 — ORDER 020: per-wake trigger-health check

> **Status:** `in-progress`

📊 Model: fable-5 · start 2026-07-12 ·
lane worker (ORDER 020, dispatched by the coordinator)

## Declared at open (born-red)

Build the per-wake trigger-health check per ORDER 020 (canonical spec: superbot
`docs/owner/trigger-health-order-2026-07-12.md`): `scripts/check_trigger_health.py`
(WEDGED-cron / DROPPED-one-shot / DEAD-chain / manager-failsafe / roster+snapshot
freshness, PASS-FAIL per invariant, nonzero exit on FAIL), per-trigger health folded
into `scripts/gen_roster.py` so the roster (Actions substrate) carries the record,
wake-ritual wiring in `docs/playbook.md` + the fleet-manager v3 prompts, proof runs
against the current snapshot AND a replay of the 2026-07-12 incident snapshot, then
the ORDER 020 DONE flip in `control/inbox.md` — in progress.
