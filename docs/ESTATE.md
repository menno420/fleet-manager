# The estate — every repository, one line each

> **Status:** `living-ledger`
>
> **What this file is:** the estate index — the one live surface that names
> **every repository the account holds**, what each is for, its state, the
> owner vocabulary that reaches it, where its truth lives, and whether a
> Layer-2 folder exists here. It answers *"which repo owns this request, and
> what do I read next?"* — the question `docs/MAP.md` answers for this repo's
> own tree, one level up.
>
> **Canonical for nothing beyond the enumeration.** Every row is a pointer
> with one line of context; the named repo's own docs win over the row, and a
> built Layer-2 folder wins over the row's summary. Rows carry the date they
> were last verified; a dated row is *visible* staleness, which is the design
> (`repos/README.md` § Threads).
>
> **Baseline:** all 26 repositories verified against the live account and
> their own trees on **2026-08-21** by the fleet-wide review (fm #878, method
> and evidence: [`findings/2026-08-21-fleet-estate-review.md`](findings/2026-08-21-fleet-estate-review.md)).
> Re-derive the account list any time: `list_repos` (claude-code-remote MCP),
> or `GET /user/repos` over the direct-PAT path. Consistency between this
> file, `docs/repos/`, and the doc-routes is checked by
> `python3 scripts/check_estate_index.py` (advisory).

## How to use it

1. The owner names work → find the repo below (the **aliases** column carries
   his vocabulary where it differs from the repo name).
2. Read the row, then the **Layer 2** folder if one exists — *before*
   attaching anything (`repos/README.md` § The working model).
3. No folder → the row's **read first** column names the repo's own entry
   point. Public repos need a raw fetch for read-only work, not `add_repo`.

## Active — where work actually goes now

| repo | what it is · aliases | state (verified 2026-08-21) | read first (in the repo) | Layer 2 |
|---|---|---|---|---|
| `fleet-manager` | this hub — the estate's router and records home | active | `README.md` six-read order | — (its intent: [`intent.md`](intent.md)) |
| `spider-swing` | **Slingy Spider** — Android 2D physics swing game, Godot 4.7.1. The owner's evening product | **active** — build 0.45.0 vc66; signed vc64 sits on Play's internal testing track (2026-08-05); core-feel tuning is the north star | `docs/current-state.md` | [`repos/spider-swing/`](repos/spider-swing/README.md) |
| `couch-legend` | **Couch Legend** — idle stoner sim, the first Grok-prototype graduation; live on Pages · "the Lucid Chronicle" = its looks contract (#3), not a rename | **active** — the life story LANDED 2026-08-21 (#7: adopted tuning, save v2 `lifeHigh`, 18 chapters + 3 painted scenes live, § 9.6 rails re-checked); kit-seeded v1.21.0 (#5: required checks `ci` + `substrate-gate`, land-it-yourself); next: the Android/Capacitor shell (DESIGN § 7) + the owner's late-game feel pass | `docs/DESIGN.md` (binding) | [`repos/couch-legend/`](repos/couch-legend/README.md) |
| `websites` | estate web surfaces: control-plane · botsite · dashboard (Railway) + review (Pages static since 2026-08-20/21) | **active** — keep-bot-only cutover landed 2026-08-20/21 | `docs/decisions.md` + `.sessions/` | [`repos/websites/`](repos/websites/README.md) |
| `product-forge` | seat-era shell whose living asset is **phone-controller** — shipped Android Bluetooth-HID controller app, v0.22.0 signed releases | **active** (app thread); graduation to own repo = program step R2, next | `products/phone-controller/README.md` | [`repos/product-forge/`](repos/product-forge/README.md) |
| `superbot` | the **FROZEN** repo behind the **LIVE production Discord bot** (Railway `reliable-grace` `worker`). No root README — its entry is `docs/AGENT_ORIENTATION.md`. Hard rail: never touch worker/Postgres uninvited | **frozen behavior/UX oracle** — maintenance class only; the clean game-community successor is planned [here](planning/2026-08-21-game-community-bot/README.md), and this repo remains untouched | `docs/AGENT_ORIENTATION.md` → `docs/current-state.md` | [`repos/superbot/`](repos/superbot/README.md) |
| `substrate-kit` | the estate's method kit (single-file `bootstrap.py`, PL register = program law, adopter registry) · "the kit" | **infrastructure** — v1.21.0 cut 2026-08-13; its next worklist lives HERE, not in the kit | `control/status.md` → `docs/PROJECT-CLOSEOUT.md` | [`repos/substrate-kit/`](repos/substrate-kit/README.md) |
| `estate-backups` | **PRIVATE** Actions venue for Railway-Postgres work (sealed-box one-shot secrets) | **infrastructure, dormant** between owner asks; executes `OQ-BOT-DB-BTD6-PRUNE` when answered | `README.md` + the two workflows | [`repos/estate-backups/`](repos/estate-backups/README.md) |

## Paused / owner-gated — real assets, waiting on the owner

| repo | what it is · aliases | state (verified 2026-08-21) | read first (in the repo) | Layer 2 |
|---|---|---|---|---|
| `superbot-next` | the ground-up bot rebuild · "SuperBot 2.0", "the rebuild" | **complete-parked architecture donor** — 533/533 golden parity green but parity ≠ ported; the former cutover/server-first fork is resolved by the [2026-08-21 game-community plan](planning/2026-08-21-game-community-bot/README.md): clean repo after GCB-1, live `superbot` behavior oracle, this repo untouched | `docs/PROJECT-CLOSEOUT.md` → `docs/current-state.md` | [`repos/superbot-next/`](repos/superbot-next/README.md) |
| `venture-lab` | the commerce lane · "Venture", **Stripe Webhook Test Kit**, **The Night Kiln**, **Lull/DREAMLINE**, **Ultramarine** | **paused by OD-11** (let it sit) — 1 live $29 SKU, 19 ready SKUs, 12 finished books; the repo's own closeout threads (kill clock, publish wave) are SUPERSEDED by OD-11 | `docs/PROJECT-CLOSEOUT.md` | [`repos/venture-lab/`](repos/venture-lab/README.md) |
| `shiftlife` | **PRIVATE** — ShiftLife, shift calendar for shift-working households (binnenvaart first); Expo + Hono/Postgres monorepo | **paused by OD-15** (not active) — stopped 2026-07-27: free core 7/8, reminders *delivery* unbuilt (`OQ-SHIFTLIFE-PHASE0`); `apps/api` code↔live gap standing (merges since `fe2fbbf` not deployed); Railway scope = `OQ-RAILWAY-SHIFTLIFE-SCOPE` | `docs/current-state.md` + `docs/plan-conformance.md` | on demand |
| `gba-homebrew` | original-IP GBA/NDS homebrew: **Lumen Drift** (released) · Wickroad · Brineward · Underroot + web arcade on Pages · "the GBA project" | **complete-parked** — resumes on the owner's A1/A3 pick + playtest verdicts (`OQ-GBA-NEXT-PICKS`); trap: required `NDS ROM build` check reds on cold-cache PRs (BlocksDS 1.21.1 pin unrecoverable; migration branch `claude/nds-toolchain-1-22-3` retained, gba #216 closed per D‑0017) | `docs/PROJECT-CLOSEOUT.md` | on demand |
| `pokemon-mod-lab` | **PRIVATE** rom-hack QoL lab (Emerald): 18 toggles, byte-identical-when-off, source-only rail (R22) | **frozen** — one owner letter unblocks it (`OQ-PML-EMERALD-LETTER`); kit hop owner-held; note: free-plan private repos cannot enable branch protection (measured 403, 2026-08-21) | `docs/PROJECT-CLOSEOUT.md` | on demand |
| `superbot-games` | the bot's game world as pure stdlib Python (mining · fishing · D&D · exploration) — README claims plugin-shipping, tree has no packaging (known drift, program R1) | **complete-parked** — kit hop to v1.21.0 queued but **owner-paced** ("no adopter yet", owner 2026-08-14); bridge flip + slice-4 are owner forks | `docs/PROJECT-CLOSEOUT.md` | on demand |
| `superbot-idle` | one idle-game engine + 21 data-only theme packs; its plugin is pinned in superbot-next's lockfile · "the idle engine" (NOT the Couch Legend idle game) | **complete-parked** — kit v1.16.0, invisible to the adopter registry (missing from the kit's `fleet-repos.txt` scan roster, as is sim-lab); daily `host-main-advisory` cron still fires | `docs/PROJECT-CLOSEOUT.md` | on demand |
| `superbot-mineverse` | staged browser dashboard over the bot's mining economy · "mineverse"; its closeout is the **SuperBot-World fleet MASTER** | **complete-parked, off Railway 2026-08-20/21** (service+project deleted; repo stays by owner word). Its own go-live checklist is moot: the web host is gone and the bot-side WRITE PR (sb #2061) closed unmerged. Trap: its `current-state.md` baton says delete a trigger — D‑0015 forbids exactly that | `docs/PROJECT-CLOSEOUT.md` (the MASTER) | on demand |
| `idea-engine` | Ideas Lab, canonical half: 566 fleet-era idea files + the closed 4-gate math-verify loop (P261/V274) | **on-demand standing asset** (OD-4/OD-10) — at rest; resume recipe: its `PROJECT-CLOSEOUT.md` §3 (`HANDOFF.md` is the older layer) | `docs/PROJECT-CLOSEOUT.md` | on demand |
| `sim-lab` | Ideas Lab, evidence half: the 4-gate verification seat + reusable `harness/`. NOTE: "sim-lab" now also names the *method* run inside a target repo (couch-legend did this) | **on-demand, at rest** — no closeout of its own (idea-engine's covers both); heartbeat deliberately historical; kit v1.15.0 and absent from the kit's scan roster | `README.md` + `CONVENTIONS.md` | on demand |
| `curious-research` | the parked gift workshop-notebook (3D printing, robot arm, Arduino) with a live site; shed kit machinery 2026-08-07 | **parked by owner choice** — "gets a new mission later" | `README.md` | on demand |
| `trading-strategy` | closed quant research · "trading-lab": 11 rounds / 5,940 configs / **0 promoted**, holdout SPENT | **complete-parked** — archive decision open (owner skipped its kit hop pending it); paper-0001 lane WATCH/FLAT | `docs/PROJECT-CLOSEOUT.md` | on demand |

## Frozen experiments & exemplars — read-only unless the owner says otherwise

| repo | what it is · aliases | state (verified 2026-08-21) | read first | Layer 2 |
|---|---|---|---|---|
| `superbot-plugin-hello` | the plugin-contract hello-world, hash-pinned in superbot-next's lockfile — **never archive**; trap: a manifest edit is a two-repo change (host pin re-land or FAILED_STARTUP) | complete-parked | `README.md` | on demand |
| `codetool-lab-opus4.8` | **mdverify** — released CLI (v0.1.0 + v0.2.0 live, re-verified 2026-08-22). **Keep-unarchived is a standing OWNER ruling (2026-07-10), not a technical dependency** — corrected 2026-08-22: this row previously read *"stays unarchived while install URLs pin it"*, which is not a reason, because an archived repo stays readable and its URLs keep resolving. The real record is [`fleet-triage.md`](fleet-triage.md) `:61` + INC-03, where two fm docs disagreed and the owner's ruling settled it: *"re-verdict only if the owner rules again."* So this is his call to revisit, not a wall | complete-parked, **keep unarchived (owner ruling)** | `README.md` + `control/status.md` | on demand |
| `codetool-lab-fable5` | **envdrift** — finished CLI; **R3 DONE 2026-08-22**: v0.1.0@`73ef38d` + v0.2.0@`13a84e5` tagged and released (2 assets each). It had no release workflow at all, so fable5 #20 added one (`workflow_dispatch` + tag input, no PyPI job — no publisher registered) | **archivable** — R3 satisfied | `control/status.md` | on demand |
| `codetool-lab-sonnet5` | **cfgdiff** — finished CLI; **R3 DONE 2026-08-22**: v0.1.1@`0b1eb60` tagged, its own `release.yml` published the Release (2 assets). Trap: its `publish-pypi` job fails on every run (no trusted publisher), so the **run reads red while the Release is intact** | **archivable** — R3 satisfied | `control/status.md` | on demand |
| `Substrate-kit-app` | a one-shot Gemini (AI Studio) experiment: "Substrate Kit Dashboard" React frontend over hardcoded demo data, committed onto a **partial v1.20.2 kit snapshot** — its README, CONSTITUTION and docs are the kit's **verbatim**, so every in-repo surface misidentifies it; copied CI reds by construction | frozen one-shot (2026-08-04, untouched since) | `metadata.json` + `package.json` (the only honest self-descriptions) | on demand |
| `proxybench` | single-file proxy benchmark, built mostly as a joke (OD-12: parked, no action) | parked | `README.md` | none needed |

## When the owner's words don't name a repo

- **"the bot"** — the live bot is `superbot` (frozen oracle, hard rail); `superbot-next` is the parked architecture donor; the planned clean game-community bot has no repository until GCB-1. Say which one you mean before acting.
- **"the idle game"** — ambiguous: the *product* is `couch-legend`; the bot's
  idle *engine* is `superbot-idle`. Recent context decides; ask only if it
  genuinely could be either.
- **"the controller app"** — `product-forge` (phone-controller).
- **"the review site"** — websites' Pages export
  (menno420.github.io/websites); there is **no Railway service behind it**
  since 2026-08-20/21.
- **"backups"** — the *venue* is `estate-backups`; the *recurring bot backup*
  is a `superbot` workflow (weekly). A backup ask usually means both.
- **"the old rebuild" / "SuperBot 2.0"** — `superbot-next`.
- **"research tooling"** — usually `idea-engine`+`sim-lab` (the Ideas Lab
  pair); `curious-research` is the gift notebook; `trading-strategy` is closed
  quant research. Ask which if the context does not say.
- **"the kit"** — `substrate-kit`. The similarly named `Substrate-kit-app` is
  a frozen dashboard experiment that *masquerades* as the kit from inside.

## Cross-repo edges a router must know

- `superbot` → planned game-community bot ← `superbot-next`: the live repo is the behavior/UX oracle; the parked rebuild is the architecture donor. The 2026-08-21 plan resolves the old fork in favor of a clean repository after GCB-1; neither source repo is modified, deployed, renamed, or archived by that planning decision.
- `superbot-next` ⇐ `superbot-idle` + `superbot-plugin-hello`: plugins pinned
  by hash in its `plugins.lock.json`; games' adapters were never built (R1).
- `superbot-mineverse` closeout = the SuperBot-World fleet **MASTER**; the
  games/idle closeouts route their fleet-wide threads to it.
- `websites` serves the bot's public surfaces (botsite, dashboard) under the
  old names since W1; `review` is Pages-static.
- `couch-legend` → `product-forge`: the Android/Capacitor step reuses
  phone-controller's keystore/release rails.
- `spider-swing` + `couch-legend` → this repo's `image-prompt` /
  `asset-pipeline` / `audio-prompt` skills carry the art/audio method.
- `substrate-kit` → every adopter (registry `docs/adopters.md`, GENERATED);
  its scan roster misses `sim-lab`, `superbot-idle`, `product-forge`,
  `spider-swing` and `couch-legend` (the last two measured 2026-08-21), so
  registry-driven rollouts cannot see them.
- `shiftlife`'s product plan lives HERE
  (`planning/2026-07-24-app-plan-life-admin.md`); its Railway scope question is
  `OQ-RAILWAY-SHIFTLIFE-SCOPE`.
- `estate-backups` executes DB asks against the bot's Postgres (hard rail
  applies); its one archive so far: Release tag
  `postgres-botsite-final-2026-08-16`.
