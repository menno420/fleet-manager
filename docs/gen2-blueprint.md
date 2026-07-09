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

The premise: every gen-1 lane paid a tax rediscovering the same ~13 failure
classes. Gen-2 lanes are **born right** — the seed state prevents the known
classes before the first order fires.

## 1. SEED STATE checklist (repo + lane at birth, before ORDER 001)

- [ ] **substrate-kit adopted AND engaged at repo birth** — `check --strict`
      green before any domain work (mining/exploration collision; kit PL-011).
- [ ] **CI + required checks aligned before any auto-merge is armed** — the
      required contexts name the actual CI job(s); no legacy contexts; no
      skipped-check satisfying a required check (kit incidents #7/#22; P10).
- [ ] **Conventions file committed day 0**, stating explicitly:
      - **READY, never draft** (draft-PR whiplash hit 5+ lanes);
      - **MERGE AUTHORITY — the lane ALWAYS lands its own PRs** *(owner
        directive 2026-07-09)*: direct self-merge calls are
        classifier-blocked (R12), but **arming auto-merge AT PR creation**
        — in the checks-pending window — is allowed and server-side; that
        **IS** the self-merge path. REST merge-on-green is the R8 fallback
        when arming fails (GraphQL quota, window missed). Written grant, so
        no session guesses its authority (sonnet5 F1-2; mining's nullified
        output; opus4.8's falsely-owner-routed merges);
      - **no PR ever waits for review before landing** *(owner directive
        2026-07-09)*: if a PR deserves second eyes, **merge anyway** and
        flag it — one line in the committed needs-second-review ledger
        ([`review-queue.md`](review-queue.md): number · what to re-check ·
        why) and/or request review by @-mentioning Codex on the PR thread.
        Review is **post-merge**; veto = revert (forward-only). The
        do-not-automerge / owner-gated-merge pattern is **dead in gen-2
        lanes** (gen-1 carve-outs unaffected); done-when for every task is
        therefore agent-reachable: "PR merged on green" (mining D5's
        stalled-output class cannot recur);
      - forward-only git; repo conventions override harness defaults.
- [ ] **control/ files + capability manifest + PLATFORM-LIMITS.md + retro
      questions planted day 0** — walls with exact error text ("probing a
      documented wall twice is a bug"); retro questions at seed so
      self-review is continuous, not archaeology.
- [ ] **claims/ dir seeded** — with any shared surface (kit adoption,
      interface files, `.substrate/`) pre-resolved so no order delegates a
      shared-ground race (games collision; kit ORDER-005 double execution).
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
      committed-file naming policy per repo.

## 2. INSTRUCTION TEMPLATE deltas vs gen-1

What the gen-1 texts (`docs/prompts/`) lacked, per the lanes' own testimony:

1. **No PR-state convention** → harness "create as draft" default won →
   drafts sat hours. Gen-2: READY + arm-auto-merge-at-creation, in the
   founding text.
2. **No merge-authority statement** → each lane guessed; classifier outcomes
   diverged same-repo-same-day. Gen-2 *(owner directive 2026-07-09)*:
   explicit, unconditional self-merge grant in the founding text — arm
   auto-merge at PR creation (the sanctioned R12 path; REST merge-on-green
   as R8 fallback), never wait for review; needs-second-eyes → merge anyway
   + a [`review-queue.md`](review-queue.md) line and/or @Codex mention;
   review post-merge, veto = revert. **No gen-2 lane is owner-gated on
   merges** — the owner-gate option gen-1 lanes guessed themselves into is
   retired for gen-2 (gen-1 carve-outs unaffected).
3. **No write-scope contract** → every lane burned time probing tag/release/
   branch-delete 403s. Gen-2: state the walls up front + the sanctioned
   release path (Actions workflow_dispatch route, proven by opus4.8).
4. **No liveness contract** → dead sessions invisible for hours. Gen-2:
   heartbeat-before-work + spawn-liveness watchdog (first heartbeat within
   5–10 min or treat as dead and respawn).
5. **No order claim/lease** → double executions (kit #50/#51; manager's own
   ORDER-008 race). Gen-2: order-lease line + "re-read the inbox at HEAD
   immediately before composing/merging an append" (playbook R19).
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
   batch heartbeats into substantive PRs.
10. **Inbox `status: new` semantics unstated** → lanes re-executed or waited.
    Gen-2: "orders stay `new` in the file — diff the inbox against your own
    status" baked into control/README.

## 2a. Wake cadence — measured, not asserted (ping test 2026-07-09)

The ack sweep ([`findings/ping-test-2026-07-09.md`](findings/ping-test-2026-07-09.md)
§ "Ack sweep results") measured the read half of the coordination loop:

- **With a live session, order pickup is minutes:** 9m47s / 14m43s
  dispatch→ack-on-main (superbot-next, substrate-kit — both discovered the
  ping via mid-session inbox re-reads; in-session read→ack cost 2–11 min).
- **Without a live session, it is unbounded:** 7 of 9 lanes never acked —
  hours later. One lane (opus4.8) was *awake after the ping landed and still
  missed it* (heartbeat 15m31s post-ping without an inbox re-read).

So: **order-pickup SLA ≈ routine cadence + ~15 min.** The routine *is* the
liveness design; everything else in §2 only works once something wakes the
lane. Concrete cadence per lane class:

| lane class | cadence | 2026-07-09 members | rationale |
|---|---|---|---|
| **A — active mission** (deep order queue / P0 band in flight) | **hourly** | superbot-next, substrate-kit, venture-lab at launch | orders arrive multiple times/day; hourly bounds pickup at ~75 min worst-case for the cost of a cheap no-op wake ("read inbox at HEAD; no new orders → one-line heartbeat, no PR") |
| **B — standing-default product** (idle between orders, has a between-orders default) | **every 4 h** | websites, trading-strategy | order volume is a few/day at most; the standing default (groom, next lane) makes each wake productive even with an empty inbox |
| **C — shipped / owner-gated tail** | **daily** | 3 codetool arms, superbot-games lanes post-mission | remaining work waits on owner clicks; a daily wake catches new orders and keeps status honest without burning quota |

Rules that ride the cadence table:

1. **Every routine prompt = the standing ritual** (inbox at HEAD FIRST →
   act → status LAST), never a bespoke prompt per wake.
2. **Reclassify on transition, not on schedule:** a Class-C lane given a new
   mission becomes Class A the same day (owner-queue carries the routine
   click); a Class-A lane whose mission completes drops to C.
3. **A no-op wake must be cheap:** no new orders → at most a control-fast-lane
   heartbeat (delta #9); never a full PR round.
4. **Timestamps from `date -u`**, never the model's sense of time — the sweep
   caught two lanes stamping local-time-as-Z (+1h drift); commit history is
   the clock of record (R2).

## 3. OWNER SETUP checklist (the clicks only the owner can do, per new lane)

1. **Repo:** create it; General → tick "Allow auto-merge" + "Automatically
   delete head branches."
2. **Ruleset:** main requires PRs + the repo's real CI context(s) (exact
   names!); do NOT restrict push; do NOT require up-to-date branches (or add a
   merge queue).
3. **Auto-merge sanity:** confirm the required context actually reports on a
   test PR before the lane relies on it.
4. **Project (claude.ai):** create; paste Custom Instructions; set the model.
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
