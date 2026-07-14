# Fleet inconsistency ledger

> **Status:** `living-ledger`
>
> Generated 2026-07-13 by the fleet review (owner directive). Live re-verification of
> individual items extended into 2026-07-14 (noted inline where it matters). Derived
> from the 19 per-repo deep-review notes (`fleet-review/notes/`, the truth source for
> this ledger); every item carries its citation (repo + path@SHA, PR #, or dated card)
> as recorded in the notes, and draft-only items were spot-checked against the review
> clones before inclusion. All repo content was treated as data (injection guard);
> "not found" beats invention throughout. This is a living doc: retire items by
> striking the row and citing the fixing PR/ORDER, never by deleting it.

---

## 1 · Count summary

- **82 ledger items** (INC-01 … INC-82), deduplicated from ~120 raw findings across 19
  per-repo review notes (the below-bar residue is now listed explicitly in §10a so
  dedup is auditable against the notes). Biggest collapses: stale capabilities-pointer
  class (≥10 repos → INC-29), kit-version drift (8+ instances → INC-40/41/42), inbox
  order-status lag (8+ repos → INC-73), coordination-protocol home split (13 repos →
  INC-32), dead-template weight (6+ repos → INC-71).
- **By severity:** **4 standing HIGH** (INC-01, INC-07, INC-16/17 as a pair, INC-18 —
  plus INC-44 rated HIGH by its lane's notes, INC-43 rated MED-HIGH pending the fleet
  ruling, and INC-68's historical-HIGH with an unmerged residual guard) · **~36 MED** ·
  remainder LOW / INFO.
- **By disposition:** **~24 fix-now-in-fm** (Class A nearly entire — the records
  custodian can repair its own surfaces today) · **~40 ORDER-to-lane** (substrate-kit
  the biggest single target with 9 items, several fix-once-ship-everywhere via seed
  templates) · **7 owner-call** (frozen-archive doctrine ruling · pokemon-mod-lab merge
  sweep · @codex gate-vs-suspend ruling · protocol canonical home · codetool release
  clicks · plugin-hello PR #1 disposition · `ROSTER_READ_TOKEN` secret + deliberate-pin
  rulings).
- **By class:** A fm-canonical-surface contradictions ×15 · B heartbeat/freshness ×14 ·
  C stale pointers/dead links ×11 · D version-line drift ×3 · E doctrine drift ×16 ·
  F contradictory records / false alarms ×6 · G historical errata ×7 · H dead template
  weight ×2 · I INFO/by-design ×8.

**Review pins** (state each repo was reviewed at): superbot @ `bbc524e4` ·
fleet-manager @ `ff6361a` (roster gen #36) · substrate-kit @ `727f5db` · superbot-next
@ `abe80c0` (#446) · websites @ `ba1aa86` · idea-engine @ `f6b1ff8` · sim-lab @
`3d7ae2c` · venture-lab @ `d1edd7c` · trading-strategy @ `0d12515` · gba-homebrew @
`982b23a` · pokemon-mod-lab @ `759dee4` · superbot-games @ `73111d0` · superbot-idle @
`24e468d` · superbot-mineverse @ `58657ed` · superbot-plugin-hello @ `bbaccec` ·
product-forge @ `4fdfa8a` · codetool-lab-fable5 @ `a6cf1a9` · codetool-lab-opus4.8 @
`80f6cd1` · codetool-lab-sonnet5 @ `66c3dfc`.

**Severity key:** HIGH = misleads owner/fleet operations right now · MED = misleads a
booting session or burns owner attention · LOW = localized, resolving pointer, or
self-disclaimed · INFO = by-design, recorded so sweeps stop re-flagging.
**Disposition lanes:** `fix-now-in-fm` = fleet-manager fixes in its own files /
generators, no cross-repo write · `ORDER-to-lane(<repo>)` = route via the control bus ·
`owner-call` = needs an owner ruling or click.

---

## 2 · Class A — Contradictory records in fm's own canonical surfaces (highest leverage)

fleet-manager is the declared records custodian (Option A, 2026-07-11); these are wrong
at the custodian itself. Cheapest, highest-trust fixes in the whole ledger.

| ID | Item — both sides cited | Severity | Disposition |
|---|---|---|---|
| INC-01 | **fm owner-queue OQ-PLUGIN-SEED-WORD says superbot-plugin-hello "exists but is EMPTY … re-verified today, Contents API 409" and blocks idle PLUG-001 on an owner word already delivered** — the repo was seeded 2026-07-12T13:29Z (`bbaccec`, ORDER 002/014 done per superbot-next `control/status.md:6`). Side A: fm `docs/owner-queue.md` L468–483 @ `d74eca4`; same staleness in fm `docs/fleet-triage.md:51` ("⚪ empty / SEED"). Side B: plugin-hello @ `bbaccec` (seeded, adapter built — idle PRs #75/#78). | HIGH | fix-now-in-fm — retire the queue item + re-verdict the triage row; note idle PLUG-001's HOLD reason is gone |
| INC-02 | **fm README front door still says "It is NOT program record. The fleet manifest … live in menno420/superbot (docs/eap/)"** — contradicting fm's own custodian mission and the superbot manifest's SUPERSEDED banner (fm PR #59 `b0639a9`, 2026-07-11). Side A: fm `README.md` L6–9 @ `ff6361a` (touched as late as PR #178 without the fix). Side B: fm PR #59 + superbot `docs/eap/fleet-manifest.md` SUPERSEDED banner. A booting agent reading only the README is pointed at a superseded doc. | MED | fix-now-in-fm — one-paragraph README fix |
| INC-03 | **fm fleet-triage vs fm consolidation plan verdict fork on codetool-lab-opus4.8**: `docs/fleet-triage.md:53` says **ARCHIVE** "after gen-3 succession settles" while `docs/planning/2026-07-12-repo-consolidation-plan.md:78` records **KEEP unarchived — "Agree — standing 2026-07-10 ruling + live mdverify releases"**. Two fm docs, opposite verdicts; the triage row contradicts a standing owner ruling (opus4.8 notes §5.1). | MED | fix-now-in-fm — re-verdict triage rows against the plan + owner rulings |
| INC-04 | **fm owner-queue OA-002 (sim-lab codex) marked resolved while sim-lab holds it open**: fm `docs/owner-queue.md:1430` + `docs/fleet-triage.md:48` "~~enable Codex~~ resolved — Codex envs exist for all 12 repos" vs sim-lab `control/status.md` ⚑ OA-002 open ("6+ @codex questions pending") + sim-lab current-state OA-002 open. The two conflate integration-ENABLED vs usage-QUOTA-capped; neither repo states the reconciliation. | MED | fix-now-in-fm — split the item (enabled=done, quota=open); cross-link sim-lab's ledger |
| INC-05 | **fm owner-queue #56 (OQ-TRADING-KILLSIG-VERDICT-CLASS) still asks the owner to approve the KILL-SIG verdict class trading already ratified and shipped** decide-and-flag. Side A: fm `docs/owner-queue.md` item #56 @ `ff6361a`. Side B: trading PR #109 "KILL-SIG ratification — verdict-class review ACCEPT" (2026-07-13); Round 6 grades 8 lanes KILL-SIG (PR #118, HEAD `0d12515`). (trading notes L175–180.) | MED | fix-now-in-fm — retire to decided-and-flagged |
| INC-06 | **fm owner-queue OQ-MINEVERSE-PYTEST-REQUIRED-CHECK stale-resolved**: still asks the owner to add `pytest` as required on mineverse main ("LIVE-PROVEN today"), but the owner did it 2026-07-11 and it is verified blocking — enabler rules probe verbatim `required contexts (2): ["substrate-gate","pytest"]`, Actions run 29260140367; re-confirmed live 2026-07-14, queue item carries no ✅ marker (mineverse notes §5.1/§11). Same class: C#20 (superbot codex-yaml) — superbot `control/status.md:16` says "RESOLVED by superbot PR #1995 — retire that line at the next sweep". | MED | fix-now-in-fm — expiry sweep; extend `check_owner_queue.py` to verify already-satisfied asks (the drift class the centralization plan's P2 checker exists for) |
| INC-07 | **fm `projects/README.md` superbot-idle registry row badly stale**: "PRs #1–#25, 216 tests, kit v1.7.1, failsafe **ARMED** `trig_01TWKGFW8RUsMvxUMt2ndzqA`" vs idle reality: 111 PRs / 1363 tests / kit v1.15.0 / that exact trigger **DELETED at close-out 2026-07-11** (idle `control/status.md` § ROUTINE RECORD; fetched live 2026-07-14, idle notes inconsistency 3). An fm reader acting on the row relies on a dead trigger id. | HIGH | fix-now-in-fm — regenerate registry rows from tree + live `list_triggers`, never hand-rows |
| INC-08 | **fm seat brief v3.6 claims corrected by mineverse's outbox; correction uptake unverified**: brief said mineverse CI = "substrate-gate + schema-gate" (no `schema-gate` context exists — the workflow file is `schema-gate.yml` but its check context is `pytest`) and "idle = NO enabler at HEAD" (refuted live: idle PR #87 merged by github-actions[bot] 2026-07-13T13:31Z). Four correction outbox entries in one day (mineverse outbox, 2026-07-13). | MED | fix-now-in-fm — apply the corrections; move seat-brief facts (CI contexts, enabler, kit) to a machine-derived registry (mineverse candidate 1) |
| INC-09 | **Q-id provenance fork**: fm surfaces label the pokemon QoL-deepening pick "Q-0266" where the verbatim superbot router entry is **Q-0262.7** (verified at superbot HEAD `58040c6` per pml PR #70); pml's own backlog / current-state / review-queue rows also cite "Q-0266". Provenance ids diverge across fm, pml, and superbot. | MED | fix-now-in-fm + ORDER-to-lane(pokemon-mod-lab) — correct the label; adopt repo-qualified ids (`superbot#Q-NNNN`) going forward |
| INC-10 | **Two enabled identical fm failsafe crons, both passing health checks**: `trig_01FpTbpXCeGcotnBpTkscAdr` and `trig_01UQTZFvknBosXVo4YKKfazZ`, both `30 */2 * * *` — invariant I4 verifies a failsafe *exists* but never flags duplication; double-fire every wake window. Clone-verified this pass (fm `.sessions/2026-07-13-wake-1633z.md:16`; proposed I8 DUPLICATE-CRON invariant unshipped). | MED | fix-now-in-fm — delete one; ship the I8 duplicate-cron invariant |
| INC-11 | **Dead local link in fm owner-queue**: OQ-POKEMON-ROM-REQUIRED-CHECK cites "docs/PLATFORM-LIMITS.md" with no repo qualifier — no such file exists in fleet-manager (3 hits, clone-verified). The real file is pokemon-mod-lab's. | LOW | fix-now-in-fm — qualify as `pokemon-mod-lab docs/PLATFORM-LIMITS.md@SHA` |
| INC-12 | fm `docs/current-state.md` §In-flight self-stale: PR #86 (merged 2026-07-11) and #178 (merged 07-13/14) still listed in-flight; the header defends itself as a dated snapshot. | LOW | fix-now-in-fm — next re-stamp |
| INC-13 | fm `docs/evidence-index.md` header declares "Program-narrative home: … superbot docs/eap" but the generated body contains **zero** links into docs/eap (grep 0 @ `eff4c7d`/`ff6361a`) — the "one front door" (consolidation plan §3c) reaches heartbeats but not the program record. | LOW-MED | fix-now-in-fm — add per-document EAP index rows |
| INC-14 | fm `docs/fleet-triage.md:48` "10 verdicts" vs 62 verdicts at sim-lab HEAD `3d7ae2c` — dated-snapshot class in the custodian's own register. (Counting note: 62 is the verdict-numbering high-water mark, which is how sim-lab itself counts — the ledger runs through VERDICT 062 and `sims/verdict-062-*` exists; 57 verdict directories are on disk.) | LOW | fix-now-in-fm — same sweep as INC-01/03 |
| INC-15 | fm ORDER 019 relay to superbot-next cites "the stamped owner decision in `docs/owner-queue.md`" — no such file exists in superbot-next (it is fm's own path); a seat obeying the order cannot resolve the reference in-repo. | LOW | fix-now-in-fm — relay template always repo-qualifies paths |

## 3 · Class B — Heartbeat / freshness-signal failures (stale meta, operational)

Shared root cause: ORDERs forced appends into status files some seats treat as "frozen
archives" (superbot `docs/fleet-reading-path.md:55-56` even blesses this) while every
`control/README.md` mandates overwrite-per-session — and fm's roster reads heartbeat
prose as truth. One doctrine ruling covers INC-16/17/19/80.

| ID | Item — both sides cited | Severity | Disposition |
|---|---|---|---|
| INC-16 | **superbot-games heartbeat frozen at `updated: 2026-07-12T10:16:22Z` while ~50 PRs (#61–#113) shipped since.** Side A: games `control/status.md` @ `73111d0` (internal conflict recorded in the file itself: "frozen archive" vs the overwrite contract). Side B: fm roster gen #36 rated the seat DARK ~37h, and fm's final-night worklist (L239) asked the owner to re-wake a seat that shipped #92–#106 that same night; the seat's #94 NIGHT HEADLINE had to rebut the verdict. | HIGH | owner-call (doctrine: frozen-archive vs overwrite, ruled once fleet-wide) + fix-now-in-fm — roster gains a commits-vs-heartbeat divergence column so DARK is never declared on heartbeat alone |
| INC-17 | **superbot-idle heartbeat stale the same way**: `updated: 2026-07-13T17:43Z`, `orders: done=000-005` while ORDERs 006/007 were served (PRs #101–#111); the ORDER 005 preamble itself records "Doctrine conflict flagged, not resolved." Two binding texts disagree about the same file. | HIGH | same ruling as INC-16; ORDER-to-lane(superbot-idle) to re-stamp once ruled |
| INC-18 | **pokemon-mod-lab `docs/current-state.md` @ HEAD `759dee4` materially false**: "ARCHIVE-READY … zero open PRs … all 46 PRs merged" + cites the retired hourly trigger as armed — vs live 14 open PRs / 72 total and the trigger retired at the 07-12 cutover. The truth fix (PR #64) is itself parked green-unmerged: the park-and-sweep convention is holding its own fix hostage. | HIGH | owner-call — one merge sweep of the parked green PRs (#57 .gitignore guard, #64 truth fix, #70 Q-id fix + `repo.private` CI assert); the repo has no enabler, only owner clicks land anything |
| INC-19 | gba-homebrew `control/status.md` top block stale ("updated 2026-07-12T16:20Z … PR #68/#69 parked awaiting clicks" — both merged) while 3 dispatch sections were appended below; the session-37 dispatch itself flags the staleness. Its own contract says wholesale-overwrite. | MED | ORDER-to-lane(gba-homebrew) — one overwrite re-stamp; covered by the INC-16 ruling |
| INC-20 | fm roster misclassified pokemon-mod-lab **DARK/UNREADABLE** (gen #35) while it had 8 green-parked PRs and live wakes — "the UNREADABLE wall was the terminal-prompt access path, not the repo" (pml ORDER 007 @ `990b79c`); needed an owner override to reactivate. Durable fix (fm PR #144 `ROSTER_READ_TOKEN` wiring) awaits the owner's Actions secret. | MED | owner-call — set the secret; fix-now-in-fm — render the one private repo distinctly from DARK until then |
| INC-21 | superbot `docs/operations/autonomous-routines.md` presents a dead trigger as live: dispatch schedule "every ~2-3h, owner-enabled 2026-06-15" (L28–30, L286–289 @ `bbc524e4`) while fm telemetry shows it owner-paused with `next_run_at` frozen 2026-07-02 (11+ days). ORDER 003 (fix + annotate) `status: new` at HEAD. | MED | ORDER-to-lane(superbot) — already ordered; escalate/re-fire ORDER 003 |
| INC-22 | superbot-next top orientation docs ~3–4 days of extreme velocity stale: README "band 5 live-testing in flight" + current-state §In-flight (snapshot 2026-07-10, "62 decisions") vs parity 0-pending/51-ported, `decisions.md` at 89 entries, report leg live-green 07-13, ~250 PRs since. The entry docs contradict the README's own next paragraph. | MED | ORDER-to-lane(superbot-next) — re-stamp both entry docs |
| INC-23 | websites `docs/current-state.md:125` still says the control-plane GITHUB_TOKEN "is currently UNSET (live finding 2026-07-10/11)" under In-flight, vs `docs/CAPABILITIES.md` 2026-07-12 entry "RESOLVES the … wall — the live control-plane now runs with a working GITHUB_TOKEN (OWNER-ACTIONS Decided row H)". Survived two truing passes (#308). | MED | ORDER-to-lane(websites) |
| INC-24 | websites `.session-journal.md` Quick reference stale: line 11 "one repo, three independent services" and line 29 "Tests (60 total)" vs four services / 1345+ tests; last touched 2026-07-10. It is a session-start orientation doc (websites notes §stale-journal). | MED | ORDER-to-lane(websites) |
| INC-25 | mineverse `docs/current-state.md` § CI still declares the born-red "Known gap … interim rule: push the flip BEFORE opening the PR" though kit v1.15.0 (PR #80 `1520e05`) closed it — contradicts both the workflow file and `control/status.md` at the same HEAD `58657ed`. | MED | ORDER-to-lane(superbot-mineverse) |
| INC-26 | substrate-kit `docs/current-state.md:95-98` still lists PR #263 (grounded-skills plan) as THE in-flight item — the 8 slices + wrap shipped 2026-07-12 (wrap #301 `6d5ce67`, rode v1.15.0). By the repo's own CONSTITUTION rule this is fix-on-sight. | LOW | ORDER-to-lane(substrate-kit) |
| INC-27 | Smaller ledger lags, self-disclaimed dated-snapshot class: superbot-games current-state "#107" vs main #113 (3× recurrence → KIT-ASK ledger-drift check filed, unserved); venture current-state PR #174 spliced into the #141–#161 day list + "12 complete EN manuscripts" vs NEXT-SESSION "11"; mineverse "In flight: Nothing" vs open PR #90; sim-lab "verdicts through 059" vs 62; idea-engine In-flight ~1 day behind (P049 vs P052). | LOW | ORDER-to-lane(each, next touch); the venture/games items motivate the `docs-counts`/ledger-drift advisory checkers already proposed in-lane |
| INC-28 | product-forge heartbeat never carried the `kit:`/`last-shipped:`/`blockers:` lines its own protocol copy requires (whole-life gap; archive-bound); its priority grammar also drifted (inbox P3 vs protocol P0–P2). | LOW | ORDER-to-lane — fold into the forge close-out (E#44); no standalone fix |
| INC-81 | **venture-lab `docs/review-queue.md` PR #9 row 3+ days stale**: says #9 is "not yet landed — awaiting the owner merge" while #9 MERGED 2026-07-10T05:11:50Z (squash `95b755b`, ORDER 004 context; outbox ORDER 006 citations), and the queued re-check was never recorded as done — the merge-then-flag ledger's only row is wrong in a repo whose whole rhythm is post-merge review (venture notes, inconsistency 3). | MED | ORDER-to-lane(venture-lab) — re-stamp the row + record the re-check disposition |

## 4 · Class C — Stale pointers & dead links (single root cause, fleet-replicated)

| ID | Item — both sides cited | Severity | Disposition |
|---|---|---|---|
| INC-29 | **Kit-seeded "Fleet master copy: fleet-manager → docs/capabilities.md" pointer is stale in ≥10 repos** — the target became a MOVED stub 2026-07-12 (I-44 fold into fm `docs/CAPABILITIES.md`). Confirmed in the notes for: substrate-kit (its own `docs/CAPABILITIES.md:7-9`, stale BOTH directions — fm's fold note says the master is "the kit-owned uppercase file" while the kit points at fm's dead lowercase path), superbot-next, websites, idea-engine, sim-lab (implied via empty ledger), superbot-idle, superbot-games, superbot-mineverse, pokemon-mod-lab, product-forge, codetool-lab-fable5 (PLATFORM-LIMITS rider ×2), trading-strategy. fm's own `docs/seat-digest.md:71-73` "No third copy" step 3 names the same dead lowercase path. Stub resolves → LOW per instance; MED aggregate as the drift-by-construction exhibit. | MED (aggregate) | ORDER-to-lane(substrate-kit) — fix the seed template once, ships to all adopters at next upgrade; fix-now-in-fm for fm's own seat-digest line |
| INC-30 | **Superseded superbot `docs/eap/fleet-manifest.md` still cited as the live registry** by idea-engine `docs/architecture.md:10`, `docs/AGENT_ORIENTATION.md:18`, `docs/ownership.md:25`, `.claude/CLAUDE.md:49` (stale interview slots never re-rendered after the 2026-07-11 supersession — fm PR #59 `b0639a9`). A session following the binding architecture doc consults a dead registry; the manifest's banner saves it in practice. | MED | ORDER-to-lane(idea-engine) — re-interview + `bootstrap render`, not hand-edit |
| INC-31 | **superbot `docs/fleet-reading-path.md:48` claims superbot has "no heartbeat file"** while `control/status.md` has existed since 2026-07-11 (PR #2003, `573ba978`) and is aggregated by fm's roster + evidence-index; both files last touched 2026-07-13 — the row survived the refresh. Misleads every new cross-repo session about where superbot truth lives. | MED | ORDER-to-lane(superbot) — one-row fix |
| INC-32 | **Coordination-protocol canonical home split across three repos**: every fleet repo's `control/README.md` names superbot `docs/planning/fleet-coordination-protocol-2026-07-09.md` as canonical spec (found in the notes for websites, idea-engine, sim-lab, trading, gba, pokemon, games, idle, mineverse, forge, all three codetool arms), while grammar truth sits in kit `src/engine/grammar.py` and the lane registry in fm `gen_roster.py` — "nothing says which wins" (websites notes §8). Several local copies have grown load-bearing local doctrine (idea-engine claim ritual) a naive centralization would lose. | MED (structural) | owner-call (small): ratify fm (or kit program docs) as the canonical protocol home, then ONE kit/fm pass converts N copies to pointer+delta — do not fix per-repo piecemeal |
| INC-33 | substrate-kit `docs/AGENT_ORIENTATION.md` step 1 says read `.claude/CLAUDE.md` — no `.claude/` exists in the self-hosting repo (the agreement is root `CONSTITUTION.md`). Clone-verified this pass @ `727f5db`. | LOW | ORDER-to-lane(substrate-kit) |
| INC-34 | superbot-next `.claude/CLAUDE.md:56` (and its render source) say the pre-push verify is `python3 -m pytest` at repo root, while `ci.yml` runs `pytest tests/ -q` and CAPABILITIES records the verified wall "repo-root pytest breaks on examples/". A fresh session following the binding doc hits a false red. | LOW-MED | ORDER-to-lane(superbot-next) — re-render the verify slot |
| INC-35 | codetool-lab-fable5 `docs/ROADMAP.md` "Parked" still says the Actions release route is "policy-denied … do not re-attempt" though PR #14 corrected the wall to **SEAT-DEPENDENT** (opus4.8 shipped 2 live Releases via the same route); NEXT-BOOT sends gen-2 to ROADMAP as reading item 5, so a successor could re-inherit the corrected-away lesson. Sonnet5's NEXT-BOOT/status similarly teach the superseded owner-tag-push recipe vs the fm-recommended workflow_dispatch path (fm evidence E#45). | MED | ORDER-to-lane(codetool-lab-fable5, -sonnet5) — one-line fixes at next touch (or fold into the archive disposition) |
| INC-36 | superbot-next / plugin-hello contract split: superbot-next `docs/game-plugin-contract.md:9-11` still says the working example is in-tree "**pending** the owner-created repo … move it verbatim" — the move happened 2026-07-12 (plugin-hello `bbaccec`) and the verbatim in-tree duplicate still exists: two sources of truth for the template every game repo copies. | MED | ORDER-to-lane(superbot-next) — fix the note; mark the in-tree copy frozen-mirror or delete |
| INC-37 | Succession packs target generations that will never boot: fable5 + opus4.8 `NEXT-BOOT.md` ("you are the next incarnation") vs fm `meta.md` "Fully retired — no successor seat" (2026-07-11); opus4.8 README still self-describes "throwaway eval repo" while the owner's ruling keeps it as a live released-tool host. | LOW | ORDER-to-lane — tombstone notes at next touch; archive-bound repos |
| INC-38 | CHANGELOG release links dead in two public tool repos: fable5 CHANGELOG links v0.1.0/v0.2.0 tags that don't exist (0 tags, 0 releases — owner ritual never ran); sonnet5 links v0.1.0/v0.1.1 with `git ls-remote --tags` empty (release.yml has never fired; cfgdiff not on PyPI). Public-facing front doors of installable tools. | MED | owner-call — execute the queued release clicks (fable5 ⚑ items; sonnet5 E#45 decision A = release-in-place), or strip the links |
| INC-39 | superbot-idle `CONSTITUTION.md:55` asserts fleet instruction text is canonical at "fleet-manager `projects/`" — fm has `projects/README.md` but no `projects/superbot-idle.md` (404); the pointer resolves only loosely. | LOW | ORDER-to-lane(substrate-kit) — template pointer precision |

## 5 · Class D — Version-line drift (kit: lines / pins vs tree)

One systemic item, many instances. The fleet's own CONSTITUTION template predicts it
("heartbeat `kit:` lines chronically lag the tree by 1–3 releases — verify against the
tree"), yet the roster/registries still parse kit versions from heartbeat prose.

| ID | Item — both sides cited | Severity | Disposition |
|---|---|---|---|
| INC-40 | **Registries derive kit-version from self-reports, so the record is wrong wherever a lane forgot a re-stamp**: fm itself has NO `kit:` line at all (kit `docs/adopters.md:36` renders a stale remembered v1.7.0 where the evidence was "absent"; fm `bootstrap.py` = 1.15.0); pokemon heartbeat `kit: v1.12.0` vs tree 1.15.0; idle heartbeat v1.7.1 vs tree 1.15.0 (8-release gap); sim-lab current-state "kit v1.7.0" vs status/tree v1.15.0; idea-engine current-state baseline pins v1.10.0 vs tree v1.15.0; fm roster renders superbot-games archived gen-1 lane rows as "substrate-kit v1.7.1" as if current; kit's archived visiting-lane heartbeat carries a parseable `kit: v1.7.0` line a naive fleet grep collects. Positive checks: trading, gba, and venture-lab are drift-FREE (tree = line = 1.15.0, verified; full verified-consistent list in §10b). | MED | fix-now-in-fm — generator reads `substrate.config.json` / `.substrate/state.json` from each tree as primary, heartbeat as fallback; fm adds its own `kit:` line (the kit's outbox ask, unactioned); exclude archived per-lane files from KIT_LINE parsing |
| INC-41 | Deliberate pins, listed so no registry "fixes" them: superbot `substrate.config.json` pins kit 1.0.0 (acknowledged per CLAUDE.md Q-0254 note "until superbot itself upgrades from a real kit release" — 15 minor releases, the largest gap in the fleet, and fm roster shows the hub's pin as "—", invisible); substrate-kit self-pin 1.0.0 = the designed owner-held pin path (DRIFT row rendered by design). | LOW | owner-call — land the superbot kit upgrade / keep the designed rows labeled intentional; fix-now-in-fm — roster surfaces the hub's pin instead of "—" |
| INC-42 | superbot-plugin-hello pins kit 1.13.0 while host superbot-next pins 1.15.0 — the seed commit's "mirroring the host's pin" claim no longer holds; no planted docs, so nothing in-repo flags it. Same commit cites manifest hash `06023075…` "stays valid unchanged" that was already stale when written (drifted at host #232; live lock pins `ff75b9eb…`, fixed by host #311). | LOW-MED | fix-now-in-fm — fleet kit-version table (repo → pinned → current) + plugin-pin drift check (plugin-hello audit suggestions 2/4) |

## 6 · Class E — Doctrine drift (live doctrine contradicts practice or itself)

| ID | Item — both sides cited | Severity | Disposition |
|---|---|---|---|
| INC-43 | **@codex review doctrine fork**: sim-lab README L61–63, CONVENTIONS, and owner-profile still MANDATE the @codex step on every verdict PR ("no verdict bypasses… Q-0264.4") while the step is **SUSPENDED** @ `dedc12e` after 3/3 verified fabricated reviews (incidents #1–#3, sim-lab outbox L163); current-state fixed its own wording 2026-07-13 but the three binding docs still contradict it. Meanwhile fm ordered fleet-wide adoption of the VERDICT 016 authenticity gate ("gate, don't suspend" — fm inbox L1095) — reinstatement parked with manager/owner. | MED-HIGH | owner-call — one fleet ruling: gate (VERDICT 016 spec) vs suspend; then ORDER-to-lane(sim-lab) annotates the binding docs once |
| INC-44 | **venture-lab binding conventions grant what the classifier denies**: `docs/conventions.md` rules 2–3 "This lane ALWAYS lands its own PRs — written grant … arm it at creation" (cited by `review-queue.md` as "the self-merge grant") vs PLATFORM-LIMITS' verbatim classifier denials of BOTH the self-merge and the arm, and current-state's "Lanes never arm or merge their own PRs" (the enabler workflow arms). The binding text was superseded in practice, never updated. | HIGH (per lane notes) | ORDER-to-lane(venture-lab) — rewrite rules 2–3 to the enabler doctrine |
| INC-45 | **"Cannot arm routines" wall falsified but still taught**: substrate-kit current-state 👤 P4 tells the owner to arm the kit-lab loop via Console → Schedules while ORDER 010 self-armed the hourly wake 2026-07-10 (CAPABILITIES append-log correction); venture-lab `docs/CAPABILITIES.md:146` groups "Environment / routine / Project creation" as owner-click though the seat demonstrably arms/deletes its own triggers. Both clone-verified this pass. Fleet-wide, agent-side `create_trigger` was proven 2026-07-10/11 (games, pml ORDER 002). | MED | ORDER-to-lane(substrate-kit, venture-lab) — narrow the wall to environments/Projects only; retire P4 |
| INC-46 | substrate-kit current-state "prefer merging by hand (MCP) after verifying CI green" (L336, clone-verified @ `727f5db`) vs live practice (enabler auto-merge on green; direct agent self-merge classifier-DENIED in unattended venues) — a literal follower hits the classifier wall. | MED | ORDER-to-lane(substrate-kit) |
| INC-47 | **Claims-directory dual homes**: venture conventions rule 6 + root `claims/README.md` still `binding` while config + practice use `control/claims/`; pokemon root claims/README same (kit checker names it `claims-legacy-location`); gba legacy root `claims/` flagged across 3 consecutive kit-upgrade cards with zero pickup. A fresh session files a claim where nobody looks. | MED | ORDER-to-lane(venture-lab, pokemon-mod-lab, gba-homebrew) — demote root claims/ to pointer stubs |
| INC-48 | **Two walls ledgers split the record and empty the machine surface**: sim-lab's real walls live in PLATFORM-LIMITS.md so `docs/seat-digest.md` renders "(no walls recorded)" — the digest fm's seat-prompt regen consumes shows ZERO walls while ~10 verified walls exist; venture-lab's digest likewise empty (entries lack venue tags) with ~8 verified walls on file; gba carries THREE overlapping capability records (manifest copy vs kit ledger vs PLATFORM-LIMITS) with README and CONSTITUTION pointing at different ones; pokemon's two copies "differ from line 1" with README linking the stale one. | MED | ORDER-to-lane(sim-lab, venture-lab, gba-homebrew, pokemon-mod-lab) — fold walls into the kit CAPABILITIES ledger with venue tags; stub the others (the seat-digest "no third copy" contract already mandates this) |
| INC-49 | substrate-kit CONSTITUTION register line enumerates PL-001…PL-009 while the rulings register holds PL-011 — the first-read file is 2+ rulings behind (clone-verified, `CONSTITUTION.md:50-53` @ `727f5db`). Related: fm `docs/decisions.md` holds only D-0001 while its real rules live as playbook R1–R27 (MISSION.md even cites "drift-fix D6", an F-number, as a D-entry); sim-lab cites D-0008 in current-state + cards while its `decisions.md` holds only D-0001 — the provenance ledgers the CONSTITUTION mandates are behind their own citations. | LOW-MED | ORDER-to-lane(substrate-kit, sim-lab) + fix-now-in-fm — sync registers or declare the alternate grammar canonical |
| INC-50 | fm ORDER phrasing "ack in your inbox thread" contradicts the kit's inbox-order-grammar gate (rejects non-ORDER inbox appends — verified live on idle PR #104; mineverse ORDER 006 hit the same machine-unsatisfiable done-when, ack rerouted to outbox with a grammar-fix ask filed 23:44Z; trading's lane also appended an inbox ack under ORDER 014 against the one-writer header). | MED | fix-now-in-fm — change the ORDER template to "ack via outbox/status line"; playbook note |
| INC-51 | mineverse `.claude/CLAUDE.md` architecture slot still stage-1: "no auth … no database … the server never writes" vs shipped `server/auth.py` (PR #11) and the FLAG-1 ingest endpoint that WRITES `MINING_SNAPSHOT_PATH` (PR #88 @ `82b7caa`). The boot-set doc misdescribes the runtime surface. | MED | ORDER-to-lane(superbot-mineverse) — re-interview + `bootstrap render`, not hand-edit |
| INC-52 | superbot-games ORDER 008 INTERPRETATION (b) "bring all three games to production-grade" while the hub registers FOUR (mining, fishing, dnd, exploration) and the owner verbatim said "all the games" — an order interpretation under-counting scope by one game. | LOW-MED | ORDER-to-lane(superbot-games) — correct the interpretation line |
| INC-53 | gba `conventions.md` rule 16/2 seed-time claims ("No CI workflows exist at seed", "REST merge is PRIMARY") vs 4 live workflows + enabler (PR #76); qualified by "at seed" but a fast reader lands on the wrong merge path. Same class: pml `substrate.config.json` declares automerge for `claude/*` while no enabler workflow exists there and park-and-sweep is the convention (OWNER-ACTION 1 open). | LOW-MED | ORDER-to-lane(gba-homebrew) — diverged/render stamp + delta list (its own candidate 7); the pokemon item folds into the INC-18 owner sweep |
| INC-54 | websites `auto-merge-enabler.yml` vs `host-automerge-extras.yml` — self-documented unreconciled arm/disarm race on workflow-touching PRs (host file header; websites audit finding #4). | LOW-MED | ORDER-to-lane(websites) — reconcile the two workflows |
| INC-55 | websites CONSTITUTION binding rail names only three services ("control-plane, botsite/, dashboard/ [D-0007]") — review/ live since 2026-07-12 is absent from the rail. README founding text similarly stale in gba ("Play it" lists 2 of 7 shipped ROMs, PLAYING-BRINEWARD.md unlinked — public front page under-selling 5 games). | LOW-MED | ORDER-to-lane(websites, gba-homebrew) — front-door refresh at next touch |
| INC-56 | trading `docs/owner-profile.md:11` carries "menno420 (mennovanhattum@gmail.com)" while the same file's Privacy note says "No contact details… nothing that identifies the person." Public repo; kit-template class (every adopter carries a variant). | LOW | ORDER-to-lane(substrate-kit) — fix at the template; one canonical owner profile + pointers is the centralization candidate |
| INC-57 | trading CONSTITUTION line 55 slot "When a doc and a source file disagree:" is filled with adopt-time narrative instead of a precedence rule, and the "Rails specific to trading-lab" section is an empty placeholder while the repo's strongest rails (research-only, holdout SPENT, D-0002) live elsewhere. Substrate-kit's own "Rails specific to substrate-kit" placeholder is likewise empty after ~350 PRs. | LOW-MED | ORDER-to-lane(trading-strategy, substrate-kit) — fill or delete the slots; kit-product feedback (see INC-71) |
| INC-82 | **substrate-kit `README.md` never updated since extraction**: `README.md:124-126` @ `727f5db` (last touched by `3d303a0`, 2026-07-08) still says "Tests live in the host repo at `tests/unit/substrate_kit/` during the in-repo proving phase and move to `substrate-kit/tests/` on extraction" — the extraction happened 2026-07-08 and `tests/` holds 1366 tests (#351 card). The front door of the fleet's most-adopted artifact describes the pre-extraction world (kit notes §5.2); same public-front-page class as INC-55. | LOW-MED | ORDER-to-lane(substrate-kit) — README refresh at next touch |

## 7 · Class F — Contradictory records / false alarms burning owner attention

| ID | Item — both sides cited | Severity | Disposition |
|---|---|---|---|
| INC-58 | **superbot-next ⚑8 history-rewrite false alarm — standing owner ask contradicting git ground truth**: `control/status.md`@HEAD asks the owner to confirm a possible history rewrite ("history now roots at 2cb4d91, ~104 commits; #319's SHA no longer resolves"). Full-clone ground truth (this review): 446 commits, root `de36d28`, #319's squash `91b0767` resolves, `2cb4d91` is just PR #334 — a shallow-clone artifact the coordinator's own 07-12 addendum had already identified. Safe to withdraw. | MED | ORDER-to-lane(superbot-next) — withdraw ⚑8 with the ground-truth citation |
| INC-59 | **codetool-lab-sonnet5 archive is self-blocked by an unexecuted fm ORDER**: consolidation-plan P1-4 (port the differential-oracle method + release-decision writeups into substrate-kit) issued 2026-07-12, verified UNEXECUTED at kit @ `4e09862`/`727f5db` (no cfgdiff/differential hits); neither repo surfaces the gap; the done-when requires sonnet5's status to point at the ported docs. | MED | ORDER-to-lane(substrate-kit) — execute P1-4, then sonnet5 status pointer; unblocks the E#45 archive click |
| INC-60 | **superbot-plugin-hello PR #1 (fleet audit) can never land**: repo has no CI, no enabler, no merge convention — open indefinitely against Q-0103 terminal-state doctrine; the PR body defers to "this repo's own auto-merge/sweep convention", which does not exist. Sonnet5's freshest evidence (the 26/26-green 07-13 audit) is likewise stranded on unmerged branch `audit/fleet-cleanup-2026-07-13` @ `14cedd5`, invisible to main-only indexes. | MED | owner-call — one manual merge (or fm sweep decision) each; fix-now-in-fm — add plugin-hello to a no-heartbeat-by-design allowlist (its own audit suggestion 3) and index the sonnet5 branch @SHA in evidence-index |
| INC-61 | **Duplicate grading fire 2026-07-17 (time-bound)**: trading's seat cron fires 09:05Z and a FOREIGN `trig_01YXNmgqYeYQ1LuepsLmbNCG` send_later fires 09:00Z — concurrent-grading double-write risk stated in trading's outbox GRADING PRE-VERIFY (2026-07-13T22:50Z), disposition still awaiting the manager; venture-lab's status flags the same foreign trigger as a potential duplicate 2026-07-17 grading fire. fm telemetry still carries it. | MED (deadline 07-17) | fix-now-in-fm — disposition before Friday: delete/re-own the foreign trigger, log in triggers-snapshot |
| INC-62 | fm roster gen #36 (`docs/roster.md` @ `ff6361a`) shows idea-engine "**NONE** — (no attributed triggers)" while idea-engine's heartbeat claims failsafe cron "Ideas Lab failsafe wake" `trig_01YGs7oTwL3XoXj59hDHbPyi` ENABLED and live (idea-engine notes, inconsistency 3) — either roster trigger-attribution misses it or the heartbeat claim is stale; either way the manager's wedge watchdog cannot see this seat's chain. | MED | fix-now-in-fm — extend roster trigger name→lane attribution; verify against the registry |
| INC-63 | product-forge's own resume recipe contradicts the fleet's archive verdict: `archive-ready-2026-07-11.md` + status instruct a fresh session to re-arm the wake and resume continuous mode; fm's 07-12 plan verdicts MIGRATE-THEN-ARCHIVE and "product-forge is DARK and never receives ORDERs". Nothing in the forge repo mentions the verdict — a session booted per its own docs would re-arm a wake on a repo slated for archive. | MED | fix-now-in-fm — land the final-status pointer the plan's own done-when wants (ORDER 023), ahead of the E#44 click |

## 8 · Class G — Record/evidence errata (historical; index-don't-rewrite)

| ID | Item — both sides cited | Severity | Disposition |
|---|---|---|---|
| INC-64 | opus4.8 `project-review-final` claims "#19 `c96318c` = the main tip at wind-down" — superbot's winddown audit (finding 2) shows #20–#22 merged after, real tip `80f6cd1`; plus a citation misattribution (finding 5: quoted error text attributed to the self-review that only paraphrases) and the 102-vs-103 test-count slip never amended in-file. Corrections live only in superbot docs, never in-repo. | LOW-MED | fix-now-in-fm — attach errata notes to the evidence-index rows pinning those retros |
| INC-65 | sonnet5 "two-arm model-comparison" wording in README/reviews (three arms; its own PR #1 body names both siblings) — flagged by its own unmerged audit, unfixed on main @ `66c3dfc`. | LOW | fix-now-in-fm — same errata pass as INC-64 |
| INC-66 | gba PR #104 titled "control: ack night ORDER" while its entire body reports the ORDER **missing** ("no night ORDER in control/inbox.md at HEAD — please re-deliver") — a manager parsing titles would misread the night as ordered. | LOW | fix-now-in-fm — sweep rule: parse ack bodies, not titles |
| INC-67 | websites `docs/CAPABILITIES.md:226` corrupted append entry — the 2026-07-09 release-asset capability lost its bullet lead line (present at `ab0995d`; orphaned "HTTPS** (…)" fragment reads as a continuation of the entry above) in the ledger the fence-extraction contract feeds. | LOW-MED | ORDER-to-lane(websites) — restore the line from the earlier blob |
| INC-68 | pokemon "repo is PRIVATE" was asserted in README + 8 PR bodies while world-readable with vendored Nintendo source (2026-07-10→11; owner-fixed; fleet rule R22 born from it). Historical and guarded — but the `repo.private` CI assert (PR #70) is still parked unmerged. | HIGH historical / MED residual | owner-call — the INC-18 merge sweep activates the guard |
| INC-69 | Trigger-record residue handled correctly but trap-prone: trading's append-only night report cites three trigger ids deleted by the same-day cutover (supersession notes exist; a reader sampling one report gets dead ids); superbot's live registry carries the "suberbot docs reconciliation" name typo verbatim into fm roster + superbot status. | INFO/LOW | fix at next trigger re-arm; supersession notes already the right pattern |
| INC-70 | superbot-next cosmetic residue, tracked by its own ⚑7: "RED BY DESIGN"/"EXPECTED RED" strings live in the parity harness/workflow step names although the report leg went live-green 2026-07-13 — exactly the class README-first warns misleads fresh sessions, now in the opposite direction. Checker-count drift ("22-checker" vs "23-checker fleet") same class. | LOW | ORDER-to-lane(superbot-next) — next touch |

## 9 · Class H — Dead template weight (kit-planted, never filled — kit-product feedback)

| ID | Item — both sides cited | Severity | Disposition |
|---|---|---|---|
| INC-71 | `project.index.json` still the "example-area" generator stub in websites, gba-homebrew, pokemon-mod-lab (audit-confirmed, flagged in the fleet-cleanup audits); `.session-journal.md` an empty template after 62 sessions (gba), 140 cards (fm), and in sim-lab/pml; product-forge died with current-state/decisions/CONSTITUTION-rails all placeholders despite 23 PRs ("the kit's parallel ledgers were dead weight at 25-hour lifespan"); `question-router.md` carries zero Q-blocks in fm, kit, sim-lab, games, gba, forge, idle (owner intent flows via inbox ORDERs instead — kit surface vs practiced surface diverge). | LOW per-file, MED aggregate | ORDER-to-lane(substrate-kit) — kit-product feedback: force-fill at interview, make optional, or don't plant; per-repo fixes are whack-a-mole |
| INC-72 | Telemetry planted but inert: `telemetry/model-usage.jsonl` outcome fields permanently null in superbot-games and mineverse (48/48 rows); kit's own file has 1 seed row "never adopted"; fm's likewise. Model-matrix consumers must not expect outcomes. | INFO/LOW | ORDER-to-lane(substrate-kit) — outcome backfill by the claim-release session (games' own wishlist) or drop the fields |

## 10 · Class I — INFO / by-design (recorded so sweeps stop re-flagging)

- **INC-73 · Inbox ORDERs read `status: new` forever while status.md says done** — 8+
  repos (superbot-next "016 stale metadata, not an open order", sim-lab, trading,
  games, forge, all three codetool arms). Documented one-writer convention (fable5
  NEXT-BOOT even documents it), but only fm can flip and fm demonstrably doesn't — the
  manager's flips lag days. Disposition: fix-now-in-fm — run the flip in a manager
  sweep OR amend the protocol to declare status.md the sole order-state surface.
  (Upgrades to MED if left: every inbox misleads standalone, and any fm mirror must
  read status.md, not inbox.md.)
- **INC-74** · ORDER-number append races are a known, self-corrected class: pokemon
  duplicate-ORDER-007 (earlier-at-HEAD-wins + renumber precedent), fm rule R19 born
  from two day-1 collisions. Parsers must expect renumbering. INFO.
- **INC-75** · fm roster wake-state rows print past-due "next" stamps copied from the
  snapshot basis (gen #36: websites "next 20:45" vs generated 23:28Z) — snapshot lag
  reading as overdue; the health section explains the basis, the row doesn't.
  Presentation nit; fix-now-in-fm at leisure.
- **INC-76** · Roster-vs-heartbeat minute-level lag (websites "ORDER 027 in progress"
  @ 23:28Z vs status "COMPLETE" @ 23:47Z) — benign by design; roster self-declares
  derived-snapshot with kill-switch. INFO.
- **INC-77** · superbot's 5 standing supersede-banner soft warnings — the in-repo
  checker can't model cross-repo supersession (successors live in the fm registry);
  honest + documented, carried every recon pass since band-#1980. Closes only when fm
  models cross-repo successor links. Tracked, not per-repo actionable.
- **INC-78** · idea-engine superbot harvest pin ~2 days behind superbot HEAD — managed
  drift, its own `check_harvest.py` exists to size it; twin v1.15.0 kit-upgrade session
  cards self-explain a benign collision. INFO.
- **INC-79** · sim-lab boot card still `Status: in-progress` while `check --strict` is
  green — self-disclosed cosmetic. INFO.
- **INC-80** · idle/mineverse "frozen archive" heartbeats are BLESSED by superbot
  `docs/fleet-reading-path.md:55-56` while `control/README.md` mandates overwrite —
  recorded here as the doctrinal root of Class B; resolves with the INC-16 owner
  ruling, not per-repo.

## 10a · Consciously dropped (below the ledger bar — recorded so dedup is auditable)

These note findings were reviewed and deliberately NOT promoted to ledger rows
(localized, self-disclaimed, or folded into an existing class); they remain in the
per-repo notes (`fleet-review/notes/<repo>.md`), the truth source, if a lane wants them:

- venture-lab notes item 5 — PLATFORM-LIMITS in-file contradiction: the 2026-07-10 PR #9
  entry still claims "substrate-gate is not a required context" while the 2026-07-11
  PR #55 entry says it IS required and even instructs "Update any stale claim above" —
  flagged in-file, never edited. (Self-disclosed in the same file.)
- trading notes item 5 — fm `docs/review-queue.md` trading#21 row says the P1 drops are
  "CONFIRMED still undocumented at HEAD" while the annotation shipped in trading PR #53
  (`f4d9669`, 2026-07-11, `docs/p1-trend-following-results.md:88`). Row is
  RETIRED-SUPERSEDED, so no decision weight.
- superbot-games notes items 5–6 — outbox line 1 still titled "# game-mining · outbox"
  (gen-1 residue on the unified seat's outbox); two advisory claims docs
  (`docs/claims/world-games-inventory-{contract,seam}.md`) persist though their stated
  delete-conditions have fired (`games/shared/inventory/` long merged + tested).
- mineverse notes item 3 — README staged-ladder row (d) says "planned" vs current-state
  "PREPARED, owner-flag-gated" (PR #16 `ff1e5a6`); same-repo wording drift, current-state
  wins.
- product-forge notes item 6 — OA-003 (enable Pages) double-listed with diverging
  dispositions: forge status.md carries it open while fm owner-queue marks it effectively
  mooted pending the E#44 archive; coordinated, but a forge-only reader sees a live ask.
- pokemon-mod-lab notes item 11 — `docs/ideas/README.md` backlog has never had an entry;
  the lane's real ideas live per-card and in idea-engine `ideas/pokemon-mod-lab/*`
  (harvest ordered in the night worklist). Folds conceptually into INC-71's
  dead-template class.
- codetool-lab-fable5 notes item 6 — committed `__pycache__/*.pyc` under
  `src/envdrift/commands/` and `tests/`, no `.gitignore` (the seed lacked one per its own
  self-review E3). Hygiene only; archive-bound repo.

## 10b · Verified consistent (positive findings — recorded so sweeps stop re-flagging)

- trading-strategy and gba-homebrew kit lines drift-FREE: tree = heartbeat line =
  v1.15.0 (gba additionally verified `kit_version` = latest kit tag via
  `git ls-remote` — gba notes item 9, "unusual in the fleet and worth crediting").
- venture-lab kit line consistent at review: local tree = v1.15.0 (venture notes item 7 —
  the CONSTITUTION's own lag warning did NOT apply here).
- idea-engine, five checks all consistent (idea-engine notes): ASK 004 "unanswered at fm
  HEAD `eff4c7d`" matches fm `control/status.md`; kit v1.15.0 = latest substrate-kit tag;
  the manifest supersession banner exists exactly as its README describes; fm roster
  active lanes ↔ the 13 `ideas/` sections match; the outbox 368KB→459KB growth matches
  ASK 004's ~30KB/day estimate.

---

## 11 · Dominant root causes (what one fix retires)

1. **Heartbeat treated as truth by the roster while seats treat it as frozen archive**
   — one doctrine ruling + a commits-vs-heartbeat divergence column retires
   INC-16/17/19/80 and half of Class B.
2. **Kit seed text replicated per-repo, then the target moved out from under it** —
   one template fix retires the INC-29/33/39/56 class at the next upgrade wave.
3. **fm canonical surfaces lack an already-satisfied-ask expiry sweep** —
   INC-01/03/04/05/06/14 are one checker extension (`check_owner_queue.py` +
   triage re-verdict).
4. **Hand-carried cross-repo assertions** (seat briefs, registry rows, pin claims) age
   within hours at fleet velocity — machine-derived registries (INC-07/08/40/42/62)
   are the structural fix the lanes themselves keep proposing.

## 12 · Honest gaps

- **Snapshot basis, not live**: every item is pinned to the review SHAs above (plus a
  handful of live re-checks dated 2026-07-14 inline: INC-06 required-check probe,
  INC-07 idle status fetch, INC-58 full-clone git ground truth). Fleet velocity means
  some items may already be fixed by the time this is read — verify a row's citation
  against HEAD before acting on it, and strike-and-cite rather than delete.
- **Some corroborations rest on lane self-reports**: INC-08 (seat-brief corrections),
  INC-61 (foreign-trigger duplicate-fire risk), and INC-62 (trigger attribution) cite
  outbox/heartbeat claims that were not independently re-verified against the live
  trigger registry during this review — the fix-now dispositions include that
  verification step deliberately.
- **Line numbers are as-recorded in the per-repo notes** at the review pins; they
  drift with edits. The @SHA qualifiers are the durable anchors.
- **Draft-only inheritance**: items marked "clone-verified this pass" (INC-10, INC-11,
  INC-33, INC-45, INC-46, INC-49) were re-checked against the review clones; a small
  number of LOW items (e.g. INC-27's per-repo count lags) rest on the notes alone.
- **No fix has shipped from this review** — this ledger records findings and routes
  them; dispositions are recommendations for fm / the lanes / the owner, not completed
  work.
- **Where the raw residue lives**: the ~120 raw findings this ledger deduplicates from
  are in the per-repo notes at `fleet-review/notes/<repo>.md` (the declared truth
  source); note findings reviewed but held below the ledger bar are listed in §10a, so a
  reader can distinguish dedup from drop.
