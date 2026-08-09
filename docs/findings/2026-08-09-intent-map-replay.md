# The intent map, walked through ten real owner messages

> **Status:** `reference` · 2026-08-09
>
> Phase 2's first exercise, and **not** the test the roadmap prescribes.
> [§ 4.8](../planning/2026-08-08-agent-operating-environment-roadmap.md) requires
> that **a fresh agent's map is scored**. This is the procedure's own author
> scoring cases whose outcomes he had already read. Codex named that on fm #830
> and was right: disclosing the bias does not satisfy the protocol. So this file
> is **an author walkthrough**, the prescribed fresh-agent test **remains
> outstanding**, and nothing here should be cited as Phase 2 having been
> validated.
>
> What it does establish is narrower and still worth having: the corpus is
> assembled (§ 8 recorded that it *"exists but has not been assembled"*), the
> procedure runs end-to-end on real input, and it produced three results the
> author did not intend — §§ 2.1, 3 case 7, and 4.
>
> Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
> The corpus is `MEASURED` (verbatim, cited). The scoring is `REASONED`.

## 1 · The corpus, and why these ten

Nine asks come from one real owner instruction, preserved clause-by-clause in
[`2026-08-05-handoff-fidelity-and-boot-path.md`](2026-08-05-handoff-fidelity-and-boot-path.md)
§ 1, where each was already scored against what an agent actually carried:
**eight faithful, one narrowed.** That table beats a corpus of loose quotes
because the outcomes are known and owner-confirmed.

The tenth is OD-6, the estate's clearest documented intent *misread* —
**`Pace: slow.`** — corrected by the owner 13 days later
([`../planning/2026-07-26-consolidation-program.md:31`](../planning/2026-07-26-consolidation-program.md)).

## 2 · The two instructive cases

### 2.1 Case A — ask #1, the one that was narrowed

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
this order, and do not skip ahead."* The finding's conclusion: **"When a goal and
an imperative conflict, the imperative wins."**

**Verdict: `PARTIAL`, and it is the most useful result in the file.** The map puts
*"reading a fixed minimum list and stopping"* in **NON-GOALS**, in writing, next
to the four-path list — where the contradiction is visible instead of implicit.
But the intent was **already correctly understood** and still lost. The defect was
in the *carrying*, not the *resolving*, and it was fixed where it lived:
[`continuation-prompt`](../../.claude/skills/continuation-prompt/SKILL.md) § 4b.
**An intent map does not protect intent downstream of itself.**

### 2.2 Case B — OD-6, and why it is not a catch

> `EXPLICIT` (verbatim, his **correction**): *"That does not mean we should ever
> rush things, though it does also not mean we can't make progress. What I meant
> by it is that we should just focus on one thing at a time and do it properly
> from start to finish."*

| part | content |
|---|---|
| **EXPLICIT** | not rushing ≠ not progressing; one thing at a time; start to finish |
| **ESTABLISHED** | OD-6 as then written: **`Pace: slow.`** |
| **DERIVED** | *(inference)* "slow" was someone's compression of "properly" |
| **OPEN** | none |
| **GOAL** | completion discipline — finish one thing before starting the next |
| **NON-GOALS** | **deliberately working slowly**; unhurriedness as a virtue in itself |
| **SUCCESS** | work judged finished-or-not, never fast-or-slow — *"three hours because the task needs three hours is right; three hours because a rule says do not move quickly is not"* (`REVIEWED`, [`../intent.md:205`](../intent.md) § 8b — a ChatGPT distillation the section states is **not his verbatim words**, unlike every other cell here) |

**Verdict: `CORRECTION-HANDLED` — not a catch, and this was scored wrong until
Codex caught it on fm #830.** The input here is the owner's *correction*, which
already contradicts `Pace: slow.` in so many words. Feeding the map a message
that states the answer and then observing that the map reaches the answer
demonstrates only that the procedure reconciles a correction against stale
ESTABLISHED text. It does **not** show what the original verdict claimed — that
the map would have prevented "slow" being written in the first place.

**Testing that claim is impossible from the committed record, and the reason is
itself a finding.** The original 2026-07-26 utterance that produced `Pace: slow.`
**was never preserved** — only the compression survived, which is precisely the
defect. *You cannot replay an input that the failure mode deleted.* The general
lesson: where a record keeps only the agent's compression of an owner message,
the evidence needed to audit that compression is already gone. Keeping the
verbatim input is what makes the audit possible later.

## 3 · The remaining eight, scored compactly

| # | ask (abbreviated) | outcome then | map result |
|---|---|---|---|
| 2 | *"After, and only after… add the superbot repo"* | faithful | correct silence |
| 3 | *"all files… a fair share of the session journals"* | faithful | correct silence |
| 4 | *"how the help system works… assert the proper baseline… use its own judgements"* | near-verbatim | correct silence |
| 5 | *"games should remain out of scope for now"* | faithful | correct silence |
| 6 | *"gemini for reviews… preferably through vertex… my own paid credits"* | faithful | correct silence, **but** ESTABLISHED now cites `conventions/vertex-first-for-gemini.md` and `[D-0011]`, which the original restatement did not |
| 7 | *"which parts are genuinely better built"* | faithful | **`INTENT STATUS: NEEDS OWNER`** — see below |
| 8 | *"should not be the final planning session… verify things that aren't sure"* | faithful, improved | correct silence |
| 9 | *"a comprehensive document… and a summary in the chat"* | faithful | correct silence |

**Case 7 exercises the HIGH branch, and an earlier draft of this file scored it
both ways at once** — as a correct silence *and* as an unresolved HIGH — which
Codex caught. It cannot be both. *"Better"* is undefined, no retrieved record
defines it, and it sets the definition of success, so under § 4.3 it is **HIGH**
and the procedure must ask rather than decide:

```
INTENT STATUS: NEEDS OWNER
OPEN HIGH:
  - "genuinely better built" — by what measure? (architecture · test coverage ·
    defect rate · maintainability) The comparison's conclusion changes with it.
```

That is the procedure working, not failing: the old *"fuller picture"* paragraph
absorbed this ambiguity into confident prose, and the map refuses to.

**Tally: 0 clean catches · 1 partial · 1 correction-handled · 1 HIGH surfaced ·
7 correct silences · 0 false alarms.** No case got *worse* under the map, which
is the property that matters most for something running before every non-trivial
ask. **Zero clean catches is the honest headline** — and it is a weaker result
than the first version of this file claimed.

## 4 · What this does not establish — read before citing anything above

- **It is not the § 4.8 test.** A fresh agent must produce and score the maps.
  This author knew every outcome. The prescribed test is **outstanding**.
- **n=10, from two source documents**, one of them a single owner instruction.
- **The strongest case cannot be run at all** (§ 2.2): the input that produced
  the estate's clearest misread was never preserved.
- **"7 correct silences" is the weakest number here.** It means the map did not
  manufacture problems on seven known-good cases — not that a cold reader would
  have been silent on them.
- **The map caught a provenance error in this file, and that is the only
  unbiased datum in it.** Case B's SUCCESS cell first carried the "three hours"
  line as a bare quote beside owner-verbatim cells. It is `intent.md:205`, inside
  § 8b — a **`REVIEWED` ChatGPT distillation the section explicitly calls "not his
  verbatim words."** Writing the map did not surface that; **going to fetch the
  citation the ESTABLISHED rule demands** did. Small, but it is the § 4.8 thesis
  — retrieval catches what recall does not — landing on the author of the rule
  one screen after he wrote it.

## 5 · The one thing this changes about Phase 3

Case A is the argument for § 5.5's review-from-intent, and it sharpens it. A
correctly resolved intent was lost between the map and the artifact, by an
imperative that contradicted the goal stated four paragraphs above it. **Intent
fidelity therefore has to be checked against the *produced artifact*, not against
the planner's understanding** — those two came apart here in the one case that
failed, and reviewing the plan's author would have found nothing wrong.
