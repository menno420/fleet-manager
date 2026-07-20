# 2026-07-20 · fm build slice — liveness checker honors declared-idle heartbeats

> **Status:** `in-progress`

About to happen (declared born-red): teach `scripts/check_lane_liveness.py` to
honor a DECLARED idle. Ground truth motivating it (today): the Self Improvement
seat closed its wake chain deliberately at 07:53Z per its honesty guard — its
substrate-kit heartbeat's Baton reads "Agent-buildable kit slices are drained
through v1.20.1 + #555" (updated 07:45:00Z) — and the 15:52Z liveness run still
scored the lane STALLED, triggering the OQ-SI-CHAIN-DEAD escalation and a
manager nudge. An honest idle should read differently from a silent stall.
Plan: scan the heartbeat text the checker ALREADY fetches (same transport, zero
new reads; "not measured" walls unchanged) for an idle declaration
(case-insensitive: "backlog dry" / "honest idle" / "idle-declared" /
"standing down" / backlog-slices-queue…drained — grounded on the real
substrate-kit grammar above); a STALLED/QUIET lane WITH a fresh declaration
(dated by the declaring heartbeat's `updated:` stamp, within one cadence window
of the lane's newest signal) becomes verdict `IDLE-DECLARED` — exit-neutral,
`--strict` does not fail on it, headline lists it separately. Undated
declaration → `IDLE-DECLARED (undated …)` and the STALLED escalation hint
stays. Selfcheck extended; Q-0105 provenance note; ground-truth run quoted.
Then: OQ-SI-CHAIN-DEAD owner-queue update (SI responded to the 16:0xZ nudge —
halt was deliberate honest-idle; retire condition noted), one-line triage
addendum, `control/status.md` bump. Claim
`control/claims/claude-fm-declared-idle.md` (deleted in the flip commit).
Decide-and-flag rationale: S, pure-logic extension of a verified checker over
data it already reads; reversible. No trigger-MCP calls from this venue.

- **📊 Model:** fable-5 · high · feature build — extend verified checker (Q-0105 provenance tier)

*(payload, ground-truth run, and enders land before the flip)*
