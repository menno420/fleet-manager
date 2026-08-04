# 2026-08-04 · hub — four-surface image-generation comparison, measured on the game's own sprites

> **Status:** `complete`

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

- **`docs/CAPABILITIES.md`** — append-log entry with the full four-surface
  result: ChatGPT 3/3 on technical specs (only surface to obey the enumerated
  leg layout); Gemini Flash style-strong but its anatomy prior overrides
  layout instructions; Grok chat 0/3 on the background spec; Grok Imagine
  standard obeys *layout* specs (three-band parallax with keyed foreground,
  correct "SWING" text) but not background *uniformity*; Imagine quality tier
  compliant nearly every time. All surfaces fail out-of-distribution physics
  poses; small-delta edits succeed where pose-from-scratch fails.
- **`docs/providers/grok.md`** — first estate-measured section in the file:
  chat tab vs Imagine split, the standard/quality recipe, weakness entry
  reframed per the measurement.
- Working recipes recorded: canonical sprites → ChatGPT; variant exploration →
  Imagine standard batch + quality pass; pose changes → edit path, never
  text-to-image.

## Honest nulls

- The quality-tier compliance rate is owner-reported ("nearly every time"),
  not counted; no numeric denominator.
- Horizontal tiling of the parallax bands is untested — thumbnails cannot show
  seams; flagged to the owner as the pick-time check.
- Gemini and ChatGPT were not re-run through their own dedicated
  quality/upscale paths; the comparison is chat-surface vs chat-surface plus
  Grok's Imagine — the one asymmetry in the design.
- All scoring is against one reference sprite (Garden Spider); a different art
  style could reorder the ranking.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
