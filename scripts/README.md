# `scripts/` — Repo-side checkers and generators

> **Status:** `reference`
>
> **Tier: TASK** — live; read when your task touches it.
> Where you are in the estate: [the map](../docs/MAP.md).

The one that matters daily is `preflight.py` — the added-card lane, repo
checkers, and owner-comment contract/tests, the same predicate CI's
`substrate-gate` evaluates. Most of the rest are seat-era advisory checkers
whose subjects (roster, lanes, triage register) are retired; their own headers
say so unevenly — see the audit findings before trusting one.

| file | what it is |
|---|---|
| `check_docs_links.py` | Intra-repo markdown link/anchor checker over the living scan set (docs/, projects/, environments/, registry/, templates/, root *.md, cont…. |
| `check_owner_queue.py` | Owner-queue drift checker — **DEAD against the current queue** (2026-08-11, audit D30 + Codex round 2 on fm #849: the 2026-07-21 restructure removed the `## Active` region its parser enters by, so a run parses zero items and exits via its own `[no-items]` FLAG with none of its four checks executed; the module comment says so and the rebuild for the current headings is open work). Was: flags active queue items whose cited PRs already merged/closed, dirty parked PRs, missing/duplicate OQ- slugs. |
| `env-setup.sh` | Kit-planted per-repo environment setup shim implementing the four-rule setup contract: set +e, guarded non-fatal pip installs of requirem…. |
| `gen_roster.py` | The R25 mechanized fleet-roster generator: a hand-maintained LANES registry, verified git-transport heartbeat reads, verdict ladder (FRES…. |
| `preflight.py` | The local-ritual/CI-gate parity script wired in via substrate.config.json preflight_scripts: runs the added-session-card bootstrap lane p…. |
| *…13 more* | see the files themselves — each gist is in [the audit's raw record](../docs/audits/2026-08-10-full-read/raw/gists.tsv). |
