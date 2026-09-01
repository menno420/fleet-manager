# 2026-09-01 — correct the misread page's own overstatement

> **Status:** `complete` — the corrected page is pushed, fm #1000 is open and
> ready, and the strict check ran with its real exit code read; its only
> blocking finding was this card's own born-red hold.

- **📊 Model:** withheld · high · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_013ME1H7CPbqA1FBxJ61VPC2](https://claude.ai/code/session_013ME1H7CPbqA1FBxJ61VPC2) · "Owner-directed documents review"

💡 Session idea: a page that measures three failures and then names one cause
for all of them has committed a fourth. The table was right; the conclusion
drawn one paragraph below it was not, and nothing checks a document against
its own evidence.

## Mission

fm #999 landed `why-agents-misread-this-repo.md` claiming **"shape is the
failing axis, not location."** Its own table lists three distinct causes and
only one is shape. Correct the claim on the file the owner reads, not only in
chat — he is pausing every AI subscription for about a week and no agent will
be present to correct it there.

**Fourth PR this session** (D-0024 guideline: one main PR, extras carry a
stated reason). The reason: a landed document contains a claim already
established as wrong, on a surface he will read offline.

## Previous-session review

- fm #997 — the four workbook sections and the answer convention.
- fm #998 — three filename-level claims corrected.
- fm #999 — the misread measurement, which introduced the claim this card
  fixes. Fourth instance of the same class in one session: **a label read as
  substance.** Here the label was my own conclusion sentence.

## Shipped

- `owner/intent-workbooks/successor/why-agents-misread-this-repo.md` — the
  cause and enforceability now sit **in the table, per miss**, so the
  conclusion cannot drift from the evidence again. Trimmed 66 → 54 lines: it
  had become the longest unanswered worksheet, on a page about over-packing.

## Verification

- `python3 bootstrap.py check --strict` → **exit 1, read directly, not after a
  pipe**. Sole blocking finding: this card's designed born-red hold.
- **The index's own length claim re-tested after the edit, not assumed.** The
  corrected page came back at 66 lines, then 55, then 54; `owner/intent-workbooks.md`
  states the longest unanswered worksheet is 54, and the measured max across
  the collection is 54. Had I stopped at 55 the claim I corrected earlier today
  would have been false again within the hour.
- Both generated pages `--check` current.

## The pattern this session actually produced

Four corrections, one root: **a label read as substance.** A date read as a
citation · a table-row title read as a finished rebuild · an inherited
invariant read as true · and here, my own conclusion sentence read as what the
table under it said. The last is the instructive one, because the evidence was
three lines above the claim and still lost the argument to it.

`REASONED`, not measured: nothing in the gate compares a document's conclusion
with its own table. That is a candidate mechanism, not a finding — one session,
`n=4`.

No Codex round, per the owner's 2026-08-29 cadence correction.

Capability delta: null. Owner ask: null.
