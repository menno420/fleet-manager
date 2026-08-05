# 2026-08-05 · hub — it was retrieval, not reading

> **Status:** `complete`

- **📊 Model:** opus-5 · high · research

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/swingy-spider-play-submission-wno3nb`

💡 Session idea: **the first benchmark measured one platform and wrote a
conclusion about a model.** "Gemini cannot read `support.google.com`" was the
finding; it was wrong in scope, and the owner's two follow-up questions —
*"what about the file reviews?"* and *"I also mean, directly sending the files
without url"* — are what turned one arm into four. Vertex's `urlContext`
retrieved **8/8** of the pages AI Studio failed on, and handing the text inline
scored **4/4 on both platforms with near-identical wording.** The model reads
fine. One platform's fetcher does not fetch. A benchmark with a single arm
cannot tell those apart, and mine had one arm.

## previous-session review

`2026-08-05-vertex-first-directive.md` (PR #748, merged) made Vertex the default
and verified the Railway → SA → OAuth route. That route is what made this
correction cheap to run: the four new arms are credit-funded.

## What landed

- `docs/findings/2026-08-05-gemini-url-accuracy-benchmark.md` — an UPDATE section
  correcting the original conclusion, the four-arm table, the practical ranking,
  and the source-checked note that `gemini_delegate.py` was never exposed.

## Measured

**Four arms, same ten questions, ground truth from pages fetched by hand:**

| Arm | Retrieval | Answers |
|---|---|---|
| AI Studio `url_context` | **0/8** support · 2/2 developer | 5/10; **2 materially wrong** |
| Vertex `urlContext` | **10/10** incl. **8/8 support** | all checked correct |
| Vertex `googleSearch` | n/a | all checked correct |
| Inline text, both platforms | n/a | **4/4 each**, near-identical wording |

Vertex `urlContext` got right both facts AI Studio got wrong: **12 testers**
(not 20) and **RSA ≥2048** (not "NOT ON PAGE").

**It is not bot-blocking.** Plain `curl` returns the pages: raw HTML for
`answer/14151465` contains "12 testers" and "14 days"; `answer/6112435` contains
"US$25". The content is public; one fetcher does not retrieve it.

**The inline arm is the control that settles causation.** Remove retrieval, hand
over the text, and both platforms answer correctly and almost identically. So
the variable was never comprehension.

**Tool names differ by platform** — Vertex `urlContext` / `googleSearch`
(camelCase); AI Studio `url_context` / `google_search`.

**Checked in source, not assumed:** `tools/gemini_delegate.py` passes file
contents inline and uses neither URL-reading nor grounding, so the estate's
read-delegation path sat on the 100% arm throughout. It does post to the
card-funded AI Studio endpoint, which is now a funding defect under the
Vertex-first directive — noted, not urgent.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- `python3 bootstrap.py check --strict` → **exit 0**, run post-commit (the
  grammar check reads committed cards, so a pre-commit pass proves nothing —
  learned the hard way earlier today on spider-swing #163).
- Every figure is a live HTTP response from this session, not a re-reading of a
  prior doc. The new arms ran on Vertex, so the correction was credit-funded.
- `gemini_delegate.py`'s inline transport was read in source, not inferred.

**Honest nulls:** the inline arm covers 4 of the 10 cases, not all 10 — enough to
settle causation, not a full head-to-head. `googleSearch` on Vertex was scored on
the discriminating subset. n=1 platform-pair, one model, one day; no claim beyond
these hosts and these questions.
