# 2026-08-22 — the first pre-archive write executed, and the record now says so

> **Status:** `complete` — branch `claude/estate-repo-dispositions-spa3i0`,
> restarted from `origin/main` at `0e461ff` after fm #906 merged, landed as
> fm **#907**. Flipped after `python3 bootstrap.py check --strict` returned a
> real exit 0 on this tree, read directly and never after a pipe.

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

## What landed

**The write itself, in the repo it belonged to** — superbot-mineverse #145,
merged `fc7c349`, verified by re-reading that repo's `main`. Corrected in place
with the bullet struck through, header re-badged HISTORICAL, so the historical
handoff survives beside the correction. Bounded by a sibling search that
returned **zero hits**, so the family had exactly one instance and no follow-on
is owed.

**Then the three record repairs here**: § 4 item 1 marked done so R5 does not
redo merged work; § 6's merge recommendation withdrawn to the confidence its
evidence actually carries; and the plugin-hello justification upgraded from
"the files are there" to the host's own boot proof.

## The correction worth carrying

**I judged a change safe against a rule I had never read.** The file lists for
`superbot`'s eight open updates were measured here; the watch filter deciding
what they *do* is Railway service configuration, and `watchPatterns` has zero
hits in that repo — there was nothing in the tree to have read. The estate's
account of the filter is real but second-hand. Stating a merge-safety conclusion
on it was the error; the table's own `MEASURED` tag was already scoped correctly
to the file lists, and only the concluding sentence outran it — which is exactly
the half a later session would have acted on.

Same shape as the plugin-hello miss earlier in this thread: a vendored copy in
`examples/` was cited as proof the host does not fetch the standalone repo,
before anything confirmed the host *loads* that copy. Both were fixed by going
and reading the resolution path. Guard recipe for a later session: when a
disposition turns on "X cannot affect Y", the check is the thing that decides
it — the deploy config, the loader, the entry point — not the artifact's
presence. Anchors: `docs/planning/2026-08-22-repo-dispositions.md` § 6 and its
`superbot-plugin-hello` row.

## Verify

`python3 bootstrap.py check --strict` → **exit 0**, read directly. Before the
flip it returned 1 on the designed born-red hold alone.
