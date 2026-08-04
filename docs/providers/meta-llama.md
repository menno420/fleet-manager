# Meta (Llama / Muse) — provider capability reference

> **Status:** `living-ledger`
>
> The open-weights Llama generations, the license that governs them, and the
> 2026 pivot to Muse. **Derived 2026-08-04 from Meta's own blog
> ([ai.meta.com/blog](https://ai.meta.com/blog/)), the official `meta-llama`
> Hugging Face model cards, and the `meta-llama/llama-models` GitHub repo**
> (the license's canonical home). A reachability finding up front: **every
> `llama.com` URL 301s to `developer.meta.com`, whose pages are client-rendered
> shells serving no content to a fetcher** — the docs behind them need a
> browser (`tools/read_shared_chat.py`'s headless-Chromium path would apply).
> **Not a routing table** — see [`README.md`](README.md).

## The 2026 picture — read this before the tables

*Source: Meta's own blog posts.* Meta's flagship is no longer Llama. **Muse
Spark** launched **2026-04-08** from Meta Superintelligence Labs, in Meta's own
words reaching *"the same capabilities with over an order of magnitude less
compute than our previous model, Llama 4 Maverick"* — Meta itself filing Llama 4
as *"our previous model."* **Muse Spark 1.1** followed 2026-07-09 (a "Thinking"
mode in the Meta AI app and meta.ai, plus a Meta Model API). No Meta primary
source states whether Muse weights are open; the widely repeated claim that
Muse is proprietary and Llama's open-weights line is over is **press-sourced
only** — marked as such, not asserted here.

Practical consequence: **Llama 4 (April 2025) is the newest open-weights
generation**, and it is what "Llama" means for self-hosting purposes.

## Open-weights models

*Source: HF model cards + `llama-models` GitHub model cards.*

| Model | Params | Context | Modalities | Released | License |
|---|---|---|---|---|---|
| Llama 4 Scout | 17B active / 109B total (MoE, 16 experts) | **10M** | text+image in → text/code out | 2025-04-05 | Llama 4 Community |
| Llama 4 Maverick | 17B active / 400B total (128 experts) | **1M** ¹ | text+image in → text/code out | 2025-04-05 | Llama 4 Community |
| Llama 3.3 70B | 70B | 128k | text → text/code | 2024-12-06 | Llama 3.3 Community |
| Llama 3.2 1B/3B (+ Vision 11B/90B) | — | 128k (8k quantized) | text; Vision: image+text → text | 2024-09-25 | Llama 3.2 Community |
| Llama 3.1 8B/70B/405B | up to 405B | 128k | text → text/code | 2024-07-23 | Llama 3.1 Community |

¹ The launch blog says Maverick "supports 10M"; the model card says 1M. **The
model card is treated as authoritative.** Also from the card: image
understanding *"tested up to 5 input images"*; 12 supported languages. Llama 4
**Behemoth** (~2T total) was previewed at launch and no Meta source since
confirms it shipped — null, not a release.

Scout's 10M context is the largest window claimed by any model in this
directory — and, per the sourcing rules, an uncontested vendor claim, not a
measured one.

## The license — the fact that governs everything else

*Source: the LICENSE file in `meta-llama/llama-models`, read verbatim.* "Open
weights" here is the **Llama Community License**, not OSI open source:

- Royalty-free use, reproduction, distribution, derivatives — **but** products
  with **>700M monthly active users need a separate Meta license** (*"you are
  not authorized… unless or until Meta otherwise expressly grants"*).
- Attribution: *"Built with Llama"* displayed prominently; derivative model
  names must begin with "Llama"; an acceptable-use policy is incorporated by
  reference.
- Since Llama 3.1, outputs may be used *"to improve other models"* — synthetic
  data and distillation are explicitly permitted.

For this estate's scale none of the restrictions bite — but the naming and
attribution clauses apply even to hobby derivatives.

## Tool calling, structured output, running it

*Source: `llama4/prompt_format.md` (GitHub) + HF cards.*

- **Tool calling is prompt-format-level, not API-level:** zero-shot function
  calls emitted as a Python-ish list (`[func_name(param=value)]`), custom-tag
  formats supported; Llama 3.3 works through Transformers chat-template tool
  formats. **No Meta source documents native JSON-schema enforcement** — on a
  raw Llama deployment, schema-guaranteed output is the *server's* feature
  (vLLM etc.) or nobody's. Weakness, not limitation.
- **Running it:** weights on Hugging Face (gated behind accepting the license)
  and the llama.com download flow (now behind the unreadable redirect);
  partner-hosted everywhere (AWS, Azure, Google Cloud, Groq, Together,
  Databricks, Cloudflare…). Scout runs in Transformers ≥4.51 bf16, with FP8
  and int4 variants published. A **Llama API** platform (free preview,
  announced 2025-04-29, OpenAI-SDK-compatible, Cerebras/Groq-backed) exists;
  its current status was not verified.

## Consumer surface

Meta AI in WhatsApp, Messenger, Instagram and meta.ai ran *"built with Llama
4"* at the April 2025 launch; Muse Spark now serves meta.ai and the Meta AI app
(Meta's posts). Whether Llama remains anywhere in the consumer stack is
press-contested and unverified — the surface a message actually hits is not
knowable from Meta's published pages.

## Weaknesses — relative, not absolute

Graded per [`README.md`](README.md): worse at, not incapable of.

- **Frozen at April 2025 capability** for open weights, while every other
  provider in this set shipped 2026 generations. Steer: for self-hosted
  frontier-adjacent weights, DeepSeek V4 (MIT) and Mistral (Apache 2.0) are
  the fresher lines; Llama remains the widest-deployed ecosystem.
- **No first-party generation stack** (image/video/audio out) in the open
  line.

## Honest nulls

- Muse weights status; whether Behemoth or a "Llama 3.3 8B" (named once in a
  Meta post, absent from HF) ever shipped; the Llama API's current state; the
  developer.meta.com docs content (JS-shell to fetchers — a browser pass would
  close this); Llama-Guard/Prompt-Guard specs beyond org-listing level.
- Nothing here is measured in this estate yet.
