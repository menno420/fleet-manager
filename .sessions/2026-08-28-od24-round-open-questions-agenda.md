# 2026-08-28 — the OD-24 round's open-questions agenda + the continuation prompt

> **Status:** `complete` — landed after two answered Codex rounds (5 + 7
> findings, **all 12 conceded and fixed**; R2's seven fixed post-review under
> the spent two-re-review cap, dispositions in the thread). Flip exemption per
> the close discipline: the reviewed SHA is `31c0dc1`; after it come only the
> R2 fixes and this flip.

- **📊 Model:** opus-5 · high · idea/planning
- **📍 Venue:** cloud-container

## Mission

The owner, live, after the round's three audits landed: *"Use the continuation
prompt skills so the next session can review everything that these 3 audits have
produced, and then helps me to discuss and answer the open questions."*

Two deliverables, and the first is what makes the second short:

1. **A committed discussion agenda** — every open question the OD-24 round
   produced, harvested across the three audits (genesis dig · router band
   re-read · kit-tree truth pass), the owner-queue, both owner-direction
   records, the Layer-2 round thread, the v1.21.0 worklist and the program;
   each verified still-open at HEAD, classified owner-only vs agent-derivable,
   phrased so he can answer it in a sentence, with what it unblocks and what
   would settle it. Plus the two halves an agenda usually omits: **what the
   round already ANSWERED** (so the sitting cannot re-open settled ground) and
   **what a session should simply decide** (so his attention is not spent on
   questions that are not his).
2. **The continuation prompt** for that sitting — per `continuation-prompt` +
   `prompt-preflight`, pointing at the agenda rather than inlining it, and
   carrying the comprehension exception (§ 4b: reviewing the audits IS the job,
   so `READ FIRST` names the corpus, not a curated subset).

This session answers no open question on his behalf and executes no disposition
— it inventories, verifies and routes. Everything owner-gated stays gated.

## Shipped

- **[The OD-24 round's open-questions agenda](../docs/planning/2026-08-28-od24-round-open-questions.md)**
  — the sitting's working document: **eleven** owner questions in § 2 (in
  dependency order, each with options, minimum answer and what it unblocks) +
  four short ones in § 2b; § 3 the estate items that are his but not the
  round's; § 4 what the round already answered; § 5 what a session should just
  decide; § 6 the unverified residue, named; § 7 method and coverage. Indexed
  in `docs/planning/README.md`, pointed at from the queue and the round thread.
- **Two queue entries created that never existed** — `OQ-KIT-MOVE1-GO` and
  `OQ-KIT-JOURNAL-SURVIVES` — plus narrowing notes on the two the round queued
  the same day (`OQ-KIT-PROMPT-DOCTRINE` reframed to the surviving fork;
  `OQ-EAP-SPEND-WINDOW-MOOT` reframed since Q-0249 is already PL-005).
- **The round thread's next-session line** now records the owner's live
  selection (a review-and-discussion sitting) as superseding the build
  candidates a session proposed earlier the same day.
- **The continuation prompt** for the sitting, handed to the owner in chat per
  the skill's step 6 (pointer, not payload).

## The two findings this session produced

1. **The round asked him for things his own record already answers.** Five of
   the queued questions are answered in the committed record; two more were
   narrower than posed. The sharpest: `OQ-KIT-PROMPT-DOCTRINE` cited a
   2026-06-13 ruling while `.claude/hooks/README.md:483-486` carries him
   verbatim on **2026-08-09** on the same subject.
2. **The three standing letters were never in the surface he reads.**
   `MEASURED` at `origin/main`: the owner-queue held **134 `OQ-` references and
   no entry** for Move 1's GO, the journal question or the §10 confirmations,
   while every session card since 2026-08-28 recorded them as "unanswered".
   Two are now real entries; the third turned out agent-executable.

## Verify

- Harvest: 7 lanes over the three audits + queue (all ~1,900 lines) + both
  direction records + thread + worklist + program/roadmap → 68 candidates → 66
  after mechanical dedup → 26 adversarially verified (13 open / 13 closed as
  returned) + a completeness critic (9 new, 5 promoted after I verified each at
  source) + a sequencing pass. 35 agents, 0 errors.
- Every promoted claim source-checked by this session before it was written:
  the OD-24 § 5 quote at line 185 · OD-13's two-prerequisite sentence ·
  `initiative` returning zero hits across the kit's README/closeout/register ·
  the kit README's placeholder-name line · D-0011's €10 prepay · the program's
  NOW-selection rule · the queue's 134-references-no-entry measurement.
- `python3 bootstrap.py check --strict` — hold-only at the flip (real exit
  codes, no pipes). Card counts re-derived here rather than carried: kit 343,
  fm 431.

## Codex review (fm #961)

- **R1 on `93857eb`: 5 findings — 5 `[conceded]`, fixed in `31c0dc1`.** The P1:
  I folded the confirmation-doctrine fork into § 2 · B, which is a different
  subject (waiting for review, not interrupting him) — restored as § 2 · B2.
  Plus: NOW-selection is the session's by the program's own rule; D-0011 does
  record a cap so "cap or no cap" was ambiguous; the release ask belonged on
  the agenda not in the do-not-ask residue; the tally did not reconcile.
- **R2 on `31c0dc1`: 7 findings — 7 `[conceded]`, fixed post-review under the
  cap.** The P1: § 2 · B2's options (b)/(c) could have re-authorised
  `delete_trigger`, which his 2026-08-09 line unconditionally prevents — now
  carved out of every branch. **Two findings re-opened questions I had
  wrongly closed**, and in both the record beat my inference: the AGENTS.md
  **mechanism** fork is reserved for this sitting in his own direction record
  (`:147-150`), and the journal fork is called *"a round question for the
  owner"* by the dig while roadmap § 5.4 never mentions the journal at all.
  Also: Move 1 needed a real `OQ-` entry rather than a blockquote; the PL-002
  pinning item was mapped to § 5 before it existed there; the tally needed
  recomputing again after the re-openings.
- **Process failure worth recording:** I twice pushed while a review was in
  flight, superseding my own request — the exact failure the close discipline
  names. Both times I re-requested rather than landing on an unreviewed head,
  and I corrected a comment that mistakenly called the cap spent when only one
  round had been answered.

⚑ Owner decisions needed: **eleven, assembled and waiting** — the agenda is the
list, and § 2 · 0 is the one to start with. Two new queue entries carry the two
that had none.

💡 **Session idea:** this file's own audit arithmetic was wrong three times in
a row (the closed/open tally), each time because a count was hand-carried
across an edit rather than recomputed from the section it summarises. Every
correction came from a reviewer, not from the estate's own gates. A tiny
checker — "a stated count of rows in section X must equal the rows in section
X" — would catch this class mechanically, and this repo is full of documents
that assert counts about their own tables.

## ⟲ previous-session review

Session 3 (this session's own earlier half) produced the truth pass whose § 5
this agenda leans on, and its habit of stating a disposition *and* what a
session may decide without the owner is what made the agenda's § 5 possible.
One narrowing of it: its § 4 row calling the journal letter answered was
carried into this agenda and turned out wrong on review — the roadmap section
it cited never mentions the journal. The lesson is the one this round keeps
re-learning: a citation that supports a *related* claim is not a citation for
the claim you are making.

Layer-2 handoff: docs/repos/substrate-kit/README.md — the round thread's
next-session line now carries the owner's live selection and points at the
agenda.
