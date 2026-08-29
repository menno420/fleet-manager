# 2026-08-29 — the fan-out's own telemetry, measured and recorded

> **Status:** `in-progress` — born-red. Recording the method half of the
> estate-wide audit, plus an `ultracode` fleet-preparation skill derived from it.

- **📊 Model:** withheld · high · research
- **⚑ Model-slot note:** the harness policy for this session forbids a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container

## Mission

Owner ask, live, after the audit landed: *"I'd like you to properly write down
what you just told me, because I think this is just as valuable as the audit
itself"* — and then a second, sharper one: build an **`ultracode` skill that
does the proper preparation to start a well-organised fleet**, explicitly *not*
a skill about how to invoke ultracode, but one carrying *"things you'd do
differently next time."*

Two deliverables, and the first makes the second honest:

1. **[The orchestration retrospective](../docs/findings/2026-08-29-fleet-orchestration-retrospective.md)**
   — measured from the run's own agent transcripts rather than recalled.
2. **The skill**, derived only from those measurements and from the six real
   failures, judged by an acceptance test that asks of every step: *would a
   session following this have avoided the failure that actually happened?*

## The measurement this session owed

The previous turn ended by conceding that the concurrency figure reported to the
owner — *"roughly 10–16 agents at once, about five waves"* — had been **read from
the tool reference and reported as observed**, and that the journals held the
real number. This session opened by getting it.

**It was 4.** Peak 4, mean 3.8, median 4, across 4,097 fifteen-second samples.
The published claim was wrong by 3–4×, and the correction changes planning: at
concurrency 4 and ~190 s mean duration, **an added agent costs ~48 s of wall
clock**, so 1,063 agents is a ~14-hour serialised job.

The same pass overturned the session's *other* self-assessment. It had told the
owner the harvest was over-provisioned and verification under-provisioned.
Measured: **verification was 929 of 1,063 agents and 88 % of output tokens**, and
killed 7 of 284 patterns. It was not under-resourced — **its decision rule was
broken**, and it discarded a signal (`already_covered_by`, present in 815 of 925
verdicts) that it had already paid to collect.

## Verify

- All figures from `agent-*.jsonl` transcripts (per-message timestamps + usage),
  not from tool documentation — the distinction is failure 6 in the finding.
- Concurrency by 15-second sampling across the full span; lane attribution by
  matching each agent's first user message against its launch prompt.
- `python3 bootstrap.py check --strict` → real exit code, no pipe.

## ⟲ Previous-session review

Previous card:
[`2026-08-29-audit-banner-counts.md`](2026-08-29-audit-banner-counts.md)
(fm #969, merged).

**Held up.** It was itself a correction of a stale counter, caught by re-grepping
main after the merge rather than by waiting for a reviewer — the right reflex,
and the one the four review rounds had been training.

**What it could not know:** its own closing argument — that the review loop had
stopped converging — rested on counting findings per round, which is the same
denominator problem the audit refuses elsewhere. The rounds were not comparable:
round 1 reviewed a 350-line finding, round 4 reviewed a 9-line diff. **The
non-convergence call was probably right for the wrong reason.** Named here, not
re-litigated; the loop did stop, and stopping was correct on the P1 trend alone.

## 💡 Session idea

**The estate has no instrument for its own fan-outs.** Every number in the
retrospective came from parsing raw agent transcripts by hand, in a one-off
script, after the fact. The journals carry timestamps and per-message usage for
every subagent, so concurrency, per-lane cost, duration distribution and the
discovery/judgement budget split are all mechanically derivable at any time.

A small reader — `tools/fleet_telemetry.py <run-id>` — would make *"what did that
fan-out actually cost and where did the budget go?"* a one-command question
instead of an afternoon. It is the measurement half of the promotion rule the
roadmap already orders: you cannot promote what measures useful if measuring
costs more than the promotion.

**Why an idea and not an action:** it is tooling nobody asked for, and OD-26 §13
puts mechanisms behind the revised plan. It is also the natural companion to the
skill this session is writing — the skill tells a session what to plan for; the
reader tells it what actually happened.
