# The door test

> Your analogy, live 2026-09-01: *"you are standing in a room with a few named
> doors… you can't see past the doors unless you walk through them, so you must
> make the right choice… if you could only see the named doors with no other
> guideline, you should be able to find your way to the room that holds the
> information you seek."*

## The analogy is right, and it is a test, not a metaphor

`PROPOSED`: make it the acceptance test for the successor. Pick a question,
walk from the root using **only folder names**, and count. Any door you open
and back out of is a design defect at that level, not a mistake by the walker.

## First run — "what is the current work on spider-swing?"

`MEASURED` 2026-09-01 against this repo. Four doors: root → `docs/` →
`repos/` → `spider-swing/`. Three defects, one per level:

| Level | What you see | Defect |
|---|---|---|
| root | 10 doors | **3 are dead rooms with live names** — `control/`, `projects/`, `telemetry/` are seat-era history |
| `docs/` | 15 doors **+ 64 loose files** | you must check the floor before you can trust the doors |
| `repos/spider-swing/` | 5 files, named by *type* | **no door says "current"** — the thing you came for is not a door |

`DERIVED`: the leaf failure is the one your scheme fixes outright.
`goals/{current,future,historical,superseded}` makes the state a door. Today it
is a fact buried inside `records.md`, and you cannot see it from outside.

## One amendment — it binds agents *harder*, not softer

`DERIVED`: you wrote *"for an AI agent this would work differently since you
can probably see the whole structure at once."* I can list the whole tree — but
listing gives me **door names only**, exactly as it gives you. The difference
runs the other way: **you open a wrong door, see an unfamiliar room, and back
out. I open a wrong door and confidently describe it.** Three times today.

## The one thing the analogy cannot express

`DERIVED`: doors make a tree, and some things belong in two rooms. The Play
Store testing floor is a `problems/` fact *and* a `goals/current` fact. A
strict tree picks one and the other room is empty. The estate's existing answer
holds: **one home, and the other room gets a signpost** — `docs/intent.md` § 1,
*"this repo points, it does not copy."*

## Questions for you

1. Should a room ever hold both doors and loose files, or is that always wrong?
2. When something belongs in two rooms, who decides which one is the real home?
3. What question should the door test use as its standard walk?

## Your words

`OWNER`:
