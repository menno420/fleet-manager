# 2026-08-05 · hub — establish what is actually true across fleet-manager, superbot and superbot-next

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: the previous session's every failure came from the same move —
reading code and inferring, while skipping both repositories' required boot
files. This session inverts it: read the documents first, trust them until they
contradict the tree, and run the one-command check whenever one exists.

## Previous-session review

PR #760 corrected the menu-parity claim and established that **the navigation
graph is the product**, not the command list — 60 of 66 `help` panels in
superbot-next have zero buttons. PR #759 recorded the live audit and the
`CAPTURE-WORLD LITERAL` finding. Both left explicit honest nulls (§ 9 of the
live-audit doc): the literal sweep was never run, and the two-tap reachability
property was never measured. This session picks up from those nulls.

## Scope

Three phases, strictly ordered — reading first, verifying second:

1. **fleet-manager** — the estate's history and terminal states, completely.
2. **superbot** — docs, a fair share of the 967 session cards, then the CODE:
   the help system, cog construction, helper files, how it fits together.
   Separate files that are sound from files that need work (server-relevant only).
3. **superbot-next** — same treatment, comparative: which parts are genuinely
   better built.

Deliberate non-scope: no bot code written; game subsystems noted but not
depth-read; the disband decision is the owner's; the rebuild plan is a later
session's job. This is the foundation, not the plan.

## What landed

*(in progress — filled at close)*

## Verification

*(in progress — both gates, real exit codes, post-commit)*
