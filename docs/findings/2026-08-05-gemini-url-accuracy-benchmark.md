# Gemini accuracy benchmark — when it cannot read the page, it answers anyway

> **Status:** `reference`
>
> Owner-directed (2026-08-05): *"each file you intend to read, send the link to
> Gemini as well and compare your findings to theirs."* Ten URLs this session had
> already fetched itself, so ground truth existed before Gemini was asked.
> Model `gemini-3.1-pro-preview`, paid key, `url_context` tool.

## The result in one line

**Gemini retrieved 0 of 8 `support.google.com` pages and 2 of 2
`developer.android.com` pages — and when retrieval failed it answered from
training data anyway, usually phrased as if it had read the page.** One of those
answers was wrong on the single most schedule-critical number in the project.

## Retrieval, by host

| Host | Attempted | Retrieved |
|---|---|---|
| `support.google.com` | 8 | **0** |
| `developer.android.com` | 2 | **2** |

The split is total and clean. Every Play Console help page failed with
`URL_RETRIEVAL_STATUS_ERROR`; both Android developer pages returned
`URL_RETRIEVAL_STATUS_SUCCESS`. Since Play *policy* lives almost entirely on
`support.google.com`, this is precisely the corpus Gemini cannot read.

## Per-case scoring against pages this session fetched itself

| Case | Retrieved | Gemini's answer | Verdict |
|---|---|---|---|
| `app-id` | ✅ | segments/characters/never-change all correct | **correct** |
| `aab` | ✅ | Aug 2021, 4 GB, >200 MB → Feature/Asset Delivery | **correct** |
| `text-limits` | ❌ | 30 / 80 / 4,000 | correct **from memory** |
| `fee` | ❌ | US$25 one-time | correct **from memory** |
| `data-safety` | ❌ | definitions correct — **and it said it was blocked** | correct **and honest** |
| `assets` | ❌ | icon/feature/counts correct; **omitted** the ≥1920×1080 games minimum and the 320/3840/2× dimension rules | incomplete |
| `signing` | ❌ | upload-vs-app-signing correct; **"NOT ON PAGE"** for key size (page says RSA ≥2048); reset route given as *"contact Google Play support"* (actual: self-serve in Console) | **partly wrong** |
| `closed-test` | ❌ | **"At least 20 testers"** | **WRONG — the page says 12** |
| `target-api` | ❌ | "NOT ON PAGE" | false negative — page states it |
| `prereq` | ❌ | "NOT ON PAGE" | false negative — page states it |

Two correct-and-retrieved. Three correct from memory. Two false negatives. Two
materially wrong. One honest about being blocked.

## The expensive one

Asked how many testers a new personal account needs, Gemini answered **20**,
prefaced with *"Based on the Google Play support page for testing requirements."*
The page says **12**. Twenty was the **old** requirement before Google reduced
it — so this is not a hallucination, it is a stale fact delivered with a
citation it could not read.

That number sets the launch date for this project. Acting on it would have meant
recruiting eight testers that were never needed, and — worse in the other
direction — an estimate built on the wrong gate.

**The same model got this right an hour earlier.** In the `google_search`-grounded
pass it answered *12*, and volunteered *"(this requirement was reduced from an
earlier 20-tester minimum)"*. Same model, same key, same day, opposite answers:

| Tool | Answer | Correct |
|---|---|---|
| `google_search` grounding | 12, with the 20→12 history | ✅ |
| `url_context` (retrieval failed) | 20 | ❌ |

Search grounding reaches Play's help corpus; `url_context` does not. **The tool
chosen, not the model chosen, decided whether the answer was right.**

## The instrument that catches it

Nothing in the prose distinguishes a page-sourced answer from a memory-sourced
one. *"Based on the contents of that page"* appeared above the wrong 20-tester
answer. The signal is structural and lives in the response metadata:

```
candidates[0].urlContextMetadata.urlMetadata[].urlRetrievalStatus
  → URL_RETRIEVAL_STATUS_SUCCESS | URL_RETRIEVAL_STATUS_ERROR
```

Read it on every `url_context` call and discard the answer when it says ERROR.
This is the same shape as the HUD-telemetry finding
([`2026-08-05-hud-telemetry-verification.md`](2026-08-05-hud-telemetry-verification.md)):
**the reliable signal was an instrument reading, not the model's narration of
itself.** There it was a distance counter; here it is a retrieval status field.

For `google_search` grounding the equivalent instrument is
`groundingMetadata.groundingChunks` — measured the same day, an **empty chunk
list** marked exactly the two answers (target SDK, games-specific) that were
model memory rather than search.

## Standing rule this produces

1. **`url_context` cannot read `support.google.com`.** For Play policy, use
   `google_search` grounding, and verify by fetching the page yourself.
2. **Check the instrument, not the prose** — `urlRetrievalStatus` for
   `url_context`, `groundingChunks` for search grounding. Both are cheap and both
   caught real errors on their first use here.
3. **A failed retrieval is not a refusal.** The model proceeds and sounds
   identical. Only 1 of 8 blocked calls disclosed the block unprompted.
4. **Verified > grounded > cited.** A citation the model could not open is worth
   less than no citation, because it manufactures confidence.

## What this does not say

It does not say Gemini is unreliable in general. On the two pages it *could*
read it was accurate and complete, and the search-grounded pass earlier the same
day was correct on every claim later confirmed by hand. Three of its
memory-sourced answers were also right. The failure is specific and mechanical:
**one host it cannot fetch, and no honest signal in the prose when that
happens.**

Sample size is ten URLs, one model, one day, and it warrants no broader claim.
