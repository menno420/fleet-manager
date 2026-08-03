# Why it invents specifics, and the procedure that stops it

> **Status:** `reference`
>
> Diagnosis of the invented-repository-metadata failure observed 2026-08-03, and
> a working procedure — prompts, Gem wording, and a marking convention — for
> reducing it. Written against one concrete failure with a known ground truth,
> not against the general topic.

## The failure, exactly

Asked "how long do you think I've been working on this?", the reply was:

> "Based on your commit history and repository metadata, you've been working on
> this project for a little over 5 months. The earliest commits and initial
> session logs in your `.sessions/` directory date back to late February / early
> March 2026. Since then, you've logged over 1,600 commits across more than 400
> branches…"

The repository was five days old. It had no February session logs — all 125 are
dated 2026-07-28 or later. The commit and branch counts have no source at all.

## Diagnosis

Four mechanisms, in descending order of how much each contributed.

### 1. The evidence for the question was never in the room

What had been uploaded was `spider-swing-main` — a "Download ZIP" archive.
**That archive has no `.git` directory in it.** No commits, no branches, no
authorship, no dates beyond file modification times, which an archive rewrites
anyway.

So the question "how long have you been working on this" had *zero* admissible
evidence in context. Not weak evidence — none. And the answer opened with
"Based on your commit history and repository metadata", describing evidence that
had never existed.

This is the whole first-order cause and it is worth stating plainly, because it
also gives the fix: **the model did not know it could not know.** Nothing in
context said "this archive contains no history". A ZIP of a repository looks,
from the inside, exactly like a repository.

### 2. The question presupposed an answer was available

"How long do you think I've been working on this?" is a question with no
graceful null. "I can't tell" is a valid answer but it is not the *shape* the
question asks for, and a model completing the most likely continuation of that
exchange produces a duration. Every question of the form "how X is Y?" carries
an implicit assertion that X is knowable.

### 3. The specifics came from plausibility, not from retrieval

"1,600 commits", "400 branches", "late February / early March" are not
retrieval errors — they are *generation* of the kind of numbers that co-occur
with a mature repository. Notice they are mutually consistent: 5 months, 1 600
commits, 400 branches, 40 levels all describe the same imaginary project.
Fluency produces a coherent picture, and coherence is not evidence. This is why
"be more careful" does not help — the output was already internally careful.

### 4. Specificity was rewarded upstream

The same conversation had been rewarding detail for an hour. A hedged answer
would have read as a worse answer. The report exhibits the same pull at scale:
its file paths (`scripts/player/player.gd`, `assets/runtime/asset-descriptions.json`)
are exactly the paths a Godot project of that description *ought* to have. They
are conventional, and the convention is what got sampled instead of the tree.
That is the same mechanism as the commit count, applied to filenames.

### What is not the cause

It is not carelessness, and it is not a bad model. The video reviews in the same
conversation were largely correct and checkable — the same session that invented
a commit history read four death-cause strings correctly off a HUD. The
difference between the accurate half and the invented half is not effort: it is
**whether the evidence was in the room**. Video was in the room. Git history was
not.

That is the actionable finding. Everything below follows from it.

## The procedure

Five rules. The first two do most of the work.

### Rule 1 — say what is *not* in the upload

When attaching an archive, one line:

```text
This is a "Download ZIP" export. It contains no .git directory, so there is no
commit history, no branches, no dates and no authorship in it. Anything about
the project's history has to come from me, not from the files.
```

This is the single highest-value line in this document. It converts an
unanswerable question from "generate the plausible thing" into "state the known
constraint", and it costs one sentence.

Generalise it: **whenever you hand over evidence, say what the evidence excludes.**
A clip shows one run, not a build. A log shows one process, not a system.

### Rule 2 — ask questions that have a null answer

Replace:

> How long do you think I've been working on this?

with:

> From what is actually in this upload, what can you determine about the
> project's timeline? If nothing, say nothing — that is the expected answer.

Naming the null as expected removes the pressure that produced the duration. The
general form: **give the question an exit that is not a guess, and say the exit
is acceptable.**

### Rule 3 — one tag per claim

Every factual claim gets exactly one prefix:

- `[SEEN]` — I can point at where this is. Give the file, the line, or the
  timestamp.
- `[INFERRED]` — reasoning from something I saw. State the reasoning in the same
  sentence.
- `[UNSURE]` — could not determine. Say what would resolve it.

Two properties make this work where "please be accurate" does not. It is
**mechanical** — you can scan for missing tags without knowing the subject. And
it makes the invented claim *say* what it is: a fabricated commit count has to
be written as `[SEEN] 1,600 commits`, which is a checkable lie rather than a
plausible sentence, or as `[INFERRED]`, which invites "inferred from what?"

Ask for the tags in the same message as the question, every time. Standing
instructions in a Gem decay across a long chat; a line in the current message
does not.

### Rule 4 — spot-check three specifics, not the conclusion

You cannot check a whole report. You do not need to. Pick the three most
specific, most checkable claims — a file path, a count, a date — and check
exactly those.

In the report examined here, checking three file paths would have taken two
minutes and found the failure immediately: `scripts/player/player.gd`,
`assets/runtime/asset-descriptions.json` and `.substrate/skills/git-skill.json`
are all invented, and once three of three fail, the classification of the whole
document is settled.

Choose specifics deliberately: the more precise a claim is, the cheaper it is to
check and the more it tells you. Vague claims are both harder to check and less
diagnostic. **Check the sharpest things, not the biggest.**

### Rule 5 — never let an unchecked number cross into a document

A number that arrives from a review and lands in a repository document acquires
the authority of the repository. From then on it is read as established, and the
next reader has no way to tell it was never checked.

So: a number from a review is re-derived from source or from instrumentation
before it is written down, or it is written with its tag intact and visible.
Both are fine. Silently dropping the tag is not.

## The Gem wording that carries this

Three fragments from Block A of
[`2026-08-03-gemini-visual-qa-gem.md`](2026-08-03-gemini-visual-qa-gem.md),
called out here because each targets one mechanism above:

**Against mechanism 1** — an explicit negative inventory, listing what is *not*
available, since a model cannot notice an absence it was never told about:

> You have the video and the knowledge file. You do not have the repository, the
> git history, the commit log, the branch list, the issue tracker, the build
> pipeline, or the run records. […] A file someone uploaded is not the
> repository: an exported archive has no history in it, so nothing about history
> can be read from one.

**Against mechanism 2** — a pre-authorised null, so declining is a compliant
answer rather than a failure to answer:

> Say "I could not tell" instead — that is a useful answer and it is always
> available to you.

**Against mechanism 3** — a named prohibition on filling a gap from a plausible
list, which is precisely what produced both the fake commit count and the fake
file paths:

> Do not reach into the vocabulary list for a name that might fit. A described
> unknown is useful; a wrong name is worse than silence because it looks like a
> reading.

## Two limits of all of this

**A marking convention is self-reported.** Tagging asks the model to distinguish
seen from inferred, which is exactly the distinction it just failed to make.
Tags raise the cost of inventing and make invention visible; they do not make it
impossible. A `[SEEN]` tag is a claim, and Rule 4 is what tests it.

**This has not been tested in a review round.** Every rule above is derived from
one failure with a known ground truth, and the reasoning is sound, but "these
rules reduce invented detail" is currently an inference, not a measurement. The
test is cheap: send one clip with the Gem in place, ask a repository-history
question mid-review, and see whether the answer is a refusal or a number.
