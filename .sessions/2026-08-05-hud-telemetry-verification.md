# 2026-08-05 · hub — the HUD was the instrument

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · research — turn a judgement call into arithmetic

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1`

💡 Session idea: **give a model a reading task, not a judging task.** Asked
"are there collisions in this footage?", Gemini reviewed a 30-second trailer
and reported **zero** — the owner then produced two exact frames. Asked instead
to *read the HUD's distance number once per second*, three independent runs
returned **86/86 identical readings**, and the collision fell out of the
arithmetic. Nothing about the model changed between those two answers; only the
question did. Judging pixels is where it fails silently. Reading text and
letting the caller do the maths is where it is reliable — and the maths is
checkable, which the judgement never was.

## previous-session review

`2026-08-05-video-generation-pipeline.md` (PR #741, merged) shipped the trailer
pipeline with an honest null: collision detection had failed at both ends.
This closes that null with a method.

## What landed

- `docs/findings/2026-08-05-hud-telemetry-verification.md` — the method, the
  measured numbers, and why the quorum idea needed refining.
- `docs/owner-queue.md` — `OQ-SWINGY-NAME`, the store-name availability check.

## Measured

The owner named the mechanism: a collision costs a life and stalls forward
progress, so the distance readout is the tell. Refined by the data — distance
never *decreases* on a collision, it loses about a second of momentum:

| interval | gain |
|---|---|
| 50→51s | 87.5 m |
| 51→52s | 75.8 m |
| **52→53s** | **42.2 m — 59% of median** |
| 53→54s | 75.1 m |

Median gain 71.4 m/s. Three intervals in 86 seconds fall below 60% of median:
the counter initialising, **the owner's collision**, and the run ending. His
screenshot read **3693.2 m**, which sits between the 52s reading (3658.6) and
the 53s reading (3700.8) — the instrument located the event he found by eye.

**The quorum question, answered with a distinction.** Three-model agreement is
real evidence against *fabrication* (independent models do not invent the same
thing) and worthless against *blindness* (correlated failure — three models
agreeing they see nothing at 12 px is three times the confidence and zero times
the information). Rule: **quorum for claims of presence, instrumentation for
claims of absence.**

## Honest nulls

- **Local OCR was worse than asking the model** — tesseract on the cropped
  readout returned `62090.75` for a frame reading ~2800 m. Not pursued; the
  model read it correctly, which I would have bet against.
- The 60%-of-median threshold is fitted to **one clip, one collision**. It
  separates cleanly here and is untested elsewhere.
- Perfect cross-run agreement may indicate genuine legibility **or** server-side
  determinism; this session cannot distinguish them.
- `tools/clean_run_windows.py` is **not built** — the method is proven, the tool
  is the next session's.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
