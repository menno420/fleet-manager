# 2026-08-22 — the first pre-archive write executed, and the record now says so

> **Status:** `in-progress` — branch `claude/estate-repo-dispositions-spa3i0`,
> restarted from `origin/main` at `0e461ff` after fm #906 merged. Flips to
> `complete` after `python3 bootstrap.py check --strict` returns a real exit 0.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

fm #906 landed the disposition table and, in its § 4, a **pre-archive write
list** — things a repo still needs written before it goes read-only. Item 1 was
the sharp one: `superbot-mineverse`'s coordinator baton told the next session to
delete a trigger, which this estate forbids, against a trigger that no longer
exists. **It has now been executed** — superbot-mineverse #145, merged
`fc7c349`, verified live on their `main`.

Two record repairs follow, and both are about not leaving a false statement
standing:

1. § 4 item 1 still reads as pending work. R5 executes from that list, so a
   stale item means someone redoes a merged fix.
2. § 6's dependabot conclusion states flatly that three PRs *"can be merged at
   any time with no live effect"*. The file lists behind that are measured; the
   **deploy rule they were judged against is not** — `watchPatterns` has zero
   hits in `superbot` and there is no `railway.json`, so the filter is Railway
   service configuration this session never read. The table's `MEASURED` tag is
   already correctly scoped to the file lists; the conclusion sentence is not,
   and that is the half a later session would act on.

## previous-session review

The previous card (`2026-08-22-estate-repo-dispositions.md`) produced the table
this one repairs. Its own close-out named the § 4 list as work available without
the owner — this session did the first item rather than leaving it named. Where
it was wrong: it stated the dependabot conclusion at a confidence its evidence
did not carry, which the owner-review hook caught after the merge; the fix is
below rather than argued away.

## What this will carry when it flips

- item 1 marked done with its evidence, and the sibling check that bounds it
- the § 6 provenance qualifier, and the exact read that would settle it
- the verify line with its real exit code
