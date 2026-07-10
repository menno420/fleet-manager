# 2026-07-10 — Night-review audit landing (26 Q&A, first fully-autonomous night)

> **Status:** `in-progress`

📊 Model: Fable 5 (claude-fable-5) · fleet worker (review lane, commissioned) · start 2026-07-10T12:15Z (`date -u`)

## Declared at open (born-red)

Docs-only landing PR for the commissioned night review of the gen-2 fleet's
first fully-autonomous night (2026-07-09 ~22:00Z → 2026-07-10 ~06:30Z; 116 PRs
merged across 10 repos, zero stuck). About to land:

1. `docs/findings/night-review-2026-07-10.md` — the full audit: badge,
   plain-language executive summary (the night in 10 sentences), the complete
   26-question Q&A by cluster (questions verbatim, answers in one voice,
   evidence kept), "For the Anthropic email" (send-ready platform findings),
   "Recommendations before scaling" (ranked), and an honest "Where we were
   lucky" section. Sources: the eight discovery digests (fm, kit, trading,
   venture, games, superbot, web-games-next, telemetry), each verified at live
   GitHub HEAD, plus live checks made during the answer passes (fm
   `docs/capabilities.md` at `41c4250`, substrate-kit at `21d3ead`, the
   `repo.private` bit for all 13 repos).
2. `docs/findings/README.md` — index row for the new findings doc.
3. `docs/dispatch-log.md` — one dated dispatch section for this landing.

Landing: born-red card holds substrate-gate red; flips `complete` as the
deliberate last commit; REST merge-on-green (R21 — born-red shape, no arm
attempt). Re-read main at HEAD `41c4250` before composing (R19; no newer
commits at open).
