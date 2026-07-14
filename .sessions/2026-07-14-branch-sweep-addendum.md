# 2026-07-14 — branch-sweep addendum (dispatched executor)

> **Status:** `complete`

About to: append the settled root-cause research + remedy to docs/findings/branch-recreation-census-2026-07-14.md and true owner-checklist row 11 (remedy = kit scheduled cron sweep, kit inbox ORDER 023 dispatched by a sibling worker).

📊 Model: fable-5

## Done
- Census addendum (root cause settled: app/bot-actor merges skip auto-delete; remedy: kit scheduled cron sweep — ORDER 023) — docs/findings/branch-recreation-census-2026-07-14.md
- Owner-checklist row 11 trued to the settled remedy.
- Kit lane write handled by sibling worker (substrate-kit PR, ORDER 023).

💡 Session idea: the owner-checklist rows that reference findings docs could carry a `last-trued:` date stamp per row, so a staleness sweep can machine-check which rows predate their cited finding's newest addendum.

⟲ Previous-session review: the walkthrough-sweep session (2026-07-14) landed 11/13 walkthroughs and flagged stragglers explicitly — good honest accounting; improvement: it left row 11's remedy as "enable the setting" although the census it cited already showed the setting not firing for bot merges — a truing pass should reconcile the rec column, not just the note, when evidence undercuts the rec.
