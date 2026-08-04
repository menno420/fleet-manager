---
name: sprite-prompt
description: "Write a generation prompt for a character or object SPRITE that must slot into an existing set — canonical camera and layout, enumerated body parts, chroma field, runtime dimensions. Use for spiders, creatures, obstacles, collectibles; loads on top of image-prompt."
---

# sprite-prompt

The type skill for sprites: an isolated subject on a chroma field that must
match a committed set. Carries the deltas on top of
[`image-prompt`](../image-prompt/SKILL.md) — read that first; its eight
sections and hard rules all apply.

## When this runs

A new character, character variant/skin, obstacle, or collectible for a game —
anything that will be keyed to alpha and drawn by the engine among existing
sprites of the same kind.

## The deltas

1. **The set's contract outranks everything in the prompt.** Look it up before
   writing: spider-swing's spiders are **384×181 RGBA**, three-quarter side
   profile facing right, in the committed roster docs. Generate at ≥2× the
   runtime size; the contract governs the downscale target, not the canvas.
2. **Anchor to the set's best member and exclude its identity.** Attach the
   existing sprite; inherit pose, orientation, dimensions, lighting and
   quality bar; explicitly exclude its species/identity traits. This is the
   mechanism that kept five spiders pixel-identical in format while reading as
   five different creatures.
3. **Enumerate the canonical layout by position, and give the checkable
   total.** spider-swing's, verbatim-tested (only enumeration worked; counts
   alone failed):
   - NEAR side: all 4 legs fully visible, spaced left to right as rear,
     back-middle, front-middle, front — each separate, none overlapping.
   - FAR side: only the 2 front-most legs visible past the head and chest.
   - "Total visible legs: exactly 6. Do not draw a 5th near leg. Do not draw a
     3-legged side."
4. **Neutral stance only.** "A character portrait pose, not an action pose."
   Swing/fall/action poses come from in-engine rotation or from a small-delta
   edit of the accepted sprite — never from text-to-image (failed on all four
   surfaces tested).
5. **Chroma by palette:** green `#00FF00` for warm/brown/orange subjects,
   magenta `#FF00FF` for green/pale subjects. State "solid uniform, edge to
   edge, no gradient, no vignette, no glow, no cast shadow, no contact shadow,
   no reflection."

## Skeleton (fill the CAPS)

```
Create one 2D game sprite for GAME.

REFERENCE: the attached EXISTING_SPRITE is the exact style, finish and quality
bar. Inherit its painterly semi-realistic finish, its fur/material rendering,
its three-quarter side camera, its body proportions relative to canvas, and
its lighting direction. Do NOT inherit its species anatomy or its colour
palette — this is a different creature.

SUBJECT: ONE_SENTENCE_IDENTITY.

STYLE: painterly semi-realistic digital art. NOT cartoon, NOT vector, NOT flat
illustration, no graphic outline. Rich texture, convincing natural material
detail, subtle warm rim lighting from the upper left.

PALETTE: SUBJECT_COLOURS.

COMPOSITION AND CAMERA: three-quarter side profile, facing right and slightly
toward the camera, body horizontal, neutral relaxed stance. Head right,
body/abdomen left. Large in frame. A character portrait pose, not an action
pose.

LAYOUT — follow exactly: ENUMERATED_PARTS_AND_CHECKABLE_TOTAL.

BACKGROUND: solid uniform CHROMA_HEX, edge to edge. No gradient, no vignette,
no glow, no cast shadow, no contact shadow, no reflection on the background.

DO NOT INCLUDE: text, letters, numbers, UI, watermark, border, frame, ground
plane, horizon, web, silk, other creatures, or any second object.

FUNCTION: read at roughly GAMEPLAY_PIXELS during fast motion — the silhouette
must stay legible when small and distinguishable from a dark background.

Produce ONE subject only, on a single image. No sprite sheet, no pose grid, no
variants in one image.
```

## Acceptance questions (in this order)

1. Is the chroma edge-to-edge uniform with no shadow under the subject?
2. Does the enumerated total check out (e.g. exactly 6 visible legs)?
3. Squinted small — does the silhouette still read?

Then pipeline: key by corner-pixel sample → **despill at full resolution** →
downscale to the contract size → re-check fringe at runtime and 25% gameplay
scale.

## Traps

- **Sheets kill consistency** — one pose per call, always; four separate
  generations from the same reference match better than one four-pose image.
- **The model's anatomy prior beats your layout on cold prompts** — the anchor
  image is the fix, not more words.
- **A near-miss (one fused leg) is an edit, not a re-roll**: "same image, but
  separate the two overlapping legs into two distinct legs."
