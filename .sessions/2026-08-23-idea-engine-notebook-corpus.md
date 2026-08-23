# 2026-08-23 — the second corpus: idea-engine in 3 notebooks, and a number corrected twice

> **Status:** `in-progress` — branch `claude/gemini-notebook-corpus-f7sa69`, restarted
> from `origin/main` at `0f41be4` (fm #935) because the branch's previous PR
> (#934) was already merged. Born red on purpose: the card is the merge hold
> (TRAP-006). Flips only after `python3 bootstrap.py check --strict` returns a
> real exit 0 on this tree, read directly and never after a pipe.

- **📊 Model:** opus-5 · high · feature build

## 💡 Session idea

fm #934 shipped the `curious-research` notebook and left one thing flagged: the
`idea-engine` seam counts, which `@codex` showed could not describe a partition
(249 + 221 + 103 + 86 = **659** against a **566**-file corpus). That flag was the
blocker on the second notebook, and resolving it is agent work, so this session
measured instead of leaving an `UNVERIFIED` marker in the records.

## previous-session review

fm #934's correction was **half right and half wrong, and the wrong half was
mine.** Codex was right that 659 and 566 cannot describe the same set. I then
inferred *why* — "overlapping consumer references" — and wrote that inference
into two documents as though it were the finding. **It was not measured, and it
is false.**

## What the measurement shows

`GET /repos/menno420/idea-engine/git/trees/main?recursive=1` — 1,373 blobs, not
truncated. Grouping `ideas/` by its second path component:

| consumer dir | recorded | measured, ALL files | measured, `.md` |
|---|---|---|---|
| `ideas/superbot` | 249 | **249** ✓ | 248 |
| `ideas/fleet` | 221 | **221** ✓ | 135 |
| `ideas/venture-lab` | 103 | **103** ✓ | 67 |
| `ideas/superbot-games` | 86 | **86** ✓ | 50 |

**All four match exactly on all-files.** The recorded seams were never
overlapping — they are **exclusive directory counts**, and every path lives in
exactly one of them by construction. The mismatch was a **denominator error**:
`566` counts `.md` minus 14 README/index files, while `659` counts *all* files
(including 157 `.py`) in only the four largest of fourteen consumer dirs. 659 ⊂
742 total under `ideas/`, leaving 83 in the other ten. Both numbers were right;
pairing them was not.

**So the seams are usable, and the estate's original plan was sound.** What was
wrong was one sentence of my own inference layered on top of it.

## What landed

- **`--group-depth`** on the builder. `idea-engine` keeps everything under a
  single `ideas/` directory, so the default depth-1 seam sees **one 742-file
  group** and cuts it alphabetically — the exact arbitrary split the seam exists
  to prevent. Depth 2 gives `ideas/superbot`, `ideas/fleet`, … Set per corpus.
- **Prefix exclusions**, decided *before* the file is read: `.sessions/` alone is
  504 session cards, and converting them only to discard them wasted the work and
  bloated `excluded/`.
- **First-fit-decreasing packing across all open notebooks.** Packing only
  forward produced **4** notebooks, the last holding 12 files while the first had
  50 free slots. Largest-first with backfill gives **3**, every seam whole.
- **The `idea-engine` bundle, published**: 779 sources + 3 indexes = **782**
  across 3 notebooks (300 / 292 / 190).

## Verification

- Against the live tree: **779 expected, 779 written, 0 missing, 0 unexpected.**
- **612 `.md` byte-identical**, 0 differing, 0 missing.
- No consumer dir split: `superbot` 249 entirely in #1, `fleet` 221 entirely in #2.
- 594 held back = `.sessions` 504 + `.substrate` 50 + `control` 30 + `scripts` 6
  + `.github` 2 + `.claude` 2. Sums exactly.
- `curious-research` rebuilt after every change and **byte-identical to the
  published asset** — the new options changed nothing for it.
- Release asset re-downloaded: sha256 `c6a6b940…` identical both sides, `testzip` OK.
- 49 regression assertions still pass, exit 0.

## The lesson, stated so it is not re-learned

**An inference that explains a real finding is still an inference.** Codex found
a true inconsistency; I supplied a mechanism for it without measuring, and the
mechanism went into two documents in the same commit that praised the catch.
Measuring cost one API call. `docs/traps.md` **TRAP-001** already covers this —
*"never launder a citation into a measurement"* — and this is the same failure
with an inference in place of a citation.
