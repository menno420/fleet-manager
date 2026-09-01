# 2026-09-01 — the findings index generated, the offline bundle, two foldings

> **Status:** `complete` — all three items are pushed, fm #1006 is open and
> ready, and the strict check ran with its real exit code read; its only
> blocking finding was this card's own born-red hold.

- **📊 Model:** withheld · high · docs-only
- **⚑ Model-slot note:** this session carries an instruction against a model
  identifier in a pushed artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_013ME1H7CPbqA1FBxJ61VPC2](https://claude.ai/code/session_013ME1H7CPbqA1FBxJ61VPC2) · "Owner-directed documents review"

💡 Session idea: **the no-op control is the one that finds the bug.** The
bundle's round trip looked fine on the interesting test (an answer reaches its
worksheet) and was broken on the boring one: generate-then-split with no edits
rewrote **46 of 74** worksheets, silently normalising trailing whitespace. A
tool that reformats a week of the owner's handwriting is worse than no tool,
and only the change-nothing case exposed it.

## Mission

Three items the owner authorized in one word after each was measured and put
to him.

## Previous-session review

fm #997–#1005, this session. #1005 added TRAP-008 and its route; that route
fired on this session's own commands twice while doing this work.

## Shipped

1. **`tools/gen_findings_index.py`** + the regenerated
   `docs/findings/README.md`, + a `findings index drift` preflight lane.
   `MEASURED` before the fix: **72 files on disk, 65 rows, 7 unindexed, 0
   ghosts.** The index's own header records being *"regenerated complete on
   2026-08-10 … after the old index was measured listing 25 of 42"* — so this
   is the **second** decay in three weeks by the same mechanism.
2. **`tools/gen_workbook_bundle.py`** + `owner/intent-workbooks/ALL-IN-ONE.md`
   — all 74 worksheets in one file for phone/tablet reading during his offline
   week, and `--split` to put the answers back.
3. **Two foldings** — `products/what-you-would-build-with-more-agents.md` and
   `you/what-you-want-to-learn.md` Q1, both asking what he answered on
   2026-08-31.

## The design split that matters

**Membership is mechanical; description is authored value.** The findings
generator reconciles *which* findings are listed and never rewrites a
description — existing rows carry through byte-identical, ★ included, and a
newly-indexed file gets a placeholder built from **its own `# ` title, quoted**.
A generator that summarised files it had not read would have automated TRAP-008,
added to the register hours earlier for exactly that.

**The bundle is deliberately NOT gated.** A drift lane would red continuously
the moment he writes in it — a gate fighting its own user. It reconciles by
`--split`, not by a check. The findings index *is* gated, because its drift is
silent decay rather than intended edits.

## Two real bugs, both found by controls, both fixed

- **Round trip was not byte-exact.** `MEASURED`: 49 of 85 files in the tree do
  not end in exactly one newline; the first splitter normalised them and
  rewrote **46 worksheets on a no-op**. Body is now embedded and extracted
  verbatim.
- **The bundle counted itself.** `gen_workbook_progress.py` saw `ALL-IN-ONE.md`
  as a 75th worksheet *and* read it as answered — it contains every other
  worksheet's `OWNER` markers — inflating numerator and denominator at once.
  Added to its skip set with the measurement recorded beside it.

## A self-inflicted loss, recorded

While fixing the above I ran `git checkout -q owner/intent-workbooks` to reset
test damage, which **also reverted both foldings** made earlier in the same
working tree. Caught by re-grepping for their markers rather than assuming;
redone. A blanket checkout is not a scalpel, and this session used it as one.

## Verification

- `python3 bootstrap.py check --strict` → **exit read after a redirect, not a
  pipe**. Sole blocking finding: this card's designed born-red hold. All nine
  preflight lanes exit 0, including the new `findings index drift`.
- **No description was lost or altered**, proved rather than eyeballed: parsed
  `HEAD:docs/findings/README.md` and the new file into `{filename: (star,
  description)}` maps and asserted set equality on the 65 pre-existing rows —
  **0 lost, 0 altered, 7 added, 0 ghosts.**
- **The round trip is byte-exact**, proved by sha256 over all 74 worksheets
  before and after `generate → --split`: **74 of 74 identical.** This is the
  control that failed first and found the normalisation bug.
- **Drift check negative-controlled**: clean → 0; a ghost row appended → 1;
  restored → 0.
- **`--split` refusal negative-controlled**: an END marker deleted → refuses,
  exit 1, names the file, and the worksheet tree is untouched afterwards.
- **The bundle's self-counting bug was caught by the progress generator's own
  output** reading `3 of 75` where 74 was the truth — the denominator moved,
  which is what exposed it.

## What this does NOT establish

`REASONED`, not measured: that the owner will find one 2,932-line file easier
to work in than 74 small ones. That is the premise he stated and I built to it;
nobody has used it yet. If it reads badly on a phone the fix is the bundle's
shape, not the split mechanism, which is independently verified above.

The findings placeholders are honest placeholders, not descriptions: seven rows
now carry each file's **own quoted title** plus *"description still owed"*.
Writing real gists means reading seven findings, which is a separate job and is
not claimed here.

No Codex round, per the owner's 2026-08-29 cadence correction.

Capability delta: null. Owner ask: null.
