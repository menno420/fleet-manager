# 2026-07-12 — repo consolidation census (phase A)

> **Status:** `complete`

📊 Model: fable-5 · start 2026-07-12 ·
research worker (repo consolidation census, phase A)

## Declared at open (born-red)

Phase A of owner-directed repo consolidation program: full-fleet census (identity/activity/assets/cost/verdict per repo) → docs/research/2026-07-12-repo-consolidation-census.md

## Close-out

- **Deliverable:** `docs/research/2026-07-12-repo-consolidation-census.md` — the full phase-A census, synthesized from 5 parallel worker reports (setup / core / kit-planted / game-product / labs clusters), indexed in `docs/research/README.md`.
- **Verdict roll-up (19 repos, exact list_repos match):** 11 KEEP (superbot, superbot-next, substrate-kit, fleet-manager, websites, idea-engine, sim-lab, venture-lab, trading-strategy, pokemon-mod-lab, gba-homebrew) · 5 KEEP-QUIET (codetool-lab-opus4.8, superbot-games, superbot-idle, superbot-mineverse, superbot-plugin-hello) · **3 MIGRATE-THEN-ARCHIVE** (product-forge, codetool-lab-sonnet5, codetool-lab-fable5) · 0 ARCHIVE-NOW.
- **Target shape:** 8 seats → repo mapping; post-consolidation **19 → 16 unarchived repos**; phased reversible sequencing (agent PRs → owner-queue decisions → owner-only settings clicks; migrations before archive toggles, nothing deleted).
- **Key negative findings preserved:** venture-lab "trading engine absorbed" premise DISPROVEN; superbot-plugin-hello "empty" finding STALE (seeded `bbaccec` 13:29Z); codetool labs inert but `archived:false` ×3; pokemon-mod-lab `main` unprotected (only one in fleet); branch-protection rules unverifiable fleet-wide (403 quoted once in the methods note).
- **Trigger cross-check:** no armed trigger references the 3 MIGRATE-THEN-ARCHIVE repos; trading-strategy + venture-lab (both KEEP) carry live triggers.

💡 Session idea: the census's verdict table should become a machine-readable sidecar (`docs/research/census-verdicts.json`: repo → seat → verdict → date) that `scripts/gen_roster.py` ingests, so the roster's per-repo disposition and the latest census can never disagree — the same one-source-of-truth fix the midday-sweep session proposed for sweep verdicts, extended to consolidation verdicts; phase-1/2/3 progress could then be checked off against it mechanically.

⟲ Previous-session review: the midday staleness sweep (#113) was thorough (832-trigger snapshot, 8 verdict mismatches caught against roster gen #12) — but its "superbot-world 3/3 STALE" and the earlier sweep's "plugin-hello empty / codetool labs DARK" labels were snapshot claims that this census found stale or over-strong within hours (plugin-hello was seeded the same day; the labs are STALE-BY-DESIGN, not DARK). Improvement: sweep reports should stamp per-claim verification timestamps and mark repo-state claims as perishable (verify-before-reuse), which the census doc now does explicitly in its own Status banner and Negative-findings section.
