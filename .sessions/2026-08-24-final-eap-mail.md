# 2026-08-24 — E1: the source sweep and the assembled final EAP mail

> **Status:** `in-progress` — branch `claude/final-eap-mail-x2s9kx`, cut from
> `origin/main` at `27b81a4` (fm #942). Born red on purpose; flips only after
> `python3 bootstrap.py check --strict` returns a real exit 0 read directly.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

E1 has been owner-reserved since 2026-08-01 and deferred four times. The owner
lifted the reservation live on 2026-08-24: *"today I want to work on and
possibly finish the final EAP mail."* The reservation was a stored instruction;
the live word wins, and the conflict is named rather than resolved silently.

The work is the half the evidence pack deliberately did not do: sweep **what was
already sent**, so the mail repeats nothing, and assemble the draft. The sweep
found one measured correction to the committed correspondence record and one
genuinely new spine for the mail — the estate spent the month **after** the
program auditing what the fortnight produced, and no other EAP participant can
send that.

## previous-session review

fm #942 (spider-bot registration) landed the ESTATE row and Layer-2 folder. It
left the repo clean at `27b81a4`; nothing about it blocks or feeds this session.

## Adversarial review — round 1, 10 findings, all conceded

`@codex` at `39753f5`: **10 inline findings, 9×P2 + 1×P3, every one accepted.**
Disposition `[conceded] ×10`, `[survived] ×0` — the tally is countable per
[`../docs/conventions/adversarial-review.md`](../docs/conventions/adversarial-review.md).
Four of them are the same species: **a bounded measurement restated at a wider
scope.** The mechanism behind the audit's worst findings became "the dominant
class of all 101"; a self-attested containment became "no access to the
answers"; a storage-composition measurement became "waste"; a grammar covering
undated standing walls became "reds any PR documenting a limitation". Each was
heading into a mail to a third party.

**A defect in the watching instrument, and a causal claim about it that had to
be withdrawn within the hour.** The poll loop interpolated curl output into a
`python3 -c` heredoc with `|| echo NO` as its fallback, so **any failure of the
check printed the same token as a genuine absence** — TRAP-003 committed by the
instrument built to detect it, with `docs/CAPABILITIES.md` already recording a
session losing 24 minutes to the same shape.

**The defect is real. The story first told about it was not.** This card, and
the reply to the owner, first said the loop *"reported no verdict for 11
iterations while a review and ten comments were already on the PR."*
`MEASURED` afterwards: `submitted_at` is **2026-08-24T19:29:21Z** and all ten
inline comments carry 19:29:21–22Z, whereas the loop's ~11 × 28 s ran before
that and a clean status-checked probe *preceding* it returned a genuine
`entries=0`. **So the review was absent for most of the loop, and the defect
cannot be shown to have hidden anything.** What actually happened is duller:
Codex answered at ~35 min against a recorded ~335 s.

Recorded because of *when* it happened — the over-claim was written into the
reply that was itself reporting four Codex findings of exactly this shape, a
bounded fact restated wider. The lesson the session already had in hand did not
bind the sentence it was writing, which is N3 measured on itself twice in one
session.

*(Two of the ten comments are anchored at `f4e8160` rather than `39753f5`;
`created_at` on both is 19:29:2xZ, so they are round-1 findings GitHub
re-anchored to the newer head, not a second round.)*

## What landed

- `docs/findings/2026-08-24-e1-source-sweep.md` — what was already sent, topic by
  topic; what was never sent; the mailbox correction; today's re-measured figures.
- `docs/planning/2026-08-24-final-eap-email-draft.md` — the assembled mail.
