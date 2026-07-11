# 2026-07-11 — fleet restructure slice 2: prompt re-sync (coordinator + failsafe, all live seats)

> **Status:** `in-progress`

📊 Model: fable-5 · lane worker dispatched by coordinator (restructure program, slice 2 of the 2026-07-11 owner directive) · start 2026-07-11 (born-red at open)

## Declared at open (born-red)

Re-sync every `coordinator-prompt.md` + `failsafe-prompt.md` across the 8
standing seats (venture-lab, superbot-world, game-lab, ideas-lab,
self-improvement, superbot-2.0, websites, fleet-manager) to their slice-1
v2/v3 instructions: replace the v0 placeholders in the 5 new seat dirs with
real prompt bodies, refresh venture-lab/websites prompts to the merged seat
shape, and sweep product-forge + all live prompts for references to retired
or merged seats (codetool-lab-*, mobile-lab, games-program, superbot-retro,
trading-strategy-as-seat, superbot-games/idle/mineverse-as-seat,
gba-homebrew/pokemon-mod-lab-as-seat, idea-engine/sim-lab-as-seat,
substrate-kit/superbot-next-as-seat). Version stamps bumped with date
2026-07-11 + provenance (owner restructure directive 2026-07-11). Branch
`claude/restructure-prompts` STACKED on `claude/restructure-seats` (PR #88);
PR opens with base = `claude/restructure-seats`. No trigger calls, no merges,
no auto-merge arming — trigger re-arm/retire text ships as prompt+meta
content only.
