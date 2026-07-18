# 2026-07-18 · universal "Continue" resume prompt (new registry artifact)

> **Status:** `complete`

About to happen: add `docs/prompts/v3/universal-continue.md` — a new universal
paste artifact for RESUMING an existing project (post-night-run, after new
instructions, or to un-stall), distinct from the cold-start per-seat startups.
Owner-directed 2026-07-18. It tells a project to: resume and keep going; plan
when the execution backlog is drained; decide-and-flag on clear recommendations
(do it, explain what/why); and report genuine owner steps in plain,
link-included, easy-to-follow language, refreshing its own status/incomplete
file so the fleet roll-up stays current.

- **📊 Model:** opus-4.8 · high · docs-only

## What shipped
- `docs/prompts/v3/universal-continue.md` — the Continue resume prompt.

## 💡 Session idea
Pair the Continue prompt with a fleet-manager aggregator that, given the per-repo
incomplete-actions files, emits the consolidated plain-language owner-steps list
this prompt teaches each seat to produce — closing the loop the prompt opens.

## ⟲ Previous-session review
The prompt library had a cold-start artifact per seat and a session-ender, but no
mid-life "resume/continue" artifact — so a stalled project had nothing purpose-built
to re-paste. This fills that gap; the control-plane registration follows in websites.
