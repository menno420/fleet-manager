<!-- v3.0-draft · 2026-07-12 · provenance: research PRs #93/#95 + owner baseline 2026-07-11 -->
<!-- char-count: 5,820 chars = this whole file (planning doc, no paste budget applies) -->

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
| 2 | **SuperBot 2.0** | superbot + superbot-next | `superbot-2.0-startup.md` + `-custom-instructions.md` | Core §superbot (heartbeat asserts superseded facts w/o `verified-against:` stamps; 79 KB orientation payload) + §superbot-next (no `.claude/CLAUDE.md` at HEAD — fresh session loads nothing; wake loop disarmed; stale OWNER-ACTION asking for an already-existing repo). |
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
