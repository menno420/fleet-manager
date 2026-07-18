# NEXT-TASKS — the fleet-manager's task set

> **Status:** `living-ledger`. A clean, prioritized task set for the manager Project,
> distilled from the overnight planning menu ([`planning/overnight-menu-2026-07-17.md`](planning/overnight-menu-2026-07-17.md),
> 25 proposals) and the fleet-wide recon. Durable open owner asks live in
> [owner-queue.md](owner-queue.md); the immediate paste-ready action list is
> [owner-actions-2026-07-17.md](owner-actions-2026-07-17.md).

This file is the live work source for the manager seat. The loop runs on the
coordinator↔manager reply bounce (no timers); the wake chain is armed agent-side
(failsafe `trig_01Bo7dZxM9xz2hwR36L424Z8` + pacemaker).

## Immediate

1. **Execute the fleet-wide owner actions in one sitting.** Drive
   [owner-actions-2026-07-17.md](owner-actions-2026-07-17.md) end-to-end — the admin-override
   merges, the ready-flips (DO-FIRST: gba-homebrew #153 to repair main's substrate-gate and
   unblock ~27 parked arc PRs), and decisions D1–D5. This lands the fleet-wide frozen work.
   *(Largely executed by the owner 2026-07-17 morning close-out; verify residue and any newly
   parked PRs.)*
2. **Trigger-registry hygiene sweep** per
   [project-recreation-runbook.md](project-recreation-runbook.md): delete failsafe/self-poll
   cron triggers attributed to stopped seats, collapse duplicate-cron sibling-seat pairs
   (keep-OLDEST after live-verifying each), and confirm each active seat's prompt paste +
   failsafe are current.
3. **Decide the sizing scope for fleet-manager's own apparatus.** Which of
   `merge-on-green.yml` / `roster-regen.yml` self-poll / `roster-freshness.yml` / the `control/`
   message-bus / `telemetry/triggers-snapshot.json` the manager keeps vs retires.
   The fleet is smaller now, so the ORDER-relay + roster autogen may be over-built —
   **recommend keeping only `merge-on-green.yml`** (the
   server-side landing path that is not classifier-gated) and retiring the self-poll roster/relay
   loop unless a real multi-seat fleet returns.
   **→ Recommendation recorded → [`OQ-FM-APPARATUS-SIZING`](owner-queue.md) (awaiting owner)**
   (2026-07-18): KEEP `merge-on-green.yml` + `substrate-gate.yml` + `roster-freshness.yml` + the
   S3/S5/S9 advisory checkers; HOLD/right-size `roster-regen.yml` (reduce the 2-hourly self-poll
   cadence rather than delete); `control/`+`telemetry/` stay historical. Decide-and-flag — EXECUTION
   is owner/hub-venue (touches `.github/workflows/**`); nothing self-executed.

## Records hygiene

4. **Owner-queue stays slim.** [owner-queue.md](owner-queue.md) is curated to a genuinely-open
   active set + a closed index. Keep it that way — do not let the resolved log re-interleave with
   active items.
5. **current-state stays a true snapshot.** [current-state.md](current-state.md) reflects live
   reality (open PRs, backlog, apparatus status). Re-verify against live GitHub each wake.

## First build set (from the overnight menu — S3/S5/S9)

The overnight menu's recommended first-build trio — pure drift/staleness checkers, durable and
zero-coupling to the autonomous apparatus. Each ships as a stdlib-only `scripts/`-side checker
with a provenance + kill-switch header (kit convention).

6. **S3 — fleet-triage staleness advisory.** A checker that flags fleet-triage register rows whose
   evidence pin has gone stale past a threshold, so keep/replace/archive verdicts can't silently
   rot. Advisory (never merge-blocking).
7. **S5 — docs link-drift sweep.** Resolve every intra-repo markdown link in `docs/` +
   `control/README.md` and report dead targets (catches broken links when docs move). Advisory.
8. **S9 — CAPABILITIES wall-age flagger.** Flag `docs/CAPABILITIES.md` entries whose "verified
   wall" finding is older than N days, prompting a re-probe — so a wall that has since been lifted
   (e.g. a classifier change) doesn't stay recorded as permanent. Advisory.

**Drop the heavier L-tier telemetry-warehouse ideas** from the menu — they assume the full
autonomous apparatus.

## Backlog

- Groom `docs/ideas/` (~15 idea files) into the roadmap; the overnight menu's remaining
  S/M proposals are the near-term candidates.
- The genuine cross-repo product asks (venture-lab revenue publish, websites Postgres/PAT) and the
  repo-consolidation delete-vs-archive gate are tracked in [owner-queue.md](owner-queue.md) — re-scope
  the consolidation program against the smaller fleet.
- **Idea routing (2026-07-18)** — the verified Ideas-Lab verdict routing (candidates A–H → target
  lanes, first slices, verification) is recorded in
  [idea-routing-2026-07-18.md](idea-routing-2026-07-18.md); the per-lane seats pick up
  their slice when live (owner-only residue tracked as `OQ-IDEA-ROUTING-OWNER-ONLY`).
