# 2026-08-05 · hub — what the eight catches were actually made of

> **Status:** `complete`

- **📊 Model:** opus-5 · high · research

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: the foundation doc concluded the owner's detection is exterior
and therefore catches only loud failures. That was written before he caught two
**quiet** ones. The correction is small in words and large in consequence.

## What landed

- `docs/findings/2026-08-05-foundation-continuation.md` § 2 — a same-day
  correction. The original claim holds for when he is away; it is wrong for when
  he is present, and § 1's build order inherits the error.
- `docs/owner-profile.md` § Presence model — his working model in his own words,
  with the measured base rate behind it.

## The measurement

Eight problems flagged across one session. **Eight correct. Zero false
positives.** The composition is the finding:

| | Count | Caught by |
|---|---|---|
| Execution errors | **0** of 8 | — |
| Judgement errors at decision points | **8** of 8 | him, reading the reasoning |
| Off-taxonomy card fields | 2 | CI, in seconds |

The two quiet catches that break § 2's model:

1. **Step 0 scoped to "provisioning".** Passed every gate, read as careful, and
   licensed a session to overturn an owner statement with a failed probe hours
   later. No exterior signal exists for a boundary written one word too narrow.
2. **A mis-recorded root cause.** The Interactions-API card blamed a skipped
   document — true, and second-order. Nothing exterior tells a correct
   post-mortem from a plausible one.

## The conclusion, and it is uncomfortable for § 1

> **This estate instruments execution. It does not instrument judgement.**

Both foundation items — the reachability checker and the transcript-plus-state
gate — are real and worth building, **and both cover execution.** That is the
half CI already covers. Nothing proposed covers *"is this the right thing to
decide"*, which is where all eight failures lived.

So automating the owner out of the planning loop is a **harder** problem than
the revised order implies, not a nearer one. The test for any claim to have done
it: *what, specifically, would have caught step 0 being scoped one word too
narrow?*

## Verification

- `python3 bootstrap.py check --strict --require-session-log --session-log <card>
  --simulate-added-card <card>` → recorded below, run post-commit.
- `python3 tools/check_doc_routes.py --strict` → exit 0.
- `python3 tools/check_no_false_walls.py --strict` → exit 0.

## Honest nulls

- **`n = 1` session.** Eight catches by one person on one day. The precision is
  measured; the *rate* is not, and a session where he flags nothing is not
  evidence he missed nothing.
- **His "at least right now" is load-bearing** and preserved verbatim. This is a
  present-tense claim about a gap, not a permanent division of labour.
- **The false-negative rate stays `NOT-VERIFIABLE`.** Nothing here counts what
  nobody detected; the correction narrows where the blind spot is, not how big.

## ⟲ Previous-session review

The card before this one recorded a mechanism built because prose failed four
times in one day. This one records why that keeps happening: **every mechanism
built today guards execution, and every failure today was judgement.** The hook
is still worth having — it converts one recurring judgement error into a
mechanical prompt — but it is one route table against a category, not coverage
of it.
