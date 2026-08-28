# 2026-08-28 — the substrate-kit genesis dig (OD-24 review round, session 1)

> **Status:** `complete` — landed on green after two Codex rounds; every
> finding dispositioned.

- **📊 Model:** fable-5 · high · docs-only
- **📍 Venue:** cloud-container

## Mission

OD-24 §6 steps 1–2, executed as the review round's first session
(owner-scheduled overnight, ultracode): trace from the committed record how
the substrate-kit's practices came into existence (superbot's journal culture
→ EAP extraction → post-close), establish when practice was at its best, cite
every regression since, judge intent drift against the owner's recorded words,
classify every gap (absent · unrouted · unenforced · missing-procedure) with a
fix family, and test the owner's "too many files" lead hypothesis against
rivals. Deliverables fixed at three: the dated finding in `docs/findings/`,
the document-dispositions table (recommendations only — execution deferred to
the owner), and the Layer-2 review-round thread pointing at both.

Read-only everywhere but fleet-manager: superbot via raw fetches only (frozen
behind the live bot), substrate-kit untouched, no packet executes (OD-23 hold),
PR #955 and its branch untouched (merged 2026-08-28T00:07:55Z — verified).

## Shipped

- `docs/findings/2026-08-28-substrate-kit-genesis-dig.md` — NEW: the round's
  evidence base (three-era history · twelve classified gaps · rival verdict ·
  §10 dispositions table, recommendations only, zero deletions proposed) +
  its `docs/findings/README.md` index row.
- `docs/repos/substrate-kit/README.md` — review-round thread: session 1 done,
  next-session order recorded.
- `docs/planning/2026-07-26-consolidation-program.md` — §7 row (OD-24 round,
  session 1); NOW pointer unchanged.
- `docs/current-state.md` — OD-24 work-state bullet gains the session-1 line.

## Verify

- `python3 bootstrap.py check --strict` → exit 1 with exactly the designed
  born-red hold on this card (run before every push; the pre-flip run is the
  same predicate CI evaluates). CI `substrate-gate` on `144e8a5` red on the
  same two hold findings only (job log read, not inferred).
- Deterministic re-check battery: 21 checks, 20 PASS; the 1 FAIL corrected
  two counts in the finding (displacement rows 7→5; ender files 8→9 of 9).
- Adversarial verification workflow (6 agents): 1 CONFIRMED · 5 PARTIAL · 0
  REFUTED; all corrections applied and marked in the finding (§9 tally).

## Method (for the round's next session)

Ultracode: 14 era-reader lanes + 6 verifiers (~2.9M subagent tokens, 519
tool calls) over whole-population mechanical sweeps (969 superbot + 428 fm
cards, every file opened programmatically) with live-API date anchors.
superbot read as an API tarball of main — no clone, no writes. The one
in-flight self-correction worth inheriting: a glyph-presence metric read as
practice decline until phrase-level re-measure overturned it (§9 of the
finding).

- **⚑ decide-and-flag:** dispositions scope = the kit-practice lineage set
  (finding §10 states it); "best use" criterion stated in §3. Both MEDIUM,
  decided per intent map, flagged here.
- **💡 Session idea:** the finding's §7 gap 12 as a one-line kit norm — every
  kit release PR gets one non-author read (Codex) *of the dist diff itself*,
  recorded in the release card; it is the only mechanism that has ever found
  the kit's own checker defects (7 + 34 rows, all from adoption-diff reads).
- **⟲ Previous-session review:** fm #955 (the OD-24 record this session
  executes) — its §6 method held up as a work contract: steps 1–2 were
  executable exactly as written, and its DERIVED gap classes fit the harvest
  with one addition its authors could not have known: verification split one
  of its classes (two "absent" gaps turned out to be shipped-but-unrouted
  apparatus — the class boundary between absent and unrouted is where this
  round's real work sits). One miss to carry: #955's thread pointed the round
  at the worklist but not at Q-0266's phase plan, which §8 needed.

## Codex review (two rounds, the cap)

- **R1 on `9b1f92e`: 3 findings (2 P2, 1 P3) — 3 [conceded], fixed in
  `aa31581`.** Layer-2 carried a pre-correction gap split; a stale 8-file
  census; a four-item "three journals" list.
- **R2 on `aa31581`: 4 findings (3 P2, 1 P3) — 4 [conceded], fixed
  post-review.** The §7 ledger row's same pre-correction split; the
  superseded 86·2 PR pair replaced with the ordering-only claim; the card
  censuses restated as final-tree 161/161; two dispositions rows corrected
  (both findings already indexed).
- **Tally: 7 findings · 7 [conceded] · 0 [survived] · 0 open.** Reviewed SHA:
  `aa31581` (review object `commit_id` verified on /pulls/956/reviews). What
  came after it: the four R2 concession fixes + this close-out/flip commit —
  taken under the skill's flip exemption, named here per its own rule; the
  two-re-review cap is reached and nothing reviewable remains unfixed.

Layer-2 handoff: docs/repos/substrate-kit/README.md — review-round thread updated
PR: fm #956 — merged on green after Codex review (state verified at close).
