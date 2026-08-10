---
state: captured
origin: lab
shipped_pr: null
shipped_repo: null
merged_date: null
outcome: open
---

# Derive, don't state — a checker for counts about the repo's own contents

> **Status:** `ideas`

**Idea:** a narrow lint that flags a *numeric count of repo contents* written
into prose — "5 hooks", "27 skills", "the four gates", "seven defects" — in the
read-path docs, and asks the author to derive it instead. Not a spell-checker
for numbers: it should fire only where the counted thing is enumerable from the
tree (`.claude/hooks/*.py`, `.claude/skills/*/SKILL.md`, a workflow's step list),
which is exactly the class that goes stale silently.

**Why worth having:** this estate keeps rediscovering the same failure, and
always the same way — the count was right when written and wrong a commit later.

- `docs/execution-surfaces.md` said **"none of the five hooks"** while there were
  six. `git log -S` puts the sentence in `e9214c5`, committed *after* `a02a4b1`
  added the sixth hook **in the same session**. It survived a Codex round and an
  owner read; the independent fm #835 reviewer caught it by running `ls`.
- `.claude/hooks/README.md` said the trigger suite had **31 cases** while the
  executable reported **52**.
- The `session-close` skill enumerated **two of three** gate commands until
  2026-08-08, which is why the boot file now says outright that the check list
  lives in the script and not in prose.

Three instances, three different documents, one mechanism. The current defence
is a sentence telling authors not to do it — and the boot file's own rule is
that *"the fix for an unfollowed rule is a mechanism that delivers it at the
right moment, never another statement of it"* (`docs/intent.md` § 4).

**Why it might not be worth having — state this honestly before building.** The
false-positive surface is large: prose is full of legitimate numbers ("two of
the nine", "a 48-character window", dates, PR numbers, measured results). A
checker that cannot tell *"27 skills"* from *"23/24 cases passed"* would be
noise, and this repo has already withdrawn two gates for mechanising meaning.
The narrow version — only counts immediately followed by a noun naming a
tree-enumerable artifact, only in the five read-path docs — may be small enough
to be worth it. That judgement needs a measurement, not an argument: run the
candidate regex over the repo's history and count how often it would have fired
correctly versus wrongly.

**Route:** cheap to prototype as a `tools/` checker alongside
`check_no_false_walls.py`, advisory-only at first so its false-positive rate is
observable before it can ever block a merge. Promotion to the gate follows the
same rule as every other checker here: the measured false-positive rate decides.

**Status:** captured, not approved. Do not build it inside a session whose job
is something else.
