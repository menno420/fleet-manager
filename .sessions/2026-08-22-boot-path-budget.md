# 2026-08-22 — OD-17's other half: the boot path was 7000/7000 and 70% merge log

> **Status:** `in-progress` — branch `claude/estate-repo-dispositions-spa3i0`,
> rebased onto `origin/main` at `88ddb63` (#908). Flips to `complete` after
> `python3 bootstrap.py check --strict` returns a real exit 0 on this tree.

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

## What this will carry when it flips

- what moved, what stayed, and the word conservation proving nothing was lost
- the before/after headroom, read from the gate rather than counted by hand
- the cold-read test result on the trimmed file
