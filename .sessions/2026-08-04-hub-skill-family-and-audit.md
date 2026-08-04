# 2026-08-04 · hub — fresh-eyes audit + the image-prompt skill family

> **Status:** `in-progress`

- **📊 Model:** fable-5 · max · docs-only — session-output audit, skill review, three-skill family

Time: 2026-08-04 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1` (restarted from main post-#719)

💡 Session idea: **a day of corrections leaves the corrected claims consistent
and the summaries of them stale.** Each of today's three correction waves fixed
the section it targeted; none re-read the document's own recap. The recipe list
at the bottom of the art finding still said "never a batch" and "audit after
downscaling" — both superseded hours earlier in the sections above it. A
summary inside a document is a copy, and copies drift exactly the way the
cite-never-copy rule predicts; the fix is the same as the register's: summaries
should carry the least restatement that still reads, and corrections should
grep the whole file, not the section they came to fix.

## previous-session review

`2026-08-04-hub-chroma-spill-measured.md` (PR #719, merged) replaced a quoted
mechanism with a measured one and updated the skill's hard rule — but not the
finding's own recipe recap, which is precisely the drift described above. Its
honest null "conversation images arrive as inline vision, not files" was left
on the card only; it is a venue-scoped surface fact and belongs in the
capabilities ledger, where this session puts it.

## Scope

Owner-directed, on a model/effort change (opus-5 high → fable-5 max) taken for
fresh eyes: audit today's output for undocumented value and internal drift;
review all skills and judge fitness; split image generation into a family —
sprites, parallax backgrounds, cover/icon/banner — each carrying the measured
standard so recurring art tasks stop depending on session memory. Not a program
step; NOW (E1) untouched.

## What landed

*(written at close)*

## Honest nulls

*(written at close)*

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
