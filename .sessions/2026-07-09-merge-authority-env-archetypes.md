# 2026-07-09 — merge-authority policy + env archetypes + merge-queue verification

> **Status:** `in-progress`

📊 Model: Claude Fable 5 (claude-fable-5) · worker session · docs/policy/environments

## Declared at open (born-red)

Three owner directives (2026-07-09), one PR:

1. **Merge-authority policy** — gen-2 lanes ALWAYS land their own PRs
   (auto-merge armed at creation = the sanctioned self-merge path; REST
   merge-on-green R8 fallback). No PR waits for review: merge anyway + flag
   in a committed `docs/review-queue.md` ledger and/or @-mention Codex;
   review is post-merge, veto = revert. Kill do-not-automerge/owner-gated
   merge for gen-2 lanes. Folds into gen2-blueprint §1 + §2 and the
   venture-lab founding text; seed `docs/review-queue.md`.
2. **Environment consolidation** — ≤4 archetypes covering all current +
   planned projects; one TESTED defensive setup script + env var NAME union
   each; `environments/archetypes.md` mapping table + scripts; two-source
   layout test (the trading-strategy provision killer) demonstrated.
3. **Merge queue** — re-verify the open-PR sweep at live HEAD; commit
   `docs/merge-queue-2026-07-09.md` for the owner's merge session.

Then: owner-queue consolidation (one click-level environments item + merge-
queue pointer), handoff in-flight update, card flip, auto-merge verification.
