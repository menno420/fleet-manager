# 2026-08-06 · hub — a free key hidden behind a paid one, and the route that decides who pays

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-06 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: the boot file said *"the AI Studio key spends the owner's
card."* Singular. There are two AI Studio keys and **one of them is free** — so
the compression did not merely lose detail, it steered every session away from a
zero-cost resource and onto a paid one.

## What was wrong

| source | said |
|---|---|
| `.claude/CLAUDE.md` | *"The AI Studio key spends the owner's card"* — **singular, and the defect** |
| `docs/conventions/vertex-first-for-gemini.md` | headed *"the **two** paths are funded differently"*; named `GEMINI_API_KEY_PAID` correctly but **never mentioned the free key exists** |
| `tools/gemini_delegate.py`, `docs/CAPABILITIES.md`, `delegate-read` | already used `GEMINI_API_KEY` and already called it free-tier — **these were right** |

So the estate half-knew this. The half that was compressed into the boot file is
the half every session reads first.

## The corrected model

**Two identities, and the paid one has two routes that bill differently.** The
first draft of this card called it "three paths", which implied three separate
credentials. The owner corrected the framing, and his version is the one that
predicts behaviour:

> *"Vertex is only available on the paid key, which uses the $300 of free
> credits when routed through Vertex. But uses my own personal credit when
> directly invoking the Gemini API."*

| identity | route | who pays | constraint |
|---|---|---|---|
| **`GEMINI_API_KEY`** — free tier | AI Studio | **nobody** | ~20 req/day flagship Flash, 500/day Flash Lite. **Serves the Interactions API** (server-side history) |
| **paid GCP project** — SA | **Vertex** | prepaid credit, €251.37 left | no daily cliff; **no server-side history** — `interactions:create` → `RESOURCE_PROJECT_INVALID` here, so transcripts resend every turn |
| **paid GCP project** — `GEMINI_API_KEY_PAID` | AI Studio | **the owner's card** | none, which is the problem |

Rows 2 and 3 are the **same billing account**. The credit excludes the "Gemini
API in AI Studio" SKU and does not exclude Vertex, so one project is
credit-funded on one host and card-funded on the other. **The route decides who
pays, not the key** — and it follows that `generativelanguage` is not one thing:
free on one key, billed on the other.

The non-obvious consequence: **for a long multi-turn exchange the free key beats
Vertex on both axes** — free, and server-side history means linear rather than
quadratic token growth. Vertex stays the default for volume, image and video,
where 20 requests/day is the real ceiling.

## How it was established, and what I did not do

The owner said a free token existed and that I had defaulted to the paid one.
Under DISCOVERY RULE step 0 that is source truth — so the question was never
*whether* he was right, only **which variable**.

- Both vars present and **genuinely distinct** — 53 vs 39 chars, different
  digests, confirmed without printing either value.
- Railway `reliable-grace`/`worker`/`production`: 35 variables, only
  `GEMINI_VERTEX_SA_JSON` Gemini-related. Not there.
- The docs said `GEMINI_API_KEY` was free; he said I had used the paid one.
  **Irreconcilable by inference, and every probe either spends his card or
  writes a guess into a doc that is already wrong about this.** So I asked one
  question instead of testing — he confirmed `GEMINI_API_KEY` is the free one.

Worth naming: there *was* a zero-ambiguity probe available (grounding returns
429 on a free key, per `providers/gemini.md`). I did not run it. A question to
the person who provisioned the key is cheaper than a call that might bill him,
and step 0 exists precisely so that asking beats probing when he is present.

## What landed

- `.claude/CLAUDE.md` — the Gemini bullet now carries all three paths and says
  outright that it used to hide the free one.
- `docs/conventions/vertex-first-for-gemini.md` — new lead section carrying the
  identity/route split and the owner's own statement of it; the old heading said
  "the two paths" and never mentioned the free key.
- `.claude/hooks/doc-routes.json` — the `gemini` route carries the three-path
  model and now also triggers on `GEMINI_API_KEY_PAID`, so reaching for the card
  surfaces the free alternative.
- `docs/CAPABILITIES.md` — append-log entry.

## Verification

- `python3 tools/check_doc_routes.py --strict` → **exit 0** (20 routes, 15 docs).
- Railway read over direct egress → **HTTP 200**, 35 variables (the proxied path
  403s, as documented).
- Remaining gates recorded at close.

## Honest nulls

- **The free/paid assignment is `OWNER`, not measured.** The naming is
  ambiguous enough (`GEMINI_API_KEY` beside `GEMINI_API_KEY_PAID`) that only he
  could settle it, and nothing here re-derives it.
- **The RPD figures are `MEASURED-PRIOR`** — from his AI Studio dashboard via
  `providers/gemini.md`, not re-read today.
- **Whether Vertex's `RESOURCE_PROJECT_INVALID` is preview gating stays
  unproven.** One call, one project. It is recorded as what that call did.
- **No call was made on either AI Studio key this session**, so nothing here
  re-verifies that the free key still works.

## ⟲ Previous-session review

Three cards in a row now with the same shape: the estate knew the right thing
somewhere and the place a session actually reads said something narrower. First
a requirement filed in a skill the reader never opens, then a recipe missing its
sampling parameter, now a funding model compressed until a free resource
disappeared. **The failures are not wrong facts — they are correct facts that
lost a distinction on the way to the page that gets read.**
