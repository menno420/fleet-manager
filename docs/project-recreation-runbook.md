# Project Recreation Runbook — EAP Wind-Down Cutover

> **Status:** `audit`
> **Owner:** menno420 · **Scope:** whole fleet (all Projects) · **Author:** fleet-manager seat
> **Created:** 2026-07-16 · **Trigger:** Anthropic EAP wind-down (owner email 2026-07-16)

Neutral operational runbook for stopping and recreating fleet Projects inside the EAP wind-down window. Seat state lives in each repo (stateless, D-9), so recreation loses nothing that has been pushed. This is a records/oversight artifact — the manager seat writes it; the owner and each seat's coordinator execute it.

## 1. Why this exists — the EAP wind-down facts

Per the owner's Anthropic EAP notice dated 2026-07-16:
- The Early Access Program **ends Tuesday 2026-07-21 at 17:00 PT**.
- At that cutoff: **Projects are disabled**, existing **sessions become read-only**, and project data is **deleted after 180 days**.
- The announced **coordinator communication improvements apply only to NEW Projects** — an existing Project cannot receive them by any in-place action.

The owner's plan, within the ~5-day window (2026-07-16 → 2026-07-21):
- **Stop some or all current Projects and recreate them fresh** to pick up the new-Project improvements.
- **Keep 1–2 existing Projects unchanged as controls** for an A/B comparison (see §4).

Because seats are **stateless** — all durable state (orders, roster, heartbeats, cards, claims) lives in the repo, not the Project — recreation is a control-plane operation, not a data migration. Nothing pushed to a repo is at risk from stopping a Project.

## 2. Per-project CLOSEOUT checklist (before stopping a Project)

Run this for each Project the owner decides to stop. Goal: no orphaned triggers, no lost in-flight work, a clean heartbeat at HEAD.

For each seat, in order:
1. **Ask the seat's coordinator to run its session ender** (send it a wake). The routine disposition:
   - closes/expires the pacemaker (`send_later`) so it can't fire into a dead Project,
   - records the seat's **failsafe trigger id** into its heartbeat/card,
   - lands any open PR to a terminal state (merged/closed) so nothing is stranded read-only.
2. **If no ender can be run** (coordinator unreachable / already read-only), **record the seat's live trigger ids from `telemetry/triggers-snapshot.json`** (captured 2026-07-16T15:26:43Z) so a post-stop sweeper session (§5) can find and delete them. Copy the seat's failsafe id + cron from the table below.
3. Confirm the repo heartbeat (`control/status.md` for the manager; each seat's equivalent) is **current at HEAD** — that heartbeat is what the recreated Project reads to resume.

### Failsafe triggers by seat (from the 2026-07-16T15:26:43Z snapshot)

| Seat / Project | Failsafe trigger name | id | cron | Notes |
|---|---|---|---|---|
| Fleet Manager | Fleet Manager failsafe wake | `trig_01An9YmU3KC1kLhB5c9cv4Ax` | `30 */2 * * *` | this seat |
| Game Lab | Game Lab failsafe wake | `trig_0123fLkN1pzY6uNN3Y7ksYaW` | `50 */2 * * *` | |
| Ideas Lab | Ideas Lab failsafe wake | `trig_01KPMLtWuAc2FaYNzuSSukgH` | `30 1-23/2 * * *` | |
| Self Improvement | Self Improvement failsafe wake | `trig_01Mw9yn9r21Bi5q19v7QcqjN` | `0 */2 * * *` | |
| SuperBot 2.0 | SuperBot 2.0 failsafe wake | `trig_01E86nBnXqesQTwm6WA4mSUD` | `0 1-23/2 * * *` | **+ dup** `trig_01UC7wiV3n5Vgs3RpSQt4gWz` (I8) |
| SuperBot World | SuperBot World failsafe wake | `trig_01B32hfwxfA67orKfBzQVdmU` | `15 1-23/2 * * *` | **+ dup** `trig_01RwQK2cBpgvY2xc2LZPSNtQ` (I8) |
| Venture Lab | Venture Lab failsafe wake | `trig_01Er6TUtwybs9D9EuHCH32qX` | `45 1-23/2 * * *` | **+ dup** `trig_01GeQiMM3nHMQTyuLMsWj7q3` (I8) |
| Websites | Websites failsafe wake | `trig_01Cn7F2UvE62uDykSYQCDhtF` | `45 */2 * * *` | **+ dup** `trig_01VRT9F6jYNXym3nn18vVQQK` (I8) |

Also live (do **not** delete on a seat stop unless that seat is being retired):
- **Venture Lab weekly grading** `trig_01BsYsMABu2vfH4d2MzuSLs6` (`0 9 * * 5`) — business cron; each fire spawns a fresh session, so it survives a Project swap. Keep unless Venture Lab is fully retired.
- **Pacemakers** (`send_later …`, one-shot `run_once_at`) — self-expire; list them for completeness but they need no manual deletion after they fire.
- `suberbot docs reconciliation` `trig_018wP6XTPmf9DLnxrG4RpGVh` — legacy `http_api` trigger, no bound session; verify separately before touching.

**The 4 duplicate failsafe pairs above are the standing I8 DUPLICATE-CRON ×4 warning** — each fires two sessions per slot. The stop/recreate is the right moment to collapse each pair to one (see §5).

## 3. RECREATION steps (per seat)

For each stopped Project, recreate it fresh:
1. **Create a new Project** in the console (owner-only — console/settings live in the owner-queue).
2. **Attach the same repo(s)** the old Project had (seat repo + whole-fleet read as configured).
3. **Paste the seat's v3.7 registry prompt** — assembled from `docs/prompts/v3/` (shared registry) + `projects/<seat>/` (per-seat overlay) in the fleet-manager repo. This is the same prompt lineage the current seats run (ORDER 048 registry adoption).
4. **Coordinator boots** and runs standard orientation (CONSTITUTION → status → inbox → HARD-SYNC at HEAD).
5. **Cut over the failsafe** — the new coordinator: **create the new failsafe trigger → verify it via `list_triggers` (paginate fully) → only then delete the old seat's id** (from the §2 table). Never delete the old id before the new one is confirmed live; an unattributable trigger belongs to a sibling — leave it.
6. **Read the repo heartbeat and resume.** All state (orders, roster, claims, cards) is in the repo — **stateless (D-9), nothing is lost**. The seat picks up exactly where the last pushed commit left it.

## 4. A/B test notes (new Projects vs. retained controls)

With 1–2 Projects kept unchanged as controls, compare against the recreated ones on:
- **Coordinator message signal/noise** — volume and usefulness of coordinator-injected routing context per wake (fewer spurious/duplicated injections = improvement).
- **Classifier denial rate on identical dispatch shapes** — send the same worker-relay / cross-repo write shapes to a new vs. a control seat and compare wall-denials (the improvements should reduce false denials).
- **Model self-report on session cards** — whether the `📊 Model:` line on new-Project cards matches the intended model family (verifies model routing carried over on recreation).

Record observations in a new dated `docs/experiments/` file so the comparison is a durable artifact, not chat-only.

## 5. ORPHAN SWEEP procedure (after Projects are stopped)

Once the owner has stopped Projects, a sweeper session (any live seat with trigger tools) reconciles:
1. **`list_triggers`, paginating fully** (the last export was 21 pages / 2033 records — do not stop at page 1).
2. **Match live triggers against the pre-stop id list** in §2 (snapshot + each repo's heartbeat = attribution source).
3. **Delete only ids attributed to stopped seats** — the failsafe id (and its I8 dup) for each Project the owner stopped. Attribution rule: a trigger is a stopped seat's **only** when both the snapshot **and** that repo's heartbeat name it. **Unattributable = a sibling's — leave it.**
4. **Keep business crons that spawn a fresh session per fire** — e.g. Venture Lab weekly grading (`0 9 * * 5`) — unless that seat is fully retired.
5. **Collapse the I8 duplicate pairs** (SuperBot 2.0 / SuperBot World / Venture Lab / Websites) to one failsafe each while sweeping — recreation already replaces the primary, so both stale ids in each pair are deletable once the new failsafe is verified.
6. Record the sweep (ids deleted, ids kept + why) in `control/status.md` trigger-health and a `.sessions/` card.

**Safety:** deleting a trigger is reversible only by recreating it (name + cron are in §2), so sweep conservatively — when attribution is uncertain, leave it and flag in the owner-queue.

---
*Records custodian: fleet-manager. This runbook is oversight documentation — execution (Project stop/create, trigger cutover) is done by the owner and each seat's coordinator, not by this seat.*
