# Dispatch log

> **Status:** `living-ledger` — dated log of what the manager dispatched and shipped.
> One line per dispatch; PR numbers where memorable.

## 2026-07-09 — gen-1 baseline day

- Kickoff recon — 4 workers fanned out across the fleet for ground-truth state.
- Control-file plant — protocol `control/` files planted in 4 repos (PR fallback where
  main is protected).
- CI unjam + arbitrations — unstuck red pipelines; applied first-declared+claim-filed
  precedent (playbook R10).
- Three arm seeds + trading + games launches — sb#1892/#1897/#1901/#1903, games#3.
- Env shim + multi-repo verification probe — defensive setup scripts (playbook R15).
- Four-reviewer quality audit — cross-checked worker output against git evidence
  (playbook R2).
- Retro protocol — retro collection run across 9 repos.
- External review pack — assembled and shipped; next#57/#78.
- Universal wake-up prompt — one prompt any Project can boot from.
- Owner-directed merge sweep — 5 PRs merged (incl. games#6).
- Manager home repo seeded — this repo: playbook v1, templates, owner queue,
  dispatch log, control heartbeat.

## 2026-07-09 — afternoon (retro synthesis → capability/env bands)

*(Retro protocol rollout ×9 repos, owner-directed merge sweep, universal wake-up
prompt, and the external review pack are logged above; review pack ref: sb#1903
+ next#57/#78.)*

- Email addendum — findings 1–10 completed for the Anthropic email pack (send is
  an owner-queue item).
- Retro synthesis sweep — fleet self-reviews collected + synthesized into the
  gen-2 input set; owner-queue rewritten from it.
- Owner-action quality band — playbook R17 + owner-queue header mirror (#3).
- Capability manifest — `docs/capabilities.md` master + playbook R18 (#4);
  kit-side band ordered (substrate-kit inbox ORDER 006).
- Env registry — `environments/` seeded (#5: README, `setup-universal.sh`,
  `env-vars.md`, `multi-repo.md`, SPEC-TEMPLATE).
- websites ORDER 005 (/queue + /environments pages) — dispatched; ⚠ verification
  17:43Z found it NOT on main and no PR carrying it (worker died) →
  **re-dispatch needed**.
- Follow-ups queued: superbot-next agent-audit nudge (next#89, open ORDER 006
  append); kit PR#50 disposition + order-lease convention (kit#56, open ORDER
  append — **stale premise**: #50 was owner-merged 17:40Z after #51, both retro
  sets landed disambiguated by filename suffix; #56 also collides with the
  capability band already numbered ORDER 006 on kit main → renumber + rewrite
  before merge).
- Housekeeping verification sweep (this session) — audited all afternoon
  dispatches against live GitHub; findings above + in `.sessions/`
  2026-07-09-housekeeping-verification card.

## 2026-07-09 — evening (succession)

- Ping test — one PING order appended + merged to all 9 fleet inboxes across
  8 repos (write latency 30s–14min by required-check weight; substrate-kit
  ORDER-008 collision → R19). Table:
  `docs/findings/ping-test-2026-07-09.md`. **Ack sweep pending at handoff.**
- GPT-5.6 research — live-web worker; facts+pricing+relevance, Codex-arm
  recommendation, METR eval-gaming caution:
  `docs/findings/gpt-5-6-report-2026-07-09.md`.
- Transcript + miner — yt-dlp transcript recipe (→ capabilities.md) +
  monetization-video analysis → venture shortlist:
  `docs/findings/venture-shortlist-2026-07-09.md`.
- Retro synthesis + UI-visibility analyses consolidated from worker outputs
  into `docs/findings/` (previously uncommitted, chat-only).
- Succession package (this PR) — `docs/prompts/` verbatim ledger (8 deployed
  texts + venture-lab draft), `docs/findings/` ×5, `docs/gen2-blueprint.md`
  draft, `docs/handoff-2026-07-09.md`, playbook R19, capabilities yt-dlp
  recipe, heartbeat refresh. Chat archives after merge; successor session
  takes over.

## 2026-07-09 — late evening (successor: ping-ack collection + gen-2 finalization)

- Ping-ack read-half sweep — all 9 lane status files + commits-API ack
  timestamps read at HEAD: **2/9 acked** (superbot-next 9m47s, substrate-kit
  14m43s dispatch→ack-on-main — both via live-session inbox re-reads; next's
  ack landed on main 4m10s *before* the order itself did), **7/9 NO ACK**
  (no live session; opus4.8 awake-but-missed 15m31s post-ping). Results +
  6 conclusions appended to `docs/findings/ping-test-2026-07-09.md`.
- gen-2 blueprint FINALIZED `plan` → `binding` — read latencies folded into
  new §2a wake-cadence (Class A hourly / B 4-hourly / C daily); §5 open
  items resolved; late retro deliverables reconciled at HEAD (next
  project-review EXISTS via next#92; games retro #9 MERGED by owner
  19:02:46Z; port #5 still open+draft).
- venture-lab founding Custom Instructions finalized
  (`docs/prompts/venture-lab-draft.md`, paste-verbatim) + ONE consolidated
  launch click-list in `docs/owner-queue.md` (repo → ruleset → Project →
  environment → hourly routine → boot); mining owner-queue item narrowed to
  the remaining #5 click.
- Handoff in-flight list updated (ping-ack: collected; venture-lab:
  finalized; Codex arm + external campaign: tracking) + fleet-state drift
  fixes verified at HEAD (kit v1.6.0/orders done; next retro; games #9).
- Rails held: fleet-manager writes only; no lane inbox touched (R19).

## 2026-07-09 — night (wind-down sweep, PR #10 package, venture-lab seed, EAP extension)

- Gen-1 wind-down progress — **7 of 9 repos DONE** (wind-down succession
  packages committed lane-side); manager follow-up: sweep the remaining 2
  lanes' `control/status.md` markers, then queue gen-2 relaunch clicks.
- PR #10 package shipped — merge-authority policy (gen-2 blueprint §1/§2
  rewrite), 4 tested environment archetypes (`environments/archetype-*.sh`),
  verified merge queue (`docs/merge-queue-2026-07-09.md`); landed via REST
  merge-on-green after 3 failed auto-merge arm attempts (→ playbook R21).
- venture-lab **SEEDED** (`d065c68`) + **owner green light** in tonight's
  session — the gen-2 born-right pilot is live-pending the owner-queue
  click-list (ruleset, Project, environment, routine) + ORDER 001.
- EAP window **EXTENDED to 2026-07-14** — Anthropic email 2026-07-09 22:29Z
  (supersedes the Friday 2026-07-10 close); free-window burn re-planned.
- Owner-session idea capture — 9 brainstorm ideas (~22:30–23:00Z) committed
  to `docs/ideas/` (mobile-lab, spend instruments, email chief-of-staff,
  superbot watchdog, security auditor, devlog, bot analytics, design system,
  research desk); all `captured (not approved)`.
- Playbook **R21** + blueprint alignment — REST merge-on-green PRIMARY on
  born-red/no-CI repos (provenance: this repo's PR #10 + venture-lab PR #1).
- In-flight carried: **Anthropic follow-up draft early next week** (before
  the 2026-07-14 close) — on the handoff in-flight list.

## 2026-07-09 — night, later (game-lab decision + founding package)

- **Owner decision: game-lab launches, BOTH tracks** — Track A private
  Pokémon Emerald mod (pret/pokeemerald), Track B public original GBA
  homebrew (Butano). Decided in tonight's owner session on the strength of
  the toolchain scout proof.
- Toolchain scout (same night) — all three loops PROVEN in-container:
  pokeemerald byte-identical 1m20s/2.0s; Butano 17.5s via the leseratte10
  devkitARM r68 mirror route (official installers Cloudflare-403); mGBA
  headless boot/run/PNG at ~290 fps with scripted in-game verification.
  Distilled to `docs/findings/gba-toolchain-proof-2026-07-09.md`
  (screenshots live in the scout session's chat).
- game-lab founding package shipped (this PR) — findings doc, gba-lab
  environment archetype (justified 5th: `environments/archetype-gba-lab.sh`
  + archetypes row), paste-ready founding prompt
  (`docs/prompts/game-lab-founding.md`, gen-2 template, ORDER 001 draft),
  ideas entry (decided — in founding), owner-queue launch click-list
  (2 repos: gba-homebrew public / pokemon-mod-lab PRIVATE · Project ·
  gba-lab env · hourly routine · boot line), capabilities.md GBA recipe +
  devkitPro-403 wall (R18).

## 2026-07-10 — night (Fable-5 ultracode fleet review landing)

- Fable-5 fleet review landed (this PR) — 30/30 adversarially confirmed
  findings synthesized to `docs/findings/fable5-review-2026-07-09.md`
  (owner exec summary, per-dimension dispositions, blueprint amendment
  **PROPOSALS P1–P11** — blueprint/playbook/owner-queue NOT edited; the
  next blueprint edit stays with the CI-tier sim session — and drift-fix
  list D1–D6); 10 gen-2 founding instruction packages copied to
  `docs/proposals/instructions/` (ALL PROPOSED, none deployed, paste-time
  delta-8 lint in the README); 3 verified new ideas captured
  (review-queue drainer, lane-seeder automation, fleet economics ledger);
  handoff websites drift fixed on sight (F15/D3). ⚑ Self-initiated within
  scope: D3 handoff fix + findings-README index row.

## 2026-07-10 — morning (gen-2 launch consolidation)

- Gen-2 fleet launched overnight — **116 PRs merged 00:00–06:15Z, zero
  stuck** (verified against the merged-PR search, not reports; the "~80"
  brief undercounted). Full record + dispositions + archetype map:
  `docs/planning/gen2-launch-record-2026-07-10.md`.
- `control/status.md` REWRITTEN (was stale at the gen-1 handoff,
  last-shipped #7) — gen-2 lanes, in-flight, morning pointers.
- `docs/owner-queue.md` REFRESHED into one deduplicated queue (8 active,
  HOT = kit F-5 ruling; superseded items retired: environments created,
  kit #26/#49 + games #5 merged, launch click-lists executed).
- Two instruction packages DEPLOYED fitted (websites, trading-strategy —
  ≤7,500-char re-trims recorded in the package files); capability walls
  appended (Custom Instructions 8,000-char cap; routine/trigger creation
  walled on BOTH sides — PLATFORM GAP, interim = morning "continue" per
  Project).
- Idea captured: GBA play-through-Discord
  (`docs/ideas/gba-play-discord-2026-07-10.md`).

## 2026-07-10 — morning, later (routine-wall correction + wake-arm rollout)

- PLATFORM-GAP correction — owner-verified (2026-07-10 ~morning): Claude Code
  Projects CAN create their own routines that fire inside the Project; the
  "walled on BOTH sides" conclusion stands only for non-Project surfaces
  (webagent coordinator + spawned workers: no send_later/self-trigger;
  cross-session trigger binding refused — verbatim error texts KEPT in
  capabilities.md). Corrected: capabilities.md (narrowed wall + CAN entry),
  gen2-blueprint §2a rider (wake cadence now agent-executable), owner-queue
  item 7 (→ "self-arm rollout dispatched; owner fallback only on a recorded
  lane failure"). Exact in-Project mechanism unknown — recipe pending: first
  successful lane records the exact tool/UI path.
- Wake-arm ORDER rollout dispatched to 6 active lanes — venture-lab,
  substrate-kit, pokemon-mod-lab, gba-homebrew hourly (Class A); websites,
  trading-strategy 4-hourly (Class B), per blueprint §2a. (PR #19.)

## 2026-07-10 — midday (ROUND-3 INTAKE, brief §1 task 1)

- **ROUND-3 BRIEF received** (superbot
  `docs/planning/round3-launch-pack-2026-07-10.md` §1; context: the overnight
  review + EAP program review, both 2026-07-10). Intake recorded here; the six
  STANDING DEBTS are now **ORDERS 001–006 in the manager's OWN
  `control/inbox.md`** (the program-review §5.1 doctrine fix: amendments get
  an ORDER + a named next-session owner, never a dangling "some future
  session" — the one channel the manager built for everyone is no longer
  unused on itself). ORDER 005 (ping-test websites false NO-ACK row) and
  ORDER 006 (codetool release-wall contradiction + seat-contamination caveat)
  executed immediately in the same PR (#20) + codetool-lab-fable5 PR #14
  (MERGED a6cf1a9: PLATFORM-LIMITS item 4 release-wall corrected to
  seat-dependent, citing opus4.8's two live workflow_dispatch releases).
- **SECOND routines correction landed** — `capabilities.md` + blueprint §2a:
  agent-armed routines WORK via the claude-code-remote scheduling tools
  (`create_trigger` / `send_later` family), **SEAT-DEPENDENT** (same per-seat
  class as the merge classifier); evidence: owner recordings 11:01Z/11:04Z —
  two ACTIVE "Created by Claude" routines (trading-strategy 4-hourly, run
  10:09; kit-lab hourly, runs 12:28/12:28/12:30). "Recipe pending" retired.
- **STANDING AUTONOMOUS CORE (owner design, launch-pack §5) recorded** — four
  Projects run permanently on ~2-hourly routines and loop without the owner:
  (1) the manager, (2) a NEW dedicated **Idea Engine** Project on the superbot
  repo, (3) the superbot-next builder, (4) a **Product Forge** (seat: candidate
  TBD per corrected round3-launch-pack §5 — owner retracted venture-lab
  pairing, 2026-07-10; default fallback = seed a dedicated `product-forge` repo
  born-right with a required check; venture-lab keeps its own venture mission
  unchanged). Manager's role in the loop: route the
  Idea Engine's proposals as ORDERs, consolidate the owner-queue, and watch
  the four routines' liveness in the staleness sweep. Loop shape: Idea Engine
  files/promotes → Manager routes → Builder + Forge consume → Manager
  consolidates → Idea Engine grooms from what shipped; cadence staggered
  (lanes even hours, manager odd/+1h). Owner-queue item 0 carries the Idea
  Engine creation click. All other Projects stay owner-started, one by one.
- **GEN-3 GATE recorded** — collect every lane's night self-review (the owner
  is pasting a continuation+review prompt into each lane; answers land in the
  lane repos) plus the Codex external reviews, and synthesize the gen-3
  blueprint delta the same way the gen-1 retro fed gen-2. **Do NOT relaunch
  lanes for gen-3 until the owner has seen the consolidated "state of the
  fleet + gen-3 delta" report** — the owner wants ONE gate, at the blueprint.
- Also expected: owner tests the three websites today — a suggestions ORDER
  for the websites lane will follow; treat his notes as product feedback with
  priority.
## 2026-07-10 — midday (night-review audit landing)

- Commissioned night review LANDED (this PR) — 26-question audit of the first
  fully-autonomous night, answered against the eight HEAD-verified discovery
  digests + live API checks: `docs/findings/night-review-2026-07-10.md`
  (exec summary, full Q&A, send-ready Anthropic-email items, ranked
  recommendations, "Where we were lucky"). Headline catches requiring action:
  venture-lab ⚑B invites publishing a product whose headline Stripe claim has
  never executed and near-certainly fails (D1) → ⚑B is "DO NOT publish yet"
  until the ~1h fix session; superbot-games substrate-gate collects 73 of 121
  tests (one-line fix named); pokemon-mod-lab is PUBLIC against its "no
  exceptions" PRIVATE rail — all 13 account repos are public (owner decision
  this week: flip private vs. amend the rail). Must-land-before-scaling set
  (3): visibility/rails structural guard (kit v1.8.0), truth-boundary rule on
  owner asks (next blueprint pass, with the R21 rewrite), scheduled
  deep-review layer (self-armed fm routine). Economics-ledger commitment:
  2026-07-12, else no new lanes after 07-14.

## 2026-07-10 — afternoon (night-review remediation dispatch)

- **Night-review follow-ups executed (this PR, #23)** — the audit's must-act
  set converted from findings into live guardrails:
  - **owner-queue:** venture-lab **⚑B and ⚑D publish clicks FROZEN**
    ("FROZEN 2026-07-10: D1 Stripe defect (headline paid path never executed;
    customer_email null on live events + invalid {CHECKOUT_EMAIL} success-URL
    placeholder) — unfreezes when venture-lab's fix ORDER lands with a
    real-path test"); new **🚨 URGENT top-of-queue item**: owner flips
    pokemon-mod-lab to PRIVATE (Settings → Danger Zone) — vendored Nintendo
    source is world-readable against the lane's "no exceptions" rail; second
    line invites an account-wide visibility review (all 13 repos public).
    Item 3's stale "(PRIVATE — never publish)" note corrected on sight.
  - **playbook:** **R22 VISIBILITY GUARD** (rails that depend on visibility
    verify the actual `repo.private` bit via API every session start) +
    **R23 OWNER-ASK TRUTH-CHECK** (no outward-facing/irreversible owner click
    ships without non-author end-to-end verification evidence). Provenance:
    Q-0194 friction→guard class, night-review-2026-07-10 Q16/Q2/Q6/Q18.
  - **capabilities:** CAN entry with the exact visibility-check recipe
    (`GET /repos/{owner}/{repo}` → `.private`/`.visibility`; curl/gh/MCP forms).
- **Four lane ORDERs dispatched immediately after this PR lands** (one repo at
  a time, R19 serialization, each via that repo's fast lane):
  1. **venture-lab (P0)** — fix D1/D2/D3 on the REAL Stripe path (handle
     customer_email null, replace the {CHECKOUT_EMAIL} placeholder, HTTP-layer
     real-path test, buyer-zip README → v0.2 reality, QUICKSTART mock-mode
     trap, rebuild both zips); done-when includes "⚑B/⚑D unfreeze requested".
     Publish clicks stay frozen until it lands.
  2. **superbot-games (P0)** — CI collection-scope fix: the pytest gate
     collects 73/121 tests (`games/exploration/tests/` invisible); collect ALL
     suites + a collected-count assertion so scope-shrink is loud.
  3. **trading-strategy** — add the founding-plan's deflated-Sharpe (or
     equivalent) significance bar to the promotion rule BEFORE any holdout
     use; re-grade AAPL-donchian honestly (expected: demote to candidate);
     ledger the re-grade.
  4. **pokemon-mod-lab** (effective after the owner's visibility flip) —
     verify visibility=private via the API, record in `control/status.md`;
     R22 applies every session thereafter.

## 2026-07-10 — afternoon (visibility saga: the private-plan auto-merge wall)

- pokemon-mod-lab visibility saga — sequence: the owner executed the 🚨 URGENT
  flip to PRIVATE (night-review Q16: vendored Nintendo source was
  world-readable); then flipped the repo PUBLIC again **solely to reach the
  repo-settings auto-merge toggle**; the manager countered (same Q16
  exposure); the owner flipped it back PRIVATE. **Root cause: on this GitHub
  plan, private repos cannot enable the auto-merge toggle at all**
  (owner-verified 2026-07-10). **Resolution: REST merge-on-green (R21) needs
  no toggle** — recorded as a WALLED entry in `docs/capabilities.md`; a
  visibility flip is never the fix for a merge-path problem. End state
  verified live per R22 at this session: pokemon-mod-lab `private: true`;
  fleet-manager itself still `private: false` (account-wide flips in
  progress — successor retires/updates the URGENT owner-queue item once the
  sweep settles, verifying bits per R22).

## 2026-07-10 — afternoon (archive prep: manager succession package)

- Owner archiving the manager chat — everything chat-only from that session
  committed as the successor package (PR #24, `manager/archive-prep-2026-07-10`):
  `docs/handoff-2026-07-10.md` (gen-2 → gen-3 succession: read order, live
  state, in-flight/promises incl. the ⚑B/⚑D freeze + gen-3 gate + ORDER
  001–004 pointers + the Anthropic follow-up material, and the
  delivery-channel SOP with the comment-at-open + ack-token rule),
  `docs/capabilities.md` append (private-plan auto-merge toggle wall + REST
  merge-on-green resolution), this log's visibility-saga entry, and the
  `.sessions/2026-07-10-archive-prep.md` card. Landed via REST
  merge-on-green (R21 — no arm attempt).

## 2026-07-14 — overnight wake 0235Z, Slice C (central-docs-plan Slice 0)

- **codetool-lab-fable5 disposition DECIDED: ARCHIVE, no relaunch**
  (decide-and-flag, Q-0240 class — the lane sat "ready for archive + fresh
  session" for 4 days with no decision either way; fable5 candidate 7 /
  plan C2). Rationale: the gen-2 8-seat structure has no codetool seat, the
  CLI (envdrift) is finished and wound down, and the consolidation plan's
  reconciled verdict is HARVEST-THEN-ARCHIVE with release-in-place. No fresh
  session will be armed. Sequencing (unchanged, all prior gates retained):
  P1-5 repo hygiene → D5 mirror-before-archive (succession pack,
  PLATFORM-LIMITS, custom-instructions-proposal, ROADMAP stale-recipe
  correction) → tag/Release clicks → owner archive click (E#44/E#45 gate).
  Recorded here + fleet-triage row re-stamped; owner veto reverses it with
  one word.
- **idea-engine ASKs 001–004 ANSWERED fm-side** (Slice 0 item 8; all four
  read verbatim at idea-engine `control/outbox.md` @ `3ae82cb`, live-fetched
  this wake). Answers (delivery INTO idea-engine's inbox is a lane write —
  see the pending-lane-writes ledger below):
  - **ASK 001** (upstream `claude/` head-branch prefix into the kit
    auto-merge-enabler template): **ACCEPTED** — kit-owned surface;
    ORDER-to-lane(substrate-kit). Evidence standard: the next idea-engine
    kit-upgrade PR retains the line.
  - **ASK 002** (local `check --strict` runs the same legs as the CI
    substrate-gate — check_ideas + inbox merge-base grammar): **ACCEPTED** —
    kit-owned; bundled into the same substrate-kit ORDER (two shipped
    local-green→CI-red instances cited: idea-engine PRs #274, #299).
  - **ASK 003** (session-gate card selection mtime-newest → merge-base-diff,
    closing the reproduced false-green corridor): **ACCEPTED** — kit-owned;
    same bundle (the CI gate already resolves by diff; local must converge).
  - **ASK 004** (outbox rollover convention): **ANSWERED with the convention
    itself** — `docs/conventions/outbox-rollover.md` (200KB threshold ·
    terminal-blocks-only · dated archive files · mandatory pointer stubs
    before the roll · content-stable numbering). First execution targets:
    sim-lab (~875KB) + idea-engine (459KB), each via lane ORDER.
- **Central-docs plan landed at its §1 home** (Slice 0 item 9):
  `docs/planning/2026-07-14-central-docs-plan.md` (moved from
  `docs/central-docs-plan.md`, permanent MOVED stub left); the two frozen
  superbot seeds indexed as provenance in `docs/planning/README.md`
  (verified present at superbot `3477594`).

### Pending lane writes (Slice 0 deferrals — fm-write-scope wake; dispatch from here)

One line each: target repo · what · why deferred. All are inbox-ORDER
deliveries the next dispatch/coordinator turn performs; nothing below blocks
the Slice 0 items themselves, which are complete fm-side.

1. **superbot** · supersession stub on
   `docs/owner/trigger-health-order-2026-07-12.md` → pointer to fm
   `docs/trigger-health-spec.md` (plan A2 / Slice 0 item 4, the #1974
   pattern) · superbot outside fm write scope tonight.
2. **superbot** · supersession banners on the two frozen seeds
   `docs/planning/fleet-centralization-plan-2026-07-11.md` +
   `docs/planning/fleet-review-2026-07-11.md` → pointer to fm
   `docs/planning/2026-07-14-central-docs-plan.md` (plan §1
   Self-application / Slice 0 item 9) · same.
3. **substrate-kit** · one bundled ORDER: (a) enabler-template `claude/`
   head-branch allowlist line (idea-engine ASK 001); (b) `check --strict`
   converges on the CI substrate-gate legs (ASK 002); (c) session-gate card
   selection mtime→merge-base-diff (ASK 003); (d) A10 outbox-size advisory
   in `check --strict`; (e) seat-digest/CAPABILITIES templates' dead
   lowercase `fleet-manager docs/capabilities.md` pointer → uppercase
   `docs/CAPABILITIES.md` (INC-29 / plan B2 — one template fix heals ~14
   adopters) · all kit-owned surfaces.
4. **idea-engine** · deliver the ASK 001–004 answers (above) into its
   `control/inbox.md` + ORDER its own outbox rollover per the convention ·
   lane write.
5. **sim-lab** · ORDER the ~875KB outbox rollover per
   `docs/conventions/outbox-rollover.md` + cross-link the OA-002 split
   verdict (enabled=resolved / quota=open, INC-04) into its ledger · lane
   write.
6. **pokemon-mod-lab** · correct its own "Q-0266" citations for the QoL+
   pick to `superbot:Q-0262.7` (INC-09, ORDER-to-lane half; fm's side fixed
   this wake in `docs/q-index.md` + the findings doc) · lane write.
