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
**couch-legend #2** + **fm #873**:
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

Also verified — with the conclusion sized to the evidence, per its own
review round: the Codex *cloud task* comment on fm #872 (00:05:28Z)
describes a commit `d73e867` whose described snapshot never merged
unchanged. Two of
this claim's earlier arguments died in review — "the SHA doesn't exist"
(object-absence; rebases and cherry-picks preserve work under new ids)
and "locally authored + SHA-identical merge head" (that proves *which
tree* merged, not where its changes originated — a copied patch would
look the same). The argument that stands is a comparison of the actual
content, made checkable by a surprise: the comment's blob links resolve
HTTP 200 because they point at `e117177` — **this session's own born-red
commit** (reflog `@{8}`, authored in this container 00:00:21Z, parent
#870's merge), the branch tip the cloud viewer could see — and at that
state the card is still born-red, so the links don't even show the
"completed card" the comment describes. The cloud's own commit appears
nowhere checkable: not among this session's local objects (which keep
even unreachable commits), no commit subject "Complete couch-legend
phase 2 records" anywhere in merged history, and its described PR
("Complete couch-legend phase 2 planning and testing records") never
opened. Decisively, the merged records postdate it: the merged card
cites `5edac9a` (committed 00:27:59Z) and the round-2 fixes — facts
created ~23 minutes *after* the cloud comment, which its 00:05 state
could not contain — and the merged §7 row lacks the "PR #1 remains open"
note the comment describes. What this establishes, and no more: the
merged tree is the one this session built, and the cloud-described
snapshot did not merge unchanged. Whether any individual cloud sentence
was copied in cannot be checked from the record — the patch itself is
unavailable to compare (the links expose only the pre-task state) — so
the claim stops there. (fm #873's own review binding got the
same treatment and a plainer answer: Codex's "reviewed commit" `4c7ae9f`
is simply that PR's squash-merge on `main` — merge-on-green landed it at
`01:06:27Z`, thirteen minutes before the review (`01:19:26Z`), because
the card it edits was already `complete`, leaving no born-red hold to
stop the sweep. Tree `93b9e0b…` equals branch-head `b8b42bd`'s — a
squash of a single commit guarantees it — so the review covered exactly
this content, post-merge. A first draft of this paragraph guessed
"sandbox application"; the merge fact was checked only after.)

**The lesson, sized for a mechanism (and corrected twice itself in
review):** "review count reached N" plus "zero comments since T" is not
evidence for any T at or after the point comments could exist — this
correction's first version prescribed deriving `since` from the review's
`submitted_at`, and Codex pointed out that reproduces the same
false-clean: inline comments are created while the review is pending, so
their timestamps can precede submission, and the API's `since` filters
on `updated_at` regardless. (Its second version overcorrected to "not
evidence for ANY choice of T" — also wrong: a T provably before the PR
existed is valid, since every comment's `updated_at` postdates it; it is
just never the T a mid-review freshness check reaches for.) The robust
form correlates by identity, never by time: fetch
`GET /pulls/{n}/reviews/{review_id}/comments` for the new review's own id.
Candidate for the estate's trap list; not built into a checker this
session.

**The race, recorded (and its round dispositioned):** fm #873 needed no
flip — the card it edits was already `complete` — so merge-on-green's
sweep landed it the minute ci went green, while the requested review sat
in Codex's ~5.5-minute queue. Same failure class as the query-window miss
(a merge outrunning its asked review), different mechanism (a correction
PR carries no born-red hold). Its round answered post-merge with two
findings, both [conceded] and fixed here: the lesson above rewritten to
review-ID correlation (its first form prescribed `since=submitted_at`,
which reproduces the same false-clean), and the `d73e867` paragraph
rebuilt on the content-bearing argument (its first form used the
object-absence reasoning the same review rejected). This correction rides
a successor PR parked `do-not-automerge` — the sweep's designed hold —
until its own round answers, then unparks. That round answered with two
more P2s, both [conceded] and folded into the paragraphs above: the
rebuilt provenance argument still only proved *which tree* merged, not
where its changes originated — replaced by the actual content comparison
(which also surfaced that the comment's links resolve to this session's
own `e117177`, not cloud content) — and the lesson's "ANY choice of T"
overcorrection narrowed (a T provably before the PR existed is valid
evidence; identity correlation is still the form that avoids the class).
Its final round narrowed the provenance conclusion once more — the
comparison proves the described snapshot did not merge *unchanged*, not
that no cloud text was incorporated, since the patch itself is
unavailable to compare — [conceded], folded in above, and the
two-re-review cap reached: fixed, dispositioned here, landed without a
further ask.

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
