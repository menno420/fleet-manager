# 2026-07-09 — seed home repo + adopt substrate-kit

> **Status:** `complete`

- **📊 Model:** unrecorded-by-policy · standard · docs-only
  (fleet program policy: no model identifiers in committed files)

## Goal

Seed the fleet manager's home repo (playbook v1, worker templates, owner queue,
dispatch log, control heartbeat) and adopt substrate-kit v1.4.0 toward
`check --strict` green.

## What happened

- Bootstrapped the empty repo: first commit via Contents API (playbook R13), then
  git worked normally.
- Main is ruleset-protected (PR required) — seed content landed via `seed/home`
  READY PR #1, squash-merged.
- Adopted substrate-kit v1.4.0 (release asset, sha256-verified), answered all
  interview slots, rendered docs live, wired the staged CI gate
  (`.github/workflows/substrate-gate.yml`).
- Fixed check findings: badge tokens `living` → `living-ledger` (kit token set,
  playbook R14), linked the manager docs from `docs/AGENT_ORIENTATION.md`
  (reachability rule), wrote this first session card.

## 💡 Session idea

Add a tiny `scripts/heartbeat-check` (or reuse the kit's `check --status-only`)
to the manager's own wake ritual so a stale `control/status.md` is caught by the
manager itself before the owner notices the repo has gone dark.

## ⟲ Previous-session review

No previous session in this repo (first session). The gen-1 fleet day that led
here (see docs/dispatch-log.md) taught the R-series rules now in
docs/playbook.md — capturing them as the seed content was the improvement.
