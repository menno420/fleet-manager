# 2026-07-11 — Port superbot agent-permission rules (.claude/settings.json) for auto-mode landing

> **Status:** `complete`

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

## What landed (PR #92)

- **`.claude/settings.json`** (new) — `permissions.allow` with exactly the 12
  explicit `mcp__github__*` grants superbot carries at
  `menno420/superbot` `.claude/settings.json` @ `fae8bd0a543638ff5ee0e7bd039b8990b2048c60`:
  pull_request_read, list_pull_requests, create_pull_request,
  update_pull_request, merge_pull_request, subscribe_pr_activity,
  unsubscribe_pr_activity, get_file_contents, list_commits, get_commit,
  get_job_logs, actions_list. Valid JSON verified via `json.load`.
- **`docs/findings/permission-rules-port-2026-07-11.md`** — provenance
  (source file @ SHA, owner direction 2026-07-11) + the decide-and-flag list
  of superbot grants deliberately NOT ported (`defaultMode:
  bypassPermissions`, bare `mcp__github` server-wide allow, Bash lists,
  hooks; `enable_pr_auto_merge` granted nowhere).
- **Claim lifecycle:** `control/claims/claude-permission-rules.md` rode this
  branch (main is PR-only — direct fast-lane push rejected: "Changes must be
  made through a pull request") and is deleted in this close-out commit.
- **Deliberately NOT done:** no auto-merge armed, no self-merge — PR #92
  parks READY on green for the owner's hand-merge.

## 💡 Session idea

**Permission-denial telemetry → allowlist PR loop:** when a fleet session
hits a permission-classifier denial, the denial string (tool name + rule
name, e.g. "Merge Without Review") should be appended to
`docs/capabilities.md` per its discovery rule AND surface as a one-line
paste-ready owner-queue candidate proposing the specific allow rule. This
session existed because a denial was only visible in a chat transcript; a
standing capture rule makes the next one self-service.

## ⟲ Previous-session review

The restructure stack (#88→#89→#91) declared merge order and no-auto-merge
discipline clearly in every PR body — good template, reused here. One miss
worth naming: slice PRs stack on branch bases, so the whole stack's CI truth
depends on #88's base staying fresh against main; none of the three cards
name a rebase-on-merge owner. Improvement: a stacked-PR card should state who
retargets/rebases when the base lands (GitHub retargets the base branch
automatically but does not rebase the diff), otherwise the last slice can go
stale-green.
