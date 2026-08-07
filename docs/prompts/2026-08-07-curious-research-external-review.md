# External review of `curious-research` — the paste-ready prompt

> **Status:** `reference` · written 2026-08-07 for the owner.
>
> He plans to have independent sessions (ChatGPT, Grok) review `curious-research`
> to find out whether they understand its purpose and can suggest additions.
> **That plan has a measured failure mode**, and this file is the fix.

## Why not just paste the repo and ask "what do you think?"

`findings/2026-08-06-provenance-mechanism-measured.md` established it in three
controlled runs:

> **An unframed reviewer endorses whatever it is shown.**

It endorsed a design this estate had already superseded, and praised the specific
defect as the best part. The same model, same input, given a stand-in system
prompt, returned three real objections and one defect that three deep-research
reports had missed.

So an unframed *"what do you think of my repo?"* will very likely come back warm,
fluent and worthless. That is not a property of ChatGPT or Grok. It is a property
of the question.

Two rules carried over from [`../conventions/adversarial-review.md`](../conventions/adversarial-review.md),
which is the version that survived five rounds of being attacked:

- **Agreement is nearly worthless as evidence; the objections are the product.**
  If a review raises nothing, that is a result to record, not a pass.
- **Ask for provenance and specifics, not opinions.** A reviewer asked *"is this
  good?"* must manufacture a judgement. A reviewer asked *"what would he do
  first, and where would he get stuck?"* only has to read.

## The design: two parts, and part 1 must run unprimed

**Part 1 is the actual comprehension test.** It only measures something if the
reviewer has *not* been told the answer. So do not paste any description of the
repo, and do not paste this file's explanation, before part 1 is answered.

**Part 2 is the gap hunt**, and it runs *after* you reveal who the reader really
is. Only then can a reviewer tell a real gap from a thing it merely did not know.

Run part 1, get the answer, *then* paste part 2. Not both at once.

---

## PART 1 — paste this first, alone

```
I'm going to give you a public GitHub repository. Read it before answering:
https://github.com/menno420/curious-research

Do not evaluate it yet. Do not tell me whether it is good. I am testing whether
the repository explains itself, so your first answer is a comprehension test and
praise would only tell me you are agreeable.

Answer these six questions from the repository alone. Where it does not say,
answer "the repo does not say" rather than inferring — a gap in your answer is
the most useful thing you can give me here.

1. Who is this repository for? Describe the person as specifically as the repo
   lets you: what they can already do, what they cannot, what tools they own.
2. What is it FOR? Not what it contains — what is it supposed to change for
   that person?
3. What is the single thing it wants them to do first, and where does it say so?
4. What language is it in, and why is it in more than one?
5. Name three things in it you are confident about, and for each, cite the file
   or page you got it from.
6. Name everything you found confusing, contradictory, or could not answer.

Be blunt in question 6. That list is the reason I am asking you.
```

---

## PART 2 — paste this only after part 1 is answered

```
Here is what is actually true, so you can tell a real gap from something you
simply did not know.

The repository is a gift. The reader is a Dutch hobby maker in his sixties —
the giver's weekend foster-father. He is NOT a beginner and must never be
addressed as one:

- He already uses Claude weekly (Arduino, 3D printing, Fusion 360). He is new to
  GitHub, not to AI. What he has never had is PERSISTENCE — every good answer he
  gets dies with the chat window. That, and only that, is the repo's pitch.
- Hardware: a Bambu Lab A1 mini and an A1 with AMS Lite; a 6-DOF robot arm on six
  MG996R servos that is already built, wired, and moving under program control;
  a busy Arduino bench. He also laser-cuts and CNC-mills, drawing 2D in Fusion 360.
- He solved his own servo power supply — enclosed switching supply, distribution
  board — months before the repo mentioned power.
- Low coding skill. High everything else. Anything that reads as talking down to
  him is a defect, not a style choice.

He will be given a Claude subscription along with the repository, so a Claude
session reading it is a first-class user of it, alongside him.

Now, with that in hand, four questions. I want specifics I can act on, not an
assessment.

1. Where does the repository still treat him as a beginner, or explain something
   he demonstrably already knows? Quote the line.
2. He owns a laser cutter and a CNC mill and draws 2D for both in Fusion 360.
   What implementation guidance is missing for getting from a Fusion sketch to a
   cut part? Be concrete: name the steps a guide would have to cover.
3. What would he most plausibly try in his first hour, and where would he get
   stuck? Trace the actual path.
4. What is here that should not be — anything that serves the giver, or the
   machinery that built it, rather than him?

Rules for your answer:

- Number every objection separately so each can be accepted or rejected on its
  own. Do not bundle.
- For each, say what you are basing it on — a file, a page, a line. "It feels
  incomplete" is not usable; "guides/X says Y, which contradicts Z" is.
- If you cannot find a real problem in one of these areas, say so plainly. I
  would rather have two solid objections than eight padded ones, and inventing
  a problem to seem thorough is the worst outcome here.
- Do not soften. I am not attached to any of it and nothing here is finished.
```

---

## What to do with the answers

**Record each objection individually as `[survived]` / `[conceded]` /
`[partial]`.** The convention doc explains why: *"three objections raised, three
conceded"* reads as rigour and is equally consistent with pure deference. Forcing
a per-item disposition is what makes the tally countable rather than a vibe.

**Do not concede on reflex.** These reviewers have a known error rate — one
Gemini review in this estate was flatly wrong about a dependabot deadlock;
another overclaimed and was caught only by independent measurement. An objection
you can refute with a file is a refuted objection, and worth recording as one.

**Expect part 1 to be the more useful half.** Question 6 — what was confusing or
unanswerable — is the closest thing available to watching a stranger open the
repo cold, which is exactly what will happen when the maker is handed it.

**Two reviewers is a real design, not redundancy.** Where ChatGPT and Grok
disagree about what the repo is for, the repo is ambiguous — and that is a
measurement neither one alone can give you.
