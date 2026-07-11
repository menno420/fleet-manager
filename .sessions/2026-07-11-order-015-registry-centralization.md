# 2026-07-11 — ORDER 015: registry centralization (Seat A + Seat B packages)

> **Status:** `complete`

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

## Close-out (what actually landed)

All seven declared items landed as declared, one commit each (this PR, #58):

1. Seat A package v2 (5 files regenerated in place; setup-script.sh kept +
   marked NEVER-DEPLOYED with truth in meta.md).
2. Seat B package v1 (meta rewrite + 3 new files; no setup-script.sh —
   absence stated explicitly in meta.md; never-deployed parts say so instead
   of inventing content).
3. `projects/README.md` — both matrix rows, stub list (line ~28), and the
   stale "rides first merged-lane boot" paste-wave bullet.
4. `docs/review-queue.md` — superbot-games#16 CLOSED,
   VERIFIED-FIXED-AND-MERGED (second-ever closed row), trading#21 style.
5. `control/inbox.md` — ORDER 015 ✅ DONE append-only block.
6. `control/status.md` — slice record + ⚑ reconciliation flag + phase/
   last-shipped update; carried Seat B's SIM-001 relay as a standing manager
   to-do.
7. This flip.

Verification: fleet-manager has no test suite/kit gate of its own beyond CI
on the PR; all load-bearing claims were verified against the live trigger
registry extraction (01:26:43Z) and ls-remote-matched repo HEADs
(superbot-games `773fab0`, superbot-idle `677b74d`) — citations inline in
each file.

💡 Session idea: the registry's deployed-state tables now encode a checkable
invariant — every `failsafe-prompt.md` marked DEPLOYED+REGISTRY-VERIFIED
should byte-match `list_triggers` output. A tiny manager-side sweep script
(read each package's fenced block, diff against the live registry) would turn
prompt drift into a mechanical finding instead of a manual re-extraction;
worth a chain slice.

⟲ Previous-session review: the F-1 cutover slice (#57) executed the
rebind-then-delete recipe cleanly and re-stamped the registry header in the
same PR — exactly the edit-registry-first doctrine. One improvement it
surfaced: its "ORDER 015 remains the one OPEN order" line was written into a
*historical* record section, which reads as live state to a skimmer; slice
records should date-scope such lines ("open as of 01:1xZ") so later readers
don't need the phase line to disambiguate.

📊 Model: fable-5 · end 2026-07-11T01:4xZ
