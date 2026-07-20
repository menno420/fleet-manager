# 2026-07-20 · fm build slice — lane-liveness ledger + transition diff

> **Status:** `in-progress`

About to happen (declared born-red): the committed lane-liveness ledger + `--diff`
idea (recorded on the #381 card). Each liveness run currently prints a table that
evaporates — lane-state transitions across runs (LIVE→STALLED, WAKING-IDLE
onset/recovery) are invisible unless a human diffs old outputs. Extend
`scripts/check_lane_liveness.py` with `--ledger [path]` (default
`telemetry/lane-liveness-ledger.jsonl`): append one JSON line per run
`{evaluated_at, snapshot_captured_at, lanes: {lane: {verdict, wake_state,
fires_since, age_hours}}}`; and `--diff` mode: compare the current run vs the
ledger's last entry — print TRANSITIONS (lane · old→new verdict/wake_state) + a
one-line headline (N transitions; recoveries vs degradations). Ground-truth demo:
run twice (seed entry + diff). Selfcheck extended; Q-0105 provenance note; seeded
first ledger entry committed (telemetry, like triggers-snapshot). Then
`control/status.md` baton advance. Claim
`control/claims/claude-fm-liveness-ledger.md` (deleted in the flip commit).
Decide-and-flag rationale: S/M, zero network beyond what the checker already
does, turns the checker into a time series. No trigger-MCP calls from this venue.

- **📊 Model:** fable-5 · high · feature build — extend verified checker, tooling+telemetry (Q-0105 provenance tier)
