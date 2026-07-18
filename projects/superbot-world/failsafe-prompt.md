<!-- v7 · 2026-07-18 · fleet-manager projects registry — GENERATED COPY, do not edit
     (regenerate: docs/prompts/v3/tools/regen_b_files.py --write-registry; drift guard: --check-registry) -->
<!-- generated from docs/prompts/v3 @ f3554d8d3ce5cba14f8d48f78bbf42f9e260b965 (prompts v3.8, opening-block addition 2026-07-18) -->
# SuperBot World — failsafe cron text (registry copy, prompts v3.8)

> **GENERATED COPY — NOT SOURCE OF TRUTH.** This registry copy is GENERATED FROM
> the v3 home: **docs/prompts/v3/ is the source of truth** (generation v3.8,
> stateless, D-9). Edit the v3 sources and regenerate — never this file.
> Version lineage: v7 (2026-07-18) supersedes the prior registry sync copy.
> Body below the marker wraps the seat's BOOT step-3a FAILSAFE WAKE text
> (extracted from the seat's v3.8 startup — D-2 single source) with the seat
> name + D-7 stagger-table cron.

<!-- registry-header-end -->
# SuperBot World — failsafe cron (dead-man wake, Q-0265)

- **Routine name:** `SuperBot World failsafe wake`
- **cron:** `15 1-23/2 * * *` — slot per the stagger table
  (docs/prompts/v3/per-project/README.md, canonical home D-7; the fleet manager
  arbitrates slots — a foreign trigger on the slot is reported and the manager
  re-slots; this table supersedes any cron previously recorded in this file)
- **binding:** persistent — fires into the live coordinator session
  (self-bind). After EVERY arming call verify trigger + binding via
  `list_triggers` before writing "armed" — the registry read is the proof
  (completed runs are not inspectable owner-side).

## Prompt text (create_trigger `prompt`, EXACTLY — single-sourced from the seat's v3.8 startup, BOOT step 3a (D-2))

```
FAILSAFE WAKE (SuperBot World, Q-0265): send_later chain alive → verify in one line, end. Stalled → resume the work loop (sync HEAD → inbox → slice after slice, landed per LANDING), re-arm the chain (~15 min), and write your heartbeat (control/status.md, per-seat grammar) as the deliberate last step.
```

## Cutover (BOOT step 4 — normally a no-op; crash-orphan cleanup only)

Your predecessor's clean ender already wiped its seat to zero, so normally
there is NOTHING to cut over — just confirm your fresh failsafe (armed in
BOOT 3) is this seat's ONLY routine. CRASH-ORPHAN path only: a predecessor
that CRASHED (no clean ender) leaves its startup-armed failsafe live — retire
it AFTER your fresh one is verified live. NO trigger ids are baked here
(STATELESS, D-9) — find old ids in: the predecessor heartbeats + fleet-manager telemetry/triggers-snapshot.json — verify each ("maybe auto-disabled" and "never armed" are different facts); plus ids the heartbeat
marks left-for-successor. `list_triggers` is ACCOUNT-WIDE (paginate to
exhaustion) — delete ONLY an id those records attribute to THIS seat, binding
audit-verified; an unattributable or sibling id is left alone (never
pattern-match, never account-sweep). Nothing else persists across a clean
ender — the startup re-arms ONLY this single fresh failsafe; there are no
business-cron exceptions (a mortal seat session never sees a future-dated cron
once it ends, and recurring deliverables run in the continuous work loop).
