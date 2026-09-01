# 2026-09-01 — the session's own error pattern, documented as a finding and a trap

> **Status:** `complete` — the finding, TRAP-008, its route and its controls
> are pushed; fm #1005 is open and ready; the strict check ran with its real
> exit code read and its only remaining blocking finding was this card's own
> born-red hold.

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

- `python3 bootstrap.py check --strict` → **exit read after a REDIRECT, not a
  pipe** (TRAP-002). First run surfaced a **real** finding beyond the born-red
  hold: `invalid badge token 'finding'`. I had invented the token from the
  folder's name instead of reading the allowed set — **TRAP-008 committed while
  writing TRAP-008**, the seventh instance and the second inside its own
  document. Corrected to `audit` after reading what three sibling findings
  actually carry (`audit`, `audit`, `reference`). Re-run: born-red hold alone.
- **The route was proved end-to-end, not merely validated.** Immediately after
  registration it fired unprompted on this session's own `grep -c` /
  `grep -n` call, quoting TRAP-008 back at me — the `mistake → entry → route`
  lifecycle observed live rather than asserted.
- **Positive and negative controls, both required to pass:** 7 must-fire cases,
  each an actual command this session ran or a sentence it actually wrote,
  and 3 must-be-silent cases guarding the noise boundary (reading a whole file
  with `sed -n`, grepping for content rather than names, ordinary prose).
  `tools/test_doc_route_patterns.py` → 71 cases CLEAN.
- `python3 tools/check_doc_routes.py` → 72 routes · 37 docs routed · 0 errors.
- The register's summary count corrected 7→8 in the same change that made it
  stale.

## What this does NOT establish

`REASONED`, not measured: that the route will catch the *next* instance. It
fires on the listing-command and label-characterisation surfaces only; the
never-opened half belongs to `read_before_write.py` and the inherited-claim
half (instance 4) has **no** delivery at all. The coverage table states that
rather than implying full cover. Six — now seven — instances in one session is
a set of named instances, which is the register's stated bar, and not a rate.

No Codex round, per the owner's 2026-08-29 cadence correction.

Capability delta: null. Owner ask: null.
