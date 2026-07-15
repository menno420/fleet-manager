# Merge-on-green rollout verification — 19-repo sweep (2026-07-15)

> **Status:** `audit`
>
> Read-only verification of the fleet's merge automation at every repo's
> main@HEAD, run 2026-07-15T14:00–14:10Z (wall clock `date -u` =
> 14:00:49–14:01:19Z at worker start) by four read-only sweep workers
> (raw.githubusercontent.com + GitHub MCP; private pokemon-mod-lab via MCP
> Contents API). Every claim below is cited from those sweeps — file blob/
> commit SHA, PR number, ISO merge timestamp, merged_by. Recorded by the
> wake-0715c working session (fm PR #233). Verify against live repos before
> acting (playbook R2 / Q-0120).

**Headline: 13/19 PROVEN · 5/19 INSTALLER-PR-OPEN · 1/19 MISSING.** The 13
proven repos each carry a same-day (2026-07-15) bot-attributed merge — or,
for superbot, its deliberate PAT attribution — via the OLDER
`auto-merge-enabler.yml` mechanism (installed 2026-06-13…2026-07-14) or
fleet-manager's own `merge-on-green.yml` (PR #146, 2026-07-13). **Today's
13:41–13:57Z rollout wave landed nothing on any main**: all five installer
PRs self-parked on the very workflow-file owner-merge-only rail they install.

## Per-repo table (mechanism measured at main@HEAD, 14:0xZ)

| Repo | Mechanism at main@HEAD (file + SHA + install date/PR) | Gates on | Evidence (PR #, merged_at, merged_by) | Verdict | Notes |
|---|---|---|---|---|---|
| superbot | `auto-merge-enabler.yml` blob `6897fac` @ main `3fb5dd0`; last commit `14c550b` 2026-06-22 (#1319) | head `claude/*`, non-draft, no `do-not-automerge`; arms `gh pr merge --auto --merge` via ROUTINE_PAT; required check **Code Quality** | #2111 merged 2026-07-15T12:54:47Z, merged_by **menno420** (by-design PAT attribution); enabler run 29416330051 success 12:43:42Z | **PROVEN** | PAT attribution deliberate (keeps reconciliation-trigger firing); merged_by never shows the bot here. `bot/*` heads (#2108/#2109) outside allowlist — enabler runs `skipped` |
| superbot-next | `auto-merge-enabler.yml` blob `e01634c` @ main `454ec71`; installed `e9f1cd5` 2026-07-13 (#321, fm ORDER 029) | 6-prefix allowlist (`claude/ port/ mining/ test/ docs/ fix/`); session-card in-progress skip; squash-arm; required named gates | #489 merged 2026-07-15T03:41:00Z, merged_by **github-actions[bot]** | **PROVEN** | Allowlist holes real: #491/#492 (heads `band5-*`) merged manually by menno420 10:36–10:40Z |
| substrate-kit | `auto-merge-enabler.yml` blob `05e93ec` @ main `b958bfd`; last commit `18e5adc` 2026-07-12 (#300) + `auto-merge-disarm.yml` | heads `claude/*`+`claim/*`; 0-required-contexts refusal; fresh label re-read; squash-arm; required **kit-quality** | #393 (probe) merged 2026-07-15T14:02:37Z, merged_by **github-actions[bot]** | **PROVEN** | Probe PR created 13:59:03Z explicitly to prove zero-click landing |
| websites | `auto-merge-enabler.yml` blob `d60ed77` @ main `68df965` (kit v1.15.0, `43988f4` 2026-07-12, #199) + `host-automerge-extras.yml` blob `0e2fa27` | enabler `claude/*` + required **quality**; extras add cron `13,43 * * * *` sweep, direct-squash fallback, workflow-diff park rail | #351 (probe) merged 2026-07-15T14:03:26Z, merged_by **github-actions[bot]** | **PROVEN** | fm's merge-on-green.yml cites websites `host-automerge-extras.yml @ 0aeb803f` as its model |
| sim-lab | `auto-merge-enabler.yml` blob `3f79c7e` @ main `e26996b`; kit v1.15.0 `daf00da` 2026-07-13 (#115) | 11-prefix allowlist via `substrate.config.json`; required **substrate-gate** | #158 merged 2026-07-15T12:06:25Z, merged_by **github-actions[bot]** (also #154–#157 same-day, 09:53–11:35Z) | **PROVEN** | Highest-volume same-day evidence |
| idea-engine | `auto-merge-enabler.yml` blob `819a8d5` @ main `828b18e`; last commit `daf9d50` 2026-07-12 (#272) | 14-prefix allowlist; session-card skip; required **substrate-gate** | #440 merged 2026-07-15T11:37:34Z, merged_by **github-actions[bot]** (merged_by verified via API) | **PROVEN** | #434→#440 chain: each session verifies its predecessor's bot merge |
| gba-homebrew | `auto-merge-enabler.yml` blob `67c333b` @ main `0048a5d`; commit `0e08695` 2026-07-13 (#76, fm ORDER 029) | head `claude/*`; 3-source required-contexts lookup (required **ROM builds**, classic protection); session-card skip | #147 merged 2026-07-15T11:01:27Z, merged_by **github-actions[bot]** (also #142–#146) | **PROVEN** | Host-adapted copy of idea-engine@`819a8d5` |
| venture-lab | `auto-merge-enabler.yml` blob `9feb8bc` @ main `520bdfc`; commit `305646f` 2026-07-11 (#59) | head `claude/*`; 0-contexts refusal (rulesets); required **substrate-gate** | #203 merged 2026-07-15T04:10:06Z, merged_by **github-actions[bot]** | **PROVEN** | Kit-generated template; born-red hold enforced by substrate-gate itself |
| superbot-games | `auto-merge-enabler.yml` blob `f387896` @ main `446a84e`; installed `dd867c8` 2026-07-13 (#67), last `8c9c320` 2026-07-14 (#142) + `automerge-card-guard.yml` blob `72f1a8e` | 17-prefix allowlist; card-guard disarms on in-progress cards; required **substrate-gate** | #145 merged 2026-07-15T03:38:31Z, merged_by **github-actions[bot]** | **PROVEN** | Guard split into separate host workflow (mirror of idle #137) |
| superbot-mineverse | `auto-merge-enabler.yml` blob `9feb8bc` @ main `b9ade33` (byte-identical to venture-lab's); seeded `d1d8c9f` 2026-07-11 (kit v1.8.0) | head `claude/*`; required **substrate-gate + pytest** (per PR #110/#112 bodies) | #113 merged 2026-07-15T03:40:12Z, merged_by **github-actions[bot]** | **PROVEN** | Present since repo seed; never modified |
| superbot-idle | `auto-merge-enabler.yml` blob `c5449a5` @ main `8a7275d`; last `8ff9f59` 2026-07-14 (#137) + `automerge-card-guard.yml` blob `cd8848f` | allowlist `claim/ claude/ close-out/ control/`; required **substrate-gate + theme-gate** (per PR #134 body) | #139 merged 2026-07-15T03:38:40Z, merged_by **github-actions[bot]** | **PROVEN** | Same guard-split pattern as games |
| trading-strategy | `auto-merge-enabler.yml` blob `9feb8bc` @ main `458b43c`; commit `bf885f0` 2026-07-12 (#65) | head `claude/*`; 0-contexts refusal; required **substrate-gate**; needs owner "Allow auto-merge" setting — evidently ON | #128 merged 2026-07-15T03:38:26Z, merged_by **github-actions[bot]** (also #126, 07-14T20:53:11Z) | **PROVEN** | Resolves owner-queue B#8 (OQ-TRADING-ALLOW-AUTOMERGE) — see queue sweep |
| fleet-manager | `merge-on-green.yml` blob `8671d8c` @ main `eb7fec0`; added `f0e3d65` 2026-07-13 (#146) | REST verify-then-squash sweep: check_suite/PR events + workflow_run + cron `7,37 * * * *`; head `claude/*`; all check runs green; `do-not-automerge`/`owner-held` + workflow-diff + in-progress-card skips; `--match-head-commit` race guard | #232 merged 2026-07-15T13:00:15Z, merged_by **github-actions[bot]** (also #228/#229/#230, 10:21–11:56Z) | **PROVEN** | The fleet's only true merge-on-green.yml at a main; GitHub-native auto-merge unavailable on this repo/plan per the file header |
| codetool-lab-opus4.8 | none @ main `0e0ec02` (only ci.yml `e345d36`, release.yml `d76bf91`) | (per open PR #24: REST sweep, no single required-check name — 5-cell CI matrix) | none — no bot-merged PR ever | **INSTALLER-PR-OPEN** | PR #24 opened 2026-07-15T13:44:19Z (head `claude/install-merge-on-green` @ `342f793`), self-parked owner-merge-only |
| codetool-lab-sonnet5 | none @ main `0331176` (only ci.yml `4f8941a`, release.yml `9f0cc33`) | n/a | latest merge #17 2026-07-14T07:07:03Z by **menno420** (manual) | **MISSING** | **Rollout skipped this repo** — 0 open PRs, no installer PR at 14:04Z; wind-down/archive candidate (B#41; own #16/#17 bodies) |
| codetool-lab-fable5 | none @ main `3f83cbb` (only ci.yml `cdefd44`) | (per open PR #17: cron+event sweep, no branch-prefix filter, no card skip) | none | **INSTALLER-PR-OPEN** | PR #17 opened 2026-07-15T13:49:04Z (head `ci/merge-on-green-automation` @ `b37b3ca`), self-parked owner-merge-only |
| product-forge | none @ main `f7f2dd2` (deploy-pages `8ae52b3`, heartbeat-guard `ee50f43`, substrate-gate `2123e26` — gate only, never merges) | (per open PR #25: sweep any same-repo non-draft PR→main; card skip kept) | none | **INSTALLER-PR-OPEN** | PR #25 opened 2026-07-15T13:56:45Z (head `ci/merge-on-green` @ `78ff3bc`); its body cites its motivating gap: #24 sat green 7+ h before manual merge |
| pokemon-mod-lab (private) | none @ main `7d4fa41` (rom-builds `441abe1`, substrate-gate `a354a27` — gate only) | (per open PR #89: fm port @ `8671d8c`, workflow_run `[substrate-gate, rom-builds]`, card skip kept) | none — #87 (07-14T21:15Z) + #88 (07-15T04:00Z) sit open awaiting owner click | **INSTALLER-PR-OPEN** | PR #89 opened 2026-07-15T13:56:05Z (head `claude/install-merge-on-green` @ `9e49a1e`), self-parked owner-merge-only; MCP reads worked, no access wall |
| superbot-plugin-hello | none — no `.github/` directory at all @ main `5d97aa7` | (per open PR #3: fm-modeled REST sweep @ `eb7fec0` base) | no bot merge ever: #2 merged 07-14T14:20:55Z by **menno420**; #1 hand-merged 07-14T07:06:54Z (zero check runs on either head) | **INSTALLER-PR-OPEN** | PR #3 opened 2026-07-15T13:41:30Z, self-parked. **Inert even if merged**: repo has zero CI, and the sweep treats zero check runs as NOT-ready by design |

## Headline count

**13 PROVEN** (superbot · superbot-next · substrate-kit · websites · sim-lab
· idea-engine · gba-homebrew · venture-lab · superbot-games ·
superbot-mineverse · superbot-idle · trading-strategy · fleet-manager) ·
**5 INSTALLER-PR-OPEN** (codetool-lab-opus4.8 #24 · codetool-lab-fable5 #17
· product-forge #25 · pokemon-mod-lab #89 · superbot-plugin-hello #3) ·
**1 MISSING** (codetool-lab-sonnet5 — rollout skipped it; wind-down/archive
candidate B#41).

## Today's rollout — what actually happened

The five installer PRs opened 13:41:30–13:56:45Z (plugin-hello #3 →
opus4.8 #24 → fable5 #17 → pokemon-mod-lab #89 → product-forge #25). Each
ports the fleet-manager `merge-on-green.yml` REST-sweep shape (fm blob
`8671d8c`), each adapts gates to its host (opus4.8 drops the single
required-check assumption for its 5-cell CI matrix; fable5 drops the
branch-prefix filter and card skip; pml wires `workflow_run` to
`[substrate-gate, rom-builds]`), and **each self-parked on the
workflow-file owner-merge-only rail it installs** — a PR whose diff touches
`.github/workflows/**` is exactly what these workflows refuse to land.
**Nothing landed on any main today.** The 13 proven repos owe their merges
to the older enabler mechanism (installed 2026-06-13…07-14) or fm's #146
file, not to this wave. superbot #2111 (merged 12:54:47Z) was a routine
enabler-armed merge on an ordinary `claude/*` head — not an install.

## Cross-cutting gaps

1. **superbot PAT attribution** — the enabler deliberately merges via
   ROUTINE_PAT so merged_by reads menno420, never github-actions[bot] (file
   comments: keeps `reconciliation-trigger.yml` on-push firing). Bot-merge
   evidence there must be read from enabler runs + timing, not merged_by.
2. **Branch-prefix allowlist holes** — superbot-next #491/#492 (heads
   `band5-*`, outside its 6-prefix list) were merged manually by menno420
   within ~3 min; superbot `bot/*` heads (#2108/#2109) skipped the enabler
   entirely. Real PRs ride unarmed and manual merges paper over the hole.
3. **plugin-hello inert-without-CI** — even after PR #3 merges, the sweep
   never fires usefully: zero check runs = NOT-ready by deliberate design,
   and the repo has no CI workflow at all. The install needs a paired
   minimal CI gate or it is a no-op.
4. **sonnet5 skipped** — the one repo with no automation got no installer
   PR; consistent with its ARCHIVE verdict but undocumented at rollout time.
5. **fm #227 conflict-dirty despite green checks** — the roster-regen cron
   (PR #231, Gen #59, 12:04Z) advanced main past #227's 09:16Z base;
   `mergeable_state` now `dirty`, so the owner-queue A#63 "one merge click"
   fails until a session merges main in and regenerates. Checks on the old
   head are still green — green checks do not imply mergeable.

## Method

Four parallel read-only workers, 14:00–14:10Z: raw.githubusercontent.com
file fetches (404 = file-absent, cross-confirmed via MCP directory
listings), GitHub MCP `get_file_contents` / `list_pull_requests` /
`pull_request_read` / `list_commits` / `actions_list`, `git ls-remote` for
main@HEAD SHAs. pokemon-mod-lab (private, raw-walled) read via MCP only —
no access wall hit. No writes to any repo. Sweep transcripts live in the
dispatching session; this doc is the committed distillation.
