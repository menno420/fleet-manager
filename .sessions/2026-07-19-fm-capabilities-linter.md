# 2026-07-19 · fm build slice — `check_capabilities_grammar.py` capabilities ledger format linter

> **Status:** `in-progress`

About to happen (declared born-red): the LAST below-the-line slice from the PR #349
plan (baton item 2 of the 11:02Z heartbeat) — `scripts/check_capabilities_grammar.py`,
a stdlib advisory linter for `docs/CAPABILITIES.md`'s hand-written append surfaces
(the `## Append log` + `## Mirrored lane findings` regions), per the PR #337 card's
💡 idea. It validates the ledger's own declared grammar — leading parseable UTC date,
kind classifiable capability|wall|UPDATE, venue token from the declared set (absent =
note, the file's own grandfather rule), newest-first ordering per section, supersession
notes dated + matching `check_capabilities_wall_age.py`'s exclusion shape, no undated
bare claims — plus the lowercase-stub rule (`docs/capabilities.md` stays a pointer,
never a diverging copy). WARN-level default (exit 0), `--strict` exits 1, `--selftest`
offline; Q-0105 provenance header naming what each neighbor covers
(`check_no_false_walls.py` = prose false walls in the active region; the S9 ager =
staleness of dated walls; this = the format surface both stand on). Run against the
real file; any real pre-existing drift it flags gets fixed in this same PR (smallest
true edits). Also: index line in `docs/current-state.md`'s advisory-checker bullet,
`control/status.md` heartbeat bump (fence `updated` via `emit_routine_claims.py` —
dogfood) + baton advance (below-the-line queue DRY), claim
`control/claims/claude-fm-capabilities-linter.md` (deleted in the flip commit).
No trigger-MCP calls from this venue; no sibling repo written.

- **📊 Model:** fable-5 · high · feature build — new advisory linter over the ledger grammar (Q-0105 provenance tier)
