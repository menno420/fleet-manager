# 2026-07-10 — Coordinator boot: ORDER 007 (@codex relay rule), routine-arming record, status heartbeat

> **Status:** `in-progress`

📊 Model: coordinator-boot execution worker (seat-based; model line intentionally generic — no model identifiers in this PR per boot instructions) · start 2026-07-10T13:41Z (`date -u`)

## Declared at open (born-red)

The session-based coordinator seat (round-3 pack §1 brief) booted 2026-07-10. This PR
lands the boot's durable record. About to land:

1. **Standing wake routine armed** — `fleet-manager 2-hourly standing wake`,
   cron `30 */2 * * *`, bound to the coordinator session; verbatim tool call +
   result recorded in `control/status.md` (the fleet is building a reproducible
   arming recipe; the record is first-class).
2. **`control/inbox.md` — APPEND ORDER 007** (@codex review-relay playbook rule,
   owner directive Q-0258) — round-3 brief §1 standing debt 6, the only one of the
   seven brief debts without an inbox ORDER (001–006 cover debts 1–5 and 7).
3. **`control/status.md` — OVERWRITE** (deliberate last content step): coordinator
   seat LIVE, routine state with the verbatim arming record, and the stale
   `orders:` footer fixed to reality (001–004 open, 004 P0 deadline 2026-07-14;
   005–006 done; 007 new).
4. **This card**, flipped `complete` as the deliberate last commit.

Landing: born-red card holds the gate red; flips as the last commit;
REST merge-on-green (R21 — auto-merge arming is walled in this repo; no arm attempt).
