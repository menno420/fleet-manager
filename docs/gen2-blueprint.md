# Gen-2 blueprint — Phase-2 (born-right) Project seed standard

> **Status:** `plan`
>
> **DRAFT for the successor session to finalize and execute.** Drafted
> 2026-07-09 at succession, synthesized from the fleet's own retros
> ([`findings/retro-synthesis-2026-07-09.md`](findings/retro-synthesis-2026-07-09.md)
> — especially the 13 cross-patterns and the lanes' F1/F4 prescriptions), the
> quality-review prescriptions, and the launch kit experience. Gen-1 texts
> being revised: [`prompts/README.md`](prompts/README.md).

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
      - **self-merge-on-green where the repo allows it** — written grant, so
        no session guesses its authority (sonnet5 F1-2; mining's nullified
        output; opus4.8's falsely-owner-routed merges);
      - **done-when = agent-reachable states** — "PR open, READY, green" for
        owner-gated merges, never a merge the agent cannot perform (mining D5);
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
   diverged same-repo-same-day. Gen-2: explicit self-merge grant (or explicit
   owner-gate + agent-reachable done-when).
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
   lane that stalled silently would have been caught by its next wake).

## 4. MIGRATION POLICY

- **Gen-1 lanes finish as-is** — no mid-flight restarts; their conventions
  are patched by inbox order where cheap (e.g. READY-not-draft already
  ordered), not by re-seeding.
- **New lanes launch gen-2** from this blueprint (venture-lab is the pilot
  candidate — `prompts/venture-lab-draft.md`).
- A gen-1 lane may be upgraded to gen-2 seed state **only at a natural
  boundary** (mission complete / repo reset), never mid-mission.

## 5. OPEN ITEMS for the successor

1. **venture-lab as the born-right pilot** — finalize its gen-2 instruction
   text from §1–§2 + the draft mission; owner clicks from §3; opening corpus =
   [`findings/venture-shortlist-2026-07-09.md`](findings/venture-shortlist-2026-07-09.md).
2. **Codex comparison arm** — proposed off the GPT-5.6 research
   ([`findings/gpt-5-6-report-2026-07-09.md`](findings/gpt-5-6-report-2026-07-09.md)):
   runs in OpenAI's environment; fair-comparison requirements are in that doc
   (native harnesses, fixed dollar+wall-clock budget, artifact-based judging).
3. **Ping-ack results** — collect the pending ack sweep
   ([`findings/ping-test-2026-07-09.md`](findings/ping-test-2026-07-09.md)) and
   fold read-latency into the wake-cadence design.
4. **External campaign reports** — as the owner pastes ChatGPT/Codex/deep-
   research reports back, commit to superbot `docs/eap/external-reviews/` and
   cross-check every finding against repos (R2) before it drives changes.
5. **Finalize this draft** — reconcile against any late gen-1 retro
   deliverables (superbot-next's missing project-review, mining's PR #9) and
   promote to `binding` convention docs where the fleet adopts it.
