---
state: captured
origin: owner
shipped_pr: null
shipped_repo: null
merged_date: null
outcome: open
---

# Fleet security & dependency auditor

> **Status:** `ideas`

**Idea:** a weekly cross-repo sweep — vulnerability scan, secret scan,
dependency-update review — done with judgment (what actually matters, what
to pin vs bump), reported as a committed brief with fix PRs where safe.
**Why worth having:** the fleet now spans 10+ repos with pinned deps nobody
re-audits; a Dependabot-with-judgment beats both silence and notification
spam.
**Unblocks:** a security baseline before any venture takes real users or
real money; catches the rot that accumulates while lanes focus on features.
**Status:** captured (not approved)
