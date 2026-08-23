# 2026-08-23 — re-deriving the corpus sizes killed a partition plan that was never needed

> **Status:** `complete` — branch `claude/r5-archive-execution-4dsvoh`, cut from
> `origin/main` at `c6305a3` (fm #932). Flipped after
> `python3 bootstrap.py check --strict` returned a real exit 0 on this tree,
> read directly and never after a pipe.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

`continuation-prompt`'s trap list says: *"Do not carry a number you have not
re-derived."* Regenerating the handoff meant re-deriving the two corpus sizes the
Gemini-notebooks plan rests on. Both moved, and one of them invalidated advice
this session had given an hour earlier.

## previous-session review

fm #932 (`c6305a3`) fixed the concatenate-vs-partition error and was right to.
But it left *"2–3 themed notebooks"* attached loosely to both corpora, and this
pass shows that framing was only ever correct for one of them.

## What landed

`docs/owner-queue.md` → `OQ-GEMINI-NOTEBOOKS`, constraint 1, sizes measured live:

- **`curious-research` is 126 files (75 markdown)** — `guides` 49 · `projects`
  22 · `ideas` 15 · `research` 14 · `docs` 7 · `site` 6 · `arm` 2. **It fits in
  ONE notebook.** The partition advice applies to `idea-engine` only, and the
  earlier suggestion to split `curious-research` into themed notebooks was
  unnecessary work proposed against a limit it never approached.
- **`idea-engine/ideas/` reconciles at 566** — 742 blobs, 580 `.md`, minus 14
  README/index = **566**, matching OD-4's long-standing figure, with the
  remainder being 157 `.py` plus indexes. The estate's number was right; nothing
  had ever shown *why* the raw tree count disagreed.
- **It partitions on natural seams** — by consumer repo: `superbot` 249 ·
  `fleet` 221 · `venture-lab` 103 · `superbot-games` 86. Two notebooks split
  there with **no file merged**, so citation granularity survives intact.

## The correction worth carrying

**A constraint I had not measured against generated a plan for work that was not
needed.** 300 was real; 566 was real; but I applied the resulting partition
strategy to a corpus I had never sized, and `curious-research` turns out to be
under a quarter of the ceiling. The recipe: **before planning around a limit,
measure the thing against the limit** — not just the limit.

Same family as the day's other errors but a distinct mechanism: not a stale
document ([TRAP-001](../docs/traps.md)) and not an absence read from a bad query
([TRAP-003](../docs/traps.md)), but a **correct constraint applied to an unmeasured
subject**. Not registered as its own trap yet — one instance, and the register's
own bar is two or a real cost.

## Verify

`python3 bootstrap.py check --strict` → **exit 0**, read directly, never after a
pipe. Sizes from `GET /git/trees/{branch}?recursive=1` on each repo.
