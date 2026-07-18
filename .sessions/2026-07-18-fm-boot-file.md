# 2026-07-18 · fleet-manager boot file (main-repo migration prep)

> **Status:** `complete`

About to happen: fleet-manager has NO auto-loaded `.claude/CLAUDE.md`, so a fresh
session booting here loads nothing — the single blocking gap for migrating the
hub boot repo from superbot to fleet-manager. Add a lean `.claude/CLAUDE.md`
written for a FRESH HUB READER (not the coordinator seat): boot triad · fleet map
/ reading-path / owner-queue pointers · the verified capabilities ledger + the
"record capabilities, never limitations" doctrine · how to act on any repo · the
hub aggregation role · the live-owner precedence rule · keep-going. Excludes
seat-only content (wake chain, failsafe cron, "you are the coordinator") which
would mislead a one-off session.

- **📊 Model:** opus-4.8 · high · feature build

## What shipped
- `.claude/CLAUDE.md` (new) — the fresh-hub boot file above. Adding it also
  resolves the dangling `docs/AGENT_ORIENTATION.md` pointer to this file.

## Sequencing (owner-side step remains)
The actual boot-repo switch is owner-side environment config (claude.ai/code →
Environments — a documented platform wall agents cannot edit). This file must
exist BEFORE that switch, or the first fresh boot loads nothing. This PR is that
prerequisite; the file is inert until the environment points fresh sessions here.

## 💡 Session idea
A per-repo `control/incomplete.md` convention (seeded via the kit) + a
fleet-manager aggregator (sibling to `gen_roster.py`) that rolls every repo's
incomplete-action file into one hub list — the standing mechanism behind the
owner-steps roll-up.

## ⟲ Previous-session review
The fleet-manager repo has been the coordinator seat's home but never had a
generic boot file, because every session here was assumed to be the seat. The
migration exposes that assumption: a fresh hub session and a persistent seat are
different readers, and the repo should greet both — the seat via its pasted
prompt, everyone else via this file.
