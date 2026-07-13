<!-- v7 · 2026-07-13 · fleet-manager projects registry — GENERATED COPY, do not edit
     (regenerate: docs/prompts/v3/tools/regen_b_files.py --write-registry; drift guard: --check-registry) -->
<!-- generated from docs/prompts/v3 @ 6715ade82b16d19ae9a96b6d6837e9a0e4684bc1 (prompts v3.6, stage-2 fold 2026-07-13) -->
# Venture Lab — failsafe cron text (registry copy, prompts v3.6)

> **GENERATED COPY — NOT SOURCE OF TRUTH.** This registry copy is GENERATED FROM
> the v3 home: **docs/prompts/v3/ is the source of truth** (generation v3.6,
> stateless, D-9). Edit the v3 sources and regenerate — never this file.
> Version lineage: v7 (2026-07-13) supersedes the prior registry sync copy.
> Body below the marker wraps the seat's BOOT step-3a FAILSAFE WAKE text
> (extracted from the seat's v3.6 startup — D-2 single source) with the seat
> name + D-7 stagger-table cron.

<!-- registry-header-end -->
# Venture Lab — failsafe cron (dead-man wake, Q-0265)

- **Routine name:** `Venture Lab failsafe wake`
- **cron:** `45 1-23/2 * * *` — slot per the stagger table
  (docs/prompts/v3/per-project/README.md, canonical home D-7; the fleet manager
  arbitrates slots — a foreign trigger on the slot is reported, never
  re-slotted; this table supersedes any cron previously recorded in this file)
- **binding:** persistent — fires into the live coordinator session
  (self-bind). After EVERY arming call verify trigger + binding via
  `list_triggers` before writing "armed" — never wait for a first fire
  (completed runs are not inspectable owner-side).

## Prompt text (create_trigger `prompt`, EXACTLY — single-sourced from the seat's v3.6 startup, BOOT step 3a (D-2))

```
FAILSAFE WAKE (Venture Lab, Q-0265): send_later chain alive → verify in one line, end. Stalled → resume the work loop (sync HEAD → inbox → slice after slice, landed per LANDING), re-arm the chain (~15 min), and write your heartbeat (control/status.md, per-seat grammar) as the deliberate last step.
```

## Cutover (BOOT step 4 — rebind-then-delete)

Create + verify the NEW failsafe first, then delete the old id and verify it
absent. NO trigger ids are baked here (STATELESS, D-9) — find old ids in:
the money-seat heartbeats (trading status carries the trigger-id records); the weekly grading cron is a BUSINESS cron — rebound per step 4, never just deleted; plus ids the heartbeat marks left-for-successor. `list_triggers` is
ACCOUNT-WIDE (paginate to exhaustion) — delete ONLY an id those records
attribute to THIS seat, binding audit-verified; unattributable = a sibling's:
record, never delete. A BUSINESS cron (a scheduled deliverable) is rebound,
never dropped — EXCEPT a FRESH-SESSION-PER-FIRE business cron: KEPT as-is,
never rebound and never deleted (it binds to no mortal seat session).
