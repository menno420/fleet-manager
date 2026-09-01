# 2026-09-01 — why agents misread this repo, measured

> **Status:** `complete` — the measured worksheet and both corrections are
> pushed; fm #999 is open and ready; the strict check ran with its real exit
> code read and its only blocking finding was this card's own born-red hold.

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

- `python3 bootstrap.py check --strict` → **exit 1, read directly, not after a
  pipe** (TRAP-002). Sole blocking finding: this card's designed born-red hold.
  Every other lane exit 0, including `workbook progress drift`.
- **The index claim cross-checked against the generator rather than counted by
  hand**: `owner/intent-workbooks.md` says 72, `tools/gen_workbook_progress.py`
  says 72. Hand-counting is what produced the stale 71 this PR fixes.
- **The false invariant tested before replacing it**, not assumed: the three
  longest worksheets on `main` measured 67, 47, 46 against a claimed ceiling of
  44. Two of the three were shipped by fm #997 in the same change that carried
  the claim forward.
- The new worksheet was **63 lines on first write and trimmed to 54** before
  landing. Left as it was, a page arguing that over-packed documents get
  half-read would have been the longest unanswered page in the collection.

## What this does NOT establish

The three misses are one session's, and the sample is three. The
document-shape measurements are exact and repeatable; the causal claim that
shape produced the misread is `REASONED` from one instance, not measured across
sessions. `docs/traps.md` would take it as a candidate, not an entry.

No Codex round — per the owner's 2026-08-29 cadence correction, and consistent
with the two preceding owner-document landings today.

Capability delta: null. Owner ask: null — the three questions live in the
worksheet where he will read them next week.
