# Fleet-wide PR-Landing Audit — 2026-07-16

> **Status:** `audit`
>
> Point-in-time audit of PR auto-landing across all 19 fleet repos, taken
> 2026-07-16 ~15:21 UTC. Source files and live GitHub win over this snapshot.
> Companion to fm ORDER 048. **NOT SOURCE OF TRUTH** — a dated readout.

## Executive summary (plain language)

1. **Every one of the 19 fleet repos has a working auto-landing workflow at HEAD.** fm ORDER 048's four suspected-missing repos — superbot-next, superbot-games, gba-homebrew, pokemon-mod-lab — were each verified to HAVE one. Nothing is missing infrastructure.
2. **Merges are NOT random.** ~259 PRs merged across the fleet in the last 48h; ~250 landed **automatically**. Merge *order* = each PR's own CI-completion time on its all-green head SHA — not a queue. A PR opened later can land earlier simply because its checks finished first. That is the entire "randomness."
3. **Only ~9 merges in 48h were human clicks, and every one is explainable:** 7 were the auto-merge-workflow *install* PRs themselves (workflow-file diffs are owner-merge-only by design), 1 was a pre-automation merge, and 1 was an owner-live manual order (superbot-next #497). No unexplained manual merges.
4. **Only 2 PRs are genuinely stuck** (green but not landing, needing a human hand): **websites #359** — a non-draft data bake, checks green, but auto-merge failed to arm (mergeable_state `blocked`) while sibling bakes auto-landed → needs one manual merge; and **pokemon-mod-lab #87** — checks green but a real merge conflict (`dirty`) → needs a rebase or an owner close.
5. **One systemic pattern, working as designed, is the main source of "why won't this merge":** ~13 open PRs are **deliberate drafts**. Many are sessions honestly parking their PR because the auto-mode classifier denied the autonomous ready-flip/merge shape (`[Merge Without Review]` / `[Auto Mode Bypass]`). Several are green-and-ready and just need an owner one-click (gba-homebrew #153, superbot-idle #145, superbot-games #149). A `merged_by` caveat: **superbot & substrate-kit auto-merges record `menno420` as the merger** (their auto-merge is armed with the owner's PAT), so a `menno420` login there does NOT mean a manual click.

## Summary table

| Repo | Landing workflow | Open PRs | Stuck PRs | Auto-merges 48h | Manual merges 48h |
|---|---|---|---|---|---|
| superbot | auto-merge-enabler.yml (native) | 1 | 0 | ~24 * | 0 |
| substrate-kit | auto-merge-enabler.yml (native) | 1 | 0 | ~30 * | 0 |
| websites | auto-merge-enabler.yml (native) | 9 | **1 (#359)** | 22 | 0 |
| superbot-next | auto-merge-enabler.yml (native) | 5 | 0 | 24 | 1 (#497 owner-live) |
| trading-strategy | auto-merge-enabler.yml (native) | 0 | 0 | 10 | 0 |
| superbot-games | auto-merge-enabler.yml + card-guard | 1 | 0 | 8 | 0 |
| codetool-lab-opus4.8 | merge-on-green.yml (REST) | 0 | 0 | 1 | 1 (#24 install) |
| codetool-lab-sonnet5 | merge-on-green.yml (REST) | 0 | 0 | 1 | 1 (#19 install) |
| codetool-lab-fable5 | merge-on-green.yml (REST) | 0 | 0 | 1 | 2 (#16 pre-auto, #17 install) |
| fleet-manager | merge-on-green.yml (REST) | 0 | 0 | 26 | 1 (#227 workflow-file) |
| pokemon-mod-lab | merge-on-green.yml (REST) | 1 | **1 (#87 conflict)** | 5 | 1 (#89 install) |
| venture-lab | auto-merge-enabler.yml (native) | 0 | 0 | 12 | 0 |
| gba-homebrew | auto-merge-enabler.yml (native) | 3 | 0 | 16 | 0 |
| product-forge | merge-on-green.yml (REST) | 0 | 0 | 1 | 1 (#25 install) |
| idea-engine | auto-merge-enabler.yml (native) | 1 | 0 | 25 | 0 |
| sim-lab | auto-merge-enabler.yml (native) | 0 | 0 | 24 | 0 |
| superbot-plugin-hello | merge-on-green.yml (inert — no CI) | 0 | 0 | 0 | 1 (#3 install) |
| superbot-mineverse | auto-merge-enabler.yml (native) | 0 | 0 | 8 | 0 |
| superbot-idle | auto-merge-enabler.yml + card-guard | 1 | 0 | 12 | 0 |
| **TOTAL** | **19/19 have one** | **24** | **2** | **~250** | **~9** |

\* superbot & substrate-kit arm native auto-merge with the owner's PAT, so their automatic merges record `merged_by: menno420` rather than `github-actions[bot]`. Counted as automatic (proven: superbot #2122, an automated dashboard bake, records `menno420`).

## Two landing mechanisms in the fleet

- **`auto-merge-enabler.yml` (GitHub-native auto-merge)** — arms native auto-merge on non-draft `claude/*` PRs; GitHub lands them the instant required checks pass. Used by: superbot, substrate-kit, websites, superbot-next, trading-strategy, superbot-games (+card-guard), venture-lab, gba-homebrew, idea-engine, sim-lab, superbot-mineverse, superbot-idle (+card-guard).
- **`merge-on-green.yml` (REST verify-then-squash sweep)** — a workflow that sweeps READY `claude/*` PRs on events + cron, verifies every head-SHA check green, then squash-merges via REST. Carve-outs: `do-not-automerge`/`owner-held` labels + any `.github/workflows/**` diff = owner-merge-only. Used by: codetool-lab-{opus4.8,sonnet5,fable5}, fleet-manager, pokemon-mod-lab, product-forge, superbot-plugin-hello (installed 2026-07-15).

## What does NOT auto-merge (by design)

1. **Draft PRs** — never arm auto-merge. Biggest open bucket; mostly the classifier-denial park pattern.
2. **`.github/workflows/**` diffs** — owner-merge-only in the merge-on-green repos (the workflow refuses to merge PRs that touch workflows). The native-enabler repos vary: venture-lab auto-landed a workflow-touching PR (#207); superbot-games/superbot-idle add a card-guard that can disarm.
3. **`do-not-automerge` / `owner-held` labels** — explicit owner carve-out (e.g. websites #345, superbot-games #149).
4. **Born-red session cards** — a `.sessions/*.md` with `> Status: in-progress` reds the substrate-gate and holds the merge until the session flips it to `complete`. Working as intended, not stuck (e.g. substrate-kit #430, idea-engine #456 in-flight).
5. **Merge conflicts** — a `dirty` PR can't be squashed (pokemon-mod-lab #87).

## Per-repo detail (open-PR diagnoses)

### superbot — enabler (native), gate = code-quality
- **#2061** mineverse FLAG 2 HMAC WRITE endpoint — draft, created 07-13. **[draft — never auto-merges]**, held deliberately ("merge = deploy; owner flips ready"). Not stuck.
- 48h: 24 merges, overwhelmingly automated dashboard bakes; PAT-armed auto-merge records `menno420`. Healthy.

### substrate-kit — enabler (native), gate = kit-quality
- **#430** registry-refresh — created 07-16 15:18, `kit-quality` (+2 aliases) failure. **[checks red — born-red session-card hold, BY DESIGN]** (job log verbatim confirms the born-red HOLD). auto-merge armed; lands when the card flips. Working as intended.
- 48h: 30 merges, dense autonomous close-out stream. Healthy.

### websites — enabler (native), gate = quality — 9 open
- **#370, #369, #368, #357** owner-console/arcade drafts — **[draft]**, bodies say no ready-flip requested (#357: ready-flip blocked by GitHub API rate-limit; owner one-click to ready).
- **#367, #363, #361** rescue straggler cards — **[draft]** on purpose, owner picks canonical (#361 also has unresolved `[[fill:]]` slots = would born-red).
- **#345** quality-main-sweep — **[owner-label carve-out]** `do-not-automerge` + workflow-file diff.
- **#359** [bake] fleet data refresh — non-draft, `quality` = success, no card, yet `mergeable_state: blocked`, open ~8h while sibling bake #343 auto-landed. **[other: auto-merge failed to arm — the "waits for a human hand" fallback]. GENUINELY STUCK — recommend owner merge #359 by hand (or re-arm).**
- 48h: 22 merges via `github-actions[bot]`.

### superbot-next — enabler (native), 15 named gates — 5 open
- **#503, #500, #499** — **[draft]** by design, "owner lands / flip of the card releases the path"; bodies document `[Auto Mode Bypass]` / `[Merge Without Review]` denials that forced draft.
- **#485, #484** lane→manager outbox notes — **[other: informational parked, no auto-merge requested]**; #484 head SHA = all 15 checks green, `enable-auto-merge` skipped for `lane/*`. Held open on purpose.
- 48h: 25 merges, mostly bot; **#497 genuinely manual** (owner-live merge-queue order, `do-not-automerge` labels lifted per live instruction). Healthy but owner-gated.

### trading-strategy — enabler (native)
- 0 open. 48h: 10/10 automatic. Healthy.

### superbot-games — enabler + card-guard (native)
- **#149** mirror reconcile-race fix — draft, `do-not-automerge` label, workflow-file diff, checks green, `clean`. **[draft — never auto-merges]** stacked with two more intentional holds. Held-by-design, not stuck.
- 48h: 8/8 automatic. Healthy.

### codetool-lab-opus4.8 / sonnet5 / fable5 — merge-on-green (REST)
- 0 open each. Manual merges are the workflow-install PRs (opus #24, sonnet #19, fable #17) + fable #16 (pre-automation); each install was immediately proven by an auto-landed probe (#25/#18/#18). Healthy.

### fleet-manager — merge-on-green (REST) — CONFIRMED
- 0 open. 48h: 27 merges, **26 automatic** (roster-regen bot generations #61–#70 + wake/oversight sessions), **1 manual #227** (touched `roster-regen.yml` → workflow-file carve-out). Healthy and dominant automation.

### pokemon-mod-lab — merge-on-green (REST)
- **#87** seat-dormant shutdown doc — non-draft, `substrate-gate` + `ROM builds` both green, but **`mergeable_state: dirty`**. **[merge conflict] — GENUINELY STUCK.** Base advanced via #88/#90–#93 which rewrote the same `control/status.md`. Needs merge-main-in or an owner dormancy-vs-reboot close.
- 48h: 6 merges (5 bot + #89 install manual). Otherwise healthy.

### venture-lab — enabler (native)
- 0 open. 48h: 12/12 automatic — including workflow-touching #207 (native enabler has no workflow-file carve-out). Healthy.

### gba-homebrew — enabler (native), required check = "ROM builds" — 3 open, all draft
- **#153** gate-orphan-fix — ALL checks green incl. substrate-gate, card flipped complete; repairs main's substrate-gate orphan red. **[draft — never auto-merges]** — green-and-ready, blocked only by draft. Needs an owner ready-click.
- **#155** underroot slice-1 — substrate-gate ❌ = inherited #151 orphan red (would be fixed by #153); own card complete; "ROM builds" green. **[draft]**.
- **#154** denial-triage — substrate-gate ❌ = born-red-by-design (card left in-progress) + inherited orphan; "ROM builds" green. **[draft]**.
- Root cause: the auto-mode classifier denies the autonomous ready-flip/merge shape on this repo (`[Merge Without Review]` quoted in #154), so sessions honestly park draft. 48h: 16/16 prior merges automatic — auto-landing itself works.

### product-forge — merge-on-green (REST)
- 0 open. 48h: #26 probe auto-landed, #25 install manual (workflow-file, owner-merge-only). Healthy.

### idea-engine — enabler (native)
- **#456** PROPOSAL 084 — opened 15:21 (audit minute), substrate-gate + enable-auto-merge both `in_progress`. **[checks pending]** — healthy in-flight, lands on green when the card flips.
- 48h: 25/25 automatic. Healthy.

### sim-lab — enabler (native)
- 0 open. 48h: 24/24 automatic. Healthy.

### superbot-plugin-hello — merge-on-green (REST, INERT)
- 0 open. Landing workflow installed (#3, owner-merged as a workflow-file PR) but the repo has **no check-producing CI**, so the sweep treats "zero checks = not verified" and merges nothing until CI exists. Mechanism present but currently inert.

### superbot-mineverse — enabler (native)
- 0 open. 48h: 8/8 automatic (incl. workflow-touching kit upgrade #112 that kept live workflows byte-identical). Healthy.

### superbot-idle — enabler + card-guard (native)
- **#145** control stale-claims sweep — draft, control/**-only, all checks green, `clean`. **[draft — never auto-merges]** — green-and-ready; authoring session left it draft after a harness merge denial. Needs an owner ready-flip.
- 48h: 12/12 automatic (incl. workflow-touching #137 after its born-red card flipped). Healthy.

## Recommended owner actions

1. **websites #359** — merge by hand (or re-arm auto-merge); it's a green data bake that missed its auto-merge arm.
2. **pokemon-mod-lab #87** — resolve the conflict (merge main in) or close it per the dormancy decision.
3. **The green-and-ready drafts** — one-click ready-flip to land: gba-homebrew #153 (repairs main's gate red), superbot-idle #145, superbot-games #149. These are the classifier-denial parks; nothing is wrong with them.

_Audit method: read-only via github MCP (list_pull_requests + head-SHA check runs + `merged_by` on merged PRs) across all 19 repos; direct GitHub REST is walled for these sessions, so all evidence is MCP-sourced. High-volume repos (superbot, substrate-kit, idea-engine, sim-lab) had `merged_by` sampled on a representative spread, not exhaustively — no exceptions found. No rate-limiting hit._
