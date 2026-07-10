---
state: captured
origin: lab
shipped_pr: null
shipped_repo: null
merged_date: null
outcome: open
---

# Review-queue drainer — a standing owner for post-merge review

> **Status:** `ideas`

**Idea:** the merge-authority law (owner directive 2026-07-09, blueprint §1)
makes review strictly post-merge — "merge anyway and flag it: one line in
`review-queue.md` … veto = revert" — but **no lane, routine, or order owns
draining `review-queue.md`.** Add a standing reviewer mechanism before gen-2
lanes accumulate flags: either a fleet-manager wake-routine step ("read every
lane's review-queue.md; for each open line, re-check the named concern
against the merged diff; clear the line or open a revert/fix PR; escalate
only genuine vetoes") or a dedicated cross-repo reviewer lane using a
**different model than the author** (the corpus' own external-oracle lesson:
real defects were found by judges and live fire, never by the author's own
green tests).
**Why worth having:** the fleet already proved what happens to a file nobody
is obligated to act on — inbox orders "stay new forever," and websites'
ORDER 005 sat acked-but-unexecuted behind a misleading PR title. Without a
drainer, review-queue.md becomes a graveyard and "review is post-merge"
silently degrades to "review is never" — on exactly the PRs a lane itself
judged to deserve second eyes. Distinct from the captured security-auditor
idea (weekly vuln/dependency scans): this is **correctness review of
self-flagged merges**.
**Unblocks:** makes the self-merge-always law safe at fleet scale; gives the
@Codex-mention path a fallback when Codex isn't watching.
**Provenance:** Fable-5 fleet review finding F10 (verified at HEAD —
policy quote verbatim-accurate; no drain rule anywhere in R1–R21, the
standing rituals, or any founding text; the independent 2026-07-10 doctrine
review missed this gap). Synthesis:
[`../findings/fable5-review-2026-07-09.md`](../findings/fable5-review-2026-07-09.md).
**Status:** captured (not approved).
