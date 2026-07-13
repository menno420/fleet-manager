# 2026-07-13 — Route batch-2 SIM-REQUESTs + venture sandbox ask (Q-0264 fan-in, batch 2)

> **Status:** `complete`
> 📊 Model: fable-5 (worker, dispatched by the fleet-manager coordinator)

Routing slice for the Q-0264 fan-in, batch 2 (batch 1 = ORDER 043 →
idea-engine local ORDER 005, 07:51Z — untouched, not duplicated). No
trigger calls made.

- **ORDER 044** (control/inbox.md, P1, Ideas Lab): the 7 new batch-2
  SIM-REQUESTs as priority intake AFTER ORDER 005's two —
  **venture pricing (3)** from the ~05:00Z morning tally (venture-lab
  control/outbox.md): photo packs PWYW-vs-$5 + $3 anchor + two-pack
  bundle · Ship-It Bundle $59 vs $64/$68 anchors · $19-fixed vs PWYW
  narrow-TAM cookbooks; **superbot-games balance (4)** from its outbox
  @ HEAD (all `status: open`, constants verbatim-pinned per request):
  mining-economy-tuning · fishing-economy-tuning ·
  dnd-escort-double-mint · exploration-reward-bands. Per-module packet
  pointers carried inline; sim-lab prior art named
  (verdict-017-t10-cost-curve, verdict-006-idle-economy-sim-kernel).
- **Local relay same slice:** idea-engine `claude/fm-order-044-relay`
  PR #304 appends the self-contained **local ORDER 006** (the seat
  reads its LOCAL inbox — the ORDER 043/005 lesson applied at dispatch
  time, not discovered later). Their `bootstrap.py check --strict`
  green; control-only fast lane; their enabler lands it on green.
- **B#54 · OQ-VENTURE-SANDBOX-REPO** (docs/owner-queue.md): the tally's
  one owner-gated ask — a tiny sandbox repo (or a one-word approval) to
  production-verify `merge-on-green.yml` before venture adopts it; ~1
  min, reversible, repo creation = owner capability wall. Plus a
  one-line prior-art note under E#52 pointing at sim-lab
  `sims/verdict-017-t10-cost-curve/`.
- **control/status.md** restamped 09:00Z: batch-2 routed; orders line
  reconciled (041 SHIPPED-IN-FULL, 042 ACK SATISFIED per the websites
  08:41Z heartbeat, 043 relayed as local ORDER 005, 044 NEW); next-3
  item 1 now tracks the 005+006 pickups. **Websites batch-2 needed no
  routing** — the seat self-triaged all 8 venture WEBSITE-IDEAs (its
  heartbeat, updated 2026-07-13T08:41:55Z: 4 built #254/#255/#256/#258,
  1 in flight, 1 remaining, 1 dup of #248, 1 owner-gated on the photo
  originals).

## Verification

- `python3 scripts/check_owner_queue.py` → CLEAN (slugs intact +
  unique; exit 0).
- `python3 bootstrap.py check --strict` → red only on this card's
  designed born-red hold while in-progress; green at the complete-flip
  commit.
- idea-engine: `python3 bootstrap.py check --strict` → all checks
  passed (run in their clone before pushing PR #304).

## 💡 Session idea

**SIM-REQUEST route-once ledger (slug + cross-ref check).** Batch
routing now depends on prose memory to avoid double-serving: ORDER 044
had to say "AFTER ORDER 005's two — do not duplicate" because nothing
machine-checks that a lane outbox's `SIM-REQUEST · <slug>` blocks map
1:1 to relay orders. The sibling gap already flagged for OWNER QUESTION
blocks (previous card's tripwire idea) exists for the much busier
SIM-REQUEST class, plus the inverse failure: double-routing burns a
whole Ideas Lab sim cycle, not just a queue line. Cheap enforcing
guard: lane outboxes already name their requests
(`SIM-REQUEST · mining-economy-tuning`); a wake-time checker greps each
lane's `control/outbox.md` for open SIM-REQUEST slugs and requires each
to appear in exactly ONE fm inbox ORDER (flag >6h unrouted AND any slug
appearing in two orders). Deduped: the previous card's tripwire covers
OWNER QUESTION→OQ- mapping only; check_owner_queue.py audits queue
citations; neither sees SIM-REQUEST slugs or the double-route case.

## ⟲ Previous-session review

The route-idle-questions slice (#159) wrote two exemplary six-field
E-items (E#52/E#53 — the recommendation-first structured-choice format
the owner asked for) and its read-only morning checks were accurate:
ORDER 043 was indeed not picked up at 07:30Z as it predicted might
happen. The genuine miss is in that same observation: it saw the
Ideas Lab heartbeat "acked=001-004 only" — proof the seat reads its
LOCAL inbox — and still left ORDER 043 sitting only in the fm inbox
("no intervention taken"), so a separate 07:51Z slice had to relay it
as local ORDER 005. Concrete workflow improvement, applied in this
slice: **dispatch = fm ORDER + same-slice local-inbox relay, always**
— an order to a seat that reads its local inbox isn't dispatched until
it exists there; making the pair one atomic routing step removes the
pickup-lag class entirely. Worth an R-rule in the manager playbook.

## Merge posture

No self-merge — merge-on-green sweeps this PR (#162; control/** +
docs/owner-queue.md + session card, no workflows). idea-engine PR #304
lands via their enabler. ≤2 CI polls each, then report.
