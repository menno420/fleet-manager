# § 4.8 fresh-scorer half — raw record

> **Status:** `reference` · 2026-08-13 · evidence folder for
> [`../2026-08-13-intent-map-fresh-scorer.md`](../2026-08-13-intent-map-fresh-scorer.md).
> Everything here is either verbatim (scorer outputs, the handed rubric, the
> prompt template) or a probe record. Read the finding first; this folder
> exists so its claims can be re-derived.

## Inventory

| file | what it is |
|---|---|
| [`rubric-handed.md`](rubric-handed.md) | The redacted §§ 1–2 design-and-rubric text handed to both scorers, verbatim below its provenance wrapper |
| [`scorer-prompt.md`](scorer-prompt.md) | The scorer prompt template, verbatim with the per-sandbox path generalised to `{SANDBOX}` |
| [`leak-probes.md`](leak-probes.md) | The isolation probe record: the mechanical grep, the measured boot-file snapshot leak, the failed neutralization, the sandbox-rooted CLI pivot, the route-doc audit, the stated residual |
| [`scorer-1.md`](scorer-1.md) / [`scorer-2.md`](scorer-2.md) | The two blind scorers' full reports, verbatim (committed when the runs completed) |
| `citations-s1-*.tsv` / `citations-s2-*.tsv` | Each scorer's own citation rows, exactly as run against the pinned trees |

Reproduce the snapshots: `git archive 7fbc065 | tar -x -C pinA` and
`git archive f53d7ea | tar -x -C pinB`. Re-run a scorer's rows:
`python3 ../2026-08-12-intent-map-fresh-agent-test/verify_citations.py <pin-dir> <tsv>`
(the checker is the committed fm #851 one, reused unchanged).
