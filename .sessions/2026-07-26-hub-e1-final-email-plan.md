# 2026-07-26 · hub — E1 planned: the final EAP email (source map + seeded list)

> **Status:** `complete`

- **📊 Model:** fable-5 · high · docs-only

Time: 2026-07-26 (late night) · venue: owner-live hub chat · branch
`claude/repo-consolidation-plan-jl7z6x` (restarted from main after #549)

💡 Session idea: the owner's format ask — "clear pointers, without too much
explanation" — is the email-shaped version of the same principle the whole
program runs on: **the reader's attention is the scarcest resource.** The
earlier mails optimized for evidence completeness; this one optimizes for a
five-minute read that cannot be misunderstood. Hence fresh thread (no quoted
history), one page per part, one line of *why* per item, and the good parts
in the same mail so the picture is whole.

## previous-session review

Same session: #548 recorded OD-10/11/12; #549 committed the telemetry ledger.
The owner then set tomorrow's priority: the final EAP email he promised —
"probably the most important thing we can do separate from our own repo
work" — and asked for a plan so the next session knows where to look.

## What this commit does (docs-only)

- **`docs/planning/2026-07-26-final-eap-email-plan.md`** (new) — program step
  E1's working doc: the owner's requirements distilled · verified facts the
  writing session needs (incl. **the 07-18 follow-up draft was never sent** —
  checked against sent mail tonight, so its findings are unused material) ·
  the source map in priority order (reflection §vendor-email guidance →
  retrospective §§1–4 → the consolidated classifier findings → the unsent
  draft → eap-story §10 numbers → the sent thread itself) · a **pre-harvested
  candidate list** (13 wishes in the owner's exact "what + because" format +
  the good-parts block + the two review-paragraph numbers) · the method
  (harvest → owner picks → Part 2 ≤1 page → **Part 1 never ghost-written** →
  fresh compose, new subject) · boundaries (never re-argue the
  already-reported cases; nothing sends without the owner).
- **`docs/planning/2026-07-26-consolidation-program.md`** — Track E added;
  **NOW → E1** (D2 queued next); §7 ledger rows.
- **`docs/planning/README.md`** — index row.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
python3 scripts/check_docs_links.py
```
