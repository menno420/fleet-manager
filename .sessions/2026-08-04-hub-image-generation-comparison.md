# 2026-08-04 · hub — four-surface image-generation comparison, measured on the game's own sprites

> **Status:** `in-progress`

- **📊 Model:** fable-5 · high · research — score owner-run generation tests, record the findings

Time: 2026-08-04 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1` (restarted from main post-#710)

💡 Session idea: **a provider's chat tab and its dedicated generation surface
can be different models with different obedience — and judging the provider by
the wrong one writes off a capability that was one tab away.** "Grok makes bad
images" was true of the chat surface across three rounds and false of Imagine's
quality tier on the first try. The provider docs already recorded the two-model
split (`grok-imagine-image` vs `-quality`) as a vendor fact; the owner's test
turned it into a measured one. The generalisable form: when a provider fails,
note which *surface* failed before recording the verdict — the unit of
capability is the model serving the surface, not the brand.

## previous-session review

`2026-08-04-hub-provider-refs-deep-research-review.md` (PR #710, merged)
closed on "the five new files are vendor-doc-sourced and estate-unmeasured —
measurement is the natural next pass." This session is that pass arriving
within hours, owner-driven: the same prompts run across four surfaces, scored
against the game's own reference sprite.

## Scope

The owner ran three rounds of identical prompts (sprite-sheet, style-anchored
single pose, enumerated leg placement) across ChatGPT, Gemini Flash, Grok chat
(Vraag/Expert), and finally Grok Imagine (standard + quality), sharing
screenshots and a screen recording. This session authored the prompts, scored
the results against the game's Garden Spider sprite, and records the findings.
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
