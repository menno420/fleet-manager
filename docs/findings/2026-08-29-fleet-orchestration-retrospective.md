# How the estate-wide audit was actually run — orchestration telemetry and six failures

> **Status:** `reference` · 2026-08-29 · the method half of
> [the agent-error audit](2026-08-29-estate-agent-error-audit.md).
>
> **What this is:** the audit measured the estate. This measures **the audit** —
> how 1,063 subagents were coordinated, what that cost, where the design was
> wrong, and the numbers a future fan-out should plan against. It exists because
> the owner judged the method account *"just as valuable as the audit itself"*,
> and because a retrospective that lives only in a chat is the loss mode this
> repo keeps writing findings about.
>
> **Every figure here is `MEASURED`** from the run's own agent transcripts
> (`~/.claude/projects/…/subagents/workflows/wf_*/agent-*.jsonl`, which carry
> per-message timestamps and usage). Nothing is quoted from tool documentation —
> see failure 6 for why that distinction is the point.

## 1 · What was run

Two workflows over 4,583 session cards and 1,592 PR review comments across 20
repositories, plus a 20-repo instruction census. Structure of each:

```
harvest (N lanes, one per evidence shard)
  → group by error class          [plain code, no agent]
  → synthesize (1 lane per class)
  → verify (3 lenses per pattern)
  → prescribe + completeness critic
```

`parallel()` where the next stage needed **all** prior results (grouping cannot
start until every incident exists); `pipeline()` where each item could flow
independently (a class could be verified as soon as its own synthesis landed).

## 2 · The telemetry

| | |
|---|---|
| agent transcripts | **1,063** |
| output tokens | **913,042** |
| wall clock | **17.1 h** (including a ~95 min deliberate pause) |
| **measured concurrency** | **peak 4 · mean 3.8 · median 4** |
| idle samples | 379 of 4,097 15-second samples (9 %), almost exactly the pause |

**Cost by lane:**

| lane | agents | output tokens | share | mean duration |
|---|---|---|---|---|
| **verify** | **929** | **805,679** | **88 %** | 189 s |
| harvest (cards) | 68 | 52,640 | 5 % | 214 s |
| synthesize | 32 | 40,036 | 4 % | 358 s |
| census | 20 | 12,400 | 1 % | 226 s |
| harvest (reviews) | 12 | 2,122 | 0 % | ~310 s |
| prescribe + critic | 2 | 165 | 0 % | 498 s / 196 s |

### The one planning number worth carrying

**Concurrency was 4, not the 10–16 the tool reference describes** (the documented
cap is `min(16, CPUs−2)`; this container yielded 4). At 4 concurrent and a ~190 s
mean agent duration, **each additional agent costs roughly 48 seconds of wall
clock**. 1,063 agents is therefore a ~14-hour serialised job, and the whole run's
17.1 h is explained by that arithmetic rather than by any stall.

**A fan-out's size is a wall-clock decision, not only a token decision** — and
the conversion factor must be measured on the box, not read.

## 3 · The verification stage was mis-designed, not under-resourced

This is the finding that overturns the session's own first read of itself.

**929 of 1,063 agents and 88 % of all output tokens went to verification** — and
it rejected almost nothing: of 284 candidate patterns, **7 died**. Individual
verdicts: 293 CONFIRMED, 572 PARTIAL, 60 REFUTED; only **7.0 %** set
`refuted=true`.

The mechanism, exactly:

1. **Only one of three "adversarial" lenses was actually told to refute.** The
   other two answered *"is this already covered?"* and *"is this buildable?"* —
   different questions. A pattern died on `refuters >= 2`, so the single genuine
   sceptic was outvoted 2–1 **by construction**.
2. **The aggregation ignored a signal it had already collected.** **815 of 925
   verdicts named something in `already_covered_by`** — 88 % of verdicts said the
   pattern was not new — and the survival rule never read that field.

So the corrective is **not** "spend more on verification". An earlier statement
of this lesson said exactly that, and it was wrong in the same direction it was
criticising: it prescribed *"half the reader lanes, triple the adversarial
ones"*, which is invented precision on top of a stage already consuming 88 % of
the budget. **The corrective is to fix the decision rule and read the fields you
collect.**

**Where the quality actually came from:** external review (`@codex`) returned
**37 findings over four rounds, all conceded, zero survived**, several of them
overturning conclusions. Essentially all real quality came from outside the
fleet's own verification stage.

## 4 · The six failures

Recorded as instances, not as advice.

1. **Unvalidated instrument.** The error-matching regex was compiled with
   `re.X`, which silently strips literal spaces inside multi-word alternatives:
   `was wrong` became `waswrong`. **6 of 7 tested phrases were inert.** 986
   agents ran on it before anyone checked. Five known-positive strings would
   have caught it in seconds. Re-running the whole extraction with it fixed
   moved the corpus +127 sections (+1 %) — the defect was real, its size effect
   small, and *neither was known until it was measured*.
2. **Corpus mislabelled.** The finding said *"7,214 sections from 4,583 cards"*.
   The fetch also took findings, retros, audits and program docs; measured after
   the fact, **89 % cards, 10 % other documents**. The fetch scope and the
   sentence describing it were written hours apart and never reconciled.
3. **Aggregation ignored its own signal** — §3 above.
4. **Stale base.** `main` was never re-read at launch. Mid-run, one PR merged
   that **fixed the exact defect being measured**, and another landed an owner
   ruling that **retired the framing of the recommendation**. Both were found at
   the end, costing an extra PR.
5. **Inputs discarded.** The extractor kept the resulting document text and threw
   away the authoring input. The audit's own recommended follow-up — *"would this
   route have fired on that incident?"* — is therefore **impossible from its own
   corpus**, and had to be downgraded to a heuristic.
6. **Documented values reported as measured.** The concurrency figure was taken
   from the tool reference and stated as observed. The journals held the real
   number the whole time. This finding exists partly because that was caught.

Failures 1, 2, 5 and 6 are all one shape: **a property of the instrument
asserted rather than measured**, in a study about asserting rather than
measuring.

## 5 · What transfers

- **Do the mechanical work before spawning anything.** Fetching, extracting and
  sharding were done in plain Python and shell first. An agent that spends its
  context on retrieval has less left for judgement. Sharding is what turns
  *"read an impossible amount"* into *"N agents each read a possible amount"*.
- **Force structured output.** Every lane returned a JSON schema — class, gap
  class, trigger moment, verbatim quote, citation — so results arrive as data to
  group and count in code, not prose to re-read. The difference between 986
  essays and one queryable table.
- **Control flow belongs in the script, not in model judgement.** The workflow
  decides what runs and with what data; agents supply only the thinking.
- **Pause and resume works and should be verified, not assumed.** Both runs were
  stopped mid-flight for a usage-limit reset and resumed from cache: each journal
  gained **2** new `started` entries, not 68. That check is one command and it is
  the difference between resuming and silently re-running.
- **The strongest signal came from asking the reviewer to attack the weakest
  part by name.** Four rounds, 37 findings, all conceded.

## 6 · What this does NOT establish

- **Concurrency 4 is this container, this day.** It is a measurement of one box,
  not a constant. The method (read the journals) transfers; the number may not.
- **No counterfactual was run.** That a better decision rule would have produced
  better patterns is `REASONED` from the 815/925 discard, not demonstrated.
- **Agent-count-to-quality is unmeasured.** Nothing here says what the right
  number of verifiers is — only that 929 with a broken rule bought little.
- **The failure list is what was caught.** Failures nobody noticed are invisible
  here for the same reason the audit's own frequencies are floors-with-caveats.
