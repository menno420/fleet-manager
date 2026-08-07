# 2026-08-07 · hub — counting what the substrate caught

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-07 · venue: owner-live hub chat · branch `claude/substrate-measurement`

💡 Session idea: the owner knows he corrected me once today. He almost certainly
does not know his machinery corrected me **eleven** times, because that is the
whole point of it — a check that works is one you never hear about. The ratio is
information he cannot get from his side of the glass.

## What this is

He said the enforcing checks exist so he would not have to correct every session.
That is a testable claim and today is a clean dataset, so it is now a counted one:
[`docs/findings/2026-08-07-what-the-substrate-caught.md`](../docs/findings/2026-08-07-what-the-substrate-caught.md).

**11 instrument catches to 1 owner catch.** Every item enumerated rather than
summarised, so the number can be checked — which matters, because the same session
produced four wrong counts by pattern-matching instead of reading, and a tally I
asked him to trust would be the fifth.

## The two findings worth carrying

**The one he caught is the one no gate could have.** No checker reports "you did
not wait long enough". Every *structural* error was caught by the machinery; the
single escape was a judgement call at a decision point. That is
`2026-08-05-foundation-continuation.md` § 2 confirmed with a ratio rather than
restated, and it lines up with his own presence model.

**The gates have a measured ceiling.** Four wrong numbers passed every checker in
this repo. A checker validates form, and all four were impeccably formed. Only
Codex — a reviewer, not a checker — caught them, and only because he told me the
relay existed.

## Honest nulls, in the file and repeated here

The classification is mine and arguable (drop the ambiguous hook fire and it is
10:1). The denominator is unknown by construction — this counts errors that were
*caught*, and says nothing about what got through. One session is one session.

## ⟲ Previous-session review

The card before this one concluded the pattern was "failing to treat his stated
decisions as settled". Today's fuller version is narrower and worse: **I wrote the
rule against false walls in the morning, quoted it to him at midday, and broke it
in the evening.** Knowing a rule does not invoke it.

That is why the write-up's § 5 lands where it does — the documents worked three
times today, and each time because something *made* me reach for them. The hook
that stopped me writing "Codex isn't available" was worth more than the ledger
entry it pointed at. Documents plus a trigger work; documents alone are a thing I
demonstrably walk past.

## Open

Nothing in fleet-manager. curious-research carries its own implementation-first
queue in `docs/current-state.md`, top item the Fusion→laser/CNC guide.
