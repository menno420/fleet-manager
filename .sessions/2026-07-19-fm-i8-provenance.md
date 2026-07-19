# 2026-07-19 · fm build slice — seat-provenance-aware I8 remedy + roster-cron closeout

> **Status:** `in-progress`

About to happen (declared born-red): build slice #3 from
`docs/planning/2026-07-19-next-slices.md` — rewrite the I8 DUPLICATE-CRON remedy line
in `scripts/check_trigger_health.py` from the generic "keep the OLDEST-created" rule
(which contradicted the correct call on the live SBW pair this very night — the
NEWER trigger belonged to the current seat session; the OLDER was the crash-orphan)
to provenance-aware guidance: verify EACH id's bound session against the owning
seat's live heartbeat; the id bound to the seat's CURRENT session stays, others are
crash-orphans the owning seat (or hub) deletes; keep-oldest is NOT the rule.
Selfcheck assertions updated to pin the new wording. PLUS the roster-cron owner-queue
closeout now fm #344 has merged (odd-hour second cron `40 1-23/2 * * *` verified live
on origin/main): move `OQ-FM-ROSTER-CRON-RELIABILITY` to Resolved with the delivery-
proof condition noted, and refresh the `control/status.md` baton. Claim
`control/claims/claude-fm-i8-provenance.md` (deleted in the flip commit). No
trigger-MCP calls from this venue; no sibling repo written.

- **📊 Model:** fable-5 · high · feature build — remedy-text edit to a verified checker + records closeout (Q-0105 provenance tier)
