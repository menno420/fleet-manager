# 2026-08-14 · hub — Railway websites audit: what is live, duplicates, the €30 bill

> **Status:** `in-progress`

- **📊 Model:** fable-5 · high · research — owner-directed audit: enumerate the
  live Railway estate, say what each site does, name the duplicates, explain
  the €30 bill from the receipts + usage API, and recommend the consolidation.
  Read-only toward Railway: no mutation of any service, variable, or trigger.

Time: 2026-08-14 · venue: owner-live hub chat (remote session) · branch
`claude/railway-websites-audit-gp7nc7`

## Previous-session review

⟲ fm #858 (card `.sessions/2026-08-14-v1210-phase3-review.md`) — the phase-3
review session: its §7 row is in the program ledger at `main`, gba #216 is
CLOSED-unmerged with `[D-0017]` captured in `docs/decisions.md`, registry
re-derived. Nothing left open that this session inherits; this session's ask
is a fresh owner directive, not a program step.

## Session idea

The owner received a $30.73 Railway bill (≈€30) and asked which websites are
live, what they do, whether there are duplicates, how to consolidate, and
what causes the bill. Deliverable:
[`docs/findings/2026-08-14-railway-websites-audit.md`](../docs/findings/2026-08-14-railway-websites-audit.md)
— full 4-project/14-service inventory (GraphQL over direct egress), both
Stripe receipts read from Gmail, per-service cost attribution from the usage
API, the deploy-churn defect (the frozen `superbot` repo's 2-hourly
`dashboard-data-refresh` rebuilds + restarts the production bot ~11×/day),
and the consolidation recommendation anchored on the existing cutover plan
(websites `docs/plans/site-consolidation-cutover.md`, W1/OD-8).

## Close-out

*(flips with the badge)*
