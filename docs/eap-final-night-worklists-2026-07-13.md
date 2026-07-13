# EAP final-night worklists — 2026-07-13

> **Status:** `plan`

**Provenance:** ORDER 045 — owner directive, live in the FM coordinator chat
2026-07-13 ~21:34Z, recorded verbatim in [`../control/inbox.md`](../control/inbox.md)
(the goal: every project has a full list to work on tonight — the last day of the
EAP). Phase 1+2 (sweep + synthesis) execute in this session's PR #178; Phase 3
(lane fan-out) is the follow-up dispatch.

**Generated:** 2026-07-13T21:53:16Z · **Roster basis:** Generation #35
(`docs/roster.md`, generated 2026-07-13T21:30Z) · **Sweep:** 7 parallel read-only
workers, every claim SHA-cited.

**Sweep HEADs:**

| Repo | HEAD swept |
|---|---|
| fleet-manager | `c5dc151` (origin/main at boot; session branch `59ffe56`) |
| superbot (hub) | `f969b95` |
| superbot-next | `5dac6ce` |
| superbot-idle | `1f4d774` |
| superbot-mineverse | `ae98dd0` |
| websites | `31b5d00` |
| substrate-kit | `736e114` |
| trading-strategy | `499876f` |
| venture-lab | `be6c75d` |
| idea-engine | `2808b16` |
| sim-lab | `32ff5c3` |

Why-tonight tags: `[lane]` unfinished lane work · `[standing]` standing/unconsumed
ORDER · `[verdict]` sim verdict served/approved awaiting build · `[build-direct]`
idea-engine plan marked buildable without a sim verdict · `[improve]`
feature-improvement · `[drift]` docs/heartbeat drift fix · `[deadline]` window
closes 07-14 · `[relay]` fm routing/relay debt.

---

## Fleet summary

| Seat | Roster verdict (gen #35) | Open PRs | Worklist | Top item |
|---|---|---|---|---|
| superbot (hub) | STALE ~11h45m | 11 (#2087 + 8 dependabot + 2 held drafts) | 8 | Drive PR #2087 to terminal state |
| superbot-next | FRESH ~3h27m | 7 (WP stack ×5 + #392 + #414 claim) | 8 | WP-stack conflict reconcile |
| superbot-idle | FRESH ~3h47m | 0 | 4 | Catalog wave 5 |
| superbot-mineverse | FRESH ~2h45m | 0 | 5 | FLAG-1 snapshot-ingest endpoint |
| websites | STALE ~9h59m | 9 (1 ready + 1 held + 7 lifeboats) | 8 | Shepherd #304 to green |
| substrate-kit | STALE ~5h27m | 1 (#317 owner-parked) | 7 | Session-gate false-green fix (ASK 003) |
| trading-strategy | STALE ~5h04m | 0 | 5 | Pre-registered Round-6 plan |
| venture-lab | STALE ~5h04m | 0 | 7 | Next product to publish-READY |
| idea-engine | FRESH ~1h24m | 0 | 6 | V054/V055 closure + claim prunes |
| sim-lab | FRESH ~1h22m | 0 | 5 | PROPOSAL 047 → VERDICT 058 |
| fleet-manager (self) | FRESH ~31m | 1 (#178, this session) | 7 | Route V055–V057 + verify V046–V054 |

---

## superbot (hub) — swept @ `f969b95`

No unconsumed hub ORDERs (001/002 done); no PLAN BACKLOG THIN flag anywhere.

1. Drive PR #2087 (I1b frozen-trigger disposition relay) to a terminal state — open, ready, conflict-guard green (superbot PR #2087) `[lane]`
2. Dependabot sweep: disposition/merge the 8 open bumps (superbot PRs #2077–#2084) `[standing]`
3. EAP email-3 prep — Part-1 voice + roster screenshot; SENDS 2026-07-14 (`docs/eap/anthropic-email-3-draft-2026-07-13.md@f969b95`) `[deadline]` (the send itself is owner-gated)
4. Build `check_reconciliation_consistency.py` four-homes guard — quick win, disposable (`docs/ideas/reconciliation-four-homes-consistency-guard-2026-07-12.md@f969b95`) `[improve]`
5. Casino triage trio build inputs — verdicts V022/V025/V029 closed on house-edge / entry-fee / comp-stipend (idea-engine `ideas/superbot/casino-house-edge-fairness-envelope-2026-07-13.md` +2 siblings @`2808b16`) `[verdict]`
6. One idea-engine build-direct slice: BTD6 CT event-detail relics map or leaderboard row avatars (idea-engine `ideas/superbot/btd6-ct-event-detail-relics-map-2026-07-10.md`, `leaderboard-row-avatars-2026-07-10.md` @`2808b16`) `[build-direct]`
7. S4 reconciliation-pass-history trim ratchet (`docs/ideas/s4-sector-pass-history-trim-ratchet-2026-07-13.md@f969b95`) `[improve]`
8. S2 next: curated counter lists / decode items 3–4 (`docs/current-state/S2-btd6.md@f969b95`) `[lane]`

**Blocked (do not schedule):** mineverse FLAG drafts #2058/#2061 (deploy-safety hold, owner flips) · WP-stack sweep-merge + 60-item DROP-list ratification + the stamped owner decision in `docs/owner-queue.md` (owner asks, `docs/eap/night-review-2026-07-13.md:106@f969b95`) · email-3 send (owner) · Q-0107 recon at #2100 (routine-fired, not due, Q-0124).

## superbot-next — swept @ `5dac6ce`

All 18 inbox ORDERs served except owner-side ORDER 001 (live-test token). NOTE: a
session is actively working this repo (claims #413/#414 landed 21:35–21:40Z) —
night workers must re-scan `control/claims/` at start.

1. WP-stack conflict reconcile — #312→#317→#335→#344→#371 now verifiably conflicts with main (4 files: `parity/cases/curated.py`, `parity/parity.yml`, 2 count-pin tests, via merge-tree) + re-mint the migration-0052-invalidated WP-2/3 goldens; merge itself stays owner-click (superbot-next PRs #312–#371) `[lane]`
2. Curation REWORK backlog bundle — next ~17 of the 27 backlog rows (`docs/review/curation-report-2026-07-13.md@5dac6ce`; 3 bundles already shipped as precedent) `[standing]` (ORDER 017 residue)
3. `tools/check_money_race.py` mis-classification fix — conditional-FOR-UPDATE ownership SELECT at `sb/domain/mining/ops.py:598` read as a fence; flagged in five consecutive WP PR bodies, never fixed `[improve]`
4. Fishing cast-leg profile wiring — venue/rod/bait/structure → cast (`sb/domain/fishing/service.py` PENDING-roster note; completeness table @`5dac6ce`) `[improve]`
5. Setup successor follow-ups, unclaimed subset — on-ready resume sweep, automation-rule apply seam, SectionRecoveryView, channel-recommender port; the compound-ops + routing-resolver subset is CLAIMED (PR #414) — do not duplicate (`docs/status/completeness-table-2026-07-13.md@5dac6ce`) `[lane]`
6. Host-side `plugins.lock.json` pin for the idle plugin adapter — executed from this seat; closes superbot-idle's live wiring gap (superbot-idle `control/status.md` Next-3 @`1f4d774`) `[lane]` (cross-repo)
7. Windowed-select grammar successor — needed on ≥2 surfaces, unlocks the parked mining title-equip select (completeness table @`5dac6ce`; PR #371 body) `[improve]`
8. Doc-only PR: band-binding doctrine + effect-arming compensator checklist — one `docs/collaboration-model.md` PR, gives ORDER 004 its `done=` citation hook (idea-engine `ideas/superbot-next/band-binding-doctrine-encoding-2026-07-10.md` + sibling @`2e5d73f`) `[build-direct]`

**Blocked (do not schedule):** casino/minigame section (ORDER 017 item 4 — awaits the SBW inventory/spec SIM-REQUEST answer, ⚑5) · hermes egress + AI NL lane (owner-keyed env) · ORDER 001 live-test band 1 (owner token) · mineverse #2058/#2061 flips + DROP-list ratify + the stamped owner decision in `docs/owner-queue.md` (owner).

## superbot-idle — swept @ `1f4d774`

Honest thin list — engine complete, all 5 ORDERs done (SIM-001 graduation shipped
#93; pytest CI shipped #74), zero open PRs; the queue is mostly waiting on others.

1. Catalog wave 5 — 3 data-only theme packs; explicitly sanctioned standing filler, merge on theme-gate green alone (`docs/current-state.md` roadmap item 3 @`1f4d774`) `[standing]`
2. SIM-REQUEST draft: min-visible-delta feltness floor — V038 ASK1 = CONFIRMED-INERT, needs its own sim; docs-only, unblocks a real tuning lane (`control/status.md` § ORDER 005 @`1f4d774`) `[improve]`
3. Close the `1 skipped` CI hole — CI job checking out pinned superbot-next so `plugin/tests/test_manifest.py` actually exercises the adapter contract (`docs/current-state.md` stability § @`1f4d774`) `[improve]`
4. Cross-repo pointer: the `plugins.lock.json` pin rides in superbot-next (its item 6) — track it, don't duplicate (`control/status.md` Next-3 @`1f4d774`) `[lane]`

**Blocked (do not schedule):** PRESTIGE_BONUS_PERCENT 10→25 (parked behind the SIM-PINNED re-tuning ruling, outbox ask 18:45Z) · timed-events (SIM-002 + owner Q-block) · generator-purchase economy (owner Q-block) — both Q-blocks await fleet Q-numbers from fm · OA-003 mark `pytest` required (owner click).

## superbot-mineverse — swept @ `ae98dd0`

Honest thin list — 0 open PRs, all 5 ORDERs done; most of the remainder is
owner/bot-blocked.

1. Build the FLAG-1 snapshot-ingest RECEIVE endpoint — superbot #2058 POSTs snapshots to `MINING_SNAPSHOT_RELAY_URL` every 60s but `server/app.py@ae98dd0` `do_POST` handles only `/api/action`; the receiving endpoint exists nowhere. HMAC-verified POST → v1-validate → persist (superbot PR #2058 body) `[lane]` (ORDER 004 item 5)
2. Apply VERDICT 056 — snapshot stale-indicator T=180s APPROVED, feasible, FLAG-1 badge input (sim-lab `control/outbox.md` L999 @`32ff5c3`) `[verdict]`
3. Ingest-transport spec addendum to `docs/mining-data-contract.md@ae98dd0` — record #2058's env-var names, cadence, ingest-auth decision so both repos share one written seam `[lane]`
4. Build-direct pair: snapshot field parity audit + snapshot contract shared constant (idea-engine `ideas/superbot-mineverse/snapshot-field-parity-audit-2026-07-11.md`, `snapshot-contract-shared-constant-2026-07-11.md` @`2e5d73f`) `[build-direct]`
5. Extend `scripts/readiness_check.py` (+ `docs/live-prod-cutover.md`) with the ingest-route leg once item 1 lands (`scripts/readiness_check.py@ae98dd0`) `[standing]`

**Blocked (do not schedule):** real-endpoint conformance run + audit e2e (owner's six env vars incl. `MINING_WRITE_ENDPOINT`/`MINING_WRITE_SHARED_SECRET`) · superbot #2058/#2061 draft flips (owner).

## websites — swept @ `31b5d00`

Heartbeat ~10h stale at HEAD despite an active evening wave (#291–#304); FENCE
through 2026-07-14 (no live-URL moves, no Railway consolidation).

1. Shepherd #304 (per-step question digest) to green + build its follow-on — declared raw input for the tester-question→rewrite loop (websites PR #304; `docs/ideas/backlog.md:1442@31b5d00`) `[lane]`
2. Truing pass: heartbeat 11:31Z + current-state "nothing in flight" contradicted by #291–#304 and 7 open lifeboats vs 3 documented (`control/status.md:2`, `docs/current-state.md:103@31b5d00`) `[drift]`
3. Cold-browser pass over the review site before EAP close 07-14 (ORDER 022 item 5, `control/inbox.md@31b5d00`) `[standing]` `[deadline]`
4. Read-path check of the two #275 env leads — dashboard's undocumented `SITE_PASSWORD`; possible `ANTHROPIC_API_KEY` on the parallel botsite copy (`docs/current-state.md@31b5d00`, queued "next session") `[lane]`
5. Suite-level token pin in `tests/conftest.py` — autouse sentinel for `GITHUB_TOKEN`/`RAILWAY_TOKEN`, kills the unpinned-reason-assertion flake class (`docs/ideas/backlog.md:33@31b5d00`) `[improve]`
6. Full `asked_at` timestamp on questions-ledger records — unblocks the #302 latency stat for same-day answers (`backlog.md:1421@31b5d00`) `[improve]`
7. Outbox grammar gate on the control fast lane — `quality.yml` short-circuits green on control/**-only diffs (`backlog.md:1192@31b5d00`) `[improve]`
8. One idea-engine build-direct slice: review-queue row auto-check or open-PR awareness at wake (idea-engine `ideas/websites/review-queue-row-auto-check-2026-07-11.md`, `open-pr-awareness-at-wake-2026-07-10.md` @`2e5d73f`) `[build-direct]`

**Blocked (do not schedule):** ORDER 020 writeback (owner contents:write PAT paste) · ORDER 021 environments hub (owner Discord-auth decision/Q-0004) · lifeboat disposal #245/#249/#257/#278/#279/#280/#300 (owner-click) · photo-pack originals (owner).

## substrate-kit — swept @ `736e114`

Inbox fully consumed (001–018 done); status says backlog "gated-dry" but ~25
captured ideas + 3 evidence-carrying ASKs are buildable.

1. Session-gate false-green fix — card selection mtime → merge-base-diff (idea-engine ASK 003, false-green REPRODUCED live in the sim-lab V051 session, `control/outbox.md@2808b16`) + the flip-race fail-open fix (`docs/ideas/session-gate-flip-race-fail-open-2026-07-13.md@736e114`) `[improve]` (highest-evidence kit fix)
2. ASK 001: add `claude/` to the auto-merge-enabler template allowlist — one-line, jammed green PR evidenced (#271) (idea-engine `control/outbox.md` ASK 001 @`2808b16`) `[improve]` (quick win)
3. ASK 002: converge local `check --strict` with the CI substrate-gate legs — 2 reproduced local-green→CI-red PRs (#274, #299) (idea-engine `control/outbox.md` ASK 002 @`2808b16`) `[improve]`
4. Auto-merge-enabler install-time preflight — check-time half shipped (#321); install-time half still captured (`docs/ideas/enabler-install-preflight-2026-07-13.md@736e114`) `[lane]`
5. Pre-stage the fm ORDER 025 port — differential-testing doctrine + release-writeup convention, via read-only fleet grounding; zero kit-side references exist at `736e114` (fm `control/inbox.md` ORDER 025 @`c5dc151`) `[standing]` `[relay]`
6. Staged-artifact regen-lag checker (`docs/ideas/staged-artifact-regen-lag-checker-2026-07-12.md@736e114`) `[improve]`
7. `bootstrap heartbeat` mechanical status writer — also the mechanical fix for the fleet-wide heartbeat-staleness class (`docs/ideas/heartbeat-verb-2026-07-09.md@736e114`) `[improve]`

**Blocked (do not schedule):** release wave (owner's #317 ratification click; #317 is `do-not-automerge`, never arm/close/rebase) · `adopters.md` regen (waits on resident `kit:` lines per outbox ask) · grounded-skills measurement (window opens ~07-19).

## trading-strategy — swept @ `499876f`

All 13 ORDERs consumed; 0 open PRs. Status says "round 6 awaiting direction" but
ORDER 012 item 4 is standing owner direction to keep expanding the surface —
round 6 is self-startable under the new selection-fair gate.

1. Write + commit a pre-registered Round-6 plan — new idea classes / tickers / indicators under the selection-fair gate (ORDER 012 item 4 verbatim, `control/inbox.md@499876f`; gate PR #111 `d498018`) `[standing]`
2. Run Round-6 slices once the plan is committed (plan-before-outcome per `docs/founding-plan.md@499876f`) `[standing]`
3. Fold the R5-D convention (fixed-config row in any searched-arm comparison) into the Round-6 plan (`docs/research-round-5-results.md` tail @`499876f`) `[lane]`
4. Pre-verify the 2026-07-17 grading pass — confirm the LIVE executor and flag the FOREIGN duplicate-fire risk `trig_01YXNmgqYeYQ1LuepsLmbNCG` (venture-lab `control/status.md@be6c75d`) `[lane]` (coordination hygiene)
5. Dry-run `scripts/grade_paper.py` against the FLAT paper ledger to de-risk Friday's first firing (`docs/paper-lane-protocol.md` §6–§7 @`499876f`) `[improve]`

**Blocked (do not schedule):** R5-C BTC-Bollinger OOS (owner-gated; execution impossible before ~2026-09-09) · MTF-Bollinger prereg (FROZEN, dev result NULL) · wake-resilience rebind (owner click).

## venture-lab — swept @ `be6c75d`

All 10 ORDERs consumed (ORDER 010 pricing verdicts applied, #163); 0 open PRs;
`docs/ideas/` empty by design — the generative rung IS the backlog.

1. Next product to publish-READY — packet + build cc-cost-lens, or run a fresh ideation batch (the #142 batch's 3 BUILDs are consumed) (ORDER 008 item 2, `control/inbox.md@be6c75d`; `docs/current-state.md` names cc-cost-lens) `[standing]`
2. New book titles + edition variants — EN adult catalog (11 manuscripts) still has unexecuted variants; versions are cheap per ORDER 008 item 1 (`docs/NEXT-SESSION.md@be6c75d`) `[standing]`
3. Night Kiln Book 3 at the packet's committed band, flag the length-band question (Book 2 complete 15,995w, #145; `docs/current-state.md` line 133 @`be6c75d`) `[standing]` (decide-and-flag)
4. Apply the newly-served sim verdicts on relay: V053 channel-concentration diversify (approve), V057 keyword-map first-claim-wins (approve), V049 KU-exclusivity fork (REJECT) (sim-lab `control/outbox.md` L859/L939/L1019 @`32ff5c3`; fm routing pending) `[verdict]`
5. V020-null follow-through — two-version live probe measuring audience separation s, one night-slice budget (VERDICT 020, idea-engine `control/outbox.md@2808b16`) `[verdict]`
6. WEBSITE-IDEA sweep — mark site-shaped outbox concepts for manager routing; none marked in the current window (ORDER 008 item 3 @`be6c75d`) `[standing]`
7. Queue hygiene: any new packet requires the `derive_owner_queue.py` regen + counts-sync same session (the #166 remedy class) `[lane]`

**Blocked (do not schedule):** all 177 owner publish clicks · photo-pack originals handoff · Ship-It bundle (⚑B/⚑D) · Night Kiln 2 length-band ruling · makerbench build explicitly forbidden (idea-engine ORDER 004 rule 4 @`2808b16`).

## idea-engine — swept @ `2808b16`

Zero unconsumed ORDERs; ORDER 003 (continuous pipeline) standing-active.

1. V054/V055 closure + prune 2 stale claims (`control/status.md` NEXT-2 baton @`2808b16`; claims `claude-proposal-047-creature-rarity-counter.md`, `claude-ideas-link-backfill-p037-p038.md`) `[lane]`
2. Round-8 close + round-9 open — draft PROPOSAL 048; pipeline never dry (ORDER 003 standing; seed high-water 20261328 per the P047 claim) `[standing]`
3. Heartbeat re-stamp — status 20:06Z lags HEAD by 3 landed proposals; LOOP STATE says "round 8 opens at P045" which already happened (`control/status.md@2808b16`) `[drift]`
4. Track in-flight V056/V057 into the verdict-ledger echo (P047 claim @`2808b16`) `[lane]`
5. ASK 004 follow-through — execute the outbox archival split same-session once fm answers (outbox ~395KB, +~30KB/day; `control/outbox.md@2808b16`) `[relay]`
6. `docs/current-state.md` hygiene — Stability/In-flight/Recently-shipped are empty stubs while real state lives in the heartbeat; populate or explicitly delegate (`docs/current-state.md@2808b16`) `[drift]`

## sim-lab — swept @ `32ff5c3`

Healthy and nearly drained: 57 verdicts finalized, 0 open PRs, all ORDERs done.

1. PROPOSAL 047 → VERDICT 058 — creature-rarity vs skill-counter battle sweep, the only sim-ready unverdicted proposal (idea-engine `control/outbox.md` L401 @`66a05b1`, sim-ready 21:28Z, seeds 20261325–328) `[standing]`
2. Heartbeat/ledger refresh through V057 + fleet-seed high-water 20261328 (`control/status.md` 20:08:41Z @`32ff5c3`) `[drift]`
3. `docs/current-state.md` drift — says "verdicts through 045 / V046 pending", stale by 11 verdicts (V046 landed #96) `[drift]` (fix-on-sight class)
4. Kit upgrade v1.7.0 → v1.15.0 — standing watch from the session-2 close; no upgrade PR open at sweep (`control/status.md` kit line @`32ff5c3`) `[improve]`
5. Own outbox rollover prep — 1028 lines and heading for the same 256KB wall as idea-engine ASK 004; adopt whatever convention fm answers (`control/outbox.md@32ff5c3`) `[improve]`

**Blocked (do not schedule):** OA-002 Codex quota · OA-003 review-site deploy · OA-004 harness tag-push 403 (all owner actions, `control/status.md` ⚑ @`32ff5c3`).

## fleet-manager (self) — session branch @ `59ffe56` (PR #178)

1. Route sim-lab verdicts V055–V057 (owner-readers / superbot-mineverse / venture-lab) + verify V046–V054 routing actually happened at the :30 sweeps — sim-lab keeps no routed/consumed marker; routing is fm-side per Q-0260 (sim-lab `control/outbox.md` L979–L1019 @`32ff5c3`) `[relay]`
2. Relay fm ORDER 025 to substrate-kit's inbox — it never arrived: kit inbox tops out at ORDER 018, zero "differential" hits in `docs/`+`control/` at `736e114` (fm `control/inbox.md` ORDER 025 @`c5dc151`) `[relay]`
3. Land ORDER 031-shaped work (SuperBot World mining/fishing/idle + casino inventory/spec) in the right seat inbox — neither superbot-next nor superbot-idle carries any ORDER 030/031 text (sweep negative finding @`5dac6ce`/`1f4d774`; fm ORDER 031 @`c5dc151`) `[relay]`
4. Answer idea-engine ASKs 001–004 — esp. ASK 004 outbox rollover convention (outbox ~395KB, past the 256KB single-read limit); fold ASKs 001–003 into the substrate-kit relay (idea-engine `control/outbox.md@2808b16`) `[relay]`
5. Phase 3: fan out these worklists as per-seat lane dispatches (ORDER 045, `control/inbox.md@59ffe56`) `[standing]`
6. Owner-queue note: websites lifeboat pileup (4 new `.substrate/state.json`-churn rescue drafts today: #278/#279/#280/#300) + ~10h-stale heartbeat misread risk (websites @`31b5d00`) `[drift]`
7. Issue fleet Q-numbers for superbot-idle's two waiting owner Q-blocks (timed-events content depth; generator-purchase economy) (superbot-idle `control/status.md@1f4d774`) `[relay]`

---

## DARK dispositions (owner-queue — no ORDERs planned)

- **superbot-games** — DARK ~35h14m despite served balance verdicts (its ORDER 006 done: mining V042, fishing curve, DnD escort ruling, exploration bands) and standing fm ORDERs 030/031/037. Owner call: re-wake the seat or reassign its build orders (roster gen #35; idea-engine `control/inbox.md` ORDER 006 @`2808b16`).
- **gba-homebrew** — DARK ~29h10m with approved verdicts V050 (Gloamline survival ceiling) + V054 (Brineward band-2) and build-direct plans armed. Owner call: re-wake (sim-lab `control/outbox.md` L879/L959 @`32ff5c3`).
- **product-forge** — DARK ~2.1d; fm ORDERs 023/024 (games-web → websites arcade; retro → fm docs) are GATED on owner consolidation approval E#44. No action until the owner answers.
- **substrate-kit sub-rows gba-trackb (~3.7d) + superbot-coordinator (~3.3d)** — presumed wound down; owner confirm so the roster rows can be retired (roster gen #35).
- **codetool-lab ×3** (all three seat rows) — STALE-BY-DESIGN ~4.1d, wound down. No action.
- **pokemon-mod-lab** — UNREADABLE (private repo + terminal-prompts-disabled wall). Owner call on access or wind-down (roster gen #35).

## Cross-cutting findings

1. **ORDER-relay gaps** — ORDER 025 never reached substrate-kit's inbox; ORDER 031 landed in no seat inbox at all. The manager's relay step needs a delivery-verification pass (self items 2–3).
2. **sim-lab routing lag** — 12 verdicts finalized today with no routed/consumed marker anywhere (routing is fm-side by design, Q-0260); V055–V057 certainly postdate the last sweep (self item 1).
3. **Websites heartbeat staleness** — `control/status.md` ~10h stale at HEAD against a 13-merge evening wave + open READY #304; fleet freshness sweeps misread this seat. The kit `bootstrap heartbeat` idea is the mechanical fix class.
4. **superbot-next WP stack conflict** — #312→#371 now verifiably conflicts with main (4 files) and migration 0052 invalidated the WP-2/3 goldens; the owner's ordered click-sweep is currently not one-click until the reconcile lands.
5. **EAP email-3 deadline** — SENDS 2026-07-14; still needs Part-1 voice + roster screenshot; the send is owner-gated and the window closes tomorrow (superbot `docs/eap/anthropic-email-3-draft-2026-07-13.md@f969b95`).
