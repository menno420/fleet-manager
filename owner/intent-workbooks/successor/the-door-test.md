# The door test

> Your analogy, live 2026-09-01: *"you are standing in a room with a few named
> doors… you can't see past the doors unless you walk through them… if you
> could only see the named doors with no other guideline, you should be able to
> find your way to the room that holds the information you seek."*

`PROPOSED`: make it the successor's acceptance test, not a metaphor. Pick a
question, walk from the root using **only folder names**, and count. A door you
open and back out of is a defect at that level, not a mistake by the walker.

## First run — "what is the current work on spider-swing?"

`MEASURED` 2026-09-01 against this repo, four doors:

| Level | Seen | Defect |
|---|---|---|
| root | 10 doors | **3 dead rooms with live names** — `control/`, `projects/`, `telemetry/` are seat-era history |
| `docs/` | 15 doors **+ 64 loose files** | the floor must be checked before the doors can be trusted |
| `docs/repos/` | 10 repo doors | none |
| `repos/spider-swing/` | 5 files named by *type* | you must open one to learn which |

## Level 4 was graded wrong, and how is the point

I first wrote *"no door says current — it is buried inside `records.md`"* —
from the `ls` output, **without opening anything**. `README.md` carries a
section titled *"Where it stands right now"* and answers in its first
paragraph. **I ran a door test and never opened a door.** Graded the room from
the corridor, which is the one move the analogy exists to forbid.

`DERIVED`, the real and much weaker defect: the answer is behind `README.md`
and nothing on the *outside* of those five names says so — a reader must know
the convention. `goals/current` puts it in the door name. A genuine
improvement, smaller than the false version claimed.

## The amendment — it binds agents *harder*

`DERIVED`: you wrote it would differ for an agent *"since you can probably see
the whole structure at once."* Listing gives me **door names only**, as it does
you — and the error above is the proof. **You open a wrong door, see an
unfamiliar room and back out. I grade the room from the corridor.**

## What the analogy cannot express

`DERIVED`: doors make a tree; some things belong in two rooms. The Play Store
testing floor is a `problems/` fact *and* a `goals/current` fact. A strict tree
picks one and the other is empty. The estate's answer: **one home, the other
room gets a signpost** — `docs/intent.md` § 1.

## Questions for you

1. May a room hold both doors and loose files, or is that always wrong?
2. When something belongs in two rooms, who decides the real home?
3. What question should the door test use as its standard walk?

## Your words

`OWNER`:
