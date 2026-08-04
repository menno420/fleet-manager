# 2026-08-05 · hub — Vertex AI reachable from a session

> **Status:** `complete`

- **📊 Model:** opus-5 · high · research — the credit-eligible path to Gemini

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1`

💡 Session idea: **the same model behind two product names is not the same
product.** Google's $300 welcome credit excludes "Gemini API in AI Studio" and
covers Vertex AI — which serves the identical Gemini models. Reading the
exclusion as "Gemini is excluded" would have closed a door that was open. The
transferable check: when a vendor carves out a *product*, ask what else serves
the same *capability*, because eligibility keys on the SKU, not the model.

And the surfaces are not identical where it matters most: the AI Studio API
returned **JPEG**, Vertex returned **PNG** from the same model and prompt.

## previous-session review

`2026-08-05-gemini-paid-tier-live.md` (PR #736, merged) recorded the €10 paid
tier. This adds the credit-funded path beside it, and corrects a claim made in
chat about what had been verified.

## What landed

- `docs/providers/gemini.md` — the Vertex path: auth shape, what it serves, the
  PNG-vs-JPEG difference, and the honest limit on billing verification.

## Measured — 2026-08-05

| Fact | Value |
|---|---|
| Auth | service account + OAuth; **API keys are rejected outright** (`"API keys are not supported by this API"`) |
| Endpoint | `{loc}-aiplatform.googleapis.com` · `global` works for Gemini models |
| Gemini 3.1 Pro | OK via Vertex — refused on the free AI Studio key |
| Gemini 3.6 Flash | OK |
| Image generation | OK — `gemini-3.1-flash-image`, **1408×768 PNG**, 1.3 MB, corner chroma RGB(12,248,5) |
| AI Studio API, same model | **JPEG**, 549 KB — lossy, artefacts on the chroma edge |
| Billing structure | project → `billingAccounts/01161F-0357D6-33069D`, billingEnabled, EUR, one linked project |
| Local dependency | system `cryptography` was broken (`_cffi_backend` missing); `pip install cffi` repaired it |

Provenance: all rows **measured** by call in this container.

## Honest nulls — and a correction

- **I claimed in chat that the calls were paid by the $300 credit. That was
  inference, not measurement**, and it is the exact failure PL-014 names. What
  is verified: the project bills to the account that holds the credit. What is
  not: whether the credit or the card absorbs the charge. The Cloud Billing API
  exposes billing *structure* only — no cost or credit balance endpoint exists;
  it is console-UI or BigQuery-export only.
- **Vertex is not usable by a future session yet.** The service-account JSON
  lives only on this session's disk; nothing has been added to the environment.
- **Imagen models 404** at `us-central1` on this project — image generation ran
  through the Gemini image model instead. Whether Imagen needs enabling
  separately is untested.
- ⚑ **Owner: the service-account key is compromised-by-exposure** — it was read
  into the conversation transcript when uploaded. Rotate it (delete key
  `c87c878…`, create a new one) before it is used beyond this session.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
