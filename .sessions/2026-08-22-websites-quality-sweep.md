# 2026-08-22 — the websites quality sweep that was green whenever it had nothing to do

> **Status:** `complete` — branch `claude/project-status-next-steps-hlj7p3`,
> restarted from `main` after fm #894 auto-merged. Flipped after
> `python3 bootstrap.py check --strict` returned a real exit 0 on this tree.

- **📊 Model:** opus-5 · medium · runtime bugfix

## Why a websites bug is in a fleet-manager card

The owner's directive covered two halves — *"final verification and reviews of
the repos, making sure the important ones are kept and improved"* — and the
archive half is blocked on his letter. The verification half is not, so it ran:
a CI-health sweep of the nine repos he keeps. Eight green; `websites` red.

## The defect

`quality-main-sweep` exists to close a real measurement gap: bot merges push to
main with the Actions `GITHUB_TOKEN`, GitHub's recursion guard suppresses the
push event, `quality.yml` never fires, and the new main HEAD carries no
`quality` check run. Every two hours the sweep should notice and dispatch one.

`gh workflow run quality.yml --ref main` was written **without `--repo`**, in a
job that deliberately has no checkout, so `gh` had no git remote to infer the
repository from:

    failed to run git: fatal: not a git repository (or any of the parent directories): .git

Landed as websites #511, squash `d2bba01`. The fix is the form the same script
already uses twice — both `gh api` calls name `${{ github.repository }}`.

## What the numbers actually say — and the correction that produced them

The first version of this claim said *"7 of the last 7 runs failed"* and *"it
has never done so"*, read off the 30 most recent **repository-wide** runs.
**Codex round 1 refuted it** (`[conceded]`, P2): that sample cannot carry an
all-history claim, and it named the reason it was probably false — runs exit 0
before the dispatch line when a quality check already exists.

It was false. Re-measured against the workflow's own run list: **361 runs
exist; of the 100 most recent, 71 succeeded and 29 failed.** Reading the logs
by branch is what made it useful:

| sampled | branch | outcome |
|---|---|---|
| 1 of 1 successes | `quality present … nothing to do` | exit 0 |
| 4 of 4 failures | `no quality check run on <sha>` → dispatch | died at `gh workflow run` |

**In every sampled case the workflow exited 0 when it had nothing to do and
died when it had work** — 5 run logs read out of 100 runs examined. That is
enough to justify the fix and not enough to say *never*, which is exactly the
distinction the first version collapsed.

**Why it survived:** a 71 %-green scheduled workflow reads healthy, it is green
precisely in the no-op case, the error lands *after* the decision is logged so
the log looks like a working sweep, and a second workflow
(`host-automerge-extras`) has a job also called `sweep` that is green — so
main's check list shows `sweep success` beside the failures.

## ⚑ The fix is NOT verified, and this card will not pretend otherwise

The post-merge dispatch ran green and took the **`quality pending`** branch — a
quality run was already in flight on the new main HEAD — so it exited without
touching the repaired line. **The dispatch path has not been exercised since the
fix.** It proves itself on the next bot merge that lands with no quality run;
until then the fix is correct-by-construction (it matches two working calls in
the same script) and unproven in execution. Recorded here rather than claimed,
because the whole defect above is what happens when a green run is read as
evidence of work done.

## 💡 Session idea

**A scheduled job that is green on its idle path and red on its working path
reports the exact inverse of its health.** The success rate rises the less it
does; a run that finds work is the only kind that can fail, so the greener the
history looks, the less the job has been doing. No checker here distinguishes
"exit 0 because done" from "exit 0 because nothing to do". **Guard recipe:** for
any conditional scheduled job, emit a distinguishable marker per branch and
alert on *the working branch never having succeeded within N days* — not on the
failure rate, which is the misleading statistic. Anchors:
`websites/.github/workflows/quality-main-sweep.yml`, whose three branches
already print distinct strings, so the marker exists and nothing consumes it.

## ⟲ Previous-session review

fm #893's card claimed a red run that was not a failure (cfgdiff's PyPI job) and
was right to record it in three places. It missed the mirror image, which this
session then walked into twice: **a green run that is not a success.** The pair
is one lesson — a run conclusion is a summary of the wrong thing — and #893 had
half of it while writing the sentence that should have produced the other half.

Its judgement to keep `current-state.md` untouched under the 7000/7000 budget
still holds, and still blocks: this session's work is again unrecordable on the
live ledger, so it lands in the program §7 and here instead. Second session
running.
