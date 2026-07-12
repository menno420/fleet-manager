# Research — overnight program reports

> **Status:** `living-ledger`
>
> Committed reports from dedicated research programs (multi-agent censuses,
> prompt-architecture studies) and QA audits. Each doc is `reference` — dated,
> citation-heavy, and a snapshot of its census moment: verify claims against
> the repos before acting on them (playbook R2). Each entry gets a link line
> below when it merges; reports on unmerged branches are not listed (no
> dangling links).

| Date | Report | Scope |
|---|---|---|
| 2026-07-12 | [QA boot simulation](2026-07-12-qa-boot-simulation.md) | Boot simulation of the v3 startup prompt set — per-prompt verdicts + defect list |
| 2026-07-12 | [QA question rounds](2026-07-12-qa-question-rounds.md) | Multi-direction question rounds against the prompts-v3 set (89 questions, 6 perspectives) |
| 2026-07-12 | [QA incident replay](2026-07-12-qa-incident-replay.md) | Wave 3 replay of the shipped prompts-v3 set (`docs/prompts/v3/` @ 8056b7e) against the 80-entry incident register: 50 PREVENTED / 19 WEAKLY-PREVENTED / 3 NOT-PREVENTED / 8 NOT-PROMPTABLE, 12 contradictions, 8 duplication-drift blocks, and the v3.1 fix-priority table (BLOCKERs: I-63, I-69, I-78) |
| 2026-07-12 | [Problem census — core repos](2026-07-12-problem-census-core.md) | superbot, superbot-next, websites, substrate-kit, fleet-manager, product-forge — input for regression-proof startup prompts / Project instructions |
| 2026-07-12 | [Staleness sweep — first 8-seat sweep](2026-07-12-staleness-sweep-8seat.md) | Per-repo heartbeat-vs-git verification across all 8 seats (14 repos): 1 STALE (superbot-games), 1 FRESH-borderline (trading-strategy), 12 FRESH; 783-trigger snapshot; 9-item needs-attention shortlist; roster gen #12 cross-check (8 verdict mismatches) |
| 2026-07-12 | [Staleness sweep — midday 8-seat + v3.3 adoption](2026-07-12-staleness-sweep-midday.md) | 6 FRESH / 2 STALE seats; superbot-world 3/3 STALE, game-lab new STALE; adoption: fm v3.3, websites v3.2, rest pre-rebuild; 832-trigger snapshot + roster gen 14 |
