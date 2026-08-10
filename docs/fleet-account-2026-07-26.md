# The fleet, as the record tells it — 2026-07-26

> **Status:** `historical`
>
> **Historical snapshot:** this is the owner-reviewed account as of 2026-07-26.
> It is read once for history and is never a source for live repo state, current
> owner asks, or the next action. Use [`current-state.md`](current-state.md) and
> the [consolidation program](planning/2026-07-26-consolidation-program.md) for
> those. The dated body is preserved rather than rewritten.
>
> **Purpose:** the owner asked for a full read-back of what the repositories'
> documentation says happened over the program, so he can diff it against what
> he knows actually happened. The fleet was built almost entirely by autonomous
> sessions with the owner directing at arm's length — **the documentation is the
> only shared memory**, and it may contain agent-written distortions. This doc
> therefore (a) cites everything, (b) keeps "the record claims" separate from
> "verified live tonight", (c) surfaces contradictions found between records,
> and (d) ends with what the record cannot answer.
>
> **Sources actually read for this account** (not skimmed lists — read):
> fm `docs/eap-story.md` (whole program narrative) · `docs/eap-retrospective.md` ·
> `docs/PROJECT-CLOSEOUT.md` · `docs/owner-reflection-2026-07-21.md` ·
> `docs/owner-queue.md` · `docs/current-state.md` · `docs/NEXT-TASKS.md` ·
> `docs/fleet-triage.md` (register + restructure) · `docs/playbook.md` ·
> `CONSTITUTION.md` · `docs/collaboration-model.md` · `docs/owner-profile.md` ·
> `docs/RESUME.md` · `docs/findings/fleet-economics-2026-07.md` ·
> `docs/findings/2026-07-22-pat-and-automode-capabilities.md` ·
> `control/inbox.md` ORDER index · superbot `docs/owner/maintainer-question-router.md`
> (all 278 ruling headers + key bodies) · superbot `docs/owner/fleet-grounding.md` ·
> superbot `docs/owner/fleet-8seat-structure-2026-07-11.md` · superbot
> `docs/current-state.md` · the `PROJECT-CLOSEOUT.md` of **all 11 repos that have
> one** · sim-lab `control/status.md` (its closeout-equivalent) · shiftlife
> `docs/current-state.md` + `docs/plan-conformance.md` · plus fresh shallow
> clones of **all 21 sibling repos** and live GitHub/Railway probes tonight.

---

## 1 · The timeline, as recorded

### Pre-history (2025-08 → 2026-06)
- `superbot` first commit **2025-08-10**; ~9 months dormant; **revived
  2026-05-13 on Claude Code web** — PR #10 is the first `claude/`-branch merge
  (eap-story §1). The premise from that day: agents run the project, the
  non-coder owner steers.
- **June 2026 — the substrate is invented inside superbot** as reactions to
  specific failures, each with an owner ruling: session journal (06-05), session
  cards (06-07), PR-every-session (Q-0052), auto-merge enabler (Q-0123, built
  after a forgotten manual merge), **born-red session cards** (Q-0133, built
  after auto-merge landed a partial PR), friction→guard law (Q-0194), false-green
  doctrine (Q-0120), never-wait rebuild autonomy (Q-0241),
  understand-and-reflect (Q-0254). The owner-decision register reaches **278
  rulings** (superbot `docs/owner/maintainer-question-router.md`).

### The EAP (2026-07-07 → 07-14), extended to 07-21
- **07-07** kickoff ("second mandate" — the record itself says the first mandate
  predates the evaluation journal and cannot be reconstructed). First-night
  verdict: coordinator tier amputated, worker tier superb.
- **07-08 unlock day:** the 11-test permission probe; the **Contents-API
  bootstrap discovery** that let agents create repo content prompt-free;
  substrate-kit and superbot-next founded the same day; the 14-hour rebuild
  (49 PRs, 18 sequential workers, "zero rework").
- **07-09 the explosion** — densest day: fleet-manager, websites (46 PRs day
  one), trading-strategy, superbot-games founded; the three codetool model-
  comparison arms ran (envdrift/mdverify/cfgdiff — mdverify **falsified the
  "release wall"** by shipping `release.yml` + dispatching it); GBA toolchain
  proven in-container; gen-1 wound down the same day with an adversarial audit
  (21/21 incidents verified, zero fabrication).
- **07-10 gen-2:** owner screen-recording **falsified the "agents can't self-arm
  routines" wall**; round-3 fan-out to ~10 Projects (idea-engine, sim-lab,
  product-forge, superbot-idle, venture-lab, gba, pokemon); the **Q-0264
  pipeline** (idea-engine → sim-lab → manager → lanes); **Q-0266 volume-first**
  ("maximize output at creation, **consolidate later**" — today's consolidation
  is that ruling's planned second phase); R22 born from the **pokemon-mod-lab
  public-exposure incident** (declared PRIVATE while world-readable with
  vendored Nintendo source; owner flipped it private); R23 born from
  venture-lab's Stripe false-green.
- **07-11:** owner decision **Option A custodian-primary** — fleet-manager
  becomes records custodian; the generated roster supersedes superbot's
  hand-kept manifest (measured ~33.5h stale, 9/10 rows wrong); **the owner
  restructures to 8 standing Projects** (superbot
  `docs/owner/fleet-8seat-structure-2026-07-11.md`); continuous mode Q-0265;
  substrate-kit ships **102 merged PRs in ~24h**; mineverse founded 01:20Z →
  full staged product in one day (39 PRs).
- **07-12:** the trigger-scheduler incident (9 dropped one-shots, 2 wedged
  crons, two seats dark ~6h) → R26 watchdog; **first revenue** — Stripe Webhook
  Test Kit **live at $29 on Gumroad**, buyer path verified by the owner's test
  purchase, kill clocks armed T+7/T+14; Codex fabrication incidents #1–#3 →
  sim-lab **VERDICT 016 authenticity gate** (3/3 fabrications caught, 0/24
  false alarms); the owner's Q-0269/0270/0271/0272/0273 autonomy directives.
- **07-13/14:** first fully-doctrined unsupervised night (~190–276 PRs,
  three independent counts, none identical, all committed); superbot-next
  reaches **full-corpus parity** (484/484 → later 533/533); ORDER 045 final
  worklists; **the free window closes 07-14**; the owner extends to **07-21**.
- **07-15 → 07-21 (the extension week):** v3.5/v3.6 prompt registry; the owner's
  morning close-out click-sweeps (07-17); the **classifier-scare correction**
  (07-18: "agents CAN merge their own green PRs" — the mid-July merge-wall
  belief was wrong and each session had copied and amplified it; superbot
  `docs/current-state.md` banner); **superbot FROZEN as behavioral oracle**
  (07-17, same banner); liveness/label/R30 checkers built (07-18/19);
  idea-engine/sim-lab pivot to a self-sustaining generate-and-verify loop;
  **07-21: program close** — every seat writes `docs/PROJECT-CLOSEOUT.md`, the
  owner-reflection is written, sessions go **read-only 2026-07-22T00:00Z**.

### Post-close (07-22 → today)
- **07-22:** live owner session verifies the **post-close access model**: Claude
  GitHub App for read/PR work; the fine-grained **account PAT (admin on every
  repo) over direct egress** as the owner-provisioned path for admin operations
  (fm `docs/findings/2026-07-22-pat-and-automode-capabilities.md`).
- **07-23:** owner-live session lands **phone-controller** v0.4.0 (owner
  playtest: pairing ✓ keyboard ✓ GBA-emulator ✓ gamepad ✓).
- **07-24:** owner pastes market research → the **ShiftLife plan** (fm
  `docs/planning/2026-07-24-app-plan-life-admin.md`); owner **GO** same day;
  `shiftlife` repo created; phone-controller ships v0.6.0→v0.17.0 (14 signed
  APK releases exist).
- **07-25/26:** ShiftLife sync plan completes (5/5 slices, live-proven
  two-device flow); plan-conformance ledger built after the "ten drifted
  slices" audit; **shiftlife is committing today** (latest commit 18:39Z
  tonight). fm #540/#541/#543 land the consolidation plans (this branch).

---

## 2 · The operating system the fleet ran on (still partly live)

- **The kit** (`substrate-kit`, 26 releases → v1.20.2): vendored `bootstrap.py`
  + `.substrate/`; born-red session cards; `check --strict` gate;
  capability/routine ledgers; rendered CLAUDE.md. **Program law** lives in the
  kit (`docs/program/rulings.md`, PL-register) — cite, never copy.
- **The control bus** (`control/` per repo): owner-written `inbox.md` ORDERs →
  seat `status.md` heartbeats → `outbox.md` cross-repo requests. **Retired as
  live machinery at close; historical record now.**
- **The records custody** (this repo): generated `docs/roster.md` (regen every
  ~2h by Actions — still firing), `docs/owner-queue.md` (stable OQ-slugs),
  `docs/fleet-triage.md`, `docs/evidence-index.md`, the v3 prompt registry
  (`docs/prompts/v3/` — the paste artifacts that founded/closed every seat).
- **Landing machinery:** born-red card holds PR red → flip on last commit →
  `substrate-gate` green → auto-merge/`merge-on-green` lands it. **This is still
  what lands PRs in fm today** (used by #540/#541/#543 tonight).
- **Two scheduler layers, distinct:** claude.ai Routines (failsafe crons +
  send_later pacemakers — the seat wake system) vs **GitHub Actions crons**
  (roster-regen, bakes, merge-on-green polls). The first is the one the closers
  were supposed to wipe; the second is what still runs ~397 runs/day.

---

## 3 · Repo by repo — what the record says each is, and its terminal state

**Live/active (4):**

| Repo | What the record says | Verified tonight |
|---|---|---|
| `shiftlife` | App #1 on the Personal Operations Core; free-forever charter as product law (`PRODUCT.md`); 7/8 free-core items done, reminders **half** (decision layer tested, **delivery never fired** — needs device + Expo token); sync 5/5 live-proven; CI recovered 07-25 | Committing **today 18:39Z**; API `/healthz` 200 |
| `superbot` | **FROZEN as behavioral oracle 2026-07-17** — "no new feature work"; production bot stable on Railway; open-PR surface = dependabot | 8 dependabot PRs open; automation (CodeQL, dashboard refresh) still firing |
| `product-forge` / **phone-controller** | Slice 17 / v0.17.0; owner-playtested v0.4.0; graduation to own repo is the README's own mechanic | **14 signed APK releases** (v0.4.0→v0.17.0), newest 07-24 |
| `fleet-manager` | Records custodian; hub venue | This work |

**Complete-and-parked, per their own closeouts (the owner rules their future):**

- **`superbot-next`** — 3,660 tests; **533 goldens / 49 subsystems + kernel**;
  7 required checks; 13-row owner agenda
  (`docs/design/OWNER-DECISIONS-2026-07-18.md`); D6 removal sequence for the
  autonomous apparatus documented; ~55 stale `claude/*` branches; open: #602
  (kit lane, **held by owner order 025** — do not land casually), #576 (parked
  docs). **Cutover ladder recorded:** parity green → wallet-race concurrency
  tests → 1 live-drive → **7-day shadow** → CUT-3 (fleet-grounding §3).
- **`superbot-games`** — 940 tests green; exploration engine live on a real
  verb; fishing→mining bridge built but **OFF by env-var design**; **not
  plugin-packaged** (host adapters = "later ladder rung").
- **`superbot-idle`** — engine + **21 data-only theme packs**; seven-parameter
  economy **SIM-PINNED** (V038); plugin adapter shipped and pinned in
  superbot-next's `plugins.lock.json`.
- **`superbot-mineverse`** — staged web app (READ contract → OAuth → HMAC write
  relay → HMAC ingest, all fail-closed); **live at
  web-production-97636.up.railway.app** (200 tonight); live mode blocked on
  6 env-var secrets + bot-side FLAGs; bot-side WRITE endpoint (superbot #2061)
  was **closed unmerged** 07-17 as an owner deploy-safety call.
- **`websites`** — four FastAPI services, **2,185 tests**, all four live and
  200 tonight; 10 open owner asks (Discord OAuth vars ×2 services, BAKE cron
  wiring, Gumroad/PayPal/photo/proofread ladder); **site-consolidation cutover
  plan exists** (`docs/plans/site-consolidation-cutover.md`) gated on explicit
  owner go; the nightly bake still commits (今日 #480).
- **`venture-lab`** — 1 LIVE SKU ($29, **0 organic sales**; **T+14 kill-rule
  dated 2026-07-26 — today**: keep only on ≥1 organic sale or qualified
  inbound, else pause/delist per the pre-registered packet); 19 publish-READY
  SKUs + 3 bundles + photo packs; **12 finished books** (Night Kiln ×6,
  DREAMLINE ×3, Ultramarine ×3) with KDP-ready packages; NL editions blocked
  on owner native-speaker proofread; 28-decision owner queue; 64-proposal
  veto menu; distribution named the binding constraint.
- **`trading-strategy`** — **11 rounds / 5,940 configs / 32 families / 0
  promoted**; holdout SPENT (stays spent); promotion CLOSED; paper lane
  `paper-0001` WATCH, graded **manually each Friday** now (`grade_paper.py`),
  first real grade ~early Aug; open #160 kit-upgrade parked on governance
  lines. The record's own verdict: "it is fine to let this rest."
- **`idea-engine` + `sim-lab`** (owner tonight: **stay active**) — two-phase
  history: (1) the fleet-ideation era — **566 idea files across 13 per-repo
  sections** (superbot 247, fleet 134, venture 66, games 49…), the Q-0264
  routing loop, product verdicts (economy tables, pricing, authenticity gate);
  (2) the post-fleet era — a self-sustaining **generate-and-verify math loop**:
  **261 PROPOSALs / 274 VERDICTs** (+13 offset), each a self-contained
  mathematical/algorithmic claim reproduced from a byte-identical verifier
  against 4 gates + a pinned Wikipedia revision (e.g. Stackelberg V228, Nash
  bargaining V227, Morris counting V274). Loop **at rest** — no un-verdicted
  proposal; sim-lab #344 is a lagging mirror to land or close; 3 verdicts
  below high-water remain open (V126/V132/V137).
- **`gba-homebrew`** — 4+ finished original games (Lumen Drift v1.3 **released**;
  Wickroad v1.0+arcs; Brineward; Underroot v1.0 — NDS titles too, built via
  BlocksDS); committed `dist/` ROMs; web arcade on GitHub Pages (200 tonight).
- **`pokemon-mod-lab`** (private) — **18 QoL toggles, 3 presets,
  byte-identical-when-off** discipline with recorded hash epoch; source-only
  rail (no ROM/asset bytes committed — patches only); count-guards in CI.
- **`substrate-kit`** — v1.20.2; the Self-Improvement seat closed; **the honest
  scientific result stands: steering improved, enforcement-pull unproven
  (cold-start bench 1 PASS / 8 FAIL)**; kit #552 open BY DESIGN (owner bench
  pin).
- **`codetool-lab` ×3** — finished CLIs: mdverify (2 releases LIVE), envdrift
  (0 releases), cfgdiff (0 releases); release-before-archive still pending.
- **`superbot-plugin-hello`** — contract exemplar, pinned by hash in the host's
  lockfile; **never archive** (both prior plans agree).
- **`curious-research`** — the gift workshop-notebook (3D printers, robot arm,
  Arduino); parked by owner choice 07-15 ("it gets a new mission later");
  one open slicer question (`OQ-CR-SLICER-ANSWER`).
- **`proxybench`** — single-file proxy benchmark, created 07-22, 1 commit.

---

## 4 · Money, as recorded

- **Revenue: one live SKU, $29, zero organic sales measured** (Gumroad views/
  sales are owner-dashboard-only — agents cannot see them). The kill-clock
  decision packet pre-registered today's T+14 call.
- **Costs: not measurable by agents** — CI minutes/tokens/dollars invisible
  from any agent-reachable surface (`docs/findings/fleet-economics-2026-07.md`,
  honest-nulls rule). The only cost proxies: ~18k superbot Actions runs
  all-time; 397 runs/day fleet-wide now.
- **Hard rails that held:** no spend, no account creation, no publishing
  without owner click (Q-0268 real-identity rule); trading RESEARCH-ONLY.

---

## 5 · Current situation — verified live tonight (2026-07-26 ~19:00Z)

- **12 open PRs fleet-wide:** superbot ×8 dependabot · trading #160 (parked,
  governance lines) · next #602 (owner-held kit lane) · kit #552 (owner bench
  pin, by design) · sim-lab #344 (lagging mirror). **Nothing is stuck.**
- **All 8 deployed surfaces answer 200:** control-plane, review (**both**
  `f027` and `fc91` — the Railway duplication `OQ-RAILWAY-PROJECT-SPLIT` is
  still real), botsite, dashboard, mineverse, shiftlife API, gba-homebrew
  Pages.
- **Scheduler state:** committed snapshot (07-21T16:00Z) shows **17 enabled**
  (10 standing failsafe crons + 6 one-shots + 1 poke-only). Tonight's live
  registry page 1 (everything created since 07-21) shows **1 enabled** (a
  fresh send_later for 19:57Z — a live session's pacemaker). **Unverified:**
  whether the 10 pre-close standing crons were actually wiped by the closers —
  the full 26-page re-export was not run tonight. A verify-and-wipe sweep is a
  concrete open action.
- **GitHub Actions crons still fire** (~185/day): roster-regen (gen #243
  today), websites bake, merge-on-green polls on six dormant repos.
- **shiftlife has an active working session today** (commits at 15:30–18:39Z).

---

## 6 · Contradictions and drift found between records (for the owner to adjudicate)

1. **Roster verdicts vs reality:** the generated roster stamps most lanes DARK —
  by design (heartbeats stopped at close), but it reads as failure. The roster
  measures a program that ended; its regen keeps running.
2. **fm PROJECT-CLOSEOUT lists review site as `f027`; websites' closeout says
  `fc91`.** Both are live (200 tonight) — that is the uncollapsed Railway
  duplication, not a typo.
3. **`superbot-games`' README claims plugin-shipping; the tree has no plugin
  packaging** (no `pyproject.toml`/`manifest.py`). Its own closeout is honest
  about this ("later ladder rung"); the README oversells it.
4. **The 2026-07-12 consolidation plan and the 07-11 8-seat structure encode a
  seat topology that no longer exists** — both are now marked historical, but
  many docs (roster, registry, prompts) still speak seat-language.
5. **The mid-July "merge classifier denies agents" belief was recorded, amplified
  across sessions, then falsified 07-18** — the correction banner exists
  (superbot current-state) but older docs still carry the scare verbatim.
  Standing doctrine: walls are never inherited.
6. **Idea-engine's mission ("ideas for the whole fleet") vs its late output
  (textbook-math verification)** — the record is honest about the pivot, but
  a reader of the README alone would expect 566 product ideas, not ~260
  math reproductions layered on top. Both eras are real; they are different
  assets.

---

## 7 · What the record cannot tell me — the owner's questions

The repos document the past thoroughly. What they cannot contain is **intent
going forward**. These are the genuine forks (each answerable in a sentence):

1. **The 8-Project structure itself:** do the claude.ai Projects still exist on
   your side, and do you intend to re-create standing seats at all — or is
   everything now driven from this hub chat + on-demand sessions? (Decides the
   fate of the prompt registry, failsafe crons, roster machinery, W7.)
2. **Ideas Lab going forward:** "remain active" = standing autonomous
   generate/verify loop again, or **on-demand** (a project consults
   idea-engine/sim-lab when it needs ideation/verification)? And should the
   late-era math-verification loop continue, or refocus on product ideas?
3. **Venture-lab's kill clock is today:** the pre-registered T+14 rule says
   pause/delist the $29 SKU absent a sale/inbound. Apply it, or override it?
   And the 19 ready SKUs + 12 books — publish wave, or hold?
4. **superbot-next cutover:** the recorded ladder ends in a 7-day shadow run
   before CUT-3. When you say "live testing first" — is the test-bot token +
   test guild something you want prepared now, or after the consolidation?
5. **websites:** consolidate to which Railway project (`reliable-grace` is the
   one the Anthropic emails link; `superbot-websites` is the parallel copy)?
   And do botsite/dashboard follow the bot into its repo, or stay?
6. **The EAP relationship:** the final vendor review email (guidance written
   2026-07-21, target ~07-22) — was it sent? Is the EAP thread closed on your
   side? (Affects whether `reliable-grace` URLs must stay stable.)
7. **What the record misses:** anything major that happened outside the repos
   (conversations, decisions, external commitments) that the documentation
   doesn't know and should?
