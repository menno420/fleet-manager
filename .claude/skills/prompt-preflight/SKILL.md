---
name: prompt-preflight
description: "The checks to run before writing any session prompt — verify state at HEAD, split what the repo already holds from what only this chat holds, and read the target surface's constraints. Invoked by continuation-prompt and implementation-prompt; run it directly when hand-writing a prompt."
---

# prompt-preflight

The shared pass that makes a prompt correct rather than plausible. Both
`continuation-prompt` and `implementation-prompt` run this first; it exists
separately so neither has to repeat it and so a hand-written prompt can borrow it.

## What this does

Answers four questions before a single line of prompt is written. Skipping any
one of them is how a prompt ships that reads perfectly and is wrong.

## Instructions

### 1 · Verify the state the prompt will assert — at HEAD, not from memory

A prompt inherits the authority of a decision already made. Every factual claim
in it will be believed and acted on, so each one is checked now:

```bash
git fetch origin main -q && git log --oneline -3 origin/main
git branch -a --list 'claude/*' | head
```

Then, for anything the prompt will name:

- **A branch** — does it still exist, and is it behind main? A branch whose PR
  merged is finished; new work restarts from main.
- **A PR** — open, merged or closed? "Continue PR #N" is a dead instruction if
  #N merged, and the next session will either stack commits on merged history or
  stall asking.
- **CI** — green or red right now. A prompt that says "it's green" and isn't
  sends the session hunting for a regression it did not cause.
- **A file or doc** — does the path exist at HEAD? Paths are the single most
  commonly invented detail in agent output; a prompt full of them is worth one
  `ls`.

**Anything you cannot verify does not go in the prompt as a fact.** Write it as
"the previous session believed X — confirm before relying on it".

### 2 · Split: what the repo holds vs. what only the chat holds

This is the whole judgement call, and it has one rule:

> **The prompt carries what is not in the repo. The repo carries the rest.**

- **Point at it** when it is committed and stable — architecture, conventions,
  the capability ledger, a plan document, a session card. A pointer stays true
  when the file changes; an inlined copy silently rots and then outranks the file
  it was copied from.
- **Carry it inline** only when it exists nowhere but the conversation: the
  decisions made, the options rejected *and why*, the owner's intent, the
  constraint that was stated out loud and never written down. This is the actual
  payload. It is the only part a fresh session cannot recover on its own.
- **Leave it out entirely** if the session will re-derive it anyway — file
  listings, code excerpts, directory trees, restatements of what a doc says.
  These cost tokens, go stale, and teach the reader to trust the prompt over the
  tree.

**When the inline payload gets long, that is a signal, not a formatting problem.**
A large body of chat-only decisions means the planning was never recorded. Stop
and run `decision-capture` — commit the decisions, then point at them. The prompt
shrinks to a pointer and the decisions outlive the prompt.

### 3 · Read the target surface's constraints

Prompts run somewhere, and surfaces differ in ways that break instructions
silently. Read [`docs/execution-surfaces.md`](../../../docs/execution-surfaces.md)
and check the four that actually bite:

- **Network during the task.** Off by default on some surfaces. Anything needing
  a download, a package install or a fetch either belongs in the environment's
  setup phase or must be stated as a prerequisite — never as a mid-task step.
- **Credentials.** A PAT exists in some environments and not others, and secrets
  can be stripped before the task phase. Never write a command naming a credential
  without the check that confirms it, then branch on the result.

  ```bash
  printenv GITHUB_PAT >/dev/null && echo present || echo absent
  ```
- **Tooling.** Do not assert a binary is present. A presence check costs nothing
  and converts "it's broken" into "install it".

  ```bash
  command -v <tool> >/dev/null || <install line>
  ```
- **Setup-phase exports.** Not all surfaces carry them into the task phase, so a
  prompt cannot assume an env var set by a setup script is visible.

If the surface is unknown, write the prompt so it **checks rather than assumes**,
and say so in one line: *"verify tooling and credentials before relying on them;
this prompt does not assume which environment you are in."*

### 4 · Decide what "done" is, and how it is checked

A prompt without an acceptance test delegates the definition of success to the
reader. Name:

- the **verify command** the repo actually uses (`python3 bootstrap.py check
  --strict`, `python3 tools/verify.py` — check which, do not guess);
- what a **finished** state looks like — merged PR, green CI, a specific file
  existing with specific content;
- what is **out of scope**, explicitly. Stated non-scope is the cheapest
  correction available and the most consistently omitted.

## Output

A short preflight note the calling skill consumes — not shown to the owner
unless asked:

```
STATE      : <branch / PR / CI, each verified just now>
POINT AT   : <paths that exist at HEAD>
CARRY      : <decisions that exist only in this chat>
OMIT       : <what the session will re-derive>
SURFACE    : <constraints that change the wording, or "unknown — check-don't-assume">
DONE WHEN  : <acceptance + verify command>
UNVERIFIED : <anything asserted but not checked — must appear in the prompt as uncertain>
```

An empty `UNVERIFIED` line is the goal. A non-empty one is fine — it just has to
survive into the prompt as doubt rather than being quietly promoted to fact.
