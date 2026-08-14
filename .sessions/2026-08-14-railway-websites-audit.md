# 2026-08-14 · hub — Railway websites audit: what is live, duplicates, the €30 bill

> **Status:** `complete`

*(Flip note, per the review-exemption clause: Codex ran two rounds — round 1
on `25f6d5a` (9 findings, 9 conceded, fixed in `4670a61`), round 2 on the
exact head `4670a61` (3 findings, 3 conceded, fixed in `19471fd`). Under the
two-round cap, `19471fd` carries only the three round-2 concessions and is
dispositioned on the PR rather than re-reviewed; this flip commit changes
this badge, this note, the Verify/PR close-out lines below, the telemetry
delta, and two orientation-budget trims the flip-time gate demanded — this
session's own current-state entry compressed to a pointer, and the fm #842
entry compressed per the in-file precedent (boot-read set was 49 words over
after the parallel-session merge). Nothing else.)*

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

**Verify:** `python3 bootstrap.py check --strict` — pre-flip: real exit 1,
findings exactly the designed born-red hold on this card; post-flip: real
exit recorded green before push. Railway numbers cross-foot against the
receipt in the finding's § 3 (memory 97 % · vCPU 93 % · egress ~91 %
recovered). Codex: 12 findings over two rounds, **12/12 `[conceded]`** and
fixed (`4670a61`, `19471fd`).

**⚑ decide-and-flag:**
- Flagged (owner): `postgres-botsite` disposition after W1 (dump-then-delete
  vs keep-stopped) — it is **one of the two Postgres DBs W1's hard rail
  protects** (Codex P1, conceded); its only consumer is the old botsite, so
  post-W1 it is protected-but-functionally-orphaned. Any disposition is an
  explicit owner amendment to the rail.
- Flagged (owner): whether to disable `dashboard-data-refresh.yml` outright
  or drop it to daily until the old dashboard retires; and whether to give
  `worker` a watch filter covering **every build/runtime input** (source dir
  + root `requirements*`/build config — Codex P1 narrowed the original
  `disbot/**`-only suggestion; finding § 5.3).

**💡 idea:** W3 (make the program visible) could include a monthly
Railway-usage snapshot on the control-plane — the usage API grouped by
service is one query; the bill would be visible *before* it arrives instead
of as a surprise receipt. Routed to `docs/ideas/` grooming when W3 starts.

**⟲ previous-session review:** in the header above.

**Layer-2 handoff:** null (no `docs/repos/` folder exists for `websites` or
`superbot` — both are outside the ratified Tier-1 build-now set; their truth
lives in their own repos' docs, which this audit read directly. The audit
finding + OQ update are the durable pointers.)

**PR:** fm #861 — flipped complete on top of `19471fd`; landing on green
(direct merge after required checks complete, per the landing order).
