# 2026-07-11 — coordinator archive close-out (chat archive prep)

> **Status:** `in-progress`

📊 Model: Claude Fable 5 (claude-fable-5) · archive close-out slice · night (~01:0xZ)

## Declared at open (born-red)

Owner directive (2026-07-11 ~00:5xZ): the coordinator chat is about to be
ARCHIVED — prepare the repo so a successor session boots cold from committed
state alone. ONE PR:

1. `docs/succession/coordinator-handoff-2026-07-11.md` — the successor's
   one-read state doc: LIVE seats + trigger ids (incl. this session's failsafe
   `trig_014odnv5h1tkJAFRhix3tGLq`, bound to the soon-archived chat), the
   PENDING-OWNER list, the ORDER 015 reconcile note, THE PERMISSIONS FOLD
   REBUILD RECIPE (the built fold dies with this container — recipe is the
   only survivor), known-walls pointers.
2. `projects/fleet-manager/reboot-prompt.md` (v1) — paste-ready successor
   boot prompt: read order → TRIGGER CUTOVER FIRST (F-1 rebind-then-delete)
   → continuous loop → pending-owner pointer.
3. This card with full enders.
4. Heartbeat LAST: phase → CLOSING for archive; routine line explicit that
   the failsafe stays bound to the archived session until successor cutover.

Landing: born-red card → content → heartbeat + flip `complete` last →
substrate-gate poll → REST squash on green (R21).
