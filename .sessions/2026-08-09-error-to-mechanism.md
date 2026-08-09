# 2026-08-09 · hub — turn the error ledger into mechanisms that fire at the moment

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · feature build — score fm #830's 13 errors against
  "could a hook or skill have caught this at the moment?", then build the ones
  that can

Time: 2026-08-09 · venue: owner-live hub chat · branch
`claude/intent-architecture-phase-2-ntsffd` (restarted from `1f620a8` = `origin/main`
after fm #830 merged)

💡 Session idea: **the estate could guard the moment before an action, the
prompt, and the finished reply — and had nothing at all for the moment *after* an
action succeeded.** Three `PreToolUse` hooks, one `Stop`, one `UserPromptSubmit`,
zero `PostToolUse`. That gap is not stylistic: a whole class of defect is
*only* knowable once the change lands. "Did this edit leave the old claim
standing somewhere else?" cannot be answered before the edit, because before it
the old claim is still in the target by definition. The estate had been asking
that question in review, hours later, when the reply was already written.

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached)

## Previous-session review

⟲ fm #830 landed the Phase 2 intent map, the prompt-route bar, and an audit of
the intent-architecture thread. Its most useful output was not the slice but its
**13-error ledger with catcher attribution**: 0 caught by documentation being
available, 9 by adversarial instruments. The owner read that and drew the right
conclusion — *"nearly all of them have been caught without my attention, so this
is already a good example of the system working"* — and asked the follow-on this
session answers: **which of those 13 could a hook or skill have caught at the
moment, and what do the ones that already did tell us about how to build more.**

## What is about to happen

1. **Score all 13** against a single question: is there a moment, and is the
   defect decidable by a machine at that moment?
2. **Build the ones that pass** — as hooks firing at the moment, not checkers
   firing at gate time. A gate-time check is a reviewer; a hook is a guard.
3. **Record the ones that do not pass, with the measurement that says so** —
   including one check that was built, tested against its own motivating case,
   and **failed it**.

## Verification

At close: `python3 bootstrap.py check --strict`, both checkers directly, real
exit codes, each on its own line. Every new check tested **in both directions**
and, where the defect is historical, **replayed against the real pre-fix state
from git** rather than a synthetic fixture. Codex review requested while this
card is born-red.

## Close-out

*(pending)*
