# 2026-07-19 · fm build slice — `emit_routine_claims.py` write-side fence emitter

> **Status:** `in-progress`

About to happen (declared born-red): the below-the-line "write-side fence emitter"
slice from `docs/planning/2026-07-19-next-slices.md` (baton item 2 of the 10:38Z
heartbeat) — a small stdlib script `scripts/emit_routine_claims.py` that updates the
```json routine-claims``` fence in `control/status.md` from CLI args
(`--failsafe-id/--cron/--next-run/--last-fired/--state`, repeatable `--deleted`,
`--pacemaker-cadence/--pacemaker-note`, `--updated` defaulting to now), so heartbeat
writers stop hand-editing JSON — the drift source the PR #341 review flagged (the
fence's `next_run`/`last_fired` go stale by hand). It validates the result
round-trips through `verify_routine_state.py`'s fence parser before writing,
`--dry-run` prints the new fence, and it refuses (exit 2) on zero or two fences.
Also: one doc index line where `verify_routine_state.py` is indexed
(`docs/playbook.md` R26), a status.md `updated` bump via the emitter itself
(dogfood), claim `control/claims/claude-fm-fence-emitter.md` (deleted in the flip
commit). No trigger-MCP calls from this venue; no sibling repo written.

- **📊 Model:** fable-5 · high · feature build — new write-side tool over a verified parser contract (Q-0105 provenance tier)
