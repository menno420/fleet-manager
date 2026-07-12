# Agent-permission port — `.claude/settings.json` (2026-07-11)

> **Status:** `reference`
>
> Landed via PR #92.

## Why

A fleet-manager landing session was denied merging verified CI-green PRs by
the auto-mode permission classifier ("Merge Without Review … run outside auto
mode"). Owner direction (2026-07-11): port superbot's agent permission rules
so auto-mode sessions here can land green PRs without classifier denials.

## Provenance

- **Source:** `menno420/superbot` `.claude/settings.json` at origin/main HEAD
  `fae8bd0a543638ff5ee0e7bd039b8990b2048c60` (verified live 2026-07-11 via
  `git fetch` + `git show origin/main:.claude/settings.json`).
- **What superbot explicitly grants** in `permissions.allow` for GitHub MCP:
  `mcp__github__pull_request_read`, `mcp__github__list_pull_requests`,
  `mcp__github__create_pull_request`, `mcp__github__update_pull_request`,
  `mcp__github__merge_pull_request`, `mcp__github__subscribe_pr_activity`,
  `mcp__github__unsubscribe_pr_activity`, `mcp__github__get_file_contents`,
  `mcp__github__list_commits`, `mcp__github__get_commit`,
  `mcp__github__get_job_logs`, `mcp__github__actions_list`.
- **Ported here:** exactly that explicit GitHub-MCP set — the landing lane
  (open/update/merge a PR + read files/commits/CI logs to verify green).
  Mirror, not expansion.

## Deliberately NOT ported (decide-and-flag)

Superbot's file also carries broader grants that exceed landing needs; they
were left out on purpose (owner can widen later if wanted):

- `"defaultMode": "bypassPermissions"` + `"skipDangerousModePermissionPrompt": true`
  — whole-harness bypass, far wider than the landing denial being fixed.
- A bare `"mcp__github"` server-wide allow (covers every GitHub MCP tool,
  incl. repo-creation/file-deletion) and bare `"mcp__Claude_Code_Remote"` etc.
- Superbot's large `Bash(...)` allow/ask lists and its hooks block — those are
  superbot-environment-specific (Python 3.10 toolchain, its scripts/).
- `enable_pr_auto_merge` is not explicitly granted by superbot and is not
  granted here — fleet-manager's plan cannot use the auto-merge toggle on
  private repos anyway (`docs/capabilities.md`, owner-verified 2026-07-10;
  landing lane = REST merge-on-green, R21).

## Activation

The rule is active only once this file is on `main` — the PR that carries it
parks READY on green for the owner's hand-merge (no auto-merge, no
self-merge).
