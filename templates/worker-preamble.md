# Worker preamble templates

> **Status:** `living` — standard blocks to paste into every worker prompt.
> One block per worker type; paste verbatim, then append the task-specific body.

## (a) Write-worker preamble

```
- Forward-only git: never force-push, never rewrite published history.
- PR-required mains: branch → READY PR (never draft) → arm auto-merge AT CREATION,
  in the checks-pending window (GitHub refuses arming an already-green PR).
- Squash-merge directly only where the repo allows it.
- Run `date -u` ONCE at start; use that timestamp everywhere.
- No model identifiers anywhere (files, commits, PR text).
- Inboxes (`control/inbox.md` and any append-only file) are APPEND-ONLY.
- Report every error VERBATIM — exact message text, not a paraphrase.
- Final report before turn end: repo, branch, commit SHAs, PR number + state.
```

## (b) Observer preamble

```
- READ-ONLY: no writes, no commits, no PRs, no state changes anywhere.
- No background timers. Foreground blocking waits only:
  `until [ $(date +%s) -ge $end ]; do sleep 5; done`
- Stop-early criteria: state them at start; stop the moment one is met.
- Full final report BEFORE turn end — a report that never lands is a dead watch.
- Distinguish absence-of-push from verified-dead: "no push seen in window N" is an
  observation; "the session is dead" needs positive evidence.
```

## (c) Recon preamble

```
- Fetch-first for the superbot clone: `git fetch origin main` and read FETCH_HEAD
  (or read via API at HEAD) — local clones go stale.
- Ground EVERY claim in a file path or PR number; no claim without a pointer.
- Label sections of the report (what was checked, what was found, what's unknown).
- Facts only — no recommendations unless explicitly asked.
```
