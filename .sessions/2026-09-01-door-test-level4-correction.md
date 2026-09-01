# 2026-09-01 — the door test graded a room it never entered

> **Status:** `complete` — the regrade is pushed, fm #1004 is open and ready,
> and the strict check ran with its real exit code read; its only blocking
> finding was this card's own born-red hold.

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

- `python3 bootstrap.py check --strict` → **exit 1, read directly, not after a
  pipe**. Sole blocking finding: this card's designed born-red hold.
- **All five files under `docs/repos/spider-swing/` opened**, not listed —
  the omission that produced the false finding.
- Length claim re-measured after the edit rather than assumed: the collection's
  longest unanswered worksheet is **58**, and `owner/intent-workbooks.md` now
  says 58.
- Both generated pages `--check` current; worksheet count unchanged at 74
  (an edit, not an addition).

## The mechanism gap this exposes, stated but NOT built

A `UserPromptSubmit` doc route fired correctly and put the right README in
front of me; I did not open it. So the injection worked and the reading did
not — which is the half `docs/intent.md` § 4's injection thesis does not cover:
a route can deliver a document, and nothing observes whether it was read.

`REASONED`, `n=1`. Not proposed as a checker here: a gate that tried to enforce
reading would have to infer intent from tool calls, and a bad instrument for
this is worse than none. Recorded so the next session has the observation
rather than rediscovering it.

No Codex round, per the owner's 2026-08-29 cadence correction.

Capability delta: null. Owner ask: null.
