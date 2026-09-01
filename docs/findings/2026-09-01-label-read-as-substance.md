# A label read as its contents — six instances in one session

> **Status:** `finding` · tier **RECORD** · dated 2026-09-01 · `MEASURED`
> except where marked. Certainty legend:
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
>
> **What this holds:** one session's six errors, all the same shape, each named
> and located; the document-shape measurements underneath them; and the census
> that redirects the fix. Its register entry is
> [`../traps.md`](../traps.md) **TRAP-008**.

## The shape

A claim was written about *what something is* — a repository, a document, a
table row, an invariant — sourced from its **name, title, heading, or opening
clause** rather than from the thing itself. In every case the disqualifying
detail was present and downstream: later in the cell, later in the file, or in
the document the pointer named.

## The six instances

All 2026-09-01, one session (fm #997–#1004).

| # | The claim | Where the truth was | What was read instead |
|---|---|---|---|
| 1 | `superbot-next` is a finished ground-up rebuild | `docs/ESTATE.md:85`, same cell, ~400 chars on: *"parity ≠ ported"* | the cell's opening clause |
| 2 | The successor hub needs a name | `docs/decisions.md:650`; `planning/2026-08-30-fresh-start-redirect.md:271,424` | the boot file's one-line pointer to that doc |
| 3 | 10 workbook pages cite the owner's answers | 9 did | a `2026-08-31` date-string match |
| 4 | *"No worksheet is longer than 44 lines"* | worksheets shipped at 46 and 47 in the same PR | the inherited sentence |
| 5 | `docs/MAP.md` is the source for a `docs/` index | it is the **repo-wide** router — `.claude/`, `scripts/`, `tools/`, `bootstrap.py`, `../` | its description in the boot file |
| 6 | The door test's level 4 | the five files' contents | `ls` output alone (regraded, fm #1004) |

**Instance 6 is the load-bearing one:** the error occurred *inside the document
written to describe the error*, after five prior instances had been recorded.
A stated rule did not bind its own author in the same session — the mechanism
thesis of [`2026-08-08-why-rules-dont-bind.md`](2026-08-08-why-rules-dont-bind.md)
demonstrated on itself.

## Document shape — why instance 1 was likely

`MEASURED`: `docs/ESTATE.md:85` is **869 characters** on one line; one table
cell is **673**. The claim opens the cell and its reversal sits ~400 characters
downstream, inside it.

`MEASURED`, lines over 400 characters: `ESTATE.md` **15** (max 1365) ·
`planning/2026-07-26-consolidation-program.md` **71** (max **7393**) ·
`MAP.md` 3 · `intent.md` 1 · `current-state.md` 0 · `.claude/CLAUDE.md` 0.

## Findability was never the failing axis

`MEASURED`: none of the six was unfindable. Instance 2's answer existed in
**three** places, in a document both `README.md` and `.claude/CLAUDE.md` name by
path. Instance 1 was found on the **first** grep.

`MEASURED`, the navigability census: **70 of 79** directories under `docs/` and
`owner/` carried a `README.md`. The two live gaps — `docs/` itself and
`owner/intent-workbooks/` — were confirmed against the live API (per-directory
readme endpoint: `Not Found` for both, `README.md` for `docs/repos` and
`owner`) and closed in fm #1003.

`MEASURED`, the population census: `docs/repos/<name>/` implements
folder-per-topic with fixed filenames, adopted 2026-08-08. **10 of 28**
repositories have a folder; **3 of 10** hold anything past `README.md`; **1 of
10** (`spider-swing`) is complete. Designed, adopted, never populated.

`DERIVED`: a rebuild aimed at findability targets the half that already works.
The unpopulated half is the one with the evidence against it.

## What this does not establish

`REASONED`, not measured: that document shape *caused* instance 1. The shape
numbers are exact and repeatable; the causal link rests on one instance.
`n = 6` in one session is a rate for nothing — it is six named instances, which
is what TRAP-008 needs, and not a frequency.
