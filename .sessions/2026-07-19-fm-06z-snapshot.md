# 2026-07-19 · fm 06:15Z triggers snapshot + SBW duplicate-failsafe escalation (records slice)

> **Status:** `complete`

About to happen (declared born-red): records slice for the coordinator seat.
Commit the fresh 2026-07-19T06:15:10Z full `list_triggers` export (2024 records,
17 enabled) as `telemetry/triggers-snapshot.json` via the R26 assembler; run and
quote the trigger-health + routine-state gates; fire the 00:06Z watch item's
**escalation tripwire** in `docs/fleet-triage.md` (SBW duplicate failsafe pair
still duplicated at the second capture) and raise the owner-queue item
`OQ-SBW-DUP-FAILSAFE`; refresh the `control/status.md` heartbeat + baton.
No trigger-MCP calls from this venue.

- **📊 Model:** fable-5 · high · docs-only — records slice (snapshot assemble + escalation + heartbeat; telemetry JSON included)

## What shipped (PR #347)

- `telemetry/triggers-snapshot.json` — refreshed from the 2026-07-19T06:15:10Z
  full export (2024 records, 17 enabled, 21 pages, cursor-to-exhaustion; +62 new
  / -0 gone vs the 00:06:22Z capture; read-only export, no trigger touched).
- `docs/fleet-triage.md` — "2026-07-19 · SBW duplicate-failsafe ESCALATION"
  entry: the 00:06Z watch item's tripwire **FIRED** — both SBW failsafe crons
  still enabled at the second capture (both fired ~05:15Z, both next 07:15Z);
  both captures cited; seat-aware delete recommendation recorded (inverts the
  checker's seat-blind keep-oldest heuristic, with the honest note why).
- `docs/owner-queue.md` — new Active item **`OQ-SBW-DUP-FAILSAFE`** (six-field,
  VENUE: hub): delete one of the pair from hub-chat trigger tools; recommendation
  = delete the older `trig_01XJJ88pQaQFRSpVAviCfAZe` (the 07-18 one is the
  current SBW seat's cutover-armed failsafe); paste-ready steps; ✅ reversible.
  Honest note: fm doctrine forbids this seat deleting a sibling's id — hence
  the hub routing.
- `control/status.md` — `updated:` → 06:23Z; routine-claims fence refreshed from
  the export (failsafe last_fired 04:32:17Z, next 06:31:48Z — written pre-fire
  at 06:23Z, fire noted as imminent); "06:15Z snapshot refresh + SBW escalation"
  facts subsection; baton → (1) hub queue: forge #29 + fm #344 +
  `OQ-SBW-DUP-FAILSAFE`; (2) watch websites 036 (`OQ-WEBSITES-036-STALL`
  stands) + odd-hour roster-cron proof post-#344.
- `.substrate/guard-fires.jsonl` — telemetry delta committed (do-not-revert).

## Ground-truth runs (verbatim verdict lines, 06:21Z)

```
[I6 SNAPSHOT-FRESH    ] PASS — snapshot capture instant 2026-07-19T06:15Z, 0.1h before now=2026-07-19T06:21Z (bar 4h)
[I8 DUPLICATE-CRON    ] WARN — 2× enabled 'superbot world failsafe wake' `15 1-23/2 * * *`, oldest→newest: `trig_01XJJ88pQaQFRSpVAviCfAZe` (created 2026-07-17T22:11Z) · `trig_01DbcKVWxn6RJPhfyRkgTg6m` (created 2026-07-18T17:08Z) …
VERDICT: PASS — 8/9 green, 1 WARN (see the WARN line(s) above for the verify-live remedy; exit stays 0).   (check_trigger_health.py)
VERDICT: OK — heartbeat routine claims match the export (2 claim(s) verified).   (verify_routine_state.py, fence-sourced)
```

## Enders

- 💡 **Session idea (dedup-checked — `docs/ideas/` 16 files + recent cards; the
  00Z card's tripwire-checker and the 03Z card's regen-window detector are
  adjacent but distinct):** **seat-provenance-aware I8 remedy in
  `check_trigger_health.py`.** The checker's generic remedy ("keep the
  OLDEST-created, delete the rest") gave the *wrong* seat-aware answer this
  session: the newer 07-18 SBW cron is the one armed by the currently-running
  seat's cutover, so the older one is the orphan. Idea: when I8 fires, read each
  duplicate's `job_config` session binding (and/or compare `created_at` against
  the lane's latest heartbeat/cutover stamp when readable) and emit a
  *provenance-ranked* recommendation naming the specific id to delete —
  falling back to "verify live, human decides" when bindings are unreadable —
  so the remedy line can never again contradict the correct escalation.
- ⟲ **Previous-session review (PR #346, the ~06Z morning sweep):** exemplary
  live-verification discipline (every PR state MCP-read before writing, the
  05:45Z failsafe window re-checked pre-flip) and the 036 escalation disposition
  was honest about what is and isn't hub-executable. One miss worth naming: it
  carried the SBW disposition forward with the checker's "keep the oldest"
  wording unexamined — this session had to invert that recommendation on
  provenance grounds. Workflow improvement it surfaces: checker remedy lines are
  *heuristics*, and records slices should re-derive them from provenance before
  quoting them as dispositions (the 💡 above mechanizes exactly this).
- **Doc-audit:** everything from this slice has a durable home — export in
  `telemetry/`, escalation evidence in `docs/fleet-triage.md`, the owner ask in
  `docs/owner-queue.md`, the baton in `control/status.md`; nothing chat-only.
  Owner-queue item cites only snapshot-verified state (Q-0120); both gate
  verdicts quoted verbatim above.
- **Guard-fires:** `.substrate/guard-fires.jsonl` delta committed with the
  payload; strict-check findings were the designed born-red HOLD + 4
  allowlist-suppressed + the known preflight NOTE — no new guard class.
- **Claim:** `control/claims/claude-fm-06z-snapshot.md` deleted in this flip
  commit (claims README step 4).
