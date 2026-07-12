# Owner-queue candidate feed — GENERATED

> **Status:** `living-ledger`
>
> **GENERATED — NOT SOURCE OF TRUTH; the manager curates `docs/owner-queue.md` from it.** Do not hand-edit; regenerated with the roster on every regen (`scripts/gen_roster.py`, P2 — centralization plan §3b).
>
> **Generation #21** · generated-at **2026-07-12T21:27Z** · by roster-regen workflow (GitHub Actions, headless), dispatched by cron 40 */2 * * * (.github/workflows/roster-regen.yml, fleet-manager PR #81)
>
> Every block below is a VERBATIM `⚑ needs-owner` / `OWNER-ACTION` extraction from a lane heartbeat (`control/status*.md` at the ls-remote-verified HEAD the roster row cites). Nothing here lands in the owner queue automatically: the manager dedups, verifies (R17), and curates. `suggested-id` is a deterministic content-derived slug the manager may adopt; `possibly-covered-by` lists active queue ids citing the same PR — `none matched` means manual dedup is still needed.

### superbot (hub) — ⚑ needs-owner: none new hub-specific (verified against fm docs/owner-queue.md @ 7ff1f75 — the hub's owner tai…

- suggested-id: `OQ-SUPERBOT-NONE-NEW-HUB-SPECIFIC`
- source: superbot/control/status.md @ `97d281e` · heartbeat `updated:` 2026-07-11T19:45:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: none new hub-specific (verified against fm docs/owner-queue.md @ 7ff1f75 — the hub's owner tail is already queued there). Manager-sweep note, NOT an owner click: fm owner-queue C#20's manager note (superbot codex-final-review invalid YAML) is RESOLVED by superbot PR #1995 (8214200) — retire that line at the next sweep.
```

### superbot-next — ⚑ needs-owner (paste-ready):

- suggested-id: `OQ-SUPERBOT-NEXT-PASTE-READY`
- source: superbot-next/control/status.md @ `8cdb7c3` · heartbeat `updated:` 2026-07-12T20:20Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner (paste-ready):
1. D‑0043 deep-game ports go/no-go — 25 mining + 15 fishing goldens; the only path to a fully-green report job (games-project overlap noted; NB the open mining slice stack #286→#300 covers the mining-deep surface).
2. sweep_paragon disposition — port or retire (open #280 re-homes the !paragon calculator surface onto the ported btd6 row).
3. Settings-prune corpus ratification for `btd6_strategy_submission_channel` + `skip_roles` (docs/review/admin-surface-audit-2026-07-12.md §8 — both shipped-dead parity artifacts, KEEP-ledgered pending ratification).
```

### superbot-next — 4. OWNER-ACTION 3 — ruleset/merge-queue (six-field record in the pre-close status at `694e056`).

- suggested-id: `OQ-SUPERBOT-NEXT-4-3-RULESET-MERGE`
- source: superbot-next/control/status.md @ `8cdb7c3` · heartbeat `updated:` 2026-07-12T20:20Z
- possibly-covered-by: none matched (manual dedup needed)

```text
4. OWNER-ACTION 3 — ruleset/merge-queue (six-field record in the pre-close status at `694e056`).
```

### superbot-next — 5. OWNER-ACTION 5 — ANTHROPIC_API_KEY + AI_ENABLED (six-field record in the pre-close status at `694e056`).

- suggested-id: `OQ-SUPERBOT-NEXT-5-5-ANTHROPIC-API`
- source: superbot-next/control/status.md @ `8cdb7c3` · heartbeat `updated:` 2026-07-12T20:20Z
- possibly-covered-by: none matched (manual dedup needed)

```text
5. OWNER-ACTION 5 — ANTHROPIC_API_KEY + AI_ENABLED (six-field record in the pre-close status at `694e056`).
6. Seat failsafes — the Builder seat's own failsafe cron is dead (`auto_disabled_env_deleted`); a successor boot needs an owner/fleet wake or a re-armed failsafe.
```

### substrate-kit — ⚑ FOR OWNER (paste-ready, carried from the standing set — full field blocks verbatim in git history of this f…

- suggested-id: `OQ-SUBSTRATE-KIT-PASTE-READY-CARRIED-FROM`
- source: substrate-kit/control/status.md @ `174b113` · heartbeat `updated:` 2026-07-12T21:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ FOR OWNER (paste-ready, carried from the standing set — full field blocks verbatim in git history of this file @ 86d2a57, ⚑ OWNER-ACTION 2/6 + ⚑ FOR MANAGER):
- **P10 required-check swap (⚑ 2):** Settings → Rules → `main` ruleset → required status checks: remove "Kit test suite" + "Cold-adoption smoke (adopt + check --strict)"; add `kit-quality`; set "Require branches to be up to date" OFF. Reversible; ends the ~35-min queue-stall class. (No agent path to rulesets — verified 403/no-endpoint.)
- **fm #122 v3.4 restamp:** the owner reviews and merges fleet-manager PR #122 PERSONALLY — do NOT agent-merge.
- **UNIVERSAL wake fetch-list vN bump + re-paste:** add `docs/seat-digest.md` (+ `docs/SKILLS.md`) to the manager-authored wake fetch list, bump vN, owner re-pastes via fm's edit-registry-first flow.
```

### substrate-kit — - **⚑ 6 public-flip-or-PAT (pick one):** make this repo public (⚠️ effectively irreversible) OR mint a fine-g…

- suggested-id: `OQ-SUBSTRATE-KIT-6-PUBLIC-FLIP-PAT`
- source: substrate-kit/control/status.md @ `174b113` · heartbeat `updated:` 2026-07-12T21:05:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ 6 public-flip-or-PAT (pick one):** make this repo public (⚠️ effectively irreversible) OR mint a fine-grained read-only PAT into the fleet environments (reversible) — unblocks the B2–B4 cross-repo sweeps.
- **Grounded-skills measurement window:** proposal to run the before/after measurement pass ~2026-07-19..26 per docs/reports/2026-07-12-grounded-skills-wrap.md §3d — say nothing to accept the window; a successor fires it when it matures.
```

### ↳ substrate-kit — `control/status-superbot-coordinator.md` — ⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLI…

- suggested-id: `OQ-SUBSTRATE-KIT-1-VERIFY-DELIVER-TESTING`
- source: substrate-kit/control/status-superbot-coordinator.md @ `174b113` · heartbeat `updated:` 2026-07-10T13:47:02Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLIPPED at 2026-07-10T13:45Z (band-5 "NEXT LANE: LIVE-DRIVE", 01:05Z heartbeat), so that lane's seven wind-down deliverables are still owed [unblocks: superbot-next lane archive]; 2) kernel-surface-drift ruling (flag 13 in superbot-next docs/status/testing-report-2026-07-09.md: "relax-compare" or "re-baseline") [unblocks: ALL parity flips]; 3) create repo superbot-plugin-hello (github.com/new, owner menno420, Public, no README) [unblocks: ORDER 002 done]; 4) paste the setup script from docs/environment-setup-script.md into the project Environment settings (re-verified exit-0 at wind-down) [unblocks: no more provisioning deaths]; 5) nod for wiring superbot's new collision/freshness checkers (#1918/#1923) into code-quality.yml — one small PR, owner said workflow edits need a nod [unblocks: checkers enforce in CI]; 6) stale trading-lab/venture-lab manifest rows (manager-owned file) + Q-0248 taxonomy lacks a "tooling" class [unblocks: honest telemetry]
```

### websites — ⚑ needs-owner: pointer — canonical six-field blocks live in docs/owner/OWNER-ACTIONS.md ONLY (do not duplicat…

- suggested-id: `OQ-WEBSITES-POINTER-CANONICAL-SIX-FIELD`
- source: websites/control/status.md @ `8998c0b` · heartbeat `updated:` 2026-07-12T21:22:10Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: pointer — canonical six-field blocks live in docs/owner/OWNER-ACTIONS.md ONLY (do not duplicate them here). The Actions "allow create PRs" toggle ask was verified SATISFIED 2026-07-12; its strike from OWNER-ACTIONS rides PR #210. Other asks there unchanged at this write: botsite SITE_PASSWORD; botsite Postgres/DATABASE_URL; PayPal Payouts creds; the fine-grained GitHub contents:write PAT (ORDER 020 owner writeback commits); Discord OAuth redirect-URI + client secret for the environments-hub gate — DECISION PENDING, seam in place.
```

### superbot-games · Seat A — ⚑ needs-owner: ORDER 004 (self-review) — SATISFIED on main: artifact at docs/retro/close-out-world-games-2026…

- suggested-id: `OQ-SUPERBOT-GAMES-ORDER-004-SELF-REVIEW`
- source: superbot-games/control/status.md @ `fbf5202` · heartbeat `updated:` 2026-07-12T10:16:22Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: ORDER 004 (self-review) — SATISFIED on main: artifact at docs/retro/close-out-world-games-2026-07-11.md (authored 201f8dd/#47, relocated at close-out 3a4eb98/#57); done=004 is backed by real, spec-compliant content, not a bare marker. Remaining owner items: the OWNER-ACTION block below + docs/retro/archive-ready-2026-07-11.md. ⚑ mining WORKFLOW seam (rung 2) — audit-schema decision (D1 which schema / D2 audit item-grants, a divergence from the oracle) needs owner/lab ratification; scoped in docs/design/mining-workflow-seam.md, PR #60.
```

### ↳ superbot-games · Seat A — `control/status-exploration.md` — ⚑ needs-owner: \|

- suggested-id: `OQ-SUPERBOT-GAMES-FLAG`
- source: superbot-games/control/status-exploration.md @ `fbf5202` · heartbeat `updated:` 2026-07-09T20:09Z
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

### superbot-idle (Seat B) — - ⚑ to manager: no longer a blocker-ask. Optional follow-up only — owner may create the standalone superbot-p…

- suggested-id: `OQ-SUPERBOT-IDLE-MANAGER-NO-LONGER-BLOCKER`
- source: superbot-idle/control/status.md @ `c753bc8` · heartbeat `updated:` 2026-07-12T10:17Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- ⚑ to manager: no longer a blocker-ask. Optional follow-up only — owner may create the standalone superbot-plugin-hello repo (still empty); exemplar is in-tree meanwhile.
```

### superbot-mineverse — ⚑ needs-owner: provision the six host env secrets (block below) — the SECURITY BEFORE SECRETS gate is CLEAR (…

- suggested-id: `OQ-SUPERBOT-MINEVERSE-PROVISION-SIX-HOST-ENV`
- source: superbot-mineverse/control/status.md @ `286d752` · heartbeat `updated:` 2026-07-12T21:03:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: provision the six host env secrets (block below) — the SECURITY BEFORE SECRETS gate is CLEAR (#42 in main).
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
- source: idea-engine/control/status.md @ `c77563c` · heartbeat `updated:` 2026-07-12T19:48:04Z (real wall-clock via date -u, per the …
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

15 candidate block(s) across 12 lane(s). Feed is additive-noise-tolerant by design: over-capture is curated out by the manager; silent stranding is the failure this feed exists to kill.

