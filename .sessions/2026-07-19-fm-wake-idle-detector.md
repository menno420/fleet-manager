# 2026-07-19 · fm build slice — wake-without-work detector in `check_lane_liveness.py`

> **Status:** `in-progress`

About to happen (declared born-red): groom slice #2 (evening re-groom's ranked #2,
baton "Next slice" as of 20:2xZ) — extend `scripts/check_lane_liveness.py` with a
wake-without-work signal. For each lane whose failsafe shows ENABLED in the committed
`telemetry/triggers-snapshot.json`, compare the failsafe's `last_fired_at` against the
lane's newest observed liveness signal: a failsafe that has fired ≥2 windows (from the
cron cadence + last_fired) after the lane's last landed output is **WAKING-IDLE** —
wakes are burning tokens with zero output, a distinct and worse state than mere quiet —
vs **asleep** (failsafe armed on paper but not actually firing at capture). Existing
verdict ladder unchanged; this refines STALLED with the burn signal as a new column.
Honest capture-lag caveat printed (fires after `captured_at` are invisible). Ground
truth demo: the STALLED SBW constituent lanes. Also: selfcheck pins for the new pure
logic, Q-0105 note on the new block, `control/status.md` baton advance, claim
`control/claims/claude-fm-wake-idle-detector.md` (deleted in the flip commit).
No trigger-MCP calls from this venue; no sibling repo written.

- **📊 Model:** fable-5 · high · feature build — extend verified checker, tooling+docs (Q-0105 provenance tier)
