# 2026-08-09 · hub — review the intent-architecture thread, then Phase 2

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · review/verify — audit what the intent-architecture
  thread landed, fix what the audit finds, then build the Phase 2 slice

Time: 2026-08-09 · venue: owner-live hub chat · branch
`claude/intent-architecture-phase-2-ntsffd` (started from `d7e7c19`, which is
`origin/main`)

💡 Session idea: **a guard's reach is set by artifact type, not by claim
location — so the estate's most-enforced rule has a hole exactly where its
own toolchain speaks.** `check_no_false_walls.py` is a required status check
built for one rule: never write down a limitation. Its SCAN SET is five file
paths. But the kit itself emits a false wall on **every** `check --strict` run
— `enforcement-required-unverified … (rules API; 403-walled to agents)`, which
`.claude/CLAUDE.md:235-237` records as measured-false since 2026-08-06 — and it
emits it to **stdout**, which no file-scanning checker can reach. The estate
then patched the hole the way it keeps patching holes: a sentence in the boot
file saying *"never quote that NOTE."* That is the injection thesis's own
counter-example sitting inside the injection thesis's home repo. **A claim does
not become safe by being unwritten; it becomes unauditable.**

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached)

## Previous-session review

⟲ fm #828 landed the Layer-2 ratification and recorded the flip-before-review
trap; fm #829 appended 49 guard-fire telemetry records. Both are sound. The
audit below is not a challenge to their conclusions — it is the re-read that
#828's own two-round cap explicitly left owed, and it found that the ledger
#828 built to be *countable* does not render as a table for six of its eleven
rows.

## What is about to happen

The owner asked for two things beyond the Phase 2 build: **why the repo's 27
skills do not appear in the claude.ai Skills settings list**, and **a review of
the already-landed intent-architecture work before continuing**.

1. **The skills answer**, recorded durably rather than only in chat.
2. **Eight audit findings**, verified against source, and the repo-side fixes
   for those that need no owner decision.
3. **The Phase 2 slice**, tested against real historical owner messages.

## Verification

At close: `python3 bootstrap.py check --strict`, plus both checkers directly,
real exit codes, each on its own line — never `$?` after a pipe. Codex review
requested **while this card is still born-red** (`session-close` 6c).

## Close-out

*(pending — this card is born-red and stays that way until everything owed to
the PR has happened.)*
