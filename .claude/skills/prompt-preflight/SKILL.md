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

### 3 · Read the target surface's constraints — ALL FOUR SOURCES, not one

**The moment the owner names who the prompt is for — ChatGPT, Codex, Gemini,
Grok, a Claude surface — reading that vendor's records is part of writing the
prompt.** Not one doc. Four, and the order matters because the last one is where
the walls get refuted:

1. **`docs/providers/<vendor>.md`** — model ids, surfaces, what the vendor
   actually is this month.
2. **`docs/prompts/<vendor>-*.md`** — any standing instruction set already
   written for that surface. Do not re-derive one that exists.
3. **[`docs/execution-surfaces.md`](../../../docs/execution-surfaces.md)** — the
   comparison table and the four constraints below.
4. **`docs/CAPABILITIES.md`, grepped for the surface name.** This one is not
   optional and it is the one that gets skipped:

   ```bash
   grep -n -i "<surface name>" docs/CAPABILITIES.md
   ```

**Why step 4 is mandatory.** `MEASURED` 2026-08-30: a session wrote a ChatGPT
Work prompt having read sources 1–3, and hedged that it *"could not verify
whether ChatGPT Work can open a PR through the connector."* The owner corrected
it — *"Gpt work has full access and you could verify that in the repo"* — and
`docs/CAPABILITIES.md:429` settles it in as many words: measured across fm #835's
entire landing, the connector created the branch, the commits, a READY PR, review
replies, resolved threads, read check runs and returned a full Actions job log,
with repo metadata `admin: true, push: true`. The entry even ends *"Do not probe
for `gh` or `$GITHUB_PAT` on that surface; their absence blocked nothing."* The
hedge was a false wall, written into an artifact the receiving session would have
obeyed — the exact failure `tools/check_no_false_walls.py` exists to catch, and it
does not scan prompts. **Before you write a single line about what a surface
cannot do, grep the ledger for it.**

Then check the four that actually bite:

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
