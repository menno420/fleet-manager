# 2026-08-29 — the borrowed denominator, corrected in both copies

> **Status:** `complete` — *"one lane of five"* is corrected to *"one lane of
> ten"* in both places on `main`. The numerator was right and measured; the
> denominator was quoted from a neighbouring PR and never checked.
> **No review was requested, and the reason is stated below**, so there is no
> outstanding verdict for the flip to outrun (TRAP-007).

- **📊 Model:** withheld · max · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container

## Mission

[fm #977](https://github.com/menno420/fleet-manager/pull/977) merged carrying a
number this session had not measured, and [fm #976](https://github.com/menno420/fleet-manager/pull/976)
had merged carrying the same one. Both say the model-withholding restriction was
live *"for one lane of five"* on 2026-07-09.

**One lane is right. Five is not a number in that document.**

## Measured

`docs/findings/retro-synthesis-2026-07-09.md`, read rather than grepped:

| question | answer |
|---|---|
| how many lanes does the doc cover? | its title is **"all 10 lanes"** |
| how many rows in the model table? | **9** — `superbot-next`, `substrate-kit`, `websites`, `trading-strategy`, the three `codetool-lab-*`, and the two `superbot-games` lanes |
| how many withheld their own build model? | **1** — the doc calls `codetool-lab-fable5` *"the only lane that deliberately does not name its model in-doc"* |
| any other withholding? | **yes, one more row** — `codetool-lab-opus4.8` records a *successor's* model *"withheld per policy"*, which is a different thing from the lane withholding its own |

So: **one of ten**, with a second row carrying a related-but-distinct case. Five
appears nowhere.

## How it got in

fm #977's session verified the *quote* — *"Withheld from repo artifacts per
harness policy"* — against the source document, correctly, and in the same
sentence carried over *"for one lane of five"* from fm #976 without checking it.
**The verified half and the borrowed half travelled together in one clause**,
and the borrowed half inherited the credibility of the checked one.

That is this estate's TRAP-004 in its least visible form. The count-only shape
the register warns about (*"X cards", "Y commits"* with no ratio) is easy to
spot; a ratio quoted from a sibling document, adjacent to a citation that *is*
sound, is not. Nothing in the sentence looked unmeasured.

**It is also TRAP-008 by construction:** the error existed in two files before
this session touched anything, because fm #976 and fm #977 landed within
40 minutes of each other and the second quoted the first.

## Why no review was requested

The change is one phrase in two files, and every figure behind it is readable
by `grep` against a single document in the same tree — the title line, a table
row count, and one quoted sentence. fm #969 set the precedent for declining a
review on exactly this shape (a two-integer documentation correction) with the
reason written down.

**The stronger argument is that a review already failed to catch this.** Codex
reviewed fm #977 twice — 7 findings, all conceded — and *"one lane of five"* sat
in the diff of the second round, in a paragraph it was actively reading, and did
not surface. That is not a criticism of the reviewer: a ratio citing a real
document, beside a quote that checks out, is not what an adversarial reader is
scanning for. It does mean a third round has no particular claim on catching it.

**If that reasoning is wrong, this is the change to point at** — one phrase,
two files, trivially reversible.

## Verify

- `python3 bootstrap.py check --strict` → real exit code, read directly, no pipe.
- Lane counts from the document's own title line and its model table, counted
  with `grep -c "^| [a-z]"` over the table range and the row names printed in
  full — not from a sibling document's summary of it.
- Post-edit copy check, and **stated so it can actually reproduce**: the phrase
  survives only inside this card, which quotes it four times in order to correct
  it. The check that discriminates is therefore
  `grep -rln "one lane of five" --include=*.md . | grep -v lane-denominator-fix`
  → **no files**. The first draft of this line claimed a bare `grep -rn` returns
  nothing, which its own text falsified — the identical defect Codex raised as
  a P3 on fm #977, committed again one PR later by the session recording it.

## Layer-2 handoff

Layer-2 handoff: null (no repo attached; fleet-manager itself)

## ⟲ Previous-session review

Previous card:
[`2026-08-29-codex-trigger-and-model-slot.md`](2026-08-29-codex-trigger-and-model-slot.md)
(fm #977, merged).

**Held up on everything it measured, and this card fixes the one thing it
didn't.** Seven Codex findings across two rounds, all conceded, 5 → 2 and
converging; it reversed its own "review-wave convention" reading against the
July source when fm #976 landed mid-review, which is the behaviour the estate
wants. Its resolution of the `guard-fires.jsonl` conflict asserted every
property it claimed — union, no dropped base records, no duplicates, every line
re-parsed — instead of eyeballing a merge.

**What it got wrong is narrow and instructive:** in the very paragraph where it
corrected a wrong claim against source, it imported an unverified denominator
from the PR that had corrected it. **Verifying a quote is not verifying the
sentence containing it.**

## 💡 Session idea

**Both live copies of this error were created within 40 minutes, by two sessions
that never saw each other's text.** fm #976 wrote it; fm #977 quoted it while
reconciling against fm #976; neither could have caught it by reading its own
diff, because the phrase was correct-looking prose citing a real document.

The generalisable part is not "check your numbers" — the estate has that rule
and it did not fire. It is that **a claim crossing a PR boundary loses its
provenance**: fm #977 knew it had verified the quote and did not track that the
adjacent ratio came from somewhere else. A convention that marks borrowed
figures inline — a bare `[fm #976]` after any number taken from another
document — would have made the unchecked half visible to the session writing it.

**Why an idea and not an action:** it is a writing convention, not a mechanism,
and OD-24 §3 keeps an agent from introducing one on its own initiative. It also
wants testing against the corpus first — how many dated figures in this repo
would need such a marker, and does adding it change whether anyone checks them.
