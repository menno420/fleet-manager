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

## 04 — the EAP-mail evidence pass (2026-09-01, pilot-validated, full run handed to the night session)

| file | what it is |
|---|---|
| [`04-eap-mail-evidence-pass.js`](04-eap-mail-evidence-pass.js) | 20 document readers · 12 pattern-shard readers · 1 census reader · 6 prior-mail readers → three merges + dedupe → two refuting lenses per candidate (rule: `dies_if (a.refuted \|\| b.refuted) \|\| (a.already_covered_by && b.already_covered_by)`, fixtures asserted before any agent spawns) → three spine proposals, three judges with their own counts, a completeness critic. Takes `args {fm, sb, pat, judgeModel}`. |
| [`04-CONTRACTS.md`](04-CONTRACTS.md) | the fleet-preflight sheet as filled for its pilot: 18 agents, 1.22 M tokens, 19 min, concurrency 6 by demand test, and what the pilot changed. |
| [`shard_patterns.py`](shard_patterns.py) | splits the 284-pattern catalogue into 12 readable shards plus the census, sorted by repo spread; prints the corpus census the sheet quotes. |

**How to run it from a fresh clone (Git Bash on the laptop):**

```bash
FM=/c/dev/<clone>; SCR=<a scratch folder>; mkdir -p "$SCR/superbot-eap" "$SCR/patterns"
for n in $(gh api repos/menno420/superbot/contents/docs/eap --jq '.[] | select(.type=="file") | .name'); do gh api "repos/menno420/superbot/contents/docs/eap/$n" --jq .content | base64 -d > "$SCR/superbot-eap/$n"; done
python docs/findings/data/workflows/shard_patterns.py "$SCR/patterns" 12
# then: Workflow({scriptPath: "<repo>/docs/findings/data/workflows/04-eap-mail-evidence-pass.js", args: {fm: "$FM", sb: "$SCR/superbot-eap", pat: "$SCR/patterns", judgeModel: "opus"}})
```

Read `04-CONTRACTS.md` first and fill your own sheet before the first agent spawns; the pilot is the step that catches what nobody thought to check.

## 05 — the night fleet (2026-09-01/02): Fleet A rerun + the EAP false-done ledger

| file | what it is |
|---|---|
| [`05-CONTRACTS-night.md`](05-CONTRACTS-night.md) | the fleet-preflight sheet for both fleets that ran overnight: the demand test that measured this container's concurrency at 2 (not the pilot's 6), the PILOT line for Fleet B (37 agents, 4 survivors from a 3-reader pilot), and the SIZE decision to cut Fleet B's satellite (superbot) readers before its fleet-manager readers once Fleet A alone proved to need the whole floor. |
| [`05-eap-false-done-ledger.js`](05-eap-false-done-ledger.js) | Fleet B: one reader per file (split over 400 lines) across superbot `docs/eap` + 11 named fleet-manager EAP docs → claims vs. corrections extracted separately → merged into false-done ledger ROWS (claim · claimed_where/when · actually · found_where/when/by · citations on both sides) → two refuting lenses per row, same shape as 04 but with negative-coverage-prose normalization 04 does not have (05-CONTRACTS-night.md AGGREGATE) → a completeness critic. Takes `args {fm, sb, judgeModel, pilotOnly, skipSatellite}`. |

Report: [`../../2026-09-02-eap-mail-evidence-report.md`](../../2026-09-02-eap-mail-evidence-report.md) — synthesizes both fleets' surviving output, drawing on each verifier's `corrected_claim` where usable (the report's own front matter states, per row, exactly what each finding draws on — direct quotation is not uniform across all rows), with both critics' key findings summarized (not reproduced in full — the report says so and points at the raw JSON for the rest). Raw JSON: [`../2026-09-02-eap-mail-evidence/`](../2026-09-02-eap-mail-evidence/).
