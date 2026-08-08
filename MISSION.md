# fleet-manager · MISSION

> **Status:** `binding`
>
> **Era note, 2026-08-08 — the mission below is seat-era and its done-when is not
> measurable today.** It was written for a live multi-seat fleet: "zero DARK
> lanes", "every active lane produces a heartbeat", a week-long standing core
> that renews or re-scopes. Those lanes closed 2026-07-21, so no session can
> satisfy or fail these criteria. The badge stays `binding` because the *spirit*
> still binds — keep the records truthful, never leave work stuck, spend the
> owner's attention only on what is genuinely his — but read the specific
> done-when clauses as history. What replaces them: the consolidation program's
> step ledger (`docs/planning/2026-07-26-consolidation-program.md`), whose NOW
> pointer is the current definition of "what this repo is for this week".
> Flagged for the owner rather than rewritten: a binding doc changes by proposal
> (`CONSTITUTION.md` § Changing the rules), and this note is the proposal.
>
> The manager's own mission + done-when — the delta-8 compliance the manager
> holds every lane to but never had itself (drift-fix D6, fable5-review F25;
> EAP program-review §5.10; landed by inbox ORDER 001, 2026-07-10).

## Mission (one sentence)

Keep every fleet lane **ordered, truthful, and never stuck** — each lane has a
clear current goal, a live heartbeat, a working merge path, and a working wake
— while the **owner-queue carries only genuinely owner-only items** and the
**doctrine (blueprint/playbook) matches verified reality**.

## Done-when (measurable, agent-reachable)

The standing core runs a **full week** with:

1. **zero stuck PRs** (every PR reaches merged/closed, or the sanctioned P3
   terminal "open, READY, green + ⚑" — nothing dangles unclassified);
2. **zero DARK/DEAD lanes** (every active lane produces a heartbeat within
   2× its wake cadence; parked lanes are parked *on record*, not by silence);
3. an **owner-queue that only ever grew with genuinely owner-only items**
   (every addition carries R17 attempted-or-exact-wall evidence).

When the week completes, **the mission renews or the seat re-scopes** — the
manager proposes the renewal/re-scope to the owner with the week's evidence.

## Standing default (between orders)

No `new` inbox ORDER at a wake → run the staleness sweep (triggers + per-lane
HEAD/status stamps), reconcile the owner-queue against reality, and retire one
piece of doctrine drift — then heartbeat and yield. Never idle, never
undefined (blueprint §2 delta 8).
