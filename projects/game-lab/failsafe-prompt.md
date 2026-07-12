<!-- v2 · 2026-07-12 · fleet-manager projects registry — GENERATED COPY, do not edit
     (regenerate: docs/prompts/v3/tools/regen_b_files.py --write-registry; drift guard: --check-registry) -->
<!-- generated from docs/prompts/v3 @ 6391b2f1f91b45cba6864693abe700cc5f9aaaca (owner-directed rebuild 2026-07-11/12) -->
# Game Lab — failsafe cron text (registry copy, prompts v3.2)

> **GENERATED COPY — NOT SOURCE OF TRUTH.** This registry copy is GENERATED FROM
> the v3 home: **docs/prompts/v3/ is the source of truth** (generation v3.2,
> stateless, D-9). Edit the v3 sources and regenerate — never this file.
> Version lineage: v2 (2026-07-12) supersedes the pre-rebuild registry copy
> in projects/game-lab/ (last synced by the 2026-07-11 restructure).
> Body below the marker wraps the seat-filled A step-3a FAILSAFE WAKE text
> (D-2 single source) with this seat's name + D-7 stagger-table cron.

<!-- registry-header-end -->
# Game Lab — failsafe cron (dead-man wake, Q-0265)

- **Routine name:** `Game Lab failsafe wake`
- **cron:** `15 */2 * * *` — slot per the v3.2 stagger table
  (docs/prompts/v3/per-project/README.md, canonical home D-7; the fleet manager
  arbitrates slots — a foreign trigger on the slot is reported, never
  re-slotted; this table supersedes any cron previously recorded in this file)
- **binding:** persistent — fires into the live coordinator session
  (self-bind). After EVERY arming call verify trigger + binding via
  `list_triggers` before writing "armed" — never wait for a first fire
  (completed runs are not inspectable owner-side).

## Prompt text (create_trigger `prompt`, EXACTLY — single-sourced from docs/prompts/v3/universal-startup.md step 3a, D-2)

```
FAILSAFE WAKE (Game Lab, Q-0265): send_later chain alive → verify in one line, end. Stalled → resume the work loop (sync HEAD → inbox → slice after slice, landed per LANDING), re-arm the chain (~15 min), and write your heartbeat (control/status.md, per-seat grammar) as the deliberate last step.
```

## Cutover (A step 4 — rebind-then-delete)

Create + verify the NEW failsafe first, then delete the old id and verify it
absent. NO trigger ids are baked here (STATELESS, D-9) — find old ids in:
this lane's heartbeats + fm telemetry/triggers-snapshot.json — this lane's only; plus ids the heartbeat marks left-for-successor. `list_triggers` is
ACCOUNT-WIDE (paginate to exhaustion) — delete ONLY an id those records
attribute to THIS seat, binding audit-verified; unattributable = a sibling's:
record, never delete. A BUSINESS cron (a scheduled deliverable) is rebound,
never dropped.
