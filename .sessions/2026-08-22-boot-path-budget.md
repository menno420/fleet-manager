# 2026-08-22 — OD-17's other half: the boot path was 7000/7000 and 70% merge log

> **Status:** `complete` — branch `claude/estate-repo-dispositions-spa3i0`,
> rebased onto `origin/main` at `88ddb63` (#908), landed as fm **#909**.
> Flipped after `python3 bootstrap.py check --strict` returned a real exit 0 on
> this tree, read directly and never after a pipe.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

OD-17 is two nouns: *"cleaning up excessive **repos and documentation** where
possible while still making it easy for an agent to understand work."* fm #906
answered the repos. This answers the documentation, at the place where the
directive's own constraint is measurably failing.

`MEASURED` at HEAD: the boot read set is **7000 of 7000 words — zero headroom**,
and the kit's own advisory says so
(`[orientation-headroom] _total: boot-read set at 7000/7000 words — 0 words of
headroom (>=95% of budget; trim before the cliff)`). Two prior sessions routed
around it rather than fixing it.

**The cause is one section.** `current-state.md` is 6,212 of those 7,000 words,
and `## Recently shipped (newest first)` alone is **4,383** — 70% of the file, a
chronological log of 45 merged-work entries reaching back to the first roster
generations. That contradicts the file's own stated contract, which is in its
header: it *"carries **live hub state**, not the program history."*

So this is not a judgement call about what to cut. It is moving RECORD-tier
material off a CORE-tier read path — OD-17's own instrument, `MAP.md`'s tiers —
and the file already says that material does not belong here.

**Nothing is deleted.** Everything moves to a dated archive beside it.

## previous-session review

The previous card (`2026-08-22-pre-archive-writes-baton.md`) executed the first
pre-archive write and withdrew a recommendation that had outrun its evidence.
Its guard recipe — *when a claim turns on "X cannot affect Y", check the thing
that decides it, not the artifact's presence* — applies here directly: before
moving the section I checked what actually depends on it rather than assuming a
merge log is inert.

## What landed

**Boot set 7000/7000 → 1995/7000, headroom 5005**, and the kit's
`orientation-headroom` advisory stopped firing (positive control: the same
command printed it before the cut).

Moved to [`current-state-shipped-log.md`](../docs/current-state-shipped-log.md),
badged `historical`, `MAP.md` row RECORD: the merge log's older 37 entries
(4,062 w), the seat-era block the file already badged *preserved, not current*
(807 w), the two *superseded* subsections (482 w), the archive-day link list
(38 w). **Nothing deleted** — 6,212 words of old content in, 853 retained,
5,389 moved, +30 residual pointer text.

## The acceptance test, run for real

The bar is a cold session stating purpose, live state and next step from ≤3
files — OD-17's own constraint, and the thing a word-count cut can silently
break. Run **controlled**: identical four questions to a fresh reader twice,
differing in exactly one file (`current-state.md` at `origin/main` vs trimmed).
**Both arms correct on 1–3; both `GAPS: NONE`.** Evidence + both verbatim
transcripts:
[`findings/2026-08-22-boot-trim-cold-read.md`](../docs/findings/2026-08-22-boot-trim-cold-read.md).

The control earned its place: the BEFORE arm named `RESUME.md` off-limits and
AFTER did not. Traced before reacting — its only pre-trim occurrence was
*inside a shipped-log entry*, never the live "do not use" line, so the trim
dropped an incidental mention, not a pointer. Added to the live line anyway.

**Named, not hidden:** the producer was fresh, **the scorer was me** — the
§ 4.8 bias, with little room on 1–3 (single named facts) and the most room on
reading `GAPS: NONE` as a pass.

## Adversarial review — Codex round 1: 3 findings, 3 [conceded]

1. **`6,212 → 853` stated retained old content as the final file size.** I
   measured before adding the trim notice and pointers. Corrected in four
   places with the instrument named — 853 retained; the file measures **1,207**
   on the kit's instrument (what the budget gates), **1,167** by `wc -w`. The
   two disagree; my arithmetic used one and the review used the other, and
   neither was wrong about its own measure.
2. **The shipped list was not the newest work** — and this is the finding worth
   carrying. Four 2026-08-22 rows sat in the program's §7 ledger and had never
   reached this file, **two recorded as omitted because the boot set was at
   7000/7000**. Creating headroom and leaving them out would have preserved the
   exact gap the trim existed to fix, under a fresh completeness claim.
   Backfilled (#906, #907, R3, the websites verification half), ~330 words —
   the right thing to spend new headroom on.
3. **The relocated marker's positional wording stopped resolving** once the
   block moved (shipped log is *above* it here; live state is in another file).
   Rewritten for the archive, naming `current-state.md`, original wording kept
   visible.

**The lesson under finding 2:** the cold-read test passed on a file that was
*stale*, because a fresh reader cannot miss what was never there. A cut and a
backfill are one job, not two — headroom created and not spent is the same gap
with better numbers.

## Verify

`python3 bootstrap.py check --strict` → **exit 0**, read directly. Before the
flip it returned 1 on the designed born-red hold alone, confirmed from the CI
job log rather than inferred.
