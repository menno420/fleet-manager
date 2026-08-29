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
| `2026-08-29-agent-error-patterns.jsonl` | **284** | a candidate recurring agent-error pattern: `name`, `one_line`, `trigger` (hook-firable moment), `instances` (cites), `repos`, `instance_count`, `repo_count`, `gap_class`, `fix_family`, `proposed_fix`, `maps_to_existing_trap`, `severity` |
| `2026-08-29-repo-instruction-census.jsonl` | **20** | one repository's agent-instruction surface: what it `instructs`, what `enforcement` exists and of what kind, its `prose_only_rules`, `divergences_from_kit`, `biggest_gap`, `portable_lesson` |

## How to read them, and how not to

**These are candidates, not findings.** The audit's §3 records that the
adversarial panel rejected 7 of 284 — a 97.5 % pass rate, which is a bar nothing
fails. **A row here has survived almost nothing.** Its `instances` are real
citations and its counts are observed mention counts, but the *pattern* is one
lane's clustering, not a verified claim.

Useful cuts, all mechanical:

```bash
D=docs/findings/data/2026-08-29-agent-error-patterns.jsonl
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

**Not regenerable.** The scripts in
[`../../../tools/agent_error_audit/`](../../../tools/agent_error_audit/README.md)
rebuild the *corpus*, but re-running the fleet would produce a different
clustering. These rows are the artefact.
