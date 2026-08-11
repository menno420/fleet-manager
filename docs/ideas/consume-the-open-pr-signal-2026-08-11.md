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
actually **observed** firing (`route_docs.py`, 2026-08-10) — one direct-REST call
listing open PRs with their head branch and changed paths, printed only when the
list is non-empty.

**Why worth having:** the estate mandates *raising* the claim signal and mandates
nobody *reading* it. `.claude/skills/session-close/SKILL.md:45` requires a
born-red card and a ready PR so that parallel sessions can see the claim; no
skill, hook or checker requires a session to look at what other sessions have
claimed. A one-directional protocol is invisible to its own gate — every checker
here verifies that a session **emitted** its signals, none verifies that a
session **consumed** anyone else's.

That cost real work on 2026-08-10. fm #838 was opened at 17:59Z against the stale
`shiftlife` pointer and the unreachable roadmap. An hour later a second session
began on the same root cause, never looked, and landed fm #839/#840/#841 across
the same files. #838 was left `dirty` and un-mergeable; its residue had to be
salvaged by hand in fm #842 and the PR closed as superseded. Both sessions did
their own job correctly. The overlap was not a judgement failure, which is why
another instruction would not have prevented it — it is the shape the protocol
has.

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

**Why it might not be worth having — state this honestly before building.** It
puts a network call on the prompt path, which is the one place latency is felt
directly; it needs `$GITHUB_PAT` and must degrade to silence rather than to an
error when the credential is absent or the call fails. And the estate has
withdrawn hooks before for being noisy: on a repo with a steady stream of open
PRs this fires on **every** prompt, and a line that appears every turn stops
being read by about the third one. The narrow version — fire once per session,
only when an open PR's changed paths **intersect** the files this session has
touched — is the one worth measuring, and it is strictly harder than the naive
version because it needs the session's own edit set.

**Route:** a `UserPromptSubmit` hook alongside `route_docs.py`, which already
solves the once-per-session dedup problem and the silent-unless-relevant rule
(`.claude/hooks/README.md` design rule 2). Advisory only; this estate has exactly
one denying hook and this is not a candidate to be the second.

**Status:** captured, not approved. Announced as a follow-up in fm #842's card
and in fm #838's closing comment — recorded here because both of those are
`RECORD` tier, and a commitment kept only in a record is a commitment nobody
actions.
