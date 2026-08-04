# 2026-08-04 · hub — how spider-swing's art got consistent: reading the sessions that made it

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · research — transcript archaeology, findings doc + skill

Time: 2026-08-04 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1` (restarted from main post-#712)

💡 Session idea: **the substrate-kit's core discipline — turn every struggle into
a guide the next session can use — transferred intact to a non-Claude agent, and
produced the estate's most consistent artifact set.** The owner's observation,
and it is the finding that outranks everything else here: spider-swing's art
pipeline was never specified by him. A ChatGPT session, working under
kit-derived project instructions, wrote its own art contract, discovered its own
failure mode, invented its own three-scale audit, and committed all of it so the
next session inherited it. That is precisely the kit's loop, executed by a
different provider. The generalisable claim: **the kit's value is not
Claude-specific — it is a working method that any capable agent can run, and its
transfer is now evidenced rather than assumed.**

## previous-session review

`2026-08-04-hub-image-generation-comparison.md` (PR #712, merged) measured four
surfaces on cold prompts and concluded ChatGPT wins on instruction compliance.
That conclusion survives but was **incomplete in its explanation**: it implied
the shipped art's quality came from the model. Reading the sessions that made
the art shows the quality came from a *committed contract plus a serial gate*,
which no cold prompt can reproduce. The correction matters — a session reading
only #712 would try to solve an art problem by writing a better prompt.

## Scope

The owner supplied six shared ChatGPT transcripts from spider-swing's art
production. Read all six via `tools/read_shared_chat.py` (verified path), plus
the spider-swing repo's own source records and the engine's parallax code.
Deliverables: a findings doc, an `image-prompt` local skill built on the
structure the model created for itself, and a paste-ready prompt for the owner.
Not a program step; NOW (E1) untouched.

## What landed

*(written at close)*

## Honest nulls

*(written at close)*

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
