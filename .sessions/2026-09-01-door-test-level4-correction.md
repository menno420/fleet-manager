# 2026-09-01 — the door test graded a room it never entered

> **Status:** `in-progress` — born red; flips last.

- **📊 Model:** withheld · high · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_013ME1H7CPbqA1FBxJ61VPC2](https://claude.ai/code/session_013ME1H7CPbqA1FBxJ61VPC2) · "Owner-directed documents review"

💡 Session idea: **the instrument committed the defect it was built to
measure.** A test about opening doors was run by reading `ls` output. Any
instrument that can be run without touching what it measures will be, and
nothing in this estate's gate distinguishes a walked tree from a listed one.

## Mission

fm #1003 landed `the-door-test.md` with a false level-4 finding: *"no door says
current — it is buried inside `records.md`."* Both halves were asserted from
the `ls` output. `docs/repos/spider-swing/README.md` carries a section titled
*"Where it stands right now"* and answers the question in its first paragraph;
`records.md` was never opened at all.

A `UserPromptSubmit` route had put that exact README in front of me at the top
of the turn — *"You named spider-swing. Read docs/repos/spider-swing/README.md
BEFORE attaching the repo"* — and I walked past it. The mechanism fired
correctly; the reader did not act on it.

## Previous-session review

fm #997–#1003 this session. The class is now seven for seven: **a label read as
substance.** This instance is the sharpest, because the artifact making the
claim was itself the anti-label instrument.

## Shipped

- `owner/intent-workbooks/successor/the-door-test.md` — level 4 regraded from
  *"no door says current"* (false) to *"you must open one to learn which"*
  (true, and much weaker). The misgrading is kept **in** the page as its
  worked example rather than quietly repaired.
- `owner/intent-workbooks.md` — measured longest-unanswered worksheet 54 → 58.

## What was actually opened this time

All five files in `docs/repos/spider-swing/`. Their first `##` headings:
`README.md` → *"The one-paragraph answer"* then *"Where it stands right now"* ·
`capabilities.md` → *"The short version"* · `intent.md` → *"Why it exists"* ·
`records.md` → *"Findings — the durable research"* · `working-here.md` →
*"The gates"*. Two files answer the current-work question: `README.md` and
`intent.md`.

## The length claim, handled the other way

The corrected page came to 58 lines against an index claiming 54. Earlier today
the same collision was resolved by trimming; this time the **claim** moved,
because it is a measurement and not a rule — and trimming a page three times to
protect a number is how a measurement quietly becomes a fiction.

## Verification

(filled at close)
