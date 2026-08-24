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

**And the review nearly did not get read.** The poll loop that watched for it
interpolated curl output into a `python3 -c` heredoc with `|| echo NO` as its
fallback, so **any failure of the check printed the same token as a genuine
absence.** It reported "no verdict" for 11 iterations while a review and ten
comments were already on the PR. Re-run with the status code checked and the
error path removed, all three surfaces answered `HTTP 200` immediately. This is
TRAP-003 committed by the instrument built to detect it, and
`docs/CAPABILITIES.md` already records a session losing 24 minutes to the same
shape — the write-up existed and did not bind, which is this session's own N3.

## What landed

- `docs/findings/2026-08-24-e1-source-sweep.md` — what was already sent, topic by
  topic; what was never sent; the mailbox correction; today's re-measured figures.
- `docs/planning/2026-08-24-final-eap-email-draft.md` — the assembled mail.
