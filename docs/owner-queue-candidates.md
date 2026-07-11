# Owner-queue candidate feed — GENERATED

> **Status:** `living-ledger`
>
> **GENERATED — NOT SOURCE OF TRUTH; the manager curates `docs/owner-queue.md` from it.** Do not hand-edit; regenerated with the roster on every regen (`scripts/gen_roster.py`, P2 — centralization plan §3b).
>
> **Generation #9** · generated-at **2026-07-11T20:18Z** · by P3 lane worker (model: fable-5), dispatched by coordinator cse_012o8pySy5K3AV6JWoPKryZL (P3, fm PR #86)
>
> Every block below is a VERBATIM `⚑ needs-owner` / `OWNER-ACTION` extraction from a lane heartbeat (`control/status*.md` at the ls-remote-verified HEAD the roster row cites). Nothing here lands in the owner queue automatically: the manager dedups, verifies (R17), and curates. `suggested-id` is a deterministic content-derived slug the manager may adopt; `possibly-covered-by` lists active queue ids citing the same PR — `none matched` means manual dedup is still needed.

### superbot (hub) — ⚑ needs-owner: none new hub-specific (verified against fm docs/owner-queue.md @ 7ff1f75 — the hub's owner tai…

- suggested-id: `OQ-SUPERBOT-NONE-NEW-HUB-SPECIFIC`
- source: superbot/control/status.md @ `76d854d` · heartbeat `updated:` 2026-07-11T19:45:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: none new hub-specific (verified against fm docs/owner-queue.md @ 7ff1f75 — the hub's owner tail is already queued there). Manager-sweep note, NOT an owner click: fm owner-queue C#20's manager note (superbot codex-final-review invalid YAML) is RESOLVED by superbot PR #1995 (8214200) — retire that line at the next sweep.
```

### superbot-next — ⚑ needs-owner: FOUR live OWNER-ACTION items below (six-field format per control/README.md) — items 2 and 3 un…

- suggested-id: `OQ-SUPERBOT-NEXT-FOUR-LIVE-ITEMS-BELOW`
- source: superbot-next/control/status.md @ `c3037d5` · heartbeat `updated:` 2026-07-11T20:20Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: FOUR live OWNER-ACTION items below (six-field format per control/README.md) — items 2 and 3 unchanged; item 5 (band-7 AI key envelope — the live-NL leg is blocked on it); item 6 NEW at close-out: fleet failsafes may still be dead from the 2026-07-11T16:31Z platform env-teardown (this lane self-healed; sibling lanes could not be — record in docs/retro/q0265-routine-loop-2026-07-11.md); item 4 stays RETIRED, its capacity half now FLAPPING rather than walled (usage-limit replies on #148/#151/#152 but full P2 reviews on #154/#157/#160 the same morning; flap update in the item 4 record). The ORDER-013 "Self-review 2026-07-11" section below MIRRORS all three live items click-level plus one FYI (codex phantom-artifact claims, Q-0120 guard holds) for the manager sweep
```

### superbot-next — ⚑ OWNER-ACTION 2 — create the hello-plugin repo (flag 18a)

- suggested-id: `OQ-SUPERBOT-NEXT-2-CREATE-HELLO-PLUGIN`
- source: superbot-next/control/status.md @ `c3037d5` · heartbeat `updated:` 2026-07-11T20:20Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 2 — create the hello-plugin repo (flag 18a)
WHAT: Create one new empty GitHub repository named superbot-plugin-hello.
WHERE: https://github.com/new (owner account menno420).
HOW: name `superbot-plugin-hello`, public, no template — agents then move `examples/superbot-plugin-hello/` verbatim (pin hashes the manifest, not the repo — no re-pin needed).
WHY-IT-MATTERS: it proves a game plugin can live in its own repo, the architecture the mining/exploration game Projects will copy.
UNBLOCKS: ORDER 002 → done; the game Projects' reference pattern.
VERIFIED-NEEDED: attempted repo-create with the integration token — GitHub returns 403 on repo creation for this token class (recorded in docs/retro/project-review-2026-07-09.md §2 item 2); only the owner account can create repos.
```

### superbot-next — ⚑ OWNER-ACTION 3 — kill the branch-update merge dance

- suggested-id: `OQ-SUPERBOT-NEXT-3-KILL-BRANCH-UPDATE`
- source: superbot-next/control/status.md @ `c3037d5` · heartbeat `updated:` 2026-07-11T20:20Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 3 — kill the branch-update merge dance
WHAT: Change the repo merge settings so PRs stop needing a manual "update branch" click before merging.
WHERE: github.com/menno420/superbot-next → Settings → Rules/Rulesets (or Settings → General → merge queue).
HOW: enable the merge queue, or drop the require-up-to-date rule for `docs/**` + `control/**` paths.
WHY-IT-MATTERS: every session lost time to the update-branch dance and one session's tail was stranded on it (PRs #86/#87), and the same dance triggered a rate-limit stall.
UNBLOCKS: unattended session wrap-ups; less API traffic.
VERIFIED-NEEDED: repo Settings/Rulesets are admin-only — agent tokens can read but not modify rulesets (the #86/#87 stranding is the captured evidence of the wall in effect); an agent re-verified it cannot edit the ruleset when un-stranding those PRs.
```

### superbot-next — ⚑ OWNER-ACTION 4 — RETIRED 2026-07-11 (was: configure Codex for this repo — environment + code-review capacit…

- suggested-id: `OQ-SUPERBOT-NEXT-4-RETIRED-2026-07`
- source: superbot-next/control/status.md @ `c3037d5` · heartbeat `updated:` 2026-07-11T20:20Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 4 — RETIRED 2026-07-11 (was: configure Codex for this repo — environment + code-review capacity)
RESOLVED owner-side, both halves: the connector produced a FULL substantive review on #138 — comment 4941074976 (line-anchored walkthrough of all four changes; it ran the PR's 4 new tests itself, ✅) + verdict comment 4941104857 "Codex Review: Didn't find any major issues. Nice work!" (reviewed commit `77f9345`) — so the environment exists AND code-review capacity is restored. Historical evidence trail (kept for the record): "create an environment for this repo" on #117 (comment 4939224869) and #120 (comment 4939692286); "reached your Codex usage limits" on #124 (comment 4940004903), #125 (comment 4940095408) and #130 (comment 4940441924); no text reply on #114 (comment 4938835129) and #133 (comment 4940819831). The Q-0259/Q-0120 return path is now LIVE; the standing rule continues unchanged — @codex question on every substantive PR's final head, merge on green without waiting (Q-0258). REGRESSION NOTE (2026-07-11 late-night, folded at the 05:01Z heartbeat): the CAPACITY half is back at the wall — the connector answered BOTH band-7 questions with usage-limit replies: #148 comment 4942100526 ("You have reached your Codex usage limits") and #151 comment 4942514698 ("…usage limits for code reviews"). The environment half stays resolved (the #138 full review proved it exists), so this item stays RETIRED rather than reopened — but the owner may want to know the credit pool drained again the same day it was declared restored; until it refills, substantive questions keep landing per the standing rule and simply queue unanswered (the #148/#151 questions are in the open-questions note below). FLAP UPDATE (2026-07-11 morning, folded at the 06:35Z heartbeat): the pool REFILLED within the hour — one more usage-limit reply on #152 (comment 4942577962, 05:08Z), then FULL substantive P2 reviews on #154 (review 4676723779, 05:54Z, 2 P2s, final head `43b9b44`) and #157 (review 4676836079, 06:31Z, 1 P2, final head `f8532ef`). Item stays RETIRED; the capacity half is best described as FLAPPING — reviews arrive post-merge when the pool happens to be up (findings ledgered in the wave-5 records above).
```

### superbot-next — ⚑ OWNER-ACTION 5 — provide the band-7 AI key envelope (live-NL leg)

- suggested-id: `OQ-SUPERBOT-NEXT-5-PROVIDE-BAND-7`
- source: superbot-next/control/status.md @ `c3037d5` · heartbeat `updated:` 2026-07-11T20:20Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 5 — provide the band-7 AI key envelope (live-NL leg)
WHAT: Put a real `ANTHROPIC_API_KEY` in the agents' session environment and turn `AI_ENABLED` on for the live-drive guild.
WHERE: the Claude Code session environment the builder lanes run in (same place `DISCORD_BOT_TOKEN_PRODUCTION` already lives) — config seam sb/spec/config.py:166 (`ANTHROPIC_API_KEY`, SecretSpec, activation_link `ai.on_when_keyed`) and :148 (`AI_ENABLED`, default False, dormant posture).
HOW: export both vars into the session env (key value never recorded in-repo — env var NAME only, the §0.4 grant convention); optionally scope `AI_ENABLED=true` to the Superbot Admin live-drive guild posture.
WHY-IT-MATTERS: band 7's remaining legs — the live NL shell (mention→answer), `verify_and_regenerate_once`, and live routing — need a real model call to produce live-drive evidence; deterministic surfaces shipped regardless (#151), so this gates EVIDENCE, not code.
UNBLOCKS: the band-7 live-NL slice's ORDER 004 live-drive leg; until provided, those legs can only ship deterministic-provider tests (A-17 posture), not live-drive proof.
VERIFIED-NEEDED: verified during #151's ORDER 004 live drive — `ANTHROPIC_API_KEY` absent and `AI_ENABLED` off in the session env (PR #151 body, key-gap honesty section); the deterministic operator surface went live regardless (six real posts). An `OPENAI_API_KEY` exists in the sandbox env but arming NL on it was explicitly out of scope and the shipped default provider posture is deterministic.
```

### superbot-next — ⚑ OWNER-ACTION 6 — re-arm the fleet's dead failsafe routines (2026-07-11T16:31Z env-teardown fallout)

- suggested-id: `OQ-SUPERBOT-NEXT-6-RE-ARM-FLEET`
- source: superbot-next/control/status.md @ `c3037d5` · heartbeat `updated:` 2026-07-11T20:20Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 6 — re-arm the fleet's dead failsafe routines (2026-07-11T16:31Z env-teardown fallout)
WHAT: Check every lane's scheduled Routines and re-create the ones the platform teardown auto-disabled.
WHERE: the Claude Routines/schedules surface for each Project (or ask each lane's next fired session to self-check via list_triggers).
HOW: for each affected lane (substrate-kit, trading-strategy, sim-lab, idea-engine, product-forge; venture-lab/superbot-games/superbot-idle also touched) look for triggers with ended_reason "auto_disabled_env_deleted" and re-arm per that lane's recorded routine text; THIS lane needs nothing until un-archived (its loop was deliberately DISARMED at close-out — re-arm recipe in docs/retro/q0265-routine-loop-2026-07-11.md).
WHY-IT-MATTERS: a lane whose failsafe is dead never wakes on its own — it goes dark silently, not red.
UNBLOCKS: the standing autonomous core's sibling lanes resuming their loops.
VERIFIED-NEEDED: a platform ENV TEARDOWN at 2026-07-11T16:31Z auto-disabled scheduled triggers fleet-wide (ended_reason "auto_disabled_env_deleted" observed via list_triggers from the coordinator session); this lane self-healed its own failsafe but has no tool path to another lane's triggers — cross-lane trigger repair is owner/manager-only; owner was alerted ~2026-07-11T17:31Z; no repo evidence shows the sibling failsafes re-armed since.
```

### substrate-kit — ⚑ FOR MANAGER (relay debts owed to the kit — refreshed at the v1.12.0-wave close):

- suggested-id: `OQ-SUBSTRATE-KIT-MANAGER-RELAY-DEBTS-OWED`
- source: substrate-kit/control/status.md @ `17ac5ad` · heartbeat `updated:` 2026-07-11T19:51:53Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ FOR MANAGER (relay debts owed to the kit — refreshed at the v1.12.0-wave close):
- **NEW — pokemon-mod-lab lane-owed items (from the v1.6.0 → v1.12.0 catch-up, pokemon-mod-lab#43; Q-0261.3 scope, deliberately NOT done by the wave):** (a) its `control/status.md:40` heartbeat still says kit v1.6.0 — one-writer per file, the lane must bump it; (b) claims-home decision owed — legacy root `claims/` is the binding practice there vs the kit's `control/claims/`; the check advisory fires every session until the lane pins one via `substrate.config.json` → `claims_dir`; (c) its `automerge.required_context` defaults to "substrate-gate" but the repo's actual required check is **"ROM builds"** — must be fixed BEFORE its staged auto-merge enabler is ever wired live; (d) `control/README.md` classified DIVERGED — manual merge owed, delta preserved in `.substrate/upgrade-report.md` § Template deltas; (e) its heartbeat uses the bold-label `- **kit:** vX` form the kit's KIT_LINE_RE doesn't parse (kit-side grammar follow-up idea filed on the #232 session card).
- **heartbeat `kit:`-line bump OWNERSHIP question (wave-report inconsistency)** — still open: the wave records disagree about who owes the post-upgrade heartbeat bump (websites bumped its `kit:` line in-lane on the wave PR itself and scanned clean at the #207 regen; every other adopter's bump is recorded as "lane-owed" and chronically lags 1–3 releases — the registry's whole recurring self-report DRIFT class). The manager should rule which seat owns the post-wave `kit:`-line bump — the wave-upgrade PR itself (websites' shape) vs each lane's next wake — so the drift class ends fleet-wide instead of regenerating as ⚠️ noise every wave. The pokemon-mod-lab item (a) above is the newest instance.
- **superbot-next origin/main was force-pushed mid-wave** (the v1.10.x window) — flagged, not touched by any kit-seat session; their lane owns the history reconcile.
- **v1.12.0-wave heartbeat `kit:` bumps still lane-owed** (self-report lag class, per the wave records + the #232 regen: fleet-manager, superbot-games — its status.md still has NO `kit:` line at all — and trading-strategy all lane-owed; kit-seat quad self-report lag persists per the chronic class; trees all already v1.12.0). Also lane-owed from the trio wave: `docs/AGENT_ORIENTATION.md` diverged manual merges on all three (template delta preserved in each repo's `.substrate/upgrade-report.md`).
- Carried from earlier waves, still standing as far as kit evidence shows: superbot-next duplicate session cards guard-firing (their gate noise — lane dedup) · venture-lab dual claims homes (control/claims/ + legacy — consolidate per §6.4) · gba-homebrew docs pending `upgrade --apply-docs` · fleet-manager owner-action-fields advisory (chronic) · trading-strategy docs/CAPABILITIES.md landing-constraints entry (chronic).
```

### substrate-kit — ⚑ needs-owner: thirteen open items (items 2–12 carried verbatim — ordinals kept stable so cross-references ho…

- suggested-id: `OQ-SUBSTRATE-KIT-THIRTEEN-OPEN-ITEMS-ITEMS`
- source: substrate-kit/control/status.md @ `17ac5ad` · heartbeat `updated:` 2026-07-11T19:51:53Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: thirteen open items (items 2–12 carried verbatim — ordinals kept stable so cross-references hold — plus 14 + 15, the two parked pin PRs; item 13 RESOLVED 2026-07-11: the owner merged #181 @ f7aa633 — full resolution record in the retro §2 postscript + git history of this file). The two HOT ones are one click each:
```

### substrate-kit — ⚑ OWNER-ACTION 15 — T5 v3 probe re-shape — pin PR #238 awaits your ratification (do-not-automerge by design; …

- suggested-id: `OQ-SUBSTRATE-KIT-15-T5-V3-PROBE`
- source: substrate-kit/control/status.md @ `17ac5ad` · heartbeat `updated:` 2026-07-11T19:51:53Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 15 — T5 v3 probe re-shape — pin PR #238 awaits your ratification (do-not-automerge by design; PAIRS with OWNER-ACTION 14 / PR #220)
WHAT: Ratify (merge) or reject (close with a word) the T5 task-text re-shape that restores the probe's discriminating tension.
WHERE: https://github.com/menno420/substrate-kit/pull/238
HOW: click "Merge pull request" to ratify, or close it with a one-line reason — the PR is READY, CI-green at head 917318d, labeled at open, diff = bench/tasks/T5.md + its session card only.
WHY-IT-MATTERS: run-9 proved the v2 probe degenerate post-#222 — T4 now completes the card, so T5 boots on a "complete" push and the skip-vs-ritual tension the probe exists to measure never arises (run-9 report §5.5). v3 has the runner seed the drafted/unresolved state (and commit the arm tree clean — retiring the 4/4 commit-sweep confound of runs 8–9), so the probe discriminates regardless of T4's behavior.
UNBLOCKS: run-10 fires a non-degenerate T5. PAIRING: judge items are unchanged from v2, so rubric pin PR #220 scores v3 as-is and needs no re-cut — ratify both (one click each) and run-10 judges v3 task text under the §3-v2 rubric coherently.
VERIFIED-NEEDED: pin-path law (§5.0, check_bench_integrity rule 1): the lab never merges its own change to the bench oracle — labeled `do-not-automerge` at open, auto-merge verified not armed (enabler run 29164948745 arm step conclusion=skipped, KL-5 fresh-label guard; the head-917318d synchronize run 29165025432 skipped the whole enable-auto-merge job on the labeled payload; PR sat open at mergeable_state=clean on green CI), parked; only the owner's click lands it.
```

### substrate-kit — ⚑ OWNER-ACTION 14 — rubric §3 T5 v2 alignment — pin PR #220 awaits your ratification (do-not-automerge by des…

- suggested-id: `OQ-SUBSTRATE-KIT-14-RUBRIC-3-T5`
- source: substrate-kit/control/status.md @ `17ac5ad` · heartbeat `updated:` 2026-07-11T19:51:53Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 14 — rubric §3 T5 v2 alignment — pin PR #220 awaits your ratification (do-not-automerge by design)
WHAT: Ratify (merge) or reject (close with a word) the judge-rubric alignment your #181 merge made due.
WHERE: https://github.com/menno420/substrate-kit/pull/220
HOW: click "Merge pull request" to ratify, or close it with a one-line reason to reject — the PR is READY, CI-green at head c582006, diff = bench/rubric/cold-start-rubric.md (§3 T5 block only) + its session card.
WHY-IT-MATTERS: the judge already scores T5 from the ratified v2 task text, but the written rubric still describes the retired v1 items — every bench run carries a "protocol pins applied" deviation note until the two documents agree.
UNBLOCKS: bench runs from run-9 on score T5 straight from rubric §3; retires the run-8 report §5 limitation line.
VERIFIED-NEEDED: pin-path law (§5.0, check_bench_integrity rule 1): the lab never merges its own change to the bench oracle — this session labeled #220 at open, verified the enabler's arm step was SKIPPED (run 29158862553, step "Enable native auto-merge (squash)" conclusion=skipped) and a disarm probe mutated nothing (PR updated_at unchanged), and parked it. Only the owner's click can land it — the designed wall, not an assumed one.
(PAIRING note added 2026-07-11: T5 v3 pin PR #238 / ⚑ 15 keeps the v2 judge items verbatim — ratifying both, one click each, gives run-10 a coherent text+rubric pair.)
```

### substrate-kit — ⚑ OWNER-ACTION 2 — P10 required-check swap

- suggested-id: `OQ-SUBSTRATE-KIT-2-P10-REQUIRED-CHECK`
- source: substrate-kit/control/status.md @ `17ac5ad` · heartbeat `updated:` 2026-07-11T19:51:53Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 2 — P10 required-check swap
WHAT: Swap which CI check main requires, from the two legacy names to the current one.
WHERE: repo Settings → Rules → the `main` ruleset → required status checks
HOW: remove "Kit test suite" and "Cold-adoption smoke (adopt + check --strict)"; add `kit-quality` (source: GitHub Actions); set "Require branches to be up to date" OFF
WHY-IT-MATTERS: the legacy alias jobs cause ~35-min queue stalls purely to satisfy old names; the up-to-date requirement stalls green PRs `behind` (live-hit #107).
UNBLOCKS: an agent deletes the two legacy-alias-* jobs (queue item 9); the queue-stall class ends; fast-lane PRs stop paying an update round-trip.
VERIFIED-NEEDED: no agent path to rulesets — direct api.github.com is 403 through the proxy and the MCP toolset has no ruleset endpoint; Settings → Rules is owner-only UI.
```

### substrate-kit — ⚑ OWNER-ACTION 3 — P4 arm the daily lab loop

- suggested-id: `OQ-SUBSTRATE-KIT-3-P4-ARM-DAILY`
- source: substrate-kit/control/status.md @ `17ac5ad` · heartbeat `updated:` 2026-07-11T19:51:53Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 3 — P4 arm the daily lab loop
WHAT: Create the scheduled session that runs the lab every morning.
WHERE: Console → kit repo environment → Schedules → New schedule
HOW: paste the fenced prompt from docs/operations/lab-loop.md § Arming verbatim · cron `0 6 * * *` (UTC) · fresh session per fire ON · Sonnet-class model · unrestricted-branch-push OFF · auto-fix PRs ON
WHY-IT-MATTERS: turns the lab from manually-fired sessions into the self-running daily loop the program is built around.
UNBLOCKS: D3 (the autonomous daily loop; needs ≥3 scheduled fires).
VERIFIED-NEEDED: the console Schedules pane is owner UI — routine/schedule creation is an enumerated wall in docs/CAPABILITIES.md; no in-session API/MCP path.
(Correction note appended 2026-07-10, ORDER 010 — the VERIFIED-NEEDED line above is now PARTIALLY invalidated: routines CAN be armed agent-side via `create_trigger` (the ORDER 010 arm and both cutovers above prove it). The ask stays open because the lab loop wants a fresh-session-per-fire daily schedule with specific console options (model class, branch-push, auto-fix PRs), which the MCP arm has NOT been verified to cover — per THE DISCOVERY RULE a next session should ATTEMPT `create_trigger` (fresh-session mode) before treating this as owner-only.)
(RESOLUTION note appended 2026-07-11, the P4 slice — the directed ATTEMPT was made and SUCCEEDED: `create_trigger` with `create_new_session_on_fire=true` armed the loop agent-side — trigger trig_01MHwmBrA1bziEp49g6xqGt5, cron `0 6 * * *`, substrate-kit environment, lab-loop.md prompt verbatim, next fire 2026-07-12T06:01:54Z (full record: ROUTINE STATE). The founding plan's P4 row itself blesses this path ("or agent-created trigger + owner kill-switch"); the kill switch exists both sides (owner pause toggle + agent delete_trigger). **The ask is REDUCED to an optional console verification**: the three console-only knobs — model class Sonnet-class, unrestricted-branch-push OFF, auto-fix PRs ON — are not settable/readable via MCP; the fired sessions run on environment defaults. If the defaults are acceptable, say nothing — the loop is live; to adjust, open the Routine in the console and set the knobs. D3's ≥3-consecutive-fires count starts 2026-07-12.)
```

### substrate-kit — ⚑ OWNER-ACTION 4 — P5 create Railway project kit-lab

- suggested-id: `OQ-SUBSTRATE-KIT-4-P5-CREATE-RAILWAY`
- source: substrate-kit/control/status.md @ `17ac5ad` · heartbeat `updated:` 2026-07-11T19:51:53Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 4 — P5 create Railway project kit-lab
WHAT: Create a separate Railway project so the lab gets its own infra lane.
WHERE: Railway console → New project
HOW: name `kit-lab` · region `europe-west4` · no spend caps (PL-005) · notification rule → HQ #railway-alerts; then put a project-scoped RAILWAY_TOKEN in the kit repo's environment
WHY-IT-MATTERS: the lab has no infra lane of its own; sharing production's is forbidden.
UNBLOCKS: the P6 console move (agent-built the moment the token exists).
VERIFIED-NEEDED: Railway project creation is owner console UI, and the ambient-IDs-are-production rule bars agents from touching existing Railway IDs — both walls enumerated; no agent path.
```

### substrate-kit — ⚑ OWNER-ACTION 5 — P8 confirm MIT

- suggested-id: `OQ-SUBSTRATE-KIT-5-P8-CONFIRM-MIT`
- source: substrate-kit/control/status.md @ `17ac5ad` · heartbeat `updated:` 2026-07-11T19:51:53Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 5 — P8 confirm MIT
WHAT: Confirm the kit's license with one word.
WHERE: any channel
HOW: reply "MIT ok", or name a replacement license
WHY-IT-MATTERS: the kit ships to consumer repos with no declared license until this lands.
UNBLOCKS: closing the license ⚑ carried since KL-1.
VERIFIED-NEEDED: a license choice is a legal/product decision — owner judgment by nature; nothing for an agent to attempt.
```

### substrate-kit — ⚑ OWNER-ACTION 6 — P11 public flip OR P13 read-only PAT (pick one)

- suggested-id: `OQ-SUBSTRATE-KIT-6-P11-PUBLIC-FLIP`
- source: substrate-kit/control/status.md @ `17ac5ad` · heartbeat `updated:` 2026-07-11T19:51:53Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 6 — P11 public flip OR P13 read-only PAT (pick one)
WHAT: Let the other fleet repos read this one — either make it public or mint a read-only token.
WHERE: P11: Settings → General → Danger Zone → Change visibility. P13: github.com/settings/tokens → fine-grained PAT, read-only, consumer-repo scope, then add to the fleet environments
HOW: P11 is click-through; P13 is create-token + paste into environment settings
WHY-IT-MATTERS: sibling repos cannot see kit data today, so the merged console and the loop's cross-repo sweeps run blind.
UNBLOCKS: kit data in the merged console + the lab loop's B2/B3/B4 sweeps (queue item 12).
VERIFIED-NEEDED: repo visibility and credential minting are account-owner surfaces; the wall is verbatim in docs/CAPABILITIES.md — cross-repo get_file_contents returned "Access denied: repository … is not configured for this session".
```

### substrate-kit — ⚑ OWNER-ACTION 7 — superbot upgrade decision

- suggested-id: `OQ-SUBSTRATE-KIT-7-SUPERBOT-UPGRADE-DECISION`
- source: substrate-kit/control/status.md @ `17ac5ad` · heartbeat `updated:` 2026-07-11T19:51:53Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 7 — superbot upgrade decision
WHAT: Rule on superbot's kit pin — upgrade it or keep holding.
WHERE: any channel
HOW: decide-and-flag recommendation — adopt at the next stable release in one hop; say nothing to accept, "upgrade now" or "hold pin-only" to override
WHY-IT-MATTERS: superbot's deliberate pin is now 14 releases behind (v1.0.0 vs v1.12.0) and the drift window keeps growing.
UNBLOCKS: the fleet's last non-ENGAGED adopter upgrading, whenever taken.
VERIFIED-NEEDED: the pin is a recorded owner decision (docs/adopters.md: "the v1.2.0+ upgrade is an owner decision") — agents don't overrule a deliberate stance; product judgment, not a wall.
```

### substrate-kit — ⚑ OWNER-ACTION 8 — web-environment setup script paste

- suggested-id: `OQ-SUBSTRATE-KIT-8-WEB-ENVIRONMENT-SETUP`
- source: substrate-kit/control/status.md @ `17ac5ad` · heartbeat `updated:` 2026-07-11T19:51:53Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 8 — web-environment setup script paste
WHAT: Paste the corrected environment setup script so no more sessions die at startup.
WHERE: Claude console → the environment's settings → "Setup script" field (owner-only dialog)
HOW: paste the guarded script from docs/gen2/setup.sh (gen-2 variant) verbatim
WHY-IT-MATTERS: the current script already killed one session at provisioning (wrong cwd + hard-fail on a missing requirements.txt — PR #47 documents the casualty + fix).
UNBLOCKS: reliable session starts in this environment. If already pasted, say so and this ask is withdrawn — agents cannot read the settings dialog to confirm.
VERIFIED-NEEDED: the environment settings dialog is owner-only console UI (docs/CAPABILITIES.md); PR #47 is the live evidence of the one confirmed casualty.
(§6.5 note appended 2026-07-10: the kit-side setup-script CONTRACT shipped without this — PR #147 planted `scripts/env-setup.sh` + the `check_setup_script` enforcer from the fleet-manager archetype material. This ask remains the ENV-PANEL half: the owner-pasted shim is what makes any repo's `scripts/env-setup.sh` actually run at provisioning. The paste-ready archetype scripts live at fleet-manager `environments/archetype-*.sh`.)
```

### substrate-kit — ⚑ OWNER-ACTION 9 — (informational, low priority) optional self-merge permission rule

- suggested-id: `OQ-SUBSTRATE-KIT-9-INFORMATIONAL-LOW-PRIORITY`
- source: substrate-kit/control/status.md @ `17ac5ad` · heartbeat `updated:` 2026-07-11T19:51:53Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 9 — (informational, low priority) optional self-merge permission rule
WHAT: Optionally grant a permission rule so future sessions can self-merge PRs directly instead of relying on the enabler workflow.
WHERE: Claude console → the environment's permission/auto-mode settings
HOW: allow `mcp__github__merge_pull_request` / `mcp__github__enable_pr_auto_merge` for this environment's sessions
WHY-IT-MATTERS: one gen-2 lane's auto-mode classifier refused these as "Merge Without Review" while another lane's were permitted the same night — the wall is session-dependent. auto-merge-enabler.yml covers the refused case server-side.
UNBLOCKS: nothing blocked — both paths land PRs today; this only removes the indirection. LOW priority.
VERIFIED-NEEDED: the classifier denial is verbatim in docs/CAPABILITIES.md (2026-07-10); the permission grant is an owner console surface — no agent path to change auto-mode rules.
```

### substrate-kit — ⚑ OWNER-ACTION 10 — branch cleanup (lowest priority)

- suggested-id: `OQ-SUBSTRATE-KIT-10-BRANCH-CLEANUP-LOWEST`
- source: substrate-kit/control/status.md @ `17ac5ad` · heartbeat `updated:` 2026-07-11T19:51:53Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 10 — branch cleanup (lowest priority)
WHAT: Turn on auto-delete for merged branches, then delete the stale branches of already-closed PRs.
WHERE: Settings → General → Pull Requests → check "Automatically delete head branches"; then each closed PR's "Delete branch" button
HOW: one checkbox + click-throughs (this window added the release/regen/bench lanes' merged branches to the pile)
WHY-IT-MATTERS: pure hygiene — ends the clutter class permanently; nothing functional waits on it.
UNBLOCKS: nothing functional; the checkbox prevents recurrence forever.
VERIFIED-NEEDED: branch deletion is 403 on EVERY agent path (git push :branch 403, REST 403, GraphQL deleteRef disabled, no MCP tool — docs/CAPABILITIES.md "Branch deletion" wall). A full session attempted it and deleted zero.
```

### substrate-kit — ⚑ OWNER-ACTION 11 — enable "automatically update branches" (closes the auto-merge behind-stall)

- suggested-id: `OQ-SUBSTRATE-KIT-11-ENABLE-AUTOMATICALLY-UPDATE`
- source: substrate-kit/control/status.md @ `17ac5ad` · heartbeat `updated:` 2026-07-11T19:51:53Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 11 — enable "automatically update branches" (closes the auto-merge behind-stall)
WHAT: Turn on the repo setting that auto-updates a PR branch when its base moves, so an armed auto-merge PR that goes `behind` gets refreshed and lands without an agent round-trip.
WHERE: Settings → General → Pull Requests → check "Always suggest updating pull request branches" / the auto-update-branch control (the counterpart to OWNER-ACTION 2's "Require branches up to date")
HOW: one checkbox
WHY-IT-MATTERS: with "Require branches up to date" ON, a green armed PR stalls `behind` whenever a sibling merges first (live-hit #107 + the §6.4/§6.5/§6.8/§6.10 window; #144, #147, #150 and #153 pre-empted it only by a manual branch update). The enabler `synchronize` re-arm (#111) narrows this — a fix-push now re-arms — but a PR that goes behind AFTER its last push still needs a manual `git merge origin/main` + push. Auto-update removes that residual manual step.
UNBLOCKS: armed auto-merge completes on green even when a sibling merges first with no later push; fully ends the behind-stall class (complements OWNER-ACTION 2, which offers the alternative of turning the requirement OFF entirely).
VERIFIED-NEEDED: repo General settings are owner-only UI; no agent path to toggle repo settings (same class as the ruleset/branch walls in docs/CAPABILITIES.md). Live evidence: #107 (and later close branch updates) sat `behind` with green checks until a manual branch update; the enabler `synchronize` fix (#111) is a partial, not a full, close.
```

### substrate-kit — ⚑ OWNER-ACTION 12 — route the websites ORDER 005 fleet relay

- suggested-id: `OQ-SUBSTRATE-KIT-12-ROUTE-WEBSITES-ORDER`
- source: substrate-kit/control/status.md @ `17ac5ad` · heartbeat `updated:` 2026-07-11T19:51:53Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 12 — route the websites ORDER 005 fleet relay
WHAT: Send the unexecuted ORDER 005 from the `websites` repo's inbox to a session that has websites scope, so it gets done.
WHERE: the `menno420/websites` repo — its `control/inbox.md` ORDER 005 (route it to a websites-scoped session; e.g. dispatch a session on that repo)
HOW: assign/relay ORDER 005 to a websites-scoped session (a substrate-kit / coordinator session cannot — no websites write scope)
WHY-IT-MATTERS: a dispatched fleet order is sitting unexecuted; the coordinator surfaced it but has no websites scope to route or run it, so it stalls until the owner routes it.
UNBLOCKS: whatever ORDER 005 on websites was meant to deliver (its substance lives in that repo's inbox).
VERIFIED-NEEDED: cross-repo write to `menno420/websites` is out of this session's scope (the per-session repo allowlist governs reads; execution needs a websites-scoped session) — genuinely owner-routed, not an assumed wall. Provenance: coordinator relay 2026-07-10 (docs/retro/coordinator-session-2026-07-10.md § 4); origin is this lane's gen-1 status notes.
```

### substrate-kit — ⚑ version-truth deference (flagged for the owner's §7 layering ruling, decide-and-flag): generated `docs/adop…

- suggested-id: `OQ-SUBSTRATE-KIT-VERSION-TRUTH-DEFERENCE-FLAGGED`
- source: substrate-kit/control/status.md @ `17ac5ad` · heartbeat `updated:` 2026-07-11T19:51:53Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ version-truth deference (flagged for the owner's §7 layering ruling, decide-and-flag): generated `docs/adopters.md` is now the SINGLE home for the fleet's kit-version spread; other homes (hand-kept registries, release-json narratives, status-prose version claims) should DEFER to it pending the owner's §7 ruling. Concretely open under that ruling: the kit repo's own `substrate.config.json` pin (v1.0.0, self-adopt-era) vs its dist (v1.12.0) — the registry's one tree-internal DRIFT row, deliberately NOT hand-fixed because what consumer-#0's pin *means* is the §7 question.
```

### ↳ substrate-kit — `control/status-superbot-coordinator.md` — ⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLI…

- suggested-id: `OQ-SUBSTRATE-KIT-1-VERIFY-DELIVER-TESTING`
- source: substrate-kit/control/status-superbot-coordinator.md @ `17ac5ad` · heartbeat `updated:` 2026-07-10T13:47:02Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLIPPED at 2026-07-10T13:45Z (band-5 "NEXT LANE: LIVE-DRIVE", 01:05Z heartbeat), so that lane's seven wind-down deliverables are still owed [unblocks: superbot-next lane archive]; 2) kernel-surface-drift ruling (flag 13 in superbot-next docs/status/testing-report-2026-07-09.md: "relax-compare" or "re-baseline") [unblocks: ALL parity flips]; 3) create repo superbot-plugin-hello (github.com/new, owner menno420, Public, no README) [unblocks: ORDER 002 done]; 4) paste the setup script from docs/environment-setup-script.md into the project Environment settings (re-verified exit-0 at wind-down) [unblocks: no more provisioning deaths]; 5) nod for wiring superbot's new collision/freshness checkers (#1918/#1923) into code-quality.yml — one small PR, owner said workflow edits need a nod [unblocks: checkers enforce in CI]; 6) stale trading-lab/venture-lab manifest rows (manager-owned file) + Q-0248 taxonomy lacks a "tooling" class [unblocks: honest telemetry]
```

### websites — ⚑ needs-owner: SEVEN asks — canonical list in docs/owner/OWNER-ACTIONS.md: (1) PR #141 merge click (+ branch …

- suggested-id: `OQ-WEBSITES-SEVEN-ASKS-CANONICAL-LIST`
- source: websites/control/status.md @ `556ff9b` · heartbeat `updated:` 2026-07-11T19:49:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: SEVEN asks — canonical list in docs/owner/OWNER-ACTIONS.md: (1) PR #141 merge click (+ branch update; its watchdog session keeps it fresh — exact head SHA in the PR + its session card's park record); (2) botsite DATABASE_URL Postgres; (3) control-plane GITHUB_TOKEN PAT; (4) review/ Railway service (Root Directory = review); NEW from #145 (full six-field blocks in OWNER-ACTIONS.md): (5) answer Q-0004 — WHERE live bot control lives (websites / superbot / superbot-next) or explicitly stay dry-run — THE gate for everything below; (6) create the Discord OAuth application + redirect URI for the future armed panel (after Q-0004); (7) provision the scoped bot control-API token + the SEPARATE armed Railway service that holds it (env per spec §9; the dashboard service gets NOTHING). Plus the branch prune list above.
```

### websites — ⚑ OWNER-ACTION

- suggested-id: `OQ-WEBSITES-FLAG`
- source: websites/control/status.md @ `556ff9b` · heartbeat `updated:` 2026-07-11T19:49:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
  ⚑ OWNER-ACTION
  WHAT: Create a small Postgres for the botsite /submit intake and point the botsite service at it.
  WHERE: railway.app → project superbot-websites → New → Database → PostgreSQL; then service botsite → Variables.
  HOW: add variable DATABASE_URL = the new Postgres connection string Railway shows (copy-paste).
  WHY-IT-MATTERS: the public feature/bug submission form is a labeled stub until a store exists.
  UNBLOCKS: the moderated submissions queue + GitHub-issue mirror (rework Q5) — agent-buildable the moment the variable exists.
  VERIFIED-NEEDED: provisioning creates a paid resource in your Railway account and D‑0005 forbids agent-initiated Railway mutations without your explicit go — policy wall, deliberately not attempted; no DATABASE_URL exists on the service today.
```

### websites — ⚑ OWNER-ACTION

- suggested-id: `OQ-WEBSITES-FLAG-2`
- source: websites/control/status.md @ `556ff9b` · heartbeat `updated:` 2026-07-11T19:49:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
  ⚑ OWNER-ACTION
  WHAT: Mint a durable fine-grained GitHub PAT and set it on the control-plane service.
  WHERE: github.com → Settings → Developer settings → Fine-grained tokens; then railway.app → superbot-websites → control-plane → Variables.
  HOW: token scoped to menno420 repos, read for contents/actions + actions:write for the CI re-run button; set as GITHUB_TOKEN (exact steps: docs/deployment.md § owner TODO).
  WHY-IT-MATTERS: rate headroom + resilience — the fleet surfaces walk 18 lanes tokenless on the anonymous 60-req/h ceiling; a durable PAT also unlocks richer review-bake stats for private fleet repos (per #141).
  UNBLOCKS: actions-secrets + auto-merge-allowed cells; /owner re-run CI; 5000 req/h headroom across the fleet surfaces.
  VERIFIED-NEEDED: live board shows "unknown (token lacks admin scope)" / "unknown (needs push-scope token)" cells — the token is an owner-held Railway service variable agents cannot read or set. Live finding 2026-07-10/11: all fleet surfaces verified 200 with REAL content while the service token is unset.
```

### trading-strategy — ⚑ needs-owner (six-field form — what / why / exact click / where / blocking? / fallback; durable copies with …

- suggested-id: `OQ-TRADING-STRATEGY-SIX-FIELD-FORM-WHAT`
- source: trading-strategy/control/status.md @ `d3ae8f4` · heartbeat `updated:` 2026-07-11T19:33:12Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner (six-field form — what / why / exact click / where / blocking? / fallback; durable copies with full six-field detail in docs/retro/archive-ready-2026-07-11.md):
- (g) RE-ARM WEEKLY GRADING CADENCE — TRIGGER SUCCESSION (NEW, top risk) / both live triggers (2h failsafe trig_01YBaVeKAW2fSD83S9F37s2d + weekly grading wake trig_01YXNmgqYeYQ1LuepsLmbNCG, fires 2026-07-17T09:00:00Z) are bound to coordinator session session_01NwvvbgUVSdQvY8eYwtuEoo and die silently at chat archive — the 2026-07-17 grading pass and inbox watching then have NO executor / have the successor session or an owner Routine re-arm a weekly grading Routine from 2026-07-17T09:00Z ("run the weekly paper-lane grading pass per docs/paper-lane-protocol.md §6–§7") / claude.ai Routines or a new coordinator session for this project / YES for the 2026-07-17 pass — the only time-critical item / a late pass is protocol-tolerated (§6 — delay, not corruption; warm-up is expected FLAT ~3 weeks), so late is recoverable, never is not.
- (b) ENV SETUP SCRIPT / fresh-environment sessions die silently at provision without it (setup runs at cwd=/home/user with repos as subdirectories) / paste the contents of environments/setup-universal.sh into the environment's setup-script field and save / Claude environment config for this project / not blocking (current pinned env works) / keep spawning into the pinned env and treat any child with no heartbeat within 10 min as dead → respawn.
- (c) ALLOW AUTO-MERGE TOGGLE / auto-merge arm fails pending-side with "unstable status" while the repo toggle is off, so every merge needs an agent to poll-and-merge (reconfirmed on PR #36) / tick "Allow auto-merge" / GitHub → menno420/trading-strategy → Settings → General → Pull Requests / not blocking / continue REST/MCP squash-merge on green (the path every merge to date used, per ORDER 002 merged-on-green).
- (d) ARCHIVE DEAD GEN-1 SESSION / the gen-1 "ORDER 001 successor" session died at provision, emits no failure event, and still lists as active — misleading / open the project's session list, locate "ORDER 001 successor", archive it / claude.ai session list for this project / not blocking / ignore it — it consumes nothing.
- (f) DECIDE ON POST-2026 OUT-OF-SAMPLE PROTOCOL PROPOSAL / research round 2 closed with 5 dev-candidates whose ONLY path past dev-candidate is a NEW owner-gated pre-registered protocol on genuinely new post-2026 data — recorded as a PROPOSAL in docs/final-report.md (POST-HOLDOUT DEV-ONLY section) and docs/research-round-2-results.md; agents never schedule, initiate, or run it / if wanted, file an inbox ORDER authorizing a pre-registered protocol draft (decision only — nothing runs on a yes until the protocol itself is owner-approved); if not wanted, no click needed / control/inbox.md via the manager / not blocking / dev-candidates stay labeled dev-only indefinitely — flag-only, this item never self-executes. ((e) merge-PR-#37 retired: resolved by owner click, PR #37 merged 2026-07-10T20:56:34Z by menno420.)
next-update-by: 2026-07-17T23:59:00Z (weekly grading cadence, protocol §6 — first pass is expected FLAT: warm-up runs ~3 weeks; NOTE this deadline currently has no executor until ⚑ (g) is resolved)
```

### venture-lab — - **⚑ HOT — close PR #51 + delete branch `menno420-patch-1` (photo exposure)**

- suggested-id: `OQ-VENTURE-LAB-HOT-CLOSE-PR-51`
- source: venture-lab/control/status.md @ `2044dc6` · heartbeat `updated:` 2026-07-11T19:37:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ HOT — close PR #51 + delete branch `menno420-patch-1` (photo exposure)**
  · WHAT: close PR #51 and delete branch `menno420-patch-1`. · WHY: the owner uploaded **10 full-res, unwatermarked original photos** to PR #51; it is **STILL OPEN and publicly downloadable**. Treat the 10 files as permanently exposed (forks + git history retain them). Compliant watermarked previews already landed (PR #52 `dfe3332`) + validator hardened repo-wide; this is the owner cleanup click (agents do not close owner PRs). · VERIFIED-WHEN: PR #51 closed and branch `menno420-patch-1` deleted.
```

### venture-lab — - **⚑ — disposition PR #38 (stale codex pre-publish review)**

- suggested-id: `OQ-VENTURE-LAB-DISPOSITION-PR-38-STALE`
- source: venture-lab/control/status.md @ `2044dc6` · heartbeat `updated:` 2026-07-11T19:37:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ — disposition PR #38 (stale codex pre-publish review)**
  · WHAT: close or merge PR #38 (`codex/review-code-for-publish-blockers`) at owner discretion. · WHY: stale pre-publish gate review, **superseded by the #49 fail-closed hotfix**. · VERIFIED-WHEN: PR #38 closed or merged.
```

### venture-lab — - **⚑B — publish membership-kit at $49 — UNFROZEN ✅**

- suggested-id: `OQ-VENTURE-LAB-B-PUBLISH-MEMBERSHIP-KIT`
- source: venture-lab/control/status.md @ `2044dc6` · heartbeat `updated:` 2026-07-11T19:37:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑B — publish membership-kit at $49 — UNFROZEN ✅**
  · STATUS: **UNFROZEN** — freeze condition met by PR #16 (`912da3e`) + green substrate-gate run 29134433874. · WHAT: publish `candidates/membership-kit/LISTING.md` as a $49 product on Gumroad/Lemon Squeezy, uploading `candidates/membership-kit/dist/membership-kit-v0.2.zip` (click script: `docs/launch/membership-kit/owner-actions.md`). · UNBLOCKS: candidate #1 first-revenue path. · VERIFIED-WHEN: public listing URL + a test purchase completes.
```

### venture-lab — - **⚑D — publish template-packs at $19 PWYW — UNFROZEN ✅**

- suggested-id: `OQ-VENTURE-LAB-D-PUBLISH-TEMPLATE-PACKS`
- source: venture-lab/control/status.md @ `2044dc6` · heartbeat `updated:` 2026-07-11T19:37:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑D — publish template-packs at $19 PWYW — UNFROZEN ✅**
  · STATUS: **UNFROZEN** (same gate as ⚑B). · WHAT: publish `candidates/template-packs/LISTING.md` PWYW $19 suggested, uploading `candidates/template-packs/dist/template-packs-v0.1.zip` (click script: `docs/launch/template-packs/owner-actions.md`). · UNBLOCKS: candidate #2 first revenue + bundle cross-sell. · VERIFIED-WHEN: live listing URL resolves + a test download works.
```

### venture-lab — - **⚑E — publish stripe-webhook-test-kit at $29 — QUEUED (2026-07-11) ✅**

- suggested-id: `OQ-VENTURE-LAB-E-PUBLISH-STRIPE-WEBHOOK`
- source: venture-lab/control/status.md @ `2044dc6` · heartbeat `updated:` 2026-07-11T19:37:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑E — publish stripe-webhook-test-kit at $29 — QUEUED (2026-07-11) ✅**
  · STATUS: **QUEUED** — both gates met (in-CI green on head `b5b99cd` + main `fc7f39c`; R23 non-author verification, record above). · WHAT: publish per the six-field click script `docs/launch/stripe-webhook-test-kit/publish-owner-action.md`, uploading `candidates/stripe-webhook-test-kit/dist/stripe-webhook-test-kit-v0.1.zip`. · UNBLOCKS: candidate-ranking #1 first-revenue path + the first-ten-customers funnel. · VERIFIED-WHEN: live listing URL returns HTTP 200 (CI leg already satisfied).
```

### venture-lab — - **⚑F — publish the Agent Fleet Field Manual at $39 — QUEUED (2026-07-11) ✅**

- suggested-id: `OQ-VENTURE-LAB-F-PUBLISH-AGENT-FLEET`
- source: venture-lab/control/status.md @ `2044dc6` · heartbeat `updated:` 2026-07-11T19:37:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑F — publish the Agent Fleet Field Manual at $39 — QUEUED (2026-07-11) ✅**
  · STATUS: **QUEUED** — evidence reviewed by the coordinator seat: PR #41 merged `9226e22`, all three checks green on head `c77ce0d`, NON-AUTHOR spot-review of both free chapters all-CONFIRMED/none-refuted, zip sha256 `7eff9235024619a632020c06f7c47da24667f8134c828715694eaa8755a29176` recomputed on main. · WHAT: publish per the six-field click script `docs/launch/agent-fleet-field-manual/publish-owner-action.md`, uploading `candidates/agent-fleet-field-manual/dist/agent-fleet-field-manual-v0.1.zip` at $39. Gumroad-hosted — no custom payment path, so the D1/Stripe gate does not apply. Conservative: 0–4 sales/90d ($0–$156); $0 without distribution. · UNBLOCKS: candidate #4 first-revenue path + the free-chapter validation funnel. · VERIFIED-WHEN: live listing URL returns HTTP 200 on a purchasable $39 page AND ≥2 free chapters are live.
```

### venture-lab — - **⚑ — publish the free gotcha article**

- suggested-id: `OQ-VENTURE-LAB-PUBLISH-FREE-GOTCHA-ARTICLE`
- source: venture-lab/control/status.md @ `2044dc6` · heartbeat `updated:` 2026-07-11T19:37:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ — publish the free gotcha article**
  · WHAT: publish `docs/launch/stripe-webhook-test-kit/gotcha-article.md` (free funnel top). · WHY: the test-kit's **validation-signal clock starts at article publish** per its INTAKE kill rule — downstream candidates wait on this signal. · VERIFIED-WHEN: article live at a public URL.
```

### venture-lab — - **⚑A — provide test-mode Stripe API keys — OPEN (live E2E still unverified)**

- suggested-id: `OQ-VENTURE-LAB-PROVIDE-TEST-MODE-STRIPE`
- source: venture-lab/control/status.md @ `2044dc6` · heartbeat `updated:` 2026-07-11T19:37:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑A — provide test-mode Stripe API keys — OPEN (live E2E still unverified)**
  · WHAT: create a free Stripe account, paste the test-mode secret + webhook signing secret into `candidates/membership-kit/server/.env` (env NAMES `STRIPE_SECRET_KEY`, `STRIPE_WEBHOOK_SECRET` — values never in repo). · WHY: the HTTP-layer real-path tests are green locally and in CI, but a live end-to-end test-mode purchase remains UNVERIFIED without keys. · VERIFIED-WHEN: `python3 app.py` prints `mode=stripe`; `stripe trigger checkout.session.completed` grants a membership visible at `/members?email=…` returning 200.
```

### venture-lab — - **⚑ — owner photo samples upload (photo-packs)**

- suggested-id: `OQ-VENTURE-LAB-PHOTO-SAMPLES-UPLOAD-PHOTO`
- source: venture-lab/control/status.md @ `2044dc6` · heartbeat `updated:` 2026-07-11T19:37:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ — owner photo samples upload (photo-packs)**
  · WHAT: upload downsized (**≤2048px**) **watermarked** previews to `candidates/photo-packs/samples/` per the LOUD safety rule in `candidates/photo-packs/PACK-SPEC.md` — full-resolution originals NEVER enter this public repo. `candidates/photo-packs/validate_samples.py` mechanically enforces the caps. · UNBLOCKS: pack curation, the gallery site, and channel listings (per `candidates/photo-packs/MARKET-PLAN.md`). · VERIFIED-WHEN: validator exits 0 with ≥1 real sample and the gallery renders it.
```

### venture-lab — - **⚑ (optional) — Supabase project for hosted persistence**

- suggested-id: `OQ-VENTURE-LAB-OPTIONAL-SUPABASE-PROJECT-HOSTED`
- source: venture-lab/control/status.md @ `2044dc6` · heartbeat `updated:` 2026-07-11T19:37:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ (optional) — Supabase project for hosted persistence**
  · WHAT: create a Supabase project + `members` table per the six-field OWNER-ACTION in `candidates/membership-kit/server/README.md` (env NAMES only in repo). · UNBLOCKS: hosted persistent membership (SupabaseStore landed in PR #23, verified against a stub PostgREST; live round-trip owner-gated). · VERIFIED-WHEN: members survive a restart via Supabase.
```

### venture-lab — - **⚑ — decide-and-flag decisions open for retroactive veto (ORDER 006 mirror)**

- suggested-id: `OQ-VENTURE-LAB-DECIDE-FLAG-DECISIONS-OPEN`
- source: venture-lab/control/status.md @ `2044dc6` · heartbeat `updated:` 2026-07-11T19:37:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ — decide-and-flag decisions open for retroactive veto (ORDER 006 mirror)**
  · WHAT: two decisions were taken without per-action owner signoff: (1) all merges 2026-07-11 executed under the standing grant (owner in-session event b92aab44); (2) the idle pacemaker was widened 15→45 min with the 2-hourly failsafe as backstop. · ASK: veto either retroactively, or no action needed to keep them.
```

### superbot-games · Seat A — ⚑ needs-owner: (1) FIVE green + reviewed PRs each need ONE merge click — order: #34 first (ends floor churn),…

- suggested-id: `OQ-SUPERBOT-GAMES-1-FIVE-GREEN-REVIEWED`
- source: superbot-games/control/status.md @ `5a9d4d2` · heartbeat `updated:` 2026-07-11T13:19:52Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: (1) FIVE green + reviewed PRs each need ONE merge click — order: #34 first (ends floor churn), then #36, #38, then #32 & #27 (these two need a quick rebase first); a direct "merge them" in the world-games session also clears the gate. (2) Model-attribution (ORDER 003): this lane records `📊 Model: Opus 4.8` (family-level, environment-reported) on session cards, never the exact internal id — confirm that family-level form is wanted, or say if "Claude Opus" is preferred. (3) No spend / publish / external-account / production-data actions taken; no secrets in repo — only decide-and-flag items were re-scoping #36 (documented) and building churn-fix #34.
```

### superbot-games · Seat A — - **⚑ FIVE PRs are green + reviewed and need one merge click each** (agent self-merge is

- suggested-id: `OQ-SUPERBOT-GAMES-FIVE-PRS-GREEN-REVIEWED`
- source: superbot-games/control/status.md @ `5a9d4d2` · heartbeat `updated:` 2026-07-11T13:19:52Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ FIVE PRs are green + reviewed and need one merge click each** (agent self-merge is
  classifier-blocked): merge **#34 first** (ends floor churn), then **#36**, **#38**, then
  **#32** & **#27** (these two need a quick rebase first). Alternative: a direct "merge them"
  instruction in the world-games session clears the gate and the lane lands all five in order.
```

### superbot-games · Seat A — - **⚑ Model-attribution (ORDER 003):** the lane records `📊 Model: Opus 4.8` (family-level, the

- suggested-id: `OQ-SUPERBOT-GAMES-MODEL-ATTRIBUTION-ORDER-003`
- source: superbot-games/control/status.md @ `5a9d4d2` · heartbeat `updated:` 2026-07-11T13:19:52Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ Model-attribution (ORDER 003):** the lane records `📊 Model: Opus 4.8` (family-level, the
  environment-reported family) on session cards, never the exact internal id, per the
  operator's don't-embed-the-id rule — confirm that's the family-level form wanted, or say if
  "Claude Opus" is preferred.
```

### superbot-games · Seat A — - **⚑ No spend / publish / external-account / production-data actions taken; no secrets in

- suggested-id: `OQ-SUPERBOT-GAMES-NO-SPEND-PUBLISH-EXTERNAL`
- source: superbot-games/control/status.md @ `5a9d4d2` · heartbeat `updated:` 2026-07-11T13:19:52Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ No spend / publish / external-account / production-data actions taken; no secrets in
  repo.** Only decide-and-flag items were: re-scoping #36 (documented) and building the
  churn-fix #34 design.
```

### ↳ superbot-games · Seat A — `control/status-exploration.md` — ⚑ needs-owner: \|

- suggested-id: `OQ-SUPERBOT-GAMES-FLAG`
- source: superbot-games/control/status-exploration.md @ `5a9d4d2` · heartbeat `updated:` 2026-07-09T20:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: |
  NOTHING BLOCKING. Gen-2 relaunch clicks (optional, in order):
  (1) paste the proposed gen-2 Custom Instructions from
  docs/gen2-custom-instructions-exploration.md §B into the relaunched Project (agents
  cannot edit Project settings); (2) create the wake routine — relaunch starts Class A
  hourly per the lane's gen-2 feedback §3 (the measured ORDER-005 pickup without a
  routine was ~2h); (3) branch-deletion housekeeping (agents 403 on branch delete):
  claude/exploration-ping-ack-005, claude/exploration-wind-down-2026-07-09 (after #13
  merges), claude/exploration-wakeup-2026-07-09, plus the older merged branches listed
  in docs/retro/project-review-2026-07-09-exploration.md §e — do NOT delete
  mining/port-pure-domain or mining/grid-encounters (live mining drafts #5/#11);
  (4) the #13 merge click ONLY IF this session's own merge-on-green failed (the PR
  records the exact error if so). Standing veto windows unchanged: D‑0007 (Q-0040
  posture, open until the P3→P4 gate), D‑0009 (CI gate; revert = veto).
```

### superbot-mineverse — ⚑ needs-owner: 1 item — provision the six env vars to switch sign-in on (and, for test-guild write mode, the …

- suggested-id: `OQ-SUPERBOT-MINEVERSE-1-ITEM-PROVISION-SIX`
- source: superbot-mineverse/control/status.md @ `76be821` · heartbeat `updated:` 2026-07-11T19:45:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: 1 item — provision the six env vars to switch sign-in on (and, for test-guild write mode, the write-endpoint pair). Structured OWNER-ACTION block below. Also owner-side, informational: review/merge your own open PR #31 (Codex security report); Builder-lane FLAGs 1+2 below stay informational until the manager picks them up; stage-5 live-prod flag remains owner-only.
```

### pokemon-mod-lab — 1. **⚑ OWNER-ACTION 1 — `ROM builds` required-check click.** GitHub →

- suggested-id: `OQ-POKEMON-MOD-LAB-1-1-ROM-BUILDS`
- source: pokemon-mod-lab/control/status.md @ `3dcb707` · heartbeat `updated:` 2026-07-11T20:03:55Z
- possibly-covered-by: none matched (manual dedup needed)

```text
1. **⚑ OWNER-ACTION 1 — `ROM builds` required-check click.** GitHub →
   Settings → Rules → `main` ruleset → require status checks → add
   `ROM builds` (keep `substrate-gate`). No agent API surface for
   rulesets (`docs/PLATFORM-LIMITS.md`).
```

### pokemon-mod-lab — 2. **⚑ OWNER-ACTION 2 — next-arc concept pick.** One word: continue

- suggested-id: `OQ-POKEMON-MOD-LAB-2-2-NEXT-ARC`
- source: pokemon-mod-lab/control/status.md @ `3dcb707` · heartbeat `updated:` 2026-07-11T20:03:55Z
- possibly-covered-by: none matched (manual dedup needed)

```text
2. **⚑ OWNER-ACTION 2 — next-arc concept pick.** One word: continue
   Emerald QoL+ (new-lead spikes) / Emerald Hard / Nuzlocke Mode
   (`docs/mod-concepts.md`). Lane default remains QoL+; reversible.
```

### pokemon-mod-lab — 3. **⚑ OWNER-ACTION 3 — playtest verdict on the 6 game-feel patches**

- suggested-id: `OQ-POKEMON-MOD-LAB-3-3-PLAYTEST-VERDICT`
- source: pokemon-mod-lab/control/status.md @ `3dcb707` · heartbeat `updated:` 2026-07-11T20:03:55Z
- possibly-covered-by: none matched (manual dedup needed)

```text
3. **⚑ OWNER-ACTION 3 — playtest verdict on the 6 game-feel patches**
   (instant text #4, auto-run #6, HP drain 3× #7, battle msg ×0.5 #7,
   egg hatch 2×/3× #21, fishing dots 2× #23) + the Match Call
   random-nag rider. One-line header flag per revert
   (`docs/build-presets.md`); hatch-128 stacking waits on this.
```

### pokemon-mod-lab — 4. **⚑ stale ref `track-a/session-019` — owner click to delete**

- suggested-id: `OQ-POKEMON-MOD-LAB-4-STALE-REF-TRACK`
- source: pokemon-mod-lab/control/status.md @ `3dcb707` · heartbeat `updated:` 2026-07-11T20:03:55Z
- possibly-covered-by: none matched (manual dedup needed)

```text
4. **⚑ stale ref `track-a/session-019` — owner click to delete**
   (content squash-merged via PR #24 long ago; sessions must not touch
   it).
```

### pokemon-mod-lab — 5. **⚑ NEW (housekeeping) — stale ref `track-a/session-024` — owner

- suggested-id: `OQ-POKEMON-MOD-LAB-5-NEW-HOUSEKEEPING-STALE`
- source: pokemon-mod-lab/control/status.md @ `3dcb707` · heartbeat `updated:` 2026-07-11T20:03:55Z
- possibly-covered-by: none matched (manual dedup needed)

```text
5. **⚑ NEW (housekeeping) — stale ref `track-a/session-024` — owner
   click to delete** (content superseded by PR #31; PR #29 closed).
   Session 041 attempted `git push origin :track-a/session-024` at
   archive time and was DENIED by the platform's auto-mode classifier
   ("[Git Destructive] ... not named or authorized by the user") — not
   retried, per playbook. Either owner-click it away alongside
   session-019, or explicitly authorize a future session to delete it.
```

### pokemon-mod-lab — - OWNER-ACTION 4 (wake-env GitHub write tools) and OWNER-ACTION 5

- suggested-id: `OQ-POKEMON-MOD-LAB-4-WAKE-ENV-GITHUB`
- source: pokemon-mod-lab/control/status.md @ `3dcb707` · heartbeat `updated:` 2026-07-11T20:03:55Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- OWNER-ACTION 4 (wake-env GitHub write tools) and OWNER-ACTION 5
  (`add_repo` classifier denials): **RESOLVED** — 18 consecutive clean
  wake cycles (024–041). Reopen only on regression.
```

### gba-homebrew — ⚑ needs-owner (carried + one NEW):

- suggested-id: `OQ-GBA-HOMEBREW-CARRIED-ONE-NEW`
- source: gba-homebrew/control/status.md @ `75ef9ba` · heartbeat `updated:` 2026-07-11T19:56:00Z (session 20 own-section update on top …
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner (carried + one NEW):
```

### gba-homebrew — - **⚑ owner-click: create the Lumen Drift GitHub Release** (worker seat

- suggested-id: `OQ-GBA-HOMEBREW-CLICK-CREATE-LUMEN-DRIFT`
- source: gba-homebrew/control/status.md @ `75ef9ba` · heartbeat `updated:` 2026-07-11T19:56:00Z (session 20 own-section update on top …
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ owner-click: create the Lumen Drift GitHub Release** (worker seat
  gets 403 on tags/releases). Suggested tag **`lumen-drift-v1.3`**. Exact
  clicks: repo → Releases → "Draft a new release" → "Choose a tag" → type
  `lumen-drift-v1.3` (create on publish, target `main`) → title
  `Lumen Drift v1.3` → attach `dist/lumen-drift.gba` from the merged tree
  (167,996 B; sha256
  `195a86795e57e2fa0059a96782f1ac7a147cbcebc0cb28a96f353e5d9babae94` —
  paste it in the notes) → point the notes at `docs/PLAYING.md` and the
  v1.3 entry in `docs/current-state.md` → Publish. (No Gloamline release
  ask yet: pre-v1; this repo's release convention has only shipped at
  scope-complete — revisit when the arc matures.)
```

### gba-homebrew — - **⚑ owner-click: merged-branch cleanup** — worker seat gets 403 on

- suggested-id: `OQ-GBA-HOMEBREW-CLICK-MERGED-BRANCH-CLEANUP`
- source: gba-homebrew/control/status.md @ `75ef9ba` · heartbeat `updated:` 2026-07-11T19:56:00Z (session 20 own-section update on top …
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ owner-click: merged-branch cleanup** — worker seat gets 403 on
  branch-delete; merged `claude/*` branches (through PR #54 and this PR
  once merged, plus earlier kit-upgrade and wake branches) can be deleted
  in one sweep from the branches page.
```

### gba-homebrew — - **⚑ owner-click (NEW): add `NDS ROM build` to the required checks**

- suggested-id: `OQ-GBA-HOMEBREW-CLICK-NEW-ADD-NDS`
- source: gba-homebrew/control/status.md @ `75ef9ba` · heartbeat `updated:` 2026-07-11T19:56:00Z (session 20 own-section update on top …
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ owner-click (NEW): add `NDS ROM build` to the required checks**
  (repo Settings → Rulesets/Branch protection). Today only the GBA "ROM
  builds" job is required, so an armed auto-merge can fire before the
  NDS proofs finish (observed on PR #54's rebase-push; recorded in
  `docs/PLATFORM-LIMITS.md`). Until clicked, lane discipline is:
  verify the post-merge `main` run is green and say so.
```

### gba-homebrew — - **⚑ graze tuning wants owner hands-on validation** — the

- suggested-id: `OQ-GBA-HOMEBREW-GRAZE-TUNING-WANTS-HANDS`
- source: gba-homebrew/control/status.md @ `75ef9ba` · heartbeat `updated:` 2026-07-11T19:56:00Z (session 20 own-section update on top …
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ graze tuning wants owner hands-on validation** — the
  400-frames-per-graze refund and the 6px shell are reasoned and
  machine-proven (CI asserts the refund and the lane geometry), but
  whether grazing FEELS right — risk-priced, readable, not exploitable —
  needs real hands on a real run. Owner-gated polish on a complete,
  shipped game. (Same invitation applies to Gloamline hand-feel:
  Shambler speed/stagger, shove push/stun/cooldown AND now barricade
  radius/hp/plank numbers await owner taste.)
```

### gba-homebrew — - ⚑ (**awareness, no click needed**) — the routine model-attribution

- suggested-id: `OQ-GBA-HOMEBREW-AWARENESS-NO-CLICK-NEEDED`
- source: gba-homebrew/control/status.md @ `75ef9ba` · heartbeat `updated:` 2026-07-11T19:56:00Z (session 20 own-section update on top …
- possibly-covered-by: none matched (manual dedup needed)

```text
- ⚑ (**awareness, no click needed**) — the routine model-attribution
  mismatch (ORDER 003 record, session 9) belongs in whatever the
  fleet-manager coordinator compiles for a report to Anthropic, alongside
  pokemon-mod-lab's parallel finding and the `websites` PR #59 precedent.
```

### product-forge — ⚑ OWNER-ACTION (OA-003, open)

- suggested-id: `OQ-PRODUCT-FORGE-OA-003-OPEN`
- source: product-forge/control/status.md @ `4fdfa8a` · heartbeat `updated:` 2026-07-11T19:39:50Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION (OA-003, open)
WHAT: turn on GitHub Pages for this repo.
WHERE: repo Settings → Pages → Source → select "GitHub Actions".
HOW: click only (no values to paste).
WHY-IT-MATTERS: makes the games-web character-sheet preview publicly viewable.
UNBLOCKS: the prepped deploy-pages workflow publishes games-web to
  https://menno420.github.io/product-forge/ on its next run.
VERIFIED-NEEDED: deploy-pages runs 29126980391 + 29128667052 both fail at
  `actions/configure-pages` ("Get Pages site failed ... Not Found"); the site returns 404
  (last verified ~2026-07-11T19:10Z). Enabling Pages is a repo-settings toggle only the
  owner can perform.
```

### idea-engine — ⚑ needs-owner: ARCHIVE HANDOFF (this slice, wrap-up — read FIRST at next wake): (1) STANDING RULING Q-0265, C…

- suggested-id: `OQ-IDEA-ENGINE-ARCHIVE-HANDOFF-THIS-SLICE`
- source: idea-engine/control/status.md @ `a9b41f6` · heartbeat `updated:` 2026-07-11T19:53:28Z (real wall-clock via date -u, per the …
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: ARCHIVE HANDOFF (this slice, wrap-up — read FIRST at next wake): (1) STANDING RULING Q-0265, CONTINUOUS-CHAINING MODE — restored DURABLY here this slice (it previously lived only in session cards, grep of this file was negative): the coordinator chains bounded slices CONTINUOUSLY via child sessions, the next slice dispatching as each one reports; the 2-hourly cron trigger is a FAILSAFE DEADMAN WAKE, not the work cadence (README § Coordination; first recorded live in this file @ 139932e). The archiving coordinator's failsafe cron trigger AND its 15-minute send_later chain are being DISMANTLED with the chat archive — a fresh coordinator MUST RE-ARM BOTH per Q-0265 at first wake. (2) THE ≤07-13 OWNER SITTING BUNDLE (context: Projects are free through 2026-07-14, the owner consolidates after — decide ≤2026-07-13): FOUR decisions in ONE sitting — (a) Lumen Drift itch.io go/no-go (standing OWNER-ACTION entry below), (b) pokemon playtest verdicts (fm docs/owner-queue.md item 3), (c) the gba concept pick (the lane's own heartbeat ⚑), (d) the post-EAP standing-routine posture (standing entry below — RECOMMENDED Option A). (3) WEBSITES CUTOVER choice — one structured reply, RECOMMENDED Option A (the standing entry below, first item). The standing entries follow VERBATIM from the prior overwrite: STANDING (routed by #159, preserved verbatim this slice again) — WEBSITES CUTOVER-ROLE, one structured choice (fan-in of the websites lane's own OWNER-ACTIONS rows 6/4/1 @ 92c3dc6 — the canonical rows STAY on the lane's surface; this entry only bundles three rows that are really ONE decision into a single paste-ready sitting, per the fewer-clearer-asks hygiene): ⚑ OWNER-ACTION WHAT: one reply deciding the websites cutover role — go/no-go on retiring superbot's old dashboard/ + botsite/ site services, where bot control lives (websites / superbot / superbot-next), and (optionally) domains. WHERE: reply in any owner channel the manager sweep reads; the lane executes from its own list — menno420/websites docs/owner/OWNER-ACTIONS.md rows 1/4/6 (optional 2-min pre-check first: open the three live site URLs linked from the websites README, or have the lane run its scripts/healthcheck.py — its own row 6 asks for exactly that verify-then-go). HOW (paste ONE line — recommendation first): RECOMMENDED "Cutover Option A: go — retire superbot's dashboard/ + botsite/ services; the new sites keep reading old-repo data until the bot cutover; bot control home = superbot-next (ruled now, wired later); domains stay deferred." · Alternatives: "Option B: botsite-only go now, dashboard later" (the lane plan's own site order) · "Option C: hold everything for one combined cutover when superbot-next reaches parity" (zero clicks now; cost = dual-maintenance for the parity months) · "Option D: no-go — deliberately keep dual-running." WHY-IT-MATTERS: the replacements are live and verified daily (all three services deploy-verified at websites 1ff77e4); while the call is unmade you pay dual maintenance on old+new sites and the de-facto answer bakes in. UNBLOCKS: websites rework-plan steps 3/5 (retiring the last dual-running old-repo web surfaces), the Q4 control-panel wiring path, domain assignment — and closes this repo's superbot #155 shortlist item 2 for good. VERIFIED-NEEDED: owner-gated by rule, not capability — the lane's own surface marks the retirement "Gated: needs your go" (OWNER-ACTIONS row 6 @ 92c3dc6) and the control home "Do not port without an owner call" (row 1); its question-router Q6 reads "(unanswered — deferred to cutover)"; DNS/service retirement are owner-only Railway/DNS mutations (the lane's D‑0005 class), deliberately not attempted from any agent seat. ALSO STANDING (preserved verbatim from #158): SELF-REVIEW 2026-07-11 (ORDER 002): owner items collected in the Self-review record at docs/retro/self-review-2026-07-11.md (moved verbatim from the foot of this file at the 2026-07-11 wrap-up) — the ≤2026-07-14 sitting bundle (FOUR decisions as of #174, standing entries below) + the venture-lab two repo toggles (#110) + the Q-0266 framing veto window. Prior text verbatim: SHARED-WINDOW NOTE UPDATE (this slice, same fewer-clearer-asks hygiene): the gba-homebrew CONCEPT PICK (lane ⚑ @ c7592d6 — Lumen-deepening / Clockwork Courier / Shoal, full click path on the lane's own heartbeat; seeded-cave-runs is now the costed 'more Lumen' option, this slice's park) is the THIRD item landing in the SAME ≤2026-07-14 EAP sitting — deliberately NOT a new ⚑ here, the ask lives on the LANE's own heartbeat (one ask, one owner surface); the sweep should read the sitting as carrying FOUR bundled decisions: (1) the Lumen Drift itch.io go/no-go standing entry below, (2) fm docs/owner-queue.md item 3 (pokemon playtest verdicts), (3) the gba concept pick, (4) the post-EAP routine posture (#174's entry, below). The prior note follows verbatim: SHARED-WINDOW NOTE (this slice, hygiene per fewer-clearer-asks): the pokemon-mod-lab playtest-kit park (this slice) is deliberately NOT a new ⚑ here — its owner ask already lives as fm docs/owner-queue.md item 3 @ 1afca50 (one ask, one owner surface, the manager's); what the sweep must see is that BOTH owner-sitting items — the Lumen Drift ⚑ OWNER-ACTION below AND that queue item — land in the SAME EAP sitting, window ends 2026-07-14; the kit-preparation routing (fm order or lane self-serve) is the manager-side item flagged in notes. The standing entry follows verbatim: ⚑ OWNER-ACTION (from this slice, decision-adjacent — EAP window ends 2026-07-14): WHAT: post-EAP go/no-go + one itch.io sitting to publish Lumen Drift as a PWYW listing. WHERE: itch.io (account) + gba-homebrew dist/lumen-drift.gba v1.3 (sha256 195a867…, provenance dist/README.md) + the parked idea ideas/venture-lab/games-adjacent-candidate-three-2026-07-10.md. HOW: play Lumen Drift during the EAP sitting; on go: create itch.io account → New project → set pay-what-you-want → upload dist/lumen-drift.gba → publish (venture-lab pre-drafts the full listing copy so this is paste-and-click). WHY-IT-MATTERS: first second-channel distribution datapoint + a publish pipeline every finished fleet game inherits, at zero build cost. UNBLOCKS: the parked candidate #3, venture-lab's listing-kit prep, and gives revenue-ingestion-owner-relay its first non-marketplace source. Sequencing note (from the #97-era probe): the click need NOT wait on the revenue-ingestion relay — itch.io/marketplace sales exports are retro-downloadable, so pre-relay sales stay recoverable; the lane lands the ledger convention independently (fan-in below, flagged ORDER-worthy). VERIFIED-NEEDED: account creation/external publishing is rail-banned for agents on both lanes' READMEs (venture-lab @ 0ad0ea4, gba-homebrew @ 31c8672) — owner-only by rule, not by missing capability. ALSO note for the :30 sweep: the wake-resilience verdict (PR #56) is gated on an owner click that already lives as a six-field OWNER-ACTION entry on the TRADING-STRATEGY lane's own heartbeat @ `d0d789e` (⚑ (b): paste environments/setup-universal.sh into that project's environment setup-script field); deliberately NOT duplicated here per the fewer-clearer-asks hygiene — one ask, one owner surface, the lane's. Routed via the trading-strategy fan-in note below. SAME hygiene for venture-lab's ⚑B/⚑D publish clicks (launch-ready, UNFROZEN @ `9f1b616`) — they live as owner-action entries on the LANE's own docs/launch/membership-kit/owner-actions.md, deliberately NOT duplicated here; routed via the venture-lab fan-in note below. STANDING FROM #174 (decision 4 of the ≤07-14 sitting): ⚑ OWNER-ACTION (from #174, HARD deadline — decide ≤2026-07-13, EAP window wraps 2026-07-14): WHAT: one reply setting the post-EAP standing-routine posture — what keeps firing on paid usage after 07-14. WHERE: reply in any owner channel the manager sweep reads; execution is manager-side trigger edits (roster gen #5 @ fm 7c13be7: 32 enabled = 15 standing crons + 2 poke-only + 15 one-shots). HOW (paste ONE line — recommendation first): RECOMMENDED "Post-EAP routines Option A: core-6 Projects keep current cadence (per Q-0261), every other standing cron drops to daily, one-shots expire on completion; revisit at first paid invoice." · Alternatives: "Option B: keep all 15 standing crons as-is (accept unmetered paid burn)" · "Option C: freeze all crons at window close; owner wakes lanes manually" · "Option D: name a monthly budget figure; manager thins cadence to fit and reports the cut list." WHY-IT-MATTERS: with no ruling, Option B happens by inertia — every cron fires into the paid period at a burn no agent can measure (fm fleet-economics honest-nulls: token/$ "not measurable"). UNBLOCKS: the manager's pre-close cadence sweep; closes the open post-EAP pricing question (superbot projects-eap-product-review-2026-07-07.md:150); the mechanical limit-deferred half proceeds independently as superbot's plan (PR #1845). VERIFIED-NEEDED: owner-only by evidence — no post-EAP budget ruling exists anywhere (full-tree greps of fresh clones superbot @ 9f46cb7 + fleet-manager @ 7c13be7 at #174; only the open question and Q-0261's "until the EAP ends" boundary), and spend/billing surfaces are owner-UI-only (fm model-matrix: no agent-visible field on any probed surface).
```

### codetool-lab-opus4.8 — ⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTI…

- suggested-id: `OQ-CODETOOL-LAB-OPUS4-8-1-DELETE-LEFTOVER-BRANCH`
- source: codetool-lab-opus4.8/control/status.md @ `80f6cd1` · heartbeat `updated:` 2026-07-09T20:11:35Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTIONAL PyPI publish of mdverify (needs owner token; name free as of 2026-07-09); (3) OPTIONAL Claude GitHub App connect for native tag/release
```

### fleet-manager (this repo) — - **⚑ Decide-and-flag decisions (owner/coordinator may redirect):**

- suggested-id: `OQ-FLEET-MANAGER-DECIDE-FLAG-DECISIONS-COORDINATOR`
- source: fleet-manager/control/status.md @ `70c9520` · heartbeat `updated:` 2026-07-11T20:00:00Z — P2 QUEUE GENERATION SHIPPED (fleet c…
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ Decide-and-flag decisions (owner/coordinator may redirect):**
  (a) feed path `docs/owner-queue-candidates.md` (plan names no path);
  (b) feed badge `living-ledger` (kit vocabulary has no `generated` token);
  (c) ONE verbatim-quoting deviation in the feed: `D-NNN…` decision-id
  hyphens swapped to U+2011 so quotations never trip the kit's
  one-home stamp discipline (same class as P1's api_token_hint strip);
  (d) prober severity REPORT-ONLY (plan leaves it unstated);
  (e) session transport fallback: api.github.com is proxy-403 in agent
  sessions (verbatim wall recorded in the script) → github.com HTML
  state-marker fallback, Actions keeps the API path;
  (f) positional-ref lint covers THIS repo's living config surfaces only —
  the plan's cross-repo `owner-queue item <N>` lint rides P3 (DEVIATION,
  partial); `projects/UNIVERSAL.md` excluded (owner-provenance, frozen
  provenance notes);
  (g) only ACTIVE numbered items slugged; Parked/Resolved bullets keep their
  prose form until touched.
- **Roster gen #8** committed in-branch (fresh full regen; same rows feed
  both files — freshness had NOT tripped, this was the feed's first
  generation run, doubling as a gen_roster verification pass: no walls, all
  repos converged).
```

### fleet-manager (this repo) — - **⚑ Drift flagged for follow-up (spotted, out of this bounded slice):**

- suggested-id: `OQ-FLEET-MANAGER-DRIFT-FLAGGED-FOLLOW-UP`
- source: fleet-manager/control/status.md @ `70c9520` · heartbeat `updated:` 2026-07-11T20:00:00Z — P2 QUEUE GENERATION SHIPPED (fleet c…
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ Drift flagged for follow-up (spotted, out of this bounded slice):**
  the 2026-07-10 `projects/gba-homebrew/` + `projects/pokemon-mod-lab/`
  packages record their cadence as "`0 */2` spec'd — NOT armed" and the
  hourly ORDER 002s as unexecuted/superseded — stale since 01:36Z; those
  two packages need regeneration against the live retro seat.
- **Owner-queue item 17 filed** — re-paste the consolidated `environments/`
  setup scripts (PR #73 → `cf2c4ee`) into the running environments,
  coordinator environment FIRST (activates the superbot-next→python3.11
  fix, inert until re-pasted); click-level with raw URLs per archetype.
- **superbot-games nudge sent ~13:1xZ 2026-07-11** — seat alive but idle
  02:15Z→13:00Z (12 silent wakes); a direct task list was delivered to the
  seat; escalation path: rebuild the seat from its registry package
  (`projects/superbot-games/`, v2) if 2 more idle wakes pass.
```

### fleet-manager (this repo) — ⚑ **only 3/13 lanes (substrate-kit, superbot, idea-engine) have

- suggested-id: `OQ-FLEET-MANAGER-ONLY-3-13-LANES`
- source: fleet-manager/control/status.md @ `70c9520` · heartbeat `updated:` 2026-07-11T20:00:00Z — P2 QUEUE GENERATION SHIPPED (fleet c…
- possibly-covered-by: none matched (manual dedup needed)

```text
  ⚑ **only 3/13 lanes (substrate-kit, superbot, idea-engine) have
  auto-merge-enabler.yml installed**; allow_auto_merge + required checks NOT
  MEASURABLE this session (no repo-get/branch-protection MCP tool; direct REST
  403 "GitHub access is not enabled for this session" — walls quoted verbatim
  in the doc).
- **PR #68 PARKED READY+green** — the dispatched agent merge of PR #68 was
  classifier-denied ("[Self-Approval]/[Merge Without Review]", verbatim in the
  findings doc §"Live confirmation (same day)"); fm has NO enabler installed
  (per the verification table), so there is no server-side arm path either →
  **a non-author landing is needed**. Direct live evidence for the §2.4
  corrected clause and for retiring the fm `instructions.md:76`-vs-`:85`
  "REST merge-on-green is PRIMARY" contradiction (audit §3.2).
```

### fleet-manager (this repo) — - **⚑ Self-decided design decisions (decide-and-flag, owner/coordinator may

- suggested-id: `OQ-FLEET-MANAGER-SELF-DECIDED-DESIGN-DECISIONS`
- source: fleet-manager/control/status.md @ `70c9520` · heartbeat `updated:` 2026-07-11T20:00:00Z — P2 QUEUE GENERATION SHIPPED (fleet c…
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ Self-decided design decisions (decide-and-flag, owner/coordinator may
  redirect):** (1) landed at `scripts/gen_roster.py` per the coordinator
  dispatch — the proposal + gens #1–#4 said `tools/gen_roster.py`; dispatch won,
  flagged for consistency; (2) in-script `LANES` registry (19 seats incl.
  registry-only retro-games + archived codetool ×3) is the one hand-maintained
  input — add a lane there when a seat is born; (3) verdict ladder codified:
  FRESH ≤2× wake cadence (cadence parsed from the matched cron, 2h default),
  STALE >2×cadence ≤24h, DARK >24h, DEAD = not measurable; archived lanes report
  STALE-BY-DESIGN; (4) `--check` byte-compares full output — Age is computed
  against `--date`, so reproducibility requires passing the committed
  generation's args (documented in usage); (5) Deltas-vs-previous-generation
  narrative deliberately NOT auto-derived (coordinator judgment, per the
  proposal's "what stays human"); (6) `tmp-triggers.json` added to `.gitignore`
  so the documented export filename can never be committed by accident (raw
  export stays uncommitted per the dispatch).
- Usage doc = the script's own header docstring (schema, verdict ladder,
  transport doctrine, all three modes with example invocations).
- Walls: none this slice (pokemon-mod-lab private repo read fine over git
  transport; all 18 repo fetches converged on the first attempt this run).
```

### fleet-manager (this repo) — **⚑ PHASE-2 DECISION flagged above** (roster canonical; manifest → pointer stub;

- suggested-id: `OQ-FLEET-MANAGER-PHASE-2-DECISION-FLAGGED`
- source: fleet-manager/control/status.md @ `70c9520` · heartbeat `updated:` 2026-07-11T20:00:00Z — P2 QUEUE GENERATION SHIPPED (fleet c…
- possibly-covered-by: none matched (manual dedup needed)

```text
  **⚑ PHASE-2 DECISION flagged above** (roster canonical; manifest → pointer stub;
  checker retires) — superbot repo NOT edited this slice; follow-up order owed.
- **Ladder item 7 DONE (executed by a dispatched worker, coordinator
  cse_012o8pySy5K3AV6JWoPKryZL): superbot#1920 @codex re-ask posted
  2026-07-11T01:45Z as comment 4941269996** — the original ask re-issued verbatim
  after the Codex quota refusal (comment 4939891407); verified present in the
  re-fetched thread; no prior Codex answer existed — the RETRY-LATER doctrine held.
- **Walls hit this slice (verbatim class):** GitHub MCP `get_file_contents` on
  superbot-idle / superbot-mineverse → `Access denied: repository … is not configured
  for this session` (both repos absent from this seat's allowed-repo list; worked
  around via shallow clone over git transport — no roster gap). `superbot-retro`
  ls-remote → `fatal: could not read Username` (repo does not exist / not accessible:
  the retro seat is registry-only, recorded as such in the roster).
```

### fleet-manager (this repo) — > **⚑ RECONCILIATION FLAG (decide-and-flag, per the ORDER 015 re-scope —

- suggested-id: `OQ-FLEET-MANAGER-RECONCILIATION-FLAG-DECIDE-FLAG`
- source: fleet-manager/control/status.md @ `70c9520` · heartbeat `updated:` 2026-07-11T20:00:00Z — P2 QUEUE GENERATION SHIPPED (fleet c…
- possibly-covered-by: none matched (manual dedup needed)

```text
> **⚑ RECONCILIATION FLAG (decide-and-flag, per the ORDER 015 re-scope —
> `docs/succession/coordinator-handoff-2026-07-11.md` §5): ORDER 015's
> registry packages were CENTRALIZED FROM the self-booted seats, NOT AUTHORED
> as founding packages.** Reality overtook the order's filing (00:45Z): both
> games seats booted themselves before any founding package existed, so the
> executed done-when is "sweep what the booted seats ACTUALLY run into
> version-stamped `projects/` packages, regenerate-don't-fork" — the order's
> original done-when items (owner-queue paste-wave refresh for boots, boot
> clicks queued WHAT/WHERE/UNBLOCKS) are MOOT: no boots remain to click. Every
> never-deployed package part says so explicitly instead of inventing content
> (registry doctrine 1). Owner may veto/redirect any of this reading.
```

### fleet-manager (this repo) — ⚑B/⚑D unfrozen; what remains is the OWNER side (parked merges + publish clicks,

- suggested-id: `OQ-FLEET-MANAGER-B-D-UNFROZEN-WHAT`
- source: fleet-manager/control/status.md @ `70c9520` · heartbeat `updated:` 2026-07-11T20:00:00Z — P2 QUEUE GENERATION SHIPPED (fleet c…
- possibly-covered-by: none matched (manual dedup needed)

```text
  ⚑B/⚑D unfrozen; what remains is the OWNER side (parked merges + publish clicks,
  per the lane's own heartbeat @ `2021bab`).
- **ORDER 010 relay: ✅ EXECUTED (PR #63)** — the per-lane template/card checks +
  ground-truth self-report ORDER is APPENDED at 11 lane inboxes (no longer "rides
  each next lane contact"; slice record above), **including the trading#21 residue
  annotation suggestion (the two undocumented P1 drops, AAPL-SMA/AAPL-MACD — now
  trading ORDER 009, PR #52)**. Residual: superbot (no inbox — decide-and-flag
  surface recommended) + superbot-idle/superbot-mineverse (session-scope wall)
  ride next contact.
- **Review-queue drain:** trading#21 CLOSED this slice (RETIRED-SUPERSEDED — first
  closed row). Open rows: venture-lab#9 (awaits the lane's P0 fix) ·
  ~~superbot-games#16~~ (CLOSED at #58 — order-001 MERGED, PR #24 `7d4c347`) ·
  superbot-games#5 (verbatim-port read; 4 import-only modules) · trading#36 (ordinary
  drain) · superbot#1920 (**@codex re-ask POSTED 01:45Z, comment 4941269996 — await
  the answer**; botsite/in-repo half owed) · pokemon#8 · gba#12. **Next
  manager-verify candidate: pokemon#8 (sha1-chain from committed proof fixtures) or
  gba#12 (dispatch-tier asserts vs compile-only CI).** fleet-manager Codex env ask
  still open on PR #26.
- **sim-lab tag-push 403:** new platform wall recorded on its heartbeat — candidate
  for the capability ledger + a kit-side release-route note at next kit contact.
- **substrate-kit trigger naming:** ~~cutover relay owed~~ **RESOLVED — verified at
  gen #3** (failsafe wake live 23:09:56Z).
- Owner morning click-list: **docs/owner-queue.md**.
- EAP free window through 2026-07-14; economics ledger banked (#27).
```

### fleet-manager (this repo) — ⚑ needs-owner (was the PENDING-OWNER FIVE at archive; item 1 RESOLVED 2026-07-11 ~01:0xZ — full detail handof…

- suggested-id: `OQ-FLEET-MANAGER-WAS-PENDING-FIVE-AT`
- source: fleet-manager/control/status.md @ `70c9520` · heartbeat `updated:` 2026-07-11T20:00:00Z — P2 QUEUE GENERATION SHIPPED (fleet c…
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner (was the PENDING-OWNER FIVE at archive; item 1 RESOLVED 2026-07-11 ~01:0xZ — full detail handoff §3 + docs/owner-queue.md): **(1) ~~paste `projects/fleet-manager/reboot-prompt.md` into a fresh coordinator chat~~ ✅ RESOLVED — successor seat LIVE, F-1 cutover complete (record above) · (2) ~~venture-lab fresh session~~ ✅ RESOLVED at gen #4 (lane relaunched — failsafe 00:30:36Z, ORDERs 001–004 done, ⚑B/⚑D UNFROZEN; the owner's remaining venture clicks are the lane's own parked merges + publish clicks) · (3) `superbot-plugin-hello` seeded-package push (repo still EMPTY at 00:07Z ls-remote) · (4) attended-session permissions re-land (grant landed `c23223f`; the built fold DIED with this container — rebuild recipe handoff §4; PR #47 = born-red card only, the re-land vehicle or close-with-reason) · (5) games mapping §5 late-veto window (accepted-by-boot otherwise)**; then the package paste wave (owner-queue item 13 — HELD on (4): paste the folded v2 texts, not v1s) + product-forge Pages click (item 15)
PROMPT REGISTRY: **fleet-manager `projects/` — canonical, v-stamped (v1 · 2026-07-10 on all 39 prompt files); superbot founding-package copies frozen** (superseded-banner PR superbot #1967); one-writer = manager, lanes propose via ⚑/INTAKE; first full trigger snapshot committed at `projects/_inventory/trigger-registry-2026-07-10.md` (114 triggers; live sweep now 175 records / 23 enabled — see roster gen #3); websites v1-era prompt CONFIRMED deployed — v2 re-paste still owed. **Permissions v2/v3 re-stamp: owner provenance landed (`c23223f`); per-repo re-land in flight (PR #47) — not yet live at this write.**
```

### fleet-manager (this repo) — - **⚑ ESCALATION carried in the roster:** nine lane failsafes auto-disabled

- suggested-id: `OQ-FLEET-MANAGER-ESCALATION-CARRIED-ROSTER-NINE`
- source: fleet-manager/control/status.md @ `70c9520` · heartbeat `updated:` 2026-07-11T20:00:00Z — P2 QUEUE GENERATION SHIPPED (fleet c…
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ ESCALATION carried in the roster:** nine lane failsafes auto-disabled
  (`auto_disabled_env_deleted`, ~14:45–16:16Z); only superbot-next re-armed
  (`trig_01GLBYyf4aDS6AwpLVybZvVy`). 8 live lanes chain-only; product-forge (idle ~8h, dead
  failsafe) is the top DARK candidate for gen #7 — re-arm decision needed.
- **Self-review sweep state:** answered = sim-lab (87ca0dfb), superbot-games (201f8dd),
  trading (ed8add3), venture-lab (dfe3332 status); **still missing = superbot hub** (ORDER
  002 `status: new` at d647b2e despite hub-touching sessions since).
- **fm PR #77:** MERGED by the owner into main as `39b888a` (18:40:11Z) — the parked-hold
  described in the 17:05Z stamp above is RESOLVED; this record supersedes it.
- Slice record: `.sessions/2026-07-11-roster-gen-6.md`.
```

---

69 candidate block(s) across 16 lane(s). Feed is additive-noise-tolerant by design: over-capture is curated out by the manager; silent stranding is the failure this feed exists to kill.

