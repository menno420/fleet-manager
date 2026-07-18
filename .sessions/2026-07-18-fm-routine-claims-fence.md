# 2026-07-18 · fm routine-claims fence (machine-readable heartbeat routine block)

> **Status:** `in-progress`

About to happen: implement the machine-readable routine-claims fence idea from the
PR #335 session card (`2026-07-18-fm-verify-routine-state.md` 💡): teach
`control/status.md` a small fenced `routine-claims` JSON block carrying the seat's
routine facts (armed failsafe id/cron/next-fire, deleted ids, pacemaker mode) so
`scripts/verify_routine_state.py` — and future tooling — reads a contract instead of
prose-grammar scraping; prose stays for humans, fence preferred, prose fallback kept.
Plus one drive-by fix-on-sight: the merged `2026-07-18-fm-wake-oversight.md` card's
`📊 Model:` line trips two advisory PL-004 warnings (effort `high effort`, class
`fleet-oversight wake`) — amend to taxonomy form.

- **📊 Model:** fable-5 · high · feature build
