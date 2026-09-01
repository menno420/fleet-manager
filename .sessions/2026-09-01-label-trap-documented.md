# 2026-09-01 — the session's own error pattern, documented as a finding and a trap

> **Status:** `in-progress` — born red; flips last.

- **📊 Model:** withheld · high · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_013ME1H7CPbqA1FBxJ61VPC2](https://claude.ai/code/session_013ME1H7CPbqA1FBxJ61VPC2) · "Owner-directed documents review"

💡 Session idea: **the register's own bar was met and I had talked myself out
of it.** Three times today I called this pattern "a candidate, not an entry,
n=6 in one session is not a rate." `docs/traps.md` states the bar plainly —
*"at least twice, or once with a real cost, and you can name the instances"* —
and I never re-read it before declining. Declining to record something is a
claim about a threshold, and it needs its source read like any other.

## Mission

Owner, live: *"Make sure your findings are properly documented."*

Today's measurements existed only in eight session cards (per-session records)
and owner-facing workbook pages (questions for him). Neither is the estate's
home for a dated measurement. `docs/findings/` is, and nothing was there.

## Previous-session review

fm #997–#1004, this session. The through-line is the subject of this card: six
errors, one shape — a label read as its contents. #1004 is the sharpest, a
regrade of a level graded from `ls` output, committed inside the document
written to describe the pattern.

## Shipped

- `docs/findings/2026-09-01-label-read-as-substance.md` — the dated finding:
  six instances located, the document-shape numbers, the two censuses, and an
  explicit "what this does not establish".
- `docs/findings/README.md` — index row.
- `docs/traps.md` **TRAP-008 · A label read as its contents** — TRIGGER / WHY /
  REQUIRED PREVENTION / VERIFY / ORIGIN (six named, dated instances) / ROUTE,
  plus its coverage-table row.
- `.claude/hooks/doc-routes.json` — route `listing-is-not-reading`
  (Bash/Edit/Write, `repeat: true`).
- `tools/test_doc_route_patterns.py` — 7 must-fire + 3 must-be-silent cases.
- `docs/traps.md` — the register's own summary count, "seven entries, six
  delivered", corrected to eight/seven. **It was stale the moment TRAP-008 was
  inserted above it, and I did not re-read it** — TRAP-008 instance 4's exact
  class, committed inside TRAP-008's own PR and fixed in the same change.

## Why a trap and not just a finding

`docs/traps.md` is explicit: *"An entry without a route is unfinished work, not
a record"*, and the lifecycle is mistake → trap entry → route → checker. A
finding alone would have been the thing
[`findings/2026-08-08-why-rules-dont-bind.md`](../docs/findings/2026-08-08-why-rules-dont-bind.md)
measured as catching 0 of 16 incidents.

## Coverage, split honestly

The route reaches the **sub-file** half — instances 1, 3, 6, where the thing
was located and then under-read. Instances 2 and 5 are the **never-opened**
half, already `.claude/hooks/read_before_write.py`'s job. Instance 4 — an
inherited sentence restated without testing it — is **undelivered**, and the
register's coverage table says so rather than implying full cover.

## Verification

(filled at close)
