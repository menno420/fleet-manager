# Codex-gated merge — workflow-touching PRs

> **Status:** `binding`
>
> Extends **R29** (owner never reviews PRs) to the last owner-click it left
> standing — the `.github/workflows/**` rail. Owner direction, live 2026-07-19.

**Owner direction, 2026-07-19 (live):** *"remove my review from it completely — I
never look at it anyway, all it does is give me an extra click with 0 extra
guards."* Under **R29** the owner never reviews PRs; the only reason
workflow-touching PRs still waited on an owner click was the technical
`merge-on-green` workflow-file rail (the CI `GITHUB_TOKEN` cannot push workflow
changes). This removes that click by replacing it with an automated Codex gate.

## The rule

A PR whose diff touches `.github/workflows/**` is **merged by the fleet agent
path** (the Claude GitHub App token — short-lived, and able to merge workflow
files; the CI `GITHUB_TOKEN` cannot) **once, and only once, it carries the
`codex-cleared` label** applied by `.github/workflows/codex-gate.yml`.

`codex-gate` applies `codex-cleared` only when **all** hold:
1. **Codex reviewed the current head commit** (not a stale earlier commit), and
2. left **zero P1/P2 findings** on it, and
3. every check on the head is **green**, and
4. the added workflow lines are **not "exfil-shaped"** (they do not both read a
   secret / dump the environment *and* make an outbound network call — a
   deterministic regex backstop that, unlike an AI reviewer, cannot be talked
   down by wording inside the PR).

Codex replies stay governed by **R24** (untrusted until verified); here Codex is
used only as a *gate*, and the direction is fail-safe — a fabricated P1 merely
blocks a merge, and a fabricated "clean" review is backstopped by the
exfil-shape regex.

Other gate outcomes (agents must NOT merge these):
- **`needs-human-review`** — exfil-shaped diff. Route to the owner; never
  auto-merge.
- **`codex-flagged`** — Codex left a P1/P2. Fix or close; do not merge.
- **no label** — Codex has not reviewed the current head yet (the gate posts
  `@codex review` once per head and waits).

## Why not just auto-merge in CI

The CI `GITHUB_TOKEN` is not allowed to push `.github/workflows/**` changes. The
only way to make a CI job do it is to store a workflow-capable PAT as a repo
secret — which is exactly the credential a malicious "telemetry"-shaped PR would
read and exfiltrate. With no human in the loop that trade is strictly worse, so
the merge stays on the agent path and **no workflow-merge-capable token is ever
stored as a repo secret.** `codex-gate` itself holds only `GITHUB_TOKEN` and can
do nothing but label and comment.

## Residual risk (named, not hidden)

With no human anywhere in this path, **Codex's review is the last line** on
workflow changes. An AI reviewer can in principle be manipulated by wording
crafted to elicit approval; the exfil-shape regex covers the classic
secret-exfiltration case deterministically, but the residual is non-zero. This
is an accepted, owner-directed trade (destructive-tier holds under R29 are
unchanged).
