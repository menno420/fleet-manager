# 2026-08-23 — the bundling advice would have destroyed the feature it was serving

> **Status:** `complete` — branch `claude/r5-archive-execution-4dsvoh`, cut from
> `origin/main` at `7644694` (fm #931). Flipped after
> `python3 bootstrap.py check --strict` returned a real exit 0 on this tree,
> read directly and never after a pipe.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

fm #931 recorded the Gemini Notebook constraints and, alongside them, advice on
fitting `idea-engine`'s 566 files under the 300-source ceiling: *"any bundle must
consolidate (concatenate by theme, or select)."*

**That advice is wrong, and wrong in the specific way that matters.** This
product's value is a citation resolving to a *specific* source. Concatenating
fifty idea files into one themed blob makes every citation resolve to the blob —
the grounding becomes exactly as coarse as the merge. It would have optimised
for the constraint by destroying the reason for the upload.

Caught by owner-review asking what happens to the citation mechanism. I had not
thought it through.

## previous-session review

fm #931 (`7644694`) got the product identification right *after* being corrected
once, and recorded that correction properly. It then shipped this flaw in the
same entry — a reminder that a card documenting one class of error is not
immune to a different one.

## What landed

`docs/owner-queue.md` → `OQ-GEMINI-NOTEBOOKS`, constraint 1 rewritten:

- **Partition, do not compress.** The limit is per notebook, so 566 files
  becomes **2–3 themed notebooks** under 300 each, file-to-source 1:1, citations
  exact. The fix was available the whole time; compression was reached for when
  partition was the obvious move.
- **Selection is still legitimate** — best 300 of 566 is lossy but keeps
  citations precise. Concatenation is the one option that does not.
- **The per-notebook reading is marked unconfirmed.** That 300 is per notebook
  rather than per account is read from where the number appeared — a notebook's
  own feature list — and is consistent, not verified. Whether notebook *count*
  is capped is unknown. Both flagged to confirm before building.
- **Constraint 2 is scoped down**: *"Stel aangepaste instructies in"* is read off
  the splash; that it can carry a **standing brief** is an inference from the
  feature name, not a tested behaviour, and now says so.

## The correction worth carrying

**I optimised for the stated constraint and did not check what the optimisation
cost.** 300 was the number in front of me, so the reasoning went straight to
"make 566 into 300" without asking what the sources were *for*. The general
shape, and the guard recipe: **when a limit forces a transformation, state what
property the transformation must preserve before choosing one.** Here the
property is citation granularity, and naming it makes partition obviously right
and concatenation obviously wrong.

Related but distinct from [TRAP-001](../docs/traps.md): nothing here was a stale
document. It was reasoning that never questioned its own frame.

## Verify

`python3 bootstrap.py check --strict` → **exit 0**, read directly, never after a
pipe.
