# 2026-08-22 — the archive approval said "eight ungated"; it is nine

> **Status:** `complete` — branch `claude/estate-repo-dispositions-spa3i0`,
> restarted from `origin/main` at `0f13368` (#910), landed as fm **#911**.
> Flipped after `python3 bootstrap.py check --strict` returned a real exit 0 on
> this tree, read directly and never after a pipe.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

Caught while writing R5's continuation prompt, by doing the subtraction instead
of repeating the number: **12 disposition rows − 3 gated = 9 ungated.** The
just-merged approval record (#910) says **eight**, three times.

The **enumerated list was always correct** — it names nine repositories
(`superbot-games`, `superbot-idle`, `superbot-mineverse`, `trading-strategy`,
the three `codetool-lab-*`, `Substrate-kit-app`, `proxybench`). Only the count
word is wrong, which is the worse of the two failure modes: a wrong list is
obvious, a wrong tally reads as a checksum on a correct list.

**Why it had to be fixed before the prompt shipped.** This is the number the
executing session acts on, sitting in an owner-approval record. It archives nine
and reads "eight", or stops on the mismatch and asks the owner a question the
repo already answers.

The skill that caught it says so in one line — *do not carry a number you have
not re-derived* — and the number had been carried through a card, a PR body, an
owner-queue entry, an R5 row and several replies without once being recomputed.

## previous-session review

The previous card (`2026-08-22-archive-goahead-recorded.md`) committed the
go-ahead so R5 would not rest on a chat message — and shipped this miscount
inside it. The instinct was right and the arithmetic was not checked, which is
the same shape as this session's earlier miss: *the instrument was never run,
the conclusion just felt safe.*

## What landed

Five occurrences corrected — three in the owner-queue approval, one in the R5
row, one in #910's card — located by `grep -rn "eight ungated"` rather than by
recalling where I had written it. The count was re-derived mechanically from the
row set (12 total, 3 gated, 9 remaining) rather than re-read from prose.

**The nine, enumerated:** `superbot-games` · `superbot-idle` ·
`superbot-mineverse` · `trading-strategy` · `codetool-lab-sonnet5` ·
`codetool-lab-fable5` · `codetool-lab-opus4.8` · `Substrate-kit-app` ·
`proxybench`. **The three gated, unchanged:** `superbot-next` +
`superbot-plugin-hello` (GCB-1), `product-forge` (R2).

## The guard recipe

A count and the list it counts are two claims, and only one of them gets read
carefully. Cheap check, and it is machine-decidable: **anywhere a document
states a tally beside an enumeration, the tally must be derivable from the
enumeration.** `scripts/check_estate_index.py` already walks the same twelve
names and would be the natural home — flagged here rather than built, because
the correction was the urgent half and a new checker is a separate change.

## Verify

`python3 bootstrap.py check --strict` → **exit 0**, read directly. Before the
flip it returned 1 on the designed born-red hold alone.
