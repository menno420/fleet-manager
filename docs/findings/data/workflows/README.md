# The three fan-out scripts, and the panel output that judged the skill

> **Status:** `reference` · committed because **nothing else in the repo pointed
> at them** and they lived only in a container that is already the third of its
> session.

`fleet-preflight` says what contracts to write before a fan-out. **It ships no
runnable example.** These are the three that actually ran, verbatim.

| file | what it is | what it produced |
|---|---|---|
| `01-card-corpus-harvest.js` | 68 harvest lanes → group by class → synthesize → 3-lens verify → prescribe + critic | 515 agents, 2,188 incidents |
| `02-review-corpus-and-census.js` | 12 review-comment lanes + 20 per-repo census lanes → same back half | 471 agents, 687 incidents, 20 censuses |
| `03-judge-panel-skill-design.js` | 3 drafts from different angles → 3 judges each → synthesis grafting runner-ups | the `fleet-preflight` skill |

## Read 01/02 as counter-examples, not templates

Their verification stage is the defect [the retrospective](../../2026-08-29-fleet-orchestration-retrospective.md)
§3 documents: `survives: v.length > 0 && refuters < 2` with only one of three
lenses told to refute, and `already_covered_by` collected and never read. **Copy
the harvest and sharding structure; do not copy the survival rule.**

## 03 is the one that worked, and the rubric is why

Its judge panel discriminated where 01/02's did not — scores spread 6 → 8.5, and
the judges' catch counts came in **below every draft's self-report**. The single
design difference worth lifting:

> **One lens counts the acceptance criterion itself rather than trusting the
> artifact's self-report.** The prompt says: *"Report catches_count as your own
> count, not the draft's."*

Everything else — three angles, three lenses, graft the runner-ups — is ordinary
judge-panel shape. That one line is what made it bite.

## `skill-design-panel-output.json` — for reuse in other skills

Three full draft bodies (~32 KB) and nine judge verdicts. **The nine
`strongest_element` fields are the point**: each judge names the one step worth
grafting into any winner, so it is a ranked list of skill steps that survived
independent scrutiny and did not all reach the shipped skill.

The two runner-up drafts are not failures — the `budget` angle scored 7.33 with
its allocation table, and the `preflight` angle 6.5. Their good parts are
recoverable from here rather than from a re-run.
