# 2026-07-19 · fm build slice — volatile-field drift check in `verify_routine_state.py`

> **Status:** `complete`

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
lag. `--selfcheck` extended. Also: smallest-edit R26 index touch, heartbeat
bump + baton advance (next = I8-reads-lane-fence or `check_label_hygiene.py`),
claim `control/claims/claude-fm-volatile-drift.md` (deleted in the flip
commit). No trigger-MCP calls from this venue; no sibling repo written.

- **📊 Model:** fable-5 · high · feature build — extend verified checker, tooling+docs (Q-0105 provenance tier)

## What shipped (PR #365)

- `scripts/verify_routine_state.py` — **V1 volatile-field drift check**
  (Addendum 2 in the provenance header): `parse_fence_claims` now also
  collects the failsafe entries' informational `last_fired`/`next_run_at`
  strings into a `volatile` claims key (non-strings stay ignored, exactly as
  before; prose grammar returns `volatile: {}` for shape parity; a
  claimed-deleted id drops its volatile entry too); new `diff_volatile()`
  compares them against the export record's `last_fired_at`/`next_run_at`
  with a 60s tolerance (fence stamps are minute/second-truncated vs the
  export's ns precision) — export newer → INFO lag line + lag count, fence
  newer → INFO "NEWER than the export" (fence live-verified post-capture),
  match → OK "current"; `cron_period_minutes()` derives the firing count for
  the hourly-family crons (`M * * * *`, `M */N * * *`; anything else →
  honest "≥1 firing (period underivable)"), counted off the `next_run_at`
  delta (advances exactly one period per fire), falling back to
  `last_fired`. **C1/C3 exit contract unchanged** — V1 lines are only ever
  OK/INFO; `--volatile-strict` opt-in exits 1 on lag (after the OK verdict
  line, with its own `VOLATILE-STRICT:` line). Absent claimed id stays C1's
  report (no V1 double-flag); export without parseable counterparts → INFO
  "not comparable". `--selfcheck` extended with the V1 block, pinning the
  founding 2-firing shape.
- `docs/playbook.md` — R26 index line: verifier description now names the
  advisory V1 volatile-field lag + `--volatile-strict` (smallest edit).
- `control/status.md` — `updated:` → 14:45Z; slice-landed subsection; baton
  advanced (volatile drift DONE, next = I8-reads-lane-fence or
  `check_label_hygiene.py`). Fence `updated` → 14:42Z written by
  `emit_routine_claims.py` itself (dogfood — the emitter ran fine from this
  venue, no classifier block to note; volatile fields honestly carry the
  14:05:27Z export truth, no trigger-MCP calls made).

## Ground-truth run 1 (2026-07-19T14:41Z, committed 14:05:27Z snapshot + live heartbeat, verbatim)

```
[OK   ] C1 claimed failsafe `trig_01GK4mjoKBP3yCabn9ux1MB2` present + enabled, cron `30 */2 * * *` matches
[OK   ] C3 claimed-DELETED `trig_01Bo7dZxM9xz2hwR36L424Z8` — absent from export
[INFO ] no pending seat-bound one-shot identifiable in the export
[OK   ] V1 fence volatile fields on `trig_01GK4mjoKBP3yCabn9ux1MB2` current vs export (last_fired fence 2026-07-19T12:32Z / export 2026-07-19T12:32Z · next_run_at fence 2026-07-19T14:31Z / export 2026-07-19T14:31Z)
------------------------------------------------------------------------
VERDICT: OK — heartbeat routine claims match the export (3 claim(s) verified).
```
(exit 0 — clean as expected: #364's fence bump is confirmed current, now
verifiably so instead of invisibly so.)

## Synthetic lag fixture — today's exact rot (10Z-era fence values vs the 14:05:27Z snapshot, verbatim)

Fixture fence: `last_fired 2026-07-19T08:32:09Z` / `next_run_at
2026-07-19T10:31:48Z` (the values the real fence carried until #364 bumped it):

```
[INFO ] V1 fence volatile fields on `trig_01GK4mjoKBP3yCabn9ux1MB2` lag export by 2 firing(s) (last_fired fence 2026-07-19T08:32Z / export 2026-07-19T12:32Z · next_run_at fence 2026-07-19T10:31Z / export 2026-07-19T14:31Z) — fence written before the export's newer fire = expected rot, not live drift; refresh via emit_routine_claims.py
------------------------------------------------------------------------
VERDICT: OK — heartbeat routine claims match the export (2 claim(s) verified).
```
(default exit 0; same run with `--volatile-strict` adds
`VOLATILE-STRICT: exit 1 — 1 fence claim(s) carry volatile fields lagging the
export (advisory rot; refresh via emit_routine_claims.py).` and exits 1.)
`--selfcheck` → PASS (0 failures) on first run; kit gate
`bootstrap.py check --strict` → born-red HOLD only pre-flip.

## Enders

- 💡 **Session idea (dedup-checked — `docs/ideas/` 16 files, the 14Z re-groom
  ranked list, 2026-07-19 cards):** **close the volatile-refresh loop:
  emitter `--from-export` + verifier prints the paste-ready fix.** Today the
  V1 lag line names the fix path but the operator still hand-derives the
  arguments (the exact transcription step where #364-style bumps can typo).
  Give `emit_routine_claims.py` a `--from-export
  telemetry/triggers-snapshot.json` mode that reads the claimed failsafe's
  `last_fired_at`/`next_run_at` straight from the snapshot, and have the V1
  lag line print that exact one-paste command. Zero-derivation fixes match
  the owner's paste-ready doctrine; contained, both halves S-sized.
- ⟲ **Previous-session review (PR #364, 14Z cycle records slice):** strong
  cycle — the snapshot refresh, re-sweep, and re-groom each landed with
  verbatim evidence, and the re-groom's top-pick diagnosis ("the read side
  said OK throughout") was precise enough that this slice could be built
  from it without re-derivation. Miss/improvement: its baton wording queued
  this slice as "make that a WARN", but the fence contract it rides declares
  volatile fields advisory — implemented as INFO + `--volatile-strict`
  opt-in instead (decide-and-flag, contract wins over baton shorthand). The
  system improvement: when a baton queues a slice touching a contract
  surface, name the contract constraint in the baton line so the builder
  inherits the bound, not just the wish.
- **Doc-audit:** everything durable is homed — check rationale + founding
  case in the script's own provenance header (Addendum 2), index line in
  `docs/playbook.md` R26, facts + baton in `control/status.md`, verbatim
  outputs in this card. The scratchpad lag fixture is demo-only (its shape
  is pinned in `--selfcheck`), correctly not committed. No orphaned
  chat-only conclusions.
- **Guard-fires:** `.substrate/guard-fires.jsonl` delta committed with the
  payload (do-not-revert); born-red HOLD was the only red in `bootstrap.py
  check --strict` pre-flip.
- **Claim:** `control/claims/claude-fm-volatile-drift.md` deleted in this
  flip commit.
