# 2026-08-23 — the second corpus: idea-engine in 3 notebooks, and a number corrected twice

> **Status:** `complete` — branch `claude/gemini-notebook-corpus-f7sa69`, restarted
> from `origin/main` at `0f41be4` (fm #935) because the branch's previous PR
> (#934) was already merged. Born red on purpose: the card is the merge hold
> (TRAP-006), and it held while `@codex` answered. Flipped only after
> `python3 bootstrap.py check --strict` returned a real exit 0 on this tree,
> read directly and never after a pipe.

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
- **62 regression assertions**, exit 0 — 49 inherited plus 13 written here
  for the three features this PR adds, which had no coverage at all.
- Both bundles rebuilt after the validation change: **byte-identical to their
  published assets**.

## `@codex` on this PR — it did not review, it tried to *fix*

**It answered ~22 minutes after open (past the measured ~335 s) and with a
different shape than every round on fm #934: not findings, but a summary of code
it had written and committed as `d62f80d`** — including an edit to *this card*
raising the assertion count to "58".

**None of it landed, and its own summary says why:** *"A pull request could not
be created because this environment exposes neither a `make_pr` tool nor a
configured Git remote/PR CLI."* Verified rather than assumed —
`git cat-file -t d62f80d` returns **`fatal: Not a valid object name`** and
`git branch -a --contains` matches **0** branches. The work is stranded in its
sandbox. **So its "58 passing assertions" is a claim about a tree that does not
exist here, and its card edit never happened.** Treated as a suggestion, which is
all it could be.

**The suggestion was right, and the gap was mine.** This PR adds **three**
features — `--group-depth`, prefix exclusions, first-fit-decreasing packing — and
shipped them with **zero** regressions. Measured: `grep -c` over the test file
returned **0** for `group_depth`, `group_key`, `first-fit`, `exclude_prefix` and
`backfill`. The card's boast that "49 regression assertions still pass" was true
and covered only the code from the *previous* PR. A suite that grows only when a
reviewer finds a bug is a suite that never covers new work.

Its `--group-depth` point was real too, and probing showed it was worse than
"unvalidated": `group_key(path, 0)` returned `''` — one silent mega-group — and
`group_key(path, -1)` returned `'ideas/superbot'`, coincidentally *identical to
depth 2*. Both wrong quietly. Now `ValueError` at the helper and `SystemExit` at
the CLI.

**Written and counted here: 13 new assertions → 62 total, exit 0.** Not 58 —
that figure belongs to Codex's tree, and copying a number from a summary I cannot
run is the exact move this session already got burned by.

## The lesson, stated so it is not re-learned

**An inference that explains a real finding is still an inference.** Codex found
a true inconsistency; I supplied a mechanism for it without measuring, and the
mechanism went into two documents in the same commit that praised the catch.
Measuring cost one API call. `docs/traps.md` **TRAP-001** already covers this —
*"never launder a citation into a measurement"* — and this is the same failure
with an inference in place of a citation.

**And the same shape appeared twice more in one session.** A bot summary reported
"58 passing assertions" for a commit that does not exist in this repository;
copying that number would have put an unrunnable claim into the permanent record.
The defence is identical each time and costs one command: `git cat-file -t`.
**A count is only worth what the run that produced it is worth.**

**A third instance, and it is the structural one:** a regression suite that grows
only in response to review findings will always lag the features shipped between
reviews. Three features landed here with zero coverage, and nothing in the gate
noticed — the gate checks card grammar and prose, not whether new code is
tested.
