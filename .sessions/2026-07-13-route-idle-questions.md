# 2026-07-13 — Route idle owner questions (Q-0264 fan-in)

> **Status:** `complete`
> 📊 Model: fable-5 (worker, dispatched by the fleet-manager coordinator)

Routing slice per the morning tally (#158) next-3 item 3: the two owner
questions superbot-idle posted in its night `control/outbox.md`
(2026-07-13 entries, both marked "needs fleet Q-number — manager to
assign") are now E-group structured-choice items in
`docs/owner-queue.md`:

- **E#52 · OQ-IDLE-GENERATOR-PURCHASE** — generator-purchase economy
  (P1, blocks the idle seat's core growth loop). Recommendation **A**:
  add `purchase_generator` on a geometric cost curve, SIM-pinned
  PROVISIONAL numbers (T10 + fresh economy sim) before merge.
- **E#53 · OQ-IDLE-CONTENT-DEPTH** — content-depth/endgame direction
  (P2). Recommendation **A**: timed-events scoping next (the seat's
  `docs/design/timed-events-scoping.md` already exists; values stay
  unregistered pending SIM-002/Q-0264).

Both carry the six R17 fields + RISK, one-letter answers, and
provenance (superbot-idle outbox @ HEAD, night run 2026-07-13; routed
per Q-0264). `control/status.md` restamped (06:52Z); next-3 item 3 now
records the routing. Relay of the assigned numbers to the seat's inbox
rides the coordinator's next dispatch (this slice makes no trigger or
cross-seat calls).

## Read-only morning checks (no action taken)

- **ORDER 042 (websites):** PICKED UP AND SATISFIED — websites
  heartbeat (updated 06:43:25Z) records "fm ORDER 042 ACK: SATISFIED —
  both venture batch-1 pages verified live against 042's scope
  2026-07-13T06:29Z: /puddle-museum (PR #247) + /products/catalog
  (PR #248)", citing fm inbox@65db381 per 042's done-when. The seat has
  also already triaged venture batch 2 (8 markers: 1 dup, 1
  owner-gated, 6 buildable).
- **ORDER 043 (Ideas Lab):** NOT YET PICKED UP — idea-engine heartbeat
  last updated 05:14:54Z (morning tally; acked=001-004 only, "SIM-REQUESTs
  SERVED: 0"), i.e. it predates awareness of 043. Its failsafe cron
  (`30 1-23/2 * * *`) next fires ~07:30Z; expected pickup then. No
  intervention taken.
- **Roster gen #24:** NOT LANDED — latest roster-regen run is #19
  (schedule, success, 04:10:37Z = gen #23, PR #156); the ~06:40Z slot
  had not fired as of ~06:55Z and no commit hit main after 06:00Z.
  Consistent with the known GitHub best-effort cron-skip family
  (watchdog 3 saw 00:40 + 02:40 skipped the same night). Next slot
  ~08:40Z; roster staleness stays inside I5's tolerance if that one
  fires.
- **fm open PRs:** 1 — this PR (#159) only.

## Verification

- `python3 scripts/check_owner_queue.py` → CLEAN (slugs intact +
  unique, no merged/closed citations; exit 0).
- `python3 bootstrap.py check --strict` → red only on the designed
  born-red hold of this card while in-progress; green at the
  complete-flip commit.

## 💡 Session idea

**Outbox owner-question routing tripwire.** The idle seat's two OWNER
QUESTION entries sat in its append-only outbox with "Routing result:
(pending)" and only got routed because a human-readable next-3 line
remembered them. Nothing machine-checks the fan-in: `check_owner_queue.py`
audits the queue side only, and if a tally sweep misses an outbox entry
the question rots silently (the outbox is seat-owned and append-only, so
the seat can't even see it was routed). Cheap enforcing guard: a wake-time
checker (or a clause in the roster-regen advisory run) that greps each
lane's `control/outbox.md` for `OWNER QUESTION` blocks whose text lacks a
matching `OQ-` slug anywhere in fm `docs/owner-queue.md` and flags any
older than ~6h as UNROUTED. Deduped: owner-queue-candidates.md is a
curated intake feed and check_owner_queue.py checks citation drift —
neither sweeps lane outboxes for unrouted questions.

## ⟲ Previous-session review

The morning tally (#158) set this slice up well: its ORDER 042 manager
note ("the seat appears to have pre-built both — verify, don't rebuild")
was exactly right — websites ACKed SATISFIED at 06:29Z against #247/#248
with zero wasted rebuild; and its next-3 explicitly parked the two fleet
numbers so nothing was lost. The genuine miss: the tally read the idle
outbox closely enough to quote both questions into ORDER 043's SIM
detail, yet left the two-item queue edit (this whole PR) for a second
slice — routing them in the same tally PR would have cost ~60 lines in a
file it was already summarizing. Concrete workflow improvement: add
"route any OWNER QUESTION found during the outbox sweep into
docs/owner-queue.md in the same PR" to the tally checklist (and the
session idea above is the enforcing backstop when that's skipped).

## Merge posture

No self-merge — merge-on-green sweeps this PR (#159; control/** + docs +
session card, no workflows). ≤2 CI polls then report.
