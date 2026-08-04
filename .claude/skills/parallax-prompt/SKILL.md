---
name: parallax-prompt
description: "Write generation prompts for PARALLAX BACKGROUND layers and wall/rail materials — one layer per generation call, far layer opaque, mid/near layers on chroma, tiling only where the renderer needs it. Use for backdrops, environment layers, ceiling/floor strips; loads on top of image-prompt."
---

# parallax-prompt

The type skill for layered backgrounds: multiple images that the engine
scrolls at different speeds to fake depth. Carries the deltas on top of
[`image-prompt`](../image-prompt/SKILL.md) — read that first; its eight
sections and hard rules all apply.

## When this runs

A new zone/biome backdrop, an extra depth layer for an existing zone, or a
ceiling/floor/rail material strip. The shipped reference shape (spider-swing,
measured from the committed assets): **three separate files** —
`*-backdrop-far` (opaque, 1280×720), `*-backdrop-mid` and `*-backdrop-near`
(1280×720 with real alpha), plus long strips like `*-ceiling-wall` (2048×192)
and rail tiles.

## The deltas

1. **One layer = one generation call.** Never ask one image to contain the
   layer stack. On an integrated surface, run one call per layer with a shared
   style block. On a plain chat (exploration only), the **band-strip
   workaround** applies: one wide image in 3 labelled horizontal bands with
   divider lines — good for judging a look, never a master; each band was
   sliced from a composite, which the hard rules class as upscaling.
2. **Per-layer background spec differs — this is the part sessions get
   wrong:**
   - **FAR layer: fully opaque, no chroma.** It is the backplate; asking for
     chroma wastes the sky.
   - **MID and NEAR layers: subject on a flat chroma field** (magenta
     `#FF00FF` default — forest greens collide with a green key), keyed to
     alpha in the pipeline.
3. **Check the renderer before demanding seamless tiling.** Measured:
   spider-swing draws backdrops with **every second tile mirrored**
   (`SwingLabView`), so backdrop edges never need to match — requiring
   seamlessness there costs composition for nothing. Purpose-built **rail/wall
   tiles DO need it** ("left and right edges carry matching structure for
   repetition"). Ask which kind you are making; the answer changes the prompt.
4. **Depth is written as detail contrast, not just distance words.** Far: low
   detail, atmospheric haze, muted palette. Mid: medium detail, same palette
   slightly darker. Near: large bold silhouettes, darkest, meant to read at
   the fastest scroll. One light direction across all layers, stated in each
   prompt.
5. **The centre stays open.** Gameplay lives mid-screen; the accepted far
   layer in the source sessions passed because *"its centre remains open
   enough for gameplay"*. Foreground interest belongs at the frame's edges
   (the shipped near layer is leaves/branches framing all four corners).
6. **Standing negatives, plus the parallax-specific one:** no focal-point
   object, no horizon break unless the zone has one, and nothing that reads as
   a platform, anchor, or route — *"decorative geometry must not falsely imply
   collision."*

## Per-layer skeleton (fill the CAPS; repeat per layer with the same STYLE block)

```
Create the LAYER_NAME parallax layer for ZONE in GAME — one layer of a
three-layer scrolling background.

STYLE (identical for every layer of this zone): painterly naturalistic
fantasy, PALETTE_WORDS, light from LIGHT_DIRECTION, matching the attached
reference layer from the existing game.

THIS LAYER: [far] distant SUBJECT silhouettes, low detail, atmospheric haze,
fully opaque edge-to-edge scene, no chroma.
  — or —
[mid/near] SUBJECT shapes only — large, bold, DETAIL_LEVEL — everything that
is not SUBJECT must be solid uniform #FF00FF magenta, no gradient, no glow,
no cast shadow.

COMPOSITION: interest at the left and right edges and the top/bottom rim; the
central band stays open for gameplay. No focal-point object, no creature, no
text, no UI, no frame, and nothing that looks like a platform or anchor.

CANVAS: WIDTHxHEIGHT or larger, same aspect.

One image, this layer only.
```

## Acceptance questions

1. Far layer: does the centre stay visually quiet enough to play in front of?
2. Mid/near: is the magenta uniform edge-to-edge (no gradient/glow), and does
   nothing in the layer read as a platform or anchor?
3. All layers side by side: one palette, one light direction?

Then pipeline per mid/near layer: key by corner sample → despill at full
resolution → downscale to runtime → three-scale fringe check. For a rail/wall
tile only: butt two copies edge-to-edge and scroll the seam.

## Traps

- **The band-strip image is a concept, never a master** — regenerate each
  chosen band as its own full call before shipping.
- **A pretty far layer that fails is usually a recolour** — the source
  sessions' bar: it must read as a different *space*, "not the same scene
  under a green filter."
- **Magenta near-layer subjects with pink/warm fibres** (silk, blossom) need
  the green key instead — palette collision is the one reason to switch.
