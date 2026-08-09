# The intent map, replayed against ten real owner messages

> **Status:** `reference` · 2026-08-09
>
> Phase 2's first test, and the roadmap
> ([`../planning/2026-08-08-agent-operating-environment-roadmap.md`](../planning/2026-08-08-agent-operating-environment-roadmap.md)
> § 4.8) sets the terms: **real, messy, historical owner messages from the
> committed record — not synthetic examples.** § 8 of the same document recorded
> that the corpus *"exists but has not been assembled."* This assembles it.
>
> Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
> The corpus is `MEASURED` (verbatim, cited). The **scoring is `REASONED`** — see
> § 4, which states the bias before the results rather than after.

## 1 · The corpus, and why these ten

Nine asks come from one real owner instruction, preserved clause-by-clause in
[`2026-08-05-handoff-fidelity-and-boot-path.md`](2026-08-05-handoff-fidelity-and-boot-path.md)
§ 1, where each was already scored against what an agent actually carried:
**eight faithful, one narrowed.** That table is worth more than a corpus of
loose quotes, because the outcomes are known and owner-confirmed — so the
question is not *"does the map produce a nice output"* but **"does it change the
one case that went wrong, and stay quiet on the eight that did not?"**

The tenth is the clearest documented intent *misread* in the estate: OD-6, where
the owner's pacing instruction was recorded as **`Pace: slow.`** and he corrected
it 13 days later
([`../planning/2026-07-26-consolidation-program.md:31`](../planning/2026-07-26-consolidation-program.md)).

## 2 · The two instructive cases, mapped in full

### Case A — ask #1, the one that was narrowed

> `EXPLICIT` (verbatim): *"read all the required reading order files **and
> more**… **fully understand the fleet manager repo, everything that it possibly
> wants to or should know is documented there**"*

| part | content |
|---|---|
| **EXPLICIT** | read the required order **and more**; *fully* understand the repo; the premise that everything worth knowing is documented there |
| **ESTABLISHED** | the boot file's read path is *"a floor, not a ceiling"*; `CONSTITUTION.md` § "Session prompts are guidance, not orders" |
| **DERIVED** | *(inference)* a finite path list is a starting point, not the boundary |
| **OPEN** | none — he said "and more" outright |
| **GOAL** | the session can act correctly anywhere in the repo, not only on four pages |
| **NON-GOALS** | **reading a fixed minimum list and stopping** |
| **SUCCESS** | it answers a question the four paths do not cover |

**What actually happened:** the prompt's goal section was *faithful* — *"Understand
fleet-manager completely… Everything worth knowing is documented there."* Its
`READ FIRST` block, earlier and more operational, listed four paths under *"in
this order, and do not skip ahead."* The finding's own conclusion: **"When a goal
and an imperative conflict, the imperative wins."**

**Verdict: `PARTIAL`, and this is the most useful result in the file.** The map
puts *"reading a fixed minimum list and stopping"* in **NON-GOALS**, in writing,
next to the four-path list — where the contradiction is visible instead of
implicit. But the intent was **already correctly understood** and still lost. The
defect was in the *carrying*, not the *resolving*, and it was fixed where it
lived: `continuation-prompt` § 4b. **An intent map does not protect intent
downstream of itself.**

### Case B — OD-6, the misread

> `EXPLICIT` (verbatim, his correction): *"That does not mean we should ever rush
> things, though it does also not mean we can't make progress. What I meant by it
> is that we should just focus on one thing at a time and do it properly from
> start to finish."*

| part | content |
|---|---|
| **EXPLICIT** | not rushing ≠ not progressing; one thing at a time; start to finish |
| **ESTABLISHED** | OD-6 as then written: **`Pace: slow.`** |
| **DERIVED** | *(inference)* "slow" was someone's compression of "properly" |
| **OPEN** | none |
| **GOAL** | completion discipline — finish one thing before starting the next |
| **NON-GOALS** | **deliberately working slowly**; treating unhurriedness as a virtue in itself |
| **SUCCESS** | *"three hours because the task needs three hours is right; three hours because a rule says do not move quickly is not"* |

**Verdict: `CATCHES`.** The original defect was an *inference* — "slow" — promoted
into an owner-attributed directive row. Under the map that inference can only sit
in **DERIVED**, labelled as inference. A labelled inference is challengeable on
sight; an OD row reading `Pace: slow.` is not, and it stood for thirteen days and
shaped how sessions worked. **The separation is doing the work here, not the
insight** — nobody needed to be cleverer, only to put the claim in the column its
evidence supports.

## 3 · The remaining eight, scored compactly

| # | ask (abbreviated) | outcome then | map changes it? |
|---|---|---|---|
| 2 | *"After, and only after… add the superbot repo"* | faithful | no — correct silence |
| 3 | *"all files… a fair share of the session journals"* | faithful | no — correct silence |
| 4 | *"how the help system works… assert the proper baseline… use its own judgements"* | near-verbatim | no — correct silence |
| 5 | *"games should remain out of scope for now"* | faithful | no — correct silence |
| 6 | *"gemini for reviews… preferably through vertex… my own paid credits"* | faithful | no, **but** ESTABLISHED now cites `conventions/vertex-first-for-gemini.md` and `[D-0011]`, which the original restatement did not |
| 7 | *"which parts are genuinely better built"* | faithful | no — though SUCCESS is the weakest cell in the set (see § 4) |
| 8 | *"should not be the final planning session… verify things that aren't sure"* | faithful, improved | no — correct silence |
| 9 | *"a comprehensive document… and a summary in the chat"* | faithful | no — correct silence |

**Tally: 1 catch · 1 partial · 8 correct silences · 0 false alarms.** No case got
*worse* under the map, which is the property that matters most for something
about to run before every non-trivial ask.

## 4 · What this test does not establish — read this before citing the tally

- **It is retrospective and I knew the answers.** I scored a procedure I wrote,
  on cases whose outcomes are recorded in the file I harvested them from. That is
  not a blind trial, and the honest read of "8 correct silences" is *"the map did
  not manufacture problems on eight known-good cases"* — not that it would have
  been silent on them cold.
- **n=10, from two source documents, one of them a single owner instruction.**
- **Nothing here tests the sufficiency test's stopping condition.** Every case
  was resolvable from the record, so no run produced `INTENT STATUS: NEEDS OWNER`.
  The classifier's HIGH branch is **untested by this replay** — its first real
  exercise is its first live use.
- **Case #7 exposes the weakest cell.** *"Which parts are genuinely better built"*
  has no definition of "better", and the SUCCESS row I wrote for it is a
  restatement rather than a test. The map made the weakness visible and did not
  resolve it — which is the correct behaviour (that is a HIGH the owner owns) but
  should not be scored as a catch.

## 5 · The one thing this changes about Phase 3

Case A is the argument, already, for § 5.5's review-from-intent — and it sharpens
it. A correctly resolved intent was lost between the map and the artifact, by an
imperative that contradicted the goal stated four paragraphs above it. **Intent
fidelity therefore has to be checked against the *produced artifact*, not against
the planner's understanding**, because those two came apart here in the one case
that failed. Reviewing the plan's author would have found nothing wrong.
