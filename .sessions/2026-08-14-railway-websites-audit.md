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

## 💡 Session idea

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

**Shipped:**
- `docs/findings/2026-08-14-railway-websites-audit.md` — the audit: full
  inventory (4 projects / 14 services, all live, none sleeping), both Stripe
  receipts ($7.75 → $30.73), per-service cost attribution for the billed
  cycle, the deploy-churn measurement (worker 344 real deploys/cycle,
  `watchPatterns: []`), the `postgres-botsite` orphan-to-be wiring proof, and
  the consolidation recommendation anchored on websites'
  `docs/plans/site-consolidation-cutover.md`.
- `docs/owner-queue.md` — `OQ-RAILWAY-PROJECT-SPLIT` updated: reachability
  constraint lapsed, canonical home decided (websites #407), decision packet
  linked.
- Program §7 row + `docs/current-state.md` Recently-shipped entry (fm #861).

**Not done, deliberately:** no Railway mutation of any kind (no stop, no
variable write, no trigger change). W1 execution is owner-gated and its own
session.

**Verify:** `python3 bootstrap.py check --strict` → 1 finding = the designed
born-red hold on this card (added-card lane); exit read without a pipe at
close. Railway numbers cross-foot against the receipt totals in the finding's
§ 3.

**⚑ decide-and-flag:**
- Flagged (owner): `postgres-botsite` disposition after W1 (dump-then-delete
  vs keep-stopped) — the cutover plan's "never touch the two Postgres DBs"
  protected the bot's infra; this third DB serves only a retire target.
- Flagged (owner): whether to disable `dashboard-data-refresh.yml` outright
  or drop it to daily until the old dashboard retires; and whether to give
  `worker` a `disbot/**` watch filter (both recommended in the finding § 5).

**💡 idea:** W3 (make the program visible) could include a monthly
Railway-usage snapshot on the control-plane — the usage API grouped by
service is one query; the bill would be visible *before* it arrives instead
of as a surprise receipt. Routed to `docs/ideas/` grooming when W3 starts.

**⟲ previous-session review:** in the header above.

**Layer-2 handoff:** null (no `docs/repos/` folder exists for `websites` or
`superbot` — both are outside the ratified Tier-1 build-now set; their truth
lives in their own repos' docs, which this audit read directly. The audit
finding + OQ update are the durable pointers.)

**PR:** fm #861 — <terminal state recorded at flip>.
