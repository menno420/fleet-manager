# 2026-09-04 — The Couch Legend session's handoff: two records, one route, one continuation prompt

> **Status:** `complete` — merged via fm #1028, branch `claude/couch-legend-docs-handoff-iwpo96`.

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
- `docs/prompts/2026-09-04-couch-legend-phase-b-continuation.md` — the
  continuation prompt for the next Couch Legend session, `continuation-prompt`
  shape, registered in the live banner of `docs/prompts/README.md` (seven LIVE
  files → eight). It branches rather than assumes: phase B is the owner's feel
  pass and gates C and D, so the receiving session's first step is to read
  `docs/owner-comments/couch-legend/README.md` and take the ungated lanes if
  his verdict has not arrived.

## Close-out

**Landed.** Three records plus the route that delivers one of them, and the
handoff prompt that carries the rest.

Every state claim in the prompt was verified at HEAD rather than carried from
the conversation: couch-legend `origin/main` = `4934955` with 0 open PRs and
#19 merged; the old branch `claude/couch-legend-design-arch-iwpo96` still
present at `d790461` and finished; all 16 cited couch-legend paths and 4
fleet-manager paths present at HEAD; and the census numbers **re-derived by
running the instrument** (`pnpm exec tsx tools/stage-evolution.ts` at
`4934955`, exit 0 → 14/18 introduce · 3/18 deepen · 17/18 deliver something
new · 2/18 gate content · 3/18 have scene art · 17 keepsakes into 6 places)
rather than quoted from a summary.

`python3 tools/check_doc_routes.py` → 72 routes · 37 docs routed · 0 errors ·
0 notes. `python3 bootstrap.py check --strict --added-card
.sessions/2026-09-04-couch-legend-handoff-records.md` held red on the born-red
hold alone — confirmed against the CI job log for check run 101096302012,
which reported the same two findings and nothing else — and is expected green
at this flip.

One deviation, stated: a merge of `origin/main` was needed mid-PR
(`.substrate/guard-fires.jsonl` conflicted). Resolved as a union of both
sides in main-then-ours order, all 42,526 lines re-validated as JSON.
