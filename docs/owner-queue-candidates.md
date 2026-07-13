# Owner-queue candidate feed — GENERATED

> **Status:** `living-ledger`
>
> **GENERATED — NOT SOURCE OF TRUTH; the manager curates `docs/owner-queue.md` from it.** Do not hand-edit; regenerated with the roster on every regen (`scripts/gen_roster.py`, P2 — centralization plan §3b).
>
> **Generation #23** · generated-at **2026-07-13T04:10Z** · by roster-regen workflow (GitHub Actions, headless), dispatched by cron 40 */2 * * * (.github/workflows/roster-regen.yml, fleet-manager PR #81)
>
> Every block below is a VERBATIM `⚑ needs-owner` / `OWNER-ACTION` extraction from a lane heartbeat (`control/status*.md` at the ls-remote-verified HEAD the roster row cites). Nothing here lands in the owner queue automatically: the manager dedups, verifies (R17), and curates. `suggested-id` is a deterministic content-derived slug the manager may adopt; `possibly-covered-by` lists active queue ids citing the same PR — `none matched` means manual dedup is still needed.

### superbot (hub) — ⚑ needs-owner: none new hub-specific (verified against fm docs/owner-queue.md @ 7ff1f75 — the hub's owner tai…

- suggested-id: `OQ-SUPERBOT-NONE-NEW-HUB-SPECIFIC`
- source: superbot/control/status.md @ `5262fe4` · heartbeat `updated:` 2026-07-11T19:45:00Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: none new hub-specific (verified against fm docs/owner-queue.md @ 7ff1f75 — the hub's owner tail is already queued there). Manager-sweep note, NOT an owner click: fm owner-queue C#20's manager note (superbot codex-final-review invalid YAML) is RESOLVED by superbot PR #1995 (8214200) — retire that line at the next sweep.
```

### superbot-next — ⚑ needs-owner (morning queue):

- suggested-id: `OQ-SUPERBOT-NEXT-MORNING-QUEUE`
- source: superbot-next/control/status.md @ `a4d51b6` · heartbeat `updated:` 2026-07-13T02:47Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner (morning queue):
1. superbot mineverse PRs are held as DRAFTS by the merge=deploy guard (Q-0193) — owner flips ready to land+deploy: #2058 (FLAG 1 snapshot read-relay; checks green as reported) and #2061 (FLAG 2 HMAC write endpoint; still iterating, last push 02:41Z).
2. CodeQL raised 6 new alerts (1 high) on superbot#2061 — child session fixing; owner review before deploy (as reported in coordinator chat).
3. Settings-prune corpus ratification (docs/review/admin-surface-audit-2026-07-12.md §8).
```

### superbot-next — 4. OWNER-ACTION 3 — ruleset/merge-queue; OWNER-ACTION 5 — ANTHROPIC_API_KEY + AI_ENABLED (six-field records i…

- suggested-id: `OQ-SUPERBOT-NEXT-4-3-RULESET-MERGE`
- source: superbot-next/control/status.md @ `a4d51b6` · heartbeat `updated:` 2026-07-13T02:47Z
- possibly-covered-by: none matched (manual dedup needed)

```text
4. OWNER-ACTION 3 — ruleset/merge-queue; OWNER-ACTION 5 — ANTHROPIC_API_KEY + AI_ENABLED (six-field records in pre-close status at `694e056`).
5. One-click: delete branches `scratch/union-test-a` + `scratch/union-test-b` (agent branch-deletion returns 403).
```

### substrate-kit — ⚑ FOR OWNER (paste-ready, carried from the standing set — full field blocks verbatim in git history of this f…

- suggested-id: `OQ-SUBSTRATE-KIT-PASTE-READY-CARRIED-FROM`
- source: substrate-kit/control/status.md @ `917261b` · heartbeat `updated:` 2026-07-13T02:11:22Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ FOR OWNER (paste-ready, carried from the standing set — full field blocks verbatim in git history of this file @ 86d2a57, ⚑ OWNER-ACTION 2/6 + ⚑ FOR MANAGER):
- **P10 required-check swap (⚑ 2):** Settings → Rules → `main` ruleset → required status checks: remove "Kit test suite" + "Cold-adoption smoke (adopt + check --strict)"; add `kit-quality`; set "Require branches to be up to date" OFF. Reversible; ends the ~35-min queue-stall class. (No agent path to rulesets — verified 403/no-endpoint.)
- **fm #122 v3.4 restamp:** the owner reviews and merges fleet-manager PR #122 PERSONALLY — do NOT agent-merge.
- **UNIVERSAL wake fetch-list vN bump + re-paste:** add `docs/seat-digest.md` (+ `docs/SKILLS.md`) to the manager-authored wake fetch list, bump vN, owner re-pastes via fm's edit-registry-first flow.
```

### substrate-kit — - **⚑ 6 public-flip-or-PAT (pick one):** make this repo public (⚠️ effectively irreversible) OR mint a fine-g…

- suggested-id: `OQ-SUBSTRATE-KIT-6-PUBLIC-FLIP-PAT`
- source: substrate-kit/control/status.md @ `917261b` · heartbeat `updated:` 2026-07-13T02:11:22Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- **⚑ 6 public-flip-or-PAT (pick one):** make this repo public (⚠️ effectively irreversible) OR mint a fine-grained read-only PAT into the fleet environments (reversible) — unblocks the B2–B4 cross-repo sweeps.
- **Grounded-skills measurement window:** proposal to run the before/after measurement pass ~2026-07-19..26 per docs/reports/2026-07-12-grounded-skills-wrap.md §3d — say nothing to accept the window; a successor fires it when it matures.
```

### ↳ substrate-kit — `control/status-superbot-coordinator.md` — ⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLI…

- suggested-id: `OQ-SUBSTRATE-KIT-1-VERIFY-DELIVER-TESTING`
- source: substrate-kit/control/status-superbot-coordinator.md @ `917261b` · heartbeat `updated:` 2026-07-10T13:47:02Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: 1) verify/deliver the testing-lane wind-down — superbot-next control/status.md was still UNFLIPPED at 2026-07-10T13:45Z (band-5 "NEXT LANE: LIVE-DRIVE", 01:05Z heartbeat), so that lane's seven wind-down deliverables are still owed [unblocks: superbot-next lane archive]; 2) kernel-surface-drift ruling (flag 13 in superbot-next docs/status/testing-report-2026-07-09.md: "relax-compare" or "re-baseline") [unblocks: ALL parity flips]; 3) create repo superbot-plugin-hello (github.com/new, owner menno420, Public, no README) [unblocks: ORDER 002 done]; 4) paste the setup script from docs/environment-setup-script.md into the project Environment settings (re-verified exit-0 at wind-down) [unblocks: no more provisioning deaths]; 5) nod for wiring superbot's new collision/freshness checkers (#1918/#1923) into code-quality.yml — one small PR, owner said workflow edits need a nod [unblocks: checkers enforce in CI]; 6) stale trading-lab/venture-lab manifest rows (manager-owned file) + Q-0248 taxonomy lacks a "tooling" class [unblocks: honest telemetry]
```

### websites — ⚑ needs-owner: pointer — canonical six-field blocks live in docs/owner/OWNER-ACTIONS.md ONLY (do not duplicat…

- suggested-id: `OQ-WEBSITES-POINTER-CANONICAL-SIX-FIELD`
- source: websites/control/status.md @ `1a411d1` · heartbeat `updated:` 2026-07-13T02:51:21Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: pointer — canonical six-field blocks live in docs/owner/OWNER-ACTIONS.md ONLY (do not duplicate them here). Seven asks open there at this write: botsite SITE_PASSWORD; botsite Postgres/DATABASE_URL; PayPal Payouts creds; Q-0004; Discord OAuth redirect-URI + client secret (environments-hub gate — DECISION PENDING, seam in place); the armed-service ask; the fine-grained GitHub contents:write PAT (ORDER 020 owner writeback commits). The Actions "allow create PRs" toggle is Decided (row M struck via PR #210).
```

### superbot-games · Seat A — ⚑ needs-owner: ORDER 004 (self-review) — SATISFIED on main: artifact at docs/retro/close-out-world-games-2026…

- suggested-id: `OQ-SUPERBOT-GAMES-ORDER-004-SELF-REVIEW`
- source: superbot-games/control/status.md @ `5aec110` · heartbeat `updated:` 2026-07-12T10:16:22Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: ORDER 004 (self-review) — SATISFIED on main: artifact at docs/retro/close-out-world-games-2026-07-11.md (authored 201f8dd/#47, relocated at close-out 3a4eb98/#57); done=004 is backed by real, spec-compliant content, not a bare marker. Remaining owner items: the OWNER-ACTION block below + docs/retro/archive-ready-2026-07-11.md. ⚑ mining WORKFLOW seam (rung 2) — audit-schema decision (D1 which schema / D2 audit item-grants, a divergence from the oracle) needs owner/lab ratification; scoped in docs/design/mining-workflow-seam.md, PR #60.
```

### ↳ superbot-games · Seat A — `control/status-exploration.md` — ⚑ needs-owner: \|

- suggested-id: `OQ-SUPERBOT-GAMES-FLAG`
- source: superbot-games/control/status-exploration.md @ `5aec110` · heartbeat `updated:` 2026-07-09T20:09Z
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
- source: superbot-idle/control/status.md @ `c735075` · heartbeat `updated:` 2026-07-12T10:17Z
- possibly-covered-by: none matched (manual dedup needed)

```text
- ⚑ to manager: no longer a blocker-ask. Optional follow-up only — owner may create the standalone superbot-plugin-hello repo (still empty); exemplar is in-tree meanwhile.
```

### superbot-mineverse — ⚑ needs-owner: provision the six host env secrets (block below) — the SECURITY BEFORE SECRETS gate is CLEAR (…

- suggested-id: `OQ-SUPERBOT-MINEVERSE-PROVISION-SIX-HOST-ENV`
- source: superbot-mineverse/control/status.md @ `79a4018` · heartbeat `updated:` 2026-07-12T23:41:43Z
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

### idea-engine — ⚑ needs-owner (condensed from the session-1 close-out — canonical full-field detail stands in history at c775…

- suggested-id: `OQ-IDEA-ENGINE-CONDENSED-FROM-SESSION-1`
- source: idea-engine/control/status.md @ `15d1802` · heartbeat `updated:` 2026-07-12T23:44:55Z (real wall-clock via date -u, per the …
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner (condensed from the session-1 close-out — canonical full-field detail stands in history at c77563c control/status.md ⚑ block; the stale Q-0265 "must re-arm both / being dismantled" paragraph is DROPPED as superseded — routine state now lives ONLY in the phase line's routine-disposition block): (1) THE ≤2026-07-13 OWNER SITTING BUNDLE (EAP window wraps 2026-07-14). WHAT: FOUR decisions in ONE sitting — (a) Lumen Drift itch.io go/no-go (dist/lumen-drift.gba v1.3, sha256 195a867…, parked idea ideas/venture-lab/games-adjacent-candidate-three-2026-07-10.md; on go: itch.io account → New project → PWYW → upload → publish); (b) pokemon playtest verdicts (fm docs/owner-queue.md item 3 @ 1afca50); (c) the gba concept pick (lane ⚑ @ c7592d6 — Lumen-deepening / Clockwork Courier / Shoal; seeded-cave-runs = the costed 'more Lumen' option); (d) post-EAP standing-routine posture. WHERE: reply in any owner channel the manager sweep reads; (a) executes on itch.io, (b)-(d) execute manager/lane-side. HOW (paste ONE line for (d), recommendation first): RECOMMENDED "Post-EAP routines Option A: core-6 Projects keep current cadence (per Q-0261), every other standing cron drops to daily, one-shots expire on completion; revisit at first paid invoice." (Alternatives B keep-all / C freeze-all / D name-a-budget — full text at c77563c). WHY-IT-MATTERS: window closes 2026-07-14; without (d), Option B happens by inertia at unmetered paid burn. UNBLOCKS: candidate #3 publish pipeline, playtest routing, gba lane's next build, the manager's pre-close cadence sweep. VERIFIED-NEEDED: owner-only by rule and evidence — publishing/account creation rail-banned for agents (venture-lab @ 0ad0ea4, gba-homebrew @ 31c8672); no post-EAP budget ruling exists anywhere (greps at #174); spend surfaces owner-UI-only. (2) WEBSITES CUTOVER choice. WHAT: one structured reply deciding the websites cutover role (retire superbot's dashboard/ + botsite/, bot-control home, domains optional). WHERE: any owner channel; the lane executes from menno420/websites docs/owner/OWNER-ACTIONS.md rows 1/4/6 @ 92c3dc6. HOW (paste ONE line, recommendation first): RECOMMENDED "Cutover Option A: go — retire superbot's dashboard/ + botsite/ services; the new sites keep reading old-repo data until the bot cutover; bot control home = superbot-next (ruled now, wired later); domains stay deferred." (Alternatives B/C/D — full text at c77563c). WHY-IT-MATTERS: dual maintenance on old+new sites while unmade; the de-facto answer bakes in. UNBLOCKS: websites rework-plan steps 3/5, Q4 control-panel wiring, domain assignment, superbot #155 shortlist item 2. VERIFIED-NEEDED: owner-gated by rule — the lane's surface marks retirement "Gated: needs your go" (row 6) and control home "Do not port without an owner call" (row 1); DNS/service retirement are owner-only Railway/DNS mutations (D‑0005 class). (3) GIFT REPO. WHAT: one reply decides repo name (rec: makerbench), visibility (rec: private + friend as collaborator), project cut (rec: all five a-e); optional add-on: buy a PCA9685 16-ch servo driver (~€10 — the arm kit has no controller, project (c) assumes one). WHERE+HOW: full paste-ready line in ideas/venture-lab/maker-gift-repo-blueprint-2026-07-12.md. WHY-IT-MATTERS: the gift blocks on the naming/visibility call, not on build capacity. UNBLOCKS: slice-1 routing (build slices 1-5 per the blueprint). VERIFIED-NEEDED: repo creation under the owner's account + purchase are owner-only by rule.
```

### codetool-lab-opus4.8 — ⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTI…

- suggested-id: `OQ-CODETOOL-LAB-OPUS4-8-1-DELETE-LEFTOVER-BRANCH`
- source: codetool-lab-opus4.8/control/status.md @ `80f6cd1` · heartbeat `updated:` 2026-07-09T20:11:35Z
- possibly-covered-by: none matched (manual dedup needed)

```text
⚑ needs-owner: (1) delete leftover branch claude/status-heartbeat-001 (sessions 403 on ref deletes); (2) OPTIONAL PyPI publish of mdverify (needs owner token; name free as of 2026-07-09); (3) OPTIONAL Claude GitHub App connect for native tag/release
```

---

14 candidate block(s) across 12 lane(s). Feed is additive-noise-tolerant by design: over-capture is curated out by the manager; silent stranding is the failure this feed exists to kill.

