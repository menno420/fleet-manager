# 2026-08-05 · hub — video generation, end to end

> **Status:** `complete`

- **📊 Model:** opus-5 · high · feature build — a working trailer pipeline and
  the Veo constraints behind it

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1`

💡 Session idea: **prompt depth, not model choice, was the whole variable.**
Four Veo runs, same model, same references, same budget: 70 words produced a
photorealistic nature documentary; ~120 produced a generic mobile game; a
197-word specification produced recognisable Spider Swing art with zero
interface artefacts; +130 words of explicit pendulum physics produced the
actual swing mechanic — accelerate through the low point, release at the apex,
re-fire forward. The first result was recorded here as "Veo can't do game art",
which was a claim about the prompt wearing the costume of a claim about the
tool. The owner pushed back; the correction is the finding.

## previous-session review

`2026-08-05-vertex-live.md` (PR #738, merged) established Vertex. This spends
it: video generation, a delegated highlight pass, and a finished 30-second
trailer.

## What landed

- `docs/providers/gemini.md` — the Veo section: input shapes, the 8-second
  reference constraint, the prompt-depth ladder, and the app-vs-API asymmetry.
- `docs/conventions/owner-drive-folder.md` — the public Drive folder the owner
  uploads recordings to, and how to read it without the Drive API.

## Measured — Veo 3.1 on Vertex, 2026-08-05

| Input shape | Result |
|---|---|
| `image` (first frame) | works |
| `image` + `lastFrame` | works — interpolates between two real frames |
| `referenceImages`, `referenceType: asset` | works, **but only at `durationSeconds: 8`** |
| `referenceImages`, `referenceType: style` | fails at every duration tried: *"does not support this mix of references"* |
| `video` (extension) | accepted; not exercised to completion |

- Model IDs differ by surface: `veo-3.1-fast-generate-001` on Vertex vs
  `…-preview` on AI Studio. Four 404s came from using the wrong family.
- **Submission success ≠ support.** Every rejected shape was accepted by the
  API and failed only when the operation ran. The operation result is the
  instrument.
- All Veo output carries **AAC audio**. This session stripped it with `-an`
  through two ad builds before noticing.
- Vertex returns **PNG** for images where the AI Studio API returns JPEG —
  material for chroma work.

## The trailer pipeline, now repeatable

Read the owner's public Drive folder → download clips → compress → upload to
Gemini → delegate highlight windows → **verify every timestamp against real
clip duration** → cut and assemble with ffmpeg → generated opener + real
gameplay + title card.

Delegation caught 21 candidate windows; **4 pointed past the end of their own
clip** and were dropped mechanically.

## Honest nulls

- **Collision detection failed at both ends.** Gemini reviewed the finished cut
  and reported **zero** collisions; the owner then supplied two exact frames
  (0:06 and 0:11). At 1040×480 the spider is ~12px and a scrape is
  indistinguishable from a near miss in a still — this session could not verify
  the replacement windows either, and the accepted cut rests on the owner's eye.
- The audio bed under the final cut is Veo's generated ambience, **not game
  audio**. Labelled here because it plays under real gameplay.
- `style` references may work in some combination not tried; only "alone, at
  6s and 8s" was tested.
- The trailer is not committed to any repo — it exists as a session artifact.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
