# Reading a screen recording

> **Status:** `reference` · measured 2026-08-06
>
> The owner sends screen recordings to show what a session did, what a bot
> rendered, or what a UI looks like on his phone. They are usually **fast
> scrolls**, and that makes sampling rate — not legibility — the thing that
> decides whether you actually read them.

## The one fact that governs everything

**Gemini does not watch video. It samples frames, at 1 fps by default.**

A 6.6-second recording becomes **7 stills**. If the content scrolled faster than
one viewport per second — which a thumb-flick always does — most of it is never
delivered to the model at all. Nothing in the reply will look wrong; it will
simply be a confident transcription of the 63 % that arrived.

`docs/CAPABILITIES.md` § CAN says video is readable, and it is. This document is
the part that says **how much** of it you read.

## The recipe

Vertex accepts video inline up to ~20 MB base64 and exposes a per-part sampling
override. Both matter:

```python
part = {"inlineData": {"mimeType": "video/mp4", "data": b64}}
part["videoMetadata"] = {"fps": 8}          # <-- the whole point
```

`POST https://aiplatform.googleapis.com/v1/projects/{p}/locations/global/publishers/google/models/gemini-3.1-pro-preview:generateContent`

Vertex, not AI Studio — the owner's 2026-08-05 directive
([`vertex-first-for-gemini.md`](vertex-first-for-gemini.md)). Working script:
`tools/read_screen_recording.py`.

**Start at `fps: 8` for any scroll.** Measured on a real 6.65 s phone capture
whose unique content spanned 11 viewport-heights:

| sampling | frames | content seen |
|---|---|---|
| 1 fps — **the default** | 7 | **63 %** |
| 2 fps | 14 | 83 % |
| 4 fps | 27 | 98 % |
| **8 fps** | 53 | **100 %** |

Cost of the override on that clip: **518 → 3,273 prompt tokens.** It is not
worth optimising; raise the rate.

## Ask the model to report its own coverage

The most useful thing measured on 2026-08-06 was not the coverage number — it
was that **Gemini volunteers its own limitation when asked.** At default it
answered:

> *"I observed 7 distinct scroll positions… there are clear gaps in the
> narrative and context between each frame… I believe I only saw samples of the
> conversation, not the whole thing."*

So end every recording prompt with a coverage question:

> *"How many distinct scroll positions did you actually observe, and do
> consecutive positions overlap or are there gaps? Do not guess at text you
> could not read — write [unreadable]."*

That converts a silent 63 % into a stated 63 %, which is the difference between
a usable answer and a confident wrong one.

## Reading it yourself

Legibility is not the constraint — a 480×1040 phone capture reads perfectly
frame by frame. Two things to know:

- **`ffmpeg` is not installed in this container.** It is one line away and needs
  no root: `pip install imageio-ffmpeg`, then
  `python3 -c "import imageio_ffmpeg;print(imageio_ffmpeg.get_ffmpeg_exe())"`.
- Extract with `-vf fps=8`; scene-change selection
  (`select='gt(scene,N)'`) is unreliable on a scroll, because a scroll is a
  continuous change rather than a cut.

Reading frames yourself costs one image read each. Delegating the whole clip to
Gemini costs one call. **Delegate unless you need to quote exact pixels.**

## The trap that nearly shipped a wrong answer

Measuring "did I skip content?" by row-profile correlation between consecutive
frames **cannot detect a displacement larger than the band it compares.** Asked
about 1 fps samples that had jumped ~2,500 px, a 570 px comparison band returned
a bounded, plausible-looking 369 px — not an error, a *measurement*, and a wrong
one.

It was caught only because the number contradicted Gemini's own report and the
arithmetic. If you need the real displacement across sparse samples, **chain the
dense ones**: measure step-by-step at 8 fps and sum, then take
`max(position) - min(position)` for the net range — a scroll that doubles back
travels far further than it covers (measured: 11,466 px travelled, 6,256 px
covered).

## Honest nulls

- **`fps` above 8 is untested here.** 8 was sufficient for a fast thumb-scroll
  on a 1040 px-tall screen; a faster flick or a taller viewport may need more.
- **The 20 MB inline ceiling is from the API contract, not measured** — the
  largest clip actually sent through this path was 7.3 MB.
- **Audio was not tested.** These were silent screen captures.
