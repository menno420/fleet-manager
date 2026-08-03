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
| 2026-08-03 | [Gemini paid tiers for video review](2026-08-03-gemini-paid-tiers.md) | Whether a paid tier changes capability rather than quota, for gameplay-recording review: context window is the one real ceiling (32k / 128k / 1M), the token arithmetic that makes it bite on video, and a buy/don't-buy recommendation per tier |
| 2026-08-03 | [The spider-swing visual-QA Gem](2026-08-03-gemini-visual-qa-gem.md) | Paste-ready build for a gameplay-recording reviewer: system instructions, a source-derived on-screen-facts knowledge file, the per-clip message, and a four-point acceptance test |
| 2026-08-03 | [Verifying a Gemini report about spider-swing](2026-08-03-gemini-report-verification.md) | Claim-by-claim check of a deep-research report against the tree at `9642f50` — right about the engine and workflows, wrong about nearly every file path; plus seven errors found in the pre-existing grounding block |
| 2026-08-03 | [Reducing invented detail](2026-08-03-reducing-invented-detail.md) | Why "1,600 commits across 400 branches" was produced for a five-day-old repository, and the five-rule prompting procedure + `[SEEN]`/`[INFERRED]`/`[UNSURE]` marking convention that targets each mechanism |
| 2026-07-12 | [QA boot simulation](2026-07-12-qa-boot-simulation.md) | Boot simulation of the v3 startup prompt set — per-prompt verdicts + defect list |
| 2026-07-12 | [QA question rounds](2026-07-12-qa-question-rounds.md) | Multi-direction question rounds against the prompts-v3 set (89 questions, 6 perspectives) |
| 2026-07-12 | [QA incident replay](2026-07-12-qa-incident-replay.md) | Wave 3 replay of the shipped prompts-v3 set (`docs/prompts/v3/` @ 8056b7e) against the 80-entry incident register: 50 PREVENTED / 19 WEAKLY-PREVENTED / 3 NOT-PREVENTED / 8 NOT-PROMPTABLE, 12 contradictions, 8 duplication-drift blocks, and the v3.1 fix-priority table (BLOCKERs: I-63, I-69, I-78) |
| 2026-07-12 | [Problem census — core repos](2026-07-12-problem-census-core.md) | superbot, superbot-next, websites, substrate-kit, fleet-manager, product-forge — input for regression-proof startup prompts / Project instructions |
| 2026-07-12 | [Staleness sweep — first 8-seat sweep](2026-07-12-staleness-sweep-8seat.md) | Per-repo heartbeat-vs-git verification across all 8 seats (14 repos): 1 STALE (superbot-games), 1 FRESH-borderline (trading-strategy), 12 FRESH; 783-trigger snapshot; 9-item needs-attention shortlist; roster gen #12 cross-check (8 verdict mismatches) |
| 2026-07-12 | [Repo consolidation census — phase A](2026-07-12-repo-consolidation-census.md) | Owner-directed repo consolidation program, phase A: full-fleet census (19 repos, exact list_repos match) — 19-repo verdict table (11 KEEP, 5 KEEP-QUIET, 3 MIGRATE-THEN-ARCHIVE, 0 ARCHIVE-NOW), trigger map, cost findings, 8-seat target shape (19 → 16 unarchived), phased reversible sequencing |
| 2026-07-12 | [Staleness sweep — midday 8-seat + v3.3 adoption](2026-07-12-staleness-sweep-midday.md) | 6 FRESH / 2 STALE seats; superbot-world 3/3 STALE, game-lab new STALE; adoption: fm v3.3, websites v3.2, rest pre-rebuild; 832-trigger snapshot + roster gen 14 |
| 2026-07-12 | [Prompt-currency audit — v3.3 vs kit + seats](2026-07-12-prompt-currency-audit.md) | Phase A (owner-directed): v3.3 finished but no longer fully current — kit v1.13/v1.14 same-day impacts, 8-seat drift verdicts (~15:30–15:40Z), and a merged 16-item v3.4 delta list (2 P0 · 11 P1 · 3 P2) |
