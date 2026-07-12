<!-- v1 · 2026-07-12 · fleet-manager projects registry — GENERATED COPY, do not edit
     (regenerate: docs/prompts/v3/tools/seat_digest_sync.py --sync; drift guard: --check) -->
<!-- extracted per the substrate-kit machine extraction contract (kit v1.15.0, PR #279 @ dc8aeb1):
     tree scan + fence-prefix match + byte compare — kit code NEVER executed -->
# Fleet Manager — seat digest (registry render, extraction contract)

> **GENERATED COPY — NOT SOURCE OF TRUTH.** Each section below is the fenced
> digest pair extracted VERBATIM from the source repo's committed
> docs/seat-digest.md (itself a kit-derived render of that repo's
> docs/CAPABILITIES.md ledger + skill index — regenerated there, never edited).
> No-third-copy chain (kit grounded-skills plan §4.2e): ledger → seat digest
> (derived render) → this registry render → prompt blocks. A prompt block
> embedding a substrate-kit:*-digest fence must BYTE-MATCH this render
> (enforced by seat_digest_sync.py --check). Fix drift at the source and
> re-run --sync; never edit this file, never merge content back by hand.
> Sources at last sync:
> - menno420/fleet-manager/docs/seat-digest.md · sha256 f6215eeced1d · venues=autonomous-project,any

<!-- registry-header-end -->
## menno420/fleet-manager — docs/seat-digest.md

<!-- substrate-kit:skills-digest BEGIN — derived render, kit-generated; regenerate with `python3 bootstrap.py seat-digest`, never edit. -->
## Skills digest

- `session-close` — Land the session — claim, born-red card first, READY PR, batched work, close-out docs, flip complete last; never…
- `upgrade-distribution` — Roll a kit release out to one adopter repo — download, sha256 three-way, banked rollback, carve-out scan, born-red PR,…
- `release` — Cut + publish a substrate-kit release — version bump PR, workflow_dispatch publish, three-way asset verification,…
- `intake` — Turn a fragmented owner ask into main ideas, a restated fuller picture, a skill-index map, and structured-choice owner…
- `quality-gate` — Run the project's full verification before pushing and report what must be fixed.
- `review` — Review the branch diff against the binding contracts; comment with a verdict and fixes, no edits.
- `repo-health` — Audit doc + session-log hygiene (bootstrap check) and summarize drift.
- `deep-research` — Fan out web research, adversarially verify sources, and synthesize a cited report.
- `question` — Answer a direct question concisely from memory and source; make no changes.
- `analysis` — Read-only deep-dive: investigate and report findings without changing anything.

Full index (grounds + capabilities): `docs/SKILLS.md` — the source this block derives from.
<!-- substrate-kit:skills-digest END -->

<!-- substrate-kit:walls-digest BEGIN venues=autonomous-project,any — derived render, kit-generated; regenerate with `python3 bootstrap.py seat-digest`, never edit. -->
## Walls digest (venues: autonomous-project, any)

- `any` · **Tag push / release create via git**: HTTP 403 from the environment's git proxy → use the workflow_dispatch release path.
- `any` · **Branch deletion**: 403 on every path (git push `:branch` and API) → owner deletes by hand / enables "Automatically delete head branches".
- `any` · **`api.github.com` direct HTTP**: blocked → GitHub access is MCP-tools-only.
- `any` · **Environment / Project creation**: owner-click actions in the console — queue them as structured owner asks, never wait silently. Routine/schedule creation…
- `any` · **GraphQL API quota**: tight — batch queries and prefer the REST-backed MCP tools for bulk reads.

Full ledger (all venues, evidence, freshness): `docs/CAPABILITIES.md` — the seat-local source of truth; append findings THERE, never here.
<!-- substrate-kit:walls-digest END -->
