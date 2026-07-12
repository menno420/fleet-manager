# 2026-07-12 — registry sync: projects/ seat files to prompts v3.2

> **Status:** `in-progress`

📊 Model: fable-5 · start 2026-07-12 ·
lane worker (owner-directed 2026-07-12, dispatched by coordinator)

## Declared at open (born-red)

The projects/<seat>/ REGISTRY copies are stale — last synced by restructure
PR #89, which predates the overnight prompt rebuild (docs/prompts/v3, now
generation v3.2 stateless, PR #108). This session: for each of the 8 seats
(fleet-manager, superbot-2.0, websites, self-improvement, superbot-world,
game-lab, ideas-lab, venture-lab) regenerate coordinator-prompt.md /
instructions.md / failsafe-prompt.md from their docs/prompts/v3 sources
(regenerate-don't-fork, provenance headers, version bumps per each file's
own convention); minimal projects/README.md pointer update; ship a
--check-registry drift guard next to regen_b_files.py; close out + heartbeat.
