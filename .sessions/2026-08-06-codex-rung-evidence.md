# 2026-08-06 · hub — the Codex rung got tested, and it holds

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-06 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: `docs/conventions/adversarial-review.md` was landed an hour ago
carrying the honest null *"the Codex rung is described but untested here."* It
is now tested. Updating a doc the moment its own null closes is the whole point
of writing nulls down.

## The evidence

`MEASURED-PRIOR` — reported by the session that ran it, not re-derived here. On
`menno420/substrate-kit#580`, a plan **Gemini had already reviewed**, Codex
returned **9 findings: 5×P1, 4×P2.**

That is the ladder claim surviving contact. A third *opinion* overlaps with the
second; a different *instrument* returns orthogonal findings. The sharpest one
is a statement about what code does rather than what prose says:

> `currency.py` fetches four file paths, not trees — so `adopters.md` cannot
> establish absence of alternate linkage.

No prose review reaches that. It requires reading the fetch.

## The trap, which is the reusable part

**The Codex review summary body is boilerplate. The findings are inline
comments on the diff.**

A session that reads only the summary concludes Codex found nothing — a silent,
plausible-looking null, which is the exact failure shape this repo has spent two
days documenting. Landed in the convention with the instruction to fetch review
*comments*, and to say "the fetch returned empty" explicitly rather than
reporting "no findings".

## The accidental experiment passed

My two Codex rules — record what it objected to rather than that it approved,
and verify before conceding — **never reached that session.** The owner had
already sent the block without them.

It did both unprompted: fetched the findings, **verified Codex's checkable
claims before responding to any of them**, and reported which held. Both did,
including two `.gitmodules` cases it had itself missed. Same shape as the Vertex
routing test the owner ran deliberately, and the same result.

## What I did not claim

That session called the findings *"materially sharper than Gemini's."* That is
its own judgement, on one PR, about a review of its own work — recorded in the
convention as **suggestive, not measured**, with the note that the ladder
argument does not need it. Nine orthogonal findings support "different
instruments find different things" on their own; a ranking would need more than
one sample.

## Verification

- `python3 tools/check_doc_routes.py --strict` → recorded at close
- `python3 tools/check_no_false_walls.py --strict` → recorded at close
- `python3 bootstrap.py check --strict --require-session-log --simulate-added-card`
  → recorded at close

## Honest nulls

- **One data point**, and it is second-hand: reported by the session under
  review rather than measured independently. I did not read `#580`'s diff or its
  review comments myself.
- **Nothing here establishes Codex's false-positive rate.** Two of nine findings
  were verified; the other seven were not checked by me.
- **The P1/P2 severity labels are Codex's own**, not independently assessed.
- **`substrate-kit#580` was still open at the time of writing** — the fixes were
  in progress, so nothing here says the outcome was good, only that the review
  produced findings that verified.

## ⟲ Previous-session review

The card before this one landed a spec that had existed only in chat, and its
own honest-nulls section named the Codex rung as untested. That null closed
within the hour. **A null is not a disclaimer — it is a standing question with
an address**, and this is the first one today that got answered rather than
inherited.
