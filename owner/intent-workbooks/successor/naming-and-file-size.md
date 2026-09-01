# Your naming rule — and the two conditions on it

> Your words, live 2026-09-01: *"more folders and shorter but more specific
> files… the filename tells you exactly what the file contains… the folder name
> should tell you exactly which types of files are there… whenever an agent
> opens a file, it reads it whole."* Shape clarified same day: **nested**, not
> sibling — `superbot/goals/{completed,in-progress,planned}` ·
> `superbot/problems/{cogs,API,railway}`.

## Why the rule is right

`MEASURED`: against this session's three misses your scheme catches **two**; my
counter-proposal, a line-length lint, caught **one**.

`DERIVED`: *"reads it whole"* cannot be an instruction — `docs/intent.md` § 4
is explicit that instructions do not bind and mechanisms do. **Your rule
carries its own mechanism: a 30-line file is read whole because it is 30
lines.** Length is the enforcement; the sentence about reading is decoration.

## Condition 1 — state in the path needs a command

`MEASURED`: `docs/owner-comments/<repo>/{unconsumed,consumed}/` is your scheme
running today. `tools/owner_comments.py consume` moves the file, writes `state`
inside it too, and reindexes — one diff — and `tools/owner_comments.py check`
is a preflight lane, so a file whose folder and contents disagree **reds the
build**. Copy that, not the folder names. Left to agent discipline, a goal that
finishes and is not moved is wrong twice: wrong path *and* wrong state.

## Condition 2 — closed sets in the path, open sets need an index

`DERIVED`: your two examples differ. `{completed,in-progress,planned}` is
**closed** — an agent guesses the path correctly forever.
`{cogs,API,railway}` is **open**: the next subsystem invents a folder nobody
can guess, and guessing is the whole point.

## The measurement that redirects the effort

`MEASURED`: **the folder-per-topic scheme already exists.** `docs/repos/<name>/`
was adopted 2026-08-08 with fixed filenames. **10 of 28** repositories have a
folder; **3 of 10** have anything beyond `README.md`; **1 of 10**
(`spider-swing`) has the full set. It was designed, adopted, and never
populated. A rebuild that re-designs it spends effort on the half that worked.

## Questions for you

1. Which category sets are closed for good, and which will keep growing?
2. What line count should force a split?
3. Which folders must exist in *every* topic, no exceptions?
4. `docs/repos/` was adopted and left empty. What would make the new one fill?

## Your words

`OWNER`:
