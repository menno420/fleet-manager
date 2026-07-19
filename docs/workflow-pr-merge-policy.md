# Workflow-PR merge policy — agent-merge after Codex-clean

> **Status:** `binding`
>
> Extends R29 (owner never reviews PRs) + R24 (@codex review relay) to the last
> owner-click they left standing — the `.github/workflows/**` rail. Owner
> direction, live 2026-07-19.

## Rule

The owner never reviews or merges PRs (R29). Workflow-touching PRs
(`.github/workflows/**`) historically waited on an owner click only because the
CI `GITHUB_TOKEN` cannot push workflow-file changes — a technical wall, not an
owner-review gate. That click is removed: the **fleet agent path** (the Claude
GitHub App token — short-lived and workflow-capable) merges a workflow-touching
PR once, **at merge time and bound to the exact head SHA**, it verifies ALL of:

1. **Codex reviewed the current head commit** (the exact SHA about to merge, not
   a stale earlier commit); its review is **not `CHANGES_REQUESTED`**; and it
   left **zero P1/P2 findings** — checked in BOTH the inline review comments and
   the review summary body.
2. **Every check on the head is green** — check runs **and** legacy commit
   statuses.
3. The **resulting head workflow** does not pair secret / environment access
   with outbound network egress. Scan the WHOLE file at head (not just added
   lines — a PR can add only egress for a secret already present) and include
   interpreter and `/dev/tcp` egress, not just `curl`/`wget`. Anything
   ambiguous — including a diff GitHub returns with no `patch` because it is too
   large — is a **STOP**: route to the owner queue, do not merge.

The check is done by the **merge-side agent at the real head**, never delegated
to a mutable label or a cached signal: a label has no SHA binding and no
workflow-only provenance, so it must never be the merge authorization. Codex
replies stay governed by **R24** (untrusted until verified); Codex is used as a
*gate*, fail-safe in direction — a fabricated finding only ever blocks a merge.

## Why not a CI auto-gate

The first attempt (fm PR #362, **closed**) put this in a CI workflow that
labelled PRs `codex-cleared`. Codex's own review found ~7 critical bypasses: a
label is forgeable; added-lines-only scanning misses a pre-existing secret; a
missing `patch` was read as safe; stale clearance survived a new commit; and
check-name exemptions were attacker-controllable. The lesson: this belongs on
the merge-side agent re-checking the real diff at the real head, not in a CI
label anything can set. And **no workflow-merge-capable PAT is ever stored as a
repo secret** — that would be the exact credential an exfil PR targets.

## Residual risk (named, not hidden)

With no human in this path, Codex plus the agent's merge-time re-check are the
last line on workflow changes; an AI reviewer can in principle be manipulated by
wording crafted to elicit approval. The whole-file secret+egress scan covers the
classic exfiltration case deterministically; the residual is non-zero. This is
an accepted, owner-directed trade — destructive-tier holds under R29 (prod
cutover, prod-data delete/import, token swaps, spending money) are unchanged.
