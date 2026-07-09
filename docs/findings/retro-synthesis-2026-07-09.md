# Fleet retro synthesis — all 10 lanes (2026-07-09)

> **Status:** `reference`
>
> Distilled 2026-07-09 (evening) from the manager's read-only synthesis worker,
> which read every lane's merged self-review + project-review (the
> universal-wakeup deliverables; see `docs/prompts/universal-wakeup.md`) and
> spot-checked claims against live GitHub. **This is the gen-2 blueprint's
> primary input** (`docs/gen2-blueprint.md`). Reviews are testimony — verify
> against repos before acting (playbook R2). Substance kept complete on purpose.

## 1. Coverage

| Lane | self-review | project-review | Where |
|---|---|---|---|
| superbot-next | ✅ MERGED (PR #87, 17:04Z) | ❌ **MISSING ENTIRELY** — no file on main under any name (code search 0 hits), zero open PRs | `docs/retro/self-review-2026-07-09.md` |
| substrate-kit | ✅ MERGED (PR #51, 17:23:58Z) | ✅ MERGED (same PR) | Plus a **duplicate second ORDER-005 attempt sat in open READY PR #50** (opened 17:10Z by a different session, same two file paths — conflicts now that #51 landed) |
| websites | ✅ MERGED (PR #40, 17:11Z) | ✅ MERGED (same PR) | main |
| trading-strategy | ✅ MERGED | ✅ MERGED | main (no open PRs) |
| codetool-lab-fable5 | ✅ MERGED | ✅ MERGED | main; open PR #9 is 0.2.0 continuation, not retro |
| codetool-lab-opus4.8 | ✅ MERGED (PR #8) | ✅ MERGED | main; open PRs #12/#13 are continuation |
| codetool-lab-sonnet5 | ✅ MERGED | ✅ MERGED | main |
| superbot-games / exploration | ✅ MERGED (`self-review-exploration-2026-07-09.md`) | ✅ MERGED (`project-review-2026-07-09-exploration.md`) | main @ ff93007 |
| superbot-games / mining | 🟡 **IN OPEN PR #9** (`self-review-mining-2026-07-09.md`) | 🟡 **IN OPEN PR #9** (`project-review-2026-07-09-mining.md`) | PR #9 READY, deliberately NOT auto-merge-armed (classifier blocked self-merge); merging it is an owner action. Mining's build PRs #4/#5 also still open (draft) |

**Not yet answered:** superbot-next has delivered only half its retro — the
project-review (agent audit + owner actions + continuation) does not exist
anywhere. Everything else is delivered; mining's pair is in-flight (unmerged
but complete on the PR branch).

## 2. Per-lane digests

### superbot-next (self-review only; ORDER 005)

- **Shipped vs claimed:** everything on main (rebuild PRs #1–#54, CUT-1
  successors #61/#65/#67/#70/#71, fix train #56–#85, game-plugin contract #75);
  zero branch inventory. One admitted gap: `examples/superbot-plugin-hello/`
  lives in-tree because the GitHub App can't create the separate repo the ORDER
  asked for (flag 18a). Honest split: testing phase verified against live boot
  + real test guild + 465-golden replay; **the entire build phase (PR #1–#54)
  was self-tested only** — the fix train was that debt being paid.
- **Least confident:** the human-judgment CLASSIFICATION of ~90 golden-replay
  reds ("0/N but every line classified, no bug hides in the noise"), and band 7
  (AI) never exercised live (no API key).
- **Biggest silent breakages:** mutations succeeding with NO user-visible ack
  (found three separate times — one class); oversize replies swallowed by
  design; live dispatch running on empty snapshot shells while unit tests were
  green; warn-escalation phantom rows *enshrined by a unit test asserting the
  wrong behavior*; clock/RNG replay leaks. Pattern named: "silence broke where
  no oracle was looking."
- **Efficiency:** est. 25% orientation / 30% build / 30% verify / 10% CI / 5%
  blocked; biggest sink = orientation (append-only handoff prose re-assembled
  each session). Redo: build ~15–20% faster, but walking-skeleton +
  replay-before-merge would have deleted the entire ~8-PR fix-train phase.
- **Stalls/owner points (D1, 8 items):** privileged-intent toggles (owner-only),
  sacrificial ban/kick account (owner-only), flag-13 corpus ruling (genuine
  owner call), hub topology (taste), settings-edit boundary (admits: should
  have been decide-and-flag), repo creation 403 (grant-fixable),
  hand-verification of presentation (human-only interaction tokens), stale
  command tree (pre-grantable).
- **Model:** the self-review carries **no model attribution for itself or its
  sessions** — cannot determine from the delivered doc. (Merge commits ride one
  session ID; substrate-kit's registry lists superbot-next only as an adopter.)
- **F1 three rules:** (1) boot a walking skeleton before the second PR and keep
  it green in CI; (2) every mutation speaks or fails loudly — a merged op with
  no ack is a defect; (3) LOOK at rendered output before claiming PASS; attach
  the render to the PR.
- **F4 highlights:** skeleton committed at seed vs real Postgres; oracle
  vendored + goldens + red-class table day 0; replay-your-band + live-drive as
  REQUIRED checks; committed live-drive driver + dev-env doc; grants
  pre-negotiated; merge queue (kill the branch-update dance); "README-first"
  explaining that red ≠ broken.
- **⚑ owner actions:** none formally issued (that's the missing
  project-review). D4 names the grant set: repo-create + ruleset-bypass on
  sbnext-*; sacrificial test account + both privileged intents; capped
  ANTHROPIC_API_KEY for band 7; the flag-13 ruling as standing policy;
  restart-at-will.

### substrate-kit

- **Shipped vs claimed:** 41 merged PRs (38 on 07-09 alone), five releases
  v1.0.0–v1.4.0 in one day, 705 tests, bands KL-0…KL-8, ORDERS 001–005.
  Branch-only *by design*: PR #26 (PL-011) and PR #49 (pin-path seed fix) —
  owner merge = ratification. One abandoned PR (#30). Admits the 705-test suite
  is a **self-oracle**; externally verified: bench verdicts judged by a
  separate judge model, sha256 release-integrity proof, live-fire auto-merge
  guard test.
- **Biggest errors:** incident #22 — a `do-not-automerge` LAW PR auto-merged
  via the enabler's stale-label read + ~12-min runner-queue lag (part ours,
  part platform; cost two full guard-building sessions); PR #7 merged red 24s
  after open (GitHub counts a *skipped* check as satisfying a required check);
  owner-landed ruleset with legacy context names discovered via a 405 (root
  cause under both incidents + a duplicate runner burned on all 41 PRs);
  make_seed generated a SyntaxError seed (`yield` drawn as an identifier); dist
  byte-pin green while the dist itself NameError'd; one session dead at
  provisioning (owner setup script `pip install -r` on a repo with no
  requirements.txt).
- **Efficiency:** ~14.5h day; est. 35% build / 20% verify / 15% orientation /
  20% CI-merge mechanics / 10% blocked. Biggest sink: CI/merge mechanics +
  incident guard-building. The 5¾h #17 rubric-blessing wait was parallelized
  well (7 PRs merged inside it). Redo ~30–40% faster; ordering: **P10
  required-check alignment before any auto-merge use**, engagement gate before
  inviting adopters, bench smoke before run-1. Repo records no durations — C1
  is an estimate and says so.
- **Stalls a/b/c:** census: one dead-at-provisioning (a+b), one abandoned PR
  (a), two premature-merge incidents (kit#22 a+b; superbot-next#44 a), **zero
  sessions lost to the work itself (c)**.
- **Model:** recorded on every card from KL-3 (PR #13) onward; **everything
  pre-KL-3 honestly "cannot be determined"** (Model-line convention didn't
  exist yet); bench judge recorded verbatim, judge ≠ builder; dead session +
  manager writes = cannot determine.
- **F1:** (1) verify required checks name your CI's gate BEFORE first
  auto-merge — mismatch = stop-ship; (2) CHANGELOG bullet rides the same diff +
  every card records wall-clock start/end; (3) an oracle you built gets smoked
  before it judges (seed sweeps, known-bad fixtures).
- **F4:** required checks aligned at seed + auto-merge + auto-delete-branches
  ON; control bus at seed; journal pre-seeded with platform limits; born-red
  ritual + PR template from PR #1; engagement gate in the first release
  adopters see; bench with smoke suite; settings read path; guarded setup
  script; telemetry with time from row one.
- **⚑ owner actions (click-level):** (1) P10 swap: Settings → Rules → remove
  legacy contexts "Kit test suite" + "Cold-adoption smoke (adopt + check
  --strict)", add "kit-quality", leave up-to-date OFF; (2) tick "Automatically
  delete head branches" + delete stale claude/* branches; (3) merge PR #26 =
  ratify PL-011; (4) ratify/veto PL-010 by commenting on PR #22; (5) rule the
  F-5 "none regressing" wording (strict vs 7k-budget); (6) merge PR #49
  (unblocks B1 run-3); (7) paste the corrected env setup script
  (docs/environment-setup-script.md) into the Project's environment settings;
  (8) standing gates P4 (lab-loop cron `0 6 * * *`), P5 (Railway `kit-lab`),
  P11 public flip or P13 read-only PAT, P8 MIT confirm; (9) fleet-side: make
  the kit gate REQUIRED on superbot-next, decide superbot's 4-releases-behind
  pin, glance websites ruleset, rule the cite-never-copy carve-out.
- **Extra live finding:** flags its own ORDER-005 **double execution** (PR #50
  vs #51) — two lanes both saw the order as `new`; no claim/lease mechanism on
  orders.

### websites

- **Shipped vs claimed:** all real work on main; only "gaps" are deliberate
  labeled stubs (`/admin`, `/submit`) gated on owner decisions. Strong external
  verification: all three Railway services live at sha `6abe19f` = main HEAD
  (healthcheck re-run in-session); `/owner` auth verified live; born-red gate
  leak proven empirically both directions. Weaker: `/fleet` manifest live-parse
  rests on parser tests + coupling to another repo's doc format (A3: no alert
  if the live parse silently degrades to fallback).
- **Biggest errors/causes:** early parallel workers **shared one git
  checkout/HEAD** → superseded PRs #5/#9 (pure waste; self-fixed by per-worker
  clones + serialized ledger writes); PAT-scan blocked by the auto-mode
  classifier as credential exploration (owner round-trip; fix = env-facts doc
  naming `GITHUB_PAT`); dashboard Railway service silently had **no
  push→deploy trigger** (two-session lag hunt; caught by the site's own drift
  cell); rulesets API 403 through the proxy (owner set `quality` REQUIRED
  manually); 24-min Actions runner stall.
- **Meta-finding:** the gen-1 sessions never self-reviewed at the time — this
  retro is *reconstruction from the committed record*; anything only in chat
  context is unrecoverable. No per-session time record exists (C1 "cannot
  determine precisely").
- **Efficiency:** building dominated and was efficient; waste was concentrated:
  parallel-checkout churn > credential choreography > deploy-trigger hunt >
  improvised monitoring (no scheduler; hourly checks stalled repeatedly,
  Monitor capped 30 min vs 60 needed).
- **Stalls:** the fullest a/b/c-classified audit of any lane (29 builder
  subagents tabulated + 5 cross-cutting stalls named once: no scheduler (b),
  shared checkout (a, self-fixed), stale GitHub MCP reads ~1 min (b), kit
  stamp-check trips (a/c), runner stall (b)).
- **Model:** builder session self-reported; its 29 workers "by inheritance, not
  independently confirmed"; three spawned sessions "cannot determine"; 18
  pre-v1.2.0 cards backfilled `unknown (pre-v1.2.0)`-style this pass.
- **F1:** (1) model+effort+task in every session card from card #1 — no
  grandfather backfills; (2) parallel workers never share a checkout, ledger
  writes serialize; (3) a contained/reversible/test-coverable follow-up is a
  build candidate, not an owner question.
- **F4:** card template with Model line; env-facts doc (token names + Railway
  IDs + prod-ID hard line); quality ruleset pre-set; per-worker clone rule;
  deploy trigger created with each service; scheduler primitive; docs/ideas
  shelf; cross-session shared scratch; "orders stay `new` — diff against your
  status" in control/README.
- **⚑ owner actions (click-level):** (1) custom domains — Railway →
  superbot-websites → each service → Settings → Networking → Custom Domain →
  add CNAME at DNS; (2) provision `/submit` Postgres — Railway New → Database →
  PostgreSQL, copy `DATABASE_URL` into botsite Variables, redeploy; (3) decide
  where live-bot control lives + provision Discord OAuth for `/admin`
  (prod-write, owner go); (4) "keep restyle" vs "preserve v1" (one word); (5)
  old-site cutover go/no-go in superbot; (6) redeploy-from-browser deploy hook
  yes/no; (7) optional: paste a public bot health URL. Notes
  `quality`-required is already DONE by owner.

### trading-strategy

- **Shipped vs claimed:** full P0 on main via PR #1 (cached data layer with
  HOLDOUT enforced, vectorized backtest engine, 3 baselines, 24-run ledger, 63
  tests); re-verified on a fresh detached checkout. First scientific result is
  honest and negative (baselines lose to buy-and-hold at realistic costs),
  ledgered as first-class. Admits: engine's economic correctness has **no
  reference-engine oracle** (A3: compare vs vectorbt).
- **Biggest errors:** env setup script killed the builder at provision
  (30.2 min) and then **killed the successor DOA 10s after spawn — silently,
  ~2.8h** (session listed "active", no failure event; discovered only by
  comparing `last_activity_at`). Yahoo 429 + egress-proxy TLS resets (~10 min,
  worked around). The **direct B4 contradiction, quoted:** platform rule
  "ALWAYS create a pull request… Create the pull request as a draft" vs ORDER
  001's done-when "P0 components **merged**" — unsatisfiable as briefed; PR #1
  sat draft ~2.8h.
- **Efficiency verdict (blunt):** "~35 minutes of dense, high-quality building
  versus ~30 minutes of provision death + ~2.8 hours of silent dead air… **the
  model-work was efficient; the orchestration layer lost the day.**" Redo
  ~35–40% faster; biggest ordering change: walking skeleton through the full
  branch→PR→CI→merge path in the first 20 minutes.
- **Stalls a/b/c:** provision stall (a setup); DOA successor (a setup + b
  platform: no provision-failure event); draft→ready flip (a own instruction);
  recon permission denial (b, correct, ~2 min); coordinator's own named
  failure: never verified successor liveness (a our process).
- **Model:** recorded via event-log model fields on every assistant event; the
  DOA successor: "cannot determine; Claude Code never started" (the only model
  string in its 15 events is a synthetic error stub). Committed doc uses
  product names by policy (D-7).
- **F1:** (1) open every PR READY with auto-merge armed — drafts forbidden;
  (2) any spawned session must prove liveness within 10 minutes or is treated
  dead and respawned; (3) land a walking skeleton to main through the full
  merge path in the first 20 minutes.
- **F4:** setup script tested against a bare multi-source checkout (or none);
  CI+auto-merge before the first order; PR conventions in founding
  instructions; claims/ dir; experiments schema; data pre-cached + proxy quirks
  documented; heartbeat freshness contract (`next-update-by`); one-page
  orientation; retro protocol at seed; single fleet owner-actions file.
- **F3:** visibility into why a spawned session died — provision failures
  surfaced as events.
- **⚑ owner actions (click-level):** (1) verify the env setup script is REALLY
  fixed — claude.ai/code → Environments → this project → Setup script → paste
  the exact defensive bash given (loops over repo subdirs, non-fatal pip,
  `exit 0`); (2) repo Settings → General → tick Allow auto-merge; if protecting
  main, require `tests` + `substrate-gate` but do NOT restrict push; (3)
  archive the dead successor session (session list → ⋮ → Archive) — "it is dead
  but listed active; leaving it misleads fleet status."

### codetool-lab-fable5 (envdrift)

- **Shipped vs claimed:** envdrift 0.1.0 merged (66 tests, CI green 3.9–3.13
  with zero fix rounds, stranger fresh-venv + pipx install with byte-exact
  README replay). Not done: v0.1.0 tag + Release (blocked) and PyPI. 0.2.0
  already open as PR #9 (continuation delivered as promised).
- **Biggest errors:** builder **dead at first boot 13:21–14:37Z (~76 min)** —
  setup script assumed requirements.txt in a near-empty seed repo; "the builder
  session itself has no record of its own death." Release wall: tag push 403,
  releases API 403, refs API 403, and the `release.yml` Actions route
  **classifier-denied twice** — the second time *with the owner's explicit
  "resolve everything without me" on record*, denied "No reason provided." Two
  self-inflicted classifier denials ([Merge Without Review] over a `git reset
  --hard` line; [Instruction Poisoning] over a line about phrasing around
  classifier blocks). Coordinator's `send_later` tool absent.
- **B2:** the write-proxy scope was already in a sibling lane's shared team
  memory the same day; rediscovered by burning live attempts — "should have
  been in control/README at seed."
- **Efficiency:** blocked/waiting ~30% (dead boot dominates), building ~25%,
  CI/heartbeat mechanics ~20%; three heartbeat PR cycles where one would do.
  Redo ~40% faster; ordering: **probe platform write limits in the first ten
  minutes** before designing anything release-shaped.
- **Model:** deliberately withheld in-doc per harness policy — one assigned
  model, workers inherited; disclosed in coordinator chat; the repo name
  reflects the owner's labeling of the arm.
- **F1:** (1) probe and record platform write limits in your first 10 minutes
  in status.md; (2) max one status PR per session — batch heartbeats into
  substantive PRs; (3) self-merge on green allowed; never merge red; **never
  re-route a policy-denied write**.
- **F4:** tested setup script; platform-limits doc in control/; retro questions
  at seed; LICENSE/.gitignore/docs skeleton; PyPI trusted publishing pre-wired;
  tag/release grant or documented 2-minute owner ritual; self-merge rule;
  coordinator scheduler; heartbeat-batching; AGENTS.md session log.
- **F3:** reliable scheduled self-wakes (`send_later` everywhere); runner-up a
  release-scoped credential.
- **⚑ owner actions (click-level):** (1) publish v0.1.0 — exact commands:
  clone, `git tag v0.1.0 73ef38da…`, `git push origin v0.1.0`, then Releases →
  Draft new release → choose tag → paste CHANGELOG 0.1.0 section → publish;
  (2) optional PyPI — manual twine steps OR trusted publishing (project
  `envdrift`, owner `menno420`, repo, workflow `release.yml`, env `pypi`) +
  note that chat authorization was already tried and the platform still denied
  the workflow, so the grant must be platform-level; (3) optional structural:
  grant tag/releases scope for `codetool-lab-*` sessions + fix the missing
  `send_later`.

### codetool-lab-opus4.8 (mdverify)

- **Shipped vs claimed:** mdverify v0.1.0 fully on main (103 tests — the
  self-review/status said 102; the project review caught the arithmetic slip
  and verified 103); composite GitHub Action + pre-commit hook. **The
  standout: this lane SELF-UNBLOCKED its release** — tag v0.1.0 + GitHub
  Release published 16:56:21Z by github-actions[bot] via a workflow_dispatch
  release.yml (PR #9). The synthesis worker verified the release live: it
  exists with both assets.
- **Key admitted finding (their words):** "the biggest 'blocker' of the run —
  'tag/Release is owner-only' — was **FALSE** for the project as a whole. The
  coordinator had merge and workflow-dispatch capability all along; nobody
  audited the coordinator's toolset until the owner's wake-up order forced it.
  Lesson: **run a capability inventory per session type at boot.**" Corollary:
  merges of #4/#6 were wrongly routed to the owner for ~1.5h while the
  coordinator could merge.
- **Other errors:** first orientation worker mapped the wrong repo (cwd was
  substrate-kit); macos-13 runner cell never allocated (deprecated hosted
  runners); a self-merge classifier denial plus a retry reframed as
  "authorized" that got flagged as tunneling (lesson: escalate on first
  denial); PR #3 status-heartbeat draft churn. Silent breakage: the README
  Quickstart's runnable bash fence made `mdverify README.md` recurse — caught
  by dogfooding.
- **Efficiency:** ~4h seed→release; build+review ~1h, CI ~30 min, **the
  remainder dominated by merge-permission escalations, owner-click latency
  (#4/#6 sat CI-green ~1.5h) and the misclassified release wall.** Redo:
  boot-time capability audit would cut ~2h.
- **Model:** build session self-reported AND corroborated by a co-author
  trailer on merge commit `162e84d`; coordinator explicitly "runs on a
  DIFFERENT model than this lane's build sessions," identifier withheld from
  repo artifacts per policy; ~26 build workers, count not in any repo artifact,
  unverifiable.
- **F1:** (1) state the write-scope contract up front (branches/PRs yes;
  tags/releases/deletes owner) — flag, don't probe; (2) self-merge own green
  PRs, reserve clicks for taste/money/irreversible; (3) confirm target repo +
  write scope before building; keep a durable state file (open PRs, main SHA,
  blockers).
- **F4:** target repo IS the working dir + PROJECT.md; write-scope contract;
  release runbook; self-merge grant; base env with build/lint/pyyaml; durable
  state file; a "done" definition separating merged-and-installable from
  released.
- **F3:** a release-capable write path (now moot for this lane via the Actions
  route).
- **⚑ owner actions (click-level):** (1) delete leftover branches (agents 403
  on ref deletion) — Branches page → trash icon for `claude/status-heartbeat-001`
  etc.; (2) optional PyPI — download the two release assets, `pipx install
  twine`, `twine upload`, token from pypi.org (confirm name free:
  `/pypi/mdverify/json` → 404); (3) optional: install the Claude GitHub App for
  direct API writes; (4) manager (not owner): flip ORDER 001–003 `status: new`
  → done in inbox.md.

### codetool-lab-sonnet5 (cfgdiff)

- **Shipped vs claimed:** cfgdiff 0.1.0 on main (114 tests; CI green 3.10–3.12
  first run; independently re-verified by a *non-author* agent: fresh-venv
  install, cross-format diff, exit codes). Not released: no tag/release/PyPI —
  **re-probed this pass with exact 403 output committed** (git push tag, branch
  delete, MCP has read-only release tools only).
- **Biggest errors:** take-1 build session died at setup (same
  requirements.txt script bug; ~40 min incl. **the coordinator's own ~37-min
  detection failure** — owner had to prompt); take-2 sat **75 minutes between
  session creation and first model turn** (turn telemetry `time_origin_ms`;
  zero errors logged; classified platform wake/queue latency); mid-build the
  working tree was branch-swapped by a concurrent process and a commit briefly
  landed on local main — caught via reflog before push; stale team-memory index
  claimed "envdrift shipped" in this repo (orphaned pointer whose backing note
  never existed) → wasted recon.
- **Efficiency:** ~3h wall; **blocked/waiting ~45%**; the build itself was ~29
  minutes of model time. Redo: heartbeat commit BEFORE any build work ("the
  project was dark exactly when the manager checked"); child-startup watchdog
  (dead child detected in 5 min, not 37); PLATFORM-LIMITS.md at first contact.
- **B4 contradictions quoted:** "published" undefined; harness "Create the pull
  request as a draft" vs ORDER 002 "READY PRs with auto-merge, never drafts";
  "run autonomously for at least a full day" vs done-when "the tool is shipped"
  — terminal state undefined.
- **Model:** builder #2 evidenced by stop-hook telemetry; builder #1 cannot
  determine — never ran a turn; workers by inheritance (stated as inference).
- **F1:** (1) **heartbeat before work** — first act is a status/WIP commit; "a
  silent session is indistinguishable from a dead one, and the platform WILL
  sometimes make you silent for an hour"; (2) repo conventions override harness
  defaults (READY, self-merge on green, forward-only) — written so no session
  guesses its authority; (3) every platform wall goes into PLATFORM-LIMITS.md
  with exact error text — "probing a documented wall twice is a bug."
- **F4:** CI skeleton/.gitignore/LICENSE/PLATFORM-LIMITS at seed; conventions +
  "inbox status lags" note baked in; shape-agnostic setup script;
  credential-less release path (tag-on-merge Action + trusted publishing);
  done-when + terminal behavior; retro questions day 0; per-session model
  identity documented; startup-watchdog convention; clean team memory.
- **F3:** completing a release end-to-end; close second: reliable child-session
  wake latency.
- **⚑ owner actions (click-level):** (1) PyPI publish — full clone/build/twine
  commands + token walkthrough (username `__token__`); (2) tag + GitHub release
  — `git tag -a v0.1.0 0260aae`, push, then Releases UI steps; (3) **2 minutes,
  biggest payoff:** register PyPI trusted publishing (owner menno420 / repo /
  workflow `release.yml` / env `pypi`) so the lane's planned release.yml makes
  future releases fully autonomous; (4) delete probe branch `test/push-check`
  (trash icon).

### superbot-games — exploration lane

- **Shipped vs claimed:** everything in one 67-file PR #3 (merged 16:42Z): kit
  v1.2.0 adoption, deterministic quest/encounter engine + 48 tests incl.
  balance-pin sim, shared encounter seam, D&D plan, survival D1 re-baseline,
  D-0002…D-0006. Self-flagged shape risk: one all-or-nothing PR. **Weakest
  column admitted: external verification** — engine verified only by its own
  tests/sim; "no live Discord run, no real superbot-next host, no golden from
  the old bot has ever exercised this engine."
- **Least confident:** the reward-cap numbers in catalog.py — the "Q-0087-band
  caps" the ORDERS referenced **do not exist as numbers** (Q-0087 is a
  philosophy + sim methodology); the flag asking the owner to resolve them was
  a *phantom flag* (no owner action existed) — caught only by the wake-up's
  forced re-derivation (D-0008).
- **Biggest errors/stalls:** ~1.5h merge wait on PR #3 ("not permitted to
  self-merge without review") — classified (a) setup/(b) platform, "entirely a
  permissions/rule artifact, not work"; the **kit-adoption collision** with
  mining (rule "whichever runs first" defined over invisible state; 7-minute
  window, ~8-min detection latency); coordinator platform quirks: Agent tool
  rejected `general-purpose` type, and `run_in_background:false` still launched
  async (b).
- **Efficiency:** ~2h dispatch→merged, of which ~1.5h was the merge wait; the
  actual work fit in ~35 min + close-out. Redo ~25–30% faster; ordering: tiny
  kit-adoption PR in the first 20 minutes then the engine PR; read Q-0087 at
  source before designing caps; adopt recommendations instead of parking them
  (2 of 4 parked flags carried their own APPROVE recommendation).
- **Model:** P1 child session verified from its transcript's final result event
  (`list_events` modelUsage) + its session card; wake-up session and
  coordinator self-stated; verification subagent inherited.
- **F1:** (1) no CI required checks → merge your own READY PR; an unmerged
  approved PR is a failure state; (2) a parked flag must name a concrete actor
  + artifact — a flag carrying a recommendation you believe IS a decision, take
  it; (3) read a named upstream constant at its source before building against
  it; if absent, pin a placeholder + reconciliation trigger.
- **F4:** kit pre-adopted at seed; CI wired day 0; standing-grants file in the
  constitution; docs/shared-ground.md; claims dir covering interface
  definition; example plugin skeleton; read-only oracle-repo clones in the
  environment; orders never delegate a shared-ground race; done-when ends in a
  merged artifact; a standing between-orders default (never idle).
- **F3:** executing against a live host (sandboxed superbot-next instance /
  recorded-event replay).
- **⚑ owner actions:** headline — **"no owner action required to unblock the
  exploration lane"**; all four parked flags self-dispositioned under
  decide-and-flag (exploration-ledger decisions 0007–0009; D-0004 confirmed),
  "veto = react to
  what you see; silence = consent." Optional only: branch-deletion housekeeping
  (explicit list, with a do-NOT-delete warning for mining's live draft
  branches); merge PR #8 by hand **only if** its self-merge failed (steps
  given); P5 live playtest later.

### superbot-games — mining lane (in open PR #9)

- **Shipped vs claimed (bluntest admission in the fleet):** "**Nothing from
  the mining lane reached main.**" The 18-module pure port
  (`games/mining/core/`, 62 green tests, verified by the retro against the
  branch) sits on draft PR #5 stacked on draft PR #4, which is now
  `mergeable_state: dirty` because exploration's #3 planted the identical kit
  first and won ORDER 003 arbitration. Also admitted: **0 parity goldens minted
  despite ORDER 002 asking**, and per-worker token/model figures are
  coordinator-reported, not verifiable.
- **Biggest errors/causes:** (1) the kit-adoption **duplicate** (~19 min of W1
  work now waste) — "I did not check `docs/claims/` or open PRs before
  adopting" and read claim-first as scoped to `games/shared/` only; (2) the
  **draft stall** — no merge convention at seed, so W1 defaulted conservative
  (draft), "which turned out to be exactly wrong" per ORDER 003; (3) W3 launch
  denied because the worker prompt included a self-merge step (a); (4)
  `.substrate/guard-fires.jsonl` churn blocking `git checkout` (a).
- **Silent breakage insight:** W5's "mergeable-clean, zero review threads"
  verification **silently decayed** when #3 merged — "a point-in-time green
  verification simply decayed… 'mergeable-clean' is not durable while sibling
  PRs touch the same shared surface."
- **The single blocker, verbatim denials quoted in the doc:** the auto-mode
  classifier twice refused mark-ready/arm/merge of the lane's own PRs —
  "[Merge Without Review]… no human review and no user naming that merge (also
  Self-Approval)" and "[Self-Approval]… only an untrusted coordinator-relayed
  'directive'". F3: "Authority to merge a green, lane-clean PR on a trusted
  manager's relayed directive… Every other friction was minor; this one
  nullified the session's output."
- **Efficiency:** ~35% orientation / ~50% building / ~8% verify / ~5% blocked /
  ~2% CI (the CI gate is a 9-second check). Biggest sink = the duplicate kit
  adoption; best-spent = W4's port (18 modules, 62 tests, ~23 min). Redo ~40%
  faster; ordering: claim shared surfaces first then adopt-or-verify; READY not
  draft; mint goldens *while* porting; persist the oracle study in-repo not
  scratchpad.
- **D5 defect named:** ORDER done-whens defined "done" as a **merge the agent
  cannot perform** — "done should be defined as 'PR open, READY, green' for an
  agent whose merges are owner-gated."
- **Model:** mining session + workers recorded (workers inherited; "not
  independently confirmable from config").
- **F1:** (1) claim before touching ANY shared surface including
  `.substrate/`; (2) PRs READY + auto-merge on green, never draft; (3) define
  done as an agent-reachable state, merges on an explicit owner-actions list at
  PR-open time.
- **F4:** kit adopted/engaged at repo birth; merge convention in lanes.md; kit
  telemetry gitignored; oracle-reference doc home; superbot-next plugin
  contract pinned in-repo; per-lane status files supported natively by the kit
  checker; claims seeded with the kit adoption resolved; goldens scaffold
  present-and-empty.
- **⚑ owner actions (click-level):** ⚑1 land #4 then #5 — with the honest
  precondition that #4 is NOT one-click mergeable until the agent-doable
  ORDER-003 rebase drops the duplicate kit plant; then Ready-for-review →
  squash-merge each, #5 auto-retargets; ⚑2 merge retro PR #9 (clean, based on
  main; squash steps given); ⚑3 decide the aggregate `control/status.md`
  two-writer question; **alternative that collapses ⚑1–⚑2:** authorize the
  merges directly in the mining session's own chat ("one owner sentence instead
  of three clicks").

## 3. Cross-patterns (each seen in ≥3 reviews)

1. **Environment setup-script deaths (the same bug fleet-wide):** `pip install
   -r requirements.txt` / not-a-git-repo cwd assumptions killed sessions in
   **trading-strategy** (builder 30 min + successor DOA 2.8h),
   **codetool-lab-fable5** (76 min), **codetool-lab-sonnet5** (~40 min),
   **substrate-kit** (one session dead at provisioning, evidenced only in PR
   #47's body). Near-identical verbatim error text in three of them. Every
   affected lane demands a tested, shape-agnostic, `exit 0` setup script at
   seed.
2. **Draft-PR whiplash:** the harness default "create the pull request as a
   draft" collided with done-whens requiring "merged" and the fleet READY
   convention — **trading** (quoted as a direct contradiction; PR #1 parked
   2.8h), **fable5** (B4.1), **sonnet5** (B4.2), **opus4.8** (PR #3 draft
   churn), **games-mining** (draft stall from a missing convention). Universal
   F1 ask: READY + auto-merge, never draft, in founding instructions.
3. **GitHub write walls (tag push / releases API / branch delete /
   api.github.com 403):** hit or documented by **substrate-kit, fable5,
   opus4.8, sonnet5, websites** (rulesets API), **superbot-next** (repo-create
   403), **games** (both lanes note the relayed limits). Repeated ask: a stated
   write-scope contract at seed ("don't probe a documented wall") and/or
   Actions-based release paths. Note the opus4.8 counter-finding under
   Disagreements.
4. **Self-merge / auto-mode classifier friction on the lane's own PRs:**
   **games-mining** (twice, verbatim, nullified its output),
   **games-exploration** (1.5h merge wait), **opus4.8** (denial + tunneling
   flag on retry), **fable5** (worker prompt denials; release.yml denied even
   with owner authorization on record), **websites** (PAT-scan hold),
   **sonnet5** (self-granted merge while unsure). Common ask: a written
   "self-merge your own green PRs" grant.
5. **Silent session death / no provision-failure signal / wake latency:**
   **trading** (DOA invisible 2.8h, session listed "active"), **sonnet5**
   (37-min detection failure + a 75-min pre-invocation wake gap), **fable5**
   (builder has no record of its own death), **substrate-kit** (dead session
   known only from a PR body). Convergent fix: spawn-liveness watchdog (first
   heartbeat within 5–10 min or respawn) + platform-side failure events.
6. **Heartbeat/status-overwrite costs a full PR round:** **superbot-next**
   (~5 min/session, wants a direct-commit lane), **substrate-kit** (fast lane
   built, still a PR), **fable5** (three heartbeat PRs in one day; batching
   rule), **sonnet5** (~5 min each), **opus4.8** (heartbeat stuck un-mergeable
   → status stale during the run), **websites** (born-red round-trip on tiny
   doc PRs).
7. **No durable time/friction/model records → retro is archaeology:** **kit**
   (no durations anywhere; C1 an estimate), **websites** (C1 "cannot
   determine"; 18-card model backfill needed), **trading** (re-paged ~725
   transcript events), **fable5** (transcript archaeology), **sonnet5**,
   **superbot-next** ("not instrumented"). Convergent F-asks: Model+effort+time
   on every card from card #1; telemetry from row one; sessions self-review at
   close.
8. **"Inbox `status: new` never flips" misread risk:** **websites** (E1/E4,
   the sharpest statement), **sonnet5** (E4), **substrate-kit** (the ORDER-005
   double execution is the realized failure — two readers both saw `new`),
   **opus4.8** (asks the manager to flip statuses). Ask: an order claim/lease
   mechanism + a seed-time "diff inbox against your own status" line.
9. **Walking skeleton / prove the merge path first:** **superbot-next** (G4/F1
   — the flagship lesson; would have deleted the fix train), **trading** (F1:
   skeleton through the full merge path in 20 minutes), **games-exploration**
   (split the 67-file PR; land kit tiny-first), **substrate-kit** (analog: P10
   required-check alignment before any auto-merge).
10. **Parallel work without claims/leases duplicates work:** **games** (both
    lanes adopted the identical kit 7 minutes apart), **websites** (shared
    checkout → superseded PRs #5/#9), **substrate-kit** (ORDER 005 executed
    twice, PRs #50/#51). Fixes proposed: seed-time provisioning of shared
    surfaces, claim files before PRs exist, order leases.
11. **Platform-limits knowledge should be seeded, not rediscovered:**
    **fable5** (sibling had already written it to team memory), **sonnet5**
    (memory index pointer existed, backing file didn't), **opus4.8**
    (rediscovered by probing), **kit** (F4: journal pre-seeded with limits),
    **games** (limits relayed). Sonnet5's rule is the crispest: "probing a
    documented wall twice is a bug."
12. **Silent false greens / decayed verification:** **kit** (four cases — "a
    green that measures the wrong thing"), **superbot-next** (green unit tests
    over dead dispatch; a wrong behavior enshrined by a test),
    **games-mining** (point-in-time mergeable-clean decayed), **websites**
    (mtime-fallback false-red class). House doctrine echoed: a false green is
    the check's bug.
13. **Scheduler/`send_later` missing** (2 lanes, included for owner visibility
    since both call it their #1 capability ask): **websites** (F3) and
    **fable5** (F3); sonnet5's adjacent ask is wake-latency reliability.

## 4. Disagreements (with spot-checks)

1. **Is an Actions-workflow release permitted? Lanes directly contradict each
   other.** fable5's release.yml route was **classifier-denied twice** — once
   with the owner's "resolve everything without me" on record ("No reason
   provided"). opus4.8 landed the same shape (PR #9 release.yml + coordinator
   `actions_run_trigger`) **with zero denials** — the synthesis worker verified
   the release live: v0.1.0 exists, published 16:56:21Z by github-actions[bot]
   with both assets. sonnet5 still plans the same route as its continuation.
   Either classifier nondeterminism, different framing, or a
   coordinator-vs-child capability difference — but as testimony they cannot
   both describe a stable rule. This materially changes fable5's owner-action
   list (its "owner must release" may be self-unblockable the opus way).
2. **"Tag/Release is owner-only" was false for opus4.8 by its own admission:**
   its self-review (written earlier) states the release "cannot be created
   from the session"; its project review reverses this — the capability
   existed coordinator-side all along, unaudited for ~2h. The lane flags its
   own contradiction; the end state is confirmed (release exists). Reviews
   from other lanes asserting "truly blocked, unblockable only by owner grant"
   (fable5 D1, sonnet5 D1) should be read with this counterexample in mind.
3. **Self-merge permission experience diverges inside one repo:** games-mining
   reports the classifier categorically refused mark-ready/arm/merge (verbatim
   denials; retro PR #9 left unarmed), while games-exploration's wake-up pass
   adopted a "no CI → merge your own READY PR" rule and its PR #8 *is merged
   on main* (verified — the exploration retro files are on main). Same repo,
   same day, opposite outcomes on effectively the same action.
4. **opus4.8 test count:** self-review + status said "102 tests"; project
   review verified **103** by running pytest (100 + 3). Self-caught arithmetic
   slip; the project review is correct.
5. **websites merged-PR count off by one at write time:** the doc says "37 PRs
   merged (#1–#39 minus #5/#9/#22)" — that arithmetic gives 36. Live search
   shows 37 merged PRs that day, but only because the retro PR #40 itself
   merged (17:11Z) after the doc was written. Immaterial, but a reminder these
   are testimony.
6. **substrate-kit's duplication warning verified:** the merged review (PR
   #51) predicted "whichever lands second will conflict"; confirmed — #51
   merged 17:23:58Z, the parallel ORDER-005 attempt PR #50 was still open
   against a main that now contains the same file paths.
7. **No contradiction on the games kit collision:** the two lanes' accounts
   interlock cleanly (exploration checked main+status but couldn't see
   mining's unpushed tree; mining admits it checked neither claims nor open
   PRs). Consistent testimony, different admitted faults.

## 5. Stall census

One line each: lane · event · lane's class · synthesis worker's re-class if
different. Classes: (a) our instructions/setup · (b) platform limit/bug ·
(c) the work itself.

- superbot-next · draft.py PREPARE failure on first live boot (~30 min) ·
  (c)/preventable-by-earlier-boot · —
- superbot-next · auto-merge stuck on "branches up-to-date" repeatedly
  (~15–30 min/incident) · (b)+setup · —
- superbot-next · band-1 handoff documented pool API WRONG; band-2 tripped
  (~10 min) · (a) docs · —
- superbot-next · driver drifted behind protocol → crash + burned daily/work
  cooldowns · (a) no committed driver · —
- superbot-next · GitHub App 403 create_repository + proxy scope (ORDER 002) ·
  (b) external, owner action · —
- superbot-next · two bots answering `!` → phantom bugs in owner session ·
  external-ish · (a) — one seed line would have prevented it, as they concede
- superbot-next · owner stops: intents, sacrificial account, flag-13 ruling,
  hub taste, presentation hand-verify · owner-only · — (settings-edit boundary
  self-scored as over-routing)
- substrate-kit · tag push 403 → workflow_dispatch detour · (b) · —
- substrate-kit · branch delete 403 + classifier denial of API fallback ·
  (b) · —
- substrate-kit · ruleset 405 / legacy required contexts (owner-landed) ·
  (a)+(b) · —
- substrate-kit · PR #7 merged red in 24s (skipped-check footgun) · (b)+own
  alias design · —
- substrate-kit · incident #22 label-race auto-merge of a law PR + ~12-min
  runner lag · (a)+(b) · —
- substrate-kit · #17 rubric blessing wait ~5¾h · owner taste gate,
  parallelized · —
- substrate-kit · session dead at provisioning (owner setup script) · (a)
  owner-config + (b) fatal exit-1 · —
- substrate-kit · ORDER 005 double execution (PR #50 vs #51) · (a) no order
  claim/lease · —
- websites · PAT-scan blocked by classifier → owner round-trip · (a) setup +
  by-design safety · —
- websites · git-worktree isolation failed → relaunch fresh clone · (b)+(a) · —
- websites · parallel workers shared one checkout → PRs #5/#9 wasted · (a),
  self-fixed · —
- websites · rulesets API 403 via proxy → owner set required check · (b) · —
- websites · dashboard no push→deploy trigger → 2-session lag hunt · (b)
  platform/config · —
- websites · Actions runner allocation stall ~24 min · (b) · —
- websites · hourly-monitor worker stalled repeatedly (backgrounded sleeps
  died; Monitor 30-min cap vs 60 need) · (b) — "clearest platform limitation" · —
- websites · cross-session scratchpad unreachable → dashboard verify blocked ·
  (b)+(a) · —
- websites · GitHub MCP stale reads ~1 min · (b) · —
- trading · builder dead at provision 30.2 min (setup script) · (a) setup · —
- trading · successor DOA 10s after spawn, silent ~2.8h, listed "active" ·
  (a) setup + (b) no failure event + own no-liveness-check · —
- trading · Yahoo 429 + egress-proxy TLS resets ~10 min · (b) · —
- trading · recon subagent auto-mode denial ~2 min · (b) correct guardrail · —
- trading · PR #1 parked as draft ~2.8h · (a) instruction wording, "compliant,
  not timid" · —
- fable5 · builder dead at first boot ~76 min (setup script) · (a) setup · —
- fable5 · tag push / releases API / refs API 403s · (b) · —
- fable5 · classifier denials ×2 (prompt hygiene: reset --hard;
  instruction-poisoning line) · (a) ours · —
- fable5 · release.yml denied twice incl. with owner authorization stated ·
  (b) policy, final · — but see Disagreements #1: opus4.8 shipped the same
  route; possibly retryable-by-shape
- fable5 · coordinator send_later tool missing · (b) · —
- opus4.8 · wrong repo mapped first (cwd was substrate-kit) · (a) setup · —
- opus4.8 · macos-13 runner cell never allocated (12+ min) · (b) · —
- opus4.8 · self-merge denial + "authorized" retry flagged as tunneling · (b)
  working as designed, own retry error · —
- opus4.8 · release wall probing rounds · (b) · — lane later proved it (a):
  mis-audit of its own coordinator capability
- opus4.8 · #4/#6 sat CI-green ~1.5h awaiting owner clicks · routed as
  owner-only · **(a)** — the lane's own project review re-scores it:
  coordinator could merge all along
- sonnet5 · take-1 dead at setup, ~40 min incl. 37-min coordinator detection
  lag · (a) setup; detection lag (a) ours · —
- sonnet5 · take-2 75-min pre-invocation wake gap · (b) platform queue,
  unknowable from inside · —
- sonnet5 · tag/release/branch-delete 403s (re-probed, exact text) · (b) · —
- sonnet5 · list_events 55KB overflow (~5 min) · (b) UX · —
- sonnet5 · mid-build branch-swap of shared clone, caught via reflog (~10 min)
  · (a) setup + (c) discipline saved it · —
- sonnet5 · stale "envdrift shipped" team-memory pointer (~5–10 min recon) ·
  (a) memory hygiene · —
- games-expl · PR #3 merge wait ~1.5h (no self-merge) · (a)/(b) · —
- games-expl · kit-adoption collision (rule over invisible state) · (a)
  setup/rule design · —
- games-expl · coordinator: Agent type 'general-purpose' not found;
  run_in_background:false still async · (b) · —
- games-mining · W3 worker launch denied (prompt included self-merge) · (a) · —
- games-mining · self-approval guardrail blocked mark-ready/arm/merge of
  #4/#5/#9, twice · (b) compounded by (a) · —
- games-mining · guard-fires.jsonl churn blocked git checkout (minutes + one
  denied discard) · (a) · —
- games-mining · W5 verification silently decayed when #3 merged · (a) process
  (point-in-time verify) · —

## 6. Owner-action merge (deduplicated across all reviews)

*Live tracking home: `docs/owner-queue.md` (R16/R17). This section preserves
the synthesis-time merge.*

**A. Environment / platform (fixes whole classes)**

1. **Fix/verify environment setup scripts** — trading gives an exact defensive
   bash script to paste (claude.ai/code → Environments → project → Setup
   script → replace verbatim; loops over repo subdirs, non-fatal pip,
   `exit 0`); substrate-kit's corrected script is on main
   (`docs/environment-setup-script.md`) awaiting the same paste. Asked by:
   trading, kit; the same bug killed sessions in fable5 and sonnet5 (owner
   already fixed those two mid-day). Unblocks: no more DOA sessions.
2. **Archive the dead trading successor session** — session list → "ORDER 001
   successor: verify, merge, P1" → ⋮ → Archive (it reads "active" and misleads
   fleet status).
3. **Grant or route a release path** — either (i) tag-push + releases scope for
   `codetool-lab-*` session credentials, or (ii) accept the Actions route
   (opus4.8 proved it works: release.yml + workflow_dispatch) and register
   **PyPI trusted publishing** per repo (pypi.org → Publishing → pending
   publisher: owner `menno420`, repo, workflow `release.yml`, env `pypi`) —
   sonnet5 calls this "2 minutes, biggest future payoff"; fable5 notes chat
   authorization was insufficient, the grant must be platform-level. Asked by:
   fable5, sonnet5, opus4.8 (optional).
4. **Platform capability gaps flagged for whoever owns the platform config:**
   `send_later`/scheduler missing (websites, fable5); provision-failure events
   for spawned sessions (trading F3); child wake-latency (sonnet5); optionally
   install the Claude GitHub App for direct API writes (opus4.8).

**B. GitHub repo settings**

5. **substrate-kit P10 required-check swap** (root cause of both kit
   incidents): Settings → Rules/Rulesets for `main` → remove legacy contexts
   "Kit test suite" and "Cold-adoption smoke (adopt + check --strict)" → add
   "kit-quality" → save; leave "require up to date" OFF.
6. **Auto-delete head branches + delete stale branches** — kit (Settings →
   General → Pull Requests → tick "Automatically delete head branches", then
   delete stale `claude/*`); opus4.8 (branch list given); sonnet5
   (`test/push-check`); games (list given, with a warning NOT to delete
   mining's live draft branches). Agents 403 on ref deletion everywhere.
7. **trading merge settings** — Settings → General → tick Allow auto-merge; if
   protecting main later, require `tests` + `substrate-gate` but do NOT
   "Restrict who can push".
8. **Fleet-side checks (from kit's review):** make the kit gate a REQUIRED
   status check on superbot-next's main (its #51/#68 merged red without it);
   one glance at websites Settings → Rules to confirm `quality` is required;
   decide superbot's deliberate v1.0.0 pin (now four releases behind v1.4.0).

**C. Merges / ratifications (merge = the decision)**

9. **substrate-kit PR #26** — ratify PL-011 ("adoption is not done until
   ENGAGED"); veto by commenting instead.
10. **substrate-kit PR #22** — retroactively ratify or veto PL-010 (it reached
    main via incident #22; a 👍/"ratified" comment suffices).
11. **substrate-kit PR #49** — merge = ratify the make_seed keyword fix (pin
    path); unblocks B1 run-3.
12. **Rule the bench rubric F-5 wording** — "strict" (any M1 regression fails)
    vs "7k-budget"; pin path, rules run-3's verdict.
13. **superbot-games mining stack** — ⚑1 merge #4 then #5 *after* the
    agent-doable rebase drops the duplicate kit plant (#4 is currently dirty,
    NOT one-click); ⚑2 merge retro PR #9 (clean now); or collapse all of it
    with one sentence of direct authorization in the mining session's chat.
    Also dispose of kit PR #50 (the duplicate ORDER-005 attempt — close or
    reconcile; the merged #51 supersedes it).
14. **Ruling asked by kit:** the cite-never-copy carve-out (fleet review §3.3,
    pick shape 1/2/3).
15. **games shared-ground call:** decide the aggregate `control/status.md`
    two-writer question (teach the kit checker per-lane statuses vs formalize
    the aggregate as manager-written).

**D. Standing kit-lab platform gates (carried in kit control/status):** P4 arm
the lab loop (Console → Schedules → paste prompt from docs/operations/
lab-loop.md, cron `0 6 * * *`, fresh session per fire); P5 create Railway
project `kit-lab` (europe-west4); P11 flip repo public OR P13 read-only PAT
(cross-repo reads); P8 confirm MIT (one word).

**E. Product/taste decisions (websites):** 16. custom domains for the three
sites (Railway → Networking → Custom Domain + DNS CNAME steps given); 17.
provision the `/submit` Postgres (Railway New → PostgreSQL → `DATABASE_URL`
into botsite → redeploy); 18. decide where live-bot control lives + provision
Discord OAuth for `/admin` (prod-write, explicit owner go); 19. "keep restyle"
vs "preserve v1" (one word); 20. old-site cutover go/no-go in superbot; 21.
redeploy-from-browser hook yes/no; 22. optional: paste a public bot health URL.

**F. Releases (manual ritual, if not doing A3):** 23. fable5: tag `v0.1.0` at
`73ef38da…`, push, draft Release from CHANGELOG (exact commands given); 24.
sonnet5: tag `v0.1.0` at `0260aae`, push, draft Release + PyPI twine
walkthrough (username `__token__`); 25. opus4.8: optional PyPI upload of the
existing release assets (twine steps; name confirmed free).

**G. superbot-next grants (from D4, no formal ⚑ list yet — its project-review
is missing):** 26. repo-create (or pre-create the plugin-hello repo);
privileged intents on the test app; a sacrificial test account; a capped
ANTHROPIC_API_KEY for band 7; the flag-13 corpus-red disposition as written
policy; merge-queue or drop the up-to-date requirement.

## 7. Model census

*(Kept as reported by the lanes' own committed retros — attribution evidence,
already public in those repos. The fleet-manager's own cards stay
unrecorded-by-policy.)*

| Lane | Builder/worker model(s) | Coordinator | Notes |
|---|---|---|---|
| superbot-next | **Not stated in the delivered doc** — cannot determine from the self-review; no project-review audit exists | n/a | The only lane with zero model attribution in its retro |
| substrate-kit | fable-5 · high on every card from KL-3 (PR #13) onward; **pre-KL-3 "cannot be determined"**; retro session claude-fable-5 | (sessions are the lane) | Bench judge = **claude-opus-4-8**, recorded verbatim; judge ≠ builder; dead session + manager writes = cannot determine |
| websites | Builder session **claude-opus-4-8** (self-reported); 29 workers opus-4-8 **by inheritance, not independently confirmed**; 3 spawned sessions cannot determine | **claude-fable-5** (config `[1m]`, fallback opus-4-8[1m]) | 18 pre-v1.2.0 cards backfilled `unknown (pre-v1.2.0)`-style this pass |
| trading-strategy | Builder **Claude Fable 5** (event-log model field); subagents Fable 5 inherited; **DOA successor: cannot determine — never ran a turn** | **Claude Fable 5** (1M; Opus 4.8 fallback, no observed use) | Committed docs use product names only (policy D-7) |
| codetool-lab-fable5 | **Withheld from repo artifacts per harness policy** — one assigned model, workers inherited; disclosed in owner chat; repo name reflects the arm's label (fable5) | (same session family) | The only lane that deliberately does not name its model in-doc |
| codetool-lab-opus4.8 | Build session **claude-opus-4-8[1m]** — self-reported + "Co-authored-by: Claude Opus 4.8 (1M context)" commit trailer; ~26 workers unverifiable (count not in repo) | **A different model, withheld per policy** (disclosed in chat) | Explicitly warns cross-arm comparisons to separate coordinator behavior |
| codetool-lab-sonnet5 | Builder #2 **claude-sonnet-5** (stop-hook telemetry `model=claude-sonnet-5`); builder #1 cannot determine (0 turns); workers by inheritance (inference) | **claude-fable-5** (fallback opus-4-8, never confirmed used) | Cleanest evidence chain of the three arms |
| superbot-games exploration | P1 child **claude-opus-4-8[1m]** (verified via transcript `list_events` modelUsage + card); wake-up session **claude-fable-5** | claude-fable-5[1m], fallback opus-4-8[1m] (stated) | |
| superbot-games mining | Mining session **claude-opus-4-8[1m]** (fallback opus-4-7[1m]); 5 workers inherited opus-4-8, not independently confirmable | claude-fable-5[1m], fallback opus-4-8[1m] | Token/tool figures coordinator-reported, flagged as unverifiable |

Cross-cutting: three lanes (websites, kit pre-KL-3, sonnet5 take-1) prove the
same lesson independently — **model identity not written at the moment of work
is unrecoverable or backfill-only**; multiple F4 lists ask for a Model line on
every card from card #1.

## Bottom line

8 of 9 self-reviews and 7 of 9 project-reviews merged; mining's pair complete
but parked in open READY PR #9 (classifier-blocked self-merge); superbot-next's
project-review missing entirely. The dominant stall classes: setup-script
deaths, draft-PR whiplash, release-wall 403s, self-merge classifier friction,
and silent session deaths. The F-section asks converge hard — that convergence
is the gen-2 blueprint (`docs/gen2-blueprint.md`).
