# The cold-session rubric — pre-registered

> **Committed before any answer existed.** The estate's § 4.8 method requires a
> producer-and-scorer split with the rubric fixed in advance, because a rubric
> written after the outputs are read is a description of them. Commit SHA of
> this file is the timestamp that makes the claim checkable: the answering
> agents had not been spawned when it landed.
>
> **Scored blind by a separate agent** that never sees this run's synthesis,
> only the ten answers and this rubric.

## What is being tested

Not whether the baseline is well written. Whether a **cold session with no
prior knowledge of this estate** can answer real routing questions **from the
baseline artifacts alone** — which is the whole claim the successor rests on.

## What the answering agents get

`docs/findings/2026-09-04-estate-truth-baseline.md`,
`docs/planning/2026-09-04-estate-seed-manifest.csv`, and
`docs/findings/data/2026-09-04-estate-truth-baseline/` (classification, delta,
anchors, contracts). **Nothing else** — no `ESTATE.md`, no `docs/repos/`, no
boot file, no consolidation program. If an answer needs a file outside that
set, the baseline has failed the question, and saying so is the correct answer.

## The ten questions

| # | Question | What a passing answer must contain |
|---|---|---|
| Q1 | What is `spider-swing` actually for? | The product in plain language, and its state word |
| Q2 | Is `superbot-next` active, paused, archived or superseded? | The state word **and** what supersedes it |
| Q3 | Where does current product truth live for `couch-legend`? | A path **inside that repository**, not a hub document |
| Q4 | What did the owner last settle about the successor hub's name and build order? | `estate`; the four-step build order; the decision ids |
| Q5 | Is fleet-manager's description of `product-forge` still trustworthy? | A yes/no/partial **with the specific disagreement or its absence** |
| Q6 | What work is currently in flight anywhere in the estate? | The open PRs at the pinned instant, **and** that they are pinned |
| Q7 | A fresh agent must work on `creator-kit`. What does it read first, and what must it NOT trust? | The real entry point **and** the unrendered-template warning |
| Q8 | What belongs in `estate`, and what stays only in fleet-manager? | The three verbs, and the rule that decides between them |
| Q9 | Which of the baseline's claims are measured, which are owner-stated, which are derived? | That the distinction is carried per row, and where |
| Q10 | Which successor seed facts would go stale immediately if copied? | The `stale_on_copy` concept and at least one concrete instance |

## Scoring, per question

| Score | Meaning |
|---|---|
| **2** | Answered correctly and completely from the given artifacts, with the source named |
| **1** | Substantially right but incomplete, or right without naming where it came from |
| **0** | Wrong, or the agent had to guess |
| **N** | Correctly reported as **not answerable** from the given artifacts — **this is not a failure of the agent, and it counts as evidence about the baseline, which is what the run needs to know** |

## The bar, fixed in advance

- **PASS** — mean ≥ 1.6 across the ten, **no** question scoring 0, and every `N`
  accompanied by the artifact that should have carried it.
- **PARTIAL** — mean ≥ 1.2, at most two questions at 0.
- **FAIL** — anything else.

## What the scorer must also report, regardless of score

1. **Any answer that is right for the wrong reason** — the agent guessed and
   landed correctly. This is the failure mode a score cannot see, and it is the
   one that matters most for a baseline meant to be trusted by strangers.
2. **Any answer that cites an artifact that does not say what the answer says.**
3. **Which questions the baseline answers only because the answering agent
   already had estate context leaking in from its own environment** — the
   agents run in this repository, so a leak is possible and must be named.

## What this test does not establish

- It does not test the `estate` tree, which does not exist. It tests whether
  the **baseline** can seed one.
- It does not test the owner's own browsing half of the acceptance test, which
  is his to run.
- Ten questions is a sample. A pass here is evidence the baseline routes, never
  proof it routes everything.
