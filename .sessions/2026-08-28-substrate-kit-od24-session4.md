# 2026-08-28 — substrate-kit review round, session 4 (the discussion sitting: his answers, recorded)

> **Status:** `complete` — landed after **three Codex rounds: 8 + 6 + 9 = 23
> findings, 23 `[conceded]`, 0 `[survived]`**, every one verified at source
> before its fix. Flip exemption per the close discipline: the last reviewed SHA
> is `d578c02`; after it come only the R3 fixes (all nine, each named in the
> dispositions below) and this flip. The two-re-review cap is spent and **no
> review is pending** — nothing was deferred, so TRAP-007's flip-while-awaiting
> case does not apply.

- **📊 Model:** opus-5 · high · review/verify
- **📍 Venue:** cloud-container — **owner-live sitting** (he was present and answering throughout)

## Mission

The round's session 4, **selected by the owner live** after session 3 landed:
*"the next session can review everything that these 3 audits have produced,
and then helps me to discuss and answer the open questions."* A
**review-and-discussion sitting**, not a build session — read the round's
whole output, then work the open questions with him and **record each answer
as it arrives**, because answers that live only in chat are the exact loss
mode this round is about (dig gap #8, *owner-words capture*, classed
**absent**: three losses in one month with recurrence self-predicted).

Read in full before anything was put to him: the
[open-questions agenda](../docs/planning/2026-08-28-od24-round-open-questions.md)
(548 lines), all three audits — the
[kit-tree truth pass](../docs/findings/2026-08-28-kit-tree-truth-pass.md)
(652), the [router band re-read](../docs/findings/2026-08-28-router-band-reread.md)
(343), the [genesis dig](../docs/findings/2026-08-28-substrate-kit-genesis-dig.md)
(655) — the [round thread](../docs/repos/substrate-kit/README.md), and
[OD-24 in his own words](../docs/findings/2026-08-28-owner-direction-agent-autonomy.md)
(235), plus both narrowed queue entries' notes before either was put to him.

State verified at the start, not trusted from the hand-off: fm main
`b60a8f5` (**#961 merged** — the agenda is on main), kit main `7f58f0e`,
kit 0 open PRs, fm's other open PRs #958 (codex, pre-existing) and #963
(new, not this round's) both untouched.

## Shipped

- **[The sitting's answers, verbatim](../docs/findings/2026-08-28-od24-sitting-answers.md)**
  — **twelve answers** recorded as each arrived, `OWNER` quotes separated
  from `DERIVED` readings throughout. The headline: asked *which ways does
  the kit still not work* — the question no session had ever put to him — he
  **collapsed four of his own prior complaints into one root cause**:
  *"they are all related to the same root cause, which is mostly that agents
  don't take enough initiative to leave the repos in a better shape"*. The
  round had already found this (dig §6.1 called it *"the central drift …
  and the review round's real charter"*) and had then organised itself
  around the gap table instead — **the round reproduced, on itself, the
  unrouted-knowledge defect it was auditing.**
- **An unprompted sequencing directive, mid-sitting** — *"I am currently
  running 3 parrallel ultracode session to map most of all the repos, once
  this mapping is all done we should use this information to come up with a
  revised pan. Only after that will we move to execution of the 'GO'"* —
  which re-frames the whole round: its output is an **input to a revised
  plan**, not a work queue. It also confirms the Move 1 hold as a **stage
  with an exit condition**, not a deferral to re-ask next session.
- **Answers routed the same session, not batched at the end:** 7 owner-queue
  entries updated + **1 added** (`OQ-KIT-RENAME`), with **three closed** —
  `OQ-KIT-PROMPT-DOCTRINE` (presence decides), `OQ-EAP-SPEND-WINDOW-MOOT` (not
  currently relevant), and **`OQ-FM-D2-TARGET`** (`spider-swing`, the measured
  order ratified — open since 08-23 and once *falsely* closed by inference,
  fm #937, so the audit's § 6 order was re-verified at source **before** his
  ratification was recorded). Program: **OD-26** + the NOW pointer moved (flagged
  as a session's pick, per the ledger's own rule) + **two** § 7 rows — mine and
  a **back-fill for session 3**, which landed without writing one. The agenda is
  converted from an agenda into a **record**, every row annotated with his
  answer; `current-state.md`, the round thread and the findings index carry it.
- **`[D-0011]` reconciled** — the agenda's stated prerequisite to its spend
  question, which could not honestly be put to him while the ledger
  contradicted itself: the title's *"capped at its balance"* is false for the
  route the entry authorises (Vertex is credit-funded; `GEMINI_API_KEY_PAID`
  on `generativelanguage` is card-funded and uncapped). Authorisation
  survives; its *reason* changes. Not re-measured live — the cost figures are
  console-only data no session can read, quoted as his.

Everything owner-gated stayed gated: **Move 1 held** (he re-affirmed it), no
packet GO, no kit release, no adopter rollout, no rename (he deferred the
name), fm #958 and superbot untouched.

## Verify

- `python3 bootstrap.py check --strict` — **real exit codes, no pipes**, three
  runs. Run 1 surfaced **4 findings, 3 of them mine and real**: a dead link in
  the new finding (`../CONSTITUTION.md` from `docs/findings/` is one level
  short), and two `[stamp]` findings I had *caused*. Diagnosed rather than
  suppressed: the checker fires on any ledger ID cited from >1 doc and attaches
  the finding to the **alphabetically first** citing doc, so the estate's
  long-standing D-0011 citation set sat behind an allowlist entry keyed to
  `findings/2026-08-12-…/agent-A1.md` — and my new citations in
  `current-state.md` and the queue moved the finding onto **un-allowlisted**
  paths. **Fixed by not creating the duplicate citations** (prose + link carries
  the same trace), *not* by adding allowlist entries: silencing a finding I
  caused is the wall-accretion pattern OD-24 § 3 names, and OD-25 makes
  duplicated context the actual defect. Run 3: **1 finding — the designed
  born-red hold naming this card.**
- Every state claim re-verified at source rather than trusted from the hand-off:
  fm main `b60a8f5` (#961 **merged**, so the agenda was read on main, not a
  branch), kit main `7f58f0e`, kit 0 open PRs — and his D2 ratification checked
  against the intent audit's § 6 **before** being written down.
- Not verified, and named as such: the three mapping sessions' output is unread
  here (`docs/activity/` was not refreshed), and `[D-0011]`'s live billing
  figures are console-only data no session can read — quoted as his, not
  re-derived.

## Codex review — R1 dispositions: **8 findings, 8 `[conceded]`, 0 `[survived]`**

Requested explicitly (the auto-trigger produced nothing in ~10 min; all four
prior round PRs show the same explicit `@codex review` first comment), verdict
at head `a045494`, 3 × P1 + 5 × P2. Every one verified against source before
the fix; **none was argued down**, and the tally is recorded as a countable
disposition per `docs/conventions/adversarial-review.md`.

- **P1 · the journal decision's key leg was FALSE** `[conceded]` — I wrote that
  routed trap records are *"estate-scoped, not per-repo"*, which made his
  conditional (*"if the router records are functional in the same way that's
  good enough"*) fail. Codex cited the roadmap; I read it: § 5.3–5.4 is marked
  `OWNER` and says **"Each repo** defines … known traps" / **"Each repo**
  exposes its recurring traps" (`:390-399`). **Leg withdrawn** and the decision
  re-derived on a distinction that survives — **lifecycle, not scope**: a trap
  register admits what is already *recurring* and has a prevention; he asked for
  what went wrong **each session**, which is the one-off and not-yet-recurring
  the register is designed to exclude. The disposition holds, and now carries
  the condition under which it should be re-examined.
- **P1 · `[D-0011]` — the replacement justification authorised the wrong route**
  `[conceded]` — I retired *"capped at its balance"* and replaced it with
  *"Vertex is credit-funded and the credit expires unused"*, which justifies the
  **Vertex** route while the entry's verdict authorises the **card-funded**
  `GEMINI_API_KEY_PAID`. And I left the `why` block's refuted €10 chain standing.
  Now: the basis is stated as his own words, the real bound is named as the
  **route rule + disclosure** (not a balance), and the `why` block is marked
  superseded where it reasons from a cap.
- **P1 · I invented a completion gate on the EAP mail** `[conceded]` — he said
  the audits *"will provide valuable information … a valuable addition to the
  mail"* and *"soon"*. I wrote that it **waits on** the mapping, and put "wait"
  into the queue entry against his own "soon". Recorded now as an **input, not a
  gate**: fold in whatever exists at the time; do not park it.
- **P2 · "most" June rules became "all"** `[conceded]` — he allowed an
  unidentified obsolete subset; my bullet required every rule to bind until he
  personally retires one, and mis-cited OD-24 § 3 (which governs when an
  agent-made *restriction* becomes legitimate) as if it reserved obsolescence to
  him. Replaced with a **verification path**: check whether something later has
  overtaken the rule, and treat it as superseded by that evidence; retiring a
  rule nothing has overtaken stays his.
- **P2 · "the two rules were never in conflict" rewrote his older statement**
  `[conceded]` — Q-0128 says *"ever again, no matter what it is for"*, and the
  router band re-read recorded the conflict correctly. Recorded now as what it
  is: the conflict was **real**, and he resolved it by drawing a line neither
  rule drew. Q-0128 is **superseded**, not reinterpreted.
- **P2 · the twelve-gap mapping was presented inside the owner reading**
  `[conceded]` — he was shown four of his own prior statements, never the twelve
  gaps, so *"every one of our twelve is downstream of it"* is the sitting's
  inference. Now labelled `DERIVED` and separated from his answer, which matters
  because it is the claim that re-ranked the round.
- **P2 · the stalling test over-reached** `[conceded]` — *"not necessarily
  bad"* is a qualification, not a licence to treat any anti-stall benefit as
  disqualifying. The test now reads: does it stop a re-derivation? — with less
  stalling neither the case for a fix nor a mark against one.
- **P2 · a kit A/B is not a provider-mix method** `[conceded]` — his two-arm
  test measures **the kit's effect per agent**; determining the right *mix*
  needs cross-provider tasks, a shared outcome criterion and a selection rule.
  Recorded as **one arm** he named, with the which-model-for-what analysis an
  earlier cut wrongly ruled out left open and his.

## Codex R2 — **6 findings, 6 `[conceded]`, 0 `[survived]`** (head `8182c54`)

Mostly the class R1 predicted: **corrections that did not propagate**, plus one
P1 that refuted the journal decision a *second* time.

- **P1 · the journal function is already served** `[conceded]` — R1's fix argued
  *lifecycle, not scope*; R2 pointed out it never asked whether anything already
  serves the function. Verified at source: `.session-journal.md:5-7` declares the
  file **"a guidebook, not a log"** and routes per-session logs to
  `.sessions/<date>-<slug>.md` — and those cards already record what went wrong
  (this card is an instance). **Third derivation, and the simplest:** the journal
  survives **as the guidebook it already is**; his *"**easily** find out"* is a
  **retrieval** problem over 431 existing cards, not a missing record. **No new
  file, nothing enforced** — which is also the first version of this decision
  that honours superbot:Q-0101 by proposing nothing to plant.
- **P2 · the derived twelve-gap mapping did not propagate** `[conceded]` — R1
  marked it `DERIVED` in the finding while the agenda banner and OD-26 still read
  as his measurement. Marked on both.
- **P2 · the stalling qualification did not propagate** `[conceded]` — the
  Layer-2 thread and OD-26 still said "stalling is tolerable" flatly. Both now
  carry the qualification, which matters because those are the surfaces the
  revised plan will be built from.
- **P2 · "a human is present" was broader than his words** `[conceded]` — he said
  *"never while **I'm** away; freely when **I'm** present"*. A kit-planted rule
  reaching a repo with another maintainer would have permitted prompts exactly
  when the person who granted the exception is absent. Narrowed to **the owner**,
  here and in the queue.
- **P2 · Q-0128 was still listed as live estate law** `[conceded]` — § 1's
  carrier list named it among the rules to carry, while § 3 records him
  superseding it in the same sitting. A session could have restored the
  unconditional no-prompt rule and recreated the conflict. Removed from the list
  with the reason stated.
- **P2 · the completion claim swallowed the one row not asked** `[conceded]` —
  the banner said every § 2/§ 2b row was answered while its own table marks
  § 2 · G *not asked*. Now stated as every **eligible** row, with G preserved as
  an outstanding conditional question for after the census.

## Codex R3 — **9 findings, 9 `[conceded]`, 0 `[survived]`** (head `d578c02`)

Tally **8 → 6 → 9**: measurably **non-convergent**. Under the two-re-review cap
this was the last round to fix into, and the honest call was to fix all nine
rather than defer any — every one is an **objective inconsistency**, not a
judgment disagreement, and two were load-bearing. **Seven of the nine are
propagation of my own R1/R2 corrections**, which is the same class R2 already
charged and I still under-executed: a correction that stops at the canonical
finding leaves the *routed* surfaces — the ones a future session actually reads
— carrying the superseded reading.

- **P1 · I authorised unattended action by implication** `[conceded]`, and this
  is the sharpest finding of the three rounds. He answered only **when a brake
  may prompt**. I wrote that unattended it *"must decide — refuse or proceed"* —
  inventing a **fail-open authorisation for sends and deletes** while OD-24 § 3's
  confirm-before-sending-or-deleting line is still standing and un-retired. Now:
  unattended, a brake covering a send or delete **refuses**; for everything else
  the fail-open/fail-closed choice is **left explicitly unresolved** rather than
  handed to whoever builds the mechanism.
- **P1 · the superseded journal instructions were still in the file**
  `[conceded]` — the third derivation replaced the middle of § 5 but left the
  framing above it and the "open questions" paragraph below still telling a build
  session to *re-scope* the journal. The first operative-looking instruction in
  the section would have produced exactly the duplicate per-session record the
  revision rejects. Both removed.
- **P2 · the card census was wrong and I propagated it** `[conceded]` — I carried
  **431** from the agenda's § 7 into three files. Re-derived at this head:
  **433** dated cards (**432** at `b60a8f5`). Corrected, and the agenda's own
  figure is now marked wrong at both its sites rather than left to be re-copied.
  A count taken from another document and never re-run is TRAP-004's class.
- **P2 · `OQ-FM-D2-TARGET` still read OPEN in the working-plan block**
  `[conceded]` — after OD-26 closed it. A session on the step ledger would have
  re-asked him something he had just answered. Marked closed, with the "why it
  stayed open" paragraph kept as record.
- **P2 · § 5 still told a session to decide the AGENTS.md mechanism**
  `[conceded]` — a fork **he closed** in this sitting. Struck through and
  superseded; kit-planted `AGENTS.md` files are now explicitly forbidden there.
- **P2 · the round thread and current-state claimed ALL letters answered**
  `[conceded]` — while G and the BTD6 loop were never asked, the adopter half is
  open, and the name is pending. Both now say *every letter that was **asked***,
  and name the four still open.
- **P2 · the findings index still flattened the stalling qualification**
  `[conceded]` · **P2 · the agenda banner still carried the pre-correction
  June-rule rule** `[conceded]` · **P2 · the answer table still called the
  provider A/B "the method"** `[conceded]` — three more routed surfaces the
  earlier fixes had not reached.

**Three-round tally: 23 findings, 23 `[conceded]`, 0 `[survived]`.**

**The pattern, now measured across three rounds rather than guessed at.** The 23
findings are two classes, and both are this session's own thesis turned on it:

1. **Compressing an owner answer into something tidier than he said** (~8 of 23):
   an exception dropped, a conflict dissolved, an input promoted to a gate, a
   component promoted to a method, an inference folded into his voice, an
   unattended fail-open invented from an answer about prompts. A session whose
   entire product is a record of what he said eroded his answers *in the act of
   writing them down*.
2. **Corrections that stop at the canonical finding** (~12 of 23): R2 charged
   this and R3 charged it again, harder — the routed surfaces (the Layer-2
   thread, OD-26, `current-state.md`, the findings index, the agenda banner) are
   what a future session actually reads, and they kept carrying superseded
   readings after the finding was fixed. **This is exactly the round's own
   headline defect** — the dig's *unrouted* class — reproduced a third time
   inside the session that was documenting it.

The third class is a single instance worth naming separately: **the journal
disposition took three derivations**, losing a load-bearing leg in each of the
first two (the "estate-scoped" claim, refuted by the roadmap; then a lifecycle
argument that never asked whether the cards already serve the function). The
final answer proposes **nothing to build**, which is both the correct reading of
his words and the first version that honours superbot:Q-0101. A decision that
gets simpler under adversarial pressure was over-built to begin with.

⚑ Owner decisions needed: **all the round's standing letters are now answered.**
What remains his: **`OQ-KIT-RENAME`** — he ruled the kit is renamed and deferred
the name itself (one word, and no session may pick it for him); the **adopter
half** of `OQ-KIT-V1-21-RELEASE` (he answered timing only, and reading a timing
answer as an adopter answer would be the inference-as-decision error); agenda
**§ 2 · G** (card deletion — deliberately not asked, its own minimum answer is
*nothing today* pending the report-only census); and the **BTD6 history loop**,
a product question for its own sitting.

💡 **Session idea:** the sharpest structural result is *where* the round's real
charter was hiding. His one-line root cause — agents not taking enough initiative
to leave repos better — was already the genesis dig's § 6.1 verdict, called there
*"the central drift … and the review round's real charter"*; it sat in an
**intent-delta section** of a `RECORD`-tier finding, and the round's own agenda,
built by seven reader lanes over that very document, organised around the gap
table instead. So the generalizable defect is not that findings are unread — it
is that **a finding's verdict-about-the-work's-purpose has no route out of the
finding**, while its gap tables and disposition rows do (they become worklists).
The fix is routing, not mechanism — which is the half his cost function ranks
higher: when a finding reaches a verdict about what the *work itself* is for,
that sentence gets lifted into the Layer-2 thread where the next session's
agenda is built, rather than left where only a full re-read would meet it. One
convention, no new apparatus, and it is testable against this exact miss.

## ⟲ previous-session review

Two checkable findings about the sessions before me, both corrected in place
rather than noted:

1. **Session 3 landed without writing its § 7 progress-ledger row** — the boot
   file's close discipline says session close updates it, and the row is simply
   absent (grep for `#960` in the program: zero hits). This is the round's own
   `unenforced` class biting the round, so I **back-filled the row** from its
   merged finding and PR rather than leaving the gap. Worth naming precisely: it
   is not a records failure of judgment, it is a step nothing asked for at the
   moment it was due — which is the exact diagnosis the dig wrote about
   everything else.
2. **The agenda (fm #961) contradicted itself about the AGENTS.md mechanism** —
   § 2 · E asks it as his (citing his own direction record) while § 5 lists it as
   *"what a session should just decide"*. The file names this history honestly,
   so it is a surviving seam, not a hidden one; his answer (**hand-write per
   repo**) closes it in both places, and both are now annotated.

**And one about this session, recorded because it is the same class:** the § 2 · 0
answer was put to him with four options drawn from **his own prior statements**
rather than from the audits, deliberately, so the divergence measurement would
not be anchored by our reconstruction. He declined the options and collapsed
them — which is a stronger result than any pick would have been, but the
instrument only worked because the anchoring risk was designed around. A future
sitting asking "what's broken?" should do the same rather than presenting a
findings list.

Layer-2 handoff: `docs/repos/substrate-kit/README.md` — the round thread now
records session 4 and **names session 5 from his own words** (*"Records work can
go now"*): a kit-venue records session (charter rewrite + the truth pass's
23-file sweep), then the release he timed to it.
