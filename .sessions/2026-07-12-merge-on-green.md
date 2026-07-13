# 2026-07-12 — merge-on-green: permanent landing path for READY claude/* PRs

> **Status:** `complete`

📊 Model: fable-5

## What this session did

Shipped `.github/workflows/merge-on-green.yml` (PR #146) — the repo's
own landing workflow: on check completion / PR readiness or label
events / a half-hourly cron / manual dispatch, it sweeps every open,
READY (non-draft), same-repo `claude/*` PR into `main`, verifies EVERY
check run on the head SHA is completed+success (pending or missing =
skip this round), and squash-merges directly with `GITHUB_TOKEN`. No
agent merge call anywhere. Permanent fix for PRs landing "at random"
(owner directive, live coordinator chat 2026-07-12T23:00Z).

References (fleet-audit-corrected mid-session by the coordinator — the
first draft wrongly modeled sim-lab's enabler + branch-rules counting):

- websites `.github/workflows/host-automerge-extras.yml`
  @ 0aeb803f07dea996ed19fee1ee9efec220a0a363 — sweep shape (cron +
  workflow_dispatch), direct `gh pr merge --squash` landing, and the
  workflow-touching-PR rail.
- idea-engine `.github/workflows/auto-merge-enabler.yml`
  @ 819a8d57e21f7793ccf9e707ba62649b8b969f60 — in-progress session-card
  SKIP, fresh `do-not-automerge` label re-read, injection-safe argv/env
  handling, `Head-ref:` squash provenance.

Guards: `do-not-automerge` / `owner-held` labels = ratification park
(fresh API re-read, skipped); `.github/workflows/**` in the diff =
owner-merge-only (PR #146 parks itself under its own rail, by design);
in-diff `.sessions/*.md` card still `in-progress` = skip (born-red
means "more commits coming"); check verification is GENERIC — all
check runs on the head SHA completed+success, zero check runs = not
verified = skip (no reliance on branch-protection rules counts: the
rules API reported ZERO required contexts live, PR #146 run
29214147939); `--match-head-commit` pins the verified SHA so a race
push can't land unverified; the workflow's own `merge-on-green` check
run is the single documented self-exemption (an event-triggered sweep
is in_progress on the head it evaluates).

Verified: YAML parses, embedded python compiles, `bootstrap.py check
--strict` green. Sibling note: the shared checkout at
/home/user/fleet-manager was mid-merge on branch pr143 (coordinator
merge lane) — this session moved to an isolated git worktree instead
of touching it.

💡 Session idea: **fleet landing-path audit column** — add a roster
column recording each seat repo's verified landing path (native
auto-merge enabler / sweep workflow / documented owner-click), and a
periodic audit slice that re-verifies it (does the workflow exist on
main? did the last 3 claude/* PRs land without a human merge call?).
Today's stall existed precisely because "how PRs land here" was nowhere
recorded per-repo; dedup-checked docs/ideas/ + docs/roster.md — not
previously proposed.

⟲ Previous-session review: today's landing stall burned roughly an hour
of owner attention because the seat probed the classifier PR-by-PR
instead of shipping the structural fix first — merge-on-green should
have been slice #2 the moment the native-auto-merge wall was confirmed.
Workflow improvement: when a wall is confirmed structural (not
transient), the next slice is the permanent path around it, not another
probe of the wall. This session repeated a smaller version of the same
class — it modeled the fix on a reference's *name* before reading the
fleet's real files — and the coordinator's audit caught it mid-flight;
citing path@SHA before writing a line is the cheap prevention.
