# Gemini — provider capability reference

> **Status:** `living-ledger`
>
> Plans, the context ceilings, native video and the arithmetic that governs it,
> the agentic surfaces, Gems, and Deep Research. Vendor facts from Google-owned
> pages; **feature coverage re-derived 2026-08-04 from the official
> [Gemini Apps release notes](https://gemini.google/release-notes/)** after the
> first version was found incomplete and, on Drive, backwards.
> **Not a routing table** — see [`README.md`](README.md).

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

**Gemini 3.6 Flash** went to *"all Gemini app users globally"* on **2026-07-21**,
selectable from the model drop-down — which is why an owner-shared transcript
carries `Created with Flash`. **Gemini 3 Deep Think** received a major upgrade
(2026-02-19) and remains Ultra-tier.

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

## The API side — pricing and the data-use split

*Source: [Google's Gemini API pricing page](https://ai.google.dev/gemini-api/docs/pricing),
fetched 2026-08-04.* The app facts above are consumer-surface; the API is its
own ladder, per 1M tokens:

| Model | In | Out | Batch/Flex | Priority |
|---|---|---|---|---|
| `gemini-3.6-flash` | $1.50 | **$7.50** | 50% off | 1.8× |
| `gemini-3.5-flash` | $1.50 | $9.00 | 50% off | 1.8× |
| `gemini-3.5-flash-lite` | $0.30 | $2.50 | 50% off | 1.8× |
| `gemini-3.1-flash-lite` | $0.25 ($0.50 audio) | $1.50 | 50% off | — |

(3.1 Pro pricing was not in the fetched table — null, check the page.) Worth a
beat: the newer 3.6 Flash is *cheaper* on output than 3.5 Flash.

**The data-use split, verbatim from the pricing page:** free tier — *"content
used to improve our products"*; paid tier — *"content **not** used to improve
our products."* On the free API tier, prompts are training data. That is a
capability fact about what the free tier *is*, not a warning label.

## Calling it from a session — measured 2026-08-05

A free API key reaches **50 models**, including `gemini-3.6-flash` at
**1,048,576 in / 65,536 out**, at no cost. That makes Gemini the estate's
delegate for read-heavy work: see
[`../findings/2026-08-05-gemini-delegation.md`](../findings/2026-08-05-gemini-delegation.md)
and `tools/gemini_delegate.py`.

Three ceilings, all measured rather than read off a page:

- **The free tier meters input at 250,000 tokens per minute**, verbatim from a
  429: `limit: 250000, model: gemini-3.6-flash`. The 1M window is a model
  capability; this is the quota. They are different numbers and conflating them
  is the trap.
- **`gemini-3.1-pro-preview` returns 429 on a free key** — Pro is paid-quota.
- **`gemini-2.5-flash` returns 404**: *"no longer available to new users"*. A
  new key cannot reach it regardless of tier.

**What a free key actually serves** (probed 2026-08-05, one call per row):

| Surface | Result |
|---|---|
| Multi-turn chat | works. `generateContent` is stateless (history resent each call); the newer **Interactions API** stores it server-side — see below |
| `google_search` grounding | **429 on a two-token prompt** — not served to a free key |
| `url_context` | works — fetched a raw GitHub URL and quoted its first heading correctly |
| `code_execution` | works — returned fib(40) = 102334155, independently verified |
| `function_declarations` | accepted |
| `systemInstruction` | works |
| Structured output (`responseSchema`) | works, lowercase JSON-schema types |

**The Interactions API keeps state — `generateContent` is the legacy path.**
`POST /v1beta/interactions` is reachable on a free key and accepts
`previous_interaction_id`, so a conversation continues without resending its
history. Measured A/B on `gemini-3.1-flash-lite`: turn 2 carrying the id
answered `4712`; the same question without it answered *"You have not provided
a number for me to remember in this conversation."* Retention is **1 day on
free, 55 days paid** (configurable 7–55), opt-out with `store=false` — which
also disables background execution. Server-side history additionally lets the
implicit cache work across turns.

**The real ceilings, from the owner's AI Studio rate-limit dashboard**
(2026-08-05 — peak usage per model over 28 days):

| Model | RPM | TPM | RPD |
|---|---|---|---|
| Gemini 3.6 Flash | 5 | 250K | **20** |
| Gemini 3.1 / 3.5 Flash Lite | 15 | 250K | **500** |
| Gemini 2.5 Flash | 5 | 250K | 20 |
| Embedding 1 / 2 | 100 | 30K | 1K |
| Live API | unlimited | 65K / 20K | unlimited |
| Map grounding | — | — | 500 |
| Search grounding | — | — | not served |

**Twenty requests per day** on the flagship free model is the binding
constraint — not the token meter. It makes the free tier suited to a few very
large calls rather than many small ones, and it is why the delegation tool
packs each batch to the token ceiling. The lite models are the volume tier at
500/day; they are a fallback, not a downgrade to avoid.

**AI Studio's interface does not spend API quota — while the key stays free.**
Verbatim from the dashboard: *"Usage information displayed is for the API and
does not reflect AI Studio usage, which is offered free of charge (when no API
key is selected)."* Dashboard counters lag: *"Usage data may take up to 15
minutes to update."*

The condition is load-bearing once billing exists. From
[Google's billing FAQ](https://ai.google.dev/gemini-api/docs/billing): *"AI
Studio usage remains free of charge unless users link a paid API key for access
to paid features. Once you link a paid API key as part of a paid project in AI
Studio, you will be charged for AI Studio usage for that key."* The FAQ adds
that projects can be switched between paid and free tiers as needed — so paying
for API access does not have to cost the free Studio surface, but it will if the
paid key is linked there. Exactly what constitutes "linking" is untested here.

**The paid tier is live here (2026-08-05) and it closes the asymmetry.** A
€10 prepay on the billed project takes the model list from 50 to **58** and
makes Pro, Google Search grounding and image generation callable from a
session — the three things the free key refuses. Sessions may spend it without
asking ([D-0011]).

Getting there took three separate fixes, each invisible from the API side and
each legible only on the owner's screen, which is worth knowing before
diagnosing a key that "does not work":

1. **Unrestricted keys stopped working on 2026-06-19.** A key created before
   that date, left unrestricted, returns `API_KEY_INVALID` — never
   `SERVICE_DISABLED`, so it reads like a bad key rather than a policy change.
   Securing the key restores it.
2. **The Google Cloud $300 welcome credit excludes the Gemini API**, verbatim
   from the billing dialog: *"Any remaining $300 welcome credit can still be
   used on eligible Google Cloud products (excluding Gemini API) until it
   expires."* Cloud trial credit will never fund this.
3. **Enabling Cloud billing is not the same as funding the project.** Until a
   prepay balance exists, calls return *"Your prepayment credits are
   depleted"* — and models with no free-tier allowance (Pro, every image model)
   report plain free-tier quota exhaustion instead, which looks like a
   different fault entirely.

**Image generation, measured on the first paid call:**

| | |
|---|---|
| Model | `gemini-3.1-flash-image` |
| Delivery | base64 `inlineData` in the JSON response — decoded straight to disk, no URL or download step |
| Output | 1408×768 **JPEG**, 549 KB |
| Chroma at corner | RGB(6,250,5) — corner-sample keying viable |
| Tokens | 69 in · 1,120 image out |
| Cost | **≈ $0.086** (at $60/1M output tokens); Nano Banana Pro ≈ $0.134 |

Two caveats for game art specifically: it returns **JPEG, not PNG**, so
compression artefacts sit on the chroma edge before `asset-pipeline` ever runs;
and a first attempt rendered the far-side legs as pale translucent shapes rather
than solid limbs. Both are prompt-and-pipeline problems — `sprite-prompt` already
carries the leg-count contract — but neither is fixed yet.

**"Free tier" names two different products.** The AI Studio interface and the
API share a project, a dashboard and a name, and serve different models with
different tools. Measured from both ends on 2026-08-05:

| Capability | Free **API** | Free **AI Studio** |
|---|---|---|
| `gemini-3.1-pro-preview` | 429, paid quota — dashboard row reads `0/0` RPM/TPM/RPD | selected and running |
| Grounding with Google Search | 429 on a two-token prompt | toggled on, returns cited sources |
| Flash-class models | 20/day (3.6) · 500/day (lite) | free, and not charged against API quota |
| Temperature · thinking level · structured output · code execution · function calling | API parameters | UI controls, with a `Get code` export |

So the Studio surface is strictly the more capable of the two while it stays on
a free key — the strongest model plus live web search, at no cost and without
touching the API budget. **The API surface is the automatable one.** That is the
whole basis for how work should divide:

- **Owner, in Studio** — open research questions, anything needing the current
  web, anything wanting the strongest reasoning. Costs nothing here.
- **Sessions, via API** — bulk reads over material already in the repos, where
  the value is volume and every claim gets citation-checked
  (`tools/gemini_delegate.py`). Twenty calls a day, so few and large.

Unmeasured: whether Studio's Pro access carries its own ceiling, and whether its
search grounding is the same implementation as the API's `google_search` tool.

**Billing, for when the free tier stops being enough**
([billing docs](https://ai.google.dev/gemini-api/docs/billing)): Tier 1 needs a
billing account and a $10 prepay; Tier 2 opens at $100 spent + 3 days; Tier 3
at $1,000 + 30 days. The data-use line is the reason to care beyond rate limits
— on paid tiers *"prompts and responses are not used to improve Google
products"*, which is the split already recorded above.

**Two quotas, not one.** `generate_content_free_tier_input_token_count` meters
**250k tokens per minute**; `generate_content_free_tier_requests` is a separate
**per-model daily request cap**. Measured at exhaustion: `gemini-3.6-flash`
returned 429 on the request metric while `gemini-3.5-flash-lite` and
`gemini-3.1-flash-lite` still answered — the lite models are a real fallback,
not a downgrade to avoid.

**On code review** (n=1, `tools/gemini_delegate.py`, pre-commit): three findings,
two real and one fabricated — and the fabrication was ranked **first at high
severity**, asserting that lowercase schema enums break every request in code
that had already completed three runs. The two real ones (a path traversal, a
None-content crash) were genuine defects nobody here had noticed. Read every
item; trust the ranking of none.

**AI Studio's GitHub integration is a different surface with different rules**
(measured the same day): it imports up to 1000 files of one repo, drops the rest
by its own judgement, and can only push to a repo it creates. The sync is
one-way — the workspace snapshot wins, and files it lacks are deleted from the
target. Useful for prototyping an app over a repo; not a code path for work
that must land accurately.

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

## The agentic surfaces — missing from the first version of this document

All four are from Google's own release notes and none appeared in the first
draft, which is a straightforward coverage failure rather than a stale fact.

- **Gemini Agent** (2026-04-15) — *"uses Gemini 3's advanced reasoning and tool
  calling to break up complex tasks into smaller steps… it will use apps like
  Gmail or Calendar, alongside many of the tools in Gemini, like deep research
  capabilities and Canvas"*, plus live web browsing *"to research and take action
  on the web"*.
- **Gemini Spark** (2026-05-19, macOS app 2026-06-30) — a *"24/7 personal AI
  agent"* that *"organizes folders, uses your local files to build documents, and
  handles complex workflows across Google Workspace"*. **AI Ultra only**, English,
  18+, supported countries.
- **Personal Intelligence** (beta) — connects Gmail, Calendar and other apps you
  authorise. *"Connecting your apps is off by default: you choose to turn it on,
  decide exactly which apps to connect, and can turn it off anytime."* AI Pro and
  AI Ultra, US, web/Android/iOS; not on Workspace business or education plans.
- **Daily Brief** — a personalised daily overview built on Personal Intelligence,
  distilling priorities from connected apps into "Top of Mind" and "Look Ahead".
- **Scheduled actions** — AI Pro and Ultra, plus qualifying Workspace plans.

Also worth knowing: **the macOS app** (2026-07-29) adds press-and-hold voice
dictation into any window, with optional screen-context reasoning — highlight
text to rewrite, select local files to extract from, generate images in place.

## Deep Research

Available on the free tier with a limited monthly allowance; paid tiers get daily
allowances that scale with the plan.

**It takes your own files as sources** — *"you can now upload your own files and
images to use as a source in Deep Research reports"* — and reports can be
transformed **in Canvas** into interactive visuals and quizzes. The first version
of this document omitted both.

Same caution as elsewhere: strong on synthesising public sources, and its output
reads uniform whether or not the underlying evidence was actually available.
Spot-check the three most specific claims.

## Other features

- **Deep Think** (Ultra only) — a reasoning mode for hard maths and code. A
  genuine capability difference, and irrelevant to reading a HUD.
- **Gemini Spark, Project Genie** (Ultra only).
- **Image generation** in-chat, and it can analyse images it generated as if you
  had uploaded them.
- **Video generation is in-app now.** **Gemini Omni** *"helps you create and edit
  videos as easily as having a conversation… blend any combination of text,
  photos, and video"*, including a custom AI avatar. Separately, responses can
  include **Video Overviews** — generated narrated 30–60 second explainers — and
  interactive multi-layer images, on the Pro model for specific topics. The
  earlier note here that video generation was "a separate product" (Veo/Flow) is
  out of date.
- **Google Drive and Workspace — a strength, not a gap.** Earlier text here
  framed this backwards. Gemini's Drive/Workspace access is **native**: the
  Productivity Planner Gem *"seamlessly brings together information from your
  favorite productivity apps like Gmail, Calendar, and Drive"*; **Personal
  Intelligence** connects apps you authorise (off by default, you pick which);
  and **Gemini Agent** *"will use apps like Gmail or Calendar"* as part of
  completing a task. Gems themselves are shareable, and *"sharing Gems works just
  like sharing files in Google Drive"*.

  What does **not** work is pasting a Drive **URL** into a chat and expecting it
  to be fetched — that is a link-fetching limit, not a Drive limit, and the fix
  is `@Google Drive` or a direct upload. Filing that under "Drive doesn't work"
  was a framing error, and the distinction matters: this is one of the provider's
  genuine advantages.

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
