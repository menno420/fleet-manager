> **Provenance note (2026-07-17 recreation ruling, retained):** the 2026-07-17 EAP
> wind-down banner is historical — the owner ruled (coordinator relay, event 09027052)
> "This one is the recreation": this Project IS the recreated fleet-management seat and
> the FM autonomous loop stands back up. This file is the seat's neutral heartbeat.
> Live status: `docs/current-state.md`; next steps: `docs/NEXT-TASKS.md`.

---
updated: 2026-07-18T21:01Z
kit_version: 1.17.0
seat: fleet-manager (coordinator)
wake: coordinator wake (fm wake 2026-07-18). Routine cutover per v3.8 doctrine (fresh
failsafe armed + verified, predecessor crash-orphan failsafe deleted + verified absent),
triggers-snapshot refreshed from the 20:42:05Z full export (I6 PASS), carve-out PRs
pokemon-mod-lab #98 + product-forge #29 re-verified live GREEN, heartbeat recorded.
PR #332.
---

# Fleet Manager — status

Neutral heartbeat. Facts + pointers only. Live status: `docs/current-state.md`; next:
`docs/NEXT-TASKS.md`; sweep detail: `docs/fleet-triage.md`.

## This session (2026-07-18) — coordinator wake: cutover + snapshot refresh

### Routine state (verified live via list_triggers this session)
- **Fresh seat failsafe ARMED + VERIFIED:** `trig_01GK4mjoKBP3yCabn9ux1MB2`
  ("Fleet Manager failsafe wake", cron `30 */2 * * *`, bound to the live coordinator
  session, created 2026-07-18T20:58:28Z, next fire 2026-07-18T22:33:20Z).
- **Predecessor crash-orphan failsafe `trig_01Bo7dZxM9xz2hwR36L424Z8` DELETED** and
  verified absent via list_triggers — the BOOT 4 crash-orphan path of the v3.8 ender
  doctrine (fm PR #330). Attribution came from the predecessor heartbeat's routine block.
- **Pacemaker chain alive:** ~15-min `send_later` one-shots, exactly one pending at any
  time (fired 20:41Z + 20:58Z; pending fires 21:14Z). Per the v3.8 ender this seat closes
  to ZERO routines at its clean end; the successor STARTUP re-arms the single fresh failsafe.

### Doctrine / registry
- **Session-ender v3.8 full-wipe + BOOT-4 crash-orphan reframe is LIVE on main @ `173d1d6`**
  — fm PR #330, labelled `do-not-automerge` by its author, **owner-merged**
  2026-07-18T20:27Z. Clean ender = zero routines of any kind for the seat, no cron
  carve-out; STARTUP re-arms only the failsafe.

### Triggers snapshot (I6) + health
- **`telemetry/triggers-snapshot.json` refreshed** from the full 2026-07-18T20:42:05Z
  export (1903 records, 13 enabled, all pages, cursor-to-exhaustion). I6 SNAPSHOT-FRESH
  → **PASS** (0.3h at check time); overall `check_trigger_health.py` verdict PASS (8/9).
- **Capture-instant honesty:** the capture predates the cutover, so the snapshot's data
  still contains the old failsafe record and not the new one; the two post-capture deltas
  are recorded in the snapshot's `capture_notes` (do-not-fabricate rule). I4 therefore
  keys green on the old id until the next refresh — live truth is the routine block above.
- **I8 WARN (sibling lane, not this seat):** 2× enabled "superbot world failsafe wake"
  crons (`trig_01XJJ88pQaQFRSpVAviCfAZe` 2026-07-17T22:11Z · `trig_01DbcKVWxn6RJPhfyRkgTg6m`
  2026-07-18T17:08Z). Remedy per checker: verify each live, keep oldest, delete the rest —
  routed to a future wake / the SuperBot World seat; this session made no trigger calls
  against sibling lanes.

### PRs
- **#332** (this session, `claude/fm-wake-2026-07-18`) — born-red card; lands-on-green at
  the card flip (merge-on-green squash).
- **pokemon-mod-lab #98** — re-verified live 2026-07-18T20:35Z: OPEN, `mergeable_state:
  clean`, all 3 checks green on head `1ea62cd`. Awaiting hub merge (workflow carve-out).
  Queue row `OQ-POKEMON-98-WORKFLOW-MERGE` accurate.
- **product-forge #29** — re-verified live 2026-07-18T20:35Z: OPEN, `mergeable_state:
  clean`, all 3 checks green on head `cd1fcd9`. Awaiting hub merge (workflow carve-out).
  Queue row `OQ-FORGE-29-WORKFLOW-MERGE` accurate.
- **fm #330** — terminal (owner-merged 20:27Z); no owner-queue row needed.

### Roster
- Fresh: gen #95, 2026-07-18T19:45Z (I5 PASS, 1.3h at check time; bar 4h).

### Owner asks (carried forward, paste-ready)
1. **Console re-paste — three Class-A seats (fleet-manager, websites, curious-research).**
   The console-deployed prompt predates the current registry; paste each seat's current
   **v3.8** registry prompt into its console to bring the deployed copy current (the
   prior v3.7 ask now refers to v3.8 after PR #330).
2. **Optional fleet-manager branch protection.** Enable "do not allow administrators to
   bypass required checks" so a red `substrate-gate` can't be admin-merged. Owner's call.
3. **Self-heal-stamp design gap.** No machine-readable self-heal-stamp mechanism, so
   registry meta.md rows can only reach `unverified`, never `in-sync`. Flagged for a
   future rule.
4. **Owner-queue carry-forward.** Read `docs/owner-queue.md` and carry forward, paste-ready,
   any remaining genuine owner-only items (secrets, settings, money, product intent).

### Next-2-tasks baton
1. Hub lands **pokemon-mod-lab #98** and **product-forge #29** — green, ready PRs touching
   `.github/workflows/**` (`merge-on-green.yml` skips workflow diffs → owner click or
   agent MCP/REST merge).
2. Next wake: **fleet PR sweep** + roster-freshness / trigger-health watch
   (`OQ-FM-ROSTER-CRON-RELIABILITY`); pick up the I8 superbot-world duplicate-cron WARN.

### Gates
- `python3 scripts/check_trigger_health.py` → PASS (8/9 green, 1 WARN I8, exit 0).
- `python3 bootstrap.py check --strict` → EXIT 0 after the card flip (born-red HOLD by
  design pre-flip).
- PR #332.

## Pointers
- Live status → `docs/current-state.md`
- Next steps → `docs/NEXT-TASKS.md`
- Triage evidence → `docs/fleet-triage.md`
- Owner-only work → `docs/owner-queue.md`
- Prior heartbeats → git history of this file (wholesale-overwrite grammar).
