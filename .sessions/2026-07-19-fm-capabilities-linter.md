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

## What shipped (PR #358)

- `scripts/check_capabilities_grammar.py` (Q-0105 provenance header): lints the
  hand-written append surfaces only (`## Append log` bounded by the first `---`;
  each `###` subsection of `## Mirrored lane findings` separately) — the kit-owned
  seed fence and the folded legacy manifest are exempt from the entry grammar, but
  rule G5 (supersession well-formedness) scans everything below the seed fence
  because the live 2026-07-16→07-18 SUPERSEDED note sits in the folded manifest.
  Rules: **G1** leading parseable non-future date (`[g1-undated]` bare claim /
  `[g1-misdated]` date hiding mid-block / `[g1-baddate]` / `[g1-future]`) ·
  **G2** kind classifiable via the ager's own `_kind_token` (imported; verbatim
  fallback if the ager's kill-switch ever fires) · **G3** venue token ∈
  {owner-live, autonomous-project, routine-fired, subagent, any} — omitted venue
  is a NOTE (the ledger's own grandfather rule: read as `any`), a token-shaped
  typo is a FLAG · **G4** newest-first per section (non-increasing leading
  dates) · **G5** any resolution/supersession-marked block must carry a
  parseable date (the ager's date-guard input) and an UPDATE bullet must match
  the ager's exclusion regex `(?<!un-)supersed` (`RESOLVED_MARKERS[0]`, cited) —
  else it never registers as a notice there · **G6** `docs/capabilities.md`
  lowercase stub stays a pointer (must reference CAPABILITIES.md, no own append
  log, no dated capability|wall rows, stays small). Default exit 0 (WARN-level
  advisory, standalone, never wired into `bootstrap.py check`); `--strict` exits
  1 on FLAGs (notes never); `--today` for testability; `--selftest` offline
  (17 assertions). Neighbor split named in the header: `check_no_false_walls.py`
  guards the PROSE above `## Append log`; the S9 ager guards CONTENT FRESHNESS
  of dated walls; this linter guards the FORMAT both stand on.
- `docs/current-state.md` — advisory-checker bullet extended (index line: the
  S3/S5/S9 trio joined by `check_lane_liveness.py` #350 +
  `check_capabilities_grammar.py` #358).
- `control/status.md` — `updated:` → 11:38Z (fence `updated` bump written by
  `emit_routine_claims.py`, dogfood — only `updated` changed); slice subsection;
  baton advanced: **below-the-line queue DRY** (#357 + #358 exhaust the PR #349
  plan) — next executable work is a fresh planning groom, honest idle on
  watches/records until then; Gates refreshed.

## Ground-truth runs (2026-07-19T11:3xZ, verbatim)

Real file — CLEAN, so no drift fixes were needed in this PR (the fix-in-same-PR
clause was armed but unexercised):

```
check_capabilities_grammar: CLEAN — every linted append entry matches the grammar (0 note(s)) [shapes: imported from check_capabilities_wall_age]
```
(exit 0; `--strict` also exit 0.) Selftest:
```
selftest: PASS (0 failure(s)) [shapes: imported from check_capabilities_wall_age]
```

Mutation probes on scratchpad copies of the REAL file (proof the real-file path
detects seeded drift — a lenient CLEAN would be worthless):

```
FLAG [g4-order] L162 (Append log): 2026-07-19 appears BELOW the older 2026-07-17 (L147) — the section is `newest first`: 2026-07-19 · wall · autonomous-project · **Non-author merge …
```
```
FLAG [g3-venue] L135 (Append log): 3rd field 'autonomous-projct' looks like a venue token but is not one of ['any', 'autonomous-project', 'owner-live', 'routine-fired', 'subagent']: 2026-07-17 · wall · autonomous-projct · **Self-scheduling th…
```
(first probe advisory exit 0; second probe run `--strict`, exit 1 — contract
verified both ways.)

## Enders

- 💡 **Session idea (dedup-checked — `docs/ideas/` 16 files, 2026-07-18/19
  cards, the PR #349 plan doc):** **graduate the CAPABILITIES checker pair
  (S9 `check_capabilities_wall_age.py` + this grammar linter) into
  substrate-kit as kit-owned checkers.** Every fleet repo carries the same
  kit-planted `docs/CAPABILITIES.md` — same seed fence, same append-log
  grammar, same discovery rule — but only fm guards its format and staleness;
  the other ~18 ledgers drift unguarded (websites' 10-entry append log,
  idea-engine's, mineverse's). The kit already renders `bootstrap.py check`
  everywhere, so a kit release would carry the pair fleet-wide for free,
  advisory-tier, instead of each lane re-inventing or going bare. Distinct
  from the recorded cited-SHA-age idea (that ages citations; this ports
  existing checkers) and from the kit's own seed-refresh machinery (which
  owns the fence, not the hand-written region below it).
- ⟲ **Previous-session review (PR #357, `emit_routine_claims.py`):** the
  standout was making the CONSUMER'S parser the write gate — round-tripping
  the whole new file through `verify_routine_state.parse_fence_claims` before
  writing a byte means the emitter structurally cannot produce a fence the
  verifier would exit-2 on; and the dogfood write with export-truth honesty
  (refusing to bump `last_fired` for a fire it couldn't verify) carried the
  #355 no-invented-fire discipline forward. Miss/improvement it surfaces:
  `--updated` defaults to NOW, so a bare invocation silently stamps "claims
  re-verified now" even when the writer verified nothing — the stamp's
  semantics ("UTC instant these claims were (re)verified") deserve an
  explicit opt-in (e.g. require `--updated` or a `--reverified-now` flag) so
  the default can't quietly assert a verification that didn't happen. This
  session passed an explicit `--updated` for exactly that reason.
- **Doc-audit:** durable homes checked — linter rationale + neighbor split in
  its own Q-0105 header, index line in `docs/current-state.md`'s
  advisory-checker bullet, facts + DRY baton in `control/status.md`, verbatim
  runs in this card; the PR #337 card's 💡 idea is now discharged by this
  slice (provenance chain: #337 card → #349 plan → #358). No chat-only
  conclusions left unhomed.
- **Guard-fires:** `.substrate/guard-fires.jsonl` delta committed
  (do-not-revert); born-red HOLD was the only red in `bootstrap.py check
  --strict` pre-flip.
- **Claim:** `control/claims/claude-fm-capabilities-linter.md` deleted in
  this flip commit.
