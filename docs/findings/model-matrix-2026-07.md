# Fleet model matrix — 2026-07 (ORDER 010)

> **Status:** `reference` — built 2026-07-10T21:25Z by the Q-0265 continuation-chain
> slice #2 (same PR as roster generation #1). **Family-level model names ONLY**
> (Q-0262 / ORDER 008 policy 1). Basis: the newest ~3–5 session cards per repo
> (`📊 Model:` self-report lines), read at each repo's HEAD over git transport —
> bounded sweep, not a full-history census. Verify against repos before acting
> (playbook R2).

## Why this exists

Model attribution is **inconsistent across surfaces**: on the one evidenced routine
fire where surfaces could be compared — the **websites 16:01Z fire (2026-07-10)** —
the **Routines screen displayed fable-5** while the fired session's chat header showed
Sonnet 5 and its own card self-reports **`claude-sonnet-5`** (websites PR #59, squash
`2c89e96`; card `.sessions/2026-07-10-order008-first-fire-manifest-smoke.md`, verified
again at HEAD `1430f61` this sweep). `create_trigger` exposes **no model parameter**
and `list_triggers` carries no model field (re-confirmed on this slice's 99-record
sweep), so no agent-side pin or read-back exists. **Standing rule (already doctrine,
capabilities rider): per-session self-report on the card is the least-bad attribution
basis** — this matrix is that basis, aggregated once.

## Matrix (one row per repo; newest ~3–5 cards each)

"Project setting" = the model configured on the claude.ai Project. It is **not
agent-visible anywhere** — no API, no trigger field, no env var observed — so it is
UNKNOWN except where design records name it (codetool experiment arms).

| Repo | Project setting (from records) | Card-self-reported families (recent) | Routine-fired vs manual | Evidence |
|---|---|---|---|---|
| superbot (hub) | unknown | **fable-5** (worker + owner-live + prep cards) · **opus-4.8** on the autonomous docs-reconciliation routine card · newest shift-* cards carry **no `📊 Model:` line** (template gap) | Partially: reconcile-band1950 card is routine-fired = opus-4.8; shift cards indeterminable (and unlabelled) | `.sessions/2026-07-10-reconcile-band1950.md`, `-fleet-overnight-review.md`, `-eap-journal-routine-observability.md` @ `dc19b1e` |
| superbot-next | unknown | **fable-5** across all 5 newest (Builder seat) | Not card-labelled; the seat runs continuous mode (Builder failsafe wake + chain), so recent slices are chain/routine-paced — but cards don't say fired-vs-manual | `.sessions/2026-07-10-{hermes,leaderboard}-parity-flip.md` etc. @ `9e4180d` |
| substrate-kit | unknown | **mixed: fable-5 + opus-4.8** (3 opus, 2 fable in newest 5) | Not determinable from cards | `.sessions/2026-07-10-v171-payload.md` (fable-5), `-telemetry-write-at-commit.md` (opus-4.8) @ `a4369f3` |
| websites | unknown | **fable-5** on all 5 newest (several explicitly "routine-fired build slice (continuous mode)") · **sonnet-5** on the 16:01Z first-fire card | **Yes — best-labelled lane in the fleet:** cards state routine-fired explicitly. Fired sessions span **two families** (16:01Z = sonnet-5; 20:00Z wake slices = fable-5) under one unchanged trigger | `.sessions/2026-07-10-order008-first-fire-manifest-smoke.md` (sonnet-5) vs `-scheduled-healthcheck.md` (fable-5, routine-fired) @ `1430f61` |
| trading-strategy | unknown | **null — all 5 newest say "withheld per session policy"** (pre-Q-0262 convention; policy 1 un-nulls this going forward — family names are allowed and wanted) | Not determinable | `.sessions/2026-07-10-p5-holdout-evaluation.md` etc. @ `efaedf6` |
| venture-lab | unknown | **opus-4.8** (lane sessions, "[1m]" context marker) · **fable-5** (kit-upgrade distribution-wave card — manager-side visitor, not lane work) | Not determinable (lane has no trigger; all sessions manual/dispatched) | `.sessions/2026-07-10-round2-closeout.md` (opus-4.8) @ `ce22315` |
| superbot-games | unknown | **opus-4.8** (gen-1 mining close-out) · **fable-5** (gate/idea/kit visitor slices) | Not determinable (no trigger — all manual/webhook) | `.sessions/2026-07-10-mining-session-closeout-gen1.md` @ `4493292` |
| pokemon-mod-lab | unknown | **null — "game-lab lane default"** (no family name on any of the 5 newest) | Not determinable (no trigger) | `.sessions/2026-07-10-track-a-session-00{4..8}.md` @ `a76ada7` |
| gba-homebrew | unknown | **null — "Claude (ID withheld)"** on all 5 newest (pre-Q-0262 convention) | Not determinable (no trigger) | `.sessions/2026-07-10-session-{3..7}.md` @ `bc73da7` |
| product-forge | unknown | **fable-5** (seed) + **opus-4.8** (day-1 retro) — 2 cards total, young repo | Not card-labelled; seat is continuous-mode (failsafe wake firing) | `.sessions/2026-07-10-seed.md`, `-forge-day1-retro.md` @ `d2fd68d` |
| idea-engine | unknown | **fable-5** uniformly (5/5) | Not card-labelled; seat is continuous-mode (failsafe wake firing since ~20:00Z) | `.sessions/2026-07-10-*-first-batch.md` @ `aaff871` |
| sim-lab | unknown | **opus-family** (boot card) + **fable-family** (seed card) — 2 cards total | Boot/seed were dispatched (manual-class); failsafe wake armed since, no fired card yet at HEAD | `.sessions/2026-07-10-boot.md`, `-seed.md` @ `b36be88` |
| codetool ×3 (fable5 / opus4.8 / sonnet5) | **KNOWN by design** — the experiment arms were configured fable-5 / opus-4.8 / sonnet-5 respectively (harness-x-model experiment) | **null — no `.sessions/` exist** in any of the three repos | n/a (lanes wound down) | repos @ `a6cf1a9` / `80f6cd1` / `66c3dfc`; caveat: seat contamination — coordinator/wind-down seats ran fable-5 in at least the sonnet5 and likely fable5 lanes (`docs/experiments/README.md` § Standing caveats, ORDER 006) |
| fleet-manager | unknown | **fable-5** (this slice's card; the 18:31Z wake card kept its model line deliberately generic per its wake instructions) | Yes for this repo's chain slices (send_later-fired, self-reporting fable-5); the 18:31Z routine-fired card = null | `.sessions/2026-07-10-chain-order-009-010.md` @ this PR |

## Conclusions

**What the matrix CAN establish:**

1. **The fleet demonstrably runs at least three model families** (fable-5, opus-4.8,
   sonnet-5) across lanes on the same day, per self-reports.
2. **Routine-fired sessions are not pinned to one family**: the same websites trigger
   produced a sonnet-5 session at 16:01Z and fable-5 sessions at 20:00Z — direct
   evidence that the Routines screen's uniform "fable-5" display is not authoritative
   for fired-session identity (the known cross-surface disagreement, PR #59 / 2c89e96).
3. **Self-report coverage is uneven and convention-driven**: three whole lanes are
   nulled by pre-Q-0262 "withheld" conventions (trading-strategy, gba-homebrew) or a
   placeholder ("game-lab lane default" — pokemon-mod-lab); superbot's newest card
   template dropped the line entirely. ORDER 010's ground-truth step (instruct fired
   sessions to self-report family-level) is folded into lane contact per the ORDER;
   the Q-0262 policy already permits it everywhere.

**What the matrix CANNOT establish:**

1. **Any Project's configured model** — not agent-visible on any surface probed
   (no API field, no trigger field, no env var); every "Project setting" cell except
   the codetool arms is an honest unknown. Only the owner's UI shows it.
2. **Whether a given self-report is true** — a card line is the session's own claim;
   no independent read-back exists to audit it.
3. **Fired-vs-manual for most lanes** — only websites (explicit card labels),
   superbot's reconciliation routine, and fleet-manager's own chain slices are
   determinable; everywhere else the distinction is not recorded.

**Standing rule (already doctrine, restated):** per-session **self-report on the
session card is the least-bad attribution basis** — the Routines screen is NOT a
reliable attribution surface (`docs/capabilities.md` § routine self-arm rider). Lanes
still nulling their model line should adopt family-level names per Q-0262.
