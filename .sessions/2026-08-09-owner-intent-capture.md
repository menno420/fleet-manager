# 2026-08-09 · hub — the owner's intent, asked and captured

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only — capture 21 owner intent answers; reconcile the directives they change

Time: 2026-08-09 · venue: owner-live hub chat · branch
`claude/fleet-manager-rules-enforcement-18o8t1` (restarted from `f53d7ea` —
Phase 1 merged as fm #826, so the prior commits are already-merged history)

💡 Session idea: **the estate has been recording what it decided and almost never
what it is for.** Twelve OD rows, two D-entries and a PL register all answer
*"what was chosen"*; nothing answered *"what would make the owner say yes, that
is what I meant"*. This session asked, and the answers immediately contradicted
two standing directives — which is the point: intent that is never asked for
does not stay consistent with the rules written under it.

Layer-2 handoff: pending (fleet-manager itself)

## What is about to happen

The owner answered a 21-question intent batch covering purpose, success,
non-goals, decision heuristics, provider roles and question style. This session
lands them as a durable intent surface, and reconciles the standing directives
his answers change — **OD-3 (archive-never-delete)** and **OD-6 (pace: slow)**
both get amendments from his own words, and a new directive records that method
and enforcement work precedes high-value product work.

Verification at close: `python3 bootstrap.py check --strict` (fans out through
`scripts/preflight.py`), plus both checkers run directly, real exit codes.
