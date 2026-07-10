# Hub-side inventory — project-package centralization (2026-07-10, read-only sweep)

Baselines swept:
- **fleet-manager** `origin/main` = `702ba890ff21b9b1d5e1fb8a5c8f903fbaf1eca7` (short `702ba89`) — cited `fm:<path>@702ba89`
- **superbot** `origin/main` = `53fb5ef9a294ab304b679dedd44ead55849295d5` (short `53fb5ef`) — cited `sb:<path>@53fb5ef`

Doctrine baseline used for CURRENT/OUTDATED: **Q-0264** (idea-engine own-repo + sim-lab seat 6) and
**Q-0265** (continuous mode for all six core seats; cron demoted to "<seat> failsafe wake" dead-man;
send_later chain is the pacemaker) — `sb:docs/owner/maintainer-question-router.md@53fb5ef` lines 9511–9648.
The **Q-0262.6 hold**: "the 8 undeployed instruction packages STAY undeployed until re-based on the
manager's gen-3 blueprint delta" — same file line ~9468; hub-side copy of the hold:
`fm:docs/owner-queue.md@702ba89` lines 175–178. The owner's 2026-07-10 ~20:50Z centralization dispatch
effectively initiates that re-base.

**fleet-manager has NO `projects/` folder yet** (top-level tree at `702ba89`: .github, .substrate,
control, docs, environments, telemetry, templates, tools — no `projects/`). The target structure is
greenfield.

---

## A. fleet-manager @702ba89 — Custom-Instructions packages (gen-2, `docs/proposals/instructions/`)

Index + deployment ledger: `fm:docs/proposals/instructions/README.md@702ba89` — "2 DEPLOYED (fitted),
8 PROPOSED". Deployed texts are recorded per-file in a `## Deployed fitted version (≤8000 chars, pasted
2026-07-10)` section (websites line 324; trading line 332). All 10 were drafted 2026-07-10 against the
gen-2 blueprint §1–§2a + playbook R21 — i.e. ALL are pre-Q-0265 in their body text (gen-2 one-slice
pacing where pacing appears). Package shape (verified on websites.md): §1 mission · §2 Custom
Instructions paste block (worker-instructions) · §3 environment archetype assignment · §4 ORDER 001
draft · §5 divergences — so each is **mixed** (worker-instructions + env pointer + first order), NOT a
seat/coordinator prompt (that lives elsewhere).

| # | File | Target | Deployed-state | Currency |
|---|---|---|---|---|
| 1 | `fm:docs/proposals/instructions/websites.md@702ba89` | websites Project | **DEPLOYED fitted 2026-07-10** (7,496 chars; §"Deployed fitted version" L324; README banner; also `fm:docs/capabilities.md@702ba89` L204–205). In-file L3 badge still says "PROPOSED, not deployed" — stale vs its own §Deployed + README. | Gen-2 base, pre-Q-0265/pre-gen-3. Maintenance-lane pacing may legitimately stay (gen2-blueprint delta keeps §2a maintenance doctrine for bounded lanes) but needs the gen-3 re-base per the new dispatch. |
| 2 | `fm:docs/proposals/instructions/trading-strategy.md@702ba89` | trading-strategy Project | **DEPLOYED fitted 2026-07-10** (7,495 chars; §Deployed L332). Same stale L3 badge. | Same as websites. |
| 3 | `fm:docs/proposals/instructions/venture-lab.md@702ba89` | venture-lab (repo planned) | PROPOSED, held (Q-0262.6) | OUTDATED — pre-Q-0265; needs gen-3 re-base. |
| 4 | `fm:docs/proposals/instructions/game-lab.md@702ba89` | game-lab (gba-homebrew public + pokemon-mod-lab PRIVATE, repos planned) | PROPOSED, held | OUTDATED — pre-Q-0265 re-base needed. |
| 5 | `fm:docs/proposals/instructions/games-exploration.md@702ba89` | superbot-games / exploration | PROPOSED, held | OUTDATED. |
| 6 | `fm:docs/proposals/instructions/games-mining.md@702ba89` | superbot-games / mining | PROPOSED, held | OUTDATED. |
| 7 | `fm:docs/proposals/instructions/substrate-kit.md@702ba89` | substrate-kit Project | PROPOSED, held — **functionally superseded** by the round-3 kit founding package (sb side, below) which actually booted the seat | OUTDATED ×2 (pre-Q-0265 AND superseded by round-3). |
| 8 | `fm:docs/proposals/instructions/superbot-next.md@702ba89` | superbot-next / Builder | PROPOSED, held — **functionally superseded** by the round-3 Builder package that booted the seat | OUTDATED ×2. |
| 9 | `fm:docs/proposals/instructions/codetool-arm-template.md@702ba89` | codetool-lab-{fable5,opus4.8,sonnet5} (one template ×3) | PROPOSED, held | OUTDATED. |
| 10 | `fm:docs/proposals/instructions/mobile-lab.md@702ba89` | mobile-lab (idea-stage, **no repo exists**) | PROPOSED, held; source idea captured-not-approved | OUTDATED + gated on the spend-instrument discussion. |

README paste-time checklist (delta-8 lint, 5 items incl. "re-base on blueprint at HEAD on the day of
the paste") + the ≤7,500-char fitted limit (8,000-char paste cap; both ~9k drafts overflowed —
`fm:docs/findings/night-review-2026-07-10.md@702ba89` L955) are reusable centralization inputs.

## B. fleet-manager @702ba89 — prompts ledger (`docs/prompts/`, gen-1 era + gen-2 finals)

Ledger: `fm:docs/prompts/README.md@702ba89` (verbatim deployed-prompts ledger; never edit history,
append dated successors).

| File | Type | Target | Deployed-state | Currency |
|---|---|---|---|---|
| `init-prompt-universal.md` | seat-protocol init prompt (control/ contract + self-arm routine recipe + rider) | every Project | ✅ gen-1 deployed fleet-wide 2026-07-09; **2026-07-10 successor text is the one to deploy** (false routine promise replaced by VERIFIED recipe; model-attribution rider ~20:00Z) | Successor is gen-2-current but **pre-Q-0265** (no continuous mode / failsafe naming). |
| `universal-wakeup.md` | wake/self-review prompt | all 10 gen-1 lanes | ✅ deployed fleet-wide (gen-1) | OUTDATED (gen-1; superseded by Q-0265 failsafe-wake pattern). |
| `gen1-winddown-universal.md` | winddown prompt ×9 | gen-1 Projects | ❌ NOT deployed (owner-queue paste item) | Gen-1 migration artifact. |
| `trading-lab.md`, `codetool-arms.md`, `game-mining.md`, `game-exploration.md` | gen-1 Custom Instructions + startup | respective lanes | ✅ deployed (gen-1) | Historical; superseded by gen-2 packages (§A). |
| `venture-lab-draft.md` | gen-2 founding CI, FINALIZED paste-verbatim | venture-lab | ❌ NOT deployed | Superseded-ish by §A venture-lab.md (README notes it as the honored base). |
| `game-lab-founding.md` | gen-2 founding CI, FINALIZED | game-lab | ❌ NOT deployed | Base for §A game-lab.md. |
| `external-campaign-metaprompt.md`, `external-review-{opus,sonnet}-2026-07-09.md` | external-review prompts | ChatGPT / owner sessions | ✅ handed off | Not seat packages — out of centralization scope. |

## C. fleet-manager @702ba89 — environment registry (`environments/`) — THE setup-script source

`fm:environments/README.md@702ba89` — living ledger; hard rule NO secret values; agents draft specs,
owner pastes (agents cannot create/edit envs — platform wall). Rendered read-only at the websites
control-plane `/environments`.

| File | Type | Currency |
|---|---|---|
| `fm:environments/archetypes.md@702ba89` | env registry: 5 archetypes (python-lab, pinned-research, bot-prod, coordinator, gba-lab) + FULL project→archetype map + per-repo env-var NAME unions + 3.10/3.11 wrinkle + owner paste-steps | **CURRENT** — round-3 packages reference these verbatim by raw URL. Note: `SB_TEST_DB_HOSTS` still listed for superbot-next; Q-0263.1 demoted it to optional-and-silent — minor drift. |
| `fm:environments/archetype-python-lab.sh@702ba89` | setup-script (tested) — kit, codetool ×3, games, fleet-manager, venture-lab, **and reused verbatim by round-3 for idea-engine, product-forge, sim-lab** | CURRENT |
| `fm:environments/archetype-pinned-research.sh@702ba89` | setup-script (tested) — trading (two-source shape), websites (3 requirements files) | CURRENT |
| `fm:environments/archetype-bot-prod.sh@702ba89` | setup-script (tested) — superbot-next (lockfile), superbot legacy (3.10 pin); only archetype allowed prod-pointing vars | CURRENT |
| `fm:environments/archetype-coordinator.sh@702ba89` | setup-script (tested) — the live `multi-repo` manager env | CURRENT |
| `fm:environments/archetype-gba-lab.sh@702ba89` | setup-script — game-lab (devkitARM r68 + agbcc + mGBA); assembled-whole unverified until first lane boot | CURRENT (pre-boot caveat) |
| `fm:environments/templates/setup-universal.sh@702ba89` | the defensive shim contract all archetypes derive from (R15: exit 0 always) | CURRENT |
| `fm:environments/templates/env-vars.md@702ba89` | var-NAME placeholder schema + Railway-trio DANGER note | CURRENT |
| `fm:environments/templates/smoke.yml@702ba89` | tier-1 reference CI workflow | CURRENT |
| `fm:environments/multi-repo.md@702ba89`, `SPEC-TEMPLATE.md` | live coordinator-env spec; new-env proposal form | CURRENT |

## D. fleet-manager @702ba89 — gen-2 blueprint (the binding template doc)

`fm:docs/gen2-blueprint.md@702ba89` — §1 SEED STATE checklist · §2 instruction-template deltas · §2a
wake cadence (measured) · §2b CI-tier standard · §3 owner setup checklist · §4 migration policy.
**The Q-0265 continuous-mode delta IS already folded in** as a dated amendment banner (lines 60–76,
2026-07-10 night, "folded by the manager per the part-4 brief §2b MANAGER-ONLY rider"): production
seats born continuous; §2a maintenance-cadence doctrine stays valid for bounded maintenance lanes.
So the "gen-3 blueprint delta" the 8 held packages await is at least partially landed here; the
full method doc is superbot's gen-3 deployment standard (§F below).

## E. superbot @53fb5ef — round-3 founding packages (the coordinator-seat packages)

Common shape (all five files): **mixed** — §0 owner pre-clicks/finalize-first · §1 Custom Instructions
paste block (worker-instructions for the Project's agents) · §2 coordinator chat brief (seat prompt,
first message; contains the exact create_trigger cron + wake-prompt text = the failsafe-wake cron text)
· §3 environment (name, single repo per Q-0260, archetype script by raw URL, var names) · §4 boot
verification. So each file already contains ALL FOUR artifact types the centralization job wants,
per seat.

| Package | Target seat / repo | Q-0265 state | Deployed-state |
|---|---|---|---|
| `sb:docs/planning/round3-founding-package-builder-2026-07-10.md@53fb5ef` | Builder / superbot-next (core seat 3) | ⚠ AMENDED banner at top; §1/§2 body still "one bounded slice" (historical boot-paste record) | Seat LIVE (booted 2026-07-10); live seat gets the §2b amendment paste; §0 items 1–2 marked DONE |
| `sb:docs/planning/round3-founding-package-idea-engine-2026-07-10.md@53fb5ef` | Idea Engine / idea-engine (core seat 4) — **v2, own-repo per Q-0264** (v1 superbot-homed superseded, in git) | ⚠ AMENDED banner; body still "ONE bounded slice" (historical) | Seat LIVE (booted part-3); amendment via §2b paste |
| `sb:docs/planning/round3-founding-package-product-forge-2026-07-10.md@53fb5ef` | Product Forge / product-forge (core seat 5) | **REWRITTEN natively continuous** — §1 "SESSION SHAPE — CONTINUOUS MODE (Q-0265)", §2 step 5 "ARM YOUR FAILSAFE" with exact `"product-forge failsafe wake"` cron + prompt text | Seat LIVE (booted ~19:05Z **pre-Q-0265-merge** → the live chat still needs the §2b amendment paste despite the current doc; per part-4 brief §2 item 0) |
| `sb:docs/planning/round3-founding-package-simulator-2026-07-10.md@53fb5ef` | Simulator / sim-lab (core seat 6 per Q-0264, supersedes Q-0262.8 hub pick) | **Born continuous natively** (cadence `0 1-23/2` demoted-to-failsafe noted in banner; 4 Q-0265 mentions, zero "one bounded") | NOT yet booted at part-4 time — repo SEEDED born-right (`32dc75d`, gate run #1 green); §0.1 done; Project/env/Codex clicks pending (part-4 brief item 3) |
| `sb:docs/planning/round3-founding-package-substrate-kit-2026-07-10.md@53fb5ef` | substrate-kit distribution seat (core seat 2; Q-0261.3 write-all) | **NO Q-0265 banner; §2 still "ONE bounded pass — exactly one"** → the one round-3 package file with the amendment entirely missing (live seat was amended by chat-paste only) | Seat LIVE (booted 2026-07-10) |
| `sb:docs/planning/round3-dispatch-runbook-2026-07-10.md@53fb5ef` **§2** | **fleet-manager Project itself** — founding package v3 (§2a Custom Instructions + §2b coordinator brief incl. `"30 */2 * * *"` cron + wake prompt) | ⚠ AMENDED banner over §2; body "ONE bounded slice/pass" historical | Seat LIVE — owner pasted (v3 FINAL). **Note: the manager's own package lives ONLY here in superbot, not in fleet-manager.** §1 also holds the locked instruction-architecture decisions (Project-scoped job descriptions ≤7,500; brief-in-chat; env standards; Q-0260 single-writable-repo). |

## F. superbot @53fb5ef — templates / amendment blocks / method docs

| Artifact | Type | Currency |
|---|---|---|
| `sb:docs/planning/gen3-deployment-standard-2026-07-10.md@53fb5ef` | **THE born-continuous gen-3 template** — §0 core-6 finalize-first scope (Q-0261) · §1 sim-backed pipelined+gate strategy (`tools/sim/gen3_deployment_sim.py`) · §2 the standards: repo settings, env (Q-0260 + archetype verbatim), Custom-Instructions shape (≤7,500, session shape "work loop per Q-0265 *(amended; was one bounded slice)*"), coordinator-brief shape (BOOT-NOW list ending in ARM YOUR ROUTINE + calibration ask), **operating model AMENDED 2026-07-10 per Q-0265**: born continuous, send_later pacemaker, cron = `"<seat> failsafe wake"` (stagger kept: lanes `0 */2`, manager `30 */2`), backpressure brake, Q-0089 honesty guard, verify-in-registry-never-wait-for-first-fire | **CURRENT — the base document for the centralization job.** |
| `sb:docs/planning/round3-dispatch-part4-brief-2026-07-10.md@53fb5ef` **§2b** (L110–152) | **The Q-0265 continuous-mode amendment paste block** — the generic failsafe-text template: 5-point new operating model + the verbatim `"FAILSAFE WAKE (<seat>, Q-0265): …"` cron prompt + delete/create re-arm recipe + MANAGER-ONLY rider (fold into gen-3 delta + standing inventory thread) | CURRENT. Deployment: owner to paste into the 5 LIVE seat chats (manager · kit · Builder · Idea Engine · Product Forge); only sim-lab inherits natively (§2 item 0). |
| `sb:docs/planning/round3-launch-pack-2026-07-10.md@53fb5ef` | mixed prompt pack: §1 manager brief (superseded by runbook §2 v3) · §2 lane continuation + night-review prompt · §3 Codex review prompts · §4/§4b decisions + Q-0259 rulings · §5 standing-core design · §6b interface hygiene | Partially OUTDATED (superseded pieces flagged in-file); §5/§4b remain reference. |
| `sb:docs/planning/forward-only-project-custom-instructions-2026-07-08.md@53fb5ef` | worker-instructions (paste-ready CI) for an EXPERIMENTAL forward-only superbot Project + how-to | Never recorded deployed; pre-round-3, pre-Q-0265; experiment-scoped, not a seat package. |
| `sb:docs/planning/projects-eap-evaluation-log.md@53fb5ef` | evaluation log | Only ONE custom-instructions mention (L105: probe tests #7/#8 ran with a standing owner authorization in a Project's custom instructions). **No deployed-CI texts are recorded here** — deployed texts live in fm `docs/prompts/` (gen-1), fm instruction files' §Deployed (gen-2), and the runbook §2 / founding packages (round-3). |
| Router entries Q-0262/Q-0263/Q-0264/Q-0265 (`sb:docs/owner/maintainer-question-router.md@53fb5ef` L9442–9648) | doctrine provenance | CURRENT — Q-0263.2 ("agents never route derivable values; future founding packages inherit rule 2") is an additional constraint every centralized package must carry. |

## G. Repos/Projects with NO hub-side package at all

1. **superbot (legacy hub) Project** — no seat package anywhere (the Q-0262.8 hub-seat pick was vetoed
   by Q-0264; hub games-finishing routes to the games program / owner-started sessions per Q-0264.5).
   Only the experimental forward-only CI doc exists (not a seat package).
2. **fleet-manager Project — no package IN ITS OWN REPO**: its v3 package lives only in superbot
   runbook §2. For a `projects/<repo>/` folder in fleet-manager this is a gap to import.
3. **The 3 planned games-program repos** (Q-0259 r.5 — unnamed, uncreated; manager to propose the
   mapping) — nothing exists.
4. **superbot-plugin-hello** — helper repo (Builder §0.1), no Project/package by design.
5. **gba-homebrew / pokemon-mod-lab** — repos not created; covered only by the HELD gen-2 game-lab
   package (no round-3/gen-3 package).
6. Inverse case: **mobile-lab** has a held package but NO repo/Project.

Also worth flagging: idea-engine / product-forge / sim-lab packages exist ONLY in superbot planning
(not fleet-manager), and websites/trading deployed texts exist ONLY in fleet-manager — the corpus is
split across the two hubs, which is exactly what the `projects/<repo>/` centralization resolves.
