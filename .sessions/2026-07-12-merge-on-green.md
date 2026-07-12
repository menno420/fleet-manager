# 2026-07-12 — merge-on-green: permanent landing path for READY claude/* PRs

> **Status:** `in-progress`

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
(skipped); pending required check = not ready; zero required contexts =
refuse (never merge ungated); `--match-head-commit` pins the verified
SHA so a race push can't land unverified; born-red interplay intact —
substrate-gate stays red until the session card flips `complete`, so
nothing lands early by design.
