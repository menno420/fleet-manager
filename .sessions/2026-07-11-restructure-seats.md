# 2026-07-11 — Fleet restructure slice 1: the 8 standing seats (registry)

> **Status:** `complete`

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

## Shipped (close-out, 2026-07-11T22:17Z)

All declared scope landed in one content commit (`684f21e`):

- **6 seat instructions authored/updated**, every one carrying VERBATIM the
  GEN-3 HYGIENE RIDER v5 (superbot
  `docs/owner/next-round-founding-prompts-2026-07-11.md` §2 @ `76d854d` —
  NOT previously present anywhere in this repo; see drift note below) + the
  Permissions & authority grant (`projects/UNIVERSAL.md` :45–:80 @ HEAD
  `1dea86d`, v4 provenance `e1848ff`) + the 2026-07-11 incident riders
  (byte-checked in-file). Sizes (wc -c): venture-lab 7,498 ·
  superbot-world 7,489 · game-lab 7,481 · ideas-lab 7,494 ·
  self-improvement 7,486 · superbot-2.0 7,499 — all ≤ 7,500.
- **Seat-specific constraints stated explicitly:** trading-strategy
  RESEARCH-ONLY / holdout SPENT / backtest engine not live trading
  (Venture Lab); mineverse OAuth login-CSRF fix BEFORE any secrets work
  (SuperBot World); standalone + strict public/private track isolation
  (Game Lab); generate→verify loop INTERNAL, no cross-project wait
  (Ideas Lab).
- **17 dirs → single-file pointer stubs** — retired (6):
  codetool-lab-opus4.8 / -sonnet5 / -fable5, mobile-lab, games-program,
  superbot-retro; merged-source (11): trading-strategy, superbot-games,
  superbot-idle, superbot-mineverse, gba-homebrew, pokemon-mod-lab,
  idea-engine, sim-lab, substrate-kit, superbot, superbot-next. History
  preserved in git; each stub names its successor + `git log` path.
- **New dirs carry meta.md + PLACEHOLDER coordinator/failsafe prompts**
  (v0, marked NOT deployed) — prompt re-sync is slice 2, as directed.
- **projects/README.md**: restructure banner added; MATRIX + paste-wave
  marked historical pending slice 2.

Flags for slices 2/3 (recorded in the new metas/stubs): still-ARMED old
triggers (games/idle/mineverse failsafes; superbot-retro failsafe + two
hourly child wakes) fire into RETIRED/MERGED seats until re-armed;
raw-fetch consumers of old `projects/<repo>/` paths now see stubs;
`product-forge/` is NOT in the owner's 8-seat list — untouched, needs
owner disposition. No ORDER in control/inbox.md covers this restructure
(latest = ORDER 018 + ORDER 017 update) — authority is the owner's direct
2026-07-11 restructure directive relayed by the coordinator.

## 💡 Session idea

The 7,500-char instructions cap is now consumed to within ~20 chars on
every seat by three mandatory verbatim blocks (~5,100 chars) — any future
rider addition will silently force body cuts. Cheap guard: a
`scripts/check_registry.py` that (a) asserts every `projects/*/
instructions.md` ≤ 7,500 bytes, (b) byte-verifies the canonical blocks
against their source-of-truth files, and (c) prints the remaining body
budget per seat — wired into bootstrap check or CI so a drifting block or
an over-cap paste blocks red instead of being found at paste time.

## ⟲ Previous-session review

The archive-prep closeout (PR #87) made the coordinator succession fully
durable — its handoff doc + retro meant this session needed zero chat
archaeology to understand seat state; exemplary. What it missed: it
verified triggers as live-and-rebindable but left no single table of
"trigger → seat it fires into", which this restructure needed and had to
reassemble from meta files. Concrete improvement: keep
`projects/_inventory/trigger-registry-*.md` regenerated whenever seats are
created/retired, so a restructure can see at a glance which armed triggers
now point at dead seats.

## Verification

- `python3 bootstrap.py check --strict` → only the designed born-red hold
  on this card (flips with this commit) + one pre-existing owner-action
  advisory on control/status.md (untouched by this PR).
- Canonical blocks byte-verified (`in`-check against extracted sources)
  in all 6 instructions files; wc -c per file recorded above.
- PR #88 parks READY on green — NO auto-merge armed; merge is the
  manager's call (restructure directive).
