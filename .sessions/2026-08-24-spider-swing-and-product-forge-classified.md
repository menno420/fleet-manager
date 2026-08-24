# 2026-08-24 — the unjudged repo fails, and so does the one we thought we'd sized

> **Status:** `in-progress` — branch `claude/d2-fleet-manager-classify-2srczr`,
> cut from `origin/main` at `68dbe90` (fm #939). Born red on purpose: the card
> is the merge hold, and it stays `in-progress` until a `@codex` verdict covers
> the head this PR is flipped on.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

D2's order has been **PROVISIONAL** since fm #938, for one stated reason:
`spider-swing` was swept but never judged, and it is the estate's only asset
with a live external clock. Until it has a verdict the order below it may be
wrong. This session judges it, judges `product-forge` properly, and settles
the order.

## Scope, and what it deliberately is not

**In:** classification. `spider-swing` gets its first verdict; `product-forge`
gets a re-characterised one; § 5's activity table is re-measured live; § 6 is
re-ranked and the PROVISIONAL marker discharged; each failing repo gets a
turnkey fix brief so the next session executes instead of re-deriving.

**Out — and this is a decision, not an omission:** the *fixes* themselves. Each
is a write to a satellite repo with its own gates, its own born-red card and its
own PR — `spider-swing`'s `main` requires **both** `substrate-gate` and
`game-quality`. Four landings in one session is not OD-6, and the audit's own
rejected note (*presence of a file is not truth of its contents*) is the reason
classifying first was worth a session at all: it changed what the fix has to be.

## previous-session review

⟲ fm **#939** (`68dbe90`) — the immediately preceding work, and it is the reason
this session exists in the shape it does. #938 shipped TRAP-007 stating that a
clean `@codex` pass identifies its head *only* through a `Reviewed commit:` line;
#939 measured a second clean-pass shape that carries no such line and corrected
the rule to *try the line, then match your head among the body's 40-hex strings*.
That correction is load-bearing here — this PR's own flip depends on reading a
verdict correctly, and the narrower rule would have produced a false negative.

⟲ fm **#938** (`9bd48b4`) is the direct predecessor of this session's task: it
found the census defect (16 of 17 swept, `spider-swing` unjudged) and marked § 6
**PROVISIONAL** rather than papering over it. That marker held correctly and is
what this session discharges. Its judgement stands unchanged; nothing in it
needed correcting.

## Verify

`python3 bootstrap.py check --strict` → to be recorded at close, read from a
redirect and never after a pipe.
