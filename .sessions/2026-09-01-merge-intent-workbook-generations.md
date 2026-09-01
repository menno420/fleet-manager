# 2026-09-01 — point the intent-workbook generations at each other

> **Status:** `complete` — pushed, PR open, preflight run clean.

- **📍 Venue:** Claude Code, local (Menno's laptop, not the cloud pipeline)
- **Requested by:** Menno directly, after a laptop-side investigation found
  the estate has asked him the same intent questions in five separate
  document generations since late July, without closing the earlier ones.

## Mission

Not a repo-internal session in the usual sense — this ran from outside the
estate's own agent loop, at the owner's direct request, after a 33-agent
research pass (on his laptop, saved to its own hub as
`Hub/records/2026-09-01 fleet-manager owner-intent duplication map.md`)
mapped every generation of "tell us your intent" document across
`fleet-manager` and cross-referenced it against the other 27 repos.

**Caveat on that research pass, worth recording honestly:** it read this
repo from a resident local clone rather than a fresh fetch, so its picture was
about 5 hours stale by the time this session started — it missed fm #997-#1006
entirely (the `agents/`, `successor/`, `you/`, `products/` expansion, the
`OWNER:` marker convention, `PROGRESS.md`). This session re-verified against a
fresh clone before touching anything; the edits below are narrower than the
original research recommended as a result, scoped to what was confirmed still
accurate.

## Shipped

Added `VERIFIED`-labelled pointers (no deletions, per `HOW-TO-ANSWER.md`'s own
convention) so an already-answered question doesn't get asked a second time:

- `owner/intent-workbooks/repositories/{spider-bot,spider-swing,substrate-kit}.md`
  — each now cites its matching `docs/repos/<name>/intent.md` and quotes the
  owner's existing answer inline, rather than leaving the same question open
  in both places with no link between them.
- `docs/planning/2026-08-28-owner-intent-questions.md` — noted §1 is answered
  by `estate/why-this-estate-exists.md`, and §4 overlaps `agents/` and
  `docs/owner-queue.md`'s `OQ-INTENT-WRITE-UP`.
- `owner/choose-estate-archive-shape.md`, `owner/choose-estate-folder-structure.md`,
  `owner/fill-repository-purposes.md` — each pointed at its newer
  `owner/intent-workbooks/` counterpart.
- Regenerated `owner/README.md` and `owner/intent-workbooks/PROGRESS.md` via
  their own generators (never hand-edited).

## What this does NOT do

Does not touch the new `agents/`/`successor/`/`you/`/`products/` layer added
today — whether `estate/how-agents-should-work-with-you.md` now duplicates the
new `agents/` folder is flagged to the owner but not investigated here.
`owner/choose-estate-migration-order.md` and `owner/triage-recorded-ideas.md`
are genuine orphans (no Gen-5 counterpart) and were left untouched rather than
guessed at.

## Verification

- `python3 scripts/preflight.py` → all 9 checks exit 0, including owner-index
  drift and workbook-progress drift (both regenerated, both current).
- Diffed both regenerated files before committing: only the `generated-at`
  timestamp changed, confirming the edits added no new `❓` lines and no new
  `OWNER:` markers (still 1/74 answered — unchanged, honestly).
