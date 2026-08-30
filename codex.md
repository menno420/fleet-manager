# codex.md — DRAFT Codex delta for the future `estate` hub

> **Status:** `draft-for-owner-review` — proposed Codex-only facts. Shared rules
> belong in `AGENTS.md`. This file is planning evidence in fleet-manager until
> the `estate` cutover.
>
> **Last verified:** 2026-08-30 on ChatGPT Work unless a row says otherwise.

## How context loads

Codex reads `AGENTS.md` natively when the repository is present at task start.
ChatGPT Work can begin with an empty working directory; after cloning during a
session, deliberately read `AGENTS.md` and `codex.md` because neither earlier
repository context nor Claude's `.claude/CLAUDE.md` loads automatically.

`codex.md` is a routed delta, not a native boot file. `AGENTS.md` must point to
it for Codex work.

Repository-local Codex hooks may require the workspace to be trusted and may
not activate when the repository appears after the session starts. A quiet hook
is not evidence that a check ran; run the named check directly when it matters.

## Available access

In ChatGPT Work, use local git for the working tree and the connected GitHub
surface for remote operations. Measured in fleet-manager PR #835 on 2026-08-10,
that surface created a branch, commits, a ready PR, review replies, resolved
threads, read check runs, and returned a complete Actions job log; repository
metadata reported `admin: true` and `push: true`.

Do not probe for `gh` or `$GITHUB_PAT` on this surface. Their absence is not a
GitHub-access wall. If one connector operation fails, name that operation and
its error, then use another supported connector route if one exists.

## Surface limits and honest forms

ChatGPT Work does not expose a Claude session id. Use:

`- **🔗 Session:** unavailable — ChatGPT Work does not expose a Claude session id`

Use `chatgpt-work` as the venue. Codex cloud is a different surface; verify its
checkout, network, secrets, and remote-write access rather than copying this
row.

Shell exports and setup-time secrets may not survive into later task phases.
Network reachability can also be restricted by phase or allowlist. Inspect the
live environment and make one cheap attempt before recording a wall.

## Fallback

Run local repository checks with their documented plain command and capture the
real exit code. Use the connected GitHub surface to read remote checks and logs.
When the requested remote action is genuinely unavailable, leave an honest null
containing the exact attempted action, observed response, and safe next step.

