# Audit data — the raw catalogues behind the 2026-08-29 agent-error audit

> **Status:** `reference` · these are **inputs**, not findings.
>
> [The audit](../2026-08-29-estate-agent-error-audit.md) used roughly **ten** of
> the 284 patterns here. The rest were harvested, classified and adversarially
> judged, then never read by a human — they were about to die with the
> container that held them. Committed so the next session starts from the
> catalogue rather than re-running 986 subagents.

## The files

| file | rows | what a row is |
|---|---|---|
| `2026-08-29-agent-error-patterns.jsonl` | **284** | a candidate recurring agent-error pattern: `name`, `one_line`, `trigger` (hook-firable moment), `instances` (cites), `repos`, `instance_count`, `repo_count`, `gap_class`, `fix_family`, `proposed_fix`, `maps_to_existing_trap`, `severity`, **plus the panel outcome** — `survives`, `refuter_count`, `already_covered_by`, `panel_run` |
| `2026-08-29-repo-instruction-census.jsonl` | **20** | one repository's agent-instruction surface: canonical `repo` id (+ `full_name`, `aliases`, `scope_notes`), what it `instructs`, what `enforcement` exists and of what kind, its `prose_only_rules`, `divergences_from_kit`, `biggest_gap`, `portable_lesson` |

## How to read them, and how not to

**These are candidates, not findings.** The audit's §3 records that the
adversarial panel rejected 7 of 284 — a 97.5 % pass rate, which is a bar nothing
fails. **A row here has survived almost nothing.** Its `instances` are real
citations and its counts are observed mention counts, but the *pattern* is one
lane's clustering, not a verified claim.

**The seven are identifiable, and so is the margin on the rest.** Every row
carries the panel's own output: `survives` (7 false), `refuter_count`
(**`MEASURED`: 0 on 226 rows · 1 on 51 · 2 on the 7 that died**) and
`already_covered_by` — the field the survival predicate collected and never
read, which is the retrospective's §3 defect made inspectable rather than only
described. **It is populated on all 284 rows**, so every row was told by at
least one lens what already covers it and the predicate discarded all 284
answers.

A row with `refuter_count: 0` was not *endorsed* by three lenses — only one of
the three was told to refute at all. Read 0 as "unchallenged", never
"confirmed"; the 51 rows at 1 are the ones that came within one lens of dying.

Useful cuts, all mechanical:

```bash
D=docs/findings/data/2026-08-29-agent-error-patterns.jsonl
# the seven the panel actually killed, and the 51 that nearly died
jq -c 'select(.survives==false) | {name, refuter_count}' $D
jq -c 'select(.refuter_count==1) | .name' $D
# what a lens said already covers this — the field the survival rule ignored
jq -r 'select(.refuter_count>0) | [.name, (.already_covered_by|join(" || "))] | @tsv' $D
# widest first — repo spread is the strongest signal in the set
jq -s 'sort_by(-.repo_count, -.instance_count) | .[:20] | .[] | {name, repo_count, instance_count, fix_family}' $D
# the ones proposing a mechanical check
jq -c 'select(.fix_family=="checker")' $D | head
# the ones an existing trap already covers — i.e. frequency evidence, not new work
jq -c 'select(.maps_to_existing_trap | test("TRAP-0")) | {name, maps_to_existing_trap}' $D
```

**Distribution, `MEASURED` at export:** `checker` 166 · `chain` 41 · `hook` 37 ·
`skill` 20 · `route` 19 · `write` 1. **118 rows are `severity: high` and span
≥3 repositories** — that subset is the obvious place to start, and it is also
where the weak verification hurts most, because breadth was never re-checked.

## Provenance and its limits

Harvested by 986 subagents over 4,583 session cards (20 repos) and 1,592 PR
review comments; method and its defects in
[the retrospective](../2026-08-29-fleet-orchestration-retrospective.md). The
known instrument problems apply to every row: the corpus is **89 % cards / 10 %
other records**, not card-only; the two corpora are **≤5 % contaminated**, so
cross-corpus agreement is not fully independent; and counts are **observed
mentions**, with no deduplication measured.

**`instance_count` is not `instances | length`, and the gap is large.** On 32
rows the array is a cited *sample* of a larger claimed count (row 1: 28 claimed,
16 listed). The count is the lane's tally across its shard; the array is what it
chose to quote. **Only the array is checkable.** Sort by `repo_count` for spread,
but never quote `instance_count` as a verified frequency:

```bash
jq -c 'select(.instance_count != (.instances|length)) | {name, instance_count, listed:(.instances|length)}' $D
```

**`owner_flagged` does not mean the owner flagged it.** The lane that set it
assumed every review comment authored under the `menno420` account was the owner
speaking; the identity-collision finding
([the audit](../2026-08-29-estate-agent-error-audit.md) §1) establishes that
agents post with his PAT, so no GitHub text in this estate is attributable to
him. Every row carrying the key now also carries `owner_flagged_premise: "VOID"`.
Read it as *"authored under the owner account"* and give it no extra weight —
including on the 24 rows where it is `true`, which the synthesis lane ranked
above bot-only patterns on that void premise.

### The census rows have their own limits, and they are different ones

The 20 census rows are a **first pass, one lane per repository, unverified**:

- **One reader each.** No repository was censused twice, so nothing in the set
  is cross-checked. A missed enforcement surface reads exactly like an absent one.
- **Several lanes read a filtered snapshot, not the repository.** Where a row
  carries `scope_notes`, that row's lane never saw the paths it names — `websites`
  is the worst case (no `bootstrap.py`, `scripts/`, `.github/workflows/`,
  `docs/AGENT_ORIENTATION.md`, `docs/SKILLS.md`). **Its `enforcement` list is a
  floor, not an inventory.**
- **Some mechanisms were inferred from documents rather than inspected.** A row
  may name a checker because a README says it exists.

So: read `enforcement` as *"at least this"*, never as a complete inventory, and
do not aggregate the rows into an estate-wide enforcement count without
re-reading the repositories. The audit's own §2 census figures were re-derived
from source for exactly this reason; these rows were their input, not their
evidence.

**Not regenerable.** The scripts in
[`../../../tools/agent_error_audit/`](../../../tools/agent_error_audit/README.md)
rebuild the *corpus*, but re-running the fleet would produce a different
clustering. These rows are the artefact.
