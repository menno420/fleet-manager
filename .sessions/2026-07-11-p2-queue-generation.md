# 2026-07-11 — P2 QUEUE GENERATION: owner-queue candidate feed + merged-PR checker + OQ slugs

> **Status:** `in-progress`

📊 Model: Claude (Fable family, fable-5) · start 2026-07-11T~20:30Z · lane
worker dispatched by coordinator cse_012o8pySy5K3AV6JWoPKryZL

## Declared at open (born-red)

Scope: **phase P2 (QUEUE GENERATION) of the fleet centralization plan**
(superbot `docs/planning/fleet-centralization-plan-2026-07-11.md` §3b/§5,
owner-directed, Option A custodian-primary in force). Kills the
"already-satisfied ask" + "stale pending-merge" drift class (items 1–3 and 13
of the queue would all have fired today). Deliverables this PR:

1. **Candidate feed** — extend `scripts/gen_roster.py` status parsing to
   extract each lane heartbeat's `⚑ needs-owner` / `OWNER-ACTION` blocks into
   a GENERATED `docs/owner-queue-candidates.md` (marked NOT SOURCE OF TRUTH;
   the manager curates `docs/owner-queue.md` from it). Wired into the same
   regen path (manual invocation + `.github/workflows/roster-regen.yml`) so
   it refreshes headlessly.
2. **`scripts/check_owner_queue.py`** — at each wake/regen, for every
   owner-queue item citing a PR with a MERGE action or
   "RESOLVED-PENDING-MERGE of PR #N", query live PR state and FLAG
   already-merged/closed citations. Q-0105 provenance header; known-bad +
   known-good fixtures shipped AND run (verbatim output in this card);
   report-only (never merge-blocking) in the regen workflow.
3. **Stable slug IDs** — every `docs/owner-queue.md` item gets
   `id: OQ-<slug>` (content-derived, never positional — today's renumbering
   by fm PR #75 broke a cross-reference); queue migrated IN PLACE (ordering/
   groups untouched); checker + candidate feed key on slugs.
4. Heartbeat as the deliberate last content commit; card flip last.

Landing path: born-red card+claim first → PR open immediately → build →
heartbeat → card flip `complete` → substrate-gate green on final head → ONE
REST squash-merge attempt (park verbatim on denial; auto-merge arming is a
known wall in this repo — not attempted).

## Shipped (close-out)

*(to be written at close)*
