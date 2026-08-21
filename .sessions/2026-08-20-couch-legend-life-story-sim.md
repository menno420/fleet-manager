# 2026-08-20 · hub — couch-legend phase 2: the life-story design decided, the simulator built, the runaway measured

> **Status:** `complete`

*(Flip note — the loop record. couch-legend #1: R1 on `3902e77` — 4 findings,
4 [conceded], fixed in `a4ed51f` (era-framing gate correction · F6 rail scoped
with mechanism · dead-span bucketing · the strategy-envelope gate built); R2
on `a4ed51f` — 3 findings, 3 [conceded], fixed in `f8869c3` (zero-click wall
lane + pinned boundary · F5 two-tier visibility, measured displayed floor
4.0 % · StatsPanel Clarity display routed through `clarityMultiplier`); R3 on
`f8869c3` — **3 findings, read only after the merge** (originally recorded
here as "clean, zero inline findings" — false; § Correction below carries
the mechanism); squash-merged `6e61f1d`, main ci+build+deploy all green.
One retry review-request was posted when R3's ack lagged ~25 min
(list-endpoint staleness — R3 had already reviewed the exact head). fm
#872: R1 — 5 findings, 5 [conceded] (ci made REQUIRED on couch-legend main,
ruleset 21117825 · OQ-CL-LOOKS-PASS queued · Android thread resequenced ·
counts · the Lore guard recipe); R2 — 2 findings, 1 [conceded] (the
swallowed OQ-VENTURE-STRIPE-KEYS heading restored) + 1 [partial→fixed]
(boot-read budget 7,005 → measured 6989/7000); R3 on `5edac9a` — **2
findings, read only after the merge** (also originally "clean" here). This
flip commit changes: this badge, this note, the PR line, and the test-count
currency sync 61→62 across the card Verify, the §7 row and the Layer-2
entry (the suite grew by the zero-click pin after fm's R3; named here per
the flip exemption — reviewed head `5edac9a`, after it only this commit).)*

## Correction (2026-08-21, same session — after both merges)

**Both "R3 clean" claims above were false, and the cause was my own query
windows.** The round-3 reviews landed at `00:53:19Z` (couch-legend #1,
3 findings) and `00:32:51Z` (fm #872, 2 findings); my "any new inline
comments?" checks filtered `since=01:05` and `since=00:35` — both cut
*after* the actual submit times, so each query structurally excluded
exactly what it was checking for. I saw review-object counts reach the
expected number, read zero comments through the mis-set filters, recorded
"clean", and merged. The queued PR-activity notifications carried all five
findings; they were read after close.

All five verified against source and dispositioned [conceded], fixed in
**couch-legend #2** + this PR:
- CL-P1 *minimum-start boundary*: "one hit is enough" was false — 1–3 hits
  freeze a save forever (High < 4, nugs < 10, neither replenishes); 4–9
  open only the jobs half; 10 open the full game. Pinned by engine tests;
  DESIGN § 9.6.1 + results F1 restated.
- CL-P2 *taken-prestige is a move*: the dead/check-in classifiers ran after
  the reset, so an eager prestige that bought nothing counted as no move —
  `didPrestige` now feeds both.
- CL-P2 *unrecovered rebuilds*: a second prestige before regaining the
  previous peak silently overwrote the pending measurement, a survivorship
  bias in exactly the statistic F6 watches — now closed as `unrecovered`
  and counted.
- FM-P2 *shipped head*: the Shipped line below named `3902e77`; the merged
  head was `f8869c3` (corrected in place).
- FM-P2 *permanent lore lines*: the Layer-2 mechanics paragraph still sold
  "9 permanent lore lines" against this card's own defect record —
  qualified in place.

Also verified: the Codex *cloud task* comment on fm #872 (00:05Z) describes
a commit `d73e867` that exists nowhere in the repository — its work stayed
in the task sandbox; nothing foreign reached the branch (the PR merged on
`de85e23`).

**The lesson, sized for a mechanism:** "review count reached N" plus "zero
comments since T" is only evidence when T precedes the Nth review's submit
time — derive `since` from the review object's own `submitted_at`, never
from the wall clock of the check. Candidate for the estate's trap list;
not built into a checker this session.

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

**Shipped (couch-legend PR #1, merged head `f8869c3` — five commits; the
initial three plus two review-round fix commits):**
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

**Verify:** couch-legend `pnpm check` → exit 0 (typecheck + 62/62 vitest
incl. replay parity + the strategy-envelope gate + build), run after every
change set; `ci` check-run `completed success` on every PR #1 head
(`3902e77` · `a4ed51f` · `f8869c3`) and on merged `main` `6e61f1d`
(ci + build + deploy all green, polled to terminal); every sim experiment
reproducible via `pnpm sim <cmd>` (docs/sim results doc § 0). couch-legend
`main` now REQUIRES `ci` (ruleset id 21117825, created this session on the
adoption card's second-session trigger; effective-rules endpoint read back).
fm strict gate at flip: 0 findings beyond the born-red hold this commit
releases.

**⚑ decide-and-flag (MEDIUMs, all reversible):**
- The boot-read orientation budget sits near its cliff (measured 6989/7000
  words after this session's trims; the entry first landed at 7,005 —
  Codex round 2 caught it): the next `current-state.md` entry pays the
  toll — trim or demote an old entry when adding one.
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

**Owner queue:** **`OQ-CL-LOOKS-PASS` added** (§ C) — the owner's
ChatGPT-Work looks pass is the step his own sequence puts between this
session and the implementation session, so it is a genuine blocking owner
action the queue must carry (Codex round 1 caught the close-out calling it
"no new asks"; conceded). `OQ-CL-LICENSE` stands. The tuning-adoption call
itself stays the implementation session's, under his stated division of
labor, with the trade recorded in DESIGN § 9.5 for his veto.

**Deferred-fix guard recipe (revelations permanence):** seam =
`src/components/LoreTab.tsx` (`revealed = MOODS.filter(m => peakHigh >=
m.minHigh)` + the "revelations survive Wake & Bake" caption) and
`collectMoodChange` in `src/lib/store.ts` (toasts key on `peakHigh`
crossings). Fix = save v2 `lifeHigh` field (migration
`lifeHigh = max(high, peakHigh)`), re-key both sites to it; test target =
extend `tests/save.test.ts` (migration) + pin a pure
`revealedMoods(lifeHigh)` helper in the engine suite so the promise is
mechanical, not UI-read.

**Capability delta:** none new — the Codex relay confirmed working on the
day-old repo (ack reaction on couch-legend #1; already the recorded
account-wide behavior, so no ledger append).

**Layer-2 handoff:** docs/repos/couch-legend/README.md — life-story design +
simulator thread updated (landed; next = owner looks pass → implementation),
balance-pass thread closed into it.

**PR:** couch-legend #1 **MERGED** `6e61f1d` (squash; main ci+build+deploy
green, polled to terminal) · fm #872 flips complete on this commit and lands
on green.
