> **Historical scaffolding — not live coordination state.**
> The `control/` message-bus (`inbox.md`, `outbox.md`, `status.md`, `claims/`) and the
> roster/telemetry autogen are under a sizing review (`docs/NEXT-TASKS.md` item 3); the
> workflows are kept, not deleted. Live status: `docs/current-state.md`; next steps:
> `docs/NEXT-TASKS.md`. The seat's failsafe + pacemaker wake chain is armed agent-side
> (failsafe `trig_01GK4mjoKBP3yCabn9ux1MB2`, 2-hourly, coordinator-bound; pacemaker alive).

---
updated: 2026-07-18T22:14Z
kit_version: 1.17.0
seat: fleet-manager (coordinator)
wake: coordinator wake (fm wake 2026-07-18). Routine cutover per v3.8 doctrine (fresh
failsafe armed + verified, predecessor crash-orphan failsafe deleted + verified absent),
triggers-snapshot refreshed from the 20:42:05Z full export (I6 PASS), carve-out PRs
pokemon-mod-lab #98 + product-forge #29 re-verified live GREEN, heartbeat recorded
(PR #332). Fleet PR sweep recorded 2026-07-18T21:15Z — 13 open PRs / 7 repos, detail in
`docs/fleet-triage.md` § "2026-07-18 · fleet PR sweep (21:05–21:15Z)" (PR #334).
Night-watch state recorded 2026-07-18T21:32Z (this refresh, records slice).
---

## Night watch (2026-07-18, overnight)

- **Owner asleep as of ~2026-07-18T21:25Z.** Standing directive for the night: watch
  the projects, route where necessary, improve own repo.
- **Pacemaker cadence stretched to ~30 min overnight** (from ~15 min); decide-and-flag
  posture; failsafe cron `30 */2 * * *` unchanged.
- **Routed + landed tonight:** websites ORDER 036 appended to menno420/websites
  `control/inbox.md` (branch `claude/manager-order-bake-422`, PR websites#433, landed by
  the websites landing workflow 2026-07-18T21:19:37Z, merge sha `5689537`) — the
  cross-repo lane-inbox ORDER route verified end-to-end, recorded as a capability in
  `docs/CAPABILITIES.md` (this PR).
- **fm PR #335 (`verify_routine_state.py`) merged** — one-command routine-state proof
  now on main.
- **22:02–22:04Z re-sweep (this refresh):** all 6 remaining born-red PRs from the
  21:05–21:15Z sweep **self-landed on green** — substrate-kit #470 (21:13Z) ·
  superbot #2148 (owner-merged 21:12Z) · trading-strategy #152 (21:18Z) ·
  superbot-next #562 (21:19Z) / #563 (21:20Z) · idea-engine #597 (21:22Z); websites
  #425/#428 had landed earlier. gba-homebrew #177/#178 still draft-parked (07-16
  landing wall, unchanged). Hub-queue rows unchanged: pokemon-mod-lab #98 +
  product-forge #29 still OPEN/green awaiting workflow-carve-out merge.
  **ORDER 036 picked up by the websites lane:** stuck bake PR #422 CLOSED
  (terminal) 21:20:42Z; root-cause fix websites #434 (BAKE_PAT into the review-bake
  landing step) OPEN, `do-not-automerge` + workflow diff — owner-gated on the
  ASK-0008 BAKE_PAT Actions secret; the 2026-07-18 data refresh itself is not yet
  re-landed. New open PRs since 21:15Z: idea-engine #600 · pokemon-mod-lab #104 ·
  superbot-next #567 (normal lane work, expected to self-land) + websites #434
  (owner-gated, above). Local checks: roster fresh (gen #96 21:28Z, I5 PASS);
  trigger health PASS 8/9 (I8 superbot-world duplicate-cron WARN unchanged, stays
  routed to that seat); `verify_routine_state.py` → known capture-lag DRIFT (2
  mismatches on the fm failsafe cutover ids — expected until the next snapshot
  refresh). Stale-claims cleanup: this PR (claims of merged #332/#337 retired).

# Fleet Manager — status

Neutral heartbeat. Facts + pointers only. This file is not live coordination state (see banner). Live status: `docs/current-state.md`; next: `docs/NEXT-TASKS.md`; sweep detail: `docs/fleet-triage.md`.

## This session (2026-07-18) — coordinator wake: cutover + snapshot refresh

### Routine state (verified live via list_triggers this session)

<!-- routine-claims fence — the heartbeat's machine-readable routine-claims contract
     (idea: PR #335 session card 💡; consumer: scripts/verify_routine_state.py, which
     PREFERS this fence over prose-grammar scraping — the prose bullets below stay for
     humans). Shape: a ```json fence tagged `routine-claims` holding one JSON object:
       seat       string — the claiming seat
       updated    string — UTC instant these claims were (re)verified
       failsafe   object {id, cron, next_run_at, state: "armed"} — or a list of them
       deleted    [ids] — trigger ids claimed deleted / verified absent
       pacemaker  object {mode, cadence_minutes, note} — informational
     Neutral facts only, written at heartbeat time from live-verified state. To the
     verifier a present-but-malformed fence is a loud exit-2 contract violation, never
     a silent prose fallback. (The `control/README.md` grammar doc is retired/
     historical, so this contract note rides the file itself.) -->

```json routine-claims
{
  "seat": "fleet-manager (coordinator)",
  "updated": "2026-07-18T22:14Z",
  "failsafe": {
    "id": "trig_01GK4mjoKBP3yCabn9ux1MB2",
    "cron": "30 */2 * * *",
    "next_run_at": "2026-07-18T22:33:20Z",
    "state": "armed"
  },
  "deleted": ["trig_01Bo7dZxM9xz2hwR36L424Z8"],
  "pacemaker": {
    "mode": "send_later",
    "cadence_minutes": 30,
    "note": "overnight cadence ~30 min; exactly one pending one-shot at a time"
  }
}
```

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

### Next-2-tasks baton (refreshed 2026-07-18T21:32Z)
1. Hub lands **pokemon-mod-lab #98** and **product-forge #29** — green, ready PRs touching
   `.github/workflows/**` (`merge-on-green.yml` skips workflow diffs → owner click or
   agent MCP/REST merge).
2. **~22:33Z failsafe wake (`trig_01GK4mjoKBP3yCabn9ux1MB2`; or the ~22:31Z pacemaker
   tick, whichever fires first):** watch websites #434 (owner-gated BAKE_PAT wiring —
   once merged, confirm the 2026-07-18 data refresh actually re-lands, or a fresh bake
   PR supersedes #422); watch the three new lane PRs land (idea-engine #600 ·
   pokemon-mod-lab #104 · superbot-next #567); refresh `telemetry/triggers-snapshot.json`
   at a convenient wake to clear the known capture-lag DRIFT; I8 superbot-world
   duplicate-cron dedup stays routed to that seat's own wake
   (`OQ-FM-ROSTER-CRON-RELIABILITY` roster watch: gen #96 arrived on time).

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
