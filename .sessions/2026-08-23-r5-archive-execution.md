# 2026-08-23 — R5 executed: the nine ungated repositories are archived

> **Status:** `complete` — branch `claude/r5-archive-execution-4dsvoh`, cut
> from `origin/main` at `ffc0c3b` (fm #911), landed as fm **#912**. Flipped
> after `python3 bootstrap.py check --strict` returned a real exit 0 on this
> tree, read directly and never after a pipe.

- **📊 Model:** opus-5 · high · docs-only

## 💡 Session idea

R5 is the step OD-3 has described since 2026-07-26 and that has **never run on
any repository**. Its input landed 2026-08-22 (fm #906, the disposition table)
and the owner's go-ahead is recorded at `OQ-ESTATE-ARCHIVE-LIST` — covering the
**nine ungated rows**, not the three gated on GCB-1/R2.

This session executes it: the § 4 pre-archive writes first (an archived repo is
read-only), then the archive itself, then the records.

It is also three capability probes the estate has never made, because nothing
here has ever been archived: whether the archive `PATCH` succeeds agent-side at
all, whether archiving stops **scheduled Actions**, and whether an archived repo
still appears in `search/code` — the last one decides whether every future
account-wide dependency sweep is blind to archived repos.

## previous-session review

The previous card (`2026-08-22-pre-archive-writes-baton.md`, fm #907) executed
§ 4 item 1 and left items 2–4 named. Its carried correction — *when a
disposition turns on "X cannot affect Y", read the thing that decides it, not
the artifact's presence* — is directly load-bearing here: the archive's effect
on crons and on code search are exactly that shape, and neither is settled by
reading GitHub's docs, which are silent on both. So both get measured, not
reasoned.

## What landed

**The nine are archived.** `superbot-games` · `superbot-idle` ·
`superbot-mineverse` · `trading-strategy` · `codetool-lab-sonnet5` ·
`codetool-lab-fable5` · `codetool-lab-opus4.8` · `Substrate-kit-app` ·
`proxybench`. Confirmed by a fresh `GET /user/repos` after the run — **26
repositories, 9 archived, 0 deleted** — plus an individual `GET` per repo, so
the confirmation is a re-read and not the API's own 200. The three gated rows
were not touched; nothing was deleted.

**The § 4 pre-archive writes went first, and all of them.** Item 1 was already
done (#145). Items 2, 3 and 4 landed here, each verified live *before* any
archive call:

- **Item 4, both halves, on all nine** — a README notice inserted after the
  existing H1, and an updated GitHub description. The four kit-seeded repos by
  PR with a session card and green `substrate-gate` (games #186, idle #177,
  mineverse #146, trading-strategy #164); the three labs by PR; the two
  unprotected repos by direct commit.
- **Item 2** — each lab README now says the tool is **FINISHED and
  UNMAINTAINED**, names its last release, and says a release cut days before an
  archive does not imply upkeep. fable5's also records that the PyPI name
  `envdrift` belongs to an unrelated project.
- **Item 3** — `proxybench` #1 read (body: `capability probe`), commented,
  closed `not_planned`; `open_issues_count` now 0.

**The notice that does the most work is `Substrate-kit-app`'s.** That repo's
README is `substrate-kit`'s verbatim, so until today nothing in its tree said
what it actually is. The archive freezes that defect permanently — which is
precisely why the correcting notice had to go in before the archive, not after.

## What was measured, not assumed

Three things this estate had never verified, because nothing had ever been
archived. All three are in `docs/CAPABILITIES.md`:

1. **The archive `PATCH` works agent-side** — 200 over direct-PAT egress, nine
   times, no refusal and no classifier block.
2. **An archived repo stays installable** — `pip install
   "git+https://github.com/menno420/codetool-lab-sonnet5"` → **real exit 0**,
   `cfgdiff --version` → `cfgdiff 0.1.1`. That upgrades a `REASONED` claim the
   estate had flagged for testing. The mirror image proves the archive is real:
   a contents `PUT` to archived `proxybench` → **403, _"Repository was archived
   so is read-only."_**, while the read kept working.
3. **Archiving does not hide a repo from `search/code`** — 292 hits before and
   292 after.

## The finding worth more than the step

**`search/code` covers 3 of this account's 26 repositories.** Measured *before*
any archiving, with a positive control: the same query form returns 308 / 472 /
292 hits against `fleet-manager`, `substrate-kit` and `superbot-games`, and
**zero** against eight others — each using a term I had first read in that
repo's own README. So the zeros are coverage, not syntax.

That matters because a recorded `MEASURED` claim rests on the opposite
assumption: the disposition table § 3 cleared `Substrate-kit-app` with
*"account-wide search: nothing in the other 25 repositories references it."* A
zero from an unindexed repository is indistinguishable from a genuine absence,
so that sweep never established its conclusion. It may still be true — it is
just not evidence.

**What I did not do with that:** re-open the archive. The row rests on *value*
(evidence of what one Gemini one-shot produced), not on the sweep, and archiving
is reversible. Where it genuinely bites is the **deletion** call § 2 defers, and
deletion is the estate's one irreversible door — so the correction is recorded
next to that call, not used to relitigate a reversible one. Guard recipe:
for a completeness claim about this account, clone-and-grep, or run the per-repo
probe first and state which repos the sweep could see.

This is the previous card's carried lesson landing again — *when a claim turns
on "X is not there", check the thing that decides it* — and this time the thing
that decides it was whether the search index could see the repo at all.

## Still open, and deliberately not stalled on

**Whether archiving stops scheduled Actions.** Two facts recorded: after the
archive, all six of `superbot-idle`'s workflows still read `state: active`, and
the last scheduled run was `2026-08-23T05:42:49Z` (the 41st, unbroken daily).
An active definition the scheduler never calls looks identical from here, so
this is *not* the answer. The next window is up to 24 h out, which is why the
check is left as one call rather than waited on:
`GET /repos/menno420/superbot-idle/actions/runs?event=schedule&per_page=3` after
2026-08-24 ~06:00Z. A run in the 05:40–05:46Z window means archiving does not
stop crons and the estate's cron cleanup is separate work; no run means this
archive list was also the cron cleanup.

## Pre-existing, named so it is not re-derived

`python3 scripts/check_owner_queue.py` flags `[no-items] no numbered items
parsed from the Active queue region`. Checked against the unmodified tree
(`git stash`): **identical flag, exit 1, before any of my edits**. It is
advisory and not introduced here.

## Verify

`python3 bootstrap.py check --strict` → **exit 0**, read directly, never after a
pipe. Before the flip it returned 1 on the designed born-red hold alone.
