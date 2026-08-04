# 2026-08-05 · hub — the Studio/API asymmetry, and who should ask what

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only — one capability asymmetry, recorded

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1`

💡 Session idea: **"free tier" named two different products and nobody noticed
until the two halves were measured from opposite ends.** The API free tier and
the AI Studio free tier share a name, a project, and a dashboard — and serve
different models with different tools. It took the owner's Run-settings screen
(Pro + search, working) beside this session's 429s (Pro + search, refused) to
see it. The generalisable move: when a vendor word covers two surfaces, measure
each surface separately before writing either down, because the shared name
will otherwise carry one surface's facts onto the other.

## previous-session review

`2026-08-05-aistudio-billing-caveat.md` (PR #732, merged) added the paid-key
condition. This card records what the free Studio surface actually reaches,
which turns out to be strictly more than the free API surface.

## What landed

- `docs/providers/gemini.md` — the asymmetry, both instruments, and the
  resulting division of labour between the owner's Studio sessions and this
  estate's API delegation.

## Measured — two instruments, opposite directions

| Capability | Free API (this session) | Free Studio (owner's screen) |
|---|---|---|
| `gemini-3.1-pro-preview` | **429** paid-quota; dashboard row reads `0/0` RPM/TPM/RPD | selected and running |
| Grounding with Google Search | **429** on a two-token prompt | toggled on, returned cited sources |
| Flash-class models | 20/day (3.6) · 500/day (lite) | free, unmetered against API quota |
| Thinking level, temperature, structured output, code execution, function calling | API parameters | UI controls, plus `Get code` export |

## What it means for the division of work

- **Owner, in Studio** — strongest model + live web, free, not charged against
  API quota. The right surface for open research questions and anything
  needing the current web.
- **This estate, via API** — Flash-class, no search, 20 calls/day. The right
  surface for bulk corpus reads over material already in the repos, where every
  claim is citation-checked (`tools/gemini_delegate.py`).

The two barely overlap, which makes the split clean rather than a compromise.

## Honest nulls

- **Whether Studio's Pro access is unlimited is unmeasured** — only that it
  runs there while the API refuses it. No Studio-side ceiling was probed.
- The `0/0` dashboard reading for Pro was taken from a screen recording, not an
  API call; it agrees with this session's 429 but is not the same evidence.
- Whether Studio's search grounding is the same feature as the API's
  `google_search` tool, or a different implementation, is not established.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
