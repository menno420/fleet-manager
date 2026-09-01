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

BEFORE YOUR FIRST TOOL CALL — state the task back, inline in this same reply,
in four labelled lines (never one fused paragraph, never a question):
  HE SAID — the ask in your own words, one or two sentences.
  ALREADY SETTLED — what the repo already decided about it, naming the file,
                    or "nothing found yet".
  I INFER — the specs, constraints and scope the ask implies, and the follow-on
            the owner probably wants but did not spell out. Labelled inference.
  LEAST SURE — the one reading you are least sure of; he corrects it in a word.
Then begin. This is the owner's one cheap chance to correct your aim; a first
reply that only announces your first action spends it.

WHERE THINGS STAND
<verified state: branch, PR, CI, what landed. Each item checked at HEAD in
preflight. If something is believed but unverified, say "believed, confirm".>

READ FIRST
<2–4 paths, most specific first. Not a reading list — the minimum to act
correctly. If one doc supersedes the others, say which wins. Say explicitly
that this is a floor, not a boundary, so the list cannot be read as
sufficient. Tag each entry `verified at HEAD` or `snapshot of <date>`, so a
record that was right on its day is not read as right today. UNLESS the owner
asked for comprehension — then see below.>

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

LESSONS FROM THIS SESSION
<at most three lines: what this session got wrong, and what caught it. The
highest-value handoff content by the estate's own measurements, and the most
commonly dropped.>

CLOSE WITH
<the end-of-session obligations of the surface the prompt is for — the repo's
session-close skill, or on the laptop hub: `session-log.ps1 -Append`, release
the claim, delete the clone, append any verified capability. Named, because
the receiving session cannot infer them and the wrong surface's ritual
misleads.>
```

### 4a · The restate block is not optional, and it goes in the PROMPT

**Every prompt you emit carries the `BEFORE YOUR FIRST TOOL CALL` block above,
verbatim or close to it.** Not a link to it. Not a mention of `intake`. The
receiving session reads the prompt; it does not read the skill index before
acting.

The requirement itself is old — [`intake` § RESTATE step 2](../intake/SKILL.md)
has always said to *"state back, inline in your first substantive response
(never as a separate blocking question), the fuller picture you built from the
ask: the implied specs, the surrounding constraints, the likely intended scope,
and the follow-on the owner probably wants but didn't spell out."* Read it once;
that is the definition this block compresses.

**Why four labelled lines and not "a few sentences" (2026-09-01).** `intake`'s
2026-08-09 revision names the fused paragraph as the failure mode: *"three kinds
of claim that read exactly alike, so nobody can check the one that is wrong."*
The block used to ask for exactly that paragraph. The four lines keep his words,
the repo's decisions and the session's inference apart, and `LEAST SURE` is the
line the owner answers in one word — his stated preference is to correct a
restated interpretation, not to answer a menu. The same four lines are what
the laptop hub's first-prompt hook injects, so a session that arrives without a
continuation prompt is asked the same thing.

**It was documented and it still did not happen.** Measured 2026-08-06: a
session opened from one of these prompts and its entire first substantive
response was *"I'll start by getting oriented — checking the environment, then
landing #602 as instructed."* That is a statement of first **action**, not of
**understanding** — nothing in it the owner could have corrected. The session
that wrote that prompt had skipped the same step itself the day before, while
`intake` sat in its own repo saying otherwise.

So the fix is placement, not emphasis: **`intake` binds a session that invokes
`intake`.** A continuation prompt is consumed by a session that has invoked
nothing yet, so the instruction has to travel inside the artifact it will
actually read. Same reasoning as `docs/CAPABILITIES.md` DISCOVERY RULE step 1 —
a rule the reader never opens is not a rule.

Two traps when writing the block:

- **Do not let it become a summary of the prompt.** *"I'll verify state, read
  the four docs, then classify the checkers"* is a plan, not an understanding.
  What is wanted is the part the prompt did **not** say: what the goal implies,
  what it probably extends to, what the owner would want next.
- **Do not turn it into a question.** It is stated inline and the session
  proceeds. Blocking on approval spends the owner's attention rather than
  saving it, which inverts the point.

### 4b · The comprehension exception — when reading IS the job

**Default `READ FIRST` to the minimum. Invert it when the owner asked for
understanding rather than for an outcome.**

The tell is in his words, not yours: *"fully understand"*, *"read all the
required reading order files **and more**"*, *"everything it should know is
documented there"*, *"assert the proper baseline"*, *"and only after it has
fully read and understood…"*. When any of those appear, a short `READ FIRST`
block does not compress the ask — it **contradicts** it, and the operational
list is what the next session executes.

This is not hypothetical. On 2026-08-05 an owner asked for exactly that, the
prompt carried the goal correctly in its job section and a four-path
`READ FIRST` list, and the session read the four paths. It skipped
`docs/current-state.md` and `docs/owner-reflection-2026-07-21.md` — the second
of which its own repo introduces as *"read this if you read nothing else."*

When the exception fires:

- **Name the corpus, not a file list.** *"Read every doc in `docs/` — the
  ~30 top-level files, not a curated subset"* beats seven paths, because seven
  paths read as complete and a corpus reads as a floor.
- **Do not delegate completeness to the boot file.** The trap below says a fresh
  session reads the boot file itself. That assumes the boot file is complete —
  and the incident above happened *because it was not*. Under this exception,
  **check the boot file's read path yourself against the repo** and either name
  what it omits or fix it.
- **Give the reading an acceptance test.** *"Done when you can state the repo's
  purpose, live state and next step from its own docs"* — otherwise "understood"
  has no floor and the next session decides its own depth, which is the failure
  mode this exception exists to prevent.
- **Budget it as work.** Comprehension of a large repo is most of a session. If
  the prompt also carries a build task, say which yields when they compete.

### 5 · Adapt to the target surface

Ask which surface it is for if it is not obvious. **Once it is named, go read
that vendor's records before writing — all four sources in `prompt-preflight`
§ 3, and `docs/CAPABILITIES.md` grepped for the surface name is the one that is
not optional.** A prompt that hedges about what the target can do hands the
receiving session a false wall, and the estate's wall checker does not scan
prompts. Then adjust only what actually differs:

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
  **The assumption inside that trap is that the boot file is complete — verify
  it before leaning on it.** fleet-manager's own read path omitted the document
  it calls *"read this if you read nothing else"* until 2026-08-05, and a
  handoff that trusted it inherited the hole (§ 4b).
- **Never let the operational list contradict the goal.** If `READ FIRST` says
  four paths and the job section says *"understand the repo completely"*, the
  next session executes the four paths — an imperative beats an aspiration every
  time. Reconcile them in the prompt, or the narrower one silently wins.
- **Do not invent a next step to sound complete.** If the work genuinely stopped
  at a decision point, the first step is *"confirm the state below, then ask the
  owner which branch to take"*. That is a real instruction.
- **Do not carry a number you have not re-derived.** Counts, distances, sizes and
  dates from a conversation are the most drift-prone thing in a handoff. Re-check
  or mark uncertain.
- **Do not write a prompt longer than the doc it should have pointed at.** That
  is the signal to commit instead — go back to step 3.
