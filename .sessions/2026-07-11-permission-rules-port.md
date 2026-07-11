# 2026-07-11 — Port superbot agent-permission rules (.claude/settings.json) for auto-mode landing

> **Status:** `in-progress`

📊 Model: fable-5 · fleet-manager lane worker (owner-directed 2026-07-11) · start 2026-07-11T23:26Z (`date -u`)

## Declared at open (born-red)

Owner-directed port: a landing session in this repo was denied merging
verified CI-green PRs by the permission classifier ("Merge Without Review …
run outside auto mode"). About to land:

1. **`.claude/settings.json`** (new — repo has no `.claude/` today) — a
   `permissions.allow` list mirroring the GitHub-MCP landing grants superbot
   carries at `menno420/superbot` `.claude/settings.json` @ `fae8bd0` —
   minimally `mcp__github__merge_pull_request` +
   `mcp__github__update_pull_request` plus the read/CI-status equivalents
   superbot actually grants. Mirror, not expansion.
2. **`docs/findings/permission-rules-port-2026-07-11.md`** — provenance note
   (source file @ SHA, owner direction date, what was deliberately NOT
   ported).
3. This card, flipped `complete` as the deliberate last commit.

**Deliberately NOT doing:** no auto-merge arming, no self-merge — the PR
parks READY on green for the owner's hand-merge (the rule isn't active until
it's on main). Claim rides this branch (`control/claims/`) because main is
PR-only — direct fast-lane claim push was rejected by branch protection.
