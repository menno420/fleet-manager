# 2026-07-09 — game-lab founding package (two-track GBA venture)

> **Status:** `complete`

📊 Model: Claude Fable 5 (claude-fable-5) · docs+environments session · night (~23:40Z)

## Declared at open (born-red)

Owner decided tonight (2026-07-09): launch the **game-lab** venture, both
tracks — Track A: private Pokémon Emerald mod (pret/pokeemerald decomp);
Track B: public original GBA homebrew (Butano). A toolchain scout session
PROVED every loop in-container earlier tonight. This session commits the
founding package:

1. `docs/findings/gba-toolchain-proof-2026-07-09.md` — the scout's verified
   ground truth (verdicts, deps, build times, caveats) + findings README row.
2. `environments/archetype-gba-lab.sh` — defensive setup script (5th
   archetype) + `environments/archetypes.md` row + README map row.
3. `docs/prompts/game-lab-founding.md` — paste-ready gen-2 founding Custom
   Instructions (venture-lab-draft template) + prompts README row.
4. `docs/ideas/game-lab-2026-07-09.md` (decided — in founding) + README row.
5. `docs/owner-queue.md` — game-lab launch click-list item (R16/R17 fields).
6. Handoff + dispatch-log lines; capabilities.md GBA recipe append (R18).

Landing: born-red card holds the gate red; flips `complete` last; lands via
REST merge-on-green (R21 — no arm attempt; this repo is born-red by design).

## Done (all six deliverables, this PR)

- **Findings** — `docs/findings/gba-toolchain-proof-2026-07-09.md`: verdict
  per track (A: GO, byte-identical retail build 1m20s/2.0s; B: GO with
  supply-chain caveat, Butano sprites 17.5s via leseratte10 r68 mirror;
  headless mGBA loop ~290 fps with scripted in-game verification), dep
  lists, caveats index (mirror trust, mgba==0.10.2↔libmgba 0.10.x pin,
  devkitPro Cloudflare-403), provenance note (screenshots live in the scout
  session's chat). Index row added.
- **Environment** — `environments/archetype-gba-lab.sh` (defensive R15 shim
  on the setup-universal pattern: apt binutils-arm-none-eabi + mgba-sdl +
  zstd; pip mgba==0.10.2 pinned; devkitARM r68 mirror extract + make-rules/
  crt0 from devkitPro GitHub sources; agbcc auto-build on pokeemerald-shaped
  repos; unconditional exit 0). `archetypes.md` gains gba-lab as the
  **justified 5th archetype** (toolchain too heavy for python-lab) + mapping
  rows for both planned repos; README map row added. Mirror r68 dir + package
  names re-verified live this session
  (`.../devkitARM/r68 (2026-06-10)/*.pkg.tar.zst`).
- **Founding prompt** — `docs/prompts/game-lab-founding.md` on the
  venture-lab-draft template: two-track mission, verified ground-truth
  block, fleet ritual, R21 landing mechanics, provisional Tier-1 "ROM
  builds" <60s smoke CI (CI-tier standard in simulation, PR #12 — marked
  provisional), Class-A hourly wake, walking skeleton = build + headless
  screenshot in session 1, HARD RAILS (private/public split; never publish
  Track A anything; Track B external publishing owner-gated), ORDER 001
  draft (Track A: reproduce scout loop + 3 mod concepts w/ scope estimates;
  Track B: build-run one Butano example + 3 original concepts), deployment
  record NOT YET DEPLOYED. Prompts-ledger row added.
- **Idea entry** — `docs/ideas/game-lab-2026-07-09.md` (`state: promoted`,
  prose status **decided — in founding**) + README index row (own
  owner-decided cohort section).
- **Owner queue** — item 17: full launch click-list (gba-homebrew public +
  pokemon-mod-lab PRIVATE-empty with Allow auto-merge, one `game-lab`
  Project with the founding prompt, gba-lab environment, hourly routine,
  boot line) with R16/R17 WHAT/WHERE/HOW/WHY/UNBLOCKS fields.
- **Close-out** — handoff in-flight item + dispatch-log night-later section;
  capabilities.md GBA recipe (CAN) + devkitPro Cloudflare-403 (WALLED) per
  R18.

## 💡 Session idea

**Founding-package checklist as a template:** venture-lab and game-lab were
both founded by hand-assembling the same six artifacts (findings/corpus →
archetype/env → founding prompt → idea/decision record → owner-queue
click-list → handoff/dispatch lines). A `templates/founding-package.md`
checklist with the file paths + index rows each artifact must touch would
make every future lane founding mechanical and un-forgettable — the third
founding shouldn't have to reverse-engineer the pattern from the first two.

## ⟲ Previous-session review

The ideas+R21 session (#11) did the right structural thing: it converted
PR #10's landing friction into a numbered rule (R21) *with provenance in the
rule text*, and practiced it on its own landing. Two improvables it left:
(1) its 9 captured ideas all record `captured (not approved)` but none carry
a rough size/cost line, so the grooming pass that picks among them will
re-derive scope from scratch — idea files should carry a one-line effort
guess at capture time; (2) it updated the archetypes serving-list for
venture-lab but left the "≤4 archetypes" framing as an absolute, which this
session had to soften the moment a justified 5th appeared — directives with
numeric bounds should record the bound's *reason* so successors know whether
it's a cap or a preference.

