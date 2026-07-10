# init-prompt-universal — per-project fleet-protocol init prompt

> **Status:** `living-ledger`
>
> Gen-1 text deployed 2026-07-09; **superseded 2026-07-10** by the dated
> successor below (ORDER 001 / drift-fix D5, fable5-review F21: the deployed
> text asserted "a routine will wake you" as fact, but no routine existed for
> 7 of 9 lanes — the owner's next prompt was the de-facto wake). Convention:
> verbatim deployed texts are never edited; dated successors are appended.
> **Use the current text for every new deployment.**

## Current text (2026-07-10 successor — the one to deploy)

Changes vs gen-1: the false routine promise is replaced by the **VERIFIED
routine recipe** (blueprint §2a rider; proven by websites ORDER 008, trading
ORDER 006, kit ORDER 010, superbot-next ORDER 008, the manager's own trigger).

```
DECIDED: you're now on the fleet coordination protocol. From now on the owner talks to a manager Project, not to you directly — you two coordinate through committed files in THIS repo. Read control/README.md for the contract. Standing ritual, every session:
- FIRST: git pull; read control/inbox.md; do any order with status `new` (priority order); if an order is ambiguous, write it under ⚑ needs-owner in your status and do the rest.
- LAST: overwrite control/status.md — timestamp, phase, health (green/red-by-design+why/broken), last-shipped PR, blockers, orders acked/done, ⚑ needs-owner. Report progress ONLY here; never edit control/inbox.md (the manager owns it).
WAKE CADENCE — arm it yourself (verified recipe, seat-dependent): call the claude-code-remote MCP tool `create_trigger` with name, cron_expression (cadence per your lane class — blueprint §2a), the standing-ritual prompt above, and EITHER persistent_session_id (your long-lived session id — cse_/session_ prefixes both accepted) OR create_new_session_on_fire=true for a fresh session per fire (proven by websites; archive-immune). Verify with `list_triggers`; record the verbatim call + outcome in control/status.md. At seat cutover: the NEW seat re-arms its own trigger FIRST, then `delete_trigger` the old one (F-1 rule). The tool family is SEAT-DEPENDENT — if it is absent or refused on your seat, record the exact tool call + verbatim error in status and ⚑ flag the owner routine click as the fallback. Until a wake fires, assume NO routine is waking you: if no wake arrives within 2× your cadence, flag ⚑ and operate self-terminal (finish each session as if no successor is guaranteed).
Rails unchanged (forward-only git, live-test, decide-and-flag, write-back). Confirm now by overwriting control/status.md with your real current status.
```

### Known limit — routine recipe rider (dated append 2026-07-10 ~20:00Z; include with every deployment)

The model a fired session runs under is **not reliably determinable from the
Routines screen** — model attribution is inconsistent across surfaces (the
Routines menu displays fable-5 for all project-created routines while the
evidenced websites fired session's chat header and own card said sonnet-5;
evidence + probe: `../capabilities.md` § routine self-arm rider). There is no
agent-side pin: `create_trigger` exposes **no model parameter** (probed
2026-07-10). Mitigation is self-report: **record your own model identity
(family-level, e.g. fable-5 / sonnet-5 — never exact IDs) on your session card's
`📊 Model:` line every session**, taken from your own harness/environment at the
moment of work. Deployers: append this known-limit line when pasting the Current
text above (the verbatim block itself is never edited per this file's convention).

## Deployed text (gen-1, 2026-07-09 — SUPERSEDED, kept verbatim for history)

Known-false line (F21): "A routine will wake you on a cadence…" — routine
creation was never performed for most gen-1 lanes; do not redeploy this text.

```
DECIDED: you're now on the fleet coordination protocol. From now on the owner talks to a manager Project, not to you directly — you two coordinate through committed files in THIS repo. Read control/README.md for the contract. Standing ritual, every session:
- FIRST: git pull; read control/inbox.md; do any order with status `new` (priority order); if an order is ambiguous, write it under ⚑ needs-owner in your status and do the rest.
- LAST: overwrite control/status.md — timestamp, phase, health (green/red-by-design+why/broken), last-shipped PR, blockers, orders acked/done, ⚑ needs-owner. Report progress ONLY here; never edit control/inbox.md (the manager owns it).
A routine will wake you on a cadence to run this loop unattended. Rails unchanged (forward-only git, live-test, decide-and-flag, write-back). Confirm now by overwriting control/status.md with your real current status.
```
