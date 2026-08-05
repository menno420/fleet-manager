# 2026-08-05 · hub — fix the boot path and the handoff skill that narrowed an owner's ask

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: a session skipped the document its own repo calls
*"read this if you read nothing else"* — and it did so by following the
handoff prompt correctly. The prompt was faithful to eight of nine owner asks
and narrowed the first one, because the skill that wrote it caps `READ FIRST`
at *"the minimum to act"* with no exception for a session whose job **is** the
reading.

## Previous-session review

The three-repo state audit (#761/#763) measured well and landed clean, but its
Phase 1 was scoped to what the bot audit needed rather than to the repo. The
owner caught it. Root-causing that miss is this session's work, and it lands on
the skill rather than on either session's care.

## Scope

Three fixes plus their record, all owner-directed live:

1. `.claude/CLAUDE.md` — the read path omits the two docs `current-state.md`
   names as essential, including the one it calls *"read this if you read
   nothing else."*
2. `.claude/skills/continuation-prompt/SKILL.md` — `READ FIRST` is capped at
   2–4 paths, *"not a reading list — the minimum to act correctly"*, and the
   traps delegate completeness to the boot file. Both are right for a normal
   handoff and wrong for a comprehension mandate.
3. A findings doc carrying the forensic comparison and the intent review, so
   neither lives only in chat.

## What landed

*(in progress — filled at close)*

## Verification

*(in progress — both gates, real exit codes, post-commit)*
