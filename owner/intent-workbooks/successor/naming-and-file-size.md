# Your naming rule — and the measurement that changes where it applies

> Your words, live 2026-09-01: *"create more folders and shorter but more
> specific files… the filename tells you exactly what the file contains. And
> the folder name should tell you exactly which types of files are there. And I
> want to make sure that whenever an agent opens a file, it reads it whole."*

## Why the rule is right

`MEASURED` 2026-09-01, this session's three misses: your scheme catches **two**
of three. A short `successor-name.md` gets opened where a 634-line planning doc
did not (miss 1); a one-claim file cannot hide a reversing qualifier 400
characters into a table cell (miss 2). My own proposal — a line-length lint —
caught one.

`DERIVED`: *"reads it whole"* cannot be an instruction. `docs/intent.md` § 4 is
explicit that instructions do not bind and mechanisms do. **But your rule
already contains its own mechanism: a 30-line file is read whole because it is
30 lines.** Length is the enforcement; the sentence about reading is not.

## The measurement that redirects the effort

`MEASURED` 2026-09-01: **this structure already exists.** `docs/repos/<name>/`
was adopted 2026-08-08 with fixed filenames — `README.md`, `intent.md`,
`capabilities.md`, `records.md`, `working-here.md`.

- **10 of 28** repositories have a folder at all.
- **3 of 10** have anything beyond `README.md`.
- **1 of 10** (`spider-swing`) has the full set.

`DERIVED`: the scheme is not missing. **It was designed, adopted, and never
populated.** A rebuild that re-designs it spends its effort on the half that
already worked.

## One refinement worth arguing about

`PROPOSED`: your sketch reads as sibling folders — `/superbot`,
`/superbot-goals`, `/superbot-problems`. Prefer **one folder per repository
with the same filenames inside every one**: `superbot/goals.md`,
`superbot/problems.md`, `spider-swing/goals.md`. Both halves of your rule still
hold, and an agent learns the vocabulary **once** instead of 28 times.

## Questions for you

1. Sibling folders, or one folder per repo with fixed filenames inside?
2. What is the line count at which you would want a file split?
3. Which files do you want in *every* repo folder, no exceptions?
4. `docs/repos/` was adopted and left empty. What would make the new one fill?

## Your words

`OWNER`:
