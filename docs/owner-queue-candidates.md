# Owner-queue candidate feed — GENERATED

> **Status:** `living-ledger`
>
> **GENERATED — NOT SOURCE OF TRUTH; the manager curates `docs/owner-queue.md` from it.** Do not hand-edit; regenerated with the roster on every regen (`scripts/gen_roster.py`, P2 — centralization plan §3b).
>
> **Generation #19** · generated-at **2026-07-12T18:44Z** · by machine generation (scripts/gen_roster.py), dispatched by (not stated)
>
> Every block below is a VERBATIM `⚑ needs-owner` / `OWNER-ACTION` extraction from a lane heartbeat (`control/status*.md` at the ls-remote-verified HEAD the roster row cites). Nothing here lands in the owner queue automatically: the manager dedups, verifies (R17), and curates. `suggested-id` is a deterministic content-derived slug the manager may adopt; `possibly-covered-by` lists active queue ids citing the same PR — `none matched` means manual dedup is still needed.

### superbot (hub) — ⚑ needs-owner: none new hub-specific (verified against fm docs/owner-queue.md @ 7ff1f75 — the hub's owner tai…

- suggested-id: `OQ-SUPERBOT-NONE-NEW-HUB-SPECIFIC`
- source: superbot/control/status.md @ `5c84ce2` · heartbeat `updated:` 2026-07-11T19:45:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: none new hub-specific (verified against fm docs/owner-queue.md @ 7ff1f75 — the hub's owner tail is already queued there). Manager-sweep note, NOT an owner click: fm owner-queue C#20's manager note (superbot codex-final-review invalid YAML) is RESOLVED by superbot PR #1995 (8214200) — retire that line at the next sweep.
```

### superbot-next — ⚑ needs-owner: THREE live OWNER-ACTION items below (six-field format per control/README.md) — item 2 DROPPED …

- suggested-id: `OQ-SUPERBOT-NEXT-THREE-LIVE-ITEMS-BELOW`
- source: superbot-next/control/status.md @ `b7a0513` · heartbeat `updated:` 2026-07-12T18:30Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: THREE live OWNER-ACTION items below (six-field format per control/README.md) — item 2 DROPPED 2026-07-12 per ORDER 014's done-when (the owner created the repo; seeded at `bbaccec5` — record below; items keep their numbers, no renumbering); item 3 unchanged; item 5 (band-7 AI key envelope — the live-NL leg is blocked on it); item 6 NEW at close-out: fleet failsafes may still be dead from the 2026-07-11T16:31Z platform env-teardown (this lane self-healed; sibling lanes could not be — record in docs/retro/q0265-routine-loop-2026-07-11.md); item 4 stays RETIRED, its capacity half now FLAPPING rather than walled (usage-limit replies on #148/#151/#152 but full P2 reviews on #154/#157/#160 the same morning; flap update in the item 4 record). The ORDER-013 "Self-review 2026-07-11" section below MIRRORS all three live items click-level plus one FYI (codex phantom-artifact claims, Q-0120 guard holds) for the manager sweep
```

### superbot-next — - OWNER-ACTION 2 DROPPED below per the done-when ("the ask is gone"); the owner had created the repo (list_re…

- suggested-id: `OQ-SUPERBOT-NEXT-2-DROPPED-BELOW-PER`
- source: superbot-next/control/status.md @ `b7a0513` · heartbeat `updated:` 2026-07-12T18:30Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- OWNER-ACTION 2 DROPPED below per the done-when ("the ask is gone"); the owner had created the repo (list_repos: menno420/superbot-plugin-hello, public, pushed_at 2026-07-10T16:03:04Z, empty until this seed). Items 3/5/6 keep their numbers.
- Session card `.sessions/2026-07-12-order-014-plugin-hello-seed.md` + its telemetry/model-usage.jsonl row ride THIS PR (Q-0194).
```

### superbot-next — - ⚑ CORPUS RETIREMENT FLAG (prominent by design — owner-vetoable, REVERSIBLE; now THREE executed): #249 retir…

- suggested-id: `OQ-SUPERBOT-NEXT-CORPUS-RETIREMENT-FLAG-PROMINENT`
- source: superbot-next/control/status.md @ `b7a0513` · heartbeat `updated:` 2026-07-12T18:30Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- ⚑ CORPUS RETIREMENT FLAG (prominent by design — owner-vetoable, REVERSIBLE; now THREE executed): #249 retired sweep_cog (471→470, the program's FIRST — grounds: the admin.py deploy-ops declaration + the diagnostic_bot_status/system_info precedent) and #258 retired sweep_query_logs + sweep_recent_errors (470→468 — the process-state log-ring class). Accounting at HEAD: corpus 468 = 465 imported + 6 minted − 3 retired (parity.yml minted_goldens 6 / retired_goldens 3). Veto path per retirement: restore the golden from git history, drop its `_sweep_skips.json` entry, re-raise the count pins — nothing else moved with them.
- REMAINING map (truth at HEAD `9ae4902`, RESOLVED — the wave-9 working map is fully executed): `_unmapped` 41 files, ALL OWNER-PARKED — 40 D‑0043 deep-systems files (25 mining-deep + 15 fishing-gear; the per-domain pending-terminal lists in sb/domain/{mining,fishing}/service.py are the D‑0043 successor port's exact scope) + 1 btd6 sweep_paragon (band-7 shelf). NO workable parity item remains; a fully-green report job needs exactly TWO owner decisions: (1) the D‑0043 deep-systems port go/no-go, (2) the sweep_paragon disposition (port with a band-7 btd6 slice, or retire/park by ruling).
- LANE COMPLETE: no open PRs, no unmerged wave9/* work beyond this wrap-up, no control/claims/ files from this lane; interleaved sibling merges in the wave window (other lanes, zero golden movement): #251/#260 kit v1.13.0/v1.14.0, #256 program review, #257 ORDER-014, #259 ORDER-015, #262 cross-project requests, #268 sim-lab review, #271 admin-surface audit, #273 ORDER 016 runtime-smoke merge gate.
```

### superbot-next — ⚑ OWNER-ACTION 3 — kill the branch-update merge dance

- suggested-id: `OQ-SUPERBOT-NEXT-3-KILL-BRANCH-UPDATE`
- source: superbot-next/control/status.md @ `b7a0513` · heartbeat `updated:` 2026-07-12T18:30Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 3 — kill the branch-update merge dance
WHAT: Change the repo merge settings so PRs stop needing a manual "update branch" click before merging.
WHERE: github.com/menno420/superbot-next → Settings → Rules/Rulesets (or Settings → General → merge queue).
HOW: enable the merge queue, or drop the require-up-to-date rule for `docs/**` + `control/**` paths.
RISK: ↩️ reversible — re-disable the merge queue / re-add the require-up-to-date rule in the same Settings screen to undo.
WHY-IT-MATTERS: every session lost time to the update-branch dance and one session's tail was stranded on it (PRs #86/#87), and the same dance triggered a rate-limit stall.
UNBLOCKS: unattended session wrap-ups; less API traffic.
VERIFIED-NEEDED: repo Settings/Rulesets are admin-only — agent tokens can read but not modify rulesets (the #86/#87 stranding is the captured evidence of the wall in effect); an agent re-verified it cannot edit the ruleset when un-stranding those PRs.
```

### superbot-next — ⚑ OWNER-ACTION 4 — RETIRED 2026-07-11 (was: configure Codex for this repo — environment + code-review capacit…

- suggested-id: `OQ-SUPERBOT-NEXT-4-RETIRED-2026-07`
- source: superbot-next/control/status.md @ `b7a0513` · heartbeat `updated:` 2026-07-12T18:30Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 4 — RETIRED 2026-07-11 (was: configure Codex for this repo — environment + code-review capacity)
RESOLVED owner-side, both halves: the connector produced a FULL substantive review on #138 — comment 4941074976 (line-anchored walkthrough of all four changes; it ran the PR's 4 new tests itself, ✅) + verdict comment 4941104857 "Codex Review: Didn't find any major issues. Nice work!" (reviewed commit `77f9345`) — so the environment exists AND code-review capacity is restored. Historical evidence trail (kept for the record): "create an environment for this repo" on #117 (comment 4939224869) and #120 (comment 4939692286); "reached your Codex usage limits" on #124 (comment 4940004903), #125 (comment 4940095408) and #130 (comment 4940441924); no text reply on #114 (comment 4938835129) and #133 (comment 4940819831). The Q-0259/Q-0120 return path is now LIVE; the standing rule continues unchanged — @codex question on every substantive PR's final head, merge on green without waiting (Q-0258). REGRESSION NOTE (2026-07-11 late-night, folded at the 05:01Z heartbeat): the CAPACITY half is back at the wall — the connector answered BOTH band-7 questions with usage-limit replies: #148 comment 4942100526 ("You have reached your Codex usage limits") and #151 comment 4942514698 ("…usage limits for code reviews"). The environment half stays resolved (the #138 full review proved it exists), so this item stays RETIRED rather than reopened — but the owner may want to know the credit pool drained again the same day it was declared restored; until it refills, substantive questions keep landing per the standing rule and simply queue unanswered (the #148/#151 questions are in the open-questions note below). FLAP UPDATE (2026-07-11 morning, folded at the 06:35Z heartbeat): the pool REFILLED within the hour — one more usage-limit reply on #152 (comment 4942577962, 05:08Z), then FULL substantive P2 reviews on #154 (review 4676723779, 05:54Z, 2 P2s, final head `43b9b44`) and #157 (review 4676836079, 06:31Z, 1 P2, final head `f8532ef`). Item stays RETIRED; the capacity half is best described as FLAPPING — reviews arrive post-merge when the pool happens to be up (findings ledgered in the wave-5 records above).
RISK: ✅ safe / read-only — item RETIRED, no manual step remains; the block is kept for the evidence trail only.
```

### superbot-next — ⚑ OWNER-ACTION 5 — provide the band-7 AI key envelope (live-NL leg)

- suggested-id: `OQ-SUPERBOT-NEXT-5-PROVIDE-BAND-7`
- source: superbot-next/control/status.md @ `b7a0513` · heartbeat `updated:` 2026-07-12T18:30Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 5 — provide the band-7 AI key envelope (live-NL leg)
WHAT: Put a real `ANTHROPIC_API_KEY` in the agents' session environment and turn `AI_ENABLED` on for the live-drive guild.
WHERE: the Claude Code session environment the builder lanes run in (same place `DISCORD_BOT_TOKEN_PRODUCTION` already lives) — config seam sb/spec/config.py:166 (`ANTHROPIC_API_KEY`, SecretSpec, activation_link `ai.on_when_keyed`) and :148 (`AI_ENABLED`, default False, dormant posture).
HOW: export both vars into the session env (key value never recorded in-repo — env var NAME only, the §0.4 grant convention); optionally scope `AI_ENABLED=true` to the Superbot Admin live-drive guild posture.
RISK: ↩️ reversible — unset `ANTHROPIC_API_KEY` / set `AI_ENABLED=false` in the same env surface to undo; the key value never lands in-repo.
WHY-IT-MATTERS: band 7's remaining legs — the live NL shell (mention→answer), `verify_and_regenerate_once`, and live routing — need a real model call to produce live-drive evidence; deterministic surfaces shipped regardless (#151), so this gates EVIDENCE, not code.
UNBLOCKS: the band-7 live-NL slice's ORDER 004 live-drive leg; until provided, those legs can only ship deterministic-provider tests (A-17 posture), not live-drive proof.
VERIFIED-NEEDED: verified during #151's ORDER 004 live drive — `ANTHROPIC_API_KEY` absent and `AI_ENABLED` off in the session env (PR #151 body, key-gap honesty section); the deterministic operator surface went live regardless (six real posts). An `OPENAI_API_KEY` exists in the sandbox env but arming NL on it was explicitly out of scope and the shipped default provider posture is deterministic.
```

### superbot-next — ⚑ OWNER-ACTION 6 — re-arm the fleet's dead failsafe routines (2026-07-11T16:31Z env-teardown fallout)

- suggested-id: `OQ-SUPERBOT-NEXT-6-RE-ARM-FLEET`
- source: superbot-next/control/status.md @ `b7a0513` · heartbeat `updated:` 2026-07-12T18:30Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 6 — re-arm the fleet's dead failsafe routines (2026-07-11T16:31Z env-teardown fallout)
WHAT: Check every lane's scheduled Routines and re-create the ones the platform teardown auto-disabled.
WHERE: the Claude Routines/schedules surface for each Project (or ask each lane's next fired session to self-check via list_triggers).
HOW: for each affected lane (substrate-kit, trading-strategy, sim-lab, idea-engine, product-forge; venture-lab/superbot-games/superbot-idle also touched) look for triggers with ended_reason "auto_disabled_env_deleted" and re-arm per that lane's recorded routine text; THIS lane needs nothing until un-archived (its loop was deliberately DISARMED at close-out — re-arm recipe in docs/retro/q0265-routine-loop-2026-07-11.md).
RISK: ↩️ reversible — delete (or pause) any re-created Routine to undo; checking trigger state is read-only.
WHY-IT-MATTERS: a lane whose failsafe is dead never wakes on its own — it goes dark silently, not red.
UNBLOCKS: the standing autonomous core's sibling lanes resuming their loops.
VERIFIED-NEEDED: a platform ENV TEARDOWN at 2026-07-11T16:31Z auto-disabled scheduled triggers fleet-wide (ended_reason "auto_disabled_env_deleted" observed via list_triggers from the coordinator session); this lane self-healed its own failsafe but has no tool path to another lane's triggers — cross-lane trigger repair is owner/manager-only; owner was alerted ~2026-07-11T17:31Z; no repo evidence shows the sibling failsafes re-armed since.
```

### substrate-kit — ⚑ FOR MANAGER (relay debts owed to the kit — refreshed at the v1.12.0-wave close; wave-B v1.12.1 items append…

- suggested-id: `OQ-SUBSTRATE-KIT-MANAGER-RELAY-DEBTS-OWED`
- source: substrate-kit/control/status.md @ `ac612ab` · heartbeat `updated:` 2026-07-12T18:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ FOR MANAGER (relay debts owed to the kit — refreshed at the v1.12.0-wave close; wave-B v1.12.1 items appended 2026-07-11):
- **NEW — slice-6 fm-side manager asks (recorded by the fm wiring session, 2026-07-12, fm PR #126; Q-0261.3 — recorded, NOT performed):** (a) **UNIVERSAL wake fetch-list vN bump + owner re-paste** — the manager-authored startup surfaces should add `docs/seat-digest.md` (+ `docs/SKILLS.md`) to the wake fetch list (vN bump + owner re-paste via fm's edit-registry-first flow); (b) **splicing digest blocks into per-seat pastes is manager-authored content** (the fm v3.4 restamp lane, open fm PR #122) — the registry renders + the paste-fence byte-match guard are ready and will fail `--check` on any spliced block that drifts from kit truth; (c) **per-seat walls venue overrides** are seat-lane actions (`bootstrap.py seat-digest --venue …` in the SOURCE repo; fm only re-syncs); (d) the five not-yet-onboarded seats (superbot-2.0, websites, self-improvement, superbot-world, ideas-lab) onboard via `seat_digest_sync.py --sync` once their kit ≥ v1.15.0 upgrades land (wave A in flight).
- **NEW — wave-B v1.12.1 findings (fresh items only; chronic ones re-flagged in place below):** (a) **fleet-manager has no live root CLAUDE.md** (staged only) — its working agreement never loads in a real session; (b) **fleet-manager's 3×-re-flagged lane-owed items** (heartbeat bump, owner-action-fields, orientation merge) may deserve graduation from wave-report ⚠️ noise into explicit `control/inbox` ORDERs — three consecutive waves of re-flagging shows the lane isn't picking them up from status prose; (c) **venture-lab `docs/AGENT_ORIENTATION.md` points at `.claude/CLAUDE.md` which doesn't exist live** (staged only) — 2nd consecutive wave this fired; kit-side template fix pending; (d) gba-homebrew: nothing — cleanest tree of the four.
- **Re-flagged by wave B (chronic, already listed below, still true post-v1.12.1):** pokemon-mod-lab heartbeat `kit:` line STILL v1.6.0 — now TWO versions stale (3rd flag) · pokemon-mod-lab claims-home decision still open (root `claims/` vs `control/claims/`) · pokemon-mod-lab `automerge.required_context` still says "substrate-gate" but the real required check is "ROM builds" (re-confirmed live: the wave PR merged on "ROM builds") · fleet-manager heartbeat STILL v1.7.0 (now five versions stale) · fleet-manager owner-action-fields advisory (chronic).
- **NEW — adopter-outcomes report shipped** (docs/reports/2026-07-11-adopter-outcomes-measurement.md, #247) — headline: before/after effect unmeasurable (9/10 adopters born-with-kit; superbot pin-only); false-claim audit near-clean (1 confirmed instance, sbn #44, self-corrected); superbot-next heartbeat kit: line still stale at v1.10.1 vs tree v1.12.0 (lane-owned, known drift class).
- **NEW — pokemon-mod-lab lane-owed items (from the v1.6.0 → v1.12.0 catch-up, pokemon-mod-lab#43; Q-0261.3 scope, deliberately NOT done by the wave):** (a) its `control/status.md:40` heartbeat still says kit v1.6.0 — one-writer per file, the lane must bump it; (b) claims-home decision owed — legacy root `claims/` is the binding practice there vs the kit's `control/claims/`; the check advisory fires every session until the lane pins one via `substrate.config.json` → `claims_dir`; (c) its `automerge.required_context` defaults to "substrate-gate" but the repo's actual required check is **"ROM builds"** — must be fixed BEFORE its staged auto-merge enabler is ever wired live; (d) `control/README.md` classified DIVERGED — manual merge owed, delta preserved in `.substrate/upgrade-report.md` § Template deltas; (e) its heartbeat uses the bold-label `- **kit:** vX` form the kit's KIT_LINE_RE doesn't parse (kit-side grammar follow-up idea filed on the #232 session card).
- **heartbeat `kit:`-line bump OWNERSHIP question (wave-report inconsistency)** — still open: the wave records disagree about who owes the post-upgrade heartbeat bump (websites bumped its `kit:` line in-lane on the wave PR itself and scanned clean at the #207 regen; every other adopter's bump is recorded as "lane-owed" and chronically lags 1–3 releases — the registry's whole recurring self-report DRIFT class). The manager should rule which seat owns the post-wave `kit:`-line bump — the wave-upgrade PR itself (websites' shape) vs each lane's next wake — so the drift class ends fleet-wide instead of regenerating as ⚠️ noise every wave. The pokemon-mod-lab item (a) above is the newest instance.
- **superbot-next origin/main was force-pushed mid-wave** (the v1.10.x window) — flagged, not touched by any kit-seat session; their lane owns the history reconcile.
- **v1.12.0-wave heartbeat `kit:` bumps still lane-owed** (self-report lag class, per the wave records + the #232 regen: fleet-manager, superbot-games — its status.md still has NO `kit:` line at all — and trading-strategy all lane-owed; kit-seat quad self-report lag persists per the chronic class; trees all already v1.12.0). Also lane-owed from the trio wave: `docs/AGENT_ORIENTATION.md` diverged manual merges on all three (template delta preserved in each repo's `.substrate/upgrade-report.md`).
- Carried from earlier waves, still standing as far as kit evidence shows: superbot-next duplicate session cards guard-firing (their gate noise — lane dedup) · venture-lab dual claims homes (control/claims/ + legacy — consolidate per §6.4) · gba-homebrew docs pending `upgrade --apply-docs` · fleet-manager owner-action-fields advisory (chronic) · trading-strategy docs/CAPABILITIES.md landing-constraints entry (chronic).
- **NEW — superbot-next's kit gate is the plain weak form (friction #38 residual, re-verified 2026-07-12 at sbn c03df80):** its `ci.yml` checkers job runs bare `python3 bootstrap.py check --strict` — no `--require-session-log`, no diff-aware `--session-log` card selection, no control fast lane, no `--inbox-base` (inbox gate LATENT there, the v1.7.0-wave class). The wired form sits STAGED in its own tree since the v1.12.1 upgrade (`<state_dir>/ci/substrate-gate.yml`) — the lane owes the install/fold-in. Kit-side advisory idea backlogged: docs/ideas/engagement-wiring-strength-verification-2026-07-12.md.
- **RESOLVED 2026-07-12 (PR #289) — the heartbeat-grammar ◐ row, the graduation map's last open row, is SHIPPED:** negative `**kit:**` example + adopters.md deference now taught by control-README.md.tmpl + control-status.md.tmpl (grammar renderer `kit_line_negative_example()`, writer↔enforcer verbatim pins). The hardening-report graduation map is fully absorbed kit-side. Known out-of-lane remainders unchanged: slice 7 lives in the websites lane (shipped there, PR #177 @ d4a7389); the fleet-manager-side slice-6 wiring is a separate coordinated PR on the fm lane. (Adopters inherit the taught text at the next release + upgrade wave — pokemon-mod-lab item e above stays lane-owed until then.)
- **NEW — fresh-session cron delivery appears broken (now 3-for-3)**: both fresh-session (`create_new_session_on_fire=true`) cron triggers armed agent-side for the daily kit-lab loop have failed — the predecessor (trig_01MHwmBrA1bziEp49g6xqGt5) vanished from the registry within hours of creation, and its replacement (trig_01Jm57GAjNCFrYJn1oLMiYGE) missed its first scheduled fire (probed 2026-07-12T08:06Z: enabled=true, last_fired_at absent, next_run_at stuck at the missed 06:08:52Z slot; zero repo activity this morning) and NEVER self-delivered thereafter (re-checked same day: next_run_at still frozen at the 06:08Z slot, last_fired_at never) — the one kit-lab session that DID appear (08:46Z) was a MANUAL kick from the hub night-review session, not a cron fire (it stood down as a verified no-op, zero writes), and the kick payload attributes the non-delivery to **platform scheduler degradation** — while the self-bound failsafe cron fired on schedule all night; today's lab slice ran ONLY via the stopgap (PR #258). Standing context: the registry env-id anomaly (job_config surfaces env_01WAB3QKMneNpWKuR1ZLVsVX vs the recorded env_01R1G1wsWsEMShxECRsFnVor on all kit triggers — probable display artifact, ROUTINE STATE record @ PR #256). Recommendation: a platform-side look at fresh-session cron delivery, or ratify converting the daily loop to a self-bound cron. D3's ≥3-fire count has NOT started. Full finding + stopgap: ROUTINE STATE ⚑ above.
```

### substrate-kit — ⚑ needs-owner: thirteen open items (items 2–12 carried verbatim — ordinals kept stable so cross-references ho…

- suggested-id: `OQ-SUBSTRATE-KIT-THIRTEEN-OPEN-ITEMS-ITEMS`
- source: substrate-kit/control/status.md @ `ac612ab` · heartbeat `updated:` 2026-07-12T18:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: thirteen open items (items 2–12 carried verbatim — ordinals kept stable so cross-references hold — plus 14 + 15, the two parked pin PRs; item 13 RESOLVED 2026-07-11: the owner merged #181 @ f7aa633 — full resolution record in the retro §2 postscript + git history of this file). The two HOT ones are one click each:
```

### substrate-kit — ⚑ OWNER-ACTION 15 — T5 v3 probe re-shape — pin PR #238 awaits your ratification (do-not-automerge by design; …

- suggested-id: `OQ-SUBSTRATE-KIT-15-T5-V3-PROBE`
- source: substrate-kit/control/status.md @ `ac612ab` · heartbeat `updated:` 2026-07-12T18:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 15 — T5 v3 probe re-shape — pin PR #238 awaits your ratification (do-not-automerge by design; PAIRS with OWNER-ACTION 14 / PR #220)
WHAT: Ratify (merge) or reject (close with a word) the T5 task-text re-shape that restores the probe's discriminating tension.
WHERE: https://github.com/menno420/substrate-kit/pull/238
HOW: click "Merge pull request" to ratify, or close it with a one-line reason — the PR is READY, CI-green at head 917318d, labeled at open, diff = bench/tasks/T5.md + its session card only.
RISK: ↩️ reversible — a squash merge is revertable with one follow-up PR; a close can be reopened.
WHY-IT-MATTERS: run-9 proved the v2 probe degenerate post-#222 — T4 now completes the card, so T5 boots on a "complete" push and the skip-vs-ritual tension the probe exists to measure never arises (run-9 report §5.5). v3 has the runner seed the drafted/unresolved state (and commit the arm tree clean — retiring the 4/4 commit-sweep confound of runs 8–9), so the probe discriminates regardless of T4's behavior.
UNBLOCKS: run-10 fires a non-degenerate T5. PAIRING: judge items are unchanged from v2, so rubric pin PR #220 scores v3 as-is and needs no re-cut — ratify both (one click each) and run-10 judges v3 task text under the §3-v2 rubric coherently.
VERIFIED-NEEDED: pin-path law (§5.0, check_bench_integrity rule 1): the lab never merges its own change to the bench oracle — labeled `do-not-automerge` at open, auto-merge verified not armed (enabler run 29164948745 arm step conclusion=skipped, KL-5 fresh-label guard; the head-917318d synchronize run 29165025432 skipped the whole enable-auto-merge job on the labeled payload; PR sat open at mergeable_state=clean on green CI), parked; only the owner's click lands it.
```

### substrate-kit — ⚑ OWNER-ACTION 14 — rubric §3 T5 v2 alignment — pin PR #220 awaits your ratification (do-not-automerge by des…

- suggested-id: `OQ-SUBSTRATE-KIT-14-RUBRIC-3-T5`
- source: substrate-kit/control/status.md @ `ac612ab` · heartbeat `updated:` 2026-07-12T18:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 14 — rubric §3 T5 v2 alignment — pin PR #220 awaits your ratification (do-not-automerge by design)
WHAT: Ratify (merge) or reject (close with a word) the judge-rubric alignment your #181 merge made due.
WHERE: https://github.com/menno420/substrate-kit/pull/220
HOW: click "Merge pull request" to ratify, or close it with a one-line reason to reject — the PR is READY, CI-green at head c582006, diff = bench/rubric/cold-start-rubric.md (§3 T5 block only) + its session card.
RISK: ↩️ reversible — a squash merge is revertable with one follow-up PR; a close can be reopened.
WHY-IT-MATTERS: the judge already scores T5 from the ratified v2 task text, but the written rubric still describes the retired v1 items — every bench run carries a "protocol pins applied" deviation note until the two documents agree.
UNBLOCKS: bench runs from run-9 on score T5 straight from rubric §3; retires the run-8 report §5 limitation line.
VERIFIED-NEEDED: pin-path law (§5.0, check_bench_integrity rule 1): the lab never merges its own change to the bench oracle — this session labeled #220 at open, verified the enabler's arm step was SKIPPED (run 29158862553, step "Enable native auto-merge (squash)" conclusion=skipped) and a disarm probe mutated nothing (PR updated_at unchanged), and parked it. Only the owner's click can land it — the designed wall, not an assumed one.
(PAIRING note added 2026-07-11: T5 v3 pin PR #238 / ⚑ 15 keeps the v2 judge items verbatim — ratifying both, one click each, gives run-10 a coherent text+rubric pair.)
```

### substrate-kit — ⚑ OWNER-ACTION 2 — P10 required-check swap

- suggested-id: `OQ-SUBSTRATE-KIT-2-P10-REQUIRED-CHECK`
- source: substrate-kit/control/status.md @ `ac612ab` · heartbeat `updated:` 2026-07-12T18:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 2 — P10 required-check swap
WHAT: Swap which CI check main requires, from the two legacy names to the current one.
WHERE: repo Settings → Rules → the `main` ruleset → required status checks
HOW: remove "Kit test suite" and "Cold-adoption smoke (adopt + check --strict)"; add `kit-quality` (source: GitHub Actions); set "Require branches to be up to date" OFF
RISK: ↩️ reversible — re-add the old required checks in the same ruleset panel to undo.
WHY-IT-MATTERS: the legacy alias jobs cause ~35-min queue stalls purely to satisfy old names; the up-to-date requirement stalls green PRs `behind` (live-hit #107).
UNBLOCKS: an agent deletes the two legacy-alias-* jobs (queue item 9); the queue-stall class ends; fast-lane PRs stop paying an update round-trip.
VERIFIED-NEEDED: no agent path to rulesets — direct api.github.com is 403 through the proxy and the MCP toolset has no ruleset endpoint; Settings → Rules is owner-only UI.
```

### substrate-kit — ⚑ OWNER-ACTION 3 — P4 arm the daily lab loop

- suggested-id: `OQ-SUBSTRATE-KIT-3-P4-ARM-DAILY`
- source: substrate-kit/control/status.md @ `ac612ab` · heartbeat `updated:` 2026-07-12T18:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 3 — P4 arm the daily lab loop
WHAT: Create the scheduled session that runs the lab every morning.
WHERE: Console → kit repo environment → Schedules → New schedule
HOW: paste the fenced prompt from docs/operations/lab-loop.md § Arming verbatim · cron `0 6 * * *` (UTC) · fresh session per fire ON · Sonnet-class model · unrestricted-branch-push OFF · auto-fix PRs ON
RISK: ↩️ reversible — pause or delete the schedule in the console to undo.
WHY-IT-MATTERS: turns the lab from manually-fired sessions into the self-running daily loop the program is built around.
UNBLOCKS: D3 (the autonomous daily loop; needs ≥3 scheduled fires).
VERIFIED-NEEDED: the console Schedules pane is owner UI — routine/schedule creation is an enumerated wall in docs/CAPABILITIES.md; no in-session API/MCP path.
(Correction note appended 2026-07-10, ORDER 010 — the VERIFIED-NEEDED line above is now PARTIALLY invalidated: routines CAN be armed agent-side via `create_trigger` (the ORDER 010 arm and both cutovers above prove it). The ask stays open because the lab loop wants a fresh-session-per-fire daily schedule with specific console options (model class, branch-push, auto-fix PRs), which the MCP arm has NOT been verified to cover — per THE DISCOVERY RULE a next session should ATTEMPT `create_trigger` (fresh-session mode) before treating this as owner-only.)
(RESOLUTION note appended 2026-07-11, the P4 slice — the directed ATTEMPT was made and SUCCEEDED: `create_trigger` with `create_new_session_on_fire=true` armed the loop agent-side — trigger trig_01MHwmBrA1bziEp49g6xqGt5, cron `0 6 * * *`, substrate-kit environment, lab-loop.md prompt verbatim, next fire 2026-07-12T06:01:54Z (full record: ROUTINE STATE). The founding plan's P4 row itself blesses this path ("or agent-created trigger + owner kill-switch"); the kill switch exists both sides (owner pause toggle + agent delete_trigger). **The ask is REDUCED to an optional console verification**: the three console-only knobs — model class Sonnet-class, unrestricted-branch-push OFF, auto-fix PRs ON — are not settable/readable via MCP; the fired sessions run on environment defaults. If the defaults are acceptable, say nothing — the loop is live; to adjust, open the Routine in the console and set the knobs. D3's ≥3-consecutive-fires count starts 2026-07-12.)
(Pointer correction appended 2026-07-11: trig_01MHwmBrA1bziEp49g6xqGt5 above later vanished from the registry and was replaced — the LIVE trigger is **trig_01Jm57GAjNCFrYJn1oLMiYGE**, next fire 2026-07-12T06:06:34Z; full record: ROUTINE STATE ⚑ resolution. Everything else in this ask is unchanged — the loop is live under the new id.)
```

### substrate-kit — ⚑ OWNER-ACTION 4 — P5 create Railway project kit-lab

- suggested-id: `OQ-SUBSTRATE-KIT-4-P5-CREATE-RAILWAY`
- source: substrate-kit/control/status.md @ `ac612ab` · heartbeat `updated:` 2026-07-12T18:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 4 — P5 create Railway project kit-lab
WHAT: Create a separate Railway project so the lab gets its own infra lane.
WHERE: Railway console → New project
HOW: name `kit-lab` · region `europe-west4` · no spend caps (PL-005) · notification rule → HQ #railway-alerts; then put a project-scoped RAILWAY_TOKEN in the kit repo's environment
RISK: ↩️ reversible — delete the empty project to undo (no production IDs touched).
WHY-IT-MATTERS: the lab has no infra lane of its own; sharing production's is forbidden.
UNBLOCKS: the P6 console move (agent-built the moment the token exists).
VERIFIED-NEEDED: Railway project creation is owner console UI, and the ambient-IDs-are-production rule bars agents from touching existing Railway IDs — both walls enumerated; no agent path.
```

### substrate-kit — ⚑ OWNER-ACTION 5 — P8 confirm MIT

- suggested-id: `OQ-SUBSTRATE-KIT-5-P8-CONFIRM-MIT`
- source: substrate-kit/control/status.md @ `ac612ab` · heartbeat `updated:` 2026-07-12T18:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 5 — P8 confirm MIT
WHAT: Confirm the kit's license with one word.
WHERE: any channel
HOW: reply "MIT ok", or name a replacement license
RISK: ↩️ reversible — the license can still be swapped by a follow-up commit while adoption is fleet-internal.
WHY-IT-MATTERS: the kit ships to consumer repos with no declared license until this lands.
UNBLOCKS: closing the license ⚑ carried since KL-1.
VERIFIED-NEEDED: a license choice is a legal/product decision — owner judgment by nature; nothing for an agent to attempt.
```

### substrate-kit — ⚑ OWNER-ACTION 6 — P11 public flip OR P13 read-only PAT (pick one)

- suggested-id: `OQ-SUBSTRATE-KIT-6-P11-PUBLIC-FLIP`
- source: substrate-kit/control/status.md @ `ac612ab` · heartbeat `updated:` 2026-07-12T18:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 6 — P11 public flip OR P13 read-only PAT (pick one)
WHAT: Let the other fleet repos read this one — either make it public or mint a read-only token.
WHERE: P11: Settings → General → Danger Zone → Change visibility. P13: github.com/settings/tokens → fine-grained PAT, read-only, consumer-repo scope, then add to the fleet environments
HOW: P11 is click-through; P13 is create-token + paste into environment settings
RISK: ⚠️ P11 is effectively irreversible (once public, history is exposed even after flipping back) · ↩️ P13 is reversible — revoke the token anytime.
WHY-IT-MATTERS: sibling repos cannot see kit data today, so the merged console and the loop's cross-repo sweeps run blind.
UNBLOCKS: kit data in the merged console + the lab loop's B2/B3/B4 sweeps (queue item 12).
VERIFIED-NEEDED: repo visibility and credential minting are account-owner surfaces; the wall is verbatim in docs/CAPABILITIES.md — cross-repo get_file_contents returned "Access denied: repository … is not configured for this session".
```

### substrate-kit — ⚑ OWNER-ACTION 7 — superbot upgrade decision

- suggested-id: `OQ-SUBSTRATE-KIT-7-SUPERBOT-UPGRADE-DECISION`
- source: substrate-kit/control/status.md @ `ac612ab` · heartbeat `updated:` 2026-07-12T18:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 7 — superbot upgrade decision
WHAT: Rule on superbot's kit pin — upgrade it or keep holding.
WHERE: any channel
HOW: decide-and-flag recommendation — adopt at the next stable release in one hop; say nothing to accept, "upgrade now" or "hold pin-only" to override
RISK: ↩️ reversible — the pin can be restored; every upgrade banks a rollback copy.
WHY-IT-MATTERS: superbot's deliberate pin is now 14 releases behind (v1.0.0 vs v1.12.0) and the drift window keeps growing.
UNBLOCKS: the fleet's last non-ENGAGED adopter upgrading, whenever taken.
VERIFIED-NEEDED: the pin is a recorded owner decision (docs/adopters.md: "the v1.2.0+ upgrade is an owner decision") — agents don't overrule a deliberate stance; product judgment, not a wall.
```

### substrate-kit — ⚑ OWNER-ACTION 8 — web-environment setup script paste

- suggested-id: `OQ-SUBSTRATE-KIT-8-WEB-ENVIRONMENT-SETUP`
- source: substrate-kit/control/status.md @ `ac612ab` · heartbeat `updated:` 2026-07-12T18:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 8 — web-environment setup script paste
WHAT: Paste the corrected environment setup script so no more sessions die at startup.
WHERE: Claude console → the environment's settings → "Setup script" field (owner-only dialog)
HOW: paste the guarded script from docs/gen2/setup.sh (gen-2 variant) verbatim
RISK: ↩️ reversible — re-paste the previous script to undo.
WHY-IT-MATTERS: the current script already killed one session at provisioning (wrong cwd + hard-fail on a missing requirements.txt — PR #47 documents the casualty + fix).
UNBLOCKS: reliable session starts in this environment. If already pasted, say so and this ask is withdrawn — agents cannot read the settings dialog to confirm.
VERIFIED-NEEDED: the environment settings dialog is owner-only console UI (docs/CAPABILITIES.md); PR #47 is the live evidence of the one confirmed casualty.
(§6.5 note appended 2026-07-10: the kit-side setup-script CONTRACT shipped without this — PR #147 planted `scripts/env-setup.sh` + the `check_setup_script` enforcer from the fleet-manager archetype material. This ask remains the ENV-PANEL half: the owner-pasted shim is what makes any repo's `scripts/env-setup.sh` actually run at provisioning. The paste-ready archetype scripts live at fleet-manager `environments/archetype-*.sh`.)
```

### substrate-kit — ⚑ OWNER-ACTION 9 — (informational, low priority) optional self-merge permission rule

- suggested-id: `OQ-SUBSTRATE-KIT-9-INFORMATIONAL-LOW-PRIORITY`
- source: substrate-kit/control/status.md @ `ac612ab` · heartbeat `updated:` 2026-07-12T18:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 9 — (informational, low priority) optional self-merge permission rule
WHAT: Optionally grant a permission rule so future sessions can self-merge PRs directly instead of relying on the enabler workflow.
WHERE: Claude console → the environment's permission/auto-mode settings
HOW: allow `mcp__github__merge_pull_request` / `mcp__github__enable_pr_auto_merge` for this environment's sessions
RISK: ↩️ reversible — remove the permission rule to undo.
WHY-IT-MATTERS: one gen-2 lane's auto-mode classifier refused these as "Merge Without Review" while another lane's were permitted the same night — the wall is session-dependent. auto-merge-enabler.yml covers the refused case server-side.
UNBLOCKS: nothing blocked — both paths land PRs today; this only removes the indirection. LOW priority.
VERIFIED-NEEDED: the classifier denial is verbatim in docs/CAPABILITIES.md (2026-07-10); the permission grant is an owner console surface — no agent path to change auto-mode rules.
```

### substrate-kit — ⚑ OWNER-ACTION 10 — branch cleanup (lowest priority)

- suggested-id: `OQ-SUBSTRATE-KIT-10-BRANCH-CLEANUP-LOWEST`
- source: substrate-kit/control/status.md @ `ac612ab` · heartbeat `updated:` 2026-07-12T18:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 10 — branch cleanup (lowest priority)
WHAT: Turn on auto-delete for merged branches, then delete the stale branches of already-closed PRs.
WHERE: Settings → General → Pull Requests → check "Automatically delete head branches"; then each closed PR's "Delete branch" button
HOW: one checkbox + click-throughs (this window added the release/regen/bench lanes' merged branches to the pile)
RISK: ↩️ reversible — the checkbox unticks; a deleted merged branch restores via the PR's "Restore branch" button.
WHY-IT-MATTERS: pure hygiene — ends the clutter class permanently; nothing functional waits on it.
UNBLOCKS: nothing functional; the checkbox prevents recurrence forever.
VERIFIED-NEEDED: branch deletion is 403 on EVERY agent path (git push :branch 403, REST 403, GraphQL deleteRef disabled, no MCP tool — docs/CAPABILITIES.md "Branch deletion" wall). A full session attempted it and deleted zero.
```

### substrate-kit — ⚑ OWNER-ACTION 11 — enable "automatically update branches" (closes the auto-merge behind-stall)

- suggested-id: `OQ-SUBSTRATE-KIT-11-ENABLE-AUTOMATICALLY-UPDATE`
- source: substrate-kit/control/status.md @ `ac612ab` · heartbeat `updated:` 2026-07-12T18:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 11 — enable "automatically update branches" (closes the auto-merge behind-stall)
WHAT: Turn on the repo setting that auto-updates a PR branch when its base moves, so an armed auto-merge PR that goes `behind` gets refreshed and lands without an agent round-trip.
WHERE: Settings → General → Pull Requests → check "Always suggest updating pull request branches" / the auto-update-branch control (the counterpart to OWNER-ACTION 2's "Require branches up to date")
HOW: one checkbox
RISK: ↩️ reversible — one checkbox, untick to undo.
WHY-IT-MATTERS: with "Require branches up to date" ON, a green armed PR stalls `behind` whenever a sibling merges first (live-hit #107 + the §6.4/§6.5/§6.8/§6.10 window; #144, #147, #150 and #153 pre-empted it only by a manual branch update). The enabler `synchronize` re-arm (#111) narrows this — a fix-push now re-arms — but a PR that goes behind AFTER its last push still needs a manual `git merge origin/main` + push. Auto-update removes that residual manual step.
UNBLOCKS: armed auto-merge completes on green even when a sibling merges first with no later push; fully ends the behind-stall class (complements OWNER-ACTION 2, which offers the alternative of turning the requirement OFF entirely).
VERIFIED-NEEDED: repo General settings are owner-only UI; no agent path to toggle repo settings (same class as the ruleset/branch walls in docs/CAPABILITIES.md). Live evidence: #107 (and later close branch updates) sat `behind` with green checks until a manual branch update; the enabler `synchronize` fix (#111) is a partial, not a full, close.
```

### substrate-kit — ⚑ OWNER-ACTION 12 — route the websites ORDER 005 fleet relay

- suggested-id: `OQ-SUBSTRATE-KIT-12-ROUTE-WEBSITES-ORDER`
- source: substrate-kit/control/status.md @ `ac612ab` · heartbeat `updated:` 2026-07-12T18:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ OWNER-ACTION 12 — route the websites ORDER 005 fleet relay
WHAT: Send the unexecuted ORDER 005 from the `websites` repo's inbox to a session that has websites scope, so it gets done.
WHERE: the `menno420/websites` repo — its `control/inbox.md` ORDER 005 (route it to a websites-scoped session; e.g. dispatch a session on that repo)
HOW: assign/relay ORDER 005 to a websites-scoped session (a substrate-kit / coordinator session cannot — no websites write scope)
RISK: ✅ safe — routing a message; the order's own execution carries its own gates.
WHY-IT-MATTERS: a dispatched fleet order is sitting unexecuted; the coordinator surfaced it but has no websites scope to route or run it, so it stalls until the owner routes it.
UNBLOCKS: whatever ORDER 005 on websites was meant to deliver (its substance lives in that repo's inbox).
VERIFIED-NEEDED: cross-repo write to `menno420/websites` is out of this session's scope (the per-session repo allowlist governs reads; execution needs a websites-scoped session) — genuinely owner-routed, not an assumed wall. Provenance: coordinator relay 2026-07-10 (docs/retro/coordinator-session-2026-07-10.md § 4); origin is this lane's gen-1 status notes.
```

### substrate-kit — ⚑ version-truth deference (flagged for the owner's §7 layering ruling, decide-and-flag): generated `docs/adop…

- suggested-id: `OQ-SUBSTRATE-KIT-VERSION-TRUTH-DEFERENCE-FLAGGED`
- source: substrate-kit/control/status.md @ `ac612ab` · heartbeat `updated:` 2026-07-12T18:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ version-truth deference (flagged for the owner's §7 layering ruling, decide-and-flag): generated `docs/adopters.md` is now the SINGLE home for the fleet's kit-version spread; other homes (hand-kept registries, release-json narratives, status-prose version claims) should DEFER to it pending the owner's §7 ruling. Concretely open under that ruling: the kit repo's own `substrate.config.json` pin (v1.0.0, self-adopt-era) vs its dist (v1.12.0) — the registry's one tree-internal DRIFT row, deliberately NOT hand-fixed because what consumer-#0's pin *means* is the §7 question.
```

### ↳ substrate-kit — `control/status-superbot-coordinator.md` — ⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLI…

- suggested-id: `OQ-SUBSTRATE-KIT-1-VERIFY-DELIVER-TESTING`
- source: substrate-kit/control/status-superbot-coordinator.md @ `ac612ab` · heartbeat `updated:` 2026-07-10T13:47:02Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLIPPED at 2026-07-10T13:45Z (band-5 "NEXT LANE: LIVE-DRIVE", 01:05Z heartbeat), so that lane's seven wind-down deliverables are still owed [unblocks: superbot-next lane archive]; 2) kernel-surface-drift ruling (flag 13 in superbot-next docs/status/testing-report-2026-07-09.md: "relax-compare" or "re-baseline") [unblocks: ALL parity flips]; 3) create repo superbot-plugin-hello (github.com/new, owner menno420, Public, no README) [unblocks: ORDER 002 done]; 4) paste the setup script from docs/environment-setup-script.md into the project Environment settings (re-verified exit-0 at wind-down) [unblocks: no more provisioning deaths]; 5) nod for wiring superbot's new collision/freshness checkers (#1918/#1923) into code-quality.yml — one small PR, owner said workflow edits need a nod [unblocks: checkers enforce in CI]; 6) stale trading-lab/venture-lab manifest rows (manager-owned file) + Q-0248 taxonomy lacks a "tooling" class [unblocks: honest telemetry]
```

### websites — ⚑ needs-owner: pointer — canonical six-field blocks live in docs/owner/OWNER-ACTIONS.md ONLY (reconciled this…

- suggested-id: `OQ-WEBSITES-POINTER-CANONICAL-SIX-FIELD`
- source: websites/control/status.md @ `fba35dd` · heartbeat `updated:` 2026-07-12T18:23:20Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: pointer — canonical six-field blocks live in docs/owner/OWNER-ACTIONS.md ONLY (reconciled this sitting under fleet-manager ORDER 022: RAILWAY_TOKEN + ANTHROPIC_API_KEY struck to Decided; the review-service ask was already struck). Open asks there: botsite SITE_PASSWORD; the Actions "allow create PRs" toggle (review-bake); botsite Postgres/DATABASE_URL; PayPal Payouts creds; the fine-grained GitHub contents:write PAT (ORDER 020); Discord OAuth redirect-URI + client secret (owner decision pending — gates the environments hub).
```

### trading-strategy — ⚑ needs-owner (six-field form — what / why / exact click / where / blocking? / fallback; durable copies with …

- suggested-id: `OQ-TRADING-STRATEGY-SIX-FIELD-FORM-WHAT`
- source: trading-strategy/control/status.md @ `b354548` · heartbeat `updated:` 2026-07-12T12:12Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner (six-field form — what / why / exact click / where / blocking? / fallback; durable copies with full six-field detail in docs/retro/archive-ready-2026-07-11.md):
- (g) RE-ARM WEEKLY GRADING CADENCE — TRIGGER SUCCESSION: RESOLVED 2026-07-11 (re-armed by the Money-seat coordinator 2026-07-11T23:07Z — new weekly grading trigger trig_015aNMg5ncoSE2Roe4MKjQnr, cron "0 9 * * 5", next run 2026-07-17T09:05Z, plus 2h failsafe trig_017o6azZTd9pzcaSthEncT5q, both bound to the live Money-seat coordinator session; the old triggers trig_01YBaVeKAW2fSD83S9F37s2d + trig_01YXNmgqYeYQ1LuepsLmbNCG died with the archived coordinator chat; see routine state). The 2026-07-17 grading pass now has an executor — no owner action outstanding.
- (b) ENV SETUP SCRIPT / fresh-environment sessions die silently at provision without it (setup runs at cwd=/home/user with repos as subdirectories) / paste the contents of environments/setup-universal.sh into the environment's setup-script field and save / Claude environment config for this project / not blocking (current pinned env works) / keep spawning into the pinned env and treat any child with no heartbeat within 10 min as dead → respawn.
- (c) ALLOW AUTO-MERGE TOGGLE: RESOLVED 2026-07-12 — the substrate-kit auto-merge enabler landed via PR #65 (bf885f0); it arms auto-merge server-side for claude/* head branches on green, so self-landing PRs from claude/* heads no longer need an agent to poll-and-merge. (Historical: previously the repo toggle was off and auto-merge arm failed pending-side with "unstable status", reconfirmed on PR #36; every merge to date used REST/MCP squash-on-green per ORDER 002.)
- (d) ARCHIVE DEAD GEN-1 SESSION / the gen-1 "ORDER 001 successor" session died at provision, emits no failure event, and still lists as active — misleading / open the project's session list, locate "ORDER 001 successor", archive it / claude.ai session list for this project / not blocking / ignore it — it consumes nothing.
- (f) DECIDE ON POST-2026 OUT-OF-SAMPLE PROTOCOL PROPOSAL / research round 2 closed with 5 dev-candidates whose ONLY path past dev-candidate is a NEW owner-gated pre-registered protocol on genuinely new post-2026 data — recorded as a PROPOSAL in docs/final-report.md (POST-HOLDOUT DEV-ONLY section) and docs/research-round-2-results.md; agents never schedule, initiate, or run it / if wanted, file an inbox ORDER authorizing a pre-registered protocol draft (decision only — nothing runs on a yes until the protocol itself is owner-approved); if not wanted, no click needed / control/inbox.md via the manager / not blocking / dev-candidates stay labeled dev-only indefinitely — flag-only, this item never self-executes. ((e) merge-PR-#37 retired: resolved by owner click, PR #37 merged 2026-07-10T20:56:34Z by menno420.)
- (h) DECIDE ON THE BOLLINGER MTF PRE-REGISTRATION / PR #71's dev exploration produced an OWNER-GATED preregistration draft (docs/proposals/bollinger-mtf-preregistration-draft.md) — a frozen protocol for a future post-2026 minute-data OOS test of the MTF Bollinger idea; agents never schedule, initiate, or run it / if wanted, file an inbox ORDER authorizing it — an explicit ORDER plus a fresh session are required (decision only: nothing runs on a yes until the protocol itself is owner-approved); if not wanted, no click needed / control/inbox.md via the manager / not blocking / flag-only — the draft stays a plan and never self-executes.
- (i) OPTIONAL MINUTE-DATA ACQUISITION DECISION / the 15m/45m timeframes in the MTF idea are UNTESTABLE on the repo's cached hourly data (#71) — a real test needs PAID minute data / if wanted, decide to acquire paid minute data (a spend) and weigh it against the dev-window CLEAN NULL already found; if not wanted, no click / owner's data-vendor choice, then an inbox ORDER / not blocking / skip — the dev-window null is a complete negative deliverable; with no minute data the 15m/45m variants stay untested.
next-update-by: 2026-07-17T23:59:00Z (weekly grading cadence, protocol §6 — first pass is expected FLAT: warm-up runs ~3 weeks; this deadline now HAS an executor — the re-armed weekly grading trigger trig_015aNMg5ncoSE2Roe4MKjQnr fires 2026-07-17T09:05Z, ⚑ (g) RESOLVED)
```

### venture-lab — - **⚑ LAUNCH — COMPLETE END-TO-END, now in MEASUREMENT mode (⚑A VERIFIED · ⚑E LAUNCHED · article LIVE · test …

- suggested-id: `OQ-VENTURE-LAB-LAUNCH-COMPLETE-END-END`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ LAUNCH — COMPLETE END-TO-END, now in MEASUREMENT mode (⚑A VERIFIED · ⚑E LAUNCHED · article LIVE · test purchase VERIFIED); no open owner click** · WHAT: (A) ⚑A env secret — **DONE/VERIFIED via PR #74**; (E) Gumroad $29 listing — **DONE/LIVE** (<https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit>, HTTP 200); the **free gotcha article** — **DONE/LIVE** on dev.to (<https://dev.to/menno420/your-stripe-webhook-says-customeremail-is-null-heres-why-and-the-fix-1bgp>, HTTP 200 at 2026-07-12T17:24:10Z, product link present; the **4 tags — `stripe`/`debugging`/`webhooks`/`payments` — went LIVE 2026-07-12T17:24:24Z**, verified via dev.to API — the earlier "ZERO tags" reading raced the owner's edit and is corrected); (1) owner **test purchase — DONE/VERIFIED 2026-07-12** (discounted end-to-end buy; success banner shown; download page served the `stripe-webhook-test-kit-v0.1` ZIP, 19.4 KB, working Download button; checkout→receipt→download confirmed). · WHY: all four launch legs are recorded on `main`; the T→T+14 kill clock is running (T=2026-07-12T16:25Z; T+14=2026-07-26) and the launch is now in **measurement mode** — the coordinator watches Gumroad analytics + dev.to engagement at the two armed checkpoints. Runbook: `docs/launch/OWNER-LAUNCH-HOUR.md`; record: `docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`. · VERIFIED-WHEN: **SATISFIED** — all four legs done (⚑A #74 · ⚑E #84 · article #85 · test purchase). No open owner action; measurement is coordinator-side (checkpoints 2026-07-19 / 2026-07-26).
```

### venture-lab — - **⚑ NEW — books read-through → pick winner(s) → choose the illustration/publishing path** · WHAT: read the …

- suggested-id: `OQ-VENTURE-LAB-NEW-BOOKS-READ-THROUGH`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ NEW — books read-through → pick winner(s) → choose the illustration/publishing path** · WHAT: read the shipped finished manuscripts — Tummel + Dormouse (#67), Comet Biscuit trilogy (#69), Star Pirates Book 1 (#72), and the Lull (DREAMLINE) Part-1 arc (#68) — and pick which one(s) to carry forward, then decide the next path (illustration, print/ISBN, listing). · WHERE: `candidates/childrens-books/{tummel,dormouse,comet-biscuit,star-pirates}/` + `candidates/dream-series/`; each carries a `DECISIONS.md` (owner-vetoable). · HOW: read the EN masters (NL/DE are native re-tellings), mark winner(s), and record the illustration/publishing decision. · WHY: the creative wave is finished and owner-gated — no images, accounts, or spend happen until the owner picks winners and a path. · UNBLOCKS: illustration + any publish/print/listing work. · VERIFIED-WHEN: owner records the winner pick(s) + the chosen illustration/publishing path.
```

### venture-lab — - **⚑M1 — License a COMMERCIAL market-data feed (the free feeds are personal-use only)** · WHAT: replace yfin…

- suggested-id: `OQ-VENTURE-LAB-M1-LICENSE-COMMERCIAL-MARKET`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑M1 — License a COMMERCIAL market-data feed (the free feeds are personal-use only)** · WHAT: replace yfinance/Stooq (personal-use only) with a commercially-licensed feed (~€25–100/mo) whose terms permit a paid/redistributed product, for the market-state-dashboard. · WHERE: a commercial-tier market-data API — **Polygon.io** or **Tiingo** (`candidates/market-state-dashboard/MONETIZATION.md` §D/⚑M1); key NAME as an owner-managed Actions secret (never a value in repo). · WHY: charging subscribers off a personal-use feed is a ToS/licensing breach — a paid product must sit on a commercial feed. · UNBLOCKS: a legally-sellable data layer (precondition for any premium tier). · VERIFIED-WHEN: commercial plan active + licence permits a paid product + board renders off the licensed feed. **Downstream of ⚑M3 + the Phase-1 go/no-go — not requested yet.**
```

### venture-lab — - **⚑M2 — One-off NL legal/compliance counsel check of the premium copy** · WHAT: a single fixed-cost review …

- suggested-id: `OQ-VENTURE-LAB-M2-ONE-OFF-NL`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑M2 — One-off NL legal/compliance counsel check of the premium copy** · WHAT: a single fixed-cost review by qualified **Netherlands** legal/compliance counsel of the premium site + marketing copy against the §C copy rules and the MAR/MiFID lines. · WHERE: a Dutch financial-promotions / MAR-MiFID firm, engaged by the owner; copy under review = `candidates/market-state-dashboard/MONETIZATION.md` §C + the drafted premium/landing/alert text (`MONETIZATION.md` §D/⚑M2). · WHY: §C is a house posture, not a legal opinion; a professional confirmation before charging money on line-walking copy is cheap insurance. · UNBLOCKS: confidence to publish paid copy (the compliance sign-off gate). · VERIFIED-WHEN: written NL counsel sign-off on record + every required edit landed. **Downstream of ⚑M3 + the Phase-1 go/no-go — not requested yet.**
```

### venture-lab — - **⚑M3 — Existing KILL CRITERION stands: 2-week owner dogfood before any premium build** · WHAT: the owner u…

- suggested-id: `OQ-VENTURE-LAB-M3-EXISTING-KILL-CRITERION`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑M3 — Existing KILL CRITERION stands: 2-week owner dogfood before any premium build** · WHAT: the owner uses the Phase-1 board for **2 weeks** before any premium build begins or any ⚑M1/⚑M2 spend is authorized. · WHERE: the live Phase-1 dashboard (owner's dogfood instance); disuse check per INTAKE §E / `MONETIZATION.md` §D/⚑M3. · HOW: sustained real use → proceed to authorize ⚑M1/⚑M2; board unread for 2 weeks → park the candidate and spend nothing. · WHY: a screener the owner himself won't open is worth nothing to strangers — self-use is the cheapest validation before paying for a feed + legal review. · UNBLOCKS: permission to spend on ⚑M1/⚑M2 and start the premium build. · VERIFIED-WHEN: 2 weeks of sustained owner use on record. **Gated behind the Phase-1 build existing at all (the go/no-go above).**
```

### venture-lab — - **⚑ NEW — market-state-dashboard Phase 1 build go/no-go** · WHAT: approve (or decline) building the Phase-1…

- suggested-id: `OQ-VENTURE-LAB-NEW-MARKET-STATE-DASHBOARD`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ NEW — market-state-dashboard Phase 1 build go/no-go** · WHAT: approve (or decline) building the Phase-1 descriptive screener spec'd in `candidates/market-state-dashboard/INTAKE.md` (anchor-rotation primary use case; $0-hosted static; descriptive-only, no signals). · WHY: it's a spec-only intake today; nothing is built until the owner says go. Build cap ≈ 120k tokens incl. CI. · VERIFIED-WHEN: owner records go/no-go.
```

### venture-lab — - **⚑ — delete stale branch `money-seat-heartbeat` (403 for agents)** · WHAT: delete the abandoned non-`claud…

- suggested-id: `OQ-VENTURE-LAB-DELETE-STALE-BRANCH-MONEY`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ — delete stale branch `money-seat-heartbeat` (403 for agents)** · WHAT: delete the abandoned non-`claude/` branch `money-seat-heartbeat` (head `f2fac7d`, the superseded PR #58 draft). · WHY: agents get a 403 deleting branches; it lingers as noise. Not urgent. · VERIFIED-WHEN: branch absent from `list_branches`.
```

### venture-lab — - **⚑B — publish membership-kit at $49 — UNFROZEN ✅** · WHAT: publish `candidates/membership-kit/LISTING.md` …

- suggested-id: `OQ-VENTURE-LAB-B-PUBLISH-MEMBERSHIP-KIT`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑B — publish membership-kit at $49 — UNFROZEN ✅** · WHAT: publish `candidates/membership-kit/LISTING.md` as a $49 product, uploading `candidates/membership-kit/dist/membership-kit-v0.2.zip` (click script: `docs/launch/membership-kit/owner-actions.md`). · VERIFIED-WHEN: public listing URL + a test purchase completes.
```

### venture-lab — - **⚑D — publish template-packs at $19 PWYW — UNFROZEN ✅** · WHAT: publish `candidates/template-packs/LISTING…

- suggested-id: `OQ-VENTURE-LAB-D-PUBLISH-TEMPLATE-PACKS`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑D — publish template-packs at $19 PWYW — UNFROZEN ✅** · WHAT: publish `candidates/template-packs/LISTING.md` PWYW $19 suggested, uploading `candidates/template-packs/dist/template-packs-v0.1.zip` (click script: `docs/launch/template-packs/owner-actions.md`). · VERIFIED-WHEN: live listing URL resolves + a test download works.
```

### venture-lab — - **⚑E — publish stripe-webhook-test-kit at $29 — LAUNCHED ✅ 2026-07-12 (flagship; see LAUNCH block + LAUNCH-…

- suggested-id: `OQ-VENTURE-LAB-E-PUBLISH-STRIPE-WEBHOOK`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑E — publish stripe-webhook-test-kit at $29 — LAUNCHED ✅ 2026-07-12 (flagship; see LAUNCH block + LAUNCH-LOG on main)** · DONE: the owner published the $29 listing personally — <https://mennomagic01.gumroad.com/l/stripe-webhook-test-kit> returns **HTTP 200** (`price_cents 2900`, `is_published true`), independently re-verified 2026-07-12T16:28:47Z. **T = 2026-07-12T16:25Z; deadline T+14 = 2026-07-26.** Record: `docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`. · VERIFIED-WHEN: **SATISFIED** (live listing URL returns HTTP 200; T+14 clock started). Now watch for the kill-rule signal by T+14.
```

### venture-lab — - **⚑ FOLLOW-UP (post-launch, conditional) — move the paid zip out of the public repo tree if sales materiali…

- suggested-id: `OQ-VENTURE-LAB-FOLLOW-UP-POST-LAUNCH`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ FOLLOW-UP (post-launch, conditional) — move the paid zip out of the public repo tree if sales materialize** · WHAT: relocate the paid product artifacts (`candidates/stripe-webhook-test-kit/dist/stripe-webhook-test-kit-v0.1.zip` and the sibling paid zips) out of the public `menno420/venture-lab` tree so the paid download is not obtainable for free from GitHub. · WHY: the public repo currently exposes the paid zip for free — this is **KNOWN and ACCEPTED for launch** (the kit's value is the code + support, and the source lessons are already public), but if the listing draws real sales the free-download leak becomes worth closing. · TRIGGER: ≥1 organic sale (per the T+14 kill-rule signal). · VERIFIED-WHEN: the paid zip is no longer served from the public repo tree (moved to a release-gated / owner-only artifact) while the buyer download path stays intact.
```

### venture-lab — - **⚑F — publish the Agent Fleet Field Manual at $39 — QUEUED ✅** · WHAT: publish per `docs/launch/agent-flee…

- suggested-id: `OQ-VENTURE-LAB-F-PUBLISH-AGENT-FLEET`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑F — publish the Agent Fleet Field Manual at $39 — QUEUED ✅** · WHAT: publish per `docs/launch/agent-fleet-field-manual/publish-owner-action.md`, uploading `candidates/agent-fleet-field-manual/dist/agent-fleet-field-manual-v0.1.zip` at $39. Gumroad-hosted — no custom payment path, so the D1/Stripe gate does not apply. Conservative: 0–4 sales/90d ($0–$156); $0 without distribution. · VERIFIED-WHEN: live listing URL returns HTTP 200 on a purchasable $39 page AND ≥2 free chapters live.
```

### venture-lab — - **⚑ — publish the free gotcha article — PUBLISHED ✅ 2026-07-12** · DONE: the owner published it personally …

- suggested-id: `OQ-VENTURE-LAB-PUBLISH-FREE-GOTCHA-ARTICLE`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ — publish the free gotcha article — PUBLISHED ✅ 2026-07-12** · DONE: the owner published it personally on dev.to (owner click, 2026-07-12T17:18:47Z) — <https://dev.to/menno420/your-stripe-webhook-says-customeremail-is-null-heres-why-and-the-fix-1bgp> returns **HTTP 200** (independently re-verified 2026-07-12T17:24:10Z; product link `gumroad.com/l/stripe-webhook-test-kit` present 2×; **ZERO tags** observed at fetch time — discoverability follow-up flagged). The funnel top is live; article→listing→sales measurement (dev.to reactions/comments + Gumroad analytics, checkpoints 2026-07-19 / 2026-07-26) is recorded in `docs/launch/stripe-webhook-test-kit/LAUNCH-LOG.md`. · VERIFIED-WHEN: **SATISFIED** (article live at a public URL, HTTP 200).
```

### venture-lab — - **⚑G — enable GitHub Pages (Bababoefoe QR story-site) — $0** · WHAT: enable GitHub Pages per `candidates/ba…

- suggested-id: `OQ-VENTURE-LAB-G-ENABLE-GITHUB-PAGES`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑G — enable GitHub Pages (Bababoefoe QR story-site) — $0** · WHAT: enable GitHub Pages per `candidates/bababoefoe/MAKE-IT-REAL-PLAN.md` Phase 0 ($0, no accounts, no spend). · VERIFIED-WHEN: the Pages URL returns HTTP 200 on the story index.
```

### venture-lab — - **⚑ — owner photo samples upload (photo-packs)** · WHAT: upload downsized (**≤2048px**) **watermarked** pre…

- suggested-id: `OQ-VENTURE-LAB-PHOTO-SAMPLES-UPLOAD-PHOTO`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ — owner photo samples upload (photo-packs)** · WHAT: upload downsized (**≤2048px**) **watermarked** previews to `candidates/photo-packs/samples/` per the LOUD safety rule in `candidates/photo-packs/PACK-SPEC.md` — full-res originals NEVER enter this public repo; `candidates/photo-packs/validate_samples.py` enforces the caps. · VERIFIED-WHEN: validator exits 0 with ≥1 real sample and the gallery renders it.
```

### venture-lab — - **⚑ (optional) — Supabase project for hosted persistence** · WHAT: create a Supabase project + `members` ta…

- suggested-id: `OQ-VENTURE-LAB-OPTIONAL-SUPABASE-PROJECT-HOSTED`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ (optional) — Supabase project for hosted persistence** · WHAT: create a Supabase project + `members` table per the six-field OWNER-ACTION in `candidates/membership-kit/server/README.md` (env NAMES only in repo). · VERIFIED-WHEN: members survive a restart via Supabase.
```

### venture-lab — - **⚑ — decide-and-flag decisions open for retroactive veto (ORDER 006 mirror)** · WHAT: (1) all merges 2026-…

- suggested-id: `OQ-VENTURE-LAB-DECIDE-FLAG-DECISIONS-OPEN`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ — decide-and-flag decisions open for retroactive veto (ORDER 006 mirror)** · WHAT: (1) all merges 2026-07-11 executed under a standing-grant reading (owner in-session event b92aab44); (2) the idle pacemaker cadence adjusted with a 2-hourly failsafe backstop. · ASK: veto either retroactively, or no action needed to keep them.
```

### venture-lab — - **⚑ — close PR #51 + delete branch `menno420-patch-1` (photo exposure): RESOLVED.** PR #51 CLOSED unmerged …

- suggested-id: `OQ-VENTURE-LAB-CLOSE-PR-51-DELETE`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ — close PR #51 + delete branch `menno420-patch-1` (photo exposure): RESOLVED.** PR #51 CLOSED unmerged + branch deleted 2026-07-12T09:39:15Z. (The 10 uploaded originals remain in forks/history — unchangeable; noted as a standing fact above, no open action.)
```

### venture-lab — - **⚑ — disposition PR #38 (stale codex pre-publish review): RESOLVED.** PR #38 (`codex/review-code-for-publi…

- suggested-id: `OQ-VENTURE-LAB-DISPOSITION-PR-38-STALE`
- source: venture-lab/control/status.md @ `24eb11d` · heartbeat `updated:` 2026-07-12T18:09Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ — disposition PR #38 (stale codex pre-publish review): RESOLVED.** PR #38 (`codex/review-code-for-publish-blockers`) is **CLOSED, NOT merged** (closed 2026-07-11T19:58:37Z) — superseded by the merged #49 fail-closed hotfix. No owner action remains.
```

### superbot-games · Seat A — ⚑ needs-owner: see the OWNER-ACTION block below + docs/retro/archive-ready-2026-07-11.md

- suggested-id: `OQ-SUPERBOT-GAMES-SEE-BLOCK-BELOW-DOCS`
- source: superbot-games/control/status.md @ `0082ee2` · heartbeat `updated:` 2026-07-11T19:39:14Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: see the OWNER-ACTION block below + docs/retro/archive-ready-2026-07-11.md
```

### ↳ superbot-games · Seat A — `control/status-exploration.md` — ⚑ needs-owner: \|

- suggested-id: `OQ-SUPERBOT-GAMES-FLAG`
- source: superbot-games/control/status-exploration.md @ `0082ee2` · heartbeat `updated:` 2026-07-09T20:09Z
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

### superbot-mineverse — ⚑ MERGE-ORDER: merge PR #42 (this login-CSRF fix) BEFORE provisioning the secrets below, so sign-in never run…

- suggested-id: `OQ-SUPERBOT-MINEVERSE-MERGE-ORDER-MERGE-PR`
- source: superbot-mineverse/control/status.md @ `e6d4ac7` · heartbeat `updated:` 2026-07-11T23:51:34Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ MERGE-ORDER: merge PR #42 (this login-CSRF fix) BEFORE provisioning the secrets below, so sign-in never runs in production without the per-browser binding in place.
```

### pokemon-mod-lab — 1. **⚑ OWNER-ACTION 1 — `ROM builds` required-check click.** GitHub →

- suggested-id: `OQ-POKEMON-MOD-LAB-1-1-ROM-BUILDS`
- source: pokemon-mod-lab/control/status.md @ `759dee4` · heartbeat `updated:` 2026-07-11T21:03:45Z
- possibly-covered-by: none matched (manual dedup needed)

```text
1. **⚑ OWNER-ACTION 1 — `ROM builds` required-check click.** GitHub →
   Settings → Rules → `main` ruleset → require status checks → add
   `ROM builds` (keep `substrate-gate`). No agent API surface for
   rulesets (`docs/PLATFORM-LIMITS.md`).
```

### pokemon-mod-lab — 2. **⚑ OWNER-ACTION 2 — next-arc concept pick.** One word: continue

- suggested-id: `OQ-POKEMON-MOD-LAB-2-2-NEXT-ARC`
- source: pokemon-mod-lab/control/status.md @ `759dee4` · heartbeat `updated:` 2026-07-11T21:03:45Z
- possibly-covered-by: none matched (manual dedup needed)

```text
2. **⚑ OWNER-ACTION 2 — next-arc concept pick.** One word: continue
   Emerald QoL+ (new-lead spikes) / Emerald Hard / Nuzlocke Mode
   (`docs/mod-concepts.md`). Lane default remains QoL+; reversible.
```

### pokemon-mod-lab — 3. **⚑ OWNER-ACTION 3 — playtest verdict on the 6 game-feel patches**

- suggested-id: `OQ-POKEMON-MOD-LAB-3-3-PLAYTEST-VERDICT`
- source: pokemon-mod-lab/control/status.md @ `759dee4` · heartbeat `updated:` 2026-07-11T21:03:45Z
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
- source: pokemon-mod-lab/control/status.md @ `759dee4` · heartbeat `updated:` 2026-07-11T21:03:45Z
- possibly-covered-by: none matched (manual dedup needed)

```text
4. **⚑ stale ref `track-a/session-019` — owner click to delete**
   (content squash-merged via PR #24 long ago; sessions must not touch
   it).
```

### pokemon-mod-lab — 5. **⚑ NEW (housekeeping) — stale ref `track-a/session-024` — owner

- suggested-id: `OQ-POKEMON-MOD-LAB-5-NEW-HOUSEKEEPING-STALE`
- source: pokemon-mod-lab/control/status.md @ `759dee4` · heartbeat `updated:` 2026-07-11T21:03:45Z
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
- source: pokemon-mod-lab/control/status.md @ `759dee4` · heartbeat `updated:` 2026-07-11T21:03:45Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- OWNER-ACTION 4 (wake-env GitHub write tools) and OWNER-ACTION 5
  (`add_repo` classifier denials): **RESOLVED** — 20 consecutive clean
  wake cycles (024–043). Reopen only on regression.
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
- source: idea-engine/control/status.md @ `fa38a95` · heartbeat `updated:` 2026-07-12T18:10:58Z (real wall-clock via date -u, per the …
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: ARCHIVE HANDOFF (this slice, wrap-up — read FIRST at next wake): (1) STANDING RULING Q-0265, CONTINUOUS-CHAINING MODE — restored DURABLY here this slice (it previously lived only in session cards, grep of this file was negative): the coordinator chains bounded slices CONTINUOUSLY via child sessions, the next slice dispatching as each one reports; the 2-hourly cron trigger is a FAILSAFE DEADMAN WAKE, not the work cadence (README § Coordination; first recorded live in this file @ 139932e). The archiving coordinator's failsafe cron trigger AND its 15-minute send_later chain are being DISMANTLED with the chat archive — a fresh coordinator MUST RE-ARM BOTH per Q-0265 at first wake. (2) THE ≤07-13 OWNER SITTING BUNDLE (context: Projects are free through 2026-07-14, the owner consolidates after — decide ≤2026-07-13): FOUR decisions in ONE sitting — (a) Lumen Drift itch.io go/no-go (standing OWNER-ACTION entry below), (b) pokemon playtest verdicts (fm docs/owner-queue.md item 3), (c) the gba concept pick (the lane's own heartbeat ⚑), (d) the post-EAP standing-routine posture (standing entry below — RECOMMENDED Option A). (3) WEBSITES CUTOVER choice — one structured reply, RECOMMENDED Option A (the standing entry below, first item). The standing entries follow VERBATIM from the prior overwrite: STANDING (routed by #159, preserved verbatim this slice again) — WEBSITES CUTOVER-ROLE, one structured choice (fan-in of the websites lane's own OWNER-ACTIONS rows 6/4/1 @ 92c3dc6 — the canonical rows STAY on the lane's surface; this entry only bundles three rows that are really ONE decision into a single paste-ready sitting, per the fewer-clearer-asks hygiene): ⚑ OWNER-ACTION WHAT: one reply deciding the websites cutover role — go/no-go on retiring superbot's old dashboard/ + botsite/ site services, where bot control lives (websites / superbot / superbot-next), and (optionally) domains. WHERE: reply in any owner channel the manager sweep reads; the lane executes from its own list — menno420/websites docs/owner/OWNER-ACTIONS.md rows 1/4/6 (optional 2-min pre-check first: open the three live site URLs linked from the websites README, or have the lane run its scripts/healthcheck.py — its own row 6 asks for exactly that verify-then-go). HOW (paste ONE line — recommendation first): RECOMMENDED "Cutover Option A: go — retire superbot's dashboard/ + botsite/ services; the new sites keep reading old-repo data until the bot cutover; bot control home = superbot-next (ruled now, wired later); domains stay deferred." · Alternatives: "Option B: botsite-only go now, dashboard later" (the lane plan's own site order) · "Option C: hold everything for one combined cutover when superbot-next reaches parity" (zero clicks now; cost = dual-maintenance for the parity months) · "Option D: no-go — deliberately keep dual-running." WHY-IT-MATTERS: the replacements are live and verified daily (all three services deploy-verified at websites 1ff77e4); while the call is unmade you pay dual maintenance on old+new sites and the de-facto answer bakes in. UNBLOCKS: websites rework-plan steps 3/5 (retiring the last dual-running old-repo web surfaces), the Q4 control-panel wiring path, domain assignment — and closes this repo's superbot #155 shortlist item 2 for good. VERIFIED-NEEDED: owner-gated by rule, not capability — the lane's own surface marks the retirement "Gated: needs your go" (OWNER-ACTIONS row 6 @ 92c3dc6) and the control home "Do not port without an owner call" (row 1); its question-router Q6 reads "(unanswered — deferred to cutover)"; DNS/service retirement are owner-only Railway/DNS mutations (the lane's D‑0005 class), deliberately not attempted from any agent seat. ALSO STANDING (preserved verbatim from #158): SELF-REVIEW 2026-07-11 (ORDER 002): owner items collected in the Self-review record at docs/retro/self-review-2026-07-11.md (moved verbatim from the foot of this file at the 2026-07-11 wrap-up) — the ≤2026-07-14 sitting bundle (FOUR decisions as of #174, standing entries below) + the venture-lab two repo toggles (#110) + the Q-0266 framing veto window. Prior text verbatim: SHARED-WINDOW NOTE UPDATE (this slice, same fewer-clearer-asks hygiene): the gba-homebrew CONCEPT PICK (lane ⚑ @ c7592d6 — Lumen-deepening / Clockwork Courier / Shoal, full click path on the lane's own heartbeat; seeded-cave-runs is now the costed 'more Lumen' option, this slice's park) is the THIRD item landing in the SAME ≤2026-07-14 EAP sitting — deliberately NOT a new ⚑ here, the ask lives on the LANE's own heartbeat (one ask, one owner surface); the sweep should read the sitting as carrying FOUR bundled decisions: (1) the Lumen Drift itch.io go/no-go standing entry below, (2) fm docs/owner-queue.md item 3 (pokemon playtest verdicts), (3) the gba concept pick, (4) the post-EAP routine posture (#174's entry, below). The prior note follows verbatim: SHARED-WINDOW NOTE (this slice, hygiene per fewer-clearer-asks): the pokemon-mod-lab playtest-kit park (this slice) is deliberately NOT a new ⚑ here — its owner ask already lives as fm docs/owner-queue.md item 3 @ 1afca50 (one ask, one owner surface, the manager's); what the sweep must see is that BOTH owner-sitting items — the Lumen Drift ⚑ OWNER-ACTION below AND that queue item — land in the SAME EAP sitting, window ends 2026-07-14; the kit-preparation routing (fm order or lane self-serve) is the manager-side item flagged in notes. The standing entry follows verbatim: ⚑ OWNER-ACTION (from this slice, decision-adjacent — EAP window ends 2026-07-14): WHAT: post-EAP go/no-go + one itch.io sitting to publish Lumen Drift as a PWYW listing. WHERE: itch.io (account) + gba-homebrew dist/lumen-drift.gba v1.3 (sha256 195a867…, provenance dist/README.md) + the parked idea ideas/venture-lab/games-adjacent-candidate-three-2026-07-10.md. HOW: play Lumen Drift during the EAP sitting; on go: create itch.io account → New project → set pay-what-you-want → upload dist/lumen-drift.gba → publish (venture-lab pre-drafts the full listing copy so this is paste-and-click). WHY-IT-MATTERS: first second-channel distribution datapoint + a publish pipeline every finished fleet game inherits, at zero build cost. UNBLOCKS: the parked candidate #3, venture-lab's listing-kit prep, and gives revenue-ingestion-owner-relay its first non-marketplace source. Sequencing note (from the #97-era probe): the click need NOT wait on the revenue-ingestion relay — itch.io/marketplace sales exports are retro-downloadable, so pre-relay sales stay recoverable; the lane lands the ledger convention independently (fan-in below, flagged ORDER-worthy). VERIFIED-NEEDED: account creation/external publishing is rail-banned for agents on both lanes' READMEs (venture-lab @ 0ad0ea4, gba-homebrew @ 31c8672) — owner-only by rule, not by missing capability. ALSO note for the :30 sweep: the wake-resilience verdict (PR #56) is gated on an owner click that already lives as a six-field OWNER-ACTION entry on the TRADING-STRATEGY lane's own heartbeat @ `d0d789e` (⚑ (b): paste environments/setup-universal.sh into that project's environment setup-script field); deliberately NOT duplicated here per the fewer-clearer-asks hygiene — one ask, one owner surface, the lane's. Routed via the trading-strategy fan-in note below. SAME hygiene for venture-lab's ⚑B/⚑D publish clicks (launch-ready, UNFROZEN @ `9f1b616`) — they live as owner-action entries on the LANE's own docs/launch/membership-kit/owner-actions.md, deliberately NOT duplicated here; routed via the venture-lab fan-in note below. STANDING FROM #174 (decision 4 of the ≤07-14 sitting): ⚑ OWNER-ACTION (from #174, HARD deadline — decide ≤2026-07-13, EAP window wraps 2026-07-14): WHAT: one reply setting the post-EAP standing-routine posture — what keeps firing on paid usage after 07-14. WHERE: reply in any owner channel the manager sweep reads; execution is manager-side trigger edits (roster gen #5 @ fm 7c13be7: 32 enabled = 15 standing crons + 2 poke-only + 15 one-shots). HOW (paste ONE line — recommendation first): RECOMMENDED "Post-EAP routines Option A: core-6 Projects keep current cadence (per Q-0261), every other standing cron drops to daily, one-shots expire on completion; revisit at first paid invoice." · Alternatives: "Option B: keep all 15 standing crons as-is (accept unmetered paid burn)" · "Option C: freeze all crons at window close; owner wakes lanes manually" · "Option D: name a monthly budget figure; manager thins cadence to fit and reports the cut list." WHY-IT-MATTERS: with no ruling, Option B happens by inertia — every cron fires into the paid period at a burn no agent can measure (fm fleet-economics honest-nulls: token/$ "not measurable"). UNBLOCKS: the manager's pre-close cadence sweep; closes the open post-EAP pricing question (superbot projects-eap-product-review-2026-07-07.md:150); the mechanical limit-deferred half proceeds independently as superbot's plan (PR #1845). VERIFIED-NEEDED: owner-only by evidence — no post-EAP budget ruling exists anywhere (full-tree greps of fresh clones superbot @ 9f46cb7 + fleet-manager @ 7c13be7 at #174; only the open question and Q-0261's "until the EAP ends" boundary), and spend/billing surfaces are owner-UI-only (fm model-matrix: no agent-visible field on any probed surface). ⚑ GIFT REPO (from #264): one reply decides — repo name (rec: makerbench), visibility (rec: private + friend as collaborator), project cut (rec: all five a-e). Optional add-on: buy a PCA9685 16-ch servo driver (~€10) — the arm kit has no controller and project (c) assumes one. Unblocks slice-1 routing. Full paste-ready line in ideas/venture-lab/maker-gift-repo-blueprint-2026-07-12.md.
```

### codetool-lab-opus4.8 — ⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTI…

- suggested-id: `OQ-CODETOOL-LAB-OPUS4-8-1-DELETE-LEFTOVER-BRANCH`
- source: codetool-lab-opus4.8/control/status.md @ `80f6cd1` · heartbeat `updated:` 2026-07-09T20:11:35Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTIONAL PyPI publish of mdverify (needs owner token; name free as of 2026-07-09); (3) OPTIONAL Claude GitHub App connect for native tag/release
```

---

58 candidate block(s) across 14 lane(s). Feed is additive-noise-tolerant by design: over-capture is curated out by the manager; silent stranding is the failure this feed exists to kill.

