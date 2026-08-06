# 2026-08-06 · hub — the review ladder, run through itself before being written

> **Status:** `complete`

- **📊 Model:** opus-5 · high · idea/planning

Time: 2026-08-06 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: the owner asked for mandatory adversarial review. The spec for
it existed only in two chat transcripts — which is the failure this session has
now documented four times in one day: **correct things placed where nothing
reaches them.** Landing it makes reconciliation a diff instead of archaeology.

## What this is, and what it is not

`docs/conventions/adversarial-review.md`, explicitly marked **proposal with a
verification record, not ratified policy.** A second session is building the
mechanism; this is the hub session's contribution and what survived being run
through itself. It says so in its own header, because a document that reads as
decided when it is not is the same defect as a wall that reads as measured.

## The one idea it rests on

**A reviewer asked "is this right?" must form a domain opinion, and will invent
one if it has no basis. A reviewer asked "what is this based on?" needs no
domain knowledge — it only has to notice whether an answer exists.**

That is what stops mandatory review manufacturing objections, which is the
failure mode that would make it worse than nothing. And it exploits a real
asymmetry: stating a claim is cheap, stating its provenance is not.

Question 1 alone would have caught the three worst errors of today before any
reviewer was involved — the Interactions API wall, the rules-API wall, and
"100 % coverage at 8 fps".

## The mechanism verified itself, and changed

Four turns, Gemini on Vertex, ~4 600 prompt tokens, client-side history.
**Eight substantive changes, zero invented objections**, and twice it said
"well-founded, no objections there" instead of manufacturing balance.

The two that mattered most:

- It **caught the word "reliably" being over-stated — in the sentence arguing
  that agents can detect their own over-statement.** Four supporting examples,
  all fresh in context, and no evidence at all about a path abandoned twenty
  turns ago.
- It asked whether an out-of-bounds case had been run through the correlation
  search before it was trusted. **It had not** — only the happy path. That one
  test would have caught this morning's clamping failure, and it is now a
  standing practice rather than a lesson.

It also split question 5 correctly: *"what did I not run?"* is an operational
checklist an agent can answer; *"am I overconfident?"* is a blind spot by
definition and belongs to the reviewer.

**All eight came from the four times it disagreed. Its agreement taught
nothing** — which is precisely why the convention says record what survived, not
a boolean.

## Where I did not concede

The reviewer proposed a `make review` at PR phase instead of a card section,
implying cards are static. I pushed back: cards already carry entirely dynamic
content, and the owner asked for **planning**-phase review — where today's most
expensive corrections landed, before any diff exists. It accepted the
correction. Recorded because a four-turn exchange that concedes everything is
evidence of deference, not rigour, and this session criticised another for
exactly that.

## Verification

- `python3 tools/check_doc_routes.py --strict` → recorded at close
- `python3 tools/check_no_false_walls.py --strict` → recorded at close
- `python3 bootstrap.py check --strict --require-session-log --simulate-added-card`
  → recorded at close
- The review itself: 4 turns on Vertex, credit-funded, transcript summarised in
  the convention's § verification record

## Honest nulls

- **Unratified, and the doc says so.** The owner has adopted nothing; the other
  session may land something different or better.
- **The gate is unbuilt.** No `path:line` resolver exists; nothing has run in CI.
- **One review, one model, one subject.** "Eight changes" is this document
  reviewing itself; nothing establishes the rate on other material.
- **The Codex rung is described but untested here** — no PR in this session was
  reviewed by it.
- **The proposed metric is unmeasured**: corrections arriving from an instrument
  or reviewer versus from an agent re-reading its own work.

## ⟲ Previous-session review

Five cards today, one shape: a requirement filed where the reader never looks, a
recipe missing its sampling parameter, a funding model compressed until a free
key vanished, a checker that ran nowhere — and now a spec that lived only in
chat. **Every one was correct and unreachable.** This card exists to stop the
fifth becoming the sixth.
