---
name: asset-pipeline
description: "Turn a delivered generated image into an engine-ready asset: key by corner sample, despill at full resolution, downscale to the contract size, three-scale fringe audit, source-record entry. Use whenever a generated image is accepted and needs to become a runtime file."
---

# asset-pipeline

The post-generation half of every art delivery. The prompt skills
(`image-prompt` family) end where this begins: an accepted image exists and
must become a committed runtime asset with provenance. Every step below is
measured (`tools/chroma_spill_probe.py`, spider-swing's 32/33 zero-fringe
audit) — do them in this order.

## When this runs

An image from any generator has passed its acceptance question and should
enter a repo as a runtime asset. Also when an existing keyed asset shows halo
or fringe in-engine — the fix is a pipeline re-run, not a regeneration.

## Inputs to establish first

1. **The contract size** — from the set's committed docs (spider-swing
   sprites: 384×181; backdrops: 1280×720). Never from the source image.
2. **Whether the asset is keyed at all** — cover art and far backdrops are
   full-bleed: skip keying entirely, go to step 4.
3. **Where the file arrives.** Conversation image uploads are vision-only
   (measured 2026-08-04, `docs/CAPABILITIES.md`) — for programmatic work the
   file must arrive via repo commit, URL, or a container the surface uploads
   as a file.

## The steps

**1. Key by corner sample — never by the hex you asked for.** Measured:
generated "green" fields land near `#22C022` / `#3E8E3E`, never `#00FF00`.

```python
from PIL import Image
import numpy as np
img = np.asarray(Image.open(SRC).convert("RGB")).astype(np.int16)
key = img[2, 2].copy()                      # sample the actual field
dist = np.abs(img - key).sum(axis=2)
alpha = np.clip((dist - 30) * (255 / 90), 0, 255).astype(np.uint8)  # soft matte
```

Check the sample: all four corners should agree within tolerance; if they
don't, the field has a gradient — flag it, don't guess.

**2. Despill at full resolution — the step everything depends on.** Semi-
transparent edge pixels carry ≈+100 key-colour excess at every scale; the
clamp removes it entirely:

```python
r, g, b = img[:,:,0], img[:,:,1], img[:,:,2]
g = np.minimum(g, np.maximum(r, b))          # green key; swap channels for magenta
rgba = np.dstack([r, g, b, alpha]).astype(np.uint8)
```

(For a magenta key, clamp R and B against G-anchored caps instead —
`r = np.minimum(r, np.maximum(g, b))`, same for `b`.)

**3. Downscale to the contract size** with a proper filter (LANCZOS). Never
upscale; if the source is smaller than the contract, regenerate larger.

**4. Audit at three scales — a check, not a repair.** Source, runtime, and
25% gameplay scale; count key-coloured pixels among partial-alpha pixels. The
committed bar is **zero**. If fringe appears here, step 2 was skipped or the
key sample was wrong — go back, don't hand-paint.

```python
def fringe(rgba):                            # green variant
    a = np.asarray(rgba).astype(np.int16)
    semi = (a[:,:,3] > 8) & (a[:,:,3] < 248)
    gx = (a[:,:,1] - np.maximum(a[:,:,0], a[:,:,2]))[semi]
    return int((gx > 15).sum())
```

**5. Write the source record.** Per spider-swing's convention
(`assets/source/*/README.md`): the generation prompt (or prompt family), the
chroma choice and why, source SHA-256, runtime path + SHA-256, and the
audit result. Full generation canvases are hash-recorded, not committed —
the repo versions runtime files plus provenance.

**6. Verify in-engine** (or the closest available proxy — spider-swing's
phone-scale composite from exact runtime textures). Local green is not
device green; say which proxy was used.

## Acceptance question for the owner

One question, per delivery: *"any coloured fringe around the edges — including
at gameplay size?"* This question, asked every time, is the likeliest cause of
the estate's 32/33 zero-fringe record.

## Traps

- **Clean at source predicts nothing at runtime.** The fringe is proportional
  — it *grows* as a share of the sprite when you shrink. Audit all three
  scales, always.
- **A baked checkerboard is not alpha.** If the generator "helpfully" removed
  the background itself, the checkerboard is pixels; re-request on a flat
  chroma field.
- **Don't hand-repair fringe in an editor** — a wrong key sample or skipped
  despill fixed at the source costs one re-run; hand-painted edges cost every
  future re-export.
- **The engine may draw over your clean asset** — measured in the source
  sessions: "faint outlines" were renderer debug polygons, not PNG defects.
  Check the renderer before blaming the pipeline.
