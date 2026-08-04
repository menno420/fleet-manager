# 2026-08-05 · hub — delegated reads to Gemini, with a citation verifier

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · feature build — the delegation path and its
  first real job

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1`

💡 Session idea: **a verifier's threshold is itself a measurement, and it needs
its own instrument.** The citation checker started as a substring test, which
could not tell a *marker mismatch* (`## 💡 Session idea` quoted as
`- **💡 Session idea:**`) from a *fabrication* (real fragments stitched into a
passage that appears nowhere). Both read as "not present". The fix was to stop
asking whether the quote is present and start asking **how much of it lies in
one contiguous run**: the marker mismatches covered 93%+, the two fabrications
covered 59% and 70%. The threshold sits at 85% — chosen from n=8, which is a
thin sample and is recorded as such rather than presented as a constant.

## previous-session review

`2026-08-05-control-veto-ratified.md` (PR #726, merged) closed the control/
flag. This session opened a capability rather than closing a step: the owner
provisioned `GEMINI_API_KEY` after we established that free-tier Gemini reaches
a 1M-token window, and asked how to delegate work to it to save usage limits.

## Scope

Owner-directed. Build the delegation path, prove it on a real job, record the
measured limits. NOW (E1) untouched — this is capability work, not a program
step.

## What landed

- **`tools/gemini_delegate.py`** — bundle (line-numbered corpus + exact token
  count), run (chunked to the free tier's input meter, structured output,
  automatic verification), verify (re-check a saved report against the tree).
  Stdlib only, direct egress.
- **The citation contract**: every claim ships file + line + verbatim quote;
  quotes are checked mechanically; unverifiable claims are dropped before a
  human reads them.
- **First real job**: the idea groom the kit's own gate has been blocking on —
  329 session cards, 592k tokens, 4 batches, **22 distinct un-groomed ideas**
  with verified citations.
- Provider doc + capabilities ledger updated with what was measured.

## Measured

| | value |
|---|---|
| Free-tier input meter | 250,000 tokens/minute (`gemini-3.6-flash`) |
| Model window | 1,048,576 in / 65,536 out |
| Corpus read | 329 files · 1,810,216 chars · 592,887 tokens |
| Wall-clock | ~5 min for the full corpus, 4 batches |
| Cost | $0 |
| Fabricated citations | 2 of 22 in run 1 (both long quotes) |

Provenance: all rows **measured** — API responses and the tool's own output on
2026-08-05; token counts from the API's `countTokens`/`usageMetadata`, not
estimated.

## Honest nulls

- **The 85% coverage threshold is tuned on n=8.** It separates every case seen
  so far, with the nearest fabrication at 70%. It has not been tested against
  an adversarial quote that is mostly real.
- **The short-quote rule did not do what it was meant to.** Capping quotes at
  200 chars was supposed to reduce reconstruction; the rerun's rejects were all
  marker mismatches instead, so the rule's actual effect is unmeasured.
- **Only one job class has run.** Bench-evidence reads and provenance sweeps
  are proposed, not proven.
- The 22 groomed ideas are an INPUT to a kit groom pass, not a groom. Nothing
  has been routed into the backlog yet.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
