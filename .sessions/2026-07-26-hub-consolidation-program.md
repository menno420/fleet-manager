# 2026-07-26 · hub — the consolidation program + boot-file refresh (step D1)

> **Status:** `complete`

- **📊 Model:** fable-5 · high · docs-only

Time: 2026-07-26 (night) · venue: owner-live hub chat · branch
`claude/repo-consolidation-plan-jl7z6x` (restarted from main after #545)

💡 Session idea: the owner's real complaint was never repo count — it was
**orientation cost**: three tries for one session to understand the estate.
So the program's unit of account is the *future session*: every step is sized
to one session, the boot file is the entry point that must make the next
session fast, and "done" for the whole program is a fresh-session test, not a
repo count. The documentation IS the product of consolidation; the folds are
just its consequence.

## previous-session review

Same session, one PR back: #545 landed the fleet account. The owner then gave
the definitive framing (recorded as OD-5..OD-9 in the program): Projects
terminated since 07-21 (maybe back ~August for general use — not fact);
regular sessions possibly indefinitely; slow pace, no profit pressure, no
deletions; documentation first, websites second; CI toward one required check
per repo; goal = a plan he can work with any future session, one step at a
time. He also flagged that one of my questions betrayed unread email/EAP docs
— correct: the answer was in the corpus + the Gmail thread.

## What this commit does (docs-only)

- **`docs/planning/2026-07-26-consolidation-program.md`** (new, living-ledger)
  — THE plan: OD-1..OD-9 · 7-section target · step ledger in four tracks
  (D docs · W websites · R repos · C CI) with a NOW pointer · session
  protocol · non-goals · open forks (§6) · append-only progress ledger (§7).
- **`.claude/CLAUDE.md`** — **step D1 executed**: hub boot file refreshed to
  the post-program era (sessions-not-seats; the 3-file read path: program →
  account → owner-queue; live-vs-historical map; the owner's working style;
  capabilities kept, incl. the private-repo direct-clone recipe). Flagged for
  owner review per Q-0106 — the owner is live-directing this program and the
  PR is his review surface.
- **v2 plan** → `historical` with supersession banner; planning README rows.

## Gaps closed this pass (the owner's pointer)

- **The email arc, from the actual Gmail thread** (chat-side detail; kept
  generic here): reviews sent 07-08 and 07-12; vendor reply 07-14; the
  07-16 regression reports; the program-end correspondence closed warmly on
  07-21. **The final synthesis email (guidance drafted 07-21) was never
  sent.** Consequence recorded in the program: the "keep reliable-grace URLs
  reachable while the reference stands" constraint has **lapsed** — W1's
  cutover is fully unblocked.
- **The websites cutover plan** (websites `docs/plans/site-consolidation-cutover.md`)
  is complete and prerequisite-cleared: KEEP the `superbot-websites` estate;
  RETIRE `review-…-f027` + `superbot-app` + `superbot-dashboard`; **HARD
  RAIL: the `reliable-grace` `worker` service is the LIVE Discord bot and the
  two Postgres DBs are infra — never touch.** Owner has now given the go
  (OD-8); sequence review → botsite → dashboard.
- **fm's `.session-journal.md` guidebook is an empty template** — placeholder
  headings, never filled. Now step D3's first target; the "documentation is a
  mess" verdict, measurable.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
python3 scripts/check_docs_links.py
```
