# 2026-09-01 — why agents misread this repo, measured

> **Status:** `in-progress` — born red. Flips to `complete` only after the
> branch is pushed, the PR is open and ready, and the strict check has run with
> its real exit code read.

- **📊 Model:** withheld · high · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_013ME1H7CPbqA1FBxJ61VPC2](https://claude.ai/code/session_013ME1H7CPbqA1FBxJ61VPC2) · "Owner-directed documents review"

💡 Session idea: **findability and readability are different failure modes and
the estate has been treating them as one.** Three misses this session, zero of
them unfindable: one pointer read instead of its document, one qualifier
skipped inside a line already quoted, one date matched and reported as a
citation. Reorganising for findability would have prevented none of them.

## Mission

The owner, live, after the third miss: *"This is exactly why I need the
fleet-manager rebuild. So many things are already clearly documented but unable
to be found by you in one try. This is what needs to be prevented."*

His diagnosis is right about the cause and wrong about the mechanism, and the
difference decides what the rebuild optimises for. Measure the three misses
against the tree rather than agreeing, and put the result where he reads next
week — he is pausing every AI subscription for about a week from ~2026-09-10.

## Previous-session review

- `2026-09-01-owner-workbook-expansion.md` (this session, fm #997) — added the
  four new sections and the answer convention.
- `2026-09-01-owner-workbook-filename-claims.md` (this session, fm #998) —
  corrected three claims that were true of a filename and false of the file.
  **This card is the third instance of that same class**, which is why it is
  worth a measurement rather than another correction.

## Shipped

- `owner/intent-workbooks/successor/why-agents-misread-this-repo.md` — the
  measured finding, as an answerable worksheet with three questions.
- `owner/intent-workbooks/successor/README.md` — links it.
- `owner/intent-workbooks.md` — two corrections, both self-inflicted in fm #997:
  the count (71 → 72) and a **false invariant**, "no worksheet is longer than
  44 lines", which I carried forward while shipping two worksheets at 46 and
  47. Replaced with the measured statement.

## The measurements

- `docs/ESTATE.md:85` is **869 characters** on one line; one table cell is
  **673**. It opens *"the ground-up bot rebuild"* and places the reversing
  qualifier *"parity ≠ ported"* ~400 characters downstream in the same cell.
  That is the line I quoted and half-read.
- Lines over 400 characters: `ESTATE.md` **15** (max 1365) · the consolidation
  program **71** (max **7393**) · `MAP.md` 3 · `intent.md` 1 ·
  `current-state.md` 0 · `.claude/CLAUDE.md` 0.
- The hub-name decision I asked him to re-answer sits at `docs/decisions.md:650`
  and twice in `docs/planning/2026-08-30-fresh-start-redirect.md` (`:271`,
  `:424`), a document both `README.md` and `.claude/CLAUDE.md` name. Findable
  three ways; opened zero times.

## Verification

(filled at close)
