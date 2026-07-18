# NEXT-TASKS — the recreated fleet-manager's task set

> **Status:** `living-ledger` — created 2026-07-17 by the EAP wind-down fresh-start
> cleanup. A clean, prioritized task set for the **recreated** manager Project, distilled
> from the overnight planning menu ([`planning/overnight-menu-2026-07-17.md`](planning/overnight-menu-2026-07-17.md),
> 25 proposals) and the fleet-wide recon. Durable open owner asks live in
> [owner-queue.md](owner-queue.md); the immediate paste-ready action list is
> [owner-actions-2026-07-17.md](owner-actions-2026-07-17.md).

## 2026-07-17 — Recreation ruling landed

Recreation ruling landed (owner C, relay event 09027052). This file is the live work source
for the recreated manager. Loop runs on the coordinator↔manager reply bounce (no timers).
**TOP OWNER-BLOCKER:** FM wake chain unarmed — self-scheduling walled in both venues
(owner-queue [`OQ-FM-WAKE-CHAIN-ARM`](owner-queue.md)).

## Context

The Anthropic Projects EAP goes **read-only Tuesday 2026-07-21 17:00 PT**. The owner is
winding down the autonomous apparatus (the `control/` message-bus + roster/telemetry autogen
are retired 2026-07-17, historical only — files kept, workflows not deleted) and **recreating
the Projects fresh**. This file is what the recreated manager should pick up first.

## Immediate — the EAP wind-down / recreation window (do before 2026-07-21)

1. **Execute the fleet-wide owner actions in one sitting.** Drive
   [owner-actions-2026-07-17.md](owner-actions-2026-07-17.md) end-to-end — the admin-override
   merges, the ready-flips (DO-FIRST: gba-homebrew #153 to repair main's substrate-gate and
   unblock ~27 parked arc PRs), and decisions D1–D5. This lands the fleet-wide frozen work.
   *(Largely executed by the owner 2026-07-17 morning close-out; verify residue and any newly
   parked PRs.)*
2. **Run the EAP project-recreation + orphan-trigger sweep** per
   [project-recreation-runbook.md](project-recreation-runbook.md) **before the 2026-07-21
   17:00 PT cutoff**: delete failsafe/self-poll cron triggers attributed to stopped seats (incl.
   the FM failsafe `trig_01An9YmU3KC1kLhB5c9cv4Ax` if the manager seat is recreated), collapse
   the 4 duplicate-cron sibling-seat pairs (keep-OLDEST after live-verifying each), and confirm
   each recreated seat's v3.7 prompt paste + failsafe cutover.
3. **Decide the wind-down scope for fleet-manager's own apparatus.** Which of
   `merge-on-green.yml` / `roster-regen.yml` self-poll / `roster-freshness.yml` / the `control/`
   message-bus / `telemetry/triggers-snapshot.json` the **recreated** manager keeps vs retires.
   The recreated Projects start fresh and smaller, so the ORDER-relay + roster autogen may be
   over-built for a smaller relaunch — **recommend keeping only `merge-on-green.yml`** (the
   server-side landing path that is not classifier-gated) and retiring the self-poll roster/relay
   loop unless a real multi-seat fleet returns.
   **→ Recommendation recorded → [`OQ-FM-APPARATUS-SIZING`](owner-queue.md) (awaiting owner)**
   (2026-07-18): KEEP `merge-on-green.yml` + `substrate-gate.yml` + `roster-freshness.yml` + the
   S3/S5/S9 advisory checkers; HOLD/right-size `roster-regen.yml` (reduce the 2-hourly self-poll
   cadence rather than delete); `control/`+`telemetry/` stay historical. Decide-and-flag — EXECUTION
   is owner/hub-venue (touches `.github/workflows/**`); nothing self-executed.

## Records hygiene (already done in this cleanup — verify on recreation)

4. **Owner-queue stays slim.** [owner-queue.md](owner-queue.md) was curated to a genuinely-open
   active set + a superseded-by-wind-down index (2026-07-17). Keep it that way — do not let the
   resolved log re-interleave with active items.
5. **current-state stays a true snapshot.** [current-state.md](current-state.md) reflects the
   0-open-PR, backlog-cleared, apparatus-retired reality. Re-verify against live GitHub each wake.

## First build set for the recreated manager (from the overnight menu — S3/S5/S9)

The overnight menu's recommended first-build trio — pure drift/staleness checkers, durable and
zero-coupling to the (now retired) autonomous apparatus. Each ships as a stdlib-only
`scripts/`-side checker with a provenance + kill-switch header (kit convention).

6. **S3 — fleet-triage staleness advisory.** A checker that flags fleet-triage register rows whose
   evidence pin has gone stale past a threshold, so keep/replace/archive verdicts can't silently
   rot. Advisory (never merge-blocking).
7. **S5 — docs link-drift sweep.** Resolve every intra-repo markdown link in `docs/` +
   `control/README.md` and report dead targets (the wind-down moved/retired several docs — this
   catches the resulting broken links). Advisory.
8. **S9 — CAPABILITIES wall-age flagger.** Flag `docs/CAPABILITIES.md` entries whose "verified
   wall" finding is older than N days, prompting a re-probe — so a wall that has since been lifted
   (e.g. a classifier change) doesn't stay recorded as permanent. Advisory.

**Drop the heavier L-tier telemetry-warehouse ideas** from the menu — they assume the full
autonomous apparatus, which is retired.

## Backlog

- Groom `docs/ideas/` (~15 idea files) into the recreated roadmap; the overnight menu's remaining
  S/M proposals are the near-term candidates.
- The genuine cross-repo product asks (venture-lab revenue publish, websites Postgres/PAT) and the
  repo-consolidation delete-vs-archive gate are tracked in [owner-queue.md](owner-queue.md) — re-scope
  the consolidation program against the smaller post-wind-down fleet.
- **Idea routing (2026-07-18)** — the verified Ideas-Lab verdict routing (candidates A–H → target
  lanes, first slices, verification) is recorded in
  [idea-routing-2026-07-18.md](idea-routing-2026-07-18.md); the recreated per-lane seats pick up
  their slice when live (owner-only residue tracked as `OQ-IDEA-ROUTING-OWNER-ONLY`).
