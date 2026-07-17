# Session — fm-recreation-ruling

> **Status:** `complete`

**Branch:** `claude/fm-recreation-ruling-0717`

📊 Model: Opus 4.8 · medium · docs-only

**About to do:** Record owner recreation ruling (event 09027052) across heartbeat/NEXT-TASKS; document the self-scheduling capability wall + reply-bounce pacemaker substitute; file the owner-queue ask. This card held the PR red (HOLD) until the work landed + enders were filled, then flips `complete` last.

**Did:**
- **Recreation ruling recorded (`control/status.md`):** added a dated `2026-07-17 (recreation ruling)` note at the retirement banner — owner ruled (coordinator relay, event 09027052) "This one is the recreation"; this Project IS the recreated fleet-management seat and the FM autonomous loop stands back up. Retirement banner reframed as superseded historical context. Loop cadence = coordinator↔manager reply bounce (no timers). BLOCKER surfaced: wake chain unarmed → I4 MANAGER-FAILSAFE stays FAIL. Bumped `updated:` to `2026-07-17T21:48Z`.
- **Live work source flagged (`docs/NEXT-TASKS.md`):** added a top `2026-07-17 — Recreation ruling landed` entry naming this file as the recreated manager's live work source and the FM-wake-chain unarmed blocker as the top owner-blocker.
- **Capability wall recorded (`docs/CAPABILITIES.md`):** appended a verified `2026-07-17 · wall · autonomous-project` finding — self-scheduling the seat wake chain is walled in BOTH the manager venue (no direct tool; worker-relay classifier-denied ×2) and the coordinator venue (tool absent, attempted once), with the verbatim classifier denial. Substitute recorded: coordinator↔manager reply-bounce pacemaker; residual gap = no clock-based wake against silent mid-turn death.
- **Owner ask filed (`docs/owner-queue.md` §B):** new item `OQ-FM-WAKE-CHAIN-ARM` (six-field + RISK ✅ reversible) — enable the failsafe + pacemaker wake chain OR grant self-scheduling permission; UNBLOCKS I4 MANAGER-FAILSAFE + the dead-man safety net.
- **Checks green:** `check_owner_queue.py` CLEAN exit 0; `check_roster_freshness.py` OK exit 0; `bootstrap.py check --strict` exit 0.

⚑ Self-initiated: None — directed deliverable (coordinator relay of owner ruling event 09027052). No autonomous apparatus resumed; no trigger created, modified, fired, or deleted by this seat (self-scheduling was walled, not attempted-and-succeeded).

💡 Session idea: A `scripts/check_wake_chain.py` dead-man detector — on each wake it reads `telemetry/triggers-snapshot.json` for an FM-session-bound failsafe with a future `next_run_at`, and (a) flags LOUD when the loop is running on reply-bounce alone with no armed clock backstop, and (b) flags when the newest `control/status.md` heartbeat is older than the failsafe cadence (a silent mid-turn death signature). Turns the residual gap this session recorded into an active alarm instead of a documented risk. (Dedup-checked `docs/ideas/` + README — no existing wake-chain / pacemaker / dead-man idea; novel.)

⟲ Previous-session review: The previous session (fm-winddown-housekeeping / PR #288) surfaced I4 MANAGER-FAILSAFE → FAIL with strong discipline and named the exact resolving condition ("if the owner answers C, a failsafe gets armed then") — clean decide-and-flag. What it could not foresee: it assumed the owner-C path would let a failsafe simply "get armed" agent-side, but this session discovered arming is itself classifier-walled in both venues, so answering C does NOT auto-resolve I4 — it needs an owner action. Workflow improvement: when a session defers an action to a future decision, it should also record the *capability precondition* for that action (can we even do it agent-side?), so a deferred step isn't discovered to be walled only once we reach it — the same enforce-don't-exhort instinct applied to deferred work, not just current work.
