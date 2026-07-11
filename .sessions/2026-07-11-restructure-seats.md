# 2026-07-11 — Fleet restructure slice 1: the 8 standing seats (registry)

> **Status:** `in-progress`

📊 Model: Claude (Fable family, fable-5) · start 2026-07-11T22:06Z · lane
worker executing the owner-directed fleet restructure (2026-07-11), slice 1.

## Declared at open (born-red)

Scope: restructure `projects/` to the owner's 8 standing Projects (branch
`claude/restructure-seats`; PR parks READY on green — merge is the
manager's call, NO auto-merge armed):

1. **Venture Lab** = venture-lab + trading-strategy (trading is
   RESEARCH-ONLY, holdout spent — contributes the backtest engine, not
   live trading) — `projects/venture-lab/` updated in place (seat name
   matches the dir); trading-strategy dir → merged-source stub.
2. **SuperBot World** = superbot-games + superbot-idle +
   superbot-mineverse (flagship = mineverse; OAuth login-CSRF fix BEFORE
   any secrets work) — new `projects/superbot-world/`.
3. **Game Lab** = gba-homebrew + pokemon-mod-lab (standalone; strict
   public/private track isolation) — new `projects/game-lab/`.
4. **Ideas Lab** = idea-engine + sim-lab (generate→verify INTERNAL) —
   new `projects/ideas-lab/`.
5. **Self Improvement** = substrate-kit — new `projects/self-improvement/`.
6. **SuperBot 2.0** = superbot (prod) + superbot-next — new
   `projects/superbot-2.0/`.
7. **Websites** — unchanged.
8. **Fleet Manager** — unchanged (manager seat).

RETIRED → single-file pointer stubs: codetool-lab-opus4.8,
codetool-lab-sonnet5, codetool-lab-fable5, mobile-lab, games-program,
superbot-retro. MERGED-SOURCE → single-file pointer stubs:
trading-strategy, superbot-games, superbot-idle, superbot-mineverse,
gba-homebrew, pokemon-mod-lab, idea-engine, sim-lab, substrate-kit,
superbot, superbot-next. Each new seat's `instructions.md` (≤7,500 chars)
carries the GEN-3 HYGIENE RIDER v5 (verbatim from superbot
`docs/owner/next-round-founding-prompts-2026-07-11.md` §2 @ `76d854d`) +
the Permissions & authority grant (verbatim from `projects/UNIVERSAL.md`
v4 @ `e1848ff`) + the 2026-07-11 incident riders. Coordinator/failsafe
prompts in new dirs are minimal placeholders — prompt re-sync is slice 2.
`product-forge` is NOT in the owner's 8-seat list — left untouched,
flagged for disposition.
