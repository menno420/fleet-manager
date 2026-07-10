# 2026-07-10 — ORDER 003 (review-queue enforcement) + ORDER 007 (@codex relay rule) + ORDER 011 close-out

> **Status:** `in-progress`

📊 Model: fable-5 (family-level, per Q-0262 model-line policy) · start 2026-07-10T20:45Z

## Declared at open (born-red)

Q-0265 continuation-chain slice (fired 20:43Z — the chain's first fire, executed by
this worker on the coordinator's behalf). About to land, in this PR:

1. **`docs/review-queue.md`** — ORDER 003: the auto-append rule made BINDING in the
   header (>50 changed lines of runtime/product code OR any self-flagged risk → row,
   appended by the PR's own session before close; N=50 rationale documented,
   decide-and-flag), the standing drainer named two-tier (PRIMARY @codex post-merge
   review per Q-0258/Q-0259 r3 · FALLBACK manager failsafe-wake batches; 48h-unread
   escalation), and the FIRST DRAIN PASS backfilled — 8 rows for the highest-risk
   overnight/day PRs fleet-wide, each with why-risky + citation + drain path.
2. **`docs/gen2-blueprint.md`** — changelog entry making the same rule binding at the
   blueprint level (§1 review bullet amendment).
3. **`docs/playbook.md`** — ORDER 007: new REVIEW RELAY section (R24, the @codex
   relay rule — one specific question on the final head; Part C template pointer;
   Q-0120 return path; owner-queue is owner-only-items ONLY).
4. **`control/inbox.md`** — ORDERs 003 + 007 flipped ✅ DONE (this PR); ORDER 011
   flipped ✅ DONE (re-arm record verified live this session and landed verbatim in
   status.md per its done-when).
5. **`control/status.md`** — heartbeat as the deliberate last content step (chain-slice
   record, orders footer, next slice = ORDER 009).

## Close-out

*(flips on completion)*
