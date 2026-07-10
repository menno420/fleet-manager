# Games-program mapping — CONFORMED (Q-0267 owner-shaped · ORDER 013)

> **Status:** `plan` — ⚑ OWNER-QUEUE (react to the DETAILS, not the frame).
> Committed 2026-07-10 per the round-3 part-4e owner dispatch (ORDER 013 in
> `control/inbox.md`). **The frame is the owner's own** (superbot router
> **Q-0267**, verbatim there; expanded design:
> superbot `docs/ideas/games-theme-engine-website-first-2026-07-10.md`, both read
> at superbot origin/main `9624c539`) — this document does NOT re-litigate it. It
> fills in the four details Q-0267 left to the manager (data-API reconciliation ·
> theme-contract home · new repo name · sequencing), decide-and-flag (Q-0240).
>
> **Supersedes** `games-program-mapping-2026-07-10.md` (fm PR #41, ORDER 012)
> **as a shape** — the owner shaped the mapping himself ~40 minutes after that
> proposal was relayed. What carries forward from #41 unchanged: the verified
> #1920 pattern findings (§0 there), the game-state-feed placement evidence
> (§2 there, re-affirmed below), and the pokemon-mod-lab / gba-homebrew rows
> (GBA lanes — outside Q-0267's Discord-games frame; their mandates were
> already owner-ruled via Q-0262.7 / the concept-options pattern and are
> untouched here). What is superseded: the 3-project structure with
> superbot-games as an "engine+content" project, the single-API framing, and
> the "founding packages HELD until owner reacts" gate — **Q-0267 IS the
> owner's reaction to the mapping question**; the react this doc awaits is on
> the filled-in details below.

---

## 0 · The decided frame (owner's, Q-0267 — restated, not proposed)

- **Seat A — ONE Project on existing `superbot-games`:** the whole world
  ecosystem — exploration + mining + **fishing** + world-adjacent systems
  (inventory, tools, locations, encounters). Gen-2 relaunch merging the two
  terminal gen-1 lanes; their committed succession packages (`docs/retro/`,
  `docs/gen2-custom-instructions-exploration.md` in that repo) are the boot
  input.
- **Seat B — NEW repo + Project for the idle game**, template-first: an
  idle-engine CORE (code) + data-only THEME PACKS (same mechanics, different
  skin per server), themes CI-validated; **egg farm = the first theme**, not
  the game itself.
- **Website-first onboarding** (product direction): features/themes chosen on
  the website BEFORE the bot is invited; websites lane owns the selector UI;
  the games seats own the manifests it renders.
- **Plugin-native:** games ship as plugin packages on superbot-next's
  manifest/plugin contract (D-0056, `docs/game-plugin-contract.md` at
  superbot-next `4a32f61`; validation repo `menno420/superbot-plugin-hello` —
  **verified 2026-07-10: EXISTS**, owner-created, public, pushed 16:03:04Z,
  **but EMPTY** — raw main/master both 404; the seeded package at superbot-next
  `examples/superbot-plugin-hello/` has not been pushed to it yet).

---

## 1 · Detail 1 — the read-only data API: **SPLIT** (three contract surfaces, one discipline)

The #41 placement and the website-first frame are talking about **different
data**, so the reconciliation is a split, not a move:

| Surface | Data | Producer / home | Consumer path |
|---|---|---|---|
| **(a) Game-state read feed** — *stays exactly as placed in #41* | live game telemetry (character sheets, stats, leaderboards) from **superbot's production Postgres** | **superbot lane**: contracted committed-JSON feed (`games_data_contract.json` + DB-reading producer + fail-closed checker), the verified #1920 pattern | games-web phase 2 + websites stats fetch the committed JSON over raw.githubusercontent.com |
| **(b) Theme / feature manifests** — *new with Q-0267, NOT superbot data* | what is selectable: theme packs (`themes/*.yaml`) + the theme schema; the feature catalog = the per-guild plugin enable surface | theme packs live in the **game-seat repos** (Seat B first; Seat A when world themes arrive); the feature catalog derives from **superbot-next's plugin registry** (`plugins.lock.json` + per-plugin manifests, D-0056) | the **websites selector/gallery raw-fetches the committed files** — same read-only, forward-only rule verbatim (websites CLAUDE.md; `dashboard/data_source.py` precedent) |
| **(c) Provisioning manifest** — the write path website-first adds | the owner-of-a-server's pre-invite choices: plugin enable set + theme + params per guild | **plugin-contract family** (it is derived data: enable set + per-plugin params, idea doc §4); **phase-1 = setup-code** — websites generates a signed/encoded blob, one bot command applies it (`!setup apply <code>`) — no hosted backend | websites emits it; the bot (superbot-next plugin host) consumes it — join-time auto-provisioning is the later upgrade on the SAME format |

One-line statement: **the #1920-pattern game-state feed stays a superbot-lane
feed (unchanged — superbot owns the Postgres); theme/feature manifests are
committed files owned by the game seats + the plugin contract, raw-fetched by
websites; the provisioning write path is new, plugin-contract-family, setup-code
first.** No live HTTP service anywhere; the #41 live-endpoint deferral stands.

---

## 2 · Detail 2 — theme-manifest contract home: **Seat B drafts v1; promotion path into the plugin contract**

**RECOMMENDATION: the theme-manifest schema v1 + theme-gate CI live in the Seat
B repo; flagged for promotion into superbot-next's plugin-contract family
(`docs/game-plugin-contract.md` / D-0056) the moment a second game consumes
it.** One-line why: **the engine owns what its themes must satisfy — the
validator and the themes it gates must co-locate to keep "ship a theme" a
merge-on-green data PR** — while parking the schema in superbot-next now would
serialize the whole games program behind the Builder's lane (the idea doc §4
already decided this split, Q-0240), and websites only ever *renders* the
contract, so it can't own it.

How the websites selector consumes it: **raw fetch, both halves** — the schema
(to know the slots) and `themes/*.yaml` (to render the live gallery) straight
from the Seat B repo at main, exactly the committed-JSON/raw.githubusercontent
pattern websites already uses for superbot's dashboard feed. Theme choice maps
to a per-guild parameter on the game plugin (plugins declare **settings** in
contract v1 — the seam already exists; superbot-next `docs/game-plugin-contract.md`
§2).

Rejected alternates (one line each): *superbot-next from day one* — blocks Seat
B's boot on Builder throughput for zero consumer gain; *websites* — the renderer
owning the contract inverts ownership (producer-side CI couldn't gate theme PRs
in the game repo).

---

## 3 · Detail 3 — the new repo's name: **`superbot-idle`**

Grounded in fleet naming: game-seat repos are `superbot-<domain>`
(`superbot-games` is the sibling seat; `superbot`/`superbot-next` the family
root), while `superbot-plugin-<name>` is the *distribution/validation* naming
set by `superbot-plugin-hello`. The repo is a seat; the installable
distribution inside it follows the plugin-contract packaging conventions
(D-0056) and can carry the plugin-style dist name in `pyproject.toml`. The idea
doc suggested this name; owner picks the final one at creation (his click
anyway).

Alternates:
- **`superbot-plugin-idle`** — matches the plugin-distribution convention
  exactly, but reads as a sample/validation repo (the hello pattern) rather
  than a Project seat with its own theme ecosystem.
- **`idle-engine`** — names the template-first product cleanly, but drops the
  `superbot-` family grouping that keeps game repos discoverable in a
  16+-repo estate.

---

## 4 · Detail 4 — first-shippable sequencing (dependency-honest)

Website-first is the **user flow, not the build order** — the selector is the
LAST-shippable of the four tracks because a gallery needs committed themes to
render. Volume-first (Q-0266) order:

1. **NOW, three parallel tracks (no cross-dependencies):**
   - **Plugin-contract validation (superbot-next lane):** push the seeded
     `examples/superbot-plugin-hello/` package to the now-existing (empty)
     `menno420/superbot-plugin-hello` repo; install → pin → joint-compile
     against a real out-of-tree repo. Zero dependencies; de-risks both seats
     since everything downstream is plugin-native.
   - **Seat A first increment (superbot-games, on boot):** gen-2 relaunch as
     ONE Project (succession packages = boot input) → fix the known CI gap
     (gate runs only `tests/`; add `games/exploration/tests`, the one-line
     change) → **fishing as a pure-domain package reusing mining's
     encounter/energy substrate** (the idea doc's first shippable).
   - **Game-state feed first slice (superbot lane, unchanged from #41):**
     contract v1 (family = mining character-sheet on games-web's committed
     consumer schema) + DB-reading producer + fail-closed checker. Blocks
     games-web phase 2 + websites stats; blocks NEITHER seat boot.
2. **Seat B skeleton (after the owner's repo-creation click, §3 name):**
   engine core loop v1 (generators → currency → upgrades → prestige →
   collections, + offline progress) → **theme-manifest schema v1 + theme-gate
   CI** → `themes/egg-farm.yaml` (flagship default) → 2–3 more theme packs
   proving the seam (the standing never-dry backlog).
3. **Websites selector increment (websites lane, after Seat B step 2 commits
   schema + egg-farm):** feature selector + theme gallery rendered from the
   raw-fetched committed packs; output = the **setup code** (§1c) — the
   phase-1 UX promise with no hosted backend.
4. **Provisioning consumption:** `!setup apply <code>` on the plugin host;
   join-time auto-provisioning later on the same manifest format. Gen-3
   founding packages for both seats ride the standard (continuous Q-0265 +
   volume-first Q-0266); drafting them is next manager work — paper,
   reversible, vetoable at this doc's react.

---

## 5 · Flags on this document (veto points — the react this doc awaits)

- ⚑ **API SPLIT** (§1): game-state feed stays superbot-lane; theme/feature
  manifests are game-seat + plugin-contract data raw-fetched by websites;
  provisioning = setup-code first.
- ⚑ **Theme contract drafted in Seat B, promoted to the plugin-contract family
  later** (§2).
- ⚑ **`superbot-idle`** as the new repo name (§3) — owner picks at creation.
- ⚑ **Selector sequenced LAST-shippable** (§4) — website-first read as product
  direction, not build order.
- ⚑ **Q-0259-era package HOLD read as RELEASED by Q-0267** (the owner reacted
  by shaping); founding-package *drafting* proceeds, pasting/boot stays the
  owner's clicks (Seat B repo creation + paste wave).
