<!-- v9 · 2026-07-18 · fleet-manager projects registry — GENERATED COPY, do not edit
     (regenerate: docs/prompts/v3/tools/regen_b_files.py --write-registry; drift guard: --check-registry) -->
<!-- generated from docs/prompts/v3 @ caf871f12878c94162ad21cfa37a7dea3e8702e3 (prompts v3.8, opening-block addition 2026-07-18) -->
# Fleet Manager — failsafe cron text (registry copy, prompts v3.8)

> **GENERATED COPY — NOT SOURCE OF TRUTH.** This registry copy is GENERATED FROM
> the v3 home: **docs/prompts/v3/ is the source of truth** (generation v3.8,
> stateless, D-9). Edit the v3 sources and regenerate — never this file.
> Version lineage: v9 (2026-07-18) supersedes the prior registry sync copy.
> Body below the marker wraps the seat's BOOT step-3a FAILSAFE WAKE text
> (extracted from the seat's v3.8 startup — D-2 single source) with the seat
> name + D-7 stagger-table cron.

<!-- registry-header-end -->
# Fleet Manager — failsafe cron (dead-man wake, Q-0265)

- **Routine name:** `Fleet Manager failsafe wake`
- **cron:** `30 */2 * * *` — slot per the stagger table
  (docs/prompts/v3/per-project/README.md, canonical home D-7; the fleet manager
  arbitrates slots — a foreign trigger on the slot is reported and the manager
  re-slots; this table supersedes any cron previously recorded in this file)
- **binding:** persistent — fires into the live coordinator session
  (self-bind). After EVERY arming call verify trigger + binding via
  `list_triggers` before writing "armed" — the registry read is the proof
  (completed runs are not inspectable owner-side).

## Prompt text (create_trigger `prompt`, EXACTLY — single-sourced from the seat's v3.8 startup, BOOT step 3a (D-2))

```
FAILSAFE WAKE (Fleet Manager, Q-0265): send_later chain alive → verify in one line, end. Stalled → resume the work loop (sync HEAD → inbox → slice after slice, landed per LANDING), re-arm the chain (~15 min), and write your heartbeat (control/status.md, per-seat grammar) as the deliberate last step.
```

## Cutover (BOOT step 4 — normally a no-op; crash-orphan cleanup only)

Your predecessor's clean ender already wiped its seat to zero, so normally
there is NOTHING to cut over — just confirm your fresh failsafe (armed in
BOOT 3) is this seat's ONLY routine. CRASH-ORPHAN path only: a predecessor
that CRASHED (no clean ender) leaves its startup-armed failsafe live — retire
it AFTER your fresh one is verified live. NO trigger ids are baked here
(STATELESS, D-9) — find old ids in: the predecessor heartbeat (control/status.md routine block) + telemetry/triggers-snapshot.json; plus ids the heartbeat
marks left-for-successor. `list_triggers` is ACCOUNT-WIDE (paginate to
exhaustion) — delete ONLY an id those records attribute to THIS seat, binding
audit-verified; an unattributable or sibling id is left alone (never
pattern-match, never account-sweep). A BUSINESS cron (a scheduled deliverable)
is rebound, kept alive across cutover — and a FRESH-SESSION-PER-FIRE business
cron is KEPT AS-IS (it binds to no mortal seat session).
