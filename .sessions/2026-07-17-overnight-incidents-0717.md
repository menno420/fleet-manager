# Session — overnight-incidents-0717

> **Status:** `complete`

**Branch:** `claude/overnight-incidents-0717`

📊 Model: Opus 4.8 · records slice · fleet-manager overnight-incident register entry

**Title:** Overnight run incident record (2026-07-17)

**About to:** record the coordinator's 2026-07-17 overnight audit findings (decision-freeze + draft-parking stall classes) as a dated section in docs/fleet-triage.md.

**Did:** Added `## 2026-07-17 · overnight run analysis` to `docs/fleet-triage.md` (inserted before the `How to re-verdict` footer, after the 2026-07-16 late-evening sweep) — run split (10 producing seats; idea-engine ↔ sim-lab pipeline to V104) plus two PR-cited stall-class incidents (decision-freeze on superbot-next #499/#500; draft-parking on gba-homebrew ×10 + pokemon-mod-lab ×2), quiet-seats note, and an EAP recreation A/B pointer to `docs/project-recreation-runbook.md` (link target verified on disk). Refreshed `control/status.md` heartbeat wholesale (2026-07-17T06:55Z; #275/#276 moved to merged; baton = owner veto pass + recreation/orphan sweep). Left `control/inbox.md` untouched.

⚑ Self-initiated: none — coordinator-directed records slice (overnight incident register entry).

💡 Session idea: a lightweight nightly "landed vs. opened" counter per seat — a small workflow that tallies PRs opened against PRs merged for each repo over the night window and flags any seat where opened >> merged. Draft-parking (gba-homebrew's 10 unmerged drafts, pokemon-mod-lab's 2) is currently caught only by a manual audit the morning after; a per-seat open/merge delta surfaced at each wake would catch it automatically the same night, turning tonight's incident class into a standing telemetry signal instead of a retrospective finding.

⟲ Previous-session review: night-snapshot-0717 (PR #275) did a thorough full-cursor trigger export (22 pages to exhaustion) with clean verdicts and honest deltas — good discipline on the terminal-page confirmation. Its own 💡 (a derived triggers-summary.json sidecar) is well-aimed. Workflow improvement it surfaces: it flagged that the trigger snapshot has no auto-regen equivalent to roster-regen.yml, so I6 SNAPSHOT-FRESH predictably drifts to WARN between manual refreshes — a snapshot-refresh cron parallel to roster-regen.yml would keep I6 green without burning a dedicated session, the same "automate the freshness, don't audit it" instinct as this session's landed-vs-opened idea.
