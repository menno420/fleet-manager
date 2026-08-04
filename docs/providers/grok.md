# Grok (xAI) — provider capability reference

> **Status:** `living-ledger`
>
> Models at model granularity, the generation stack (image/video/voice), search
> tools, and retirements. **Derived 2026-08-04 from xAI's own docs
> ([docs.x.ai](https://docs.x.ai/developers/models)), including its release
> notes and per-model pages** — the `x.ai` news domain itself 403s from this
> environment (Cloudflare), so announcement-post dates below marked
> *snippet-sourced* are unconfirmed against the primary page.
> **Not a routing table** — see [`README.md`](README.md).

## Text models

*Source: vendor docs (models + pricing pages and per-model pages, fetched
2026-08-04).* Prices double for prompts ≥200k tokens (vendor rule: the higher
rate then applies *"for all tokens in the request"*).

| Model ID | Context | $/1M in | $/1M out | Reasoning | Notes |
|---|---|---|---|---|---|
| `grok-4.5` | 500k | $2.00 | $6.00 | effort low/medium/high, **default high, cannot be disabled** | Frontier. Cutoff 2026-02-01. Released July 2026 |
| `grok-4.3` | 1M | $1.25 | $2.50 | four levels incl. **`none`** | The workhorse; `grok-latest` points here. 20% batch discount |
| `grok-4.20-0309` (reasoning / non-reasoning) | 1M | $1.25 | $2.50 | split into two IDs | Released March 2026 |
| `grok-4.20-multi-agent-0309` (beta) | 1M | $1.25 | $2.50 | effort **controls agent count (4 or 16)** | A genuinely unusual knob |
| `grok-build-0.1` | 256k | $1.00 | $2.00 | yes | Coding model, early access; `grok-code-fast-1` now aliases here |

All are text+image in → text out, with structured outputs (`json_schema`,
guaranteed conformance; tool-call args implicitly `strict`) and function
calling. **Max output tokens are published for no model** — honest null;
only the `max_output_tokens` request parameter is documented.

Model-level notes:

- **Alias scheme:** `<name>` → latest stable, `<name>-latest`, `<name>-<date>`
  pinned. `grok-4.5` is also `grok-build-latest` (default model of the Grok
  Build coding agent).
- **Reasoning quirks:** `presencePenalty`, `frequencyPenalty` and `stop` are
  rejected with reasoning models; `logprobs` unsupported on `grok-4.20` and
  newer. Encrypted reasoning content is available via
  `include: ["reasoning.encrypted_content"]`.
- **The Responses API is primary; Chat Completions is deprecated** (still
  served). Batch API gives 20% off listed models; Priority Processing bills 2×;
  prompt caching ($0.20–0.30/1M cached) and context compaction exist.
- **Knowledge is stale by design:** the vendor's own line — *"Grok has no
  knowledge of current events"* without the server-side **Web Search / X
  Search** tools. X Search does *"keyword search, semantic search, user search,
  and thread fetch on X"* — the one integration no other provider has. Tools
  bill per call ($5/1k for web, X, code execution).

## The generation stack — where this provider is strong

*Source: vendor docs (pricing + per-model pages).* Image, video and voice are
first-class API products, not add-ons:

- **`grok-imagine-image`** $0.02/image, `-quality` $0.05/image (1K/2K).
- **`grok-imagine-video`** $0.05/sec; **`grok-imagine-video-1.5`** $0.08/sec —
  text-to-video, image-to-video and reference-to-video *"including optional
  preset voices"*, native 1080p (release notes, July 2026). No duration caps
  published — null.
- **Voice:** `grok-voice-think-fast-1.0` ($3/hr) and `-2.0` ($4.80/hr;
  `grok-voice-latest` routes here from **2026-08-05**); speech-to-text $0.10/hr
  (REST), 25 languages; text-to-speech $15/1M characters.
- Vision input on chat models: jpg/png, 20MiB per image, *"no limit"* on count.

## Surfaces

*Source: vendor docs; consumer docs do not map surfaces to model IDs (null).*

- **grok.com + iOS/Android apps** — chat, Imagine, voice, file uploads,
  connectors. Plans: free tier, SuperGrok, SuperGrok Heavy. Which API models
  serve them is not published.
- **X integration** — a "Grok 4.5 on iOS, Android, Web, and X" news post exists
  (*snippet-sourced*; the page 403s from here).
- **API** — everything above; grok-4.5 also ships as the default in **Grok
  Build** (xAI's coding agent, open-sourced July 2026 per snippet), in Cursor,
  in Office add-ins, and via gateways (OpenRouter, Vercel, Cloudflare,
  Snowflake, Databricks).
- Docs oddity, recorded verbatim: docs.x.ai pages currently brand the company
  *"SpaceXAI"* in titles while API and console remain x.ai.

## Retirements

*Source: vendor migration page.* Effective **2026-05-15**, already past:
`grok-4-1-fast-*`, `grok-4-fast-*`, `grok-4-0709`, `grok-code-fast-1`,
`grok-3`, `grok-imagine-image-pro` — but **the slugs still resolve**, silently
redirecting to `grok-4.3` (at its pricing, with mapped effort),
`grok-build-0.1`, or `grok-imagine-image-quality`. A pipeline pinned to a
retired slug keeps working while quietly running a different model — worth
knowing before comparing any pre/post-May outputs.

## Measured here — the chat tab and Imagine are different capabilities

*Source: measured 2026-08-04, owner-run sprite tests scored against
spider-swing's own reference art; full entry in
[`../CAPABILITIES.md`](../CAPABILITIES.md).*

- **Grok chat (Vraag) is the wrong surface for image work**: three rounds,
  three misses on the one hard technical spec (a `#00FF00` keyable
  background), plus invented elements.
- **Imagine standard tier**: excellent painterly style match and 8+ candidates
  per roll — but every candidate carried a forbidden cast shadow on
  non-compliant green.
- **Imagine quality tier ("Kwaliteit verbeteren") fixed compliance in one
  step** — correct background, no shadows, nearly every time. Consistent with
  the vendor fact above that standard and quality are different models.
- Working recipe: batch-explore on standard, quality-pass the pick. Judge this
  provider's image capability only from Imagine, never from the chat tab.

## Weaknesses — relative, not absolute

Graded per [`README.md`](README.md): worse at, not incapable of.

- **No published max-output figures and snippet-only announcement dates** make
  precise budget planning harder than on providers with full spec tables. Not a
  limitation — measure with a probe call.
- **grok-4.5's 500k context is the smallest current-flagship window in this
  set** (others are 1M+). Steer: `grok-4.3` on the same API carries 1M.
- **Chat-surface image requests** (measured above): weak instruction
  compliance. Not a limitation — the same subscription's Imagine quality tier
  complies; use that surface.

## Honest nulls

- Max output tokens, per model — published nowhere on the fetched docs.
- Which models serve grok.com and the X app.
- x.ai news-post dates (domain 403s from this environment; docs release notes
  give months only, and `grok-4.3`'s release date appears nowhere fetched).
- Voice model pages state modalities *"text → text"* for speech-to-speech
  models — recorded verbatim, likely a docs artifact.
- Nothing here is measured in this estate yet.
