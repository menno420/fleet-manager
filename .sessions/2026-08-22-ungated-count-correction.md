# 2026-08-22 — the archive approval said "eight ungated"; it is nine

> **Status:** `in-progress` — branch `claude/estate-repo-dispositions-spa3i0`,
> restarted from `origin/main` at `0f13368` (#910). Flips to `complete` after
> `python3 bootstrap.py check --strict` returns a real exit 0.

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

## What this will carry when it flips

- every occurrence corrected, found by grep rather than by memory
- the count re-derived mechanically, not re-read
