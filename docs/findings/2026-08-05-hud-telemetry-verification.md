# Verifying generated and captured video with the game's own telemetry

> **Status:** `reference`
>
> How a collision-detection problem that defeated both a model and a session got
> solved by changing the question — and the rule that generalises from it.

## Provenance

All figures **measured** 2026-08-05 in this container: three `gemini-3.1-pro`
runs over one 86-second gameplay recording, plus arithmetic on their output.
The ground truth is two frames the owner supplied from his own eye.

## The failure

A 30-second trailer was cut from real gameplay. Asked *"find every moment where
the spider collides with something"*, Gemini reviewed the whole cut and returned:

```json
{ "collisions": [] }
```

The owner then supplied two exact frames — trailer 0:06 and 0:11 — showing the
spider stalled against thorns. The session could not resolve them either: at
1040×480 the sprite is roughly twelve pixels and a scrape is indistinguishable
from a near miss in a still.

**Neither party was lying and neither was careless.** The signal was below the
resolution of the question being asked.

## The fix — the owner's mechanism, refined by the data

The owner named it: *"a collision triggers the one life and basically moves you
backwards a little bit, or at least stalls, so one thing to ask is: is there any
frame where the distance went down or remained the same instead of increasing."*

The game prints distance in the HUD every frame. So the question became
**read the number**, not **judge the picture**:

> Read the distance number at roughly one-second intervals through the whole
> clip. Report every interval where the distance failed to increase. Report the
> numbers you actually read; if you cannot read a value, omit that timestamp
> rather than guessing.

The refinement the data forced: distance **never decreases** on a collision. The
run continues; it loses about a second of momentum.

| interval | gain |
|---|---|
| 50→51s | 87.5 m |
| 51→52s | 75.8 m |
| **52→53s** | **42.2 m — 59% of median** |
| 53→54s | 75.1 m |

Median gain **71.4 m/s**. Exactly three intervals in 86 seconds fall below 60%
of median: the counter initialising (t=0), **the owner's collision**, and the
run ending. His screenshot read **3693.2 m**, sitting between the 52s reading
(3658.6) and the 53s reading (3700.8).

So the detector is not *"did distance decrease"* but *"did the gain drop below
~60% of the local median"*.

## The rule

> **Give the model a reading task, not a judging task — then do the maths
> yourself.**

Reading text off a frame is something these models do reliably; judging whether
two sprites touched is not. The same footage, the same model, the same budget
produced a useless null and a precise hit depending only on which was asked.

It also generalises past video: prefer questions whose answers are *checkable
values* over questions whose answers are *verdicts*. A value can be verified
arithmetically. A verdict can only be trusted.

## On multi-model quorum

The natural response to a wrong answer is to ask several models and believe the
majority. That works against one failure mode and not the other:

- **Fabrication** — models invent *differently*, so agreement is real evidence.
  Two-of-three would have caught every fabricated citation and timestamp
  recorded in this estate.
- **Blindness** — models fail *identically* when the signal is below the
  resolution they all share. Three models reporting no collisions would have
  given three times the confidence and zero times the information.

> **Quorum for claims of presence. Instrumentation for claims of absence.**

## What agreement did establish

Asked to read the numbers, three independent runs returned **86 of 86
timestamps identical to the decimal**. That is consistent with genuine
legibility — and also with server-side determinism, which this session cannot
distinguish. Treat it as encouraging rather than as proof.

## Not established

- Local OCR was **worse** than asking the model: tesseract on the cropped
  readout returned `62090.75` for a frame reading ~2800 m. Abandoned.
- The 60% threshold is fitted to **one clip with one collision**.
- `tools/clean_run_windows.py` — reading distance per second, computing gains,
  and emitting collision-free windows for trailer cutting — is **not built**.
