# 2026-07-10 — Routine-wall correction + wake-arm rollout record

> **Status:** `complete`

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

## Done (close-out) · end 2026-07-10T11:12Z (`date -u`)

All four declared deliverables landed in one batch commit (dc75554) on
PR #19:

- `docs/capabilities.md` — routine wall narrowed to non-Project surfaces
  (verbatim error texts KEPT: the create_trigger/trigger-binding rejection
  class and **"binding a trigger to another session is not enabled for this
  organization"**) + new CAN entry "Self-arm wake routines from inside a
  Project session" with the recipe-pending line.
- `docs/gen2-blueprint.md` — §2a rider (wake cadence agent-executable;
  §3 step 6's owner routine click becomes the fallback) + changelog
  provenance line (2026-07-10 morning, owner-verified).
- `docs/owner-queue.md` — item 7 replaced: self-arm rollout dispatched
  (ORDERs queued to all active lanes); owner fallback only if a lane's
  attempt fails with a recorded error.
- `docs/dispatch-log.md` new section + `control/status.md` (timestamp,
  last-shipped #19, in-flight PLATFORM-GAP bullet corrected) — the
  wake-arm ORDER rollout recorded: venture-lab, substrate-kit,
  pokemon-mod-lab, gba-homebrew hourly (Class A); websites,
  trading-strategy 4-hourly (Class B).

Gate: `python3 bootstrap.py check --strict --require-session-log
--session-log <this card>` — the only reds before this flip were the
expected born-red markers (this section clears them).

## 💡 Session idea

**Self-arm verification ledger** — a one-file table in fleet-manager
(`docs/findings/self-arm-ledger-2026-07.md` or similar) where every lane's
self-arm attempt lands as one row: lane · timestamp · exact tool/UI path
used (or the verbatim failure error). Six lanes are about to attempt the
same unknown mechanism in parallel; without a single convergence point the
recipe gets recorded six ways in six status files (or not at all), and the
owner-fallback decision per lane requires a six-repo sweep. One ledger row
per attempt makes the first success everyone's recipe and the failures a
clean fallback list.

## ⟲ Previous-session review

The morning consolidation (#18) was strong on verification discipline
(116-PR recount against live GitHub, contradictions ledgered) — but this
session exists because one of its "verified walls" over-generalized: the
routine wall was tested on two surfaces (worker-side MCP, one owner-console
paste session) and recorded as "walled on BOTH sides ... NO way to arm a
wake routine at all," which the owner falsified for Project sessions the
same morning. Concrete workflow improvement: platform-capability walls in
capabilities.md should name the **surface tested** (Project session /
coordinator / worker / owner console) as a required field, and the
discovery rule should treat an untested surface as unknown, not walled —
"attempt it once" per surface before the wall claims the platform.
