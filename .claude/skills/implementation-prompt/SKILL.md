---
name: implementation-prompt
description: "Write a prompt that directs a session to build a defined thing — scope and explicit non-scope, the contract it must satisfy, where the patterns already live, the verify command, the landing discipline, and the traps that have actually bitten here."
---

# implementation-prompt

For work whose shape is already agreed. If the shape is *not* agreed, this is the
wrong skill — the result will be a confident prompt for the wrong thing. Decide
first, then come back.

## What this does

Produces a prompt a session can execute without asking a clarifying question, and
without inventing the parts you left out. The measure is simple: **if a reasonable
session could build something you would reject, the prompt is not finished.**

## Instructions

### 1 · Run `prompt-preflight`

Same reason as always. Additionally, for implementation work, confirm the thing
being asked for does not already exist — a `grep` for the symbol or the doc
heading costs seconds and has retired more than one "build X" ask in this estate.

### 2 · Establish the contract before the prose

Answer these four for yourself. If any is blank, the prompt is not ready:

| | |
| --- | --- |
| **Built** | The observable change. Not "improve X" — what is true afterwards that is not true now. |
| **Not built** | The nearest adjacent things deliberately excluded. State them; a reader who does not see a boundary assumes there isn't one. |
| **Acceptance** | How anyone tells it worked, mechanically. A command, a test, a file that must exist with specific content. |
| **Rejected shapes** | Approaches already considered and dropped, with the reason. Omit these and they get rebuilt. |

### 3 · Point at the patterns rather than describing them

The strongest line in an implementation prompt is usually a path:

> "Follow the shape of environments/setup-base.sh — numbered blocks, every step
> non-fatal, always exit 0. Do not introduce a new pattern for this."

That is shorter, more precise and less rot-prone than any description of the
pattern, and it makes the repo the authority rather than the prompt. Give **one**
exemplar, not three; three invites averaging.

Name a file that exists **in the repo the prompt targets** — check it. A path
that resolves nowhere sends the session looking, and an invented exemplar path is
one of the most common failure modes in agent-written prompts.

### 4 · Write the prompt

```text
BUILD: <one line — the observable change>

CONTEXT
<the minimum to act correctly. Paths, not prose. If a doc explains why, link it
rather than summarising it.>

FOLLOW THIS PATTERN
<one existing file that already does the analogous thing>

REQUIREMENTS
<numbered, each independently checkable. A requirement nobody can check is a
preference — mark it as such or cut it.>

EXPLICITLY NOT IN SCOPE
<the adjacent things. Always present.>

ALREADY REJECTED
<approach → why. Skip only if genuinely nothing was rejected.>

ACCEPTANCE
<the command, the test, or the file state that proves it. Name the repo's real
verify command — check which one, do not guess.>

LANDING
<branch naming, born-red card first, PR ready immediately, green CI, flip
complete last. State it; no surface infers repo convention.>

TRAPS
<what has actually gone wrong here before — see step 5>
```

### 5 · Include the traps that have actually bitten

Generic warnings are ignored. Specific ones, with the failure attached, are read.
Pull from `docs/CAPABILITIES.md` and recent session cards. Real examples:

- *"Never read `$?` after a pipe — it reports the last command in the pipeline, so
  a red gate reads green. Capture the checker's own exit code."*
- *"A 403 from the proxied GitHub REST path is a path quirk, not a permission
  wall. Retry direct before recording anything."*
- *"CI can fail where the local gate passes — the session-card grammar check fires
  only on an added card. Local green is not CI green."*

Two or three that apply beat a list of ten that mostly don't.

### 6 · Adapt to the target surface

From [`docs/execution-surfaces.md`](../../../docs/execution-surfaces.md), and only
where it changes an instruction:

- **Network may be off during the task.** Every dependency becomes a prerequisite
  line, not a step. If the build genuinely needs a fetch, say so at the top so it
  is a configuration decision rather than a mid-task failure.
- **Credentials.** Name the check, never the bare variable. Never imply the work
  is blocked without one.
- **Tooling.** Check presence before use rather than asserting it:

  ```bash
  command -v <tool> >/dev/null || <install line>
  ```
- **Verification depth.** If the surface may not run the full suite, name the
  minimum that must pass and say what it does not cover.

### 7 · Sanity-check before handing it over

Read your own prompt as a session that knows nothing about this conversation:

1. Could I build something you would reject while satisfying every line? → the
   requirements are underspecified.
2. Is any factual claim unverified? → mark it uncertain or cut it.
3. Is anything here recoverable from the repo? → cut it and point instead.
4. Does it say what *not* to do? → if not, add it.

## Traps

- **Do not specify the implementation when the contract is what matters.** Over-
  specified prompts produce work that satisfies the letter and misses the point,
  and they waste the reader's judgement — which is the thing you are paying for.
- **Do not bundle.** One coherent deliverable per prompt. A three-part prompt
  gets a session that finishes part one well and rushes the rest.
- **Do not omit the landing discipline** because it feels like boilerplate. It is
  the most common reason otherwise-good work does not land.
