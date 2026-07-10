# 2026-07-10 — Routine-wall correction + wake-arm rollout record

> **Status:** `in-progress`

📊 Model: Fable 5 (claude-fable-5) · fleet worker (coordinator-dispatched) · start 2026-07-10T11:05Z (`date -u`)

## Declared at open (born-red)

Docs-only correction PR. Owner-verified finding (2026-07-10, morning): Claude
Code **Projects CAN create their own routines that fire inside the Project** —
the 2026-07-10 "routine/trigger creation walled on BOTH sides" conclusion was
WRONG for Project sessions. It remains TRUE for the webagent coordinator +
spawned workers (no send_later/self-trigger) and for cross-session trigger
binding. Exact in-Project mechanism unknown — recorded honestly as
owner-verified capability, recipe pending. About to land:

1. `docs/capabilities.md` — narrow the routine wall (KEEP the verbatim error
   texts) + a CAN entry with the "recipe pending: first successful lane
   records the exact tool/UI path" line.
2. `docs/gen2-blueprint.md` §2a — one-line rider: wake cadence is now
   agent-executable via in-Project self-armed routines (owner-verified
   2026-07-10); changelog provenance line.
3. `docs/owner-queue.md` — item 7 replaced: self-arm rollout dispatched
   (ORDERs queued to all active lanes); owner fallback only if a lane's
   attempt fails with a recorded error.
4. `docs/dispatch-log.md` + `control/status.md` (the live handoff surface —
   `docs/handoff-2026-07-09.md` is CLOSED OUT/historical) — correction +
   wake-arm ORDER rollout lines (6 lanes: venture-lab, substrate-kit,
   pokemon-mod-lab, gba-homebrew hourly; websites, trading-strategy
   4-hourly, per blueprint §2a classes).

Landing: born-red card holds substrate-gate red; flips `complete` as the
deliberate last commit; REST merge-on-green (R21 — born-red shape, no arm
attempt).
