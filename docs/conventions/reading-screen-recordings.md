# Reading a screen recording

> **Status:** `reference` · measured 2026-08-06
>
> The owner sends screen recordings to show what a session did, what a bot
> rendered, or how a UI looks on his phone. They are usually **fast scrolls**,
> and that makes sampling rate — not legibility — the thing that decides whether
> you actually read them.

## The one fact that governs everything

**Gemini does not watch video. It samples frames, at 1 fps by default.**

A 6.6-second recording becomes **7 stills**. Measured on a real phone capture:
at that rate, **5 of the 6 transitions share no content at all** — the reply is
seven disconnected snapshots of a continuous conversation. Nothing in it will
look wrong. It will read as a clean transcript.

`docs/CAPABILITIES.md` § CAN says video is readable, and it is. This document is
the part that says **how much** of it you read.

## The recipe

Vertex accepts video inline up to ~20 MB base64 and exposes a per-part sampling
override. Both matter:

```python
part = {"inlineData": {"mimeType": "video/mp4", "data": b64}}
part["videoMetadata"] = {"fps": 16}         # <-- the whole point
```

`POST https://aiplatform.googleapis.com/v1/projects/{p}/locations/global/publishers/google/models/gemini-3.1-pro-preview:generateContent`

Vertex, not AI Studio — the owner's 2026-08-05 directive
([`vertex-first-for-gemini.md`](vertex-first-for-gemini.md)). Working script:
`tools/read_screen_recording.py`.

**Start at `fps: 16` for a thumb-scroll.** Measured on a 6.65 s / 480×1040
capture, counting pairs of consecutive frames that share **no** content — which
is what a gap actually is:

| sampling | frames | consecutive pairs | pairs with **no shared content** |
|---|---|---|---|
| 1 fps — **the default** | 7 | 6 | **5** |
| 2 fps | 14 | 13 | 11 |
| 4 fps | 27 | 26 | 15 |
| 8 fps | 53 | 52 | 5 |
| **16 fps** | 106 | 105 | **0 — complete** |

Cost: **518 → 3 273 → 6 462** prompt tokens at 1 / 8 / 16 fps. Coverage is worth
far more than the tokens; raise the rate rather than tuning it.

**8 fps is not enough for a fast scroll** — it looks close (5 gaps of 52) and is
not. That intermediate result was published in an earlier revision of this
document as "100 % coverage" and was wrong; see the traps below.

## Ask the model to report its own coverage

The most useful property measured on 2026-08-06 is that **Gemini volunteers its
own limitation when asked.** At default sampling, unled:

> *"I observed 7 distinct scroll positions… there are clear gaps in the
> narrative and context between each frame… I believe I only saw samples of the
> conversation, not the whole thing."*

At `fps: 16` on the same clip it reported **14 positions, continuous, no gaps,
one-directional** — all three independently confirmed. So end every recording
prompt with a coverage question:

> *"How many distinct scroll positions did you resolve? Does the text flow
> continuously from one to the next, or are there gaps? Did the scroll ever
> reverse? Do not guess at text you could not read — write [unreadable]."*

That converts a silent gap into a stated one, which is the difference between a
usable answer and a confident wrong one.

## Reading it yourself

Legibility is not the constraint — a 480×1040 phone capture reads perfectly
frame by frame. Two things to know:

- **`ffmpeg` is not installed in this container.** One line, no root:
  `pip install imageio-ffmpeg`, then
  `python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())"`.
- Extract with `-vf fps=16`. Scene-change selection (`select='gt(scene,N)'`) is
  unreliable on a scroll — a scroll is continuous change, not a cut.

Reading frames costs one image read each. Delegating the clip to Gemini costs
one call. **Delegate unless you need to quote exact pixels.**

## The traps — two wrong measurements, one of them published

Both came from the same instinct: measuring *displacement* between frames.
**Don't.** Displacement estimators fail silently on this material.

1. **A correlation search cannot report a shift larger than the window it
   searches.** Given 1 fps samples that had jumped far past the window, it
   returned a bounded, plausible `369 px` — not an error, a *measurement*, and a
   wrong one.
2. **Row-profile correlation aliases on repetitive UI.** A Claude Code
   transcript is full of near-identical rows (`Ran 2 commands >`, `Received a
   GitHub event >`), and the estimator locked onto the wrong period — inventing
   **2 890 px of reverse scrolling that never happened.** That fabrication
   reached a published document and a PR body. **The owner caught it**, from
   knowing what his own thumb did; no check in this estate would have.

**The method that works asks a different question:** *do two consecutive frames
share any content at all?* Take several text bands from frame N, search each
across the whole of frame N+1, and require one strong normalized match. A pair
with no match **is** a gap — no displacement estimate needed, and nothing to
alias. Diagnostic worth keeping: at 8 fps only **9 of 52** pairs yielded a
confident displacement, and all nine were moments the scroll had *paused*. An
estimator that only works when nothing is moving will still emit numbers while
everything is.

## Honest nulls

- **Rates above 16 fps are untested.** 16 gave 0 gaps on this clip; 24 and 32
  were not run to completion.
- **One clip, one device, one app.** The gap counts are exact for this
  recording and indicative for others — a faster flick or a taller viewport may
  need more.
- **The ~20 MB inline ceiling is from the API contract, not measured** — the
  largest clip actually sent through this path was 7.3 MB.
- **Audio untested** — both clips were silent screen captures.
