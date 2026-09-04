# Kit prerequisites, what carries over, and the acceptance test (2026-09-01)

> **Status:** `plan` · plan input under OD-26 § 13 — **K1–K5 ARE NOW BUILT
> (kit #590, `8a83c73`, 2026-09-04, unreleased; see the update under the
> table). Everything else here is still plan input.** Written 2026-09-01 by the first Fable 5.1 session on the owner's laptop from a fresh clone at `cb3fc9a`; the owner chose all six defaults the same evening (A–F, see [`../../findings/2026-09-01-owner-direction.md`](../../findings/2026-09-01-owner-direction.md) § 7; four decisions in `docs/decisions.md` dated 2026-09-01). The laptop-hub copy of this folder is `OneDrive\Hub
ecords6-09-01 estate-successor-planning\`.
>

## Substrate-kit must change before `estate` is seeded

Evidence: `creator-kit`, seeded with the kit on 2026-08-25, is what a fresh
adopt produces today. Its tree shows what `estate` would inherit on day one.

| # | What the kit does now | What `estate` needs | Why before the seed |
|---|---|---|---|
| K1 | `adopt` plants `control/` (inbox, status, claims) — the retired seat-era bus | opt-out, or not planted for a hub profile | a dead room with a live name at root on day one |
| K2 | `adopt` plants a generic `docs/` set — creator-kit got 17 files including `seat-digest.md`, `ROUTINES.md`, `helper-policy.md`, `runtime_contracts.md`, `reading-path.md` | a hub profile that plants into the role folders, or plants nothing generic | recreates the `docs/` pile the fresh start exists to escape |
| K3 | `.sessions/` hidden | `sessions/` visible — `sessions_dir` is already a config key | your "no renames" condition; a rename after the archive freezes is expensive |
| K4 | `docs/owner-profile.md` planted per repo with two slots | one pointer line to the hub plus the repo's own two slots | the real fix for the 17 stubs found in file 01 |
| K5 | `.substrate/guard-fires.jsonl` telemetry committed in-tree (24 MB in fleet-manager) | untracked, or rotated with a size cap | `estate` should not be born with a ledger that grows every check |
| K6 | the four-event hook channel exists in 18 of 20 repos and carries no routing, no placement or length checks | routing and the write-time checks in file 04 delivered through `bootstrap.py hook …` | the mechanisms reach every repo, not one of twenty |
| K7 | SessionStart orientation has a section seam (`compose_orientation`; #589 added git-freshness there) | a restate section next to it, the kit-side twin of file 07 | one place, every adopter |
| K8 | `bootstrap.py` at root | accept as a tool-required root | — |

K1–K5 shape the tree at birth and cost renames later, so they belong before
the seed under your no-renames condition. K6–K7 can follow the first cold
test (question E). All of it is plan input; mechanisms wait (OD-26 § 13).

> **UPDATE 2026-09-04 — K1–K5 are BUILT and MERGED, not released.** All five
> landed on substrate-kit `main` as
> [kit #590](https://github.com/menno420/substrate-kit/pull/590),
> squash-merged `8a83c73`, as one reusable **adoption profile** rather than
> five conditionals: `bootstrap.py adopt --profile hub`. Verified against
> `main`'s own artifact after the merge, not from the PR's green. The rows
> above are the requirement as written on 2026-09-01 and are kept verbatim;
> what was actually built, what is proven, and what is deliberately deferred
> (the hub has no skill pack; doctrine prose is reported rather than forked)
> are in [`../../repos/substrate-kit/README.md`](../../repos/substrate-kit/README.md)
> § *Thread: K1–K5*. K6–K7 remain untouched, per the build order.
>
> **The cut did not happen and is not this session's to make.** His
> *"cut when the next fix batch lands"* sequences the charter rewrite and the
> doc-surface sweep first (neither has landed), and `OQ-KIT-V1-21-RELEASE`'s
> adopter half is still open. What waits for that cut, measured rather than
> recalled: kit `main` is **10 commits ahead of the `v1.21.0` tag**
> (`GET /compare/v1.21.0...main`, 2026-09-04) — five records/registry-regen
> commits (#582–#586) and five substantive PRs: #587, #588, #589, #590,
> #591.

## Carry · distill · archive — fleet-manager's living core mapped

The three verbs you agreed on 2026-08-30. "Archive only" means it stays in
fleet-manager, read-only and linkable; nothing is copied.

| fleet-manager today | Verb | Where it lands in `estate` |
|---|---|---|
| `README.md`, `.claude/CLAUDE.md` (28 KB) | distill | `README.md`, `AGENTS.md`, `CLAUDE.md`, each ≤ 80 lines |
| `docs/intent.md` | distill | `practices/how-we-work-here.md`; your § 1–7 quotes → `decisions/owner/` |
| `docs/current-state.md` | distill | `state/estate/now.md`; the shipped log archives |
| consolidation program (161 KB) | split | OD table → `decisions/owner/OD-NN-*.md` · NOW pointer → `state/estate/now.md` · tracks → `plans/{completed,superseded}/` · § 7 ledger → archive |
| roadmap · fresh-start redirect · ChatGPT review | distill | `plans/active/estate-successor/`; originals archive |
| `docs/owner-queue.md` (2,161 lines, live and history in one file) | split | `owner/decisions-needed/{open,answered}/` · `owner/actions-needed/{open,done}/`; history archives |
| `docs/CAPABILITIES.md` (2,136 lines) | split | `state/capabilities/<surface>.md`; the ledger history archives |
| `docs/traps.md` | split | `practices/traps/TRAP-NNN-*.md` with route patterns in the header |
| `docs/decisions.md` | split | `decisions/estate/D-NNNN-*.md` |
| `docs/ESTATE.md` | distill | `repositories/README.md` (generated) + each `repositories/<repo>/README.md` |
| `docs/repos/<repo>/` (10 folders) | carry | `repositories/<repo>/`; `records.md` content → `goals/completed/` and `problems/` |
| `docs/owner-comments/<repo>/` | carry whole | `repositories/<repo>/owner-comments/` |
| `owner/intent-workbooks/` + `tools/gen_owner_index.py` | carry whole | `owner/intent-workbooks/`, `tools/generators/` |
| `docs/providers/*.md` | distill | facts → `state/capabilities/`; recipes → `practices/conventions/` |
| `docs/conventions/` | carry | `practices/conventions/` |
| `docs/activity/` | carry | `sessions/off-repo/` + its generator |
| `docs/ideas/` (19) + the harvested backlog | split | `ideas/{open,promoted,retired}/`, one per file; the S1 harvester writes files, not a table |
| `docs/findings`, `audits`, `research`, `experiments` (≈ 150) | archive only | `evidence/` starts with the few still cited by a live decision: the two error audits, why-rules-dont-bind, error-to-mechanism, the cold reads |
| `.sessions/` (472 cards) | archive only | `sessions/` starts with one cutover card linking the last three |
| `control/`, `telemetry/`, `projects/`, `registry/`, `templates/`, seat-era `docs/prompts/`, `proposals/`, `retro/`, `succession/`, `eap-*`, `MISSION.md`, `fleet-triage.md`, `dispatch-log.md` | archive only | — |
| `.claude/hooks`, skills, `tools/`, `scripts/` | carry, via K6 | `.claude/`, `tools/checks/`, `tools/generators/`, `tools/moves/` |
| `docs/owner-profile.md` | distill | your words → `owner/intent-workbooks/you/`; the rest → `how-we-work-here.md`; satellites get a pointer (K4) |
| `docs/fleet-account-2026-07-26.md`, `owner-reflection-2026-07-21.md` | carry | `evidence/owner-sittings/`, linked, not mandated |

Rough size after the cut: about 250 living files today become perhaps 300
short ones in `estate`, and a thousand stay behind as the archive.

## The acceptance test that gates the cutover

1. **Retrieval, scored:** the five walks in file 03, plus five more you name
   on the day, blind-scored by a separate agent per the § 4.8 method. Pass:
   ≤ 4 doors, no back-outs, no index opened, 9 of 10.
2. **Placement, secondary:** three invented documents filed correctly by a
   cold agent without opening a guide.
3. **Your browse:** you find a named document on GitHub's web view without
   opening `README.md`.
4. **Mechanical:** boot path ≤ 6,000 tokens; R1–R9 green in CI; every checker
   has a fixture that makes it red; the migration manifest has one verb per
   candidate with a verifier's name.

## Recommended order (question E, option 1)

*(Progress marked 2026-09-04; the order itself is unchanged.)*

1. ~~Your letters on A–F~~ — **answered 2026-09-01, all defaults.** The eleven
   names stand.
2. **K1–K5 in substrate-kit — BUILT AND MERGED 2026-09-04 (`8a83c73`); the
   release is NOT cut and is owner-paced.**
3. **← THE NEXT EXECUTABLE STEP.** Write the folder READMEs and the migration
   manifest for the seed set only.
4. Seed `estate` from the manifest; the seed PR is the first session card.
5. Blind cold test; fix what fails; repeat once.
6. Absolute write cutover; fleet-manager's boot file and README get a
   one-paragraph redirect; the GitHub archive flag may lag.
7. K6–K7 and the initiative loop from measured use, not before.

> **Note, same evening:** K6's "so the mechanisms reach every repo" is
> narrowed by the owner's correction in file 04 — hooks in fleet-manager alone
> is deliberate because it is the root of every cloud session. K6 still matters
> for sessions that start with two repos attached, for Codex and ChatGPT Work,
> for local sessions opened in a clone, and for `estate` once it is the root.
