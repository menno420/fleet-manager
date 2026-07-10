# Proposal — generated fleet roster from lane heartbeats

> **Status:** `plan` — filed 2026-07-10T16:4xZ by the 16:31Z standing-wake pass
> (ORDER 002 part 2). Routed as **fleet-manager inbox ORDER 009** (decide-and-flag:
> implement v1 at a future manager wake; owner may veto). Provenance: superbot
> `docs/eap/eap-program-review-2026-07-10.md` §6.2 (generated roster) + §5.4
> (registry-disagreement finding); overnight-review finding 1 (the manifest froze at
> its 07-09 pre-launch state within hours of seeding — twice now).

## Problem

`superbot docs/eap/fleet-manifest.md` is a hand-maintained registry with a
hand-stamped `Last-seen` per lane. Evidence that this design cannot stay true:

- The gen-1 grand review (superbot #1911 §5) found **every cell stale within hours
  of seeding**; superbot #1915 reconciled it by hand.
- It froze again immediately: ORDER 002 (2026-07-10) found the whole table at the
  07-09 pre-launch state after a 116-PR overnight launch — venture-lab's row said
  "Project boot pending owner clicks" while the lane had two sellable products on
  main. Re-stamped by hand a second time (superbot PR #1954).
- `scripts/check_manifest_freshness.py` (superbot #1923) already *detects* the
  staleness by fetching each lane's `control/status.md` over git transport — i.e.
  the machine-readable source of truth exists and is reachable; only the
  *regeneration* is manual.

A registry whose freshness depends on a human-cadence hand edit in a fleet that
moves at 2-hour wake cadence will always be stale. Fix it structurally: **stop
hand-writing the roster; generate it from the same heartbeats the checker reads.**

## Design (v1)

**Data sources** (all already exist, no lane-side change required):

1. Each lane repo's `control/status.md` (or `control/status-*.md` for per-lane
   split repos like superbot-games) — the `updated:` header, `phase:`, `kit:`,
   `routine:`, `orders:` and `blockers:` lines. Read over git transport
   (shallow `git fetch --depth 1` + `git cat-file`), exactly as
   `check_manifest_freshness.py` does today — proven in agent containers where
   the REST API is proxy-blocked.
2. The account trigger registry (`list_triggers` via claude-code-remote MCP) for
   live routine state (`cron`, `enabled`, `last_fired_at`, `next_run_at`) —
   the one signal status.md self-reports can lie about (verified today: a status
   claimed NOT-ARMED while the trigger live-fired).
3. HEAD committer date as the activity fallback for repos without `control/`
   (superbot hub today).

**Generator + trigger:** a small script in fleet-manager (`tools/gen_roster.py`,
same transport pattern as the superbot checker) run by **every manager standing
wake** (2-hourly). The wake already syncs, sweeps and heartbeats; regeneration is
one extra deterministic step. Output is committed only when it changed.

**Where it lives:** `fleet-manager docs/roster.md` (generated; carries a loud
`GENERATED — do not hand-edit; regenerated each manager wake` header + the
generation timestamp + per-row evidence [repo @ SHA, status `updated:`, trigger
id/last-fire]). fleet-manager is the natural owner — the manager is already the
manifest's sole writer, and the roster is oversight data (Q-0260: manager =
read-everywhere).

**Migration (manifest becomes a pointer):**

1. Wake N: land `tools/gen_roster.py` + first generated `docs/roster.md`
   (parallel-run; hand manifest untouched).
2. Wake N+1: compare generated roster vs the hand manifest; fix generator gaps.
3. Then: superbot `docs/eap/fleet-manifest.md` is reduced to a **pointer stub**
   ("registry moved: generated at fleet-manager `docs/roster.md`, regenerated
   each manager wake") + the historical seeding note. `check_manifest_freshness.py`
   retires with it (its detection job is subsumed by regeneration) — delete per
   its own Q-0105 kill-switch header, and the freshness idea graduates into a
   `--verify` mode of the generator if wanted.

**What stays human:** the Notes-column *judgment* (frozen flags, owner items,
recommendations) is coordinator prose, not derivable from heartbeats. v1 keeps a
small hand-written `notes:` sidecar per lane (or keeps such prose in
`control/status.md`'s Lanes section, where it already lives) — the roster table
itself is 100% generated facts.

## Costs / risks

- ~1 shallow fetch × 13 repos per wake (~30 s, already paid by anyone running the
  freshness checker); zero lane-side work.
- `list_triggers` is seat-dependent (MCP availability) — the generator must
  degrade gracefully to status.md self-report + a `trigger: unverified` marker.
- Two registries during migration (manifest + roster) — bounded to two wakes by
  the plan above.

## Routing

Not owner-only (no clicks, no settings, no external surface — pure agent tooling
+ docs). Per decide-and-flag: routed as **ORDER 009** in `control/inbox.md`
(implement v1 at a future manager wake; **owner may veto** by striking the ORDER).
`docs/owner-queue.md` deliberately NOT touched.
