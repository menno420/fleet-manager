# The fleet-wide estate review — every repository, from source

> **Status:** `audit` · 2026-08-21 · fm #878
>
> Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
> This is the evidence record behind [`../ESTATE.md`](../ESTATE.md), the three
> Layer-2 entry points built the same session
> (`repos/superbot-next/` · `repos/substrate-kit/` · `repos/venture-lab/`),
> the doc-route additions, and the owner-queue corrections.

## 1 · Method

The owner directed a fleet-wide review: test fleet-manager's estate model
against the actual estate, not against its own description of it.

- **Enumeration:** the live account list (`list_repos`), 2026-08-21 —
  **26 repositories**, all shallow-cloned locally; per-repo GitHub state
  (metadata, open PRs, last 10 closed PRs, branches) harvested over the
  direct-PAT path minutes before the review ran.
- **Breadth:** 8 parallel family investigators (superbot-core ·
  superbot-satellites · games-live · game-lab · platform · research-verify ·
  ops-web · venture-codetools), each reading its repos' own trees + the
  harvest + fleet-manager's coverage surfaces, returning structured findings
  (identity, canonical docs, state, working contract, relations, aliases,
  FM gaps, recommended treatment) — ~1.2 M tokens of reading, 379 tool calls.
- **Verification before edit:** every claim that drove a fleet-manager edit
  was re-verified by the running session against the tree or the live API;
  the drafted surfaces then went to independent refuters (§ 4). Claims that
  could not be verified were **annotated, not resolved** (the OQ-POKEMON-*
  pair below).

## 2 · What the review established (the short version)

`MEASURED` unless marked. The full per-repo matrix is in
[`../ESTATE.md`](../ESTATE.md)'s rows; the headline results:

1. **The estate had no live enumeration of itself.** No live surface listed
   the account's repositories; `Substrate-kit-app` (a real repo, pushed
   2026-08-04) appeared **nowhere** in fleet-manager outside one audit JSONL,
   and it is an identity trap — its README/CONSTITUTION/docs are
   substrate-kit's **verbatim** (a partial v1.20.2 snapshot under a one-shot
   Gemini dashboard experiment), so everything inside it misidentifies it.
2. **The freshest coverage inverted importance.** The frozen repo (superbot)
   had a same-day Layer-2 entry; the successor half of OD-15's "superbot
   repos" — `superbot-next` — had none: its live truth was scattered across a
   stale RECORD (fleet-account still carrying a dead #602 "owner hold"; both
   carried PRs resolved), a handful of program-ledger rows, and one findings
   file no route reached.
3. **The reference exemplar had gone stale.** `repos/spider-swing/README.md`
   (stamped 2026-08-08) said *"nothing in this thread is agent-executable
   until the owner completes OQ-PLAY-APP-ID and OQ-PLAY-UPLOAD-KEY"* — both
   were completed 2026-08-05: a **signed AAB (vc64) sits on Play's internal
   testing track** under `com.menno420.slingyspider` (spider-swing
   `docs/current-state.md` § "What measurement has settled"). The queue
   carried both as open for 16 days. Build line (0.44.0 → 0.45.0 vc66) and
   the trademark thread ("only unresolved part" → settled-for-launch,
   PR #171) had also drifted.
4. **Owner asks lived outside the queue.** Two genuinely owner-only asks
   existed only inside satellite closeouts — gba's A1/A3 pick + playtest
   verdicts, pml's B/A/Q letter — while the queue held two overtaken asks
   (`OQ-GBA-LUMEN-RELEASE`: published 2026-07-18 — 34 days done;
   `OQ-GBA-ROM-RULESET`: ruleset active with two required contexts, verified
   live — required since at least 2026-08-13 by the program ledger; when the
   contexts were added is not agent-datable).
5. **Routing lagged coverage.** 5 of 6 built folders had doc-routes;
   product-forge (built 2026-08-14) had none — "naming a repo pulls its
   README in" was silently false for the estate's most active product repo.
6. **Registry blind spots:** the kit's scan roster (`docs/fleet-repos.txt`)
   omits `sim-lab` (kit v1.15.0), `superbot-idle` (v1.16.0) and
   `product-forge` (v1.7.0 — the actual oldest adopter, archive-bound
   post-R2) — old kits invisible to any registry-driven rollout, including
   the one `OQ-KIT-V1-21-RELEASE` describes.
7. **Booby traps in satellite docs:** mineverse's coordinator baton tells a
   successor to *delete a trigger* (D‑0015 forbids exactly that) and its
   go-live checklist targets a Railway host deleted 2026-08-20/21;
   superbot-next's closeout claims the repo went "permanently read-only
   2026-07-22" (it merged PRs in August); venture-lab's top closeout threads
   (T+14 kill clock, publish wave) are superseded by OD-11 and the repo has
   zero awareness of it.

## 3 · Refutations that changed the output

Adversarial verification earned its keep — findings the review itself killed
or narrowed before they reached a surface:

- **REFUTED:** an investigator reported superbot **#2058** (mineverse READ
  relay) *"closed unmerged"*. Re-probed: `merged_at 2026-07-14T15:55:34Z` —
  it **merged**. ESTATE.md therefore claims only what held: the WRITE
  executor (#2061) closed unmerged and the web host is gone.
- **UNVERIFIED, recorded as a conflict:** pml's own records claim required
  checks live on `main`; the API refuses to read them — 403 *"Upgrade to
  GitHub Pro or make this repository public"* on both rulesets and classic
  protection (plan-gated for free-plan private repos). Neither record was
  rewritten; both OQ-POKEMON-* entries now carry the conflict and the one
  owner UI-look that settles it.
- **CONFIRMED with a nuance:** "spider-swing is on Play" is internal-track
  only — internal testing buys **zero** progress on the 12-tester closed-test
  clock, so the listing (`OQ-PLAY-LISTING`) remains the critical path; the
  refreshed thread says exactly that rather than "released".

**Round 2 — the drafted surfaces themselves, attacked.** After the edits were
written, four independent refuters re-verified every load-bearing claim in
the new/changed surfaces against the clones, the harvest and the live API:
**116 claims checked — 106 CONFIRMED · 9 PARTIAL · 1 REFUTED**, every PARTIAL
and the REFUTED corrected in place before landing (worklist row count 22→23;
the games hop quote trued to the card's verbatim *"no adopter yet"*; the
upload-key resolution's mechanism restated — the workflow builds *unsigned*
without secrets rather than refusing; "two oldest kits" widened to include
product-forge v1.7.0, the actual oldest, also roster-invisible; the
superbot-next config-seam line gained its ledgered parity-boot exception and
the pytest caveat; venture-lab's "19 rows gated on the proofread" corrected
to ~21 gated, 11 on the proofread).

**Acceptance: 10 cold-start routing tests, 10/10.** Fresh agents with no
estate knowledge, booted on this repo with only an owner-style message
("check the bot" · "continue Couch Legend" · "look at the old rebuild" ·
"review my research tooling" · "check backups" · "work on the GBA project" ·
"the idle game needs balancing" · "publish the books" · "fix the review
site" · "can you release envdrift"), each produced the correct owning
repo(s), the genuine blockers (including OD-11 surfacing as a conflict on
"publish the books", and both venues on "check backups"), the working
contract, and — where the ask was ambiguous — said so instead of guessing.
The answers consistently named `ESTATE.md` as the resolving surface. One
harness note: the envdrift agent's *simulated answer* proposed release
actions and drew a security flag; it performed none (verified live:
0 tags, 0 releases on the lab repo).

## 4 · What changed in fleet-manager, by problem

| problem | fix |
|---|---|
| no estate enumeration | [`../ESTATE.md`](../ESTATE.md) — one routing row per repository (all 26), grouped by state, with aliases, canonical entries, cross-repo edges, and an owner-vocabulary disambiguation list; linked from `README.md`, `MAP.md` and the boot file |
| important repos unroutable | Layer-2 entry points for `superbot-next`, `substrate-kit`, `venture-lab` (the owner-cleared Tier-1 set) + route pairs; repos without folders route to their ESTATE.md rows (10 new route pairs total) |
| stale exemplar + queue | spider-swing folder refreshed; 4 OQ entries resolved-as-overtaken (each verified live first), 2 added, 2 annotated |
| routes lag folders | rule recorded in `repos/README.md` (a built folder ships with its route pair) + the product-forge route added |
| index drift | `scripts/check_estate_index.py` (advisory, selftest 7/7): folder↔row↔route consistency + a visible verified-stamp requirement |

## 5 · Honest nulls and boundaries

- **Layer-2 folders were NOT built for the other recommended repos**
  (superbot-games, superbot-mineverse, gba-homebrew, shiftlife drew
  layer2-readme recommendations from investigators). The owner's on-demand
  doctrine stands (no pre-stubbing, 2026-08-08); their load-bearing warnings
  ride their ESTATE.md rows and routes instead. If work actually goes to one,
  build its folder then.
- **No satellite repo was modified.** Satellite-side staleness found by the
  review (websites' pre-cutover ledger; venture-lab's kit line; superbot-next
  and pml README drift) is recorded in the relevant entry points/rows as
  facts for the next session that touches each repo.
- **The kit's `fleet-repos.txt` hole is recorded, not fixed** — fixing it is
  substrate-kit work; it now rides the substrate-kit entry point's adopter
  thread.
- **The `current-state.md:~487` "Tier 1 filled" stale line stays as the audit
  left it** — a correction was drafted and deliberately reverted: the audit
  record reserves that edit pass for the owner ("this session read and
  reported; the edit pass is the owner's call"), and the boot-read set sits
  exactly at its 7,000-word budget, so the correction was paid for by nothing.
  It remains on the audit worklist.
- **ESTATE.md rows are dated 2026-08-21.** They will drift; the design makes
  that visible (dated stamps + the checker's baseline requirement), and the
  `session-close` Layer-2 handoff step maintains folders, not index rows —
  a session that materially changes a repo's state should touch its row too,
  which the close step's folder update naturally passes through.
- Investigator depth reports (per family, with full evidence chains) lived in
  the session container only; their durable substance is this finding plus
  the surfaces it cites. The structured per-repo matrix survives in
  ESTATE.md; anything not promoted there was judged not worth a permanent
  home this session.
