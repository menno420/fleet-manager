> **Status:** `reference`

<!-- v3.0-draft · 2026-07-12 · provenance: research PRs #93/#95 + owner baseline 2026-07-11 -->
<!-- char-count: 10,857 chars = this whole file at draft, before the Status-badge hygiene line above (added 2026-07-12; planning doc, no paste budget applies) -->

# Per-project prompts (artifact B + seat CI blocks) — phase-2 plan

Phase 2 writes, per seat: **`<seat>-startup.md`** (artifact B = `../universal-startup.md`
verbatim + the seat delta: identity/repos/heartbeat home, 2–5 hard rails, volatile
cutover slots — old trigger ids marked "expect X, or later" — cron stagger, and
sequenced FIRST WORK ORDERS each with a done-when) and **`<seat>-custom-instructions.md`**
(the seat block per `../custom-instructions-core.md`, ≤ ~1,383 chars fitted).
Budget: B = A (~5.5k) + delta ≤ ~7,500 pasteable.

## Census inputs — AVAILABLE (write B against them, not from memory)

- **Core census — PR #94**, branch `claude/research-census-core` @ `5fa812f`,
  `docs/research/2026-07-12-problem-census-core.md` (superbot, superbot-next,
  websites, substrate-kit, fleet-manager, product-forge).
- **Satellite census — PR #96**, branch `claude/research-census-sat` @ `1daa81f`,
  `docs/research/2026-07-12-problem-census-satellites.md` (superbot-games, superbot-idle,
  superbot-mineverse, gba-homebrew, pokemon-mod-lab, venture-lab, trading-strategy,
  idea-engine, sim-lab, superbot-plugin-hello, codetool labs).

Both are dated snapshots — re-verify volatile facts at HEAD before baking any
into a prompt (and per map #13, bake state as read-at-HEAD steps, not facts).

## The 8 seats (owner restructure 2026-07-11, `projects/README.md` @ `claude/restructure-roster` f3e2dc4)

| # | Seat | Repos folded | Phase-2 files | Census findings that feed it |
|---|---|---|---|---|
| 1 | **Fleet Manager** | fleet-manager | `fleet-manager-startup.md` + `-custom-instructions.md` | Core §fleet-manager: roster-freshness time-bomb (gen #10 stuck on `bot/roster-regen`, Actions-PR wall → blocking red on every `claude/*` PR); no CLAUDE.md/`.claude/` on main (settings port parked in PR #92); seat-in-handover state. |
| 2 | **SuperBot 2.0** | superbot + superbot-next | `superbot-startup.md` + `-custom-instructions.md` (drafter's simpler slug adopted — integrator 2026-07-12) | Core §superbot (heartbeat asserts superseded facts w/o `verified-against:` stamps; 79 KB orientation payload) + §superbot-next (no `.claude/CLAUDE.md` at HEAD — fresh session loads nothing; wake loop disarmed; stale OWNER-ACTION asking for an already-existing repo). |
| 3 | **Websites** | websites | `websites-startup.md` + `-custom-instructions.md` | Core §websites: review-bake cron dies daily on the Actions-PR wall; baked stats stranded on `bake/*` branches (undeletable, 403); deliberately-parked STALE state. Baseline prompt: `../../baseline-2026-07-11/websites.md` (fresh-session-per-fire shape — B here is the wake-routine prompt + CI carries the durable context). |
| 4 | **Self Improvement** | substrate-kit | `self-improvement-startup.md` + `-custom-instructions.md` | Core §substrate-kit: adopter registry blind to ≥3 (likely 5) vendored adopters; "v1.12.1 distribution COMPLETE" false fleet-wide; substrate-gate false-green bug live downstream; kit-template root cause of the missing-CLAUDE.md class. |
| 5 | **SuperBot World** | superbot-games + superbot-idle + superbot-mineverse (flagship: mineverse) | `superbot-world-startup.md` + `-custom-instructions.md` | Sat §SuperBot World: games heartbeat instructs owner to merge 5 already-merged PRs + 5 phantom claim files at HEAD; mineverse "IN FLIGHT: (none)" while green security PR #42 sits unmerged; idle genuinely dormant/FRESH. |
| 6 | **Game Lab** | gba-homebrew + pokemon-mod-lab (standalone; Track B PRIVATE) | `game-lab-startup.md` + `-custom-instructions.md` | Sat §Game Lab: both FRESH; track-isolation hard rail + R22 private-visibility check carry over from the owner baseline `../../baseline-2026-07-11/game-lab.md` (the persistent-coordinator style baseline). |
| 7 | **Ideas Lab** | idea-engine + sim-lab (+ the superbot-plugin-hello DEAD-empty-repo finding) | `ideas-lab-startup.md` + `-custom-instructions.md` | Sat §Ideas Lab: idea-engine CI gate exits 2 at HEAD (merge gate broken, unfiled); sim-lab FRESH (11 verdicts finalized); plugin-hello: zero commits ever — second leg of a handoff never fired. |
| 8 | **Venture Lab** | venture-lab + trading-strategy (research-only) | `venture-lab-startup.md` + `-custom-instructions.md` | Sat §Venture Lab: venture-lab committed heartbeat declares ARCHIVE-READY at `e7e5c9f` while HEAD is `296a1a9` with 3 post-archive PRs; trading FRESH (marginal), open succession PR #64; money protocol rail (D1 LESSON: never claim a payment path works without executing it). |

## Not seats (do not write B files for these)

- ⚑ **product-forge** — awaits owner disposition (spec §8 flag; not in the 8-seat
  list). Core census §product-forge findings (dead CLAUDE.md pointer, dark inbox)
  are PARKED here until the owner rules; if seated, it becomes seat 9 via this
  same recipe.
- **codetool-lab-{opus4.8,sonnet5,fable5}** — DARK, wound down 2026-07-09/10;
  succession material only (sat census §codetool).
- **superbot-plugin-hello** — helper repo, folded into Ideas Lab's findings.

## Phase-2 checklist (per seat)

1. Fill A's slots from the seat row above + the seat's census section; every
   volatile fact (trigger ids, PR numbers, HEAD shas) marked "expect X, or later".
2. Write FIRST WORK ORDERS in kit ORDER grammar (sequenced, one named executor,
   concrete done-when) — the top items come straight from the census findings column.
3. Write the seat CI block within the measured budget (`../custom-instructions-core.md`
   arithmetic); re-measure the assembled paste with `wc -c` ≤ 7,500.
4. Stamp both files `v3.0-draft · <date>` + char-count line, same convention as
   the universal artifacts.

## Phase-2 status — DRAFTED + INTEGRATED (v3.0-draft, 2026-07-12)

All 16 files (8 seats × startup B + custom-instructions C seat block) are in this
directory, audited and reconciled by the integrator on 2026-07-12. Char counts are
real `wc -c` of the paste body (headers excluded), verified against each file's
declared char-count line. Assembled = universal core 6,117 + seat block.

| Seat | Startup B | Seat block C | Assembled CI | Status |
|---|---:|---:|---:|---|
| fleet-manager | 7,497 | 1,382 | 7,499 | drafted v3.0-draft, fitted |
| superbot | 7,500 | 1,380 | 7,497 | drafted v3.0-draft, fitted |
| websites | 7,497 | 1,381 | 7,498 | drafted v3.0-draft, fitted |
| self-improvement | 7,485 | 1,381 | 7,498 | drafted v3.0-draft, fitted |
| superbot-world | 7,431 | 1,380 | 7,497 | drafted v3.0-draft, fitted |
| game-lab | 7,498 | 1,382 | 7,499 | drafted v3.0-draft, fitted |
| ideas-lab | 7,498 | 1,383 | 7,500 | drafted v3.0-draft, fitted |
| venture-lab | 7,398 | 1,607 | 7,724 | drafted v3.0-draft; startup fitted after integrator trim (was 7,986); seat block over fitted by 224, under 1,883 hard — every census must-encode item retained, flagged in-file |

Hard caps: startup ≤8,000 · assembled CI ≤8,000 — **all 16 within hard**; fitted
targets startup ≤7,500 · seat block ≈1,383.

**A-line inheritance note:** the 8 B files embed the pre-edit A@`1915599`. On
2026-07-12 the integrator added one LANDING sentence to `../universal-startup.md`
(founding-brief-vs-relay dispatch rule, fm PR #99 evidence; A body now 5,868c) —
the B files predate that line and inherit it at the next regen; do NOT retrofit
it by hand.

## Failsafe cron stagger table (no collisions, verified 2026-07-12)

| Seat | cron | Slot | Provenance |
|---|---|---|---|
| self-improvement | `0 */2 * * *` | even hours :00 | proposed (integrator-harmonized) |
| game-lab | `15 */2 * * *` | even hours :15 | **baseline kept** (`../../baseline-2026-07-11/game-lab.md`) |
| fleet-manager | `30 */2 * * *` | even hours :30 | **census-verified** (core census §fleet-manager, trig_01BKpsyoBzp1K1ob9H3iu1gM per parked #97) |
| websites | `45 */2 * * *` | even hours :45 | **baseline kept** (`../../baseline-2026-07-11/websites.md`) |
| superbot | `0 1-23/2 * * *` | odd hours :00 | proposed (integrator-harmonized) |
| superbot-world | `15 1-23/2 * * *` | odd hours :15 | proposed (integrator-harmonized) |
| ideas-lab | `30 1-23/2 * * *` | odd hours :30 | proposed (integrator-harmonized) |
| venture-lab | `45 1-23/2 * * *` | odd hours :45 | proposed (integrator-harmonized) |

Every seat wakes every 2 hours; no two seats share a minute-slot in the same hour
parity. The manager's :30 even slot is the fan-in read point the lanes stagger
around. Venture-lab's kept grading trigger (`0 9 * * 5`, trig_015aNMg5ncoSE2Roe4MKjQnr)
does not collide (Friday 09:00, rebind-per-F2).

## KNOWN DEFECTS → v3.1 queue (consolidated from the 8 drafter flags, 2026-07-12)

1. **A body over budget** — 5,467c at draft (now 5,868c after the LANDING addition)
   vs the ~5,000 §6 target; squeezes every seat delta, worst for dual/tri-repo
   seats (venture-lab, superbot-world had to compress A recap lines).
2. **A BOOT-1 orientation path hardcoded but dead in ≥4 repos** —
   `.claude/CLAUDE.md → docs/current-state.md → docs/CAPABILITIES.md` should
   become a `{{ORIENTATION_PATH}}` slot (fleet-manager, superbot-next, and others
   have no CLAUDE.md at HEAD; seats patch around it via SEAT DELTA blocks).
3. **A lacks a `{{FIRST_WORK_ORDERS}}` slot** — this README mandates the section;
   all 8 drafters inserted it between BOOT and WORK LOOP. Canonize that placement
   as an explicit slot in A at next regen.
4. **A BOOT-3 inbox read needs "in EACH repo"** for multi-repo seats (venture-lab,
   superbot-world, ideas-lab, game-lab each patched it locally).
5. **A BOOT-1 "(green expected)" clashes with expected-red seats** — fleet-manager
   (roster-freshness red), superbot-next (golden-parity red-by-design), and the
   substrate-gate born-red class; seats scoped it via EXPECTED-RED blocks.
6. **PACEMAKER "before ending ANY turn" wording** can be read against the
   session-ender's never-re-arm rule; needs an A-side "(the ender alone closes
   the chain)" clause.
7. **census-core vs census-sat conflict on pokemon-mod-lab required checks** —
   drafters resolved via "read the LIVE required-check set"; carry that resolution
   into v3.1 rather than either census figure.
8. **Ledger §2.7 "enabler in 3/13 lanes" figure stale vs census** — mineverse has
   the enabler at HEAD; re-count at next ledger pass.
9. **One HYPOTHESIS rides in superbot C** — settings-grants-cause-self-arm-success
   (platform-capabilities §2.5 marks it unproven); keep the HYPOTHESIS marker until
   proven or retired.
10. **trading MCP squash-on-green is encoded as precedent, not guarantee**
    ("every merge to date") — do not harden it into a rule without fresh evidence.
