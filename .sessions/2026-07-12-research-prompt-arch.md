# 2026-07-12 · research-prompt-arch

> **Status:** `complete`

- **📊 Model:** fable-5 · high · research-worker

Research slice for the overnight prompt-set program: derive the requirements
spec for the v3 prompt set (universal startup template, per-project startup
prompts, per-project custom instructions, universal session-ender).
Deliverable: docs/research/2026-07-12-prompt-architecture.md.

Shipped: docs/research/2026-07-12-prompt-architecture.md — 24-entry failure→line
map, layer placement rules, steering-shape evidence, size budgets, 4 skeletons.
Parked READY+green on PR #95 for coordinator consumption — not merged by design.

Gate fix (post-open): substrate-gate redded this card on grammar (missing
💡 idea / ⟲ review / 📊 Model line) and the research doc on badge+reachability
(`research` is not an allowed badge token; doc was an orphan). Fixed: badge →
`reference`, doc linked from `docs/current-state.md` § In flight, card enders
added below.

## 💡 Session idea

A **research-doc lane in the badge taxonomy or a documented mapping**: this
session invented a `research` badge token because nothing in the allowed set
(`reference`, `plan`, …) obviously names "evidence spec consumed by a later
synthesis session," and CI caught it only after push. Either add a `research`
token to the kit taxonomy or state in `docs/AGENT_ORIENTATION.md` that
research deliverables badge as `reference` and link from current-state — one
line would have prevented this red.

## ⟲ Previous-session review

The 2026-07-11 UNIVERSAL-v4 merge-clause session was strong on byte-level
verification (`cmp` on both inserted occurrences) and on flagging the wake-stamp
bump as decide-and-flag. Miss worth naming: its card format (Model line +
enders) was correct because it copied a passing sibling — this session wrote a
card from memory instead and shipped without the grammar tokens, which is
exactly the drift the born-red gate exists to catch. Workflow improvement:
run `python3 bootstrap.py check --strict --session-log <card>` locally before
the flip-complete push, not only after CI reds.
