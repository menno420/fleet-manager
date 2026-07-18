# 2026-07-18 · fm routine-claims fence (machine-readable heartbeat routine block)

> **Status:** `complete`

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

## What shipped (PR #339)

- `control/status.md` — new machine-readable **`routine-claims` fence** (a ```` ```json
  routine-claims ```` block) in the "Routine state" section, carrying the current
  verified facts: seat, updated `2026-07-18T22:14Z`, failsafe
  `trig_01GK4mjoKBP3yCabn9ux1MB2` (cron `30 */2 * * *`, next fire 22:33:20Z, state
  `armed`), deleted `trig_01Bo7dZxM9xz2hwR36L424Z8`, pacemaker
  `send_later`/~30-min-overnight. JSON (not YAML) so the whole pipeline stays
  stdlib-clean. Neutral facts only; the prose bullets stay for humans. The fence
  contract is documented in an HTML comment directly above the block (the
  `control/README.md` grammar doc is retired/historical, so the live contract note
  rides the file itself, per its own banner). Top `updated:` bumped to 22:14Z.
- `scripts/verify_routine_state.py` — claims now come from the fence when present
  (`parse_fence_claims` + `extract_claims`); the prose grammar stays as fallback for
  fence-less heartbeats. A present-but-malformed fence (bad JSON, non-object body,
  unknown failsafe state, id-less entry, non-list `deleted`, two fences) is a **loud
  exit-2 contract violation, never a silent prose fallback** — silent fallback would
  hide exactly the drift the fence exists to prevent. Output header names the claims
  source. `--selfcheck` extended with 10 fence assertions (parse, fence-over-prose
  preference, failsafe-as-list, untagged-fence ignore, 6 violation shapes).
  Provenance-header addendum dated 2026-07-18 records the change.
- Drive-by (fix-on-sight): `.sessions/2026-07-18-fm-wake-oversight.md` `📊 Model:`
  line amended `fable-family · high effort · fleet-oversight wake` →
  `fable-5 · high · review/verify — fleet-oversight wake` — clears the two standing
  PL-004 advisory warnings (`model-line-effort`, `model-line-class`) that had been
  noted-but-unowned across three sessions (#335, #337, #338 all observed them).
- `.substrate/guard-fires.jsonl` — telemetry delta from this session's check runs
  committed (do-not-revert rule); swept: the new records are the recurring
  known-false-positive stamp/link fires + this card's own born-red session-log fire —
  and NO model-line fires post-fix (the drive-by's proof).

## Ground-truth runs (verbatim)

`python3 scripts/verify_routine_state.py --selfcheck` →

```
selfcheck: PASS (0 failure(s))
```

Against the committed (still pre-cutover, 20:42:05Z) snapshot — the SAME known
capture-lag DRIFT verdict as PR #335's proof run, now read from the fence
(`claims source` line new):

```
========================================================================
ROUTINE STATE — 1903 records (13 enabled) vs control/status.md
claims source: routine-claims fence
export capture instant 2026-07-18T20:42Z (1.5h before now=2026-07-18T22:11Z)
========================================================================
[DRIFT] C1 claimed failsafe `trig_01GK4mjoKBP3yCabn9ux1MB2` ABSENT from the export
[DRIFT] C3 claimed-DELETED `trig_01Bo7dZxM9xz2hwR36L424Z8` 'Fleet Manager failsafe wake' is still ENABLED in the export
[INFO ] no pending seat-bound one-shot identifiable in the export
------------------------------------------------------------------------
VERDICT: DRIFT — 2 mismatch(es) between the heartbeat's routine claims and the export. Capture predates 'now' — if the claims are NEWER than the 2026-07-18T20:42Z capture this may be capture lag, not live drift: refresh the export (list_triggers, ALL pages) and re-run for live truth.  (exit 1)
```

## Gates

- `python3 bootstrap.py check --strict` → exit 0; the only red-class note is the
  by-design born-red session-gate HOLD on this card pre-flip. The two PL-004
  model-line advisories are **gone** (grep over the full check output: zero
  `model-line` findings).
- PR #339 (`claude/fm-routine-claims-fence`), lands on green.

## 💡 Session idea

**A write-side fence emitter** (`--emit-fence` flag on `verify_routine_state.py`, or a
tiny `scripts/emit_routine_claims.py`): given a fresh verified `list_triggers` export,
render the `routine-claims` fence JSON mechanically — seat failsafes from the export's
enabled seat-named crons, deleted ids from a supplied predecessor list, pacemaker from
pending one-shots — so heartbeat writers paste generated facts instead of hand-typing
them into the fence. Today the fence closes the READ side (tooling parses a contract,
not prose) but the WRITE side is still a human transcription step, which is where the
next typo'd trig-id will come from; a shared emitter makes writer and verifier two
views of one schema. Dedup-checked: `docs/ideas/` (16 files) and the recent cards
cover the fence itself (PR #335 card — implemented here), post_capture_deltas,
auto-supersede, the capabilities-grammar linter, seat version-stamps, and the
current-state dated header — none cover write-side generation of the fence.

## ⟲ Previous-session review

**PR #338 (fm-claims-cleanup)** was honest smallest-slice control hygiene done right:
it acted on the #335 doc-audit's carried-forward observation (the stale
`claude-fm-wake-2026-07-18.md` claim on main) instead of letting it ride a third
session, retired both terminal claims (#332/#337), and its 22:04Z heartbeat re-sweep
recorded verifiable per-PR landing facts (ids + times) rather than vibes. What it
could have done better / the system improvement it surfaces: it *observed* the two
PL-004 model-line advisories (they are verbatim in the guard-fires delta it
committed) and — like #335 and #337 before it — left them standing as "not this PR's
diff". Three consecutive sessions noting the same advisory is the advisory-finding
ownership gap: advisory fires on *merged* cards have no assigned owner, so they
outlive sessions until someone claims them. This slice's drive-by cleared these two;
the durable fix is a standing wake-checklist line (or session-ender) "sweep standing
advisories — fix or explicitly route each one", so an advisory can never be noted by
three sessions without an owner.

## 📋 Doc-audit

Durable homes updated in-session: the fence contract lives in `control/status.md`'s
comment block (its consumer's docstring cross-references it); the verifier's
provenance header carries the dated addendum; this card carries the verbatim
ground-truth runs the PR body promises; the drive-by is self-documenting (the fixed
line IS the record, plus the guard-fires delta proving zero model-line fires
post-fix). Claim `control/claims/claude-fm-routine-claims-fence.md` released in this
flip commit (`bootstrap claim --delete`). No sibling repo touched; no owner-queue
change (no new owner-only work discovered); no chat-only residue.
