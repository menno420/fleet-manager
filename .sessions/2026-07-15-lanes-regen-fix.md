# 2026-07-15 — lanes-regen-fix (fm slice: lanes.json generation-counter lag under automated regen)

> **Status:** `in-progress`

- **📊 Model:** Claude Fable (Claude 5 family) · high · tooling+docs

## What is about to happen

Self-initiated grooming slice (flagged from the roster-regen-0810 card): the
Actions roster-regen workflow stages only docs/roster.md + evidence-index +
owner-queue-candidates, never `registry/lanes.json` — so lanes.json is stuck at
generation 56 while roster.md is at Gen #58 (cron PRs #224/#226). Fix the
workflow's diff-check/stage step to include registry/lanes.json, and bring
lanes.json current to the committed generation without desyncing roster.md.
Plus heartbeat + checkers + session enders.
