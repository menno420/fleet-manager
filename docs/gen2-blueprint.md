# Gen-2 blueprint — Phase-2 (born-right) Project seed standard

> **Status:** `binding`
>
> Drafted 2026-07-09 at succession, synthesized from the fleet's own retros
> ([`findings/retro-synthesis-2026-07-09.md`](findings/retro-synthesis-2026-07-09.md)
> — especially the 13 cross-patterns and the lanes' F1/F4 prescriptions), the
> quality-review prescriptions, and the launch kit experience. Gen-1 texts
> being revised: [`prompts/README.md`](prompts/README.md).
>
> **Changelog:** 2026-07-09 (late evening) — finalized by the successor
> session per [`handoff-2026-07-09.md`](handoff-2026-07-09.md): measured
> ping read-latencies folded into §2a wake cadence, §5 open items resolved
> (retro deliverables reconciled at HEAD, venture-lab founding text
> finalized), status `plan` → `binding`.
> 2026-07-09 (night) — **merge-authority policy** (owner directive
> 2026-07-09): §1 conventions bullet + §2 delta 2 rewritten — every gen-2
> lane always lands its own PRs; review is post-merge
> ([`review-queue.md`](review-queue.md)); do-not-automerge/owner-gated-merge
> patterns killed for gen-2 lanes.
> 2026-07-09 (night, later) — **landing-path mechanics aligned with playbook
> R21** (fleet-manager PR #10 + venture-lab PR #1 evidence): REST
> merge-on-green is the PRIMARY landing path on born-red and no-CI repos;
> arm-at-creation is primary only where a check can go pending.
> 2026-07-09 (night, later still) — **CI-TIER STANDARD added (§2b)** (owner
> directive 2026-07-09 + [`findings/ci-tier-sim-2026-07-09.md`](findings/ci-tier-sim-2026-07-09.md)):
> every gen-2 lane gets a CI tier at birth; the sim adjusted the prior —
> Tier 1 labs run **fast-full** (whole suite, one ≤60s cell), not a smoke
> subset; Tier 0 born-red repos keep the substrate-gate as the card hold.
> 2026-07-10 (morning) — **§2a rider added: wake cadence is agent-executable**
> (owner-verified 2026-07-10 ~morning: Project sessions CAN self-arm
> in-Project routines; correction recorded in `capabilities.md`; recipe
> pending — first successful lane records the exact tool/UI path).
> 2026-07-10 (midday) — **§2a rider mechanism VERIFIED** (owner screen
> recordings 11:01Z/11:04Z; round-3 brief §1): self-arm works via the
> claude-code-remote scheduling tools (create_trigger / send_later family),
> **SEAT-DEPENDENT** (same per-seat inconsistency class as the merge
> classifier); "recipe pending" retired in `capabilities.md`. Ping-test
> websites NO-ACK row corrected (websites acked late, +1h39m, via its
> PR #44 — `findings/ping-test-2026-07-09.md` § Correction; §2a ack count
> updated 2/9 → 3/9).
> 2026-07-10 (evening) — **blueprint amendments P1–P11 APPLIED** (provenance:
> [`findings/fable5-review-2026-07-09.md`](findings/fable5-review-2026-07-09.md)
> §7, F-numbers cited inline; applied by the 18:31Z standing wake under inbox
> ORDER 001, fleet-manager PR #33). Per-amendment landing spots: P1+P4 → §1
> MERGE AUTHORITY landing-path bullet (+§2 delta 1); P3 → §1 refusal-branch
> bullet (+§2 delta 2); P2 → §2a Class-A row + riding rule 3; P5 → §2
> delta 3; P6 → §2 delta 4; P7 → §1 new distribution checklist item; P8 → §1
> Model-line item; P9 → §3 step 4 paste-time lint; P10 → §2 delta 9; P11 →
> §1 claims item + §2 delta 5. **Today-corrections applied where a proposal
> was already superseded by verified reality, and said so:** P6's premise
> ("no scheduler primitive exists") is narrowed — the claude-code-remote
> `create_trigger`/`send_later` family IS the verified scheduler primitive
> (seat-dependent, §2a rider), so the watchdog gate now keys on that boot
> probe; P8's model line is additionally bound by the Q-0262 model-line fleet policy (ORDER 008 policy 1)
> (family-level model names ONLY, exact IDs never — same PR, ORDER 008).
> **Q-0262 fleet policies folded same pass (ORDER 008):** model-line policy
> (§1 Model line), instruction-package deployment hold (§4), OWNER-ACTION
> grammar (playbook R17 rider).
> 2026-07-10 (night) — **CONTINUOUS-MODE OPERATING MODEL (owner directive
> Q-0265, superbot router, 2026-07-10) supersedes one-slice-per-wake for
> production seats** (folded by the manager per the part-4 brief §2b
> MANAGER-ONLY rider). Any "ONE bounded pass / no excessive work — one real
> slice per wake" pacing in this blueprint's templates and in deployed
> founding packages is superseded for open-ended production seats: they are
> **born continuous** — work loop (slice after slice, each still its own
> merged-on-green PR; the throttle is removed, not the ceremony), a
> `send_later` continuation chain ~15 min out as the pacemaker where the
> seat's toolset has it, the standing cron demoted to a dead-man
> "<seat> failsafe wake" (2-hourly stagger kept: lanes `0 */2`, manager
> `30 */2`), **backpressure not time** as the brake, and the Q-0089 honesty
> guard unchanged (genuinely out of work → say so and idle until the
> failsafe). Free-window posture through 2026-07-14 is use-excessively;
> everything produced feeds the owner's post-window consolidation pass.
> §2a's *maintenance-seat* cadence doctrine remains valid for bounded
> maintenance lanes; the gen-3 deployment standard (superbot
> `docs/planning/gen3-deployment-standard-2026-07-10.md` §2, amended same
> night) carries the born-continuous routine standard for new seats. The
> companion rider lives in `prompts/init-prompt-universal.md`.
> 2026-07-10 (night, later) — **REVIEW-QUEUE AUTO-APPEND RULE made BINDING +
> standing drainer named** (inbox ORDERs 003 + 007, program-review §5.2,
> owner directives Q-0258/Q-0259 r3; fleet-manager PR #37). The §1/§2
> "needs-second-eyes → merge anyway + a review-queue line" convention now
> has a **threshold and an owner**: every PR adding **>50 changed lines of
> runtime/product code** (excluding docs/, control/, .sessions/, pure test
> additions) OR carrying any self-flagged risk MUST append its own
> [`review-queue.md`](review-queue.md) row before session close (N=50
> rationale + full rule text live in that file's header — it catches real
> logic changes, skips heartbeat churn; decide-and-flag, owner may re-tune).
> The standing drainer is **two-tier: PRIMARY = @codex post-merge review**
> on Codex-enabled repos (one specific question on the merged head, Part C
> template, Q-0120 return path — playbook **R24**), **FALLBACK = the
> manager's failsafe-wake batches** (which also escalate any row >48h
> unread). First drain pass backfilled 8 rows for the overnight band's
> highest-risk PRs. Rationale: 116 merged PRs / zero rows was the state
> that voided the post-merge-review law this blueprint's merge policy
> rests on.

The premise: every gen-1 lane paid a tax rediscovering the same ~13 failure
classes. Gen-2 lanes are **born right** — the seed state prevents the known
classes before the first order fires.

## 1. SEED STATE checklist (repo + lane at birth, before ORDER 001)

- [ ] **substrate-kit adopted AND engaged at repo birth** — `check --strict`
      green before any domain work (mining/exploration collision; kit PL-011).
- [ ] **CI + required checks aligned before any auto-merge is armed** — the
      required contexts name the actual CI job(s); no legacy contexts; no
      skipped-check satisfying a required check (kit incidents #7/#22; P10).
      The lane's **CI tier is assigned here, at repo birth — per §2b**.
- [ ] **Conventions file committed day 0**, stating explicitly:
      - **READY, never draft** (draft-PR whiplash hit 5+ lanes);
      - **MERGE AUTHORITY — the lane ALWAYS lands its own PRs** *(owner
        directive 2026-07-09; landing-path mechanics amended per P1+P4,
        F2/F5, 2026-07-10)*: direct self-merge calls are classifier-blocked
        (R12); the sanctioned self-merge path is picked **by repo shape AND
        arm timing, per playbook R21**: on a repo where a check can go
        pending and PRs aren't born-red, **arm auto-merge AT PR creation**
        (allowed and server-side), with REST merge-on-green the R8 fallback
        (GraphQL quota, window missed). On a **born-red repo**, the arm is
        refused only **once the gate check has REPORTED failure** — the
        variable is *arm timing + required-check config, not repo class*
        (P1/F2: substrate-kit armed successfully ~dozens of times *inside
        the initial pending window*): arm inside that window if you catch
        it, else **REST merge-on-green after the card flip is PRIMARY** —
        never retry a refused arm. On a **PR-requiring-ruleset repo with no
        CI**, no check ever pends, so arming is structurally impossible
        ("Auto-merge only applies when checks are pending") — REST
        merge-on-green PRIMARY. **Third shape (P4/F5, normal-CI repos):**
        the arm can fail BOTH ways — while pending it returns "unstable
        status" (which is **NOT a failing-checks signal**, just a
        misleading error), on green it returns "already clean", and fast
        checks leave a near-zero window — there, **squash/REST-merge
        directly on green and record which path fired**. Note: **MCP-created
        PRs never trigger an enabler workflow** (app-token events don't fire
        Actions) — arm yourself. Written grant, so no session guesses its
        authority (sonnet5 F1-2; mining's nullified output; opus4.8's
        falsely-owner-routed merges);
      - **classifier-refusal branch — scripted, first denial stops the
        attempt** *(P3, F4+F6, 2026-07-10)*: the auto-mode classifier denied (2026-07-10 evidence)
        self-merges inconsistently per seat (same repo, same day). On the
        **FIRST POLICY denial: never retry or reframe** (a retry is itself
        flagged); leave the PR **READY + CI green**; record the **refusal
        verbatim** in `control/status.md`; ⚑ flag the owner merge click;
        add a [`review-queue.md`](review-queue.md) line. The task's
        done-when **degrades to "PR open, READY, green"** — that terminal
        state is legal and complete. (This fixes R12's now-falsified "the
        wall blocks only the direct merge call" and the founding texts'
        "never hold a PR" absolutism: a classifier-denied (2026-07-10) lane holding a
        READY+green PR is compliant, not stalled.)
      - **no PR ever waits for review before landing** *(owner directive
        2026-07-09; bounded by the refusal branch above)*: if a PR deserves
        second eyes, **merge anyway** and flag it — one line in the
        committed needs-second-review ledger
        ([`review-queue.md`](review-queue.md): number · what to re-check ·
        why) and/or request review by @-mentioning Codex on the PR thread.
        Review is **post-merge**; veto = revert (forward-only). The
        do-not-automerge / owner-gated-merge pattern is **dead in gen-2
        lanes** (gen-1 carve-outs unaffected); done-when for every task is
        therefore agent-reachable: "PR merged on green" — or, on a
        classifier denial, the P3 terminal "PR open, READY, green" (mining
        D5's stalled-output class cannot recur);
      - forward-only git; repo conventions override harness defaults.
- [ ] **control/ files + capability manifest + PLATFORM-LIMITS.md + retro
      questions planted day 0** — walls with exact error text ("probing a
      documented wall twice is a bug"); retro questions at seed so
      self-review is continuous, not archaeology.
- [ ] **claims/ dir seeded** — with any shared surface (kit adoption,
      interface files, `.substrate/`) pre-resolved so no order delegates a
      shared-ground race (games collision; kit ORDER-005 double execution).
      **Amended (P11, F30, 2026-07-10):** prose claims don't stop 90-second
      races — seed a **machine check** too (CI lint: cross-lane path touched
      without a matching claim = warn; duplicate/stale-claim advisory), and
      dispatch obeys **"an order touching shared ground names exactly ONE
      executing lane"** (a claims dir can't catch an order that names two).
- [ ] **Referenced docs travel with the lane (P7, F9, 2026-07-10):** every
      doc a founding text or order references must be **committed (or
      copied) into the lane's own repo**, OR the order **declares its
      read-repos** and the manager checks the session allowlist at dispatch
      — two gen-1 lanes could not read the blueprint they were ordered to
      align with (verbatim "Access denied"). **Mirror the blueprint §1–§2a
      excerpt into each gen-2 seed.**
- [ ] **Environment spec from `environments/SPEC-TEMPLATE.md`** — tested,
      shape-agnostic, defensive setup script (`exit 0` always); the
      setup-script bug killed sessions in 4+ lanes.
- [ ] **Heartbeat-before-work rule** — the session's first act is a
      status/WIP commit; a silent session is indistinguishable from a dead
      one, and the platform WILL sometimes make you silent for an hour
      (sonnet5 F1-1; trading's 2.8h invisible DOA).
- [ ] **Walking skeleton through the FULL merge path in the first 20 minutes**
      — branch → PR → CI → merge proven before real work (trading F1-3;
      superbot-next's flagship lesson: would have deleted its 8-PR fix train).
- [ ] **Model + time line on every session card from card #1** — no
      grandfather backfills; identity not written at the moment of work is
      unrecoverable (proven independently by 3 lanes). Respect the program's
      committed-file naming policy per repo. **Amended (P8, F18 + Q-0262 policy 1,
      2026-07-10):** the model line is **family-level ONLY** (e.g. fable-5,
      opus-4.8; exact model identifiers **never** appear in any committed
      artifact — fleet policy Q-0262 / ORDER 008 policy 1, which also un-nulls trading's model
      rows). Where session policy withholds even the family name, write the
      **literal token "withheld per session policy"** — never guess, never
      omit silently; the owner maintains the lane→model mapping. This makes
      the line satisfiable on policy-restricted seats (two gen-1 lanes had
      to violate either their founding text or harness policy every
      session).

## 2. INSTRUCTION TEMPLATE deltas vs gen-1

What the gen-1 texts (`docs/prompts/`) lacked, per the lanes' own testimony:

1. **No PR-state convention** → harness "create as draft" default won →
   drafts sat hours. Gen-2: READY + the R21 landing path in the founding
   text — arm-at-creation where a check can go pending (on born-red repos:
   only inside the initial pending window, P1); REST merge-on-green primary
   on born-red-after-report/no-CI repos. **Amended (P4, F5, 2026-07-10):**
   if arming fails BOTH ways (pending-reads-as-"unstable status" — NOT a
   failing-checks signal — / "already clean" on green: the known
   normal-CI-repo wall), **squash/REST-merge directly on green — record
   which path fired**. MCP-created PRs never trigger an enabler workflow —
   arm yourself.
2. **No merge-authority statement** → each lane guessed; classifier outcomes
   diverged same-repo-same-day. Gen-2 *(owner directive 2026-07-09)*:
   explicit, unconditional self-merge grant in the founding text — landing
   path per playbook R21 (arm auto-merge at PR creation, the sanctioned R12
   path, where a check can go pending; **REST merge-on-green PRIMARY on
   born-red/no-CI repos**, and the R8 fallback everywhere else), never wait
   for review; needs-second-eyes → merge anyway
   + a [`review-queue.md`](review-queue.md) line and/or @Codex mention;
   review post-merge, veto = revert. **No gen-2 lane is owner-gated on
   merges** — the owner-gate option gen-1 lanes guessed themselves into is
   retired for gen-2 (gen-1 carve-outs unaffected). **Amended (P3, F4+F6,
   2026-07-10):** the grant carries the **scripted refusal branch** (§1):
   first classifier denial → stop, PR READY+green, refusal verbatim in
   status, ⚑ owner click, review-queue line — a denied seat's terminal
   state is now defined, and founding texts may not forbid holding a PR in
   that state.
3. **No write-scope contract** → every lane burned time probing tag/release/
   branch-delete 403s. Gen-2: state the walls up front + the release path.
   **Amended (P5, F7, 2026-07-10): the Actions `workflow_dispatch` release
   route is NOT uniform** — fable5 was denied twice (once with owner
   authorization on record) while opus4.8/kit shipped 9+ releases through
   it; the wall is seat-dependent. Seed every gen-2 repo with the generic
   `release.yml` (workflow_dispatch, contents:write) **AND run a birth-time
   release-capability probe** whose result (granted / owner-manual) is
   written into the lane's conventions file; document the owner-manual tag
   ritual as the fallback; **never present the Actions route as universally
   granted.**
4. **No liveness contract** → dead sessions invisible for hours. Gen-2:
   heartbeat-before-work + spawn-liveness watchdog (first heartbeat within
   5–10 min or treat as dead and respawn). **Amended (P6, F8, 2026-07-10 —
   corrected to verified reality):** the watchdog applies only where a
   scheduling tool is **verified at boot** — and the verified primitive now
   exists: the claude-code-remote `create_trigger`/`send_later` family
   (§2a rider; seat-dependent). A seat whose boot probe finds the family
   absent/refused names the substitute in its founding text (event-driven
   checks + manager ping cadence / routines as the fleet's clock) and
   **forbids improvised sleep-timers** (without colliding with R4's
   sanctioned short foreground waits). §2a's "the routine IS the liveness
   design" stays primary.
5. **No order claim/lease** → double executions (kit #50/#51; manager's own
   ORDER-008 race). Gen-2: order-lease line + "re-read the inbox at HEAD
   immediately before composing/merging an append" (playbook R19).
   **Amended (P11, F30, 2026-07-10):** plus the §1 machine check (CI lint
   for unclaimed cross-lane touches) and the dispatch rule **"an order
   touching shared ground names exactly ONE executing lane."**
6. **No capability inventory** → opus4.8's "biggest blocker was FALSE."
   Gen-2: boot-time capability audit per session type (read
   `docs/capabilities.md` / repo copy before declaring anything impossible).
7. **No time/model/friction instrumentation** → retros were archaeology.
   Gen-2: card template with Model+time lines; telemetry from row one.
8. **"Run for a day" with undefined terminal state** → sonnet5's B4. Gen-2:
   every mission names its done-when AND its between-orders standing default
   (never idle, never undefined).
9. **Heartbeat cost unaddressed** → status overwrites burned a PR round each.
   Gen-2: control fast lane in CI (this repo's substrate-gate pattern) +
   batch heartbeats into substantive PRs. **Amended with numbers (P10, F29,
   2026-07-10):** the fast lane ships **in the SEED CI**, paired with the
   scoped status gate; **max one status PR per session** — batch heartbeats
   into substantive PRs; **heartbeat-before-work is already satisfied by
   the born-red card** (no separate heartbeat commit needed); a
   direct-commit status lane is sanctioned for one-writer control files
   where the ruleset allows it.
10. **Inbox `status: new` semantics unstated** → lanes re-executed or waited.
    Gen-2: "orders stay `new` in the file — diff the inbox against your own
    status" baked into control/README.

## 2a. Wake cadence — measured, not asserted (ping test 2026-07-09)

The ack sweep ([`findings/ping-test-2026-07-09.md`](findings/ping-test-2026-07-09.md)
§ "Ack sweep results") measured the read half of the coordination loop:

- **With a live session, order pickup is minutes:** 9m47s / 14m43s
  dispatch→ack-on-main (superbot-next, substrate-kit — both discovered the
  ping via mid-session inbox re-reads; in-session read→ack cost 2–11 min).
- **Without a live session, it is unbounded:** 7 of 9 lanes had not acked at
  sweep time — hours later. One lane (opus4.8) was *awake after the ping landed
  and still missed it* (heartbeat 15m31s post-ping without an inbox re-read).
  *(Corrected 2026-07-10: websites DID ack late — +1h39m landed→ack via its
  PR #44, once a session went live in the lane — so the final count is 6 of 9
  never-acked, 3/9 acked; the unbounded-without-liveness conclusion stands.
  See `findings/ping-test-2026-07-09.md` § Correction.)*

So: **order-pickup SLA ≈ routine cadence + ~15 min.** The routine *is* the
liveness design; everything else in §2 only works once something wakes the
lane. Concrete cadence per lane class:

| lane class | cadence | 2026-07-09 members | rationale |
|---|---|---|---|
| **A — active mission** (deep order queue / P0 band in flight) | **hourly** | superbot-next, substrate-kit, venture-lab at launch | orders arrive multiple times/day; hourly bounds pickup at ~75 min worst-case for the cost of a cheap no-op wake ("read inbox at HEAD; no new orders → one-line heartbeat via the cheapest sanctioned path" — see riding rule 3/P2: on a PR-required main that is a **fast-lane PR round**, not "no PR") |
| **B — standing-default product** (idle between orders, has a between-orders default) | **every 4 h** | websites, trading-strategy | order volume is a few/day at most; the standing default (groom, next lane) makes each wake productive even with an empty inbox |
| **C — shipped / owner-gated tail** | **daily** | 3 codetool arms, superbot-games lanes post-mission | remaining work waits on owner clicks; a daily wake catches new orders and keeps status honest without burning quota |

Rules that ride the cadence table:

1. **Every routine prompt = the standing ritual** (inbox at HEAD FIRST →
   act → status LAST), never a bespoke prompt per wake.
2. **Reclassify on transition, not on schedule:** a Class-C lane given a new
   mission becomes Class A the same day (owner-queue carries the routine
   click); a Class-A lane whose mission completes drops to C.
3. **A no-op wake must be cheap — defined concretely (P2, F3, 2026-07-10):**
   the old "one-line heartbeat, no PR" was impossible on the PR-required
   main §3 itself mandates (GH013 class; kit's D4 flagged it). The
   sanctioned cheap heartbeat is, in order of preference: **(a)** where the
   owner has carved an **unprotected status/control lane** out of the
   ruleset → a direct commit, genuinely no PR; **(b)** everywhere else →
   a **fast-lane PR round (~7–30s CI)** is the stated, accepted cost of a
   no-op wake — batched into a substantive PR whenever one is in flight
   (delta #9: max one status PR per session). Founding-text WAKE paragraphs
   must not promise "no PR" on shape-(b) repos.
4. **Timestamps from `date -u`**, never the model's sense of time — the sweep
   caught two lanes stamping local-time-as-Z (+1h drift); commit history is
   the clock of record (R2).

> **Rider (2026-07-10, owner-verified; mechanism verified ~11:01Z):** the wake
> cadence above is now **agent-executable** — Project sessions CAN self-arm
> their own in-Project routines (the "walled on both sides" reading was wrong
> for Project surfaces; correction + remaining non-Project walls in
> [`capabilities.md`](capabilities.md)). **Mechanism VERIFIED:** the
> claude-code-remote scheduling tools (`create_trigger` / `send_later`
> family) — **SEAT-DEPENDENT**, the same per-seat inconsistency class as the
> merge classifier: the identical tool family that is absent/refused on some
> seats arms successfully on others. Evidence: two ACTIVE "Created by Claude"
> routines firing (trading-strategy 4-hourly, completed run 10:09; kit-lab
> hourly, completed runs 12:28/12:28/12:30 — owner screen recordings
> 2026-07-10 11:01Z/11:04Z). A lane whose seat is walled records the exact
> tool call + verbatim error in its status; §3 step 6's owner routine click
> is the fallback for those seats, not the path.

## 2b. CI-TIER STANDARD — simulated, not assumed (2026-07-09)

> **Provenance:** owner directive 2026-07-09 (tier prior: 0 = docs no-CI,
> 1 = labs smoke-only, 2 = prod full per-PR) +
> [`findings/ci-tier-sim-2026-07-09.md`](findings/ci-tier-sim-2026-07-09.md)
> (451 PRs / ~1250 runs calibration; 144-cell × 40-seed deterministic sim,
> `tools/sim/ci_tier_sim.py`). Where the sim disagreed with the prior, the
> tier parameters below are adjusted and the disagreement is flagged inline.

Every gen-2 lane is assigned a CI tier at repo birth (part of the §1 born-right
checklist). The tier decides what runs per PR, what runs nightly, and the landing
path. Required-check names must match the real workflow jobs (§1 point 2 stands).

### Tier 0 — docs / coordination repos (fleet-manager class)

- **No full CI required.** Sim: below ~1% per-PR breakage, no-CI wins the damage
  composite outright (13.3 vs 16.2 agent-min/window at p=0.003), and the whole
  regime choice for this class is worth <15 agent-min per 8h window — CI here is
  not a damage decision.
- **Amendment to the prior (flagged):** repos that use the **born-red session-card
  convention keep the single substrate-gate (~11s)** as a required check. Not for
  detection — for **enforcement**: with zero checks nothing ever pends, so the card
  hold does not exist and auto-merge can never arm (R21 shape b). The gate costs
  ~3 wait-min per 8h window in the sim — noise.
- Landing path: REST merge-on-green (R21 primary on this shape).
- Optional: one full run at window end is near-free insurance (+0.5 machine-min)
  that converts ad-hoc promotion surprises into an attributed list; sim shows it is
  otherwise indistinguishable from no-CI.

### Tier 1 — lab repos (codetool-lab class)

- **ADJUSTED FROM THE PRIOR — the sim disagrees with "smoke-only".** The prior
  assumed full CI is expensive; in labs it is not: the full suite runs in 22–45s,
  i.e. at smoke speed. Full-suite-per-PR beats smoke-only on damage from 0.4%
  breakage at 1× traffic and at ALL swept breakage rates at 2×/4× (73.6 → 17.7
  agent-min/window at p=0.03 ×1; 938 → 80 at ×4). Smoke-only's only win is machine-
  minutes (16 vs 80/window) — and most of that bill is accidental.
- **Tier 1 standard: "fast-full" per PR** — run the **entire test suite in ONE slim
  cell** (single OS, single Python, ≤60s wall; reference workflow
  [`environments/templates/smoke.yml`](../environments/templates/smoke.yml)) as the
  required check, **plus a nightly full-matrix run** (all OS/Python cells) **plus
  the promotion gate**. This captures full-CI damage numbers at ≈smoke machine cost.
- **Cost hygiene (sim-quantified):**
  - **Fix the push+PR double-fire** — `on: push` to feature branches + `on:
    pull_request` runs every check twice (fable5 verified: 10 check runs per head;
    opus4.8: 42 runs / 22 PRs). Trigger on `pull_request` + `push: branches: [main]`
    only. This alone halves lab CI spend.
  - **Concurrency-cancel superseded runs** per branch (template included).
  - **No macos in the per-PR path** — the only pathological CI state observed all
    night was a permanently-queued macos-13 runner (stall-not-fail). Keep exotic
    runners in the nightly matrix where a hang costs nothing.
- Landing path: arm-at-creation (R5) — labs are pending-capable and mostly not
  born-red; REST-on-green fallback per R8/R21.

### Tier 2 — production repos (superbot / superbot-next class)

- **Full per-PR CI stands (prior confirmed at the operating points that matter).**
  Sim: full CI wins from ~1% breakage at ≥2× traffic and from ~3.3% at 1×; at 8%
  breakage ×1 it is 145 vs 502 agent-min/window against smoke-only. Merge=deploy
  (Q-0193) puts escaped breakage in production within minutes, which is why prod
  severity outranks the calm-lane composite (flagged honestly: at 1× traffic and
  ≤2% true breakage, smoke-only scores lower — 86 vs 108 at p=0.03; we keep full CI
  for the burst regime and the tail risk, not the average day).
- **Sim-quantified riders:**
  - **Never require up-to-date branches** (and no merge queue at current scale) —
    the up-to-date rule is the single biggest latency amplifier: it produces the
    two-round tier (median merge latency 12.3 min, 37.6 stalls >10 min per window
    at 4× traffic vs 3.9 at 1×). This confirms §3's existing instruction with
    numbers.
  - **The 5–7 min Code Quality wall is the next cost target:** it accounts for
    essentially all of prod's agent-wait (98 → 494 poll-minutes/window from 1× to
    4×). Splitting a <60s required core from the 5-min deep pass would move prod
    toward lab-class latency without losing the gate.
  - Born-red session PRs: the arm is refused once the gate has *reported*
    failure ("unstable status") — on a born-red PR that is nearly the whole
    session; arming works only inside the initial pending window (P1/F2). REST
    merge-on-green after the card flip is the primary landing path (R21);
    never retry a refused arm.
  - True post-flip failure is ≤2% — a red after the flip is signal, not noise;
    fix it, don't re-run it blind. (Raw 20–35% gate "failure rates" are the
    born-red convention and must not be read as flakiness.)

### Tier assignment quick rule

| repo shape | tier | required per-PR check | nightly | landing path |
|---|---|---|---|---|
| docs / coordination | 0 | substrate-gate only if born-red convention, else none | optional single full run | REST merge-on-green |
| lab / experiment | 1 | fast-full: whole suite, 1 cell, ≤60s | full matrix | arm at creation, REST fallback |
| production (merge=deploy) | 2 | full CI (all required contexts) | full + deep scans | arm at creation; REST after born-red flip |

Escalation: a Tier-1 lane graduates to Tier 2 when its merges become deploys or
other lanes build on it same-day. A Tier-0 lane that starts carrying runtime code
is misfiled — re-tier it.

## 3. OWNER SETUP checklist (the clicks only the owner can do, per new lane)

1. **Repo:** create it; General → tick "Allow auto-merge" + "Automatically
   delete head branches."
2. **Ruleset:** main requires PRs + the repo's real CI context(s) (exact
   names!, per the lane's CI tier — §2b); do NOT restrict push; do NOT require
   up-to-date branches (or add a merge queue) — now sim-quantified: the
   up-to-date rule is the single biggest latency amplifier (§2b Tier-2 rider).
3. **Auto-merge sanity:** confirm the required context actually reports on a
   test PR before the lane relies on it.
4. **Project (claude.ai):** create; paste Custom Instructions; set the model.
   **Paste-time lint (P9, F28, 2026-07-10) — 3 lines, checked before any
   paste:** (1) the mission is ONE actionable sentence; (2) it carries a
   **measurable, agent-reachable done-when**; (3) it names the
   **between-orders standing default** (delta 8). Reference implementation:
   games-exploration's closing line. Only 2 of the gen-1 lane proposals
   satisfied delta 8 unlinted — most lanes would have been born violating
   their own law.
5. **Environment:** paste the tested setup script from
   `environments/SPEC-TEMPLATE.md`-derived spec; add only the env vars the
   lane needs (never the ambient production Railway IDs).
6. **Routine:** create the cadence wake routine — **standing note: routines
   are the highest-value click** (an unwoken lane does nothing; every gen-1
   lane that stalled silently would have been caught by its next wake — now
   *measured*: 7/9 lanes never acked the ping for lack of one). Cadence by
   lane class per **§2a** (new lane = Class A, hourly).

## 4. MIGRATION POLICY

- **Gen-1 lanes finish as-is** — no mid-flight restarts; their conventions
  are patched by inbox order where cheap (e.g. READY-not-draft already
  ordered), not by re-seeding.
- **New lanes launch gen-2** from this blueprint (venture-lab is the pilot
  candidate — `prompts/venture-lab-draft.md`).
- A gen-1 lane may be upgraded to gen-2 seed state **only at a natural
  boundary** (mission complete / repo reset), never mid-mission.
- **Instruction-package deployment hold (fleet policy Q-0262 / ORDER 008 policy 3, 2026-07-10):**
  the 8 undeployed instruction packages in
  [`proposals/instructions/`](proposals/instructions/) **STAY undeployed
  until the gen-3 blueprint delta lands**; then re-base every package on the
  gen-3 text (relaunch rule R-a — most were written blueprint-blind) and
  deploy them **in one sitting**. The 2 already-deployed fitted packages
  (websites, trading-strategy) are unaffected.

## 5. OPEN ITEMS — resolution record (2026-07-09 late evening, successor)

1. **venture-lab as the born-right pilot — RESOLVED.** Founding instruction
   text finalized in [`prompts/venture-lab-draft.md`](prompts/venture-lab-draft.md)
   (applies §1 seed state + §2 template deltas; paste-verbatim ready). Owner
   clicks consolidated into one launch item in
   [`owner-queue.md`](owner-queue.md); opening corpus =
   [`findings/venture-shortlist-2026-07-09.md`](findings/venture-shortlist-2026-07-09.md),
   seeded to the lane via ORDER 001.
2. **Codex comparison arm — MOVED TO TRACKING** (handoff in-flight list +
   owner decision), not a blueprint blocker. Proposal + fair-comparison
   requirements stay in
   [`findings/gpt-5-6-report-2026-07-09.md`](findings/gpt-5-6-report-2026-07-09.md).
3. **Ping-ack results — RESOLVED.** Read half collected
   ([`findings/ping-test-2026-07-09.md`](findings/ping-test-2026-07-09.md)
   § "Ack sweep results"); latencies folded into **§2a** above.
4. **External campaign reports — MOVED TO TRACKING** (handoff in-flight
   list): standing intake, not a blueprint blocker — commit pasted reports to
   superbot `docs/eap/external-reviews/`, cross-check against repos (R2)
   before anything drives changes.
5. **Finalize this draft — DONE.** Late retro deliverables reconciled at
   HEAD in the actual repos (R2): superbot-next's project-review retro now
   **EXISTS** (`docs/retro/project-review-2026-07-09.md`, shipped by next#92
   under ORDER 006 — the last missing lane retro is in); superbot-games
   **PR #9 (mining retro) MERGED by the owner 19:02:46Z**; mining port PR #5
   still open+draft awaiting the owner's ready+merge (owner-queue item).
   Status flipped `plan` → `binding` (changelog at top).
