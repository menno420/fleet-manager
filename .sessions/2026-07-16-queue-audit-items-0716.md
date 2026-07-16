# 2026-07-16 — queue-audit records (wake session)

> **Status:** `complete`

Recording the PR-landing-audit owner actions (websites #359 manual merge, pokemon-mod-lab #87 conflict disposition, ready-flip trio) into the owner queue + an item-68 progress note, and refreshing the PM heartbeat.

- **📊 Model:** Opus 4.8 · high · fleet oversight (owner-queue records)

💡 Session idea: Owner-queue items spawned from a dated audit doc should carry an
optional `SOURCE-AUDIT:` field linking that audit (e.g.
docs/pr-landing-audit-2026-07-16.md), so a later reconciliation pass can batch-re-verify
a whole audit's items against live GitHub in one query instead of re-deriving each item's
provenance — turns a one-time audit into a re-checkable cohort. (Dedup-grepped
`docs/ideas/` + `docs/owner-queue.md` for SOURCE-AUDIT / audit provenance / audit-linked —
novel.)

⟲ Previous-session review: the sweep-stale-claim wake (PR #265) did the housekeeping
right — it verified the claim's lane terminal with live GitHub merge timestamps
(#262 @15:07Z, #263 @15:14Z) before deleting, rather than trusting the 72h age
horizon, and left an honest evidence-first card. What it missed: it spent an entire
wake reactively sweeping one obviously-dead claim, then re-filed the fix
(`claims-terminal-lane` watchdog) as a *future idea* — even though it had the exact
reproduction in hand. Improvement it surfaces: apply the Q-0194 "friction → guard"
discipline at the moment of friction — when a wake exists solely to clean up
predictable decay, the closing move should be to ship the cheapest enforcing check
then and there, converting the recurring manual-sweep wake into a one-time tooling
commit instead of another backlog entry that waits for its own future wake.
