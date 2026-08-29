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

## Two archival corrections live at the top of 01/02 and 03

The three scripts are committed **verbatim as they ran**. Where a premise in one
is now known false, the correction is a header comment rather than an edit, so
the record of what actually executed stays intact:

- **`02` — the owner lane is invalid.** It force-sets `owner_voice=true` on all
  155 `menno420`-authored review comments. Agents post with the owner's PAT, so
  none of it is his voice; 24 exported patterns inherit `owner_flagged: true`
  from that premise and the synthesis lane weighted them up on it.
- **`03` — the concurrency block the judges read as `MEASURED TELEMETRY`
  overstates itself.** "mean 3.8" is the active-sample mean (3.43 across all
  samples) and "this box gave 4" is observed throughput on one container across
  a window that spanned two; a later container measured an effective limit of 2.
  The skill those judges were shaping exists to prevent exactly this, and it
  reached them inside its own design prompt.

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
grafting into any winner — an **unranked set** of nine judge-selected steps that
survived independent scrutiny and did not all reach the shipped skill.

**They are not ranked and cannot be.** Each was chosen under a different lens,
against a different draft; the file records no rank or comparison among the
nine, and the verdict order is not even grouped by draft. A parent draft's mean
score ranks *drafts*, not individual elements picked under different criteria.
Treat file order as arbitrary.

The two runner-up drafts are not failures — `fleet-budget` scored **7.33** with
its allocation table, and `fanout-preflight` **6.83** (an earlier draft of this
line said 6.5, which was one judge's individual score, not the draft's mean).
`fleet-preflight` won at **8.0**. Their good parts are recoverable from here
rather than from a re-run.

**Each verdict now names its draft, and the labelling is auditable without the
scratch run.** The workflow emitted the nine verdicts unlabelled, in an order
that does not group by draft, so the association was reconstructed on 2026-08-29
from the run's own `ranking` aggregates — per-draft mean score, mean catches and
verdict multiset, all computed before any labelling existed.

Checking those labels against themselves would be circular, so the file carries
a `reconstruction` block holding **the independent aggregates** and the
procedure, and
[`verify_panel_association.py`](verify_panel_association.py) re-derives the
assignment from the committed JSON alone with the labels stripped:

```bash
python3 docs/findings/data/workflows/verify_panel_association.py   # exit 0
```

It asserts both halves — that exactly **one** partition into three one-per-lens
triples reproduces all three drafts' aggregates, and that this unique partition
equals the committed labels. Stdlib only, no network, no scratch run.
