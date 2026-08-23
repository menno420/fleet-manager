# 2026-08-23 — The card-census recipe prints rows but never sums them

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

Codex raised this on fm #919 and I filed it "accepted open" while landing. That
was the wrong call, and **fm #920 is why**: that PR's whole argument is that the
evidence pack's credibility rests on *"every figure carries the command that
produced it."* Leaving a recipe that cannot emit its own headline figure
contradicts the PR I had just merged.

**MEASURED against `origin/main`:** the session-card census block ends in
`echo "$r $n"` inside the loop. It prints one `repo count` row per repository and
**never sums them, nor counts the non-zero repositories** — so running it verbatim
produces neither **4,551** nor **19 of 26**. Both are stated in the prose directly
beneath it as though the block derived them.

A recipient of this pack — the vendor — running the published command and getting
26 unlabelled rows instead of the two figures they were told it produces is
exactly the failure mode the pack claims to have designed out.

## Previous-session review

⟲ fm **#920** (`6376999`), fm **#919** (`e2fe0bb`), websites **#512** (`478cb13`)
— all merged. Checked at `main`: the pack carries the point-in-time stamp on the
PR total, the creation-date partition reads 19 / 17 / 19 across three rows and its
recipe reproduces `26 / 19 / 17 / 19`. The live review site is verified at
7 of 7 pages stating the program concluded. Nothing to repair; this card closes
one item those three left open.

**Carried lesson, and it bit twice today:** fm #915 and fm #920 both merged in
under a minute with **zero reviews** because the card was flipped to `complete`
before the branch was pushed — TRAP-006, which I registered this morning. This
card is committed and pushed **red, as its own commit, before any content work**,
which is the discipline the trap exists to enforce.

## What is about to happen

Add the aggregation to the published block so it emits both figures, and verify by
running the committed version verbatim.

## Verify

(filled before the flip — real exit codes, never after a pipe: TRAP-002)
