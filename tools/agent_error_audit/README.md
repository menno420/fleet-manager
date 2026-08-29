# The agent-error audit toolchain (2026-08-29)

Regenerates the evidence corpus behind
[`docs/findings/2026-08-29-estate-agent-error-audit.md`](../../docs/findings/2026-08-29-estate-agent-error-audit.md)
from the GitHub API. Retained because that finding claims re-derivability and
§8 recommends re-measuring proposed routes against the corpus — a claim with no
runnable inputs is the defect the finding itself catalogues (Codex, fm #967).

Run in order; each needs `$GITHUB_PAT` over **direct egress** (a
`ProxyHandler({})` opener — the proxied REST path 403s):

| script | produces |
|---|---|
| `census.py` | `repos.json`, `census.json` — per-repo card/finding counts |
| `fetch.sh` | `corpus/<repo>/` — API tarballs, filtered to records |
| `extract.py` | `evidence.jsonl` — error-bearing sections (walks dot-dirs; `glob` does not) |
| `shard.py` | `shards/` — lane-sized evidence files |
| `reviews.py` | `review_comments.json` — PR review comments across **every** repo in `repos.json` (it enumerates rather than hard-coding, so a re-run reproduces exhaustiveness as well as the corpus) |

`adopter_census.json` is the measured per-repo routing/hook-channel table behind
§4, one row per repo: `(repo, doc-routes.json, route_docs.py,
.substrate/hooks/settings.template.json, .claude/settings.json)`.

**Not a supported tool.** Single-purpose scripts kept as audit inputs; no tests,
no gate coverage.
