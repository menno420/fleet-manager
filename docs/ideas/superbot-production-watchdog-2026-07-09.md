---
state: captured
origin: owner
shipped_pr: null
shipped_repo: null
merged_date: null
outcome: open
---

# Production watchdog lane for superbot

> **Status:** `ideas`

**Idea:** a routine-driven lane that reads Railway production logs for the
live bot, writes incident reports as committed docs, and opens fix PRs for
what it can root-cause.
**Why worth having:** today production errors are only seen if the owner
happens to look; a watchdog turns the fleet's routine machinery into the
missing ops layer for its one live product.
**Unblocks:** incident history as repo data, faster fixes than
owner-noticed bugs, and the pattern every future deployed venture will need.
**Status:** captured (not approved)
