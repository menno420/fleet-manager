# sim-lab — failsafe wake routine (part 4)

> **Status: NOT ARMED.** The coordinator seat's toolset lacks `create_trigger`
> AND `send_later` (verbatim wall, control/status.md OA-003 @ sim-lab 8b8075d:
> "tool not present in session toolset") — so the routine could not be
> agent-armed at boot and, until this package, its text lived ONLY in the
> coordinator's first chat reply. **This file is the durable capture of that
> chat-only text** (source: the founding package §2 step 4, quoted verbatim
> below — superbot docs/planning/round3-founding-package-simulator-2026-07-10.md
> @ origin/main dc19b1e, which is the committed twin of what the coordinator
> pasted into chat).

## Routine fields

- **Name:** `sim-lab failsafe wake`
- **Cron:** `0 1-23/2 * * *` (ODD hours :00 — the inter-Project stagger
  contract: idea-engine writes at even hours, sim-lab reads one hour later,
  the manager reads both at :30. Change only as a PAIR with idea-engine's
  cadence, through the manager.)
- **Fires into:** the persistent Simulator coordinator chat/session.

## Prompt text — VERBATIM (founding package §2 step 4; do not rephrase)

```
FAILSAFE WAKE (simulator, Q-0265 continuous mode): if your send_later
continuation chain is alive (a pending continuation exists), verify
that in one line and end. If it stalled, RESUME THE WORK LOOP: sync
menno420/sim-lab to origin/main HEAD; read control/inbox.md; pull new
sim-ready entries from menno420/idea-engine control/outbox.md (raw, at
HEAD) into your queue; then work slice after slice — gated verdicts
(validity gate + @codex comment + finalized outbox entry), intake
triage, harness slices — each merged-on-green. Re-arm the continuation
chain (~15 min) before ending the turn; overwrite control/status.md as
each turn's last step. If this trigger is one-shot rather than
recurring, re-arm it for +120 minutes.
```

## Arming — two paths (either one closes OA-003)

1. **Owner-manual (currently pending):** claude.ai → Routines screen → create
   a Routine with the name, cron, and prompt above, targeting the Simulator
   coordinator chat. This is the path OA-003 pre-filed.
2. **Agent-armed, next capable session:** tool availability is SEAT-DEPENDENT
   — a later coordinator session may carry the scheduler tools. Each session
   re-probes its own toolset; if `create_trigger` is present, arm it with
   exactly these fields, VERIFY via `list_triggers` (never wait for the first
   fire as proof — completed runs are not inspectable owner-side), and record
   the exact call + outcome verbatim in `control/status.md`, flipping OA-003
   to done.

Until armed by either path, the seat has NO pacemaker and NO dead-man switch
(this seat's toolset also lacks `send_later`, so the Q-0265 continuation chain
is equally unavailable) — the lane advances only on manual/owner-driven wakes.
Every heartbeat must state the routine's state
(`armed-by-me` / `owner-manual-pending`) until this is resolved.
