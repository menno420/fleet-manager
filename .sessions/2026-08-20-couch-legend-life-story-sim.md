# 2026-08-20 · hub — couch-legend phase 2: the life-story design decided, the simulator built, the runaway measured

> **Status:** `in-progress`

- **📊 Model:** fable-5 · high · feature build — the continuation session the
  adoption session's brief directed (couch-legend
  `docs/planning/2026-08-20-life-story-direction.md`, owner-directive):
  think, decide, simulate, propose — design the ~18-stage life story, build
  and validate the balance simulator before any stage content, produce a
  tested balance + stage proposal. Session start 2026-08-20 ~22:40Z, spans
  into 08-21.

Time: 2026-08-20 → 08-21 · venue: scheduled continuation (remote container,
boot on fleet-manager, couch-legend attached with push) · branch
`claude/couch-legend-life-story-stages-ki6psr`

## What is about to happen

couch-legend PR #1 (design + simulator + results, live game untouched) is
open with @codex requested; this PR carries the fleet-manager records: this
card, the Layer-2 re-thread (life-story design + simulator thread → landed;
next = the owner's ChatGPT-Work looks pass, then implementation), the
program §7 row, the current-state shipped entry, close-out, strict gate,
Codex loop, flip.

## Previous-session review

⟲ fm #870 (merged `295ef37` by merge-on-green ~40 s after its flip — the
designed flow): checked at `main` — `docs/repos/couch-legend/` present, the
program §7 adoption row present, and the Codex-R3 route fix (`3ccdf4b`)
verified live in `doc-routes.json` (both couch-legend `says` strings carried
the simulator-first sequence; this session's own boot hook served that text).
Nothing to repair.

## 💡 Session idea

The optional-Tuning pattern is the estate's template for proposing balance
changes to a live game without touching it: an engine parameter whose
default reproduces today byte-for-byte (identity-pinned), a simulator that
sweeps candidates through it, and adoption as a one-line default flip with
evidence attached. spider-swing's difficulty work is the obvious second
user — its A/B harness could grow the same seam instead of forking configs.

## Close-out

**Shipped (couch-legend PR #1, head `3902e77`, three commits):**
- `src/lib/actions.ts` (+ store rewire, `tests/actions.test.ts`): the pure
  action layer — hit, three purchases, Wake & Bake — extracted with exact
  store semantics so the simulator and the UI run one implementation.
- `src/lib/sim/` (harness · seven archetype policies · replay validator ·
  `stage-proposal.ts` with the fitted 18-stage table) + `tools/simulate.ts`
  (one documented command per experiment) + `tools/trace/` (the two
  hand-played Chromium trace drivers + method README) +
  `tests/{sim,tuning,replay}.test.ts` + `tests/fixtures/` (both traces,
  recorder defects annotated with evidence).
- `src/lib/engine.ts`: optional `Tuning` parameter (clarity knee + milestone
  cap); default `PROTO_TUNING` reproduces the prototype exactly
  (identity-pinned) — **the deployed game's behavior is unchanged**.
- `docs/DESIGN.md` § 9 (the decided stage system, validated north star, six
  fairness rails, endless-tail answer + its stated trade, visual plan,
  the revelations-permanence defect recorded) ·
  `docs/sim/2026-08-20-life-story-balance.md` (evidence + sim-lab verdicts)
  · `docs/sim/data/` (both 14-day datasets, 3 seeds × 7 archetypes).

**Shipped (this PR):** this card · Layer-2 re-thread (life-story thread →
landed, balance thread → closed into it, header date) · both couch-legend
doc-route `says` strings updated to the post-session sequence (the exact
staleness class Codex R3 caught on fm #870 — not repeated) · program §7 row
· current-state shipped entry.

**Verify:** couch-legend `pnpm check` → exit 0 (typecheck + 60/60 vitest
incl. replay parity + build), run after every change set; `ci` check-run
`completed success` on PR #1 head `3902e77`; every sim experiment
reproducible via `pnpm sim <cmd>` (docs/sim results doc § 0). fm strict gate
at flip (below).

**⚑ decide-and-flag (MEDIUMs, all reversible):**
- "Numbers in the content tables" delivered as the typed
  `stage-proposal.ts` module + results doc, with live `content.ts`
  untouched — the brief scopes this session to planning/testing and the
  owner's looks pass precedes any behavior change.
- Tuning candidate knee **80** (not 40) chosen for first-2-hours invariance;
  cap 6 kept as beyond-horizon insurance, measured inert through day 14 and
  stated as such.
- Replay-band wallet floors sized to recorder resolution (~2 units ≈ one
  50 ms tick of action-timing skew), mechanism documented in the test.
- The two trace fixtures keep their recorder defects (phantom hits, lagged
  prestige record) **annotated in-fixture with the evidence** rather than
  scrubbed — the record stays honest and the replay proves the bands hold
  through the degraded window.
- Card dated 2026-08-20 (session start ~22:40Z), work spans into 08-21.

**Owner queue:** unchanged — no new owner-only asks (Codex answers on
couch-legend: eyes-ack measured on PR #1; the tuning-adoption call is the
implementation session's under his stated division of labor, with the trade
recorded in DESIGN § 9.5 for his veto). `OQ-CL-LICENSE` stands.

**Capability delta:** none new — the Codex relay confirmed working on the
day-old repo (ack reaction on couch-legend #1; already the recorded
account-wide behavior, so no ledger append).

**Layer-2 handoff:** docs/repos/couch-legend/README.md — life-story design +
simulator thread updated (landed; next = owner looks pass → implementation),
balance-pass thread closed into it.

**PR:** fm #872 — born-red until this card flips; couch-legend #1 driven to
terminal state in-session (Codex loop below).
