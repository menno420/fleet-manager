# 2026-07-12 — merge-on-green: permanent landing path for READY claude/* PRs

> **Status:** `complete`

📊 Model: fable-5

## What is about to happen

Author `.github/workflows/merge-on-green.yml` — a repo-owned REST
merge-on-green workflow that squash-merges open, READY (non-draft)
`claude/*` PRs the moment EVERY required check on the head SHA is
completed+success, using `GITHUB_TOKEN`. No agent merge call, no native
auto-merge toggle needed (unavailable on this repo/plan). This is the
permanent fix for PRs landing "at random" (owner directive, live
coordinator chat 2026-07-12T23:00Z).

Reference: sim-lab `.github/workflows/auto-merge-enabler.yml`
@ 26cbb1de65e654aac46b3667ea16806f4364e107 (repo ref f4d3e02) — its
guard shapes (refuse-on-zero-required-contexts, fresh label re-read,
injection-safe env/argv passing, `Head-ref:` squash provenance) are
carried over; the merge action is adapted from "arm native auto-merge"
to "verify-then-REST-squash-merge", the landing path sim-lab's own
fallback note names for repos shaped like this one.

Guards: `do-not-automerge` / `owner-held` labels = ratification park
(skipped); pending required check = not ready; the required-context set
is the branch-rules API unioned with a non-empty hardcoded floor
(`substrate-gate`, `freshness`) so the gate can never be empty (never
merge ungated); `--match-head-commit` pins the verified
SHA so a race push can't land unverified; born-red interplay intact —
substrate-gate stays red until the session card flips `complete`, so
nothing lands early by design.

## What happened

Shipped `.github/workflows/merge-on-green.yml` (PR #146): sweep on
check_suite/workflow_run completion + PR readiness/label events; verify
every required context (`substrate-gate`, `freshness`) on the head SHA
is completed+success; squash-merge with GITHUB_TOKEN pinned to the
verified SHA. Verified: YAML parses, embedded python compiles,
`bootstrap.py check --strict` shows only the designed born-red hold.
LIVE FINDING (this PR's own first run, Actions run 29214147939): the
`rules/branches/main` API reports ZERO required contexts on this repo
— the checks are enforced outside a token-visible ruleset — so the
sweep now gates on the rules API unioned with a hardcoded floor
(`substrate-gate`, `freshness`); without the floor the workflow would
have safely refused forever and never merged anything.
Sibling note: the shared checkout at /home/user/fleet-manager was
mid-merge on branch pr143 (coordinator merge lane) — this session moved
to an isolated git worktree instead of touching it.

💡 Session idea: **fleet landing-path audit column** — add a roster
column recording each seat repo's verified landing path (native
auto-merge enabler / REST merge-on-green / documented owner-click), and
a periodic audit slice that re-verifies it (does the workflow exist on
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
probe of the wall.
