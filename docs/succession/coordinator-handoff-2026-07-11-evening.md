# Coordinator succession handoff — 2026-07-11 (evening)

> **Status:** `reference` — succession handoff, written at the 2026-07-11
> **evening** archive of coordinator session `session_012o8pySy5K3AV6JWoPKryZL`
> (a.k.a. `cse_012o8pySy5K3AV6JWoPKryZL`). **This is the successor
> coordinator's ONE-READ state doc.** Boot flow: the owner pastes
> `projects/fleet-manager/reboot-prompt.md` **v2** into a fresh coordinator
> chat; that prompt routes here. Supersedes the morning handoff
> (`coordinator-handoff-2026-07-11.md`, written at the 01:0xZ archive of the
> *predecessor* seat) as the current-state doc; the morning doc stays valid
> as history (its §4 permissions-fold recipe was executed via PRs #76/#77;
> its §6 walls ledger still applies).
>
> Written by the archive-prep close-out worker (fable-5 family), dispatched by
> the archiving coordinator. Everything marked **verified** below was checked
> against git / the GitHub API / the live trigger registry at close-out
> (~21:2x–21:4xZ, origin/main `cddcb95`); items the worker could not verify
> are attributed "(reported by coordinator, unverified)". Source precedence
> unchanged: repos at HEAD > this doc > memory of any chat.

## 1. Seat tenure summary (what this archive contains)

- **Tenure:** booted ~01:04Z 2026-07-11 (F-1 cutover from the predecessor
  seat — failsafe `trig_01F9UdoUtLy8oknBPBkHLshS` created 01:04:10Z, verified
  live) → archived 2026-07-11 evening (~21:xxZ).
- **fleet-manager PR arc #57–#86 — ALL MERGED (verified against git history
  at `cddcb95`):** every number in 57..86 has a merge commit on main (#76 via
  merge-commit `e1848ff`, the rest as squash suffixes; spot anchors: #77
  owner-merged `39b888a`, #85 `70c9520`, #86 `cddcb95` = HEAD).
- **The fleet centralization plan is BUILD-COMPLETE and LIVE** (superbot
  `docs/planning/fleet-centralization-plan-2026-07-11.md`, Option A
  custodian-primary; P1 = fm #81–#84, P2 = #85, P3 = #86 — all verified
  merged):
  - headless roster regen cron `40 */2 * * *`
    (`.github/workflows/roster-regen.yml`) + committed trigger snapshot
    (`telemetry/triggers-snapshot.json`, 702 records) + freshness alarm
    (`scripts/check_roster_freshness.py`, 4h bar; BLOCKING on `claude/*` PRs
    via `roster-freshness.yml`);
  - owner-queue candidate feed (`docs/owner-queue-candidates.md`, generated) +
    `scripts/check_owner_queue.py` (merged-PR citation prober) + stable
    `OQ-<slug>` ids on every queue item;
  - `docs/evidence-index.md` (generated) + `docs/fleet-triage.md` (ported);
  - `scripts/gen_roster.py` **GRADUATED VERIFIED** (run 3: verdicts 8/8 vs
    independently-fetched ground truth; kill-switch kept) — roster is at
    generation #9 (20:25Z).

## 2. Merge-authority doctrine (the seat's hardest-won operating rule)

- **In-session human authorization clears the merge wall; RELAYED
  authorization never does.** Verified record: `control/status.md` PR #71
  slice record — fm #68 was classifier-denied 3× and landed only via an
  owner-authorized in-session attempt ~11:48Z, while #69 (agent-merged 06:54Z)
  and #70 (09:02Z) bracketed the wall, ruling out PR metadata / repo state /
  timing. Denial text on #68 verbatim in
  `docs/findings/enabler-install-verification-2026-07-11.md`
  ("[Self-Approval]/[Merge Without Review]").
- **Fallback when denied:** park the PR GREEN + non-author review comment +
  owner click. Never retry around a guard denial (deny-wins).
- superbot-games declined fresh-session merge attempts for its own parked PRs
  — its denials named **relayed authorization** explicitly (reported by
  coordinator, unverified; consistent with games' heartbeat at roster gen #9:
  "all deliverables parked on branches for owner merge").

## 3. OPEN WATCHES (successor picks these up)

1. **roster-regen cron has NEVER fired on schedule.** Verified via the
   Actions API at close-out: `roster-regen.yml` has exactly **3 runs, all
   `workflow_dispatch` (manual), zero `schedule` events** — run 1
   (29164975251, failure: GH013 direct-push denial), run 2 (29165152964,
   failure: PR-create denied `GitHub Actions is not permitted to create or
   approve pull requests`), run 3 (29165508699, success on the v3
   honest-degrade path, #83). **Next scheduled slot to watch: 22:40Z
   2026-07-11.** Until the owner ticks OQ-FM-ACTIONS-PR-PERMISSION the cron
   cannot land its regen PR itself (v3 degrades honestly instead of failing
   red). If the cron *still* doesn't appear in the run list at 22:40Z, that
   is a new, separate defect (scheduler-side) — file it with the run-list
   evidence.
2. **9 lane failsafes auto-disabled (env deleted).** Verified against the
   committed `telemetry/triggers-snapshot.json` (19:07Z export): 11 records
   carry `ended_reason=auto_disabled_env_deleted` — the 9 lane failsafe crons
   (product-forge, idea-engine, superbot-games, substrate-kit, Builder/
   superbot-next, sim-lab, superbot-idle, venture-lab, trading-strategy) +
   the kit-lab daily loop + one Builder one-shot; record `updated_at` stamps
   16:31–16:33Z (the env deletions themselves 14:45–16:16Z per the gen #6
   headline and `telemetry/README.md`). **The owner was asked whether this
   was a deliberate rebuild or an incident and NEVER ANSWERED** (reported by
   coordinator, unverified — no answer recorded in `control/inbox.md` or the
   owner queue). Gen #6 headline: 8 live lanes went **chain-only, with
   silent-dark risk** — a chain-only lane that stalls has no dead-man wake —
   until the paste sitting / trigger re-seat re-arms them. Note: superbot-next
   has since been re-seated (roster gen #9 shows a live Builder failsafe
   `trig_01GLBYyf4aDS6AwpLVybZvVy`, last fire 18:06Z), and superbot-mineverse
   / retro-games / pokemon / gba wakes are alive; venture-lab, superbot-games,
   product-forge and codetool ×3 show wake state **NONE** at gen #9. Live
   registry residue at ~21:3xZ: only 3 of the 11 disabled records remain
   listable (Builder failsafe, trading-strategy failsafe, Builder one-shot) —
   the others no longer appear in `list_triggers` output.
3. **superbot-games `control/status-mining.md` has an unparseable `updated:`
   stamp** — verified at roster gen #9: the sub-row is DEAD (not measurable),
   heartbeat cell reads `2026-07-11T (archive-prep VERIFY + TOP-UP; …)`.
   Lane-side fix — route an order or ride the next games contact.
4. **product-forge / trading-strategy / superbot-games STALE watches**
   (reported by coordinator). At roster gen #9 (20:25Z) all three read FRESH
   — but all three phases are close-out/archive ("close-out / archived-ready",
   "ARCHIVE-READY", "close-out + archive-prep"), so they will drift stale as
   their seats archive. Watch, don't act, unless a lane claims live work and
   goes dark.
5. **2 legacy substrate-kit heartbeat files DARK >30h** — verified at gen #9:
   `control/status-gba-homebrew-trackb.md` (~39h) and
   `control/status-superbot-coordinator.md` (~30h), both wound-down seats.
   Retirement candidates (reported by coordinator; the files describe
   completed/archived lanes — retiring them removes two permanent DARK
   sub-rows from the roster).

## 4. Pending owner items at archive (verified against `docs/owner-queue.md` @ `cddcb95`)

The queue file is the canonical click-list; verified present and current:

- **OQ-PASTE-WAVE** (item 15) — the paste sitting, **CLICK-READY** since PR
  #77 merged (`39b888a`, owner, 18:40Z). One sitting, v2 bodies everywhere
  (v3 for superbot-games). This is also what re-seats walled seats'
  instructions after the failsafe wipe-out (watch #2).
- **OQ-ENV-SETUP-REPASTE** (item 14) — re-paste consolidated env setup
  scripts, **COORDINATOR ENV FIRST** (the PR #73 python3.11 fix is inert
  until pasted).
- **OQ-FM-ACTIONS-PR-PERMISSION** — tick "Allow GitHub Actions to create and
  approve pull requests" in fleet-manager settings; unblocks the roster-regen
  cron's PR path (watch #1). Wall evidence verbatim in the queue item.
- **OQ-SITTING-0714-DECISIONS** (item 28) — the 2026-07-14 bundled sitting,
  now FOUR decisions, one with a **HARD deadline ≤2026-07-13** (post-EAP
  routine posture). Window ends 2026-07-14.
- **(D) External services section** — venture-lab Stripe keys
  (OQ-VENTURE-STRIPE-KEYS) + publish clicks + gotcha article, websites
  Railway/Postgres + PAT, product-forge Pages (OQ-FORGE-PAGES), itch.io lumen
  publish (OQ-ITCH-LUMEN-PUBLISH, rides the 07-14 sitting).
- Parked with a date: the **Anthropic email pack** — review + send before the
  2026-07-14 window close.

No mismatch found between the coordinator's reported pending list and the
committed queue.

## 5. Standing decisions in force

- **Option A (fleet-manager = records-custody primary)** was assumed +
  flagged at P1 (decide-and-flag) and **never vetoed** — verified: every
  P1/P2/P3 heartbeat stamp records "Option A custodian-primary in force"; no
  veto anywhere in `control/inbox.md` or the queue.
- Q-0265 continuous mode; Q-0089 idle-honesty (never re-arm a chain on empty
  work); deny-wins on guard denials; decide-and-flag over stop-and-ask;
  verify against git, never self-reports (Q-0120).

## 6. Work ladder for the successor (after the reboot-prompt v2 cutover)

1. Heartbeat the takeover (`control/status.md`).
2. Watch the 22:40Z roster-regen cron slot (watch #1) — record fired /
   not-fired with run-list evidence.
3. Dump a fresh `list_triggers` export → `telemetry/triggers-snapshot.json`
   (REQUIRED wake step per `coordinator-prompt.md`) — this also settles the
   watch-#2 registry-residue question with a git diff.
4. Roster regen (R25) if >2h old at boot; the generator is graduated — trust
   but keep the kill-switch.
5. Owner-queue sweep via `scripts/check_owner_queue.py`; curate
   `docs/owner-queue-candidates.md` intake.
6. Lane contacts as ORDERs/replies arrive; retire the two legacy kit
   heartbeat files (watch #5) via a kit-lane order when convenient.
7. Standing enders every slice: born-red card first commit, heartbeat + flip
   complete LAST, REST squash on green, claim file per
   `control/claims/README.md`.
