# init-prompt-universal — per-project fleet-protocol init prompt

> **Status:** `living-ledger`
>
> Gen-1 text, deployed 2026-07-09 to put existing Projects on the fleet
> coordination protocol. Verbatim — never edit history; add dated successors.

## Deployed text (verbatim)

```
DECIDED: you're now on the fleet coordination protocol. From now on the owner talks to a manager Project, not to you directly — you two coordinate through committed files in THIS repo. Read control/README.md for the contract. Standing ritual, every session:
- FIRST: git pull; read control/inbox.md; do any order with status `new` (priority order); if an order is ambiguous, write it under ⚑ needs-owner in your status and do the rest.
- LAST: overwrite control/status.md — timestamp, phase, health (green/red-by-design+why/broken), last-shipped PR, blockers, orders acked/done, ⚑ needs-owner. Report progress ONLY here; never edit control/inbox.md (the manager owns it).
A routine will wake you on a cadence to run this loop unattended. Rails unchanged (forward-only git, live-test, decide-and-flag, write-back). Confirm now by overwriting control/status.md with your real current status.
```
