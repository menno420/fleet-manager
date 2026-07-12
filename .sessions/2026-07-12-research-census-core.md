# 2026-07-12 — Problem census: core repos (research)

> **Status:** `complete`

📊 Model: fable-5 · start 2026-07-12T~00:00Z · boot worker dispatched by the
overnight research coordinator

## Declared at open (born-red)

Problem census — core repos (superbot, superbot-next, websites, substrate-kit,
fleet-manager, product-forge); deliverable
`docs/research/2026-07-12-problem-census-core.md`.

## Close-out

Assembled six parallel read-only census reports into
`docs/research/2026-07-12-problem-census-core.md`: per-repo verdicts table,
top-10 fleet-wide problems ranked by regression risk (websites owner-panel
CSRF folded into #8 as a bounded, shippable security finding), six condensed
per-repo sections with all file@sha / PR# / run-id citations preserved, and a
consolidated prompt-implications section (every-Project boilerplate ·
per-Project specifics · owner/tooling asks). Parked PRs #88/#89/#91/#92
untouched. PR #94 parks READY — per doctrine (UNIVERSAL v4 §2.4) this session
does not merge or arm its own PR. Known risk: the roster-freshness 4h bar
(census top-10 #3) reds `claude/*` pushes from ~00:25Z — if this PR shows that
red, it is the stale-roster class, not this diff.

## 💡 Session idea

Keep the six per-repo census files as **reusable fleet primitives**: commit
them (or their next generation) under `docs/research/census/<repo>.md` with a
`verified-against: <sha>` header, so prompt-writing sessions can diff a repo's
*current* state against its last census instead of re-running a full six-agent
sweep — the census becomes an incremental ledger rather than a one-shot report.

## ⟲ Previous-session review

The prior session in this lane (born-red card open, PR #94) did the open-fast
discipline right: card + PR existed before any assembly work, making the lane
visible to the four parallel research sessions. What it could have done better:
the card's "Declared at open" named the deliverable but not the input contract
(six scratchpad census files) — a resumed worker had to get that from the
coordinator prompt rather than the card. Workflow improvement: born-red cards
for multi-worker research lanes should name their expected inputs, so a
takeover session can locate them without the dispatcher.
