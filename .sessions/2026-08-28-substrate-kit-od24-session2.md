# 2026-08-28 — substrate-kit review round, session 2 (OD-24 §6 step 3, first fixes)

> **Status:** `in-progress` — born-red hold; flip is the last act.

- **📊 Model:** fable-5 · high · runtime bugfix
- **📍 Venue:** cloud-container

## Mission

Execute fm #956 §11's committed order, items 1–2, in the kit's own venue:
(1) the kit tree's one-file unrouted fix — a routed pointer to its fm-side
worklist, superseding the actively false `docs/NEXT-TASKS.md`; (2) worklist
rows 13/17/18 — the false-negative family, the checker failing at its one
job — fixed in `src/engine` with reproductions against the published v1.21.0
asset first, tests, dist regenerated via `python3 src/build_bootstrap.py`,
landed through the kit's own discipline (born-red card, READY PR, Codex
review waited, kit-quality green, flip last, merge on green). fm-side after:
rows marked fixed with the kit PR number, Layer-2 round thread advanced to
"session 2 done". If capacity remains: §11 item 4, the read-only re-read of
router bodies Q-0063–Q-0272 (superbot stays frozen).

Checked first, as ordered: the owner's morning letters (Move-1 GO · the
journal question · the §10 disposition confirmations) are **unanswered** —
no unconsumed owner comments for fleet-manager or substrate-kit, no new fm
commits past 7c3c799, nothing in the owner-queue. Everything owner-gated
stays gated: no Move 1 build, no §10 disposition execution, no release.

## Shipped

- **kit #587 MERGED on green** (merge commit `a9acc41`): the
  `docs/NEXT-TASKS.md` supersede routing the kit tree to this repo's
  worklist (gap #5), and worklist rows 13/17/18 fixed in
  `src/engine/checks/check_no_false_walls.py` with 34 named regression
  pins, dist regenerated. Each defect reproduced against the published
  v1.21.0 asset (sha256 three-way match) before its fix; a pre-push
  adversarial workflow (4 lanes, executed counterexamples + a 3,000-doc
  fence fuzz) caught 2 regressions + 2 holes in my first cut, fixed before
  review; Codex R1 (5) and R2 (6) conceded-and-fixed; R3's 4 verified and
  deferred under the two-re-review cap (tally 5→6→4, non-convergent).
- **fm-side records** (this PR): worklist rows 13/17/18 marked FIXED with
  the kit PR number; **row 35** added carrying R3's four deferred
  residuals; the Layer-2 round thread advanced to session 2 done and its
  stale routes-nowhere measurement closed in place;
  [the router band re-read](../docs/findings/2026-08-28-router-band-reread.md)
  — §11 item 4, all 208 body sections Q-0063–Q-0272 via eight reader
  lanes, 59/59 notable quotes machine-verified against the frozen router,
  seven genesis-dig claims narrowed with in-place pointers, ~13 standing
  owner rules surfaced, three letter candidates; findings-README row;
  current-state bullet extended.

## Verify

- Kit venue: repro battery (published asset → fixed engine, 41 cases at
  the end), `python3 -m pytest` 2189 passed, corpus A/B 0 newly-flagged /
  0 newly-cleared on both live trees at every round,
  `python3 scripts/preflight.py` OK — 9 legs green (real exit 0),
  kit-quality green at the flip, merged by the armed enabler.
- fm venue: `python3 bootstrap.py check --strict` — the pre-flip run's
  only findings are the two faces of the designed born-red hold (the
  `[stamp]` finding a strict run surfaced mid-session was fixed in place:
  the re-read finding now cites the trigger decision by its ledger home,
  not its token).
- superbot stayed frozen: one raw API fetch of the router file; no clone,
  no write.

⚑ Owner decisions needed: **none new** — the round's standing letters
(Move-1 GO · journal · §10 confirmations) remain open, now with the
re-read's §4 additions (the Q-0128 no-prompts vs confirm-first tension;
the ~09-07 spend-window mooting; Q-0101 as journal-letter evidence).

💡 **Session idea:** the estate's Codex rounds on new detection grammar
measured non-convergent again (5→6→4 after two full concede-and-fix
rounds) — the review cap's "land with findings named + routed to a
worklist row" exit turned that from a stall into a consumable record;
worth writing into the adversarial-review convention as the standard exit
so future sessions don't re-derive it under pressure.

## ⟲ previous-session review

Session 1's §11 order held up end-to-end: the pointer fix was one file,
all three worklist rows reproduced on the first attempt against the
published asset, and its "route, don't rebuild" note was right — nothing
here needed new apparatus. Two narrowings, both recorded in their homes:
its §9 "thinnest coverage" line is closed by the full re-read (which also
narrowed seven of the dig's claims — each now carries an in-place
pointer), and its "210 of 275" band figure counts differently from the
header-regex census (208); the re-read states both counts side by side.

Layer-2 handoff: docs/repos/substrate-kit/README.md — review-round thread
advanced to "session 2 done"; worklist thread's routes-nowhere measurement
closed.
