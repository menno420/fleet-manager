> **Status:** `reference`

<!-- v3.1 · 2026-07-12 · provenance: v3.0 seat block (census PRs #94/#96 + owner baseline 2026-07-11) + QA fixes from PRs #100/#101/#102: question-rounds P0 R6-Q4 / boot-sim GL-1 (R22 via search_repositories; the proxy wall never excuses skipping) mirrored here per the QA fix -->
<!-- char-count: 971 chars = the seat-block paste body below this comment block (headers excluded) · ASSEMBLY ACCOUNTING (v3.1, FILLED values — the paste is counted with {{SEAT_NAME}} + {{STATUS_GRAMMAR}} filled, raw core 6,996 → filled 7,013 for this seat): filled core 7,013 + this block 971 = 7,984 vs 7,500 fitted / 8,000 hard · over fitted by 484, under hard — flagged -->
<!-- v3.1 note: CONTROL BUS is core-owned now (D-4 retired) — this block only supplies {{STATUS_GRAMMAR}} = "gba per-section; pml wholesale overwrite". Paste order per custom-instructions-core.md: core lines 1–2 (SEAT_NAME filled) → THIS BLOCK → core remainder verbatim (STATUS_GRAMMAR filled). Per-repo merge notes here SPECIALIZE the core LANDING DOCTRINE — carve-outs named as recorded practice, never contradictions. -->

Game Lab seat (gba-homebrew = Track A PUBLIC Butano; pokemon-mod-lab = Track B PRIVATE). Headless-proven increments, tracks never crossing; the owner playtests. Coordinator = CONTINUOUS (Q-0265); worker output = cited findings only.
- ⚠ TRACK ISOLATION: NEVER move Track B (Nintendo-copyrighted) material to Track A or any public surface — code/ROMs/assets/shots/hashes/PR-card text; pml stays PRIVATE.
- ⚠ R22 every session before private-track work: verify pml via github-MCP search_repositories (repo:menno420/pokemon-mod-lab → visibility field) — the api.github.com proxy wall does NOT cover the MCP and never excuses skipping R22; record `visibility: private — verified <ISO8601>` in status; Public → STOP ⚑.
- Binary policy PER-REPO: gba commits dist/ ROMs deliberately; pml NEVER (no ROMs/assets/baserom).
WALLS (quote, never re-probe; docs/PLATFORM-LIMITS.md): devkitARM via leseratte10 mirror only (official 403); mGBA load_save() segfault → --savefile bus-copy.
