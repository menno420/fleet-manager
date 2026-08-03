# Gemini — provider capability reference

> **Status:** `living-ledger`
>
> Plans and what actually differs between them, the context ceilings, native
> video and the arithmetic that governs it, Gems, and Deep Research. All vendor
> facts fetched from Google-owned pages on 2026-08-03. **Not a routing table** —
> see [`README.md`](README.md).

## What this provider is good at, concretely

**Native multimodality, and video in particular.** Video, images, audio and text
go through one system — no frame-extraction step, no transcription hop. Measured
in this estate: ten gameplay screen recordings read in seconds, with every
checkable distance exactly right when a session verified them against its own
hand-read measurements. The comparison point is an afternoon of work — 693
extracted frames — to obtain the same eight numbers.

That is the capability worth reaching for here. The rest of this document is
mostly about the ceilings around it.

## Plans

Fetched from [gemini.google/subscriptions](https://gemini.google/subscriptions/)
and [Google AI plans](https://one.google.com/about/google-ai-plans/):

| | Free | AI Plus | AI Pro | AI Ultra |
|---|---|---|---|---|
| Price | $0 | $4.99/mo | $19.99/mo | $99.99 or $199.99/mo |
| **Context window** | **32k** | **128k** | **1M** | **1M** |
| Usage limits | standard | 2× | 4× | 5× or 20× above Pro |
| Storage | 15 GB | 400 GB | 5 TB | from 20 TB |
| Models | 3.6 Flash + "varying access to 3.1 Pro" | + higher Pro access | "Higher access to Gemini 3 Pro" | "Highest access" |
| Exclusive | — | — | — | Deep Think, Gemini Spark, Project Genie |

Context windows from
[Gemini Apps limits & upgrades](https://support.google.com/gemini/answer/16275805).
Limits refresh on a 5-hour rolling window under a weekly cap. Free, Plus and Pro
all reach Flash-Lite and Flash; paid tiers unlock higher access to Pro.

**Third-party figures conflict** — aggregators carried AI Plus at $7.99, AI Pro
storage at 2 TB, and AI Ultra at $249.99, all disagreeing with the Google-owned
pages. Regional and promotional pricing is in play. Read your own plan page.

## The context window is the only capability difference that matters here

For text, 32k versus 1M reads like a quota. For **video** it is a hard ceiling on
how much footage can be in the room at once, because video is expensive per
second.

[Google's video-understanding docs](https://ai.google.dev/gemini-api/docs/video-understanding):
video is sampled at **1 frame per second** and costs **≈300 tokens per second** at
default resolution, ≈100 at low resolution.

| Tier | Context | Video that fits | After instructions, knowledge file and reply |
|---|---|---|---|
| Free | 32 000 | ≈1 min 47 s | roughly **80 seconds** |
| AI Plus | 128 000 | ≈7 min 6 s | roughly **6 minutes** |
| AI Pro / Ultra | 1 000 000 | ≈55 min | roughly **50 minutes** |

The figure cross-checks against Google's own statement that a 1M context holds
*"videos up to 1 hour long at default media resolution"* — 1 000 000 ÷ 3 600 ≈ 278
tokens per second, close enough to the documented ≈300 that the ratio can be
applied downward with confidence.

**Caveat, stated plainly:** those token figures are documented for the **API**.
Whether the consumer app tokenises uploaded video identically is not verified —
the app may downsample more aggressively. The arithmetic inherits that
uncertainty.

**The inference that follows, marked as one:** a batch of ten clips sent to a
32k context is more than ten times over the ceiling, and the failure that came
back has exactly a ceiling's shape — not garbled reading, but broken *attachment*:
correct numbers filed against the wrong clip, a region carried over from the
previous run, several clips collapsed into one vague sentence. Detail survived;
the structure holding detail to its source did not. That was previously read as
attention thinning across a batch. If it is a ceiling instead, it is purchasable
— which is the entire buy/don't-buy question. Full reasoning:
[`../research/2026-08-03-gemini-paid-tiers.md`](../research/2026-08-03-gemini-paid-tiers.md).

**Test before paying: one clip per message on the free tier.** If attribution
comes back clean, the protocol already fixed it.

## Gems

Custom assistants: a name, an instructions field, and knowledge files that load
into every chat with that Gem. Available on the free tier. Up to **ten knowledge
files** per Gem.

The estate's working example is a gameplay-recording reviewer — three paste
blocks (instructions, an on-screen-facts knowledge file derived from source, and
a per-clip message) plus a four-point acceptance test:
[`../research/2026-08-03-gemini-visual-qa-gem.md`](../research/2026-08-03-gemini-visual-qa-gem.md).

Two design points from building it, both non-obvious:

- **Split behaviour from facts.** Instructions carry what to do and never rot;
  the knowledge file carries the facts and gets regenerated when the source
  changes. Putting facts in the instructions field means hand-editing them
  forever.
- **Attach less than you can.** For a Gem whose job is reading pixels, every
  extra document is more surface from which it can answer a question about the
  video with something it *read* instead of something it *saw* — and that failure
  is invisible in the output, because a document-sourced claim reads exactly like
  an observation.

## Deep Research

Available on the free tier with a limited monthly allowance; paid tiers get daily
allowances that scale with the plan.

Same caution as elsewhere: strong on synthesising public sources, and its output
reads uniform whether or not the underlying evidence was actually available.
Spot-check the three most specific claims.

## Other features

- **Deep Think** (Ultra only) — a reasoning mode for hard maths and code. A
  genuine capability difference, and irrelevant to reading a HUD.
- **Gemini Spark, Project Genie** (Ultra only).
- **Image generation** in-chat, and it can analyse images it generated as if you
  had uploaded them.
- **Video generation** (Veo / Flow) is a separate product from video *analysis*.
- **Google Drive.** A pasted Drive share link does **not** work — it is a
  client-rendered app rather than a document a fetcher can read. Upload files
  directly to the chat, or connect Drive as an integration. This is not
  tier-dependent.

## Reading a Gemini chat as evidence

`tools/read_shared_chat.py` reads `share.gemini.google/…` transcripts — verified,
70 426 characters in the measured case. Two things worth knowing: the page
displays a **canonical share URL that may differ from the one you opened** (both
resolve to the same conversation — not a wrong page), and the header carries
`Created with <model>` and `Published <date>`, which is a primary fact about
which model produced the conversation and more reliable than asking it.

Method: [`../conventions/reading-shared-ai-chats.md`](../conventions/reading-shared-ai-chats.md).

## The self-report caution, with a measured instance

Asked in a free-tier session to explain its own tiers — specifically to help
decide whether to pay — the model stated that *"the free tier models retain
support for up to 1 million tokens of context"*. Google's own page says 32 000.
The same answer put AI Pro's storage at 2 TB against the plan page's 5 TB.

Both errors ran in the direction of making the free tier look more capable than
it is. The model was not being evasive; it was reciting a number that is true of
the platform and false of the plan.

**A model's account of its own product is training data, not telemetry** — the
one topic where confidence correlates least with being right, because the answer
changed after training and nothing said so.
