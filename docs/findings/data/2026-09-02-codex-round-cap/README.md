# 2026-09-02 · Codex round cap — retained verification input

> **Status:** `reference` · raw input behind `docs/traps.md` TRAP-009 and
> the two 2026-09-02 entries of `docs/decisions.md` (the cap, the model tiers); retained so the numbers cited there
> can be re-derived from the tree, not from a chat.

| file | what it is | produced by |
|---|---|---|
| [`round-classification.json`](round-classification.json) | every one of fm #1010's 88 inline Codex review threads, bucketed by the review round that raised it and classified against the commit that answered it — **a snapshot taken before the flip**: round 17's one thread reads `fix_action: "Not yet fixed"` because it was classified while still open; it was fixed in the landing pass (`27891ea`) — (`factual-reversal-core` · `factual-correction-minor` · `script-defect` · `sync-drift-self-inflicted` · `wording-precision` · `rejected-or-disputed`), with each round's `cap3_would_have_shipped_error` flag and two independent root-cause paragraphs | two classifier agents (rounds 1–9, rounds 10–17) of the 2026-09-02 morning workflow, both run on Fable 5.1 by inheritance — the case the model-tier decision corrects |
| [`gemini-check-1-fm1010-flip-diff.md`](gemini-check-1-fm1010-flip-diff.md) | the free-key Gemini pass (the 2026-08-29 cadence decision's intermediate-push route) over the pre-flip edits to fm #1010: four source-anchored claims SUPPORTED, five not judged for lack of a supplied excerpt (each checked directly instead), none CONTRADICTED | `gemini-3.6-flash`, one `generateContent` call, temperature 0 |
| [`gemini-check-2-fm1011-round3-diff.md`](gemini-check-2-fm1011-round3-diff.md) | the same pass over fm #1011's post-round-3 diff, the cap's own exit: every item SUPPORTED, verdict RESOLVED | same route |

**How to re-derive TRAP-009's counts:** the totals (16 core reversals, 14
minor corrections, 17 script defects, 12 wording, 29 self-inflicted drift, 0
rejected) are `Counter(f["category"] for r in rounds.values() for f in
r["findings"])` over `round-classification.json`; the drift-only rounds are
those whose findings are all `sync-drift-self-inflicted` (5, 16, 17).

**What this is not:** the review threads themselves live on GitHub
(`/pulls/1010/comments`, 88 threads, `hasNextPage: false`); the classification
is a reading of them, by agents, checked in places by the landing session
(judge scores, pipeline counts, the L02 mechanism, the model fields) and not
re-read thread by thread. Treat a per-thread category as `REVIEWED`, the
totals as `MEASURED` over that review.
