# 2026-08-23 — The 8,000 figure is point-in-time, and it already moved

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

The owner's stand-in review challenged the headline PR figure: *"8,000 is an
extremely round number for an organic count — what exact command produced this,
and did you verify whether you hit a hard API or pagination limit?"*

**Both halves answered by measurement, and the second answer is the interesting
one.**

**Not a ceiling.** The figure is the sum of 26 per-repository counts, each read
from `GET /pulls?state=all&per_page=1`'s `Link` header `rel="last"`. There is no
shared query for a global limit to bite. `superbot` alone returns **2,378**,
cross-checked two ways — `per_page=1` → page 2378, and `per_page=100` → 24 pages
with **78** items on page 24 (23×100+78 = 2378). 2,378 **exceeds 1,000**, which
rules out the Search API's 1,000-result cap, the ceiling that would most
plausibly fake a round total. No repository sits at 100, 500, 1,000 or 5,000.
The round number is a coincidence; the tail addends are 21 + 17 + 4.

**But it is already stale.** Re-running the same recipe at 10:2xZ returns
**8,002** — this session's own two pull requests (websites #512, fm #919) moved
it. The pack states `8,000` in five places with **no per-figure timestamp**.

**Why that is worth a PR for a difference of two:** the pack's entire credibility
rests on *"every figure carries the command that produced it"*. A recipient who
runs the command and gets a different number than the document states, with no
explanation offered, has found a document that fails its own promise — and this
one is going to a third party. The fix is not to chase the value (it drifts
again within the hour) but to **stamp it and say it moves**.

## Previous-session review

⟲ fm **#919** (`e2fe0bb`) — the evidence pack, merged. Checked at `main`: the pack
is present at 281 lines, the creation-date partition reads 19 / 17 / 19 across
three unambiguous rows, and re-running its published recipe reproduces
`26 / 19 / 17 / 19`. Also merged: websites **#512** (`478cb13`), verified live —
7 of 7 pages now state the program ended, 10/10 defect checks clear.

## What is about to happen

Stamp the PR totals as point-in-time in the pack, at every site that states them,
plus the honest-nulls section. No other figure changes.

## Verify

(filled before the flip — real exit codes, never after a pipe: TRAP-002)
