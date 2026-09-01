# Why agents misread this repo — measured, not guessed

> Written 2026-09-01 after this session made three errors on material the
> repository already records correctly. Your reading: *"so many things are
> already clearly documented but unable to be found by you in one try."*

## What actually happened

`MEASURED` against this session's transcript. **Nothing was unfindable.**

| Miss | Findable? | Cause | A check could catch it? |
|---|---|---|---|
| Asked what the new hub is called | yes, 3 places | never opened the doc | no — a reading habit |
| Called `superbot-next` a finished rebuild | yes, first grep | stopped reading inside the line | **yes** |
| Counted 10 citing pages; 9 were real | n/a | matched a date, called it a citation | no — my method |

The name sits at `docs/decisions.md:650` and twice in
`docs/planning/2026-08-30-fresh-start-redirect.md`, a doc both `README.md` and
`.claude/CLAUDE.md` name. The `superbot-next` qualifier was inside the line I
had already quoted.

## The shape defect

`MEASURED`: `docs/ESTATE.md:85` is **869 characters**, one cell of it **673**.
That cell opens *"the ground-up bot rebuild"* and puts the reversing qualifier
*"parity ≠ ported"* ~400 characters later.

`MEASURED`, lines over 400 chars: `ESTATE.md` **15** (max 1365) · the
consolidation program **71** (max **7393**) · `MAP.md` 3 · rest 0–1.

`DERIVED`: **a mechanical rule covers one miss in three.** Corrected
2026-09-01 — this page first claimed shape was *the* failing axis, and its own
table disagrees. Worth building, but the other two need the hub designed so the
obvious read is the correct one. That is what you asked for, and it is harder
than a lint rule.

## What I propose

1. **One claim per line** — a qualifier never shares a line or cell with the
   claim it reverses. The only one of these a build can fail on.
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
