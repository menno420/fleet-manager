# 2026-07-12 — research: prompt-currency audit (v3.3 vs kit + seats)

> **Status:** `complete`

📊 Model: fable-5 · start 2026-07-12 ·
research worker (Phase A prompt-currency audit)

## Declared at open (born-red)

Phase A audit: is the v3.3 prompt set finished and still current vs substrate-kit v1.13/v1.14 and per-seat reality; deliverable docs/research/2026-07-12-prompt-currency-audit.md.

## Outcome

Deliverable shipped: `docs/research/2026-07-12-prompt-currency-audit.md`
(+ README link row). Synthesis of a three-worker fan-out (kit deep dive ·
per-seat drift review verified ~15:30–15:40Z · v3.3 finishedness sweep).

**Verdict:** v3.3 is structurally finished (v3.2 defect queue closed
checker-verified, registry 24/24) but no longer fully current — same-day
kit releases (v1.13.0/v1.14.0) plus afternoon seat activity produced a
merged, deduped **16-item v3.4 delta list (2 P0 · 11 P1 · 3 P2)**. P0s:
the park-green dictionary entry over-promises non-author review-merge
(PR #113 "cross-session permission laundering" denial, itself unrecorded)
and the fm CI landing-path line contradicts its own startup source.
Landing-path staleness in 4 seats (websites #167 enabler, sim-lab #50,
trading #74, mineverse #42 CSRF); 3 kit-doctrine staleness lines (WALLS
never-re-probe vs 14-day rule, six-field ask missing RISK:, BOOT-4
verify-exists vs verify-delivers); 4 unrouted kit surfaces (docs/SKILLS.md,
/intake, docs/ROUTINES.md pending release, seat-digest regen wiring).
Six coordinator flags incl. the kit lab-loop.md:102 falsified claim and
the stagger-table/live-trigger drift. Byte-budget caveat recorded: delta 1
(+~64 chars) breaks the 8,000-byte CI gate on superbot (7,996) and
websites (7,997) without a compensating trim.

💡 Session idea: auto-generate the seats' MERGE MECHANICS / landing-path
lines from live workflow listings (which enabler/merge-on-green files exist
at each repo HEAD) the same way the kit's seat-digest fences feed
walls/skills — four seats' hand-stamped merge lines went stale within ~5
hours of v3.3 landing today, so this line class should be rendered, never
hand-written.

⟲ Previous-session review: the midday staleness sweep (PR #113) was
accurate at its census moment but its landing-path facts aged within hours
(websites/sim-lab/trading enablers all flipped the same afternoon) — which
itself argues for delta-generation over hand-restamps; it also declared a
forbidden REST merge-on-green landing path in its own PR body, which the
v3.3 dictionary failed to prevent (now delta 1/P0).
