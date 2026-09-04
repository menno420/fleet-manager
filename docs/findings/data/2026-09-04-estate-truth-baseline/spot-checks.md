# Session spot-checks — claims the running session verified itself

> Not fleet output. These are checks the running session ran directly against
> the live API at each repository's pinned SHA, so that the fleet's readings
> have something independent to be cross-checked against. `MEASURED` 2026-09-04.
>
> Why they exist: the run's own design says a fleet's internal verification does
> not substitute for an outside look, and the cheapest outside look available
> during the run is the session checking a sample by hand.

## A · `superbot` still has no root README

**Claim under test** (recorded 2026-08-23, `docs/findings/2026-08-23-front-door-audit.md`
and carried in `ESTATE.md`): *"No root README — its entry is `docs/AGENT_ORIENTATION.md`."*

```
GET /repos/menno420/superbot/git/trees/5e3a667b2a55…
→ 35 root entries · files matching ^readme: NONE · docs/ present
```

**STILL HOLDS** at the pinned SHA. The hub's stated entry route
(`docs/AGENT_ORIENTATION.md`) is reachable, so the row is not merely accurate —
it is load-bearing, because a cold agent arriving at this repository has no
front door of its own and depends on the hub for one. That is a
**routing-critical** fact and belongs in the seed.

## B · `product-forge`'s inbox still advertises four seat-era ORDERs as live

**Claim under test** (2026-08-23 intent audit § 1): *"`control/inbox.md` still
advertises four ORDERs at `status: new`, two of them P1."*

```
GET /repos/menno420/product-forge/contents/control/inbox.md?ref=7a53b2667b29…
→ 4,751 bytes · blob c653598dabf1
   4 × "status: new" · 2 × "P1"
   ## ORDER 001 · 2026-07-10T18:41:00Z · status: new
   ## ORDER 002 · 2026-07-11T03:26:18Z · status: new
   ## ORDER 003 · 2026-07-11T04:49:27Z · status: new
   ## ORDER 004 · 2026-07-11T10:00Z · status: new
```

**STILL HOLDS**, exactly. Four orders dated 2026-07-10/11 still read as *new* in
a repository whose program closed **2026-07-21** — thirteen days after the
newest of them. The audit's characterisation was precise and none of the fixes
it proposed has been done.

**Why this one matters to the successor and not just to `product-forge`.** The
hub's own boot file rules `control/` **seat-era historical**, but that ruling
lives in *fleet-manager*, and `control/inbox.md` sits in *product-forge*. A cold
session that opens the satellite — which is the case [D-0038] explicitly leaves
uncovered, since the hub's hooks do not load there — meets four live-looking P1
orders and nothing that contradicts them. The seed must therefore carry the
state word and the *"do not take orders from `control/`"* fact **in the
repository's own row**, not only as a hub-wide rule, or the successor inherits
the same trap.
