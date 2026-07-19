# 2026-07-19 · fm build slice — volatile-field drift check in `verify_routine_state.py`

> **Status:** `in-progress`

About to happen (declared born-red): the 14Z re-groom's top pick
(`docs/planning/2026-07-19-next-slices.md` § "Re-groom — 14Z cycle") — extend
`scripts/verify_routine_state.py` with a read-side volatile-field drift check.
Evidence from today: the heartbeat fence's failsafe `last_fired`/`next_run_at`
sat two firings stale across the 10:28Z→14:05Z window while the verifier still
said OK (it checks only id/enabled/cron); the fence's volatile fields silently
rot. The check: when the fence carries `last_fired`/`next_run_at` and the
export has those fields for the claimed failsafe, diff them — INFO when the
export is newer than the fence values, with capture-lag honesty ("fence
volatile fields lag export by N firing(s) — refresh via
`emit_routine_claims.py`"); NEVER a DRIFT verdict change (C1/C3 contract
unchanged, volatile fields are advisory); `--volatile-strict` opt-in exits 1 on
lag. `--selfcheck` extended. Also: smallest-edit R26 index touch if wording
needs it, `control/status.md` slice-landed bump + baton advance (next =
I8-reads-lane-fence or `check_label_hygiene.py`), claim
`control/claims/claude-fm-volatile-drift.md` (deleted in the flip commit).
No trigger-MCP calls from this venue; no sibling repo written.

- **📊 Model:** fable-5 · high · feature build — extend verified checker, tooling+docs (Q-0105 provenance tier)
