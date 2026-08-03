---
name: continuation-prompt
description: "Carry a planning or working session into a fresh one — harvest the decisions this chat made, verify state at HEAD, commit what should be committed, and emit a paste-ready prompt that points at the repo and carries only what the repo cannot."
---

# continuation-prompt

The owner spends a session planning and deciding, the context fills, and the work
has to continue somewhere new. This produces the prompt that starts that session.

## What this does

Turns the *current* conversation into a handoff. The material is what was decided
here — never invented, never a generic restatement of the project. If this
session did not decide anything, say so plainly and stop; a continuation prompt
with nothing to continue is worse than none, because it reads as authoritative.

## Instructions

### 1 · Run `prompt-preflight`

Do not skip it and do not summarise it from memory. The two failures it catches
are exactly the two that make a continuation prompt dangerous: asserting a branch
or PR state that has since changed, and inlining what should have been a pointer.

### 2 · Harvest the decisions — from this chat, not from the repo

Walk the conversation and pull out only these:

- **Decided** — a choice that was made and is not yet in the repo. Include the
  reasoning in one clause; a decision without its reason gets re-litigated.
- **Rejected** — options considered and dropped, *and why*. This is the highest
  value item in the whole prompt and the most commonly omitted. Without it the
  next session re-proposes the rejected thing, and the owner pays for the same
  conversation twice.
- **Open** — genuinely undecided, with what would settle it. Distinguish
  "undecided" from "not yet discussed"; they need different handling.
- **Owner-stated constraints** — anything said out loud that is not written down
  anywhere. These outrank inference and are invisible to a fresh session.

Quote the owner where the wording matters. A paraphrased constraint drifts; a
quoted one does not.

### 3 · Offer to commit before you write

If the harvest is long, the right move is usually not a longer prompt. Run
`decision-capture`: land the decisions in the repo, then point at them.

Say this to the owner in one line and let him choose:

> "Six decisions here aren't in the repo. I can commit them to
> `<path>` first — then the prompt is four lines and a pointer, and the
> decisions outlive the prompt. Or I can carry them inline."

Committing is better whenever the decisions will matter beyond the next session.
Inlining is fine for a genuinely one-shot handoff.

### 4 · Write the prompt

Fixed shape. Every section earns its place; drop any that is empty rather than
padding it.

```text
CONTINUE: <one line — what this session is picking up>

WHERE THINGS STAND
<verified state: branch, PR, CI, what landed. Each item checked at HEAD in
preflight. If something is believed but unverified, say "believed, confirm".>

READ FIRST
<2–4 paths, most specific first. Not a reading list — the minimum to act
correctly. If one doc supersedes the others, say which wins.>

DECIDED (do not re-litigate)
<each decision, one line, with its reason clause>

REJECTED, AND WHY
<option → reason. This is what stops the next session re-proposing it.>

OPEN
<what is genuinely undecided, and what would settle it>

YOUR FIRST STEP
<one concrete action. Not "get oriented" — a specific first move, ideally one
that verifies the state above rather than trusting it.>

DONE WHEN
<acceptance + the verify command this repo actually uses>

OUT OF SCOPE
<what not to touch. Always present; this is the cheapest correction available.>
```

### 5 · Adapt to the target surface

Ask which surface it is for if it is not obvious. Then, from
[`docs/execution-surfaces.md`](../../../docs/execution-surfaces.md), adjust only
what actually differs:

- **Task-phase network may be off.** Move any install, download or fetch into a
  prerequisite line — *"the environment must already have X"* — instead of a
  mid-task step that will fail opaquely.
- **Credentials are not universal.** Never name a credential without the check
  that confirms it, and never imply a session is blocked without one. State the
  fallback: git over the configured remote does clone/fetch/push/branch.

  ```bash
  printenv GITHUB_PAT >/dev/null && echo "direct path available" || echo "use the remote"
  ```
- **Tooling.** Write the presence check, never "use <tool>":

  ```bash
  command -v <tool> >/dev/null || <install line>
  ```
- **Landing discipline differs per repo, not per surface.** State it explicitly
  — born-red card first, PR ready immediately, flip complete last — because it is
  repo convention and no surface infers it.

If the target is unknown, write check-don't-assume phrasing and say so in a line.

### 6 · Hand it over

Give the owner the prompt in a single fenced block he can copy without editing.
Then, in **one or two sentences outside the block**, say what you verified and
what you could not. Do not annotate the block itself — annotations get pasted in.

## Traps

- **Do not restate the project.** A fresh session in the repo reads the boot file
  itself. Every line spent re-describing the architecture is a line not spent on
  what only this chat knows, and it goes stale the moment the repo moves.
- **Do not invent a next step to sound complete.** If the work genuinely stopped
  at a decision point, the first step is *"confirm the state below, then ask the
  owner which branch to take"*. That is a real instruction.
- **Do not carry a number you have not re-derived.** Counts, distances, sizes and
  dates from a conversation are the most drift-prone thing in a handoff. Re-check
  or mark uncertain.
- **Do not write a prompt longer than the doc it should have pointed at.** That
  is the signal to commit instead — go back to step 3.
