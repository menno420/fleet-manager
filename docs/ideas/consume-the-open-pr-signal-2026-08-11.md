---
state: captured
origin: lab
shipped_pr: null
shipped_repo: null
merged_date: null
outcome: open
---

# Make a session read the open-PR signal, not just raise one

> **Status:** `ideas`

**Idea:** inject the repository's open pull requests into a session's context at
its first turn, so a session learns about work already in flight before it starts
duplicating it. On `UserPromptSubmit` — the injection path this estate has
actually **observed** firing (`route_docs.py`, 2026-08-10).

**Why worth having — and the diagnosis was wrong the first time, which is the
interesting part.** This file was first written claiming *no rule requires a
session to read the signal*. That is false at HEAD, and Codex refuted it on
review: `control/claims/README.md` is badged **`binding`** and its step 1 says
*"**Before starting work**, scan this directory AND the open PRs. If your task is
already claimed or in flight, coordinate or pick something else."* The rule
exists, it is binding, and `docs/MAP.md:44` records `control/claims/` as the live
exception inside the otherwise-retired control bus.

So the real diagnosis is worse than a missing rule, and more familiar: **the rule
is written, binding, and not delivered.** It lives in `control/` — the directory
every orientation surface here correctly teaches sessions to treat as retired
seat-era apparatus — so a session that follows the boot file faithfully never
reads it. Nothing in the six mandatory reads, the boot file's task-routing table
or any hook puts it in front of anyone at the moment it applies. And nothing
checks it: every checker in this estate verifies that a session **emitted** its
signals, none verifies that a session **consumed** anyone else's, so the
un-followed rule leaves no trace.

That is exactly the case `docs/intent.md` § 4 legislates for — *"the fix for an
unfollowed rule is a mechanism that delivers it at the right moment, never
another statement of it."* **Anyone building this must start by reading the
existing rule and asking why it failed**, not by treating the ground as empty.
A second statement of a rule nobody reaches is the failure this repo is named
after.

That cost real work on 2026-08-10. fm #838 was opened at 17:59Z against the stale
`shiftlife` pointer and the unreachable roadmap. An hour later a second session
began on the same root cause, never looked, and landed fm #839/#840/#841 across
the same files. #838 was left `dirty` and un-mergeable; its residue had to be
salvaged by hand in fm #842 and the PR closed as superseded. Both sessions did
their own job correctly, and the binding rule that would have prevented it was
sitting in a directory both had been taught to ignore.

**Route facts already measured, so the build does not rediscover them:**

- **Route, not wall:** a bare `gh pr list` 403s at GraphQL here — *"only the
  pinned set of PR-review operations is served"* — while the same listing over
  direct-PAT REST (`curl --noproxy '*' … /repos/{owner}/{repo}/pulls?state=open`)
  returns **200**. Re-confirmed 2026-08-10; `docs/CAPABILITIES.md:738` already
  carries it, **including the `gh` route this session did not use**:
  `GH_TOKEN="$GITHUB_PAT" no_proxy='*' HTTPS_PROXY= gh <command>` works. Either
  path is fine for the build; the ledger entry is the reference, not this file.
- `SessionStart` is the intuitive hook and is **not wired here**;
  `python3 bootstrap.py hook session-start` runs clean and emits nothing, so its
  injection path is unverified. `UserPromptSubmit` injection is `MEASURED`.
  Building on the intuitive one would ship a hook nobody can prove fires.
- **The open-PR list is one call; the changed paths are not.**
  `GET /repos/{owner}/{repo}/pulls?state=open` returns the PRs and their head
  refs and **no file list** — that needs the separate, paginated
  `GET /repos/{owner}/{repo}/pulls/{n}/files`, one request per PR. This repo
  already calls it, at `scripts/r30_merge_check.py:366`, with paging and a page
  cap; reuse that shape rather than re-deriving it. Any design that promises a
  path intersection off "one REST call" has not been costed: it is 1 + N
  requests on the prompt path, which is most of the argument against the narrow
  version below.

**Why it might not be worth having — state this honestly before building.** It
puts a network call on the prompt path, which is the one place latency is felt
directly; it needs `$GITHUB_PAT` and must degrade to silence rather than to an
error when the credential is absent or the call fails. Once-per-session firing
answers the noise objection this estate has withdrawn hooks for before — but it
replaces it with a **one-shot** problem, which is worse in a different way: the
line appears exactly once, at the busiest moment of the session, and if it is
skipped there is no second chance. `route_docs.py` has the same property and is
the place to measure whether once-only injection is actually read.

**A security constraint the implementer does not get to skip.** This repository is
**public** (`docs/owner-queue.md` § Parked — *"this owner queue is on the open
internet"*), so an open PR can be authored by anyone, and its title is
attacker-controlled text. Injecting titles verbatim into the first-turn context
is a prompt-injection path that opens **before the session has done anything**.
Render the list as bounded, structured, clearly-delimited data — number, head
ref, truncated title — carrying an explicit statement that the contents are
untrusted metadata to be read, never instructions to follow. A hook that hands
raw external strings to a fresh model context is not shippable in this repo
regardless of how useful the signal is.

**And the obvious narrowing does not work — Codex refuted it on review.** Filtering
to open PRs whose changed paths **intersect this session's own edit set** is
silent exactly when it is needed: at the first `UserPromptSubmit` the session has
touched nothing, so the intersection is always empty, and by the time it is
non-empty the duplicate work is already written. The filter is well-formed and
solves the wrong end of the timeline.

**Route:** a `UserPromptSubmit` hook alongside `route_docs.py`, which already
solves the once-per-session dedup and the silent-unless-relevant rule
(`.claude/hooks/README.md` design rule 2). Fire it **once, on the first prompt of
the session**, listing every open PR with its title and head ref — the cheap
`?state=open` call, no per-PR file requests, no relevance filter. Relevance on
turn one can only come from the prompt text or the session's stated scope, and
matching a title against a free-text prompt is the kind of meaning-mechanising
this repo has already withdrawn two gates for. One list, once, at the only moment
it can still change what the session does. Advisory only; this estate has exactly
one denying hook and this is not a candidate to be the second.

**Sequencing:** the delivery half is cheap and the enforcement half is not, so
they are separable — deliver the existing binding rule first (the hook, or a
route in the boot table, or both), and only then ask whether anything should
verify that a session consumed it.

**Status:** captured, not approved. Announced as a follow-up in fm #842's card
and in fm #838's closing comment — recorded here because both of those are
`RECORD` tier, and a commitment kept only in a record is a commitment nobody
actions.
