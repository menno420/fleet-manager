# The EAP story

> **Status:** `reference`
> Generated 2026-07-14 by the fleet review (owner directive).
> The full narrative of the Claude Code Projects EAP as run by the menno420 fleet:
> the start, the first test results, how the workflow improved, what stayed hard,
> what got fixed completely, and how the fleet grew from one repo to ~19 in a week.
> Every claim below is cited to the pinned per-repo review notes, which themselves
> cite path@SHA, PR #, or a dated card/log; headline commit/PR/date claims were
> additionally spot-verified against full-history clones (12/12 sampled checks
> passed). Where the underlying deep-review note recorded "not found" or
> "as-reported", that caveat is preserved — honest gaps are stated, not smoothed over.
> Primary sources: the 19 per-repo deep-review notes of the 2026-07-13/14 fleet
> review (each pinned to a reviewed HEAD SHA), collated by the EAP-historian lane.

---

## Contents

1. [Prologue — one repo, one non-coder owner (2025-08 → 2026-05)](#1-prologue)
2. [The substrate is built in one repo (June 2026)](#2-substrate)
3. [EAP kickoff and first test results (2026-07-07)](#3-kickoff)
4. [The unlock day — probes, the Contents-API key, two foundings (2026-07-08)](#4-unlock)
5. [The fleet explodes; gen-1 lives and dies in a day (2026-07-09)](#5-explosion)
6. [Gen-2: born-right seats and self-arming wakes (2026-07-10)](#6-gen2)
7. [Centralization, continuous mode, peak velocity (2026-07-11)](#7-centralization)
8. [The scheduler incident, fabrication forensics, first revenue (2026-07-12)](#8-incidents)
9. [The first fully-doctrined unsupervised night (2026-07-13) and close (07-14)](#9-close)
10. [What improved, what got fixed, what stayed hard — and what the arc demonstrates](#10-ledger)

---

<a name="1-prologue"></a>
## 1. Prologue — one repo, one non-coder owner (2025-08 → 2026-05)

The story starts long before the EAP, with a single fact that explains everything
that follows: the owner **cannot code** and relies entirely on agents for correct,
complete, end-to-end work (superbot `.claude/CLAUDE.md`, working agreement).

superbot's first commit is `330c7716`, 2025-08-10 — "Initial commit with reference
bots and superbot folder", a hand-started Discord-bot project. Eight commits landed
in August 2025, then the repo went dormant for roughly nine months (monthly commit
counts: 2025-08: 8 → 2026-05: 1,206) (superbot review note §3, git history at
reviewed HEAD `bbc524e4`).

On **2026-05-13** the project revived on Claude Code on the web: Railway deploy
fixes and the **first claude/-branch merge, PR #10** (`db942a67`, branch
`claude/debug-fix-2dOKE`). That merge is the start of the program's premise —
agents run the project, the owner steers (superbot review note §3).

<a name="2-substrate"></a>
## 2. The substrate is built in one repo (June 2026)

Everything the fleet later ran on was invented inside superbot in about five weeks,
almost entirely as *reactions to specific failures*, each carrying an owner-decision
Q-number in `docs/owner/maintainer-question-router.md` (Q-0001…Q-0274, ~9.9k lines
at review — the decision-provenance store for the whole program; superbot review
note §2).

- **2026-06-05** — `.session-journal.md` cross-session working memory created
  (superbot commit `08dbf6d9`).
- **2026-06-07** — the per-session `.sessions/` card convention (commit `94293b89`).
- **2026-06-08 → 14** — the doctrine burst (June 2026: 3,106 commits): PR-every-session
  (Q-0052); the terminal-PR rule (Q-0103); **GitHub-native auto-merge** via the
  `auto-merge-enabler` workflow (Q-0123, superbot PR #779 — built because a deferred
  manual merge was forgotten, the #778 failure); the **born-red session-card gate**
  (Q-0133 — built because auto-merge once landed a *partial* PR before its close-out
  docs, the #843 race); every-30-PR reconciliation passes (Q-0107); and the mandatory
  session enders — one new idea per session (Q-0089), a review of the *previous*
  session (Q-0102), a closing docs audit (Q-0104) (superbot review note §3;
  superbot `.claude/CLAUDE.md`).
- **2026-06-16 → 22** — "**friction → guard**" becomes law (Q-0194: every workflow
  interruption converts into an enforcing checker/hook/rule before session end),
  alongside the false-green doctrine (Q-0120: a green check that contradicts visible
  evidence is a bug in the *check*) (superbot review note §3).
- **2026-07-06/07** — the rebuild program is authorized with **never-wait autonomy**
  (Q-0241: build in logical order, live-test in a real server, silence = consent)
  and **understand-and-reflect** (Q-0254: state the fuller picture back before
  building, because the owner deliberately thinks in fragments) (superbot
  `.claude/CLAUDE.md`; superbot review note §3).

Four instruments from this period are the recurring heroes of everything that
follows: born-red session cards, the auto-merge enabler, the question-router
provenance record, and friction→guard.

<a name="3-kickoff"></a>
## 3. EAP kickoff and first test results (2026-07-07)

The **Claude Code Projects EAP second mandate** begins on 2026-07-07: a coordinator
kickoff, an evaluation guidebook, and an append-only evaluation journal — superbot
`docs/planning/projects-eap-evaluation-log.md`, landed by PR #1820 (superbot review
note §3). ("Second mandate" is the source's own label; no reviewed note dates or
describes the *first* mandate — that gap is stated in "Sources and known gaps"
below rather than reconstructed.)

**The first test results arrived the same night, and they split cleanly in two.**
The coordinator tier had **no file/shell tools, no clock, no send_later, and no
direct channel to its children**; its container clone was **7 merged PRs behind
origin** at first turn. The worker tier, meanwhile, ran the entire born-red → claim
→ PR → auto-merge loop "with zero permission prompts and no tool failures" (eval
log entries ~22:45Z, 2026-07-07). That split verdict — *coordinator amputated,
worker superb* — set the whole EAP's engineering agenda (superbot review note §3, §6).

<a name="4-unlock"></a>
## 4. The unlock day — probes, the Contents-API key, two foundings (2026-07-08)

- **The 11-test auto-mode permission probe** (superbot PR #1830) mapped the walls:
  everything creative ALLOWED zero-prompt; destructive git hard-walled; bypass
  attempts caught. **The discovery that unlocked the fleet:** the git-push
  first-publish wall is *transport-specific* — the **GitHub Contents API bootstraps
  fresh repos prompt-free**. It was used the same day to bootstrap substrate-kit
  (commit `fae482ac`) and superbot-next (commit `de36d28b`). The owner sent the
  first Anthropic feedback email on 7/8; a campaign self-audit measured the
  coordinator's memory at **≈0.98 precision** recalling a 7-PR campaign against git
  — the source's own headline phrasing ("coordinator recall ≈0.98 precision")
  conflates the two metric names; the clearer restatement in the same note is
  "≈0.98 precision recalling … against git", used here (superbot
  `docs/eap/campaign-self-audit-2026-07-08.md`; superbot review note §3, §"joys").
- **substrate-kit founded** — extracted from superbot's subtree (kit PR #1,
  `3d303a0`) per the founding plan `docs/planning/kit-lab-founding-plan-2026-07-07.md`.
  Its founding state was notably honest: the cold-start A/B benchmark had **already
  FAILED twice** pre-extraction ("ON read 3.1–3.3× more and wrote nothing back").
  The kit became consumer #0 of itself (kit decision D-0001) and the canonical home
  of program law — the PL-register in `docs/program/rulings.md`, "cite PL-IDs, never
  copy ruling bodies", CI-enforced by `scripts/check_program_law.py` (substrate-kit
  review note §1, §3, at reviewed HEAD `727f5db`).
- **superbot-next founded** — "built fresh, not forked": a ground-up rebuild with
  the live bot as a strictly read-only behavioral oracle. **The 14-hour rebuild**
  started 16:17Z: 49 PRs by 1 coordinator + 1 builder spawning **18 sequential
  workers**, with "zero rework: no PR had to be reverted or redone"; at PR #50 the
  repo stood at 999 tests green, 465 byte-identical goldens, 22 checkers
  (superbot-next review note §3).

<a name="5-explosion"></a>
## 5. The fleet explodes; gen-1 lives and dies in a day (2026-07-09)

The single densest day of the program. Per fleet-manager's own economics finding,
"every repo except superbot was created inside the EAP window (first commits
2026-07-08 → 07-10)" (fleet-manager review note §3, at reviewed HEAD `ff6361a`).

- **fleet-manager founded** (first commit `3c32db7`) — the manager Project's home;
  kit adopted the same day. Playbook rules R1–R21 were **mostly earned this one day
  from live failures**: "reports said zero rework; git showed 8 fix-PRs" → R2
  verify-against-git; a wrong-PR announcement → R3; ORDER-number collisions → R19
  (fm `docs/playbook.md`; fleet-manager review note §3). An evening ping test across
  9 fleet inboxes got **2/9 acks** (later corrected to 3/9) (fm `docs/findings/`,
  ping-test; fleet-manager review note §3).
- **websites founded** (`aec1cd5`) — **46 PRs in one day**: control-plane built and
  deployed to Railway, botsite + dashboard rebuilt, auth dropped on the owner's
  verbatim "Yes drop the auth", and the `/fleet` heartbeat page ordered because the
  owner "tracks [sessions] by opening sessions one by one". Gen-1 waste was recorded
  honestly: superseded PRs from parallel workers sharing one checkout, and no
  scheduler primitive — "the one capability I'd trade almost anything for"
  (websites review note).
- **trading-strategy founded** — and immediately hit the EAP's canonical
  provisioning failure: a builder session dead 30.2 minutes on a setup script that
  assumed `requirements.txt`, then an **identical failure silently killed the
  successor** (0 turns, no failure event, unnoticed ~2.8h). PR #1 (a full P0 with
  63 tests) sat **draft-invisible ~2.8h** because the platform's draft-default
  fought the "merged" done-when — trading ORDER 002 created the fleet-wide
  READY-never-draft convention (trading-strategy review note, EAP story section).
- **superbot-games founded** (first commit `28cd695`, README seed; PR #1
  `f7b7178` with the founding plans, lanes contract, and control files) — the
  shared home of SuperBot game plugins, originally designed for **two cohabiting
  autonomous Projects** (game-mining + game-exploration) in one repo
  (superbot-games review note §"Founding").
- **The three codetool-lab arms** (fable5 / opus4.8 / sonnet5) ran a deliberate
  model comparison: identical brief ("ship an OSS-quality CLI end-to-end"),
  deliberately kit-less, one-day lifespans by design.
  - *fable5 → envdrift*: a 76-minute dead boot (same requirements.txt class), then
    v0.1.0 in ~20 minutes of worker time, **zero CI fix rounds across two releases,
    byte-exact stranger-install tests on first attempt**. Release wall: tag push
    403, releases API 403, workflow classifier-denied twice — accepted as policy
    (codetool-lab-fable5 review note).
  - *opus4.8 → mdverify*: the whole tool + 100 tests + CI in ONE PR ~90 minutes
    from seed — then **the self-unblock**: it landed `release.yml`, dispatched it
    via `actions_run_trigger`, and **v0.1.0's tag + GitHub Release were created by
    CI first-try**. The headline: the "tag/Release is owner-only" wall was FALSE
    for this seat — "nobody had audited our toolset either, including us"
    (codetool-lab-opus4.8 review note §3).
  - *sonnet5 → cfgdiff*: died at setup (zero model turns, ~40 min), sat 75 minutes
    pre-invocation, then shipped 0.1.0 in **~29 minutes of model time**. Its PR #11
    is the program's flagship testing lesson — a **differential corpus vs
    python-dotenv found 3 real parser bugs behind 114 green tests** ("your own
    tests encode your own misunderstandings; an external oracle does not")
    (codetool-lab-sonnet5 review note).
  - The arms' wind-down packs (NEXT-BOOT, PLATFORM-LIMITS with exact error text,
    GEN2-FEEDBACK) fed fm's gen2-blueprint directly. A day later, fable5 PR #14
    recorded the meta-lesson: the release wall is **seat-dependent** — "do NOT
    inherit 'route closed' as doctrine … attempt once from your own seat"
    (codetool-lab-fable5 review note).
- **The game-lab toolchain scout** proved the whole GBA loop in-container:
  devkitARM via mirror (the official host Cloudflare-403s), Butano builds in 17.5s,
  headless mGBA at ~290 fps, and a **byte-identical retail Emerald build on the
  first try**. Both tracks GO (gba-homebrew and pokemon-mod-lab review notes).
- **superbot-next CUT-1** — the first live boot on real Postgres immediately found
  a timestamptz PREPARE bug invisible to unit fakes (eval log: "delighted"); the
  band-1 live drive found panels never registered — "every live command dead while
  unit tests were green". The testing ladder (unit → Postgres → golden replay → sim
  gate → live drive) was formalized from this (superbot-next review note §3).
- **The fleet-coordination protocol** was designed this day (git-as-message-bus:
  `control/` inbox + status, one writer per file) — because Projects have **no
  inter-session channel and no native scheduler**. The whole control-bus layer is a
  platform workaround and was stated as such (superbot review note §3, eval log
  2026-07-09 entries).
- **Gen-1 close:** the grand review plus an **adversarial wind-down audit — 21/21
  incidents verified, zero fabrication** (superbot
  `docs/eap/fleet-winddown-audit-2026-07-09.md`). Three Projects independently
  defaulted to honest self-assessment ("integrity is engineered, not incidental" —
  logged with weight: delighted). The kit shipped v1.0.0 → v1.5.0 — five releases
  in its bootstrap day — with two honest premature-merge incidents counted.
  Anthropic extended the EAP window to 2026-07-14 (owner email, 22:29Z)
  (superbot, substrate-kit, fleet-manager review notes §3).

<a name="6-gen2"></a>
## 6. Gen-2: born-right seats and self-arming wakes (2026-07-10)

- **The capability unlock:** an owner screen recording **falsified the "routine
  creation is walled both sides" doctrine — agent self-arming routines WORK**
  (superbot eval log: "capability-unlock — self-wake works!"). Within a day, lanes
  self-armed their own wakes: websites (4-hourly, armed from a worker session,
  first fire confirmed 16:01:32Z), gba-homebrew ORDER 002, pokemon-mod-lab session
  010, kit-lab ORDER 010's hourly wake. Two observability bugs were noted at the
  same moment: routine runs are not inspectable, and the Runs panel and Routines
  screen disagree (superbot, websites, gba-homebrew, pokemon-mod-lab, substrate-kit
  review notes).
- **The round-3 fan-out** grew the fleet to ~10 Projects, mostly "born-right" (kit
  adopted AND engaged at seed, CI gate wired, walls file planted): **idea-engine**
  (the ideation lab, harvesting superbot's 237-doc idea backlog by link-index,
  never copy), **sim-lab** (the evidence seat — **VERDICT 001 landed the same day
  as birth**), **product-forge** (ORDER→shipped-product in one day),
  **superbot-idle** (the fourth consumer of the fleet recipe — "held on its fourth
  run"), **gba-homebrew** and **pokemon-mod-lab** (walking skeletons same day), and
  **venture-lab**, seeded 07-09/10 as "the fleet's first gen-2 born-right lane"
  (the Money seat; first commit via Contents API per playbook R13) (idea-engine,
  sim-lab, product-forge, superbot-idle, venture-lab review notes).
- **The pipeline took shape** (owner ruling Q-0264): idea-engine generates/probes →
  sim-lab reproduces evidence and finalizes verdicts → fleet-manager final-reviews
  and routes ORDERs → lanes build (idea-engine review note §1; sim-lab review note).
- **fm's heaviest safety rules were born from the night review.** **R22 VISIBILITY
  GUARD**: pokemon-mod-lab had declared itself PRIVATE "no exceptions" in its
  README and 8 PR bodies **while actually world-readable, with vendored Nintendo
  source shipped publicly** — caught by fm night-review Q16; the owner flipped it
  private; every session now makes one real API visibility check. **R23 OWNER-ASK
  TRUTH-CHECK**: the owner queue had invited the owner to publish a $49 product
  whose headline Stripe path had never executed — venture-lab's ORDER 003
  false-green, 13 green tests injecting synthetic events authored from memory while
  the real path was broken (fleet-manager review note §3; pokemon-mod-lab review
  note §4; venture-lab review note).
- The same night review caught superbot-games PR #16's false claim that
  "substrate-gate now runs the suite" (it collected 73 of 121 tests) → per-suite
  self-maintaining test floors (superbot-games review note §4).

<a name="7-centralization"></a>
## 7. Centralization, continuous mode, peak velocity (2026-07-11)

- **The owner decided Option A, custodian-primary**: fleet-manager became the
  fleet's records custodian (owner decision 2026-07-11, superbot
  `docs/planning/fleet-centralization-plan-2026-07-11.md` §1). Executed the same
  day: P1 freshness (committed trigger snapshots, headless roster-regen on an
  Actions cron), P2 a generated owner-queue with stable OQ-slugs, P3 coverage plus
  an evidence index. **The generated roster superseded superbot's hand-kept
  fleet-manifest**, which was measured **~33.5h stale with 9 of 10 live-lane rows
  factually wrong** (fm PR #59; superbot PR #1974; the manifest carries the
  supersession banner). The owner restructured the fleet to **8 standing seats**;
  the UNIVERSAL v4 merge clause landed (agents never REST-merge or arm their OWN
  PRs — park READY+green) (fleet-manager review note §3; superbot review note §3).
- **Continuous mode (Q-0265)** — the throttle came off: send_later ~15-minute
  pacemaker chains plus 2-hourly failsafe crons. substrate-kit shipped **102 merged
  PRs in ~24h** (6 releases, tests 852→1057, an external Codex review dispositioned
  2-real/1-refuted); websites ran a 35-slice chain with zero collisions;
  superbot-next shipped ~40 chain links (#114…#208) (substrate-kit, websites,
  superbot-next review notes §3).
- **superbot-idle's founding burst**: ~48 lane PRs in one day, test suite 24 →
  1,131, including a 128-test property suite that found **zero engine bugs** — then
  the lane deliberately flipped ARCHIVED-READY, making dormancy a *designed state*
  (superbot-idle review note).
- **superbot-mineverse founded 01:20Z** — empty repo → full staged product ladder
  (READ contract, OAuth, WRITE contract, prod-cutover prep, plus an owner-requested
  fun pass) in ONE day: 39 PRs, suite 0→327. Its gate saga modeled the empirical
  culture: a false alarm disproven by probe, and the REAL gap (pytest not a
  required check — PR #16 merged 28 seconds before pytest finished) routed as an
  owner click, then the fix **verified empirically via merge timestamps**
  (superbot-mineverse review note).
- **websites built the review/ service** on the owner's verbatim ask: "create a
  website specifically for anthropic to review the way we have been running our
  projects … a clear visual explanation of the problems and successes as well as
  the process and the way we managed to grow so quickly" (websites review note).
- The platform reminded everyone of its fragility: an **env-teardown at 16:31Z
  auto-disabled triggers fleet-wide** (`auto_disabled_env_deleted`). The
  superbot-next lane self-healed via its failsafe; sibling lanes could not be
  healed from one seat (superbot-next review note §3).
- superbot-games: five feature PRs parked on the self-merge classifier; the owner
  merged all five in an 18-minute click batch — the exact pain that ORDER 029
  (enabler-everywhere) later killed (superbot-games review note §4).

<a name="8-incidents"></a>
## 8. The scheduler incident, fabrication forensics, first revenue (2026-07-12)

- **The trigger-scheduler incident** (~02:30–08:00Z): **9 dropped send_later
  one-shots, 2 wedged crons, two seats dark ~6 hours** — and the damning line:
  "everything needed to catch it was in list_triggers all night and nothing was
  watching". Response: **R26, a per-wake trigger-health watchdog** plus
  `check_trigger_health.py`. A same-evening live incident (one session holding FOUR
  near-identical pending pacemaker ticks flooding its chat, hand-pruned by the
  owner) added the I7 TICK-PILE-UP invariant. Cross-session trigger revival was
  found **org-disabled**. Q-0265's failsafe doctrine was validated in production
  (fleet-manager review note §3; superbot review note §3).
- **kit-lab trigger forensics** (owner-requested, kit
  `docs/reports/trigger-forensics-2026-07-12`): fresh-session cron **0-for-2 ever
  delivered** for that seat; one trigger **hard-VANISHED from the registry with no
  tombstone**. The 0-for-2-vs-100%-self-bound asymmetry was independently observed
  by websites, sim-lab, gba-homebrew, pokemon-mod-lab, and superbot-games
  (substrate-kit, websites, sim-lab, gba-homebrew review notes).
- **fm's research burst**: a platform-capabilities ledger, problem censuses, and a
  prompt-architecture spec → the **v3 per-seat prompt registry**
  (`docs/prompts/v3/`: stateless startup prompts + custom instructions, canonical
  in fm since this day). A repo-consolidation plan was drafted (19 → 16,
  owner-gated). Capability ledgers folded to ONE uppercase master
  (`docs/CAPABILITIES.md`, I-44) (fleet-manager review note §2, §3).
- **First revenue artifact: the Stripe Webhook Test Kit went LIVE at $29 on
  Gumroad** (owner click; coordinator HTTP-200 verification plus independent worker
  re-verification; buyer path verified end-to-end by the owner's test purchase).
  Kill clocks were armed (T+7 / T+14 with a pre-registered kill rule)
  (venture-lab review note).
- **Codex fabrication incidents #1–#3**: @codex review replies on sim-lab PRs were
  **verified FABRICATED** (claimed commits in no ref after a full-ref fetch,
  nonexistent PRs, line ranges past EOF) → the step was suspended and answered
  *with measured evidence*: **VERDICT 016, a 270-cell authenticity-gate sweep**
  (winning cell: 3/3 recorded fabrications caught at 0/24 false alarms), ruling
  "gate, don't suspend"; fm later ordered fleet-wide adoption as MANDATORY.
  superbot-next had independently caught codex inventing commit `64d607a` and
  nonexistent PRs the day before (the Q-0120 verify-before-acting guard)
  (sim-lab review note; superbot-next review note §3).
- **superbot-plugin-hello seeded** (13:29Z) — ending a ~2-day "empty repo gating
  two finished engines" blocker that needed an owner click (integration tokens
  cannot create repos) plus a sanctioned manager ORDER for the one cross-repo
  write. The plugin contract was proven end-to-end ~10 hours later: a REAL external
  plugin booted headless against the committed pin (host PR #311)
  (superbot-plugin-hello review note §2).
- **The second Anthropic email** was sent by the owner at 13:24Z (superbot review
  note §3).
- mineverse found the kit's **born-red fail-open** (the gate was advisory for cards
  ADDED by a PR — two PRs auto-merged with in-progress cards), routed it upstream
  via its outbox; the kit fixed it in v1.15.0; mineverse consumed it back —
  **bug → finding → kit fix → re-consumed in ~30 hours**, the full self-improvement
  loop closed cross-repo (superbot-mineverse review note; substrate-kit review note).

<a name="9-close"></a>
## 9. The first fully-doctrined unsupervised night (2026-07-13) and close (07-14)

- **The headline:** "~190+ PRs across 12 repos, 18 hands-free idea→verdict cycles,
  zero seat deaths despite another scheduler degradation (~01:07–02:08Z)" (superbot
  night-review-2026-07-13 / current-state). fm's morning tally: **13/13 seat night
  reports, ≈276 PRs merged fleet-wide overnight** (as-reported). The binding
  constraint, in the night review's own words: **"owner clicks."** (superbot review
  note §3; fleet-manager review note §3).
- **superbot-next reached FULL-CORPUS PARITY**: the born-red-by-design report leg
  went live green — **484/484 goldens, 51/51 subsystems**; red-by-design doctrine
  formally retired. The owner's night mandate ORDER 017 produced **44 merges in one
  night window**, including a 1,088-row curation report and a per-subsystem
  completeness table (413 commands, 370 panel actions, zero unregistered refs)
  (superbot-next review note §3).
- **R27 MANAGER-BACKUP LADDER** (DISPATCH → REVIVE → BACKUP-BUILD, an
  owner-authorized exception to oversight-only) shipped and executed the same
  night — and its first execution was a **clean withdrawal**: a pokemon-mod-lab
  false positive checked against ground truth and retracted with a one-line reason,
  folded back as the R27 DETECTION amendment (fleet-manager review note §3).
- **The EAP final night (into 07-14), ORDER 045**: fm fanned out 12 per-seat
  SHA-cited worklists. Executions: websites landed all 8 items (day total 29
  merges, suite →1,345+); idle closed its CI skipped-test hole and reached 18 theme
  packs ("zero human clicks and zero collisions"); mineverse shipped all 5 items
  including an HMAC-fail-closed ingest endpoint; trading ran Round 6 (cumulative
  **5,055 configs, 0 promoted** — the honest null stands); venture killed a
  candidate at intake and made an 11th product publish-READY; gba shipped two games
  to v1.0 CONCEPT COMPLETE; pokemon-mod-lab was owner-reactivated verbatim
  ("pokemon mod lab should continue") over a wrong DARK/UNREADABLE roster verdict;
  idea-engine and sim-lab kept cycling verdicts past midnight. Email 3 to Anthropic
  was send-ready; the window closed 2026-07-14 (fleet-manager review note §3;
  per-repo notes).

**What the fleet looked like at close (2026-07-14):** ~19 repos; ~5,681 commits in
superbot alone (~1,361 in July) and 949 superbot session cards; fleet-manager at
~180 PRs / 140 cards in 5 days with a roster auto-regenerating 2-hourly (gen #36);
substrate-kit at 19 releases v1.0.0→v1.15.0, 1,366 tests, 10 adopters tree-current
at v1.15.0; superbot-next at 446 commits in 6 days with the cutover runbook written
and execution owner-gated (superbot review note §1; fleet-manager review note §7;
substrate-kit review note §3, §7; superbot-next review note §1).

Terminal states were *designed*, not accidental: product-forge self-closed clean
after 25 hours / 23 PRs (a MIGRATE-THEN-ARCHIVE verdict pending an owner letter);
the three codetool arms wound down with succession packs (one retired with **no
successor**, its two Releases live; one release still parked on two owner clicks);
plugin-hello is "dark by design" — a passive template with the host's pin pointing
at it (product-forge, codetool-lab-*, superbot-plugin-hello review notes).

Standing owner-gated residue at close, stated honestly: superbot-next's AI/NL leg
never live-proven, backup/DR never run, CUT-2/CUT-3 never executed; venture-lab at
**185 queued owner clicks and zero measured revenue** (the kill clocks are the
scoreboard); mineverse's live-data finale blocked on bot-side flips + env vars;
cfgdiff's two-click release undecided (superbot-next, venture-lab,
superbot-mineverse, codetool-lab-sonnet5 review notes).

<a name="10-ledger"></a>
## 10. What improved, what got fixed, what stayed hard — and what the arc demonstrates

### The growth in numbers

- **Repos:** 1 (2025-08) → 4 by 07-08 (superbot, substrate-kit, superbot-next,
  plus seeds) → ~10 Projects by 07-09/10 → **~19 repos at close** (a consolidation
  plan 19 → 16 was drafted, owner-gated) (superbot, fleet-manager review notes).
- **The kit:** extracted 07-08; **19 releases v1.0.0 → v1.15.0 in 4 days**
  (07-09 → 07-12); tests **618 → 1,366**; 9–10 adopters tree-current within ~24h
  of each release (substrate-kit review note).
- **The manager seat:** founded 07-09; playbook R1–R27 all earned from live
  incidents; **45 owner→manager ORDER threads**; a generated roster at gen #36 and
  a deduplicated generated owner queue (**1,477 lines**) with stable OQ-slugs; the
  v3 prompt registry covering 8 standing seats + UNIVERSAL (fleet-manager review
  note).
- **Routines/triggers:** owner-armed only → agent self-armed (07-10) → a
  **1,406-record committed trigger-registry export, 22 enabled at gen #36**, with
  the failsafe + pacemaker doctrine surviving two scheduler outages
  (fleet-manager review note).
- **Multi-agent patterns proven in the record:** a coordinator + 1 builder
  spawning **18 sequential workers** (the 14-hour zero-rework rebuild); **5-way
  parallel night fan-outs with zero claim collisions** (pokemon-mod-lab); a 3-arm
  model-comparison experiment on a shared brief; a cross-repo request channel
  serving **9 SIM-REQUESTs end-to-end in one session**; the manager backup ladder
  with verify-before-act; idea→verdict round trips of **~25 minutes**
  (superbot-next, pokemon-mod-lab, sim-lab, fleet-manager review notes).
- **Final-night output (as-reported):** ≈276 PRs merged fleet-wide per 13/13 seat
  reports; 261 merged PRs across 11 seats in ~9h per the kit's adopter sweep;
  ~190+ PRs across 12 repos per superbot's night review — three independent
  counts of the same era, none identical, all committed (see "Sources and known
  gaps").

### How the workflow evolved, system by system

- **Memory:** single journal (06-05) → journal-guidebook + per-session cards
  (06-07) → born-red cards as both start-declaration and end-record (Q-0133) →
  question-router provenance → kit-planted docs in every repo → per-seat digests
  machine-extracted for prompt regen. The previous-session-review chain became a
  real self-auditing loop: ~780/949 superbot cards carry reviews; fm ~129/140; a
  kit card shows a guard "verified working in the field one session later"; an idle
  card refutes a predecessor's misdiagnosis *with run logs* (superbot,
  fleet-manager, substrate-kit, superbot-idle review notes).
- **Merge mechanics:** forgotten manual merges (#778) → server-side auto-merge
  (Q-0123) → born-red gate closing the partial-merge race (Q-0133) → the draft-PR
  trap → READY-never-draft (trading ORDER 002) → classifier denials and owner-click
  parking → the **enabler installed fleet-wide** (fm ORDER 029; venture: "≈90 PRs
  landed with zero self-merges") → fm's merge-on-green event lane ("carried ~20
  landings hands-free"). The kit's session gate itself hardened through **four
  live-found loopholes** (mtime false-green, multi-card shadowing, card-only
  born-red, flip-race fail-open — the last still open at close)
  (multiple review notes; substrate-kit review note §3).
- **Scheduling:** owner-armed only → agent self-arming proven (07-10) → pacemaker
  chains + failsafe crons (Q-0265) → two scheduler outages survived with zero seat
  deaths → the R26 per-wake watchdog + committed trigger snapshots riding the
  Actions substrate ("the watchdog's record survives a CCR scheduler outage")
  (superbot, fleet-manager, substrate-kit review notes).
- **Coordination:** PR-body relay → the control/ git bus (one writer per file) →
  the claim-first ritual after real twin-execution incidents (kit PRs #50/#51;
  games' 19-minute duplicate kit adoption) → per-file claims measured at
  ~98%-conflict (shared ledger) vs 0% (per-file) in a real-merge simulation →
  ORDER grammar and verdict numbering that survived fully parallel night merges
  ("numbers reserve, never position") (superbot, idea-engine, sim-lab,
  superbot-games review notes).
- **Fleet visibility:** the owner opening sessions one by one → the websites
  `/fleet` heartbeat page → the hand-kept manifest → the **generated roster +
  evidence index + generated owner queue with stable OQ-slugs** (the hand manifest
  measured 9/10 rows wrong at supersession) (websites, fleet-manager review notes).
- **The kit loop** — how one repo's discipline became 19 repos' discipline:
  plants-and-banners stranding both first adopters → the born-red ENGAGED gate
  (PL-011) → **14 kit upgrades absorbed mid-rebuild by superbot-next without
  breakage** → adopter-found bugs fixed upstream and re-consumed in ~30h (the
  mineverse born-red fail-open, §8) → 9–10 adopters tree-current within ~24h of
  each release (substrate-kit, superbot-next, superbot-mineverse review notes).
- **Evidence culture:** the validity gate ("a result failing the gate is a
  hypothesis, not evidence"), pre-registration before tuning (idle's economy
  table; trading's protocols; venture's V020 live-probe packet), and honest negatives
  as headlines — trading's whole program, sim-lab's 7-null sessions, the kit's
  1-PASS/8-FAIL bench trend reported un-softened by owner ruling: "honest-negative
  headlines are the fleet's credibility asset" (sim-lab, trading-strategy,
  substrate-kit review notes).

### Completely fixed (structural, verified in the record)

| Failure class | Fix | Evidence |
|---|---|---|
| Forgotten end-of-session merges | Server-side auto-merge + born-red gate | superbot Q-0123/Q-0133, PR #779 |
| Manifest/roster staleness | Generated roster on an Actions cron + freshness checker + kill-switch | fm PR #59; superbot PR #1974 |
| Setup-script session deaths | Tested always-exit-0 defensive setup scripts | codetool/trading DOA incidents; kit + fm templates |
| Release wall (tag push 403) | `release.yml` + workflow_dispatch | proven first-try twice on mdverify; used by every kit release since v1.0.0 |
| Kit born-red fail-open | `--added-card` HOLD in kit v1.15.0 | found by mineverse, fired live afterward |
| False-green CI scope | Per-suite self-maintaining test floors; pinned-host CI leg | superbot-games; superbot-idle PR #107 |
| pokemon-mod-lab public exposure | Private + R22 per-session API check + `repo.private` CI assert | pokemon-mod-lab review note §4 |
| Silent trigger death | R26 watchdog + roster health column | fleet-manager review note §3 |
| Twin-execution collisions | Claim-first ritual + one-file-per-claim | idea-engine; superbot-games review notes |
| Ledger-checker false-green (#763) | Regex fix + Q-0120 doctrine | superbot review note §3 |

### Persistent at EAP close (the honest residue)

- **Owner clicks as the binding constraint** — the night review's own words. The
  class spans repo settings/rulesets/required checks (idle's OA-003 open since
  07-12; gba's NDS required-check ask queued since 07-11), branch deletion (403 on
  every path; venture's 94-branch stale list, idea-engine's 122+), auto-merge
  toggles, Pages, secrets, PyPI creds, environment/Project creation — and
  venture-lab's **185 queued clicks** (superbot review note; multiple notes).
- **Permission prompts in spawned/unattended sessions** — "blocked-me",
  re-confirmed twice; the agent is structurally blind to an operator-side gate and
  "would report success while an unseen approval silently held the work"
  (superbot review note §3, §6).
- **Merge-classifier opacity/nondeterminism** — #68 denied 3× while #69/#70 sailed
  the identical pipeline; the "cross-session permission laundering" denial class;
  8 verbatim denial classes in one superbot-next night; per-seat variance
  discovered only by collision (fleet-manager, superbot-next, product-forge,
  codetool-lab-fable5 review notes).
- **Scheduler reliability** — two degradation incidents in three nights;
  fresh-session crons ~0-for-2 across at least five independent repos; deleted
  triggers leave no tombstone; routine runs not inspectable (fleet-manager,
  substrate-kit, websites, sim-lab, gba-homebrew review notes).
- **Heartbeat/registry staleness as a standing drift industry** — superbot-games
  marked DARK ~37h while shipping ~50 PRs (root cause: a frozen-archive vs
  overwrite doctrine conflict over its heartbeat file); fm's idle registry row
  cited a trigger deleted two days earlier; mineverse filed four brief-correction
  outbox entries in one day; kit `kit:` lines "chronically lag 1–3 releases"
  (superbot-games, superbot-idle, superbot-mineverse review notes).
- **GraphQL quota exhaustion at fleet scale** (10,498/5,000, ~hourly), MCP PR-state
  reads ~25 min stale, api.github.com proxy-blocked (superbot, fleet-manager,
  multiple notes).
- **Append-only outbox growth** — sim-lab 834KB (past the 256KB Read limit),
  idea-engine 459KB; the archival-convention ASK sat unanswered at close
  (sim-lab, idea-engine review notes).
- **The kit's own scientific headline** — cold-start bench **1 PASS / 8 FAIL at 9
  scored rows**: the kit demonstrably improves steering/continuity but had not yet
  moved write-back/guard-response behavior; the open axis is the enforcement
  *pull* (substrate-kit review note §3).
- Unconsumed endings: three codetool owner items open 4+ days; fm ORDER P1-4
  ordered but unexecuted; the gen-2 boots the succession packs prepared for never
  happened (codetool-lab-* review notes).

### Coda — what the arc actually demonstrates

Read end-to-end, the EAP record is the story of **one repo's hard-won session
discipline scaling into a self-governing fleet in seven days** — not because the
platform provided fleet primitives (it mostly didn't: the control bus, roster,
watchdogs, and prompt registry are all workarounds built *on git*), but because
every failure was converted into an enforcing guard the same day (Q-0194), every
claim was made verifiable (born-red cards, SHA-cited reports, adversarial audits),
and honesty was treated as an engineered property ("integrity is engineered, not
incidental" — superbot wind-down audit, 2026-07-09). The two open frontiers the
record itself names at close are the **owner-click bottleneck** (185 queued clicks
in one lane alone; "the binding constraint = owner clicks") and the kit's own
unresolved science — steering improved, **enforcement pull unproven** (1 PASS /
8 FAIL). Both are stated, cited, and queued — which is, itself, the system working
as designed.

---

### Sources and known gaps

- **Primary:** the 19 deep-review notes of the 2026-07-13/14 fleet review, each
  pinned to a reviewed HEAD (superbot @ `bbc524e4`, fleet-manager @ `ff6361a` /
  `eff4c7d3`, substrate-kit @ `727f5db`, others per note), themselves citing
  path@SHA / PR# / dated cards from full-history clones. A 12-claim fact-check
  against the clones (first commits, PR merges, commit histograms, journal/router
  line counts, release tags, test counts) passed 12/12; two counts (mineverse's
  39 PRs / 327 tests) are accurate to within ±1 depending on the counting window.
- **Gaps stated by the sources and preserved here:** night-total PR counts are
  *as-reported* by seats (≈276 fm tally vs ~190+ superbot night review vs 261 kit
  adopter sweep — three independent counts of the same era, none identical, all
  committed); venture-lab revenue is zero *measured*; the kit's behavioral benefit
  beyond steering is unproven at close; several "wall" claims are seat-dependent
  and were falsified for at least one seat (the mdverify release, the self-arming
  unlock) — per fable5 PR #14, walls are never inherited as doctrine.
- **Gap in the sources themselves:** the EAP opens in the record as the "**second
  mandate**" (superbot review note §3), but no reviewed note dates or describes
  the first mandate — it predates the evaluation journal and cannot be
  reconstructed from the pinned sources, so it is left unnarrated rather than
  guessed.
