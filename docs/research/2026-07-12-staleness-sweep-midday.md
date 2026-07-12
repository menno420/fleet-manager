# Staleness sweep — midday 8-seat sweep + v3.3 adoption check

> **Status:** `audit`
>
> Claims-vs-reality sweep of all 8 standing seats (14 repos at origin/main HEAD), executed ~2026-07-12T11:17–11:25Z by the midday oversight session (PR #113). Companion trigger snapshot: full `list_triggers` export re-captured this session (832 triggers, 9 pages) → `telemetry/triggers-snapshot.json`; roster regenerated gen 14. Previous sweep: [2026-07-12-staleness-sweep-8seat.md](2026-07-12-staleness-sweep-8seat.md) (~04:00Z).

## Verdict table

Verdicts: FRESH / STALE (heartbeat contradicted or drifted) / DARK (no heartbeat, recent commits) / DEAD (no heartbeat, no commits). Seat = worst constituent. Adoption = prompt generation evidenced by the latest live-session artifacts at origin/main (pre-rebuild is expected while owner pastes are in progress, not a fault).

| Seat | Repo | 04:00Z | Midday | Adoption | Evidence |
|---|---|---|---|---|---|
| fleet-manager | fleet-manager | FRESH | **FRESH** | **v3.3-native** | heartbeat 11:03:55Z vs HEAD `d4989c9` 11:06Z (#112); substrate-gate green; status quotes "COMPLETE through v3.3 … BOOT TRIAD (superbot Q-0270)" |
| superbot-2.0 | superbot | FRESH | **FRESH** | pre-rebuild | hub Q-0264 HEAD-activity fallback; #2017–#2026 merged this morning, HEAD `35ddf6e` all CI green; Q-0270 boot-triad doctrine merged (`28e39cc`) but no v3.x boot markers yet |
| superbot-2.0 | superbot-next | FRESH | **FRESH** | pre-rebuild | heartbeat 09:35Z (#247), HEAD `aece46b` 11:02Z; **parity program COMPLETE 50/50**; required ci+named-gates green, gate grown 346→383; golden-parity red-by-design |
| websites | websites | FRESH | **FRESH*** | **v3.2** | active boot did ORDER 012/013 work (PRs #159/#160 CI-green) but *on-main heartbeat 2026-07-11T19:49Z is contradicted* (still claims #141 open; fix parked in #160 behind the owner-merge wall); inbox provenance "STATELESS since v3.2" + boot-triad-style model line on `.sessions/2026-07-12-projects-dispatch-view.md` |
| self-improvement | substrate-kit | FRESH | **FRESH** | pre-rebuild | 9 merges since 04:00Z (ORDER 015 done #261, grounded-skills #263–#265, latest merged 11:19:53Z mid-sweep); heartbeat 09:40Z benign lag; pins #238/#220 unchanged |
| superbot-world | superbot-games | STALE | **STALE** | pre-rebuild | NOT re-stamped: `updated: 2026-07-11T19:39:14Z` byte-identical to 04:00Z; still claims 5 merged PRs "parked"; ORDER 005 truth-stamp (merged `9efe599` #61 08:34Z) unexecuted; PRs #59/#60 heartbeat-invisible |
| superbot-world | superbot-idle | FRESH | **STALE** | pre-rebuild | "ARCHIVED-READY / dormant … wake loop DISARMED" (19:37:36Z) contradicted by live PRs #72 + #74 (ORDER 003 pytest CI, opened 10:16Z); no re-stamp |
| superbot-world | superbot-mineverse | FRESH | **STALE** | pre-rebuild | "all remaining work externally blocked" (19:45Z) contradicted by green agent-actionable security PR #42 (head `2557f1a` static ~11.4h); ORDER 003 P1 (merge #42 first) unexecuted; push-to-main CI silence now covers `76be821` AND `f8b6dbf` |
| game-lab | gba-homebrew | FRESH | **FRESH** | pre-rebuild | heartbeat 09:47:37Z cycle-2; #60–#63 merged, #61 owner-clicked 10:25Z (`d1f1981`, CI green); #64/#65 parked green for owner click |
| game-lab | pokemon-mod-lab | FRESH | **STALE** | pre-rebuild | heartbeat 2026-07-11T21:03:45Z claims "no orders beyond 005" + main unchanged at `acaf139` — contradicted by ORDER 006 (#53, `2efe16d` 08:35Z) and #52; ack pending (self-flagged in seat status) |
| ideas-lab | idea-engine | FRESH | **FRESH** | pre-rebuild | heartbeat 10:49:12Z vs HEAD `f92bd26` 10:50Z (58s); ~38 PRs merged in 12h; ORDER 003 done; deliberately not front-running v3.2 cutover (self-flagged) |
| ideas-lab | sim-lab | FRESH | **FRESH** | pre-rebuild | heartbeat 10:34:41Z vs HEAD `055245e` 10:36Z; ORDER 003 merge-on-green landed live (#50–#52, zero agent merge calls) |
| venture-lab | venture-lab | FRESH | **FRESH** | pre-rebuild | heartbeat 00:36:27Z; #59–#62 + owner-clicked #57 (`4c2e623` 09:40Z, kit-tests+substrate-gate green); benign newest-lag on #57/#51 terminal states |
| venture-lab | trading-strategy | FRESH-borderline | **FRESH** | pre-rebuild | borderline CLEARED: parked #64 closed-superseded by #66, MERGED 08:24Z via new auto-merge enabler (#65); heartbeat 10:35:26Z, HEAD `1f9cbac` (#70) 11:13Z |

Seat roll-up: **6 FRESH / 2 STALE** (superbot-world 3/3 STALE — worsened from 1/3; game-lab STALE — new). No DARK, no DEAD.

## Headline deltas vs the 04:00Z sweep

1. **superbot-world worsened 1→3 STALE.** games was never re-stamped despite ORDER 005 directing exactly that; idle and mineverse heartbeats are now *contradicted* (dormancy/blocked claims vs live PR work). The manager's 08:32–08:34Z ORDER appends (#61/#73/#43) are current; the seats' heartbeats are what lag.
2. **websites v3.3-boot delta: ORDER 012/013 executed but NOT landed.** PR #159 (ORDER 013 CSRF, P1 security) and #160 (ORDER 012 records reconcile incl. the heartbeat fix) are both CI-green and parked behind the owner-merge wall; inbox still says `status: new`. #158 (dispatch console) merged 09:48Z by owner click. Note: #160's body claims an auto-merge enabler exists; #158's body says the repo has none — contradiction to resolve.
3. **superbot-next milestone: parity program COMPLETE at 50/50** (#245–#247), gate 346→383 via wave-9 re-homes (#248–#250).
4. **trading-strategy borderline cleared** — #64 superseded by #66 and auto-merge-enabler self-landing is now live in both money-seat repos.
5. **venture-lab #51 (owner photos): closed unmerged 09:39Z, branch deleted, BUT the 10 photos remain publicly fetchable via `refs/pull/51/head` (`634b528`)** — full purge is an owner/GitHub-Support action.
6. **pokemon-mod-lab FRESH→STALE**: ORDER 006 landed (#53) without a status ack.

## v3.3 adoption summary (feeds the owner's paste checklist)

- **v3.3 booted:** fleet-manager only (v3.3-native; it is the generator).
- **v3.2 evidenced:** websites (stateless-prompts provenance + boot-triad-style card; no v3.3 markers on main).
- **Pre-rebuild boots (expected):** superbot, superbot-next, substrate-kit, superbot-games, superbot-idle, superbot-mineverse, gba-homebrew, pokemon-mod-lab, idea-engine, sim-lab, venture-lab, trading-strategy — zero v3.2/v3.3/BOOT TRIAD markers at origin/main; only fleet-manager-authored inbox provenance lines mention v3.2. ideas-lab explicitly self-flags "deliberately NOT front-running the cutover".

## Trigger snapshot (832 triggers, captured ~11:10–11:40Z this session)

Of the 832 triggers, **28 are enabled** (9 standing crons + 19 pending one-shots) and **804 are disabled/ended**: 795 `run_once_fired` (normal one-shot lifecycle), 4 `auto_disabled_session_gone`, 3 `auto_disabled_env_deleted`, and 2 user-paused (empty ended_reason). Zero duplicate IDs across the 9 pages (100×8 + 32).

Standing recurring routines live in the export: `trig_01Aak59jvQQdimDgy5K1yAGQ` · Websites failsafe wake · `45 */2 * * *` · session_01GXxCAogDJm82B7dbrqV8Ek; `trig_01JD1t7rD5jUCqkJQJaNCi3E` · game-lab failsafe wake · `50 */2 * * *` · session_01SphTJEnN1PYjYZhHNWoJik; `trig_01T83UuVthszGBcENYwrTrm7` · Ideas Lab failsafe wake · `0 */2 * * *` · session_013Ex3R3fn7VMCkuXrErB9vq; `trig_01Jm57GAjNCFrYJn1oLMiYGE` · kit-lab loop · `0 6 * * *` · fresh-session-per-fire (env_01WAB3QKMneNpWKuR1ZLVsVX); `trig_01KQbKNiSVfZRWutKEWFx2q2` · SuperBot World failsafe wake · `0 */2 * * *` · session_01D89CYdLhQfzQHDFKkDSDX2; `trig_01BKpsyoBzp1K1ob9H3iu1gM` · fleet-manager failsafe wake · `30 */2 * * *` · session_01FMJoC5uC6WSUTosceTGcmo; `trig_011iJucRpsruWJ4dFB7xVbvf` · substrate-kit failsafe wake · `0 */2 * * *` · session_01G7tWPmizaEC7AXt829p5Th; `trig_015aNMg5ncoSE2Roe4MKjQnr` · trading-strategy weekly paper-lane grading · `0 9 * * 5` · session_0126Cc5VUJkxn7C3A43j31pg; `trig_017o6azZTd9pzcaSthEncT5q` · venture-lab money-seat failsafe wake · `0 */2 * * *` · session_0126Cc5VUJkxn7C3A43j31pg. Notable dead/paused: trading-strategy failsafe wake + Builder failsafe wake both `auto_disabled_env_deleted`; "superbot autonomous dispatch" (`0 */3 * * *`) and "superbot night executor" user-paused. Context for verdicts: superbot's overnight-review card documents a CCR trigger-scheduler degradation ~02:30–08:00Z on 2026-07-12 (9 one-shots dropped, 2 crons wedged) — weigh before blaming a seat for a missed wake.

## Systemic findings

1. **Bot-token merges suppress push-CI on main across the fleet.** substrate-kit, idea-engine, sim-lab, venture-lab, trading-strategy (and likely mineverse) show zero push-event workflow runs on merge commits landed by github-actions[bot]; required PR-head checks still gate every merge. Sweeps and the roster must not read absent HEAD runs as CI silence. Consider a `ROUTINE_PAT` or post-merge workflow if main-branch runs matter for telemetry.
2. **roster-regen scheduled workflow failed its landing step 4× today** (GH013 ruleset: Actions can't create PRs) — known owner item OQ-FM-ACTIONS-PR-PERMISSION; content steps green, so regens only land via sessions like this one.
3. **kit-lab fresh-session cron 2-for-2 missed fires** (substrate-kit status; platform question parked with the manager).

## Needs-attention shortlist (ranked)

1. superbot-mineverse **PR #42 security fix** (login-CSRF) green + static ~11.4h; ORDER 003 P1 says it merges before anything secrets-adjacent — unexecuted.
2. venture-lab **#51 residual photo exposure** via `refs/pull/51/head` — owner/GitHub-Support purge required (report-only).
3. superbot-world **heartbeat truth-stamps**: games ORDER 005 unexecuted; idle + mineverse contradicted heartbeats need re-stamps.
4. websites **owner merge clicks**: #160 (fixes the lying on-main heartbeat) then #159 (P1 CSRF), then #161; also resolve the #158-vs-#160 auto-merge-enabler contradiction.
5. pokemon-mod-lab **ORDER 006 status ack** (one heartbeat overwrite clears the STALE).
6. gba-homebrew **#64/#65** parked green for owner clicks.
7. substrate-kit **pins #238/#220 aging** (owner ratification) + kit-lab cron broken.
8. ideas-lab flag: **owner four-decision bundle due ≤2026-07-13**.
9. trading-strategy **draft PR #69** expects to self-land but the enabler skips drafts — flip ready or it dangles.
