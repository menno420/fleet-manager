# 2026-07-10 — Night-review remediation (freeze ⚑B/⚑D, URGENT visibility, R22/R23, visibility recipe)

> **Status:** `complete`

📊 Model: Fable 5 (claude-fable-5) · fleet worker (remediation lane, night-review follow-ups) · start 2026-07-10T12:29Z · end 2026-07-10T12:40Z (`date -u`)

## Declared at open (born-red)

Docs-only remediation PR executing the committed night review's must-act
follow-ups (`docs/findings/night-review-2026-07-10.md`). About to land:

1. `docs/owner-queue.md` — (i) FROZEN annotations on the venture-lab ⚑B and
   ⚑D publish clicks (D1 Stripe defect; unfreeze rides venture-lab's fix
   ORDER with a real-path test); (ii) a new URGENT top-of-queue item: flip
   pokemon-mod-lab to PRIVATE (night-review Q16 — vendored Nintendo source
   world-readable against the lane's own "no exceptions" rail) + an invite
   to an account-wide visibility review.
2. `docs/playbook.md` — R22 VISIBILITY GUARD + R23 OWNER-ASK TRUTH-CHECK
   (provenance: Q-0194 friction→guard class, night-review-2026-07-10
   Q16/Q2/Q6/Q18 findings).
3. `docs/capabilities.md` — CAN entry: the one-call repo-visibility check
   recipe (`GET /repos/{owner}/{repo}` → `.private`/`.visibility`).
4. `docs/dispatch-log.md` — dated section for this remediation landing +
   the four lane ORDERs being dispatched immediately after this PR merges
   (venture-lab P0 D1/D2/D3 fix; superbot-games P0 CI collection-scope fix;
   trading-strategy promotion-significance bar; pokemon-mod-lab post-flip
   visibility verification).
5. `docs/handoff-2026-07-09.md` — open-thread lines for the freeze, the
   URGENT visibility item, and the four ORDERs.

Landing: born-red card holds substrate-gate red; flips `complete` as the
deliberate last commit; REST merge-on-green (R21 — born-red shape, no arm
attempt). Composed at main HEAD `6397f09`; re-read before flip (R19).

## Done (close-out)

All deliverables landed on PR #23, with one declared-vs-shipped deviation,
flagged: **item 5's handoff lines went to `control/status.md`, not
`docs/handoff-2026-07-09.md`** — the handoff doc carries a "CLOSED OUT
2026-07-10, now historical context; current truth lives in control/status.md"
banner, so appending live threads there would have been exactly the drift
class the repo warns about. The live handoff surface got the lines instead:
the remediation-ORDERs in-flight block, the 🚨 PUBLIC-repo line, the
venture-lab lane-line freeze, and `last-shipped` updated.

Shipped:

- `docs/owner-queue.md` — ⚑B and ⚑D each carry the verbatim freeze
  annotation ("FROZEN 2026-07-10: D1 Stripe defect (headline paid path never
  executed; customer_email null on live events + invalid {CHECKOUT_EMAIL}
  success-URL placeholder) — unfreezes when venture-lab's fix ORDER lands
  with a real-path test"), original click instructions retained inside
  "(When unfrozen: …)". New 🚨 URGENT blockquote at the very top of the
  Active queue: pokemon-mod-lab → PRIVATE (Settings → Danger Zone), WHY +
  owner-only proof + second line inviting the account-wide visibility
  review. Item 3's stale "(PRIVATE — never publish)" corrected on sight
  (drift-on-sight rule).
- `docs/playbook.md` — new "VERIFICATION GUARDS" section after MERGE
  MECHANICS: R22 (visibility verified via API every session start where a
  rail depends on it) + R23 (no publish/spend/send owner ask without
  non-author end-to-end verification evidence), each with WHY + provenance.
- `docs/capabilities.md` — CAN entry "Check a repo's ACTUAL visibility —
  one API call" with curl/gh/MCP forms, cross-linked to R22.
- `docs/dispatch-log.md` — "2026-07-10 — afternoon (night-review remediation
  dispatch)" section: the landings + the four lane ORDERs (venture-lab P0,
  superbot-games P0, trading-strategy, pokemon-mod-lab post-flip).
- `control/status.md` — see deviation note above.

R19 held: composed at `6397f09`, re-fetched before this flip — main
unmoved. Landing via REST merge-on-green per R21.

## 💡 Session idea

**Freeze is a state, so give the owner-queue a tiny state grammar.** ⚑B/⚑D
now carry prose freezes, and R23 will create more of them — but nothing
machine-readable distinguishes "clickable" from "frozen" from
"depends-on-unmet". Adopt three inline tokens in owner-queue items
(`READY:` / `FROZEN(<reason-ref>):` / `DEPENDS-ON(<item>):`) and a ~20-line
advisory checker that fails when an item invites an outward-facing click
(publish/spend/send verbs) without a READY token backed by a
verification-evidence link. That converts R23 from a rule someone must
remember into the Q15 checker class the fleet already knows how to build —
and it directly implements the night review's Q18 `depends-on:` mechanism.

## ⟲ Previous-session review

The night-review landing session (#21) did the hard part right: it verified
every claim against live HEAD instead of lane reports, and its improvised
"Post-review delta" section (reconciling #20 merging mid-composition) is a
genuinely reusable template. What it left on the table is exactly what this
session had to be dispatched for: a 1,598-line audit whose top findings
(frozen clicks, the PUBLIC repo, R22/R23) remained prose recommendations
with no executor named — the review's own Q15 diagnosis ("excellent at
finding, no machinery for retiring") applied to itself within the hour.
Concrete improvement: audit-class findings docs should end with a
machine-scannable "MUST-ACT" block (item · owner-lane · deadline) that the
manager converts to ORDERs/queue edits in the same session the audit lands,
not in a separately-commissioned follow-up.
