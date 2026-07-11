# 2026-07-11 — ORDER 015: registry centralization (Seat A + Seat B packages)

> **Status:** `in-progress`

📊 Model: Claude (Fable family) · start 2026-07-11T01:3xZ (`date -u`) · lane
worker dispatched by coordinator cse_012o8pySy5K3AV6JWoPKryZL

## Declared at open (born-red)

ORDER 015 as RE-SCOPED (docs/succession/coordinator-handoff-2026-07-11.md §5):
**registry centralization, not authoring** — both games seats SELF-BOOTED, so
this session sweeps what they ACTUALLY run into version-stamped
`projects/<repo>/` packages. About to land, in order:

1. `projects/superbot-games/` — regenerate the stale PARKED+CLOCKLESS v1
   package in place → v2 (Seat A LIVE: failsafe `trig_019ZgWyL78Rx1sr6LhvL8NE3`
   `15 */2 * * *`, order-001 MERGED PR #24 / `7d4c347`, floor 230, single-seat
   contract; failsafe-prompt VERBATIM-FROM-REGISTRY).
2. `projects/superbot-idle/` — build the Seat B package fresh (meta stub → real
   v1 meta; instructions / coordinator-prompt / failsafe-prompt; failsafe
   `trig_01TWKGFW8RUsMvxUMt2ndzqA` `45 */2 * * *` VERBATIM-FROM-REGISTRY; no
   setup-script.sh — none exists deployed, stated in meta).
3. `projects/README.md` — fix both matrix rows + the line-28 stub list.
4. `docs/review-queue.md` — close row superbot-games#16 (order-001 VERIFIED
   MERGED: PR #24, merge SHA `7d4c347`, CI runs 29131622448 + 29131622510).
5. `control/inbox.md` — append-only ✅ DONE block on ORDER 015.
6. `control/status.md` heartbeat as the deliberate LAST content commit
   (⚑ reconciliation flag: centralized from self-booted seats, not authored).
7. Flip this card `complete` as the final commit; squash-merge on green.
