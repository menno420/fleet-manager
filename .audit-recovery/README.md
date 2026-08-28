# Recovery artifact — the OD-24 estate agent-error audit (transient)

Written 2026-08-28 while the audit was paused for a usage-limit reset. **This
directory is transient**: it exists so a reclaimed container cannot destroy work
already paid for, and the audit's own PR deletes it before merge.

`recovery.tar.gz` contains:

- `harvest-cache.json` — 226 completed subagent results (2,188 card-corpus
  incidents · 687 review-corpus incidents · 284 candidate patterns · 20 per-repo
  instruction censuses), zero empty.
- The five scripts that regenerate the whole evidence corpus from the GitHub API
  in about two minutes: `census.py`, `fetch.sh`, `extract.py`, `shard.py`,
  `reviews.py`, plus `census.json` and `coverage-brief.md`.

Restore with `tar -xzf recovery.tar.gz`.

Corpus it indexes: 4,583 session cards across 20 repositories (2026-05-29 →
2026-08-28) yielding 7,214 error-bearing sections, plus 1,592 pull-request review
comments (1,431 external reviewer findings, 155 written by the owner himself).
