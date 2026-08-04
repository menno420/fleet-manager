---
name: cover-art-prompt
description: "Write generation prompts for COVER ART, key art, app icons, banners and store assets — full-bleed expressive images, no chroma, composition brief with a silhouette read, short in-image text allowed and tested. Loads on top of image-prompt."
---

# cover-art-prompt

The type skill for presentation art: the images that sell or label the game
rather than run inside it. Carries the deltas on top of
[`image-prompt`](../image-prompt/SKILL.md) — read that first; its eight
sections apply, with the exceptions below.

## When this runs

Key art / cover illustration, app icon, store banner or screenshot frame,
title screen, marketing image. The tell: the asset is **full-bleed** — it will
never be keyed to alpha, so the chroma rules do not apply and the composition
rules do the work instead.

## The deltas

1. **No chroma, and the text negative flips.** Full scene edge to edge. Short
   in-image text is *allowed and worth requesting* — it is also the
   calibration signal: a correct 5-letter word ("SWING" carved into rock,
   measured 2026-08-04, rendered correctly in most candidates on two
   surfaces) predicts general capability; garbled text predicts trouble.
   Keep it to ONE short word or title; long text still fails.
2. **Write a composition brief, not a scene description.** The structure that
   measured well: subject + where it sits in frame ("spider small in frame at
   lower center"), framing elements ("gorge walls framing left and right"),
   light source and direction ("warm orange sun low on the horizon, god rays
   through hanging vines"), motion cue ("mid-swing at the lowest point of its
   arc, motion implied by the curve of the thread"), and named materials to
   render ("the translucent silk thread catching sunlight").
3. **Demand the silhouette read explicitly** — "strong silhouette read" in the
   style line — and score it: the measured failure mode was a lovely
   atmospheric scene whose subject dissolved into a backlit blob. If the
   subject doesn't pop at thumbnail size, the image fails regardless of
   beauty.
4. **Per-use geometry:**
   - **Icon:** square, generate ≥1024×1024, subject centered with generous
     margin — platforms mask icons to rounded squares and circles, so nothing
     essential in the outer ~12%. One subject, no text (illegible at icon
     size), high contrast against both light and dark.
   - **Banner / store header:** wide (store-specified aspect), subject
     off-center, title text zone left clear or the title requested in-image.
   - **Key art / cover:** portrait or landscape per target; full composition
     brief.
5. **Surface choice matters more here than anywhere** (measured 2026-08-04):
   expressive single images were the one category where **Gemini** won
   outright — it exceeded the brief in-genre (an unrequested polished title
   treatment). Grok Imagine's 8-per-roll batches suit exploring compositions;
   its per-image video button is the shortest path to an animated title
   screen. Cold-prompt spec work stays ChatGPT's strength.
6. **Character comes from the game's own art.** Attach the real sprite and
   say the key art must depict *this* character — a generic cute-cartoon
   stand-in is the default failure of cover art for a game with established
   assets. (The measured key-art round produced cartoon spiders because the
   calibration prompt asked for cartoon; yours shouldn't.)

## Skeleton (fill the CAPS)

```
Create a piece of USE_TYPE for GAME: COMPOSITION_BRIEF_ONE_SENTENCE.

CHARACTER: depict the attached CHARACTER_SPRITE — same creature, same
markings, same level of detail — not a generic substitute.

COMPOSITION: SUBJECT_PLACEMENT; FRAMING_ELEMENTS; LIGHT_SOURCE_AND_DIRECTION;
MOTION_CUE.

MATERIALS to render correctly: NAMED_MATERIALS.

TEXT: the word "TITLE" rendered as IN_WORLD_TREATMENT — this exact spelling,
once, nowhere else. [Icons: omit this line — no text.]

STYLE: polished 2D game key art, painterly but clean, strong silhouette read.

CANVAS: ASPECT_OR_SIZE. Full-bleed scene, no border, no frame, no watermark,
no UI.
```

## Acceptance questions

1. Thumbnail test: shrink it — does the subject still read as a silhouette?
2. Is the text spelled exactly right (if requested)?
3. Icon only: does anything essential sit in the outer margin that a rounded
   mask would cut?

## Traps

- **Beauty hides the silhouette failure** — score at thumbnail size first,
  full size second.
- **Store specs are facts, not vibes** — look up the exact required
  dimensions/aspect for the target store before generating, and generate at
  or above them (never upscale to meet a spec).
- **An icon is not a shrunken cover** — it needs its own generation with the
  margin rule, not a crop of the key art.
