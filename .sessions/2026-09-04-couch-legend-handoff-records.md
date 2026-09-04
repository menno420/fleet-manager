# 2026-09-04 — Two findings the Couch Legend session left in the chat

> **Status:** `in-progress` — branch `claude/couch-legend-docs-handoff-iwpo96`.

- **📊 Model:** Opus 5 · xhigh · docs-only
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01FAkSXD7ZQ7E7XzysZmLRbF](https://claude.ai/code/session_01FAkSXD7ZQ7E7XzysZmLRbF) · "Couch Legend game design and architecture"

## Previous-session review

Same session, later turn. `.sessions/2026-09-04-couch-legend-long-form-route.md`
(merged in fm #1026) carried the route update; couch-legend #19 merged as
`4934955`. Both are terminal — verified against the API, not from memory.

## 💡 Session idea

Two things cost that session a cycle each and were about to survive only as
chat. Neither is about Couch Legend; both are about how this estate's tools
actually behave, so both belong where the next session meets them rather than
in a game repo's card.

## What is about to happen

Record them, and — because the trap register's own rule is that an entry
without a route is unfinished work — deliver the second one at the moment it
applies rather than filing it and hoping.

## What changed

- `docs/CAPABILITIES.md` — a Codex inline review comment's `commit_id` is
  **not** which round produced it: GitHub re-anchors an unresolved comment to
  the newest commit touching its file. `original_commit_id` is the stable
  field. Measured on couch-legend #19: 6 of round 1's 11 comments reported the
  round-2 head while the summary still read *Running*, which looked exactly
  like six new findings and was not.
- `docs/traps.md` — **TRAP-010**: the local kit gate and the CI gate are not
  the same command. `check --strict` exited 0 while CI's added-card lane exited
  1 on card grammar, costing a red required check on an otherwise-ready head.
- `.claude/hooks/doc-routes.json` — the delivery. A new `added-card-lane` route
  was written first and **measured not to fire** (the two existing card routes
  already claim `docs/traps.md` at that moment), so the instruction was folded
  into `card-status-write`, which demonstrably does. Proven by feeding the hook
  a synthetic `.sessions/*.md` edit and grepping the delivered text.

## Close-out

*(filled at the flip)*
