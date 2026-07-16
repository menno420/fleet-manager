# 2026-07-16 — recreation-runbook-0716 (EAP project-recreation runbook)

> **Status:** `complete`
> **Branch:** claude/recreation-runbook-0716

Ship docs/project-recreation-runbook.md: the fleet's operational runbook for stopping and recreating Projects inside the Anthropic EAP wind-down window (ends 2026-07-21 17:00 PT). Adds per-project closeout, per-seat recreation, A/B-test notes, and an orphan-sweep procedure keyed to the 2026-07-16T15:26:43Z trigger snapshot. Also: a dated EAP note + runbook link in current-state.md, and a heartbeat refresh.

## Enders
- **📊 Model:** Claude Opus 4.8 family · high · fleet-manager records/oversight seat.
- **💡 Session idea:** A `scripts/check_orphan_triggers.py` that diffs a fresh `list_triggers` export against the failsafe-id table in the recreation runbook and flags any trigger bound to a session whose repo heartbeat is stale — turns the manual §5 orphan sweep into an enforcing checker (dedup-grepped docs/ideas/ — no existing orphan-trigger checker).
- **⟲ Previous-session review:** The pr-audit-0716 session correctly routed owner-only PR-landing items to the owner-queue rather than acting on them — good restraint. It could have captured the EAP wind-down as a dated current-state note the moment the owner's email landed; this session closes that gap. System improvement: the failsafe-id-by-seat mapping now lives in a durable runbook table instead of only in the transient telemetry snapshot, so an orphan sweep no longer depends on re-parsing a 2.7MB JSON.
