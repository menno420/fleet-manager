# 2026-07-12 — Research: problem census — satellite repos

> **Status:** `complete`

📊 Model: fable-5 · research worker dispatched by coordinator · start 2026-07-12 (born-red at open)

## Declared at open (born-red)

Problem census — satellite repos: superbot-games, superbot-idle,
superbot-mineverse, gba-homebrew, pokemon-mod-lab, venture-lab,
trading-strategy, idea-engine, sim-lab, superbot-plugin-hello, plus
one-paragraph checks of archived codetool-lab-opus4.8/-sonnet5/-fable5.
Deliverable: `docs/research/2026-07-12-problem-census-satellites.md`.
Part of the owner-directed overnight program to build regression-proof
startup prompts per fleet Project.

## Done

Shipped `docs/research/2026-07-12-problem-census-satellites.md` on PR #96:
synthesis of the five census fragments (SuperBot World, Venture Lab, Game
Lab, Ideas Lab + plugin-hello, archived codetool labs) into one doc with an
executive verdict table, a top-10 regression-risk ranking, the five fragment
bodies (citations preserved verbatim), and a per-seat + cross-fleet
prompt-implications rollup framed against the 8-seat restructure shape
(`projects/README.md` on `claude/restructure-roster`; PRs #88–#92 untouched).

Per-repo verdicts: superbot-games STALE · superbot-idle FRESH ·
superbot-mineverse STALE · venture-lab STALE · trading-strategy
FRESH-marginal · gba-homebrew FRESH · pokemon-mod-lab FRESH · idea-engine
FRESH (but preflight gate exits 2 at HEAD) · sim-lab FRESH ·
superbot-plugin-hello DEAD/empty · all three codetool labs DARK (none
GitHub-archived).

Top-ranked risks: idea-engine CI gate broken at HEAD; Game Lab cross-track
leak / R22 dilution; mineverse CSRF fix PR #42 parked ahead of secrets
provisioning; trigger succession dying at chat archive (incl. PROPOSAL 010
loop stop); stale heartbeats/claims steering wakes.

Hygiene held: family-level model names only; no secret values (patterns /
env-var names only); "not measured" preserved where the fragments said so.
Claim file `control/claims/claude-research-census-sat.md` deleted at close
per `control/claims/README.md` §4.

💡 Session idea: the census found the same failure class in four repos —
session-bound triggers dying silently at chat archive. Worth a kit-level
`check` warning: heartbeat lists trigger IDs → checker flags when the
heartbeat's `updated:` stamp is newer than the last recorded re-arm receipt,
so wake-chain death is surfaced by CI instead of by the next missed cadence.

⟲ Previous-session review: the born-red card opener (previous commit
824d70b) did its one job well — PR #96 opened immediately with scope
declared, so five parallel fragment workers never collided with this lane.
Improvement: the card's declared scope didn't name the deliverable's
*consumers* (the 8 seat-prompt authors); a "who reads this next" line on
research cards would let the coordinator route follow-ups without opening
the doc.
