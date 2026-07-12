# Repo consolidation census — phase A (2026-07-12)

> **Status:** `reference`
>
> Full-fleet census for the owner-directed repo consolidation program:
> identity / activity / assets / cost / verdict per repo. Snapshot of
> 2026-07-12 — verify claims against live GitHub before acting on them.

## Purpose

Phase A evidence base for the repo consolidation plan. Five parallel census
workers surveyed the full fleet — **19 repos**, and `list_repos` returned an
**exact match against the expected 19-name set** (no extras, none missing;
all `can_push=true`, `pushed_at` range 2026-07-09T20:09Z → 2026-07-12T15:31Z).
Every repo got the same five-lens treatment (identity / activity / unique
assets / cost of keeping / verdict), with citations to SHAs, PR numbers, and
files-at-SHA preserved from the raw worker reports. Verdict vocabulary:
**KEEP** (active seat-core), **KEEP-QUIET** (dormant-by-design, zero idle
cost, do not archive), **MIGRATE-THEN-ARCHIVE** (rehome named assets first,
then archive), **ARCHIVE-NOW** (none earned it).

## Verdict table (all 19 repos)

| Repo | Seat | Verdict | One-line rationale | Key citation |
|---|---|---|---|---|
| superbot | superbot-2.0 | **KEEP** | Live production Discord bot (merge=deploy, Q-0193) + the fleet's constitutional record (`docs/owner/`, 21 entries) + the parity oracle corpus | `d5e815c2` (2026-07-12); PR #2042 open |
| superbot-next | superbot-2.0 | **KEEP** | Active successor mid-cutover: 7 open PRs same day, 425 armed goldens, deploy packaging + cutover runbook in flight | `d3f3cb4`; goldens `6e8c666` (#265); runbook PR #264 |
| substrate-kit | self-improvement | **KEEP** | Kit source consumed by every planted repo — 2 releases shipped and distributed fleet-wide on census day; zero idle CI | `5363e41`; tags v1.10.1…v1.14.0 |
| fleet-manager | fleet-manager | **KEEP** | Coordination layer: `projects/` seat registry is a live data dependency of the control website; owner queue + orders | `5e404fd`; `control/status.md` "websites `app/projects.py`, 180s cache" |
| websites | websites | **KEEP** | Four live Railway-deployed FastAPI services + the active Anthropic-review artifact; same-day high velocity | `dfd6cce`; 4 Dockerfiles @origin/main |
| idea-engine | ideas-lab | **KEEP** | The fleet's only ideas corpus (329 files under `ideas/`) + active pipeline seat, near-zero idle cost | `ff48c2f` (PROPOSAL 012, same day) |
| sim-lab | ideas-lab | **KEEP** | Active evidence seat — produced VERDICT 014 the afternoon of the census; zero scheduled CI | `46d7387`; VERDICT 014 @ `477b452` (#53) |
| venture-lab | venture-lab (money) | **KEEP** | Sole holder of ~10 built-but-unpublished sellable candidates incl. a live-verified Stripe kit; "absorbed" premise disproven (§ venture-lab) | `77074ce`; Stripe HTTP 200 @ `75a5deb` (#74) |
| trading-strategy | venture-lab (money) | **KEEP** | Live paper-trading lane (first grading 2026-07-17), holdout SPENT — evidence ledger cannot be honestly regenerated | `dfd46bb`; trig_015aNMg5ncoSE2Roe4MKjQnr |
| pokemon-mod-lab | game-lab | **KEEP** | Active game-lab Track A (private by legal necessity — Nintendo-copyrighted decomp); ⚠ only unprotected default branch in the fleet | `df9d8b5` (#55, same day); `protected:false` |
| gba-homebrew | game-lab | **KEEP** | Most active lab seat: 3 shipped playable games in `dist/`, 2 ready PRs awaiting owner click | `f16e404`; PRs #68/#69 |
| codetool-lab-opus4.8 | (non-seat, wind-down) | **KEEP-QUIET** | Owner-ruled keep 2026-07-10: hosts released mdverify v0.1.0 + v0.2.0 and the proven workflow_dispatch release recipe; zero idle cost | `80f6cd1`; tags on origin; superbot `docs/ideas/adopt-codetool-lab-tools-2026-07-10.md` |
| superbot-games | superbot-world | **KEEP-QUIET** | Dormant-by-design (`phase: close-out + archive-prep`), zero idle CI; 310-test game packages awaiting the superbot-next plugin adapter | `bdc4cd1`; PRs #59/#60 open; contract @ superbot-next `d3dba9b` |
| superbot-idle | superbot-world | **KEEP-QUIET** | Dormant by design ("lane sleeps until a resume trigger fires"); 1,131-test CORE/SKIN engine with a defined but not-yet-buildable plugin path | `45ff2bf`; PRs #72/#74 open |
| superbot-mineverse | superbot-world | **KEEP-QUIET** | Zero idle CI; same-day security merge; archiving would strand the mining-write-contract counterpart superbot builds against | `3591c77` (#42); `docs/mining-write-contract.md` |
| superbot-plugin-hello | superbot-2.0 | **KEEP-QUIET** | The sweep's "empty repo" finding is **STALE** — seeded 2026-07-12T13:29Z as the out-of-tree plugin-contract exemplar; costs literally nothing (no CI, 4 KB) | `bbaccec` (sole commit, ORDER 002/014) |
| product-forge | (non-seat, closed lane) | **MIGRATE-THEN-ARCHIVE** | Self-declared "close-out / archived-ready"; 3 items to rehome, then archive — staying unarchived only adds kit re-render fan-out | `b25b090` (#23); `control/status.md` frozen 2026-07-11T19:39:50Z |
| codetool-lab-sonnet5 | (non-seat, wind-down) | **MIGRATE-THEN-ARCHIVE** | Owner-ruled harvest-first: v0.1.1 release decision (zero tags on origin) + differential-testing writeup port, then archive | `66c3dfc` (#16); superbot idea doc 2026-07-10 |
| codetool-lab-fable5 | (non-seat, wind-down) | **MIGRATE-THEN-ARCHIVE** | Owner-directed precondition: fix committed `__pycache__/*.pyc` + missing top-level `.gitignore` first; then envdrift release/adoption call, then archive | `a6cf1a9` (#14); defect verified in tree @ `a6cf1a9` |

**ARCHIVE-NOW: none.** Every inert repo either has an owner-ruled keep
(opus4.8), a named migration list (product-forge, sonnet5, fable5), or is
dormant-by-design feedstock for a defined future consumer (superbot-world
trio, plugin-hello).

## Negative findings — read these before trusting older sweeps

- **The venture-lab "trading engine absorbed" premise is DISPROVEN.** A
  full-history search (`git log --all --diff-filter=A --name-only` grep for
  backtest/trading) shows **no backtest engine ever existed in venture-lab**
  — the only trading-adjacent content is `candidates/market-state-dashboard/`
  (3 spec files, INTAKE `1db7427`, a descriptive screener spec). The real
  engine lives in **trading-strategy** `src/trading_lab/` (~126 KB source,
  15 strategy modules, 197 test functions), with the holdout **SPENT** (all
  13 ledger rows `holdout_unlocked=true`) and the paper lane **in-flight**
  (record paper-0001 WATCH, first grading due **2026-07-17**). Nothing was
  absorbed; the repos were always separate.
- **superbot-plugin-hello is NOT empty anymore.** The 2026-07-12 sweep's
  "empty repo" finding went stale at 13:29Z the same day: commit `bbaccec`
  ("seed: game-plugin-contract hello-world (ORDER 002 / ORDER 014)") landed
  6 files including the load-bearing
  `[project.entry-points."sb.plugins"]` in `pyproject.toml`. An in-tree twin
  exists at superbot-next `examples/superbot-plugin-hello/`, but the repo's
  entire point is being a *separate installable dist* exercising the
  pin/entry-point lifecycle — folding it in-tree defeats that.
- **The codetool labs are inert but NOT GitHub-archived** — `archived:false`
  in the API object for all three. The sweep "DARK" label
  (fleet-manager `.sessions/2026-07-12-research-census-sat.md:31`) and the
  roster's STALE-BY-DESIGN agree they are inert; the archive toggle has
  simply never been clicked.
- **pokemon-mod-lab `main` is UNPROTECTED** (`protected:false` via
  `list_branches`) — the only unprotected default branch found in the fleet.
  Every other checked repo reports `protected:true` or has documented
  required-check evidence.
- **Branch-protection rule details were unverifiable fleet-wide** — see
  Methods note below for the exact 403.

## Per-repo census

### superbot (KEEP — seat superbot-2.0)

- **Identity:** public, `archived:false`, **95,674 KB** (largest in fleet),
  default `main`.
- **Activity:** last commit `d5e815c2` (merge of #2040, dashboard-refresh
  automation) 2026-07-12; last non-automation `57ad8a25`/`29badae4` (#2039,
  session close) same day. Open PRs: 1 — #2042 (45th Q-0107 reconciliation
  pass, minutes old at census). Heartbeat `control/status.md` 2026-07-11T19:45Z
  (hub-touching-sessions file, not a standing seat).
- **Unique assets:** the production bot (`disbot/`, Railway auto-deploy on
  merge, Q-0193); the `docs/owner/` constitutional corpus (question router,
  decision authority, working profile — Q-numbers cited fleet-wide); the
  `parity/` golden-capture oracle superbot-next replays against (its PRs
  #269/#272 cite `menno420/superbot@main` as oracle — archiving before parity
  completes breaks the oracle); botsite/dashboard/design-system subtrees.
- **Cost:** 17 workflows, **5 with crons ≈170 scheduled runs/day** (see Cost
  findings). NOT kit-planted (no root `bootstrap.py`).
- **Verdict: KEEP.** Becomes MIGRATE-THEN-ARCHIVE only after superbot-next
  CUT-3 (token swap) lands — the cutover runbook (superbot-next PR #264)
  already plans that. Dead weight inside: the watchdog crons (phase 2).

### superbot-next (KEEP — seat superbot-2.0)

- **Identity:** public (pre-cutover; PR #264 plans a public→private flip at
  CUT-2), `archived:false`, 5,138 KB.
- **Activity:** last commit `d3f3cb4` (#271, admin-surface audit) 2026-07-12.
  **7 open PRs**, all created 15:05–15:15Z the same day (active build wave):
  #272 setup-prefix parity, #270 BrowserView, #269 rps copy, #267 poker port,
  #266 deploy packaging, #264 CUT-2/CUT-3 runbook, #263 live moderation
  adapter. Heartbeat 2026-07-12T15:05Z — freshest in the core cluster.
- **Unique assets:** the rebuild engine (`sb/` spec/namespace/kernel/domain/
  adapters/app/manifest); **`parity/goldens/` — 425 armed golden rows**
  (`6e8c666`, #265), irreplaceable without recapture.
- **Cost:** 5 workflows, 2 crons (daily/monthly backup + weekly
  restore-verify) — modest. Kit-planted (re-render PR per release: #251
  v1.13.0 + #260 v1.14.0 both landed census day).
- **Verdict: KEEP.** Nothing inside reads as dead weight.

### substrate-kit (KEEP — seat self-improvement)

- **Identity:** public, `archived:false`, 5,504 KB, MIT.
- **Activity:** last commit `5363e41` (#289) 2026-07-12. Open PRs: 2, both
  deliberately parked pin-path PRs labeled `do-not-automerge` awaiting owner
  ratification (#220, #238 — "Merge = ratify; close with a word = reject");
  oldest open PRs in the core cluster, worth an owner-queue surface so they
  don't rot.
- **Unique assets:** the kit source (`src/engine` templates →
  `dist/bootstrap.py`), releases v1.10.1…v1.14.0 consumed by every planted
  repo (v1.14.0 distribution waves A+B recorded in #285/#280); `bench/`
  cold-start benchmark corpus through run-9.
- **Cost:** 4 workflows, **zero crons — cheapest core repo when idle**.
- **Verdict: KEEP.** Archiving kills the fleet's doctrine-propagation
  mechanism.

### fleet-manager (KEEP — seat fleet-manager)

- **Identity:** public, `archived:false`, 2,632 KB.
- **Activity:** last commit `5e404fd` (roster gen #15, automation) 2026-07-12;
  last non-automation `171e24f` (kit v1.14.0, #115). Open PRs: 1 — #116
  (v3.3 seat-meta restamp, parked READY for owner click / non-author session
  — a self-merge venue wall, not necessarily branch protection).
- **Unique assets:** `projects/` seat registry (28 seat dirs) —
  **live-consumed by the control website** (`app/projects.py`, 180 s cache;
  archiving breaks a running site); owner queue
  (`docs/owner-queue.md` + checker); `control/inbox.md` orders (one writer:
  the owner); environment archetypes + prompts doctrine v3.3 (`48650f8`);
  roster tooling.
- **Cost:** 3 workflows; `roster-regen.yml` cron `40 */2 * * *` (**~12
  runs/day, each firing can commit to main** — generations #13/#15 landed
  census day). Kit-planted (#114/#115 re-renders same day).
- **Verdict: KEEP.** Cost lever: regen-on-change or 2×/day cadence (phase 2).

### websites (KEEP — seat websites)

- **Identity:** public, `archived:false`, 2,082 KB. Protection documented:
  "`quality` is now a REQUIRED status check on `main` (owner set the ruleset
  2026-07-09; verified live on PR #18)" (`docs/current-state.md@origin/main`)
  — the strongest indirect protection evidence in the fleet.
- **Activity:** last commit `dfd6cce` (#160, ORDER 012/016 records)
  2026-07-12; 5 merges within 11 minutes that day. Open PRs: 2 — #180
  (ORDER 017 C homepage rebuild, ready) + #163 (draft record-only session
  card). Heartbeat 2026-07-12T15:17:20Z.
- **Unique assets:** **four live Railway-deployed FastAPI services**
  (control-plane, botsite, dashboard, review — 4 Dockerfiles; "built,
  deployed, and live at control-plane-production-abb0.up.railway.app" per
  `docs/current-state.md`); the review service is the public evidence-backed
  site for the Anthropic review window through 2026-07-14. Archiving would
  orphan live production services.
- **Cost:** 4 workflows, **3 crons ≈53 runs/day** (see Cost findings).
  Kit-planted. Wall append 2026-07-12: `RAILWAY_TOKEN` NOT provisioned.
- **Verdict: KEEP.** Trim candidate: the `13,43 * * * *` enabler cron.

### idea-engine (KEEP — seat ideas-lab)

- **Identity:** public, `archived:false`, 2,753 KB.
- **Activity:** last commit `ff48c2f` (#260, PROPOSAL 012 routine-cadence
  economics sim → sim-lab) 2026-07-12. Open PRs: 0. Heartbeat
  2026-07-12T14:23:57Z.
- **Unique assets:** the **fleet ideas corpus — 329 files under `ideas/`**
  (superbot 239, websites 15, fleet 14, venture-lab 11, superbot-next 8, …)
  plus the control-layer pipeline records. Splitting per-section into lane
  repos would destroy the cross-fleet idea-engine → sim-lab → manager
  pipeline (superbot Q-0264).
- **Cost:** 2 workflows, zero crons. Kit-planted.
- **Verdict: KEEP.**

### sim-lab (KEEP — seat ideas-lab)

- **Identity:** public, `archived:false`, 1,038 KB.
- **Activity:** last commit `46d7387` (#54, VERDICT 014 fan-out) 2026-07-12
  17:27 — the most recently pushed repo in its cluster at census. Open PRs: 0.
- **Unique assets:** the sim harness (`harness/simharness.py`) + completed
  sim verdicts with raw judge/rep JSON runs (intake-001/-002/-003,
  owner-001); VERDICT 014 (#53, `477b452`) actively consumed by idea-engine
  PROPOSAL 012 (`ff48c2f`) the same afternoon.
- **Cost:** 2 workflows, zero crons. Kit-planted.
- **Verdict: KEEP.**

### product-forge (MIGRATE-THEN-ARCHIVE — non-seat, closed lane)

- **Identity:** public, `archived:false`, **325 KB (smallest planted repo,
  79 tracked files)**. `has_pages:true` in the API but the Pages site 404s
  (fresh curl this session) — a half-completed post-close-out enablement
  (OA-003) with no successful deploy.
- **Activity:** **self-declared close-out.** Last commit `4fdfa8a` (merge of
  #23, 2026-07-11); content commit `b25b090` "close-out: archive-ready —
  final status.md heartbeat…". `control/status.md` verbatim:
  `phase: close-out / archived-ready`, orders 001–004 DONE, "PRs #1–#22 ALL
  MERGED — zero open, zero closed-unmerged". Heartbeat frozen
  2026-07-11T19:39:50Z — the only >24 h-stale heartbeat in its cluster.
- **Unique assets → migration list (3 items):**
  1. `products/games-web/` — self-contained static character-sheet game UI
     with `game-state.schema.json` v1.0.1 contract + tests → **superbot-games**
     or the websites botsite Fleet Arcade (which shipped its catalog slice the
     next day, websites `06409f5`).
  2. `products/games-web/docs/phase2-data-api-proposal.md` — unanswered API
     request addressed to the superbot lane → **superbot docs**.
  3. `docs/retro/2026-07-11-self-review.md` → **fleet-manager**.
- **Cost:** 3 workflows, zero crons, zero idle burn — but kit-planted, so it
  keeps drawing a re-render PR per kit release while unarchived.
- **Verdict: MIGRATE-THEN-ARCHIVE.**

### venture-lab (KEEP — seat venture-lab / money)

- **Identity:** public, `archived:false`, 3,749 KB (14 kit backups under
  `.substrate/backup` explain part of the size).
- **Activity:** last commit `77074ce` (#77, Hollowtide novella wave 2)
  2026-07-12, preceded minutes earlier by `19e7e88` (#76, ~26k-word YA
  novella), `8803b99` (#75, 3 trilingual picture books), `75a5deb` (#74,
  Stripe kit live verification). Open PRs: 0. Heartbeat 2026-07-12T14:01Z.
- **Unique assets:** the unpublished revenue-candidate corpus —
  childrens-books (80 files), ya-novels (23), agent-fleet-field-manual (21
  incl. built dist zip), photo-packs (20), dream-series (20), bababoefoe
  (20), membership-kit (19 incl. buyer zip, 13 green tests), template-packs
  (14), **stripe-webhook-test-kit (13 — live-verified against the owner's
  real Stripe signing secret, HTTP 200, `75a5deb`)**, plus `docs/launch/`.
  All publishing is owner-gated by the lane's hard rail, so **this repo is
  the only copy** of finished-but-undistributed work.
- **Negative finding:** the trading-engine premise is false here — see
  Negative findings above; `candidates/market-state-dashboard/` is spec-only
  (`1db7427`).
- **Cost:** 3 workflows, zero crons. Kit-planted.
- **Verdict: KEEP.** Live triggers: 2-hourly money-seat failsafe
  (trig_017o6azZTd9pzcaSthEncT5q) + a launch-watch one-shot
  (trig_01NPebmqLbadbKbscZVW7vEG).

### trading-strategy (KEEP — seat venture-lab / money)

- **Identity:** public, `archived:false`, 4,485 KB, created 2026-07-09.
- **Activity:** last commit `dfd46bb` (kit v1.14.0, #74) 2026-07-12; 11 PRs
  merged that day. Open PRs: 0. Heartbeat 2026-07-12T12:12Z,
  `phase: ARCHIVE-READY` (coordinator chat archived — the *chat*, not the
  repo; the lane's evidence is live). **Zero cron workflows**, but two live
  Claude Routines: weekly paper-grading trig_015aNMg5ncoSE2Roe4MKjQnr
  (`0 9 * * 5`, next fire 2026-07-17T09:05Z) + the shared 2-hourly money-seat
  failsafe.
- **Unique assets:** the confirmed-real backtest engine
  (`src/trading_lab/`: engine, sweeps, walkforward, portfolio, paper lane,
  mtf, + 15 strategy modules; 10 test files / 197 test functions; "229
  passed at PR #71"); 2.4 MB `data/` fixtures + 3.0 MB `experiments/`
  evidence ledger. **Irreplaceable state: the holdout is SPENT** (all 13
  ledger rows `holdout_unlocked=true`) and paper record paper-0001 is
  in-flight with `PAPER_LANE_START` 2026-07-11 pinned in config+test —
  this ledger cannot be regenerated honestly.
- **Cross-repo tie:** venture-lab's dashboard candidate plans cross-repo
  READS of this repo via raw.githubusercontent.com (venture-lab
  `.sessions/2026-07-12-candidate-market-state-dashboard.md` L13-14) — the
  dependency is on the published ledger, not the engine code.
- **Cost:** 3 workflows, zero scheduled burn. Kit-planted.
- **Verdict: KEEP.**

### superbot-games (KEEP-QUIET — seat superbot-world)

- **Identity:** public, `archived:false`, 1,985 KB (`.substrate/` is 7.4 MB
  of on-disk bulk).
- **Activity:** last commit `bdc4cd1` (kit v1.14.0, #63) 2026-07-12. Open
  PRs: 2 docs-only, <1 day old — #60 (mining WORKFLOW audited seam) + #59
  (correct stale plugin-contract claims). Heartbeat 2026-07-11T19:39:14Z,
  `phase: close-out + archive-prep`; its "5 open PRs parked" list is stale
  (#50/#52–#55 since merged).
- **Unique assets:** `games/` pure-domain packages (dnd, exploration,
  fishing, mining, shared) with **310 passing tests** (PR #60 body), built
  as plugin-side packages targeting the superbot-next game-plugin-contract
  (binding at superbot-next `docs/game-plugin-contract.md@d3dba9b`, PR #59).
  Host adapters are "a later ladder rung" — migration is defined but not yet
  buildable.
- **Cost:** 2 workflows, zero crons, zero idle burn. Kit-planted.
- **Verdict: KEEP-QUIET.** Re-verdict to MIGRATE-THEN-ARCHIVE once the
  superbot-next plugin host consumes the packages.

### superbot-idle (KEEP-QUIET — seat superbot-world)

- **Identity:** public, `archived:false`, 862 KB, created 2026-07-10.
- **Activity:** last commit `45ff2bf` (#73, ORDER 003 pytest CI) 2026-07-12.
  Open PRs: 2 — #74 (pytest workflow; body notes "branch protection is
  owner-only", pytest not yet a required check) + #72 (un-park PLUG-001,
  citing the now-verified plugin contract @ `d3dba9b`). Heartbeat
  2026-07-11T19:37:36Z, `phase: ARCHIVED-READY / dormant — wake loop
  DISARMED`.
- **Unique assets:** `idle_engine/` CORE/SKIN engine + 12 data-only theme
  packs + **1,131 passing tests** (PR #74 body), seeded per superbot
  Q-0267 founding package. Natural home: an `sb.plugins` dist on
  superbot-next once the adapter exists.
- **Cost:** 2 workflows, zero crons. Kit-planted.
- **Verdict: KEEP-QUIET.** Land or close PRs #72/#74 first.

### superbot-mineverse (KEEP-QUIET — seat superbot-world)

- **Identity:** public, `archived:false`, 626 KB, created 2026-07-11.
- **Activity:** last commit `3591c77` (#42, **same-day security merge**:
  login-CSRF OAuth binding + snapshot ingestion validation) 2026-07-12.
  Open PRs: 1 — #31 (Codex pre-provisioning security report) whose two
  findings were already fixed by merged #42 and dispositioned by #43
  (`f8b6dbf`) — **dispositioned-but-still-open; close it** (phase 1).
  Heartbeat 2026-07-11T23:51:34Z.
- **Unique assets:** working browser game over superbot's live mining
  economy (`server/` stdlib backend with OAuth + signed writes, `web/`
  no-build frontend, 98 tests). Write contract stage c is test-guild-only;
  the bot-side endpoint is built in superbot against
  `docs/mining-write-contract.md`; stage d live-prod NOT shipped
  (`docs/live-prod-cutover.md`, all prerequisite boxes unchecked). No deploy
  config in tree.
- **Cost:** 3 workflows, zero crons. Kit-planted.
- **Verdict: KEEP-QUIET.** Archiving would strand superbot's write-contract
  counterpart.

### superbot-plugin-hello (KEEP-QUIET — seat superbot-2.0, exemplar)

- **Identity:** public, `archived:false`, **4 KB**, created 2026-07-10.
- **Activity:** exactly one commit — `bbaccec`, "superbot-next builder",
  2026-07-12T13:29:35Z, "seed: game-plugin-contract hello-world (ORDER 002 /
  ORDER 014)". Open PRs: 0. No `control/`, no workflows, no CI.
- **Unique assets:** 6 files — the canonical **out-of-tree exemplar of the
  superbot-next game-plugin-contract**, incl. the load-bearing
  `[project.entry-points."sb.plugins"]` in `pyproject.toml`; "the minimal
  working example new game repos copy from" (README@`bbaccec`).
- **Cost:** zero — no workflows, not kit-planted.
- **Verdict: KEEP-QUIET.** Do NOT archive on the stale "empty" report; the
  in-tree twin at superbot-next `examples/` does not replace the
  out-of-tree install test this repo exists to provide.

### codetool-lab-opus4.8 (KEEP-QUIET — non-seat, wind-down complete)

- **Identity:** public, `archived:false`, 122 KB, pushed 2026-07-09T20:13Z.
  `main` `protected:true` (list_branches boolean).
- **Activity:** last commit `80f6cd1` (#22, "wind-down complete — ready for
  archive + fresh session") 2026-07-09. Open PRs: 0. Zero crons. One stray
  branch (`claude/status-heartbeat-001` @ `ea1b23b`).
- **Unique assets:** **mdverify** — released markdown code-block verifier,
  **tags v0.1.0 + v0.2.0 on origin** (`git ls-remote --tags`), 162 tests;
  the proven workflow_dispatch release recipe; succession pack + retros.
  Findings already exported to superbot `docs/eap/` + fleet-manager
  `docs/experiments/harness-x-model-2026-07-09.md`.
- **Verdict: KEEP-QUIET** — owner ruled 2026-07-10: "Keep opus4.8 unarchived
  (live released tool + the proven workflow_dispatch release recipe)"
  (superbot `docs/ideas/adopt-codetool-lab-tools-2026-07-10.md`).

### codetool-lab-sonnet5 (MIGRATE-THEN-ARCHIVE — non-seat, wind-down complete)

- **Identity:** public, `archived:false`, 98 KB. `main` `protected:true`.
- **Activity:** last commit `66c3dfc` (#16) 2026-07-09. Open PRs: 0. Zero
  crons. `release.yml` triggers on tag push — but **zero tags exist on
  origin**. Stray branch `test/push-check` @ `0260aae`.
- **Unique assets → harvest list:** **cfgdiff** (semantic config
  diff/convert, 5 format parsers, 165 tests) with **v0.1.1 never released —
  archiving freezes the tag-push path forever**, so release-or-explicitly-
  accept-unreleased first; the **differential-testing method writeup**
  ("corpus vs a reference parser found 3 real bugs behind green tests") —
  named worth porting to kit-lab benchmark practice; confirm succession/retro
  content is covered by superbot `docs/eap/gen1-grand-review-2026-07-09.md`.
- **Verdict: MIGRATE-THEN-ARCHIVE** (owner ruling 2026-07-10: "Archive
  sonnet5 + fable5 … **after** this idea executes — harvest first").

### codetool-lab-fable5 (MIGRATE-THEN-ARCHIVE — non-seat, wind-down complete)

- **Identity:** public, `archived:false`, 121 KB. `main` `protected:true`
  (the only branch).
- **Activity:** last commit `a6cf1a9` (#14, "Succession-doc fix: release-wall
  is SEAT-DEPENDENT") 2026-07-10. Open PRs: 0. Zero crons; **no release
  workflow at all** — releasing envdrift requires new work before any archive.
- **Unique assets → harvest list:** **envdrift** (zero-dependency .env drift
  checker, 111 tests, tags unpushed); the seat-dependent release-wall finding;
  succession `PLATFORM-LIMITS.md`. **Known defect, owner-flagged:** committed
  `__pycache__/*.pyc` under `src/envdrift/commands/` + **no top-level
  `.gitignore`** (both verified in tree @ `a6cf1a9`); owner: "fix fable5's
  committed .pyc files + missing .gitignore before archiving".
- **Verdict: MIGRATE-THEN-ARCHIVE** (same owner ruling as sonnet5).

### pokemon-mod-lab (KEEP — seat game-lab, Track A)

- **Identity:** **PRIVATE** (the fleet's only private repo), `archived:false`,
  **19,421 KB**, language C, pushed 2026-07-12T13:52Z. **`main`
  `protected:false` (list_branches) — the only unprotected default branch
  found in the fleet**; flag for phase 3.
- **Activity:** last commit `df9d8b5` (kit v1.14.0, #55) 2026-07-12; daily
  cadence. Open PRs: 0. Zero crons. 3 stale branches.
- **Unique assets:** the Pokémon Emerald mod on the pret/pokeemerald
  decomp — vendored `pokeemerald/` (11,557 files) + `agbcc/` (932) are
  plain trees, re-obtainable upstream, NOT unique; **unique and
  irreplaceable:** `docs/proof/order-001/mod.diff` + proof screenshots,
  `docs/findings/`, `docs/mod-concepts.md`, 36 session logs. Hard rail:
  Nintendo-copyrighted content — **its only valid home is this private
  repo**; ORDER 006 added a `.gitignore` ROM guard (`2efe16d`).
- **Cost:** 2 workflows, push/PR only. Kit-planted.
- **Verdict: KEEP.**

### gba-homebrew (KEEP — seat game-lab, Track B)

- **Identity:** public, `archived:false`, 2,042 KB, pushed 2026-07-12T13:50Z.
  `main` `protected:true`.
- **Activity:** most active lab repo. Last commit `f16e404` (kit v1.14.0
  merge, #71) 2026-07-12; last Claude-authored `4039cd5` same day. Open PRs:
  2, both hours old and parked READY for the owner's merge click: #69
  (Brineward slice 5) + #68 (Gloamline slice 8, synthesized audio). Heartbeat
  2026-07-12T13:00:22Z.
- **Unique assets:** original, publish-safe GBA/NDS homebrew — **3 shipped
  playable games in `dist/`** (`lumen-drift.gba`, `brineward.nds`,
  `gloamline.nds`) + full source in `games/`, concept docs, player guides,
  py-desmume headless-proof suites (19 proofs/353 asserts and 12/265 per
  #68/#69). Entirely original IP; this repo IS the natural home. The 2 open
  PRs are unmerged work-product that would be lost as-is if archived.
- **Cost:** 3 workflows, dispatch/push/PR only. Kit-planted.
- **Verdict: KEEP.**

## Trigger map (telemetry/triggers-snapshot.json @ fleet-manager origin/main; 832 records, 28 enabled)

**9 standing crons:**

| Trigger | id | Schedule | Repo(s) referenced |
|---|---|---|---|
| Websites failsafe wake | trig_01Aak59jvQQdimDgy5K1yAGQ | `45 */2 * * *` | websites (seat; text names no repo) |
| game-lab failsafe wake | trig_01JD1t7rD5jUCqkJQJaNCi3E | `50 */2 * * *` | gba-homebrew + pokemon-mod-lab |
| Ideas Lab failsafe wake | trig_01T83UuVthszGBcENYwrTrm7 | `0 */2 * * *` | idea-engine (+ sim-lab seat) |
| kit-lab loop | trig_01Jm57GAjNCFrYJn1oLMiYGE | `0 6 * * *` (fresh session per fire) | substrate-kit |
| SuperBot World failsafe wake | trig_01KQbKNiSVfZRWutKEWFx2q2 | `0 */2 * * *` | superbot-games/-idle/-mineverse seat |
| fleet-manager failsafe wake | trig_01BKpsyoBzp1K1ob9H3iu1gM | `30 */2 * * *` | fleet-manager |
| substrate-kit failsafe wake | trig_011iJucRpsruWJ4dFB7xVbvf | `0 */2 * * *` | substrate-kit |
| trading-strategy weekly paper-lane grading | trig_015aNMg5ncoSE2Roe4MKjQnr | `0 9 * * 5` | trading-strategy |
| venture-lab money-seat failsafe wake | trig_017o6azZTd9pzcaSthEncT5q | `0 */2 * * *` | venture-lab + trading-strategy |

**1 poke-only (no schedule):** "suberbot docs reconciliation"
trig_018wP6XTPmf9DLnxrG4RpGVh — fired by the `reconcile` GitHub issue;
repo: superbot.

**18 enabled one-shots (send_later):** mostly pacemaker/continuation ticks
09:10–12:07Z on 2026-07-12 — generic "continue the work loop / PACEMAKER
TICK" ×~11 (session-bound, no repo in text); game-lab pacemakers ×3;
venture-lab launch-watch (trig_01NPebmqLbadbKbscZVW7vEG); superbot-world
owner-action pacemakers ×2 (trig_01Euwjeyp62UaEwEZE5wnaXE,
trig_011pyLrcReLqUbLrT1v7sr6H); fleet-manager overnight-review self-check-in
(trig_012WPzettDVAaqMi2KLpeCqp); trading-strategy weekly-grading one-shot
2026-07-17T09:00Z (trig_01YXNmgqYeYQ1LuepsLmbNCG).

**Consolidation-relevant read of the map:** verified against the full list
above — **no armed standing trigger (and no enabled one-shot) references
product-forge, codetool-lab-sonnet5, or codetool-lab-fable5**, the three
MIGRATE-THEN-ARCHIVE repos: archiving them breaks no automation. Meanwhile
**trading-strategy and venture-lab — both KEEP — each carry live triggers**
(the weekly grading cron firing 2026-07-17, the money-seat failsafe, and the
launch-watch one-shot), reinforcing that the money lane is operationally
live, not dormant.

## Cost findings — where the fleet's Actions burn actually is

Scheduled (idle) burn is concentrated in exactly three repos:

1. **superbot — ≈170 scheduled runs/day, the fleet's dominant burner.**
   5 of its 17 workflows carry crons: `ci-rerun-watchdog.yml` `*/12 * * * *`
   (≈120/day), `pr-conflict-guard.yml` `*/30 * * * *` (≈48/day),
   `dashboard-data-refresh.yml` every 2 h (and it generates self-merging
   `bot/dashboard-refresh` PRs — 6 in the current recon band per PR #2042),
   `backup-db.yml` daily+monthly, `codeql.yml` weekly.
2. **fleet-manager — `roster-regen.yml` every 2 h (~12 runs/day), each
   firing able to commit to main** (generations #13/#15 landed census day).
3. **websites — 3 crons ≈53 runs/day:** `auto-merge-enabler.yml`
   `13,43 * * * *` (48/day — the single biggest idle line outside superbot),
   `healthcheck.yml` every 6 h, `review-bake.yml` daily.

**Every other repo has zero scheduled burn** — verified per-repo by grepping
`schedule:` across `.github/workflows/` at origin/main (the superbot-world
trio, plugin-hello, the codetool labs, both game-lab repos, trading-strategy,
venture-lab, idea-engine, sim-lab, product-forge, substrate-kit all clean;
superbot-next carries only backup/restore-verify crons).

**Kit re-render fan-out:** 13 repos carry kit files (`bootstrap.py` +
`.substrate/`); each kit release fans ~1 re-render PR per planted repo —
**~9 planted repos received v1.13.0/v1.14.0 re-render PRs on 2026-07-12
alone, across 2 releases that day** (observed: superbot-next #251/#260,
fleet-manager #114/#115, trading-strategy #74, superbot-games #63,
pokemon-mod-lab #55, gba-homebrew #71, plus distribution waves A/B recorded
in substrate-kit #285/#280). Each unarchived dormant planted repo
(product-forge today) keeps drawing this cost for nothing.

## Proposed end-state (target shape)

8 seats → repos (post-consolidation: **19 → 16 unarchived repos**):

| Seat | Repos | Notes |
|---|---|---|
| fleet-manager | fleet-manager | coordination layer, unchanged |
| superbot-2.0 | superbot + superbot-next (+ superbot-plugin-hello) | plugin-hello kept as the out-of-tree contract exemplar; superbot itself re-verdicts after CUT-3 |
| websites | websites | live Railway services |
| self-improvement | substrate-kit (+ codetool-lab-opus4.8 kept quiet) | opus4.8 stays as released-tool host (mdverify v0.1.0/v0.2.0, owner-ruled) |
| superbot-world | superbot-games + superbot-idle + superbot-mineverse | all quiet until the superbot-next plugin host lands, then re-verdict |
| game-lab | gba-homebrew + pokemon-mod-lab | Track B public / Track A private-by-necessity |
| ideas-lab | idea-engine + sim-lab | the Q-0264 pipeline pair |
| venture-lab (money) | venture-lab + trading-strategy | live triggers; paper lane grading from 2026-07-17 |

Archived (reversibly — GitHub unarchive is a settings toggle; **nothing is
deleted**): product-forge, codetool-lab-sonnet5, codetool-lab-fable5.

## Phased, reversible sequencing

Migrations land **before** archive toggles; nothing is deleted, only
archived (reversible).

### Phase 1 — agent PRs, can start now (all agent-doable)

1. **product-forge rehoming (3 PRs):** `products/games-web/` →
   superbot-games (or the websites arcade — decide at PR time against the
   Fleet Arcade slice that shipped in websites `06409f5`);
   `phase2-data-api-proposal.md` → superbot docs;
   `docs/retro/2026-07-11-self-review.md` → fleet-manager.
2. **codetool-lab-sonnet5:** port the differential-testing method writeup to
   kit-lab benchmark practice.
3. **codetool-lab-fable5:** fix the committed `__pycache__/*.pyc` + add the
   missing top-level `.gitignore` (owner-directed precondition).
4. **superbot-mineverse:** close PR #31 — its findings are superseded by
   merged #42, per #43's disposition.
5. **Codetool findings export check:** confirm succession/retro content is
   fully covered by superbot `docs/eap/gen1-grand-review-2026-07-09.md` +
   fleet-manager `docs/experiments/harness-x-model-2026-07-09.md`.

### Phase 2 — owner decisions (route via the owner queue)

1. **sonnet5 cfgdiff v0.1.1:** release it (tag push is owner-only) or
   explicitly accept it staying unreleased — archiving freezes the tag path.
2. **fable5 envdrift:** release/adoption call (no release workflow exists;
   owner's named "environment-tidying interest" — natural home: fleet tool
   adoption).
3. **superbot cron cadences:** ci-rerun-watchdog `*/12` and pr-conflict-guard
   `*/30` are ~170 runs/day; decide reduced cadences.
4. **fleet-manager roster-regen cadence:** every-2h auto-commit loop →
   regen-on-change or 2×/day.

### Phase 3 — owner clicks, settings-only (OWNER-ONLY; after phase 1 lands)

1. **GitHub archive toggle** on product-forge, codetool-lab-sonnet5,
   codetool-lab-fable5 (repo Settings; reversible via unarchive).
2. **Protect pokemon-mod-lab `main`** (the fleet's only unprotected default
   branch; repo Settings → branch protection/ruleset).

All migration PRs in phase 1 are agent-doable today; the archive toggle and
branch protection in phase 3 are GitHub settings actions only the owner can
perform.

## Methods & could-not-verify

- **Branch-protection rule details — unverifiable fleet-wide.** `gh` CLI is
  not installed in the census containers (`gh: command not found`), the
  loaded GitHub MCP toolset exposes no branch-protection endpoint, and
  direct REST (`/repos/menno420/<repo>/branches/main/protection`) returned
  the same error for every repo attempted (once each, per the
  documented-wall discipline):
  `HTTP 403 {"message":"GitHub access is not enabled for this session. An org admin must connect the Claude GitHub App for this organization."}`
  — consistent with the fleet's documented "`api.github.com` direct HTTP:
  blocked → GitHub access is MCP-tools-only" wall (superbot-next
  `docs/CAPABILITIES.md`, LAST-VERIFIED 2026-07-10). Only the boolean
  `protected` flag from `list_branches` was obtainable (gathered in the labs
  cluster), plus indirect documentary evidence per repo (strongest:
  websites' "owner set the ruleset 2026-07-09; verified live on PR #18").
- **Authorship attribution caveat (squash-merge):** almost every main commit
  fleet-wide is authored "Menno van Hattum" but is agent-session work merged
  under the owner identity (Claude-Session trailers in PR bodies; the owner
  does not code). "Last commit" claims above mean last
  non-workflow-automation commit; human-keystroke vs agent commits are
  indistinguishable by author field.
- **Deployment liveness not probed:** websites' Railway services are
  asserted from `docs/current-state.md` + 4 Dockerfiles, not probed;
  product-forge's Pages state inferred from `has_pages:true` + a fresh 404;
  no other repo shows deploy config at origin/main; anything the owner runs
  off-repo is invisible from here.
- **opus4.8 GitHub Release objects:** tags v0.1.0/v0.2.0 verified via
  `git ls-remote --tags`; the Release objects themselves were not queried.

## Provenance

Synthesized 2026-07-12 from five parallel census worker reports (setup /
core / kit-planted / game-product / labs clusters), session
`.sessions/2026-07-12-repo-consolidation-census.md`, PR #119. Trigger data:
`telemetry/triggers-snapshot.json` @ fleet-manager origin/main (832 records,
snapshot 2026-07-12). Seat registry: `docs/roster.md` gen #15 (the superbot
`docs/eap/fleet-manifest.md` is `historical`, superseded 2026-07-11).
