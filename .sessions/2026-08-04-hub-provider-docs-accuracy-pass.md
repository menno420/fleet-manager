# 2026-08-04 · hub — provider docs were thin: accuracy pass against official changelogs

> **Status:** `complete`

- **📊 Model:** opus-5 · high · research — changelog-sourced corrections

Time: 2026-08-04 · venue: owner-live hub chat · branch
`claude/provider-docs-accuracy-pass`

💡 Session idea: **speed is not evidence of coverage, and the estate has no way
to tell them apart.** The owner's suspicion was triggered by *how fast* the
research finished — minutes, sometimes seconds — and he was right to read that as
a signal. A session that runs five searches and a session that reads three vendor
changelogs both emit a document of the same length, in the same voice, with the
same confident structure. Nothing downstream distinguishes them: the gate checks
grammar and staleness, `check_no_false_walls` checks phrasing, and neither can
see whether a claim was sourced or guessed.

The cheap fix is a **sourcing line per document** — for each major section, which
class of source it came from (vendor changelog · vendor doc · measured here ·
secondary · inference) and when. Not per-claim citation, which nobody sustains;
one line per section, which makes thinness *visible on the page* instead of
inferable only from a wrong fact later. The provider docs now carry this
unevenly; making it a rule is the follow-on.

Generalisable: **when a process can fail silently, the artifact should carry the
evidence of how much work went into it.** Otherwise the only detector is a reader
who happens to know the domain — which is what happened here, and which does not
scale past the one domain the owner knows well.

## previous-session review

`2026-08-03-hub-provider-references.md` (PR #702, merged) shipped the provider
set and closed on *a knowledge base that only records work products leaves its
agents to reinvent the environment*. That was right about the gap and wrong about
its own quality: the same card listed "ChatGPT plan details are secondary-sourced"
as its single honest null, when the real problem was that **the mode taxonomy was
secondary-sourced too** — and unlike the prices, it was outdated rather than
merely uncertain. The lesson: an honest-nulls list is only as good as the audit
behind it, and I audited what I knew was weak rather than checking what I assumed
was fine.

## Why this exists

The owner read the provider docs merged in #702 and found them thin and in places
wrong. He named two errors specifically, and both were real. His framing — *"I
don't feel like I can properly trust what you told me based on these
inaccuracies"* — is the correct response to the actual work: the first version was
built from a handful of searches that returned mostly aggregator sites, and it
never opened a vendor changelog.

## The two errors, and the pattern behind them

**1. ChatGPT's standalone "Agent mode" was retired in July 2026.** OpenAI
discontinued Atlas on 2026-07-09/10 — it stops working 2026-08-09 — and folded
its agentic and browser capability into ChatGPT Work, an enhanced desktop app and
a Chrome extension; the desktop app now combines ChatGPT, Codex and Work into
one. Corroborated on OpenAI's own docs site, where Work sits **under the Codex
platform** (`learn.chatgpt.com/codex/get-started-with-work`) rather than as a chat
mode. The six-mode table I published described the pre-consolidation Tools menu.

**2. Gemini's Drive integration was filed as a weakness when it is a strength.**
Native Workspace access: the Productivity Planner Gem pulls Gmail, Calendar and
Drive; Personal Intelligence connects apps you authorise; Gemini Agent uses Gmail
and Calendar. What fails is pasting a Drive *URL* — a link-fetching limit, not a
Drive limit. **The transcript I had already read stated this plainly** and I still
wrote the inverse, which makes it a comprehension failure rather than a sourcing
one.

Both errors sit in the same class: **the fastest-moving facts on these platforms
are product surfaces, mode lists and integrations, and those are exactly what
aggregator articles get wrong.** Prices I flagged as uncertain; surfaces I did
not, because I had no reason to think they moved — which was itself the
assumption worth checking.

## What landed

- **`gemini.md`** — re-derived from the official
  [Gemini Apps release notes](https://gemini.google/release-notes/), read in full
  (115K characters). Drive reframed as the strength it is. Four agentic surfaces
  added that were missing entirely: **Gemini Agent**, **Gemini Spark** (Ultra),
  **Personal Intelligence** (beta, AI Pro/Ultra, US, off by default), **Daily
  Brief**, plus scheduled actions and the macOS voice/screen-context app.
  Corrected: video generation is in-app via **Gemini Omni**; Deep Research takes
  **uploaded files** as sources and transforms reports in Canvas; 3.6 Flash went
  global 2026-07-21.
- **`chatgpt.md`** — the July 2026 consolidation stated up front, the mode table
  cut to what is still distinct, and an explicit warning that it is neither
  exhaustive nor settled.
- **`README.md`** — the owner's **weakness ≠ limitation** rule as a governing
  principle, and a fourth sourcing rule: *changelog first; aggregators never, for
  anything volatile.*
- **`claude.md`** — relative weaknesses, each graded as a weakness rather than a
  wall: in-chat image/video generation, interactive speed, no native consumer
  integrations.

## Honest nulls — the ones that matter this time

- **OpenAI's primary changelog is unreachable from here.**
  `help.openai.com/en/articles/6825453-chatgpt-release-notes` answers **HTTP 403
  behind a Cloudflare interstitial** to both WebFetch and headless Chromium —
  measured, same challenge shape as the ChatGPT project URL. So ChatGPT's mode
  list and plan details still rest on the docs site plus press coverage. The doc
  says so on the page rather than in a footnote.
- **Anthropic's own changelog was not swept** in this pass. `claude.md`'s model
  table still comes from the `claude-api` skill's 2026-06-24 cache.
- **The corrections are not themselves owner-verified.** He caught two errors in
  the first version; nothing guarantees this version has none.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
