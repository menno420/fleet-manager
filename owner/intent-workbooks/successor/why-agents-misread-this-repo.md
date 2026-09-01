# Why agents misread this repo — measured, not guessed

> Written 2026-09-01 after this session made three errors on material the
> repository already records correctly. Your reading: *"so many things are
> already clearly documented but unable to be found by you in one try."* The
> first half is exactly right. The second half is not what the measurements
> show, and the difference decides what the rebuild should optimise for.

## What actually happened

`MEASURED` against this session's transcript. **Nothing was unfindable.**

| Miss | Findable? | What went wrong |
|---|---|---|
| Asked what the new hub is called | yes, 3 places | never opened the doc |
| Called `superbot-next` a finished rebuild | yes, first grep | stopped reading inside the line |
| Counted 10 citing pages; 9 were real | n/a | matched a date, called it a citation |

The name sits at `docs/decisions.md:650` and twice in
`docs/planning/2026-08-30-fresh-start-redirect.md`, a doc both `README.md` and
`.claude/CLAUDE.md` name. The `superbot-next` qualifier was inside the line I
had already quoted.

## The shape defect

`MEASURED`: `docs/ESTATE.md:85` is **869 characters**, one cell of it **673**.
That cell opens *"the ground-up bot rebuild"* and puts the reversing qualifier
*"parity ≠ ported"* ~400 characters later.

`MEASURED`, lines over 400 chars: `ESTATE.md` **15** (max 1365) · the
consolidation program **71** (max **7393**) · `MAP.md` 3 · `intent.md` 1 ·
`current-state.md` 0 · `.claude/CLAUDE.md` 0.

`DERIVED`: **shape is the failing axis, not location.** A 673-character cell is
perfectly findable and reliably half-read.

## What I propose for the new hub

1. **One claim per line** — a qualifier never shares a line or cell with the
   claim it reverses. Script-checkable; findability is not.
2. **Anything settled lives in the decisions file, consulted first.**
3. **The boot file routes, it does not summarise** — 404 dense lines teach an
   agent that reading the summary is reading the source.

## Questions for you

1. Rule 3 costs you: a shorter, less useful-feeling boot file, in exchange for
   agents opening real documents. Worth it?
2. Accept a hard line-length limit enforced by a failing check?
3. Is there a document here you have half-read for the same reason?

## Your words

`OWNER`:
