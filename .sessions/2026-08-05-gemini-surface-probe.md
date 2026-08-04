# 2026-08-05 · hub — what the Gemini API actually offers, probed

> **Status:** `complete`

- **📊 Model:** opus-5 · high · research — six owner questions, answered by probe

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1`

💡 Session idea: **the delegate's best review finding was the one it could not
have guessed.** Asked to review the delegation tool, Gemini ranked a
fabrication first (uppercase schema enums, asserted to break every run, in code
that had already run three times) and buried a real path-traversal defect at
number two. The lesson is not "don't use it" — the traversal bug was genuine,
mine, and unnoticed. It is that **its severity ranking carries none of the
signal**: rank order is generated prose, while each individual finding is
independently checkable. Read every item, believe the ranking of none.

## previous-session review

`2026-08-05-gemini-delegation.md` (PR #728, merged) built the delegation path.
This session probes the surface around it, on the owner's questions, and folds
the two real defects the probe surfaced back into the tool.

## Scope

Owner asked six things: multi-turn, web search / Google integrations, code
review, self-knowledge, session visibility, purpose selection. Probed rather
than reasoned about. No subagents spawned — the owner is at 67% of his window
with four days left, and every probe here was free.

## What landed

- Two real review findings fixed in `tools/gemini_delegate.py`: **path
  traversal** (model-supplied paths are untrusted; `repo / "/etc/passwd"` is
  `/etc/passwd`) and a **None-content crash** on safety-blocked responses.
  Both confined and asserted.
- `docs/providers/gemini.md` — the probed API surface: which tools a free key
  serves, the two distinct quota metrics, multi-turn statelessness.

## Measured — all by probe, 2026-08-05

| Question | Result |
|---|---|
| Multi-turn conversation | works; **stateless** — history is resent each call |
| `google_search` grounding | **429 on a 2-token prompt** — not served to this free key |
| `url_context` | works — fetched a raw GitHub URL, quoted its heading correctly |
| `code_execution` | works — computed fib(40) = 102334155, verified |
| `function_declarations` | accepted |
| `systemInstruction` | works — "answer in exactly three words" obeyed |
| Code review, 3 findings | 2 real (path traversal, None crash), 1 fabricated, fabrication ranked #1 |
| Quota metrics | two distinct: `..._input_token_count` (250k/min) and `..._requests` (per-model daily) |
| Model exhaustion | `3.6-flash` spent while `3.5-flash-lite` and `3.1-flash-lite` still answered |

## Honest nulls

- **The self-knowledge probe never ran** — `3.6-flash` hit its daily request
  cap first. What it says about itself is therefore untested here, and the
  provider doc's existing self-report caution stands unchanged.
- The daily request ceiling's exact **number** is unmeasured; only the metric
  name and the fact of exhaustion are.
- One review of one file is a thin basis for "it reviews code well or badly".
  The 2-of-3 hit rate is a single sample.
- `url_context` was tested on one public raw URL; behaviour on private or
  rendered pages is untested.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
