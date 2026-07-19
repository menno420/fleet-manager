# 2026-07-19 · fm build slice — `scripts/check_lane_liveness.py` (seat-chain stall detector)

> **Status:** `in-progress`

About to happen (declared born-red): build slice #1 from
`docs/planning/2026-07-19-next-slices.md` — a new stdlib-only advisory checker
`scripts/check_lane_liveness.py` that measures each fleet lane's liveness signals
(newest main commit timestamp + heartbeat `updated:` stamp, read over the roster's
verified git transport) against the lane's failsafe wake cadence (parsed from the
committed `telemetry/triggers-snapshot.json`), and emits a per-lane
LIVE / QUIET / STALLED / DARK verdict table. Motivation: tonight's websites silence
(no commits after 21:52Z, ORDER 036 unacked across three failsafe windows) was caught
~4h late by a human-style read — this mechanizes exactly that sweep. Also: smallest
true playbook index edit, `control/status.md` baton advance (slice 2 = regen-window
skip detector next), claim `control/claims/claude-fm-lane-liveness.md` (deleted in
the flip commit). Advisory-only — never merge-blocking; `--strict` for wake use.
No trigger-MCP calls from this venue; no sibling repo written.

- **📊 Model:** fable-5 · high · tooling+docs — new advisory checker (Q-0105 provenance tier)
