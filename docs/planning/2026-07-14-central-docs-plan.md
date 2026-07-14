# Fleet docs centralization plan

> **Status:** `plan`
>
> Generated 2026-07-14 by the fleet review (owner directive); fact-checked and revised
> same day. The actionable plan to
> make **menno420/fleet-manager** (fm) the single source of truth for fleet docs.
> Collated from all 19 per-repo deep-review notes (`fleet-review/notes/*.md`); pinned
> review SHAs: superbot `bbc524e4`, fleet-manager `ff6361a`/`eff4c7d`, substrate-kit
> `727f5db`, superbot-next `50814bb` (corrected 2026-07-14 — the draft's `abe80c0` pin
> did not resolve to any object in the review clone; `50814bb` is the verified review
> HEAD); other repos at the per-repo HEADs cited in each
> note. Standing owner context: **Option A custodian-primary** (2026-07-11, superbot
> `docs/planning/fleet-centralization-plan-2026-07-11.md` §1) already names fm the
> records custodian; fm's design rule is "program-facing truth → superbot;
> manager-internal memory → fm" and its posture is anti-copy (fm CONSTITUTION,
> Program-law section: "cite PL-IDs — never copy ruling bodies").

---

## 1. Scope and shape

The 19 per-repo candidate lists deduplicate to **five classes and 47 enumerated items**
(§2: 15 A + 4 B + 14 C + 9 D + 5 E; fleet-review collation, 2026-07-14). Each item gets
one of four actions:

- **MOVE** — fm becomes the authored master; the source keeps a permanent pointer /
  supersession stub.
- **MIRROR** — fm holds a generated or provenance-stamped copy pinned to a source SHA.
- **INDEX** — fm holds pointers only; the bytes stay where they are written.
- **CONFIRM** — fm is already canonical; state it and close the contradicting docs.

The five biggest duplication clusters driving the plan:

1. **Fleet coordination protocol** — nominated by 12+ repos. Every fleet repo carries a
   diverging `control/README.md` "local copy" whose declared canonical is a superbot
   *planning* doc (`docs/planning/fleet-coordination-protocol-2026-07-09.md`), while the
   machine grammar lives in substrate-kit `src/engine/grammar.py` and the lane registry
   in fm `scripts/gen_roster.py`. websites note, inconsistency 8: "Protocol canon split
   across three repos … nothing says which wins."
2. **Capability/walls ledger** — flagged by 13+ repos. Every kit adopter's
   `docs/CAPABILITIES.md` header points at fm `docs/capabilities.md` — a **MOVED stub
   since 2026-07-12** (fm I-44 fold into uppercase `docs/CAPABILITIES.md`). Sync is
   manual and lags: fm's aggregate holds **zero sim-lab entries** (grep verified @
   fm `ff6361a`) while sim-lab's PLATFORM-LIMITS is among the fleet's richest ledgers.
3. **Gen-1 retro question core (IDs A–F)** — per-repo `docs/retro/QUESTIONS.md` copies
   (venture-lab, gba-homebrew, pokemon-mod-lab, all 3 codetool labs, trading-strategy).
4. **Owner working profile** — superbot `docs/owner/maintainer-working-profile.md`
   canonical vs a kit-planted digest in every repo ("drift by construction across ~19
   repos" — fm note; trading's copy carries an internal privacy-note contradiction).
5. **Model-attribution telemetry** — per-repo `telemetry/model-usage.jsonl` + per-card
   `📊 Model:` lines feed fm `docs/findings/model-matrix-2026-07.md` only by ad-hoc
   sweep; games and mineverse outcome fields are all-null (games/mineverse notes).

**Do-NOT-move confirmations** (to preempt wrong centralization):

- **Program law** (PL-001…PL-011) stays in substrate-kit `docs/program/rulings.md` —
  D-0002/KF-6, CI-enforced by `check_program_law.py`; venture-lab names this the model
  pattern to replicate. fm indexes by PL-ID only.
- **Kit bench/telemetry raw dataset** stays kit-lab (PL-004 program-dataset ownership).
- **EAP program-narrative corpus** stays in superbot `docs/eap/` (fm README design rule
  + fm evidence-index header) — the gap is indexing, not the home (§2 D1).
- **Sim-lab / idea-engine outboxes** stay the canonical proposal/verdict ledgers — fm
  holds an index, never a second copy of record (sim-lab note, candidate 1 risk line).

**Self-application** — this plan applies its own dual-write guard to itself and its
predecessors. Landing home: **fm `docs/planning/`** (the plan's thesis is that fleet
docs live in fm; it does not stay in scratchpad). When it lands, the superseded superbot
centralization docs get the same-PR supersession treatment the plan mandates for every
losing copy: superbot `docs/planning/fleet-centralization-plan-2026-07-11.md` and
`fleet-review-2026-07-11.md` stay as **frozen provenance seeds** (they are the recorded
provenance of fm's mission and triage register — fm note, candidate 2), each gaining a
supersession banner pointing here, and fm indexes both from its evidence-index/provenance
section. The banner routes via inbox ORDER (superbot is outside fm write scope) — Slice 0
item 9.

---

## 2. Per-item moves, by class

### Class A — Doctrine (protocols, playbooks, operating rules, prompts)

| # | Item | Current home(s) — exact source paths | Action → fm home | Nominated by |
|---|------|--------------------------------------|------------------|--------------|
| A1 | Fleet coordination protocol (one-writer bus; ORDER/status/claim ritual) | superbot `docs/planning/fleet-coordination-protocol-2026-07-09.md` (declared canonical) + ~14 diverging `control/README.md` copies; grammar in substrate-kit `src/engine/grammar.py` | **MOVE prose spec** → fm `docs/control-protocol.md`, version-stamped; grammar constants stay kit-master; repo copies become pointer + local-delta appendix (idea-engine's copy has load-bearing local doctrine — the claim ritual — that naive centralization would lose) | 12+ repos |
| A2 | Trigger-health per-wake spec (R26 / ORDER 020) | superbot `docs/owner/trigger-health-order-2026-07-12.md` — cited "canonical spec" by fm's roster header + playbook R26, while checker (`check_trigger_health.py`), data (`telemetry/triggers-snapshot.json`), and record (roster health section) all live in fm | **MOVE** → fm `docs/trigger-health-spec.md`; superbot keeps a supersession stub (the fleet-manifest #1974 pattern) | fm, superbot |
| A3 | Program law + program collaboration-model + agent-decision-authority | substrate-kit `docs/program/` | **INDEX only** → fm per-PL-ID link table (`docs/program-law-index.md`). Do NOT move — CI-enforced anti-copy (D-0002); kit note flags "two fleet-canonical repos is a standing collision — needs one explicit ruling"; recommendation (decide-and-flag): keep kit home | substrate-kit |
| A4 | Universal session ender | superbot `docs/owner/universal-session-ender-v3.4.md` — its own header (L19-21) names the fm prompt registry the canonicalization target; fm's final ORDER already orders v3.5 into the registry | **MOVE** → fm `docs/prompts/v3/`; superbot copy badged historical | superbot |
| A5 | Dated dispatch/order prompt kits (fleet-rearm, night-orders, direct-orders, dispatch-prompts, founding prompts, 8-seat structure — 6 files) | superbot `docs/owner/*.md` | **MIRROR** → fm `projects/<seat>/` + `docs/prompts/`; superbot copies remain as dated historical provenance | superbot |
| A6 | Owner shorthand vocabulary (review/status/ship/groom) | superbot `docs/owner/fleet-vocab.md` (hub-only) | **MIRROR** → fm docs + kit template so every seat resolves the words identically | superbot |
| A7 | Gen-1 retro question core (IDs A–F) | per-repo `docs/retro/QUESTIONS.md` copies | **MOVE** → one canonical register at fm `docs/retro/QUESTIONS.md` (or kit template); lanes keep only their addendum (venture §G, gba game addendum) + frozen historical copies (answers reference the IDs) | venture, gba, pokemon, 3× codetool, trading |
| A8 | Classifier/merge-authority doctrine (denial-shape taxonomy; "relayed authorization is never genuine" / permission laundering; enabler+required-check recipe; park-green; auto-merge pending-window recipe) | venture-lab `docs/PLATFORM-LIMITS.md` (verbatim denials) · product-forge `docs/PLATFORM-LIMITS.md` (pending-window recipe proven on 6 PRs; seat-variance ledger) · fm `docs/retro/coordinator-seat-2026-07-11.md` (4 denial shapes) · superbot-next `control/outbox.md` (8 denial classes in one night) · games gen2-feedback doc | **MIRROR** → fm playbook merge-authority chapter + venue-tagged CAPABILITIES entries; lane ledgers remain the append/evidence surface | 6+ repos |
| A9 | Codex review-authenticity doctrine (3 verified fabrications + VERDICT 016 authenticity gate: 270-cell sweep, 3/3 caught at 0/24 false alarms) | sim-lab `control/outbox.md` V016 block + incident lines — "program-wide security doctrine that shouldn't live only inside one repo's append-only outbox"; fm already ordered fleet-wide adoption (fm inbox L1095) | **MIRROR** → fm `docs/findings/`; also reconcile the OA-002 fork (fm says Codex resolved, sim-lab says open — integration-enabled vs quota-capped conflation; sim-lab inconsistency 4) | sim-lab, fm, superbot-next |
| A10 | Outbox rollover/archival convention for append-only control files | idea-engine ASK 004 (unanswered since 2026-07-13T20:05Z; outbox 459KB, past the 256KB Read wall) + sim-lab (outbox ~875KB at re-check 2026-07-14 — 895,885 bytes; the note's 834KB figure was already stale, the file is still growing) | **MOVE** → fm `docs/conventions/outbox-rollover.md` + kit threshold checker; mandate pointer stubs so `@SHA` citations into rolled files survive | idea-engine, sim-lab |
| A11 | Session-card grammar + model-attribution doctrine (📊 Model line; superbot Q-0262 / fm ORDER 012) | kit grammar is master; doctrine restated per repo + relayed as N inbox ORDERs | **INDEX** — kit-owned body; fm runs the enforcement sweep and the matrix aggregation (D4) | idea-engine, pokemon, idle |
| A12 | Wake-chain/routines doctrine (fresh-session cron measured 0-for-2 vs self-bound 100%; tombstone-less deletions; manual-fire health trap; wedge signature) **+ websites' non-wake continuous-mode doctrine** — `docs/retro/continuous-mode-lessons-2026-07-11.md`: build-and-hold under merge freeze, heartbeat-inheritance re-verification, guard-quality patterns (explicitly nominated for the fm playbook, websites candidate 4) | per-repo `docs/ROUTINES.md` (kit render) + kit trigger-forensics report + superbot-next q0265 retro + websites continuous-mode retro | **MIRROR** → fm trigger-health doctrine annex (superbot-next's retro itself recommends "the fm-side periodic fleet trigger audit") + fm playbook chapter for the non-wake lessons | games, kit, websites, next, gba |
| A13 | Claim convention (one-file-per-claim; superbot's measured ~98%→0% conflict sim) | kit template (canonical) + legacy root `claims/` dirs still `binding`-labeled in pokemon, gba, venture | **CONFIRM** kit as sole body; fm ORDERs the legacy-dir retirements; superbot keeps the measurement provenance (`tools/sim/claim_layout_sim.py`) | pokemon, gba, venture |
| A14 | fm playbook R-rules as citable register (R1–R27) | fm `docs/playbook.md`; R-rule bodies restated across pokemon `control/README.md`, `docs/conventions.md`, `docs/PLATFORM-LIMITS.md` (R1/R2/R5/R8/R9/R10/R12/R19/R21/R22) and other seed copies | **CONFIRM fm master + formalize R-IDs** analogous to the PL register; repos cite R-IDs, never restate bodies (pokemon candidate 4's explicit ask) | pokemon |
| A15 | Worker-dispatch standing brief lines + lifeboat convention (never park on timers/monitors; kit stubs → scratchpad; `claude/*` prefix) | websites `control/outbox.md` PROPOSAL 2026-07-13T11:29Z + websites fleet-cleanup-audit suggestion 1 | **MIRROR** → fm `templates/` dispatch briefs (feeds the v3 prompt registry) | websites |

### Class B — Capability ledgers (walls / verified platform findings)

| # | Item | Current home(s) — exact source paths | Action |
|---|------|--------------------------------------|--------|
| B1 | Fleet capability master aggregate | fm `docs/CAPABILITIES.md` § fleet manifest (post-I-44 single ledger) | **CONFIRM** as fleet master aggregate; rule in §3-B |
| B2 | Kit seed-fence pointer — every adopter's header targets the dead lowercase `docs/capabilities.md` stub | substrate-kit CAPABILITIES template (seed fence) + kit's own `docs/CAPABILITIES.md:7-9` (stale both directions — additionally claims kit sessions "cannot read fleet-manager directly", superseded 2026-07-09) | **One kit-template fix** (route via kit-lab ORDER; the fence is kit-owned) heals ~14 adopters at next upgrade; flagged by 13+ repos. **Status 2026-07-14T06:50Z: EXECUTED kit-side** — ordered via kit inbox ORDER 020 sub-item (e) (kit PR #361, MERGED 04:12:59Z); fix re-verified live at kit main `2a2d92b`: `src/engine/templates/CAPABILITIES.md.tmpl` header now targets `menno420/fleet-manager` → `docs/CAPABILITIES.md` (uppercase) and `seatdigest.py` has **zero** lowercase `docs/capabilities` hits. Adopter headers heal at their next kit upgrade (websites @ `868626c` + sim-lab @ `201cb01` still render the lowercase pointer — expected lag, not drift) |
| B3 | Fleet-generic findings living only lane-side | substrate-kit (send_later no-tombstone drops; fresh-cron 0-for-2; worktree-per-worker) · venture-lab `docs/PLATFORM-LIMITS.md` (verbatim classifier denials 07-10/11/13; branch-delete 403) · sim-lab PLATFORM-LIMITS (cross-session-binding org-wall verbatim; SQUASH race; tag 403; api.github wall) · 3× codetool-lab KNOWN-WALLS tables ("the fleet's best exact-error-text wall ledger" — fable5 note) · gba dated platform-issue notes (Opus-configured/Fable-delivered mismatch; OA-5 add_repo denials) · product-forge (pending-window recipe; empty-check_run wall) · trading, idle, idea-engine, mineverse appends | **MIRROR** into the fm master with per-finding **venue + seat attribution + source SHA**; dedup against fm's existing holdings; 12+ repos |
| B4 | Intra-lane ledger splits: `docs/PLATFORM-LIMITS.md` vs `docs/CAPABILITIES.md` (venture, idle, pokemon; gba ×3 incl. a third lowercase seed copy). Seat-digest walls render "(no walls recorded)" while the real walls sit in the un-fenced file (sim-lab inconsistency 5, venture inconsistency 4 — the exact surface fm's seat-prompt regen consumes) | per-repo | Lane-side folds ordered via fm inbox ORDERs; venue-tag entries so the digest stops under-reporting; the seat-digest fence becomes the single machine extraction surface fm consumes. **Status 2026-07-14T06:50Z: dispatched 0530Z (dispatch-log), execution SPLIT** — venture-lab **DONE** (fence + venue-tagged append log live at `68d57bb`; `PLATFORM-LIMITS.md` correctly demoted to a pointer/evidence appendix); websites ORDER 028 + sim-lab ORDER 007 **delivered but still `status: new`** at lane HEADs `868626c`/`201cb01` — capability-seed fence still ABSENT in both (re-probed raw); pokemon-mod-lab SKIP-satisfied at `759dee4` (fence present, digest healthy). Dispatched ≠ done: the row closes when the two remaining lanes execute their ORDERs |

### Class C — Rosters / indexes / registries

| # | Item | Action → fm home |
|---|------|------------------|
| C1 | Generated roster + evidence index + triggers snapshot (fm `docs/roster.md`, `docs/evidence-index.md`, `telemetry/triggers-snapshot.json`) | **CONFIRM** — the measured SSOT (hand manifest superseded 2026-07-11: ~33.5h stale, 9/10 rows wrong). Fix fm's own front door: `README.md@ff6361a` L6-9 still points fleet state at the superseded superbot manifest (fm inconsistency 1) |
| C2 | Owner queue (fm `docs/owner-queue.md` + candidate feed + checker) | **CONFIRM** + staleness sweep — dead/decided items found this review: OQ-PLUGIN-SEED-WORD (asks for a seed delivered 2026-07-12 — **high**), OQ-MINEVERSE-PYTEST-REQUIRED-CHECK (resolved 07-11), C#20 codex-YAML (resolved by superbot #1995), OQ-TRADING-KILLSIG (lane already ratified + shipped, trading PR #109/#118), sim-lab OA-002 state fork, and the **fable5 lane's undecided archive/relaunch limbo** (repo says "ready for archive + fresh session"; nothing has decided which, for 4 days — fable5 candidate 7; route the disposition to the fm roster/dispatch-log). Lane ⚑/OA blocks stay the write surface; fm indexes per-repo ask files by stable OQ-slug (websites candidate 8) with an expiry sweep fed by lane heartbeats; and fm's owner-attention roll-up **indexes venture's generated `docs/publishing/OWNER-QUEUE.md` headline counts + top decisions by pointer** (19 D / 33 seq / 185 clicks at review — venture candidate 2: index the generated counts, never re-derive them) |
| C3 | Machine-readable lane registry | **NEW** fm `registry/lanes.json` emitted by `scripts/gen_roster.py` — today the lane set is a python constant consumers repoint at (websites #102), and stale kit-rendered docs still derive sections from the dead manifest (idea-engine inconsistency 1: 4 docs) |
| C4 | Kit-adoption/version table (repo → pinned kit_version → tree version → current release) | **MIRROR (generated from trees, not heartbeats)** → fm `registry/kit-versions.md`; kit `docs/adopters.md` stays sole-writer kit-lab. Fixes roster kit blind spots: fm's own row "—"; superbot 1.0.0; plugin-hello 1.13.0 silent drift; idle heartbeat v1.7.1 vs tree v1.15.0 (an 8-release courtesy-line lag) |
| C5 | Fleet-roster-for-scan (kit `docs/fleet-repos.txt`) vs fm generated roster | **Unify to one source** — "two rosters/registries with different writers = drift by construction" (kit candidate 2); fm-writes-kit or kit-reads-fm; needs one kit ruling (Phase 5) |
| C6 | Q-number owner-decision register | **INDEX** → fm `docs/q-index.md` — superbot `docs/owner/maintainer-question-router.md` (Q-0001…Q-0274, ~9.9k lines) stays canonical; fm builds a repo-qualified Q→link table. Fixes the live mislabel class (fm surfaces "Q-0266" where the verbatim router entry is Q-0262.7 — pokemon inconsistency 7) and superbot-next candidate 3's ask to graduate cross-repo-cited Q-numbers (Q-0265/Q-0269/Q-0270/Q-0240) into PL entries |
| C7 | Prompt-artifact manifest | **NEW** fm `projects/manifest.json` (machine-readable) — websites `app/prompts.py` hand-pins **29** fm registry paths (9 seats × 3 SEAT_FILES + 1 FLEET_WIDE + 1 HISTORICAL at review; the note's count of 26 predates the `curious-research` seat added to `app/roster.py` 2026-07-13, commit `ff5b7c8` — the growth itself proves the hand-pin rots) because "raw host cannot list" (websites candidate 5) |
| C8 | PROPOSAL↔VERDICT crosswalk + cross-repo request/ask register | **MIRROR (generated)** → fm `docs/pipeline/` — pipeline ledger (proposal → simreq-NNN → verdict → routed ORDER → landing PR) incl. the hand-kept +2/+11 offset map that already broke once (sim-lab candidate 4); a per-ASK/SIM-REQUEST status register (idea-engine ASKs 001–004 all unanswered; superbot-next's SBW casino SIM-REQUEST sat unanswered while its owner seat was DARK); an upstream kit-asks tracker (mineverse's 3 outbox kit-asks, idle KIT-001, games KIT-ASK — "nothing tracks the other three", mineverse candidate 3); and the fleet Q/SIM number-assignment registry (idle candidate 4: three items parked on "needs fleet number — manager to assign") |
| C9 | Trigger/wake registry + dispositions | **CONFIRM** fm `telemetry/triggers-snapshot.json` + roster health section as index-of-record; lanes never restate `trig_` ids in prose (venture FOREIGN-trigger flag; trading superseded-id lesson; idle's DELETED trigger still listed ARMED in fm `projects/README.md` — idle inconsistency 3, **high**). Time-boxed: route the **2026-07-17 duplicate grading-fire disposition** (trading cron 09:05Z vs foreign send_later 09:00Z — double-write risk) through the owner queue before Friday |
| C10 | Plugin-pin + cross-repo contract-pin index | **INDEX** → fm `registry/pins.md` — plugin repos → manifest hash → host `plugins.lock.json` state (the 06023075→ff75b9eb drift was found by hand — plugin-hello candidate 4), generalized per idle candidate 7 to all cross-repo pins (superbot-next pin `9634e81` in idle CI; plugin contract @ `d3dba9b`; SIM packet pins). Record the canonical-template ruling (plugin-hello canonical; superbot-next `examples/` copy frozen or deleted) + a passive-repo allowlist row (plugin-hello: no heartbeat by design) |
| C11 | Fleet grounding (Q-0274) + product catalog | **INDEX now, MOVE later** — both owner-directed to superbot homes; superbot note argues for fm ("the manager should own what it reviews"; the sellable-catalog belongs beside owner-queue — venture candidate 4 wants the 1-live/10-ready/2-gated product roster in one place). A move is a router-Q proposal, not a unilateral act |
| C12 | Hub-side duplicate tooling (superbot `scripts/fleet_status.py` + `docs/fleet-reading-path.md`) | **Retire-or-consume** — fleet_status re-implements roster aggregation client-side; the reading-path carries the false "superbot has no heartbeat file" row (superbot inconsistency 1); kit-graduate the pattern per the doc's own header |
| C13 | Seat-digest extraction contract (fence-prefix byte-compare) | **CONFIRM fm as registered consumer** — document the consumer half centrally (contract exists producer-side in every kit repo; fm's regen tool is the named consumer); index which repos expose which fences |
| C14 | Verdict/grading vocabulary lexicon | **INDEX (small)** → fm `docs/lexicon/verdict-grammars.md` — trading candidate 7: three disjoint verdict grammars (sim-lab rulings; trading KEEP/KILL/KILL-SIG; idea-engine probe outcomes) with no single map; fm points at each repo's canonical grammar doc |

### Class D — EAP records (program narrative, retros, feedback, telemetry, audits)

| # | Item | Action |
|---|------|--------|
| D1 | EAP program-narrative corpus (superbot `docs/eap/`, 27 files) | **INDEX — do not move.** Close the measured gap: fm evidence-index names superbot `docs/eap` the "Program-narrative home" but contains **zero row-level links into it** (grep 0 @ fm `eff4c7d` — superbot inconsistency 5); generator change, one row per document |
| D2 | Gen-2 blueprint feedback docs — written explicitly "for the manager to collect" | **MIRROR** → fm `docs/findings/` / `docs/proposals/`: games ×2 (`gen2-feedback-exploration.md`, `retro/gen2-feedback-mining…`), trading GEN2-FEEDBACK (blueprint absorbed items 1–4,7; 5/6/8 not yet), sonnet5 (4 NEW items), fable5 (10 items **incl. recorded disagreements** with the blueprint that must not be lost at its next revision), opus4.8 (7 items), kit prompt-hardening input (already ported, fm ORDER 014). **Plus the paired gen-2 custom-instructions proposals** (restored — dropped in the draft): sonnet5 `docs/succession/PROPOSED-CUSTOM-INSTRUCTIONS.md` — "a full paste-ready gen-2 instruction rewrite that no live seat now points at" (seat retired; heartbeat-before-work, walking skeleton, self-merge grant wording are template material for the fm prompt registry, sonnet5 candidate 5) — and fable5 `docs/succession/custom-instructions-proposal.md` (KEEP/DROP/ADD vs the fm gen2-blueprint, fable5 candidate 3). Both sit in archive-bound repos → also on the D5 mirror-before-archive list |
| D3 | Gen-1 retro corpus + winddown-audit errata **+ superbot-next's rebuild evidence corpus** | **INDEX** with pinned SHAs (largely exists via evidence-index "(+4 more)" rows — make them per-file) + register errata beside entries: opus4.8's "main tip `c96318c`" claim falsified by superbot's winddown audit (real tip `80f6cd1`), plus the citation misattribution — corrections live only in superbot docs today (opus4.8 candidate 4). Extend the same per-file index rows to superbot-next's nominated rebuild evidence (next candidate 5): `docs/status/rebuild-completion-report…` + orchestration retrospective, `docs/retro/self-review-2026-07-09.md` + `project-review-2026-07-09.md`, `docs/review/program-review-2026-07-12.md`, `curation-report-2026-07-13.md`, and the 213-card `.sessions/` corpus (path@SHA + one-line summary; pointers only, never copy) |
| D4 | Model-attribution telemetry **+ the kit allocation ladder** | **MIRROR (generated)** → fm model-matrix aggregation naming per-repo `telemetry/model-usage.jsonl` + card `📊 Model:` lines as sources (superbot-next candidate 7: cards stay canonical, fm aggregates by pointer); note games/mineverse outcome fields all-null (games wishlist: backfill by the claim-release session). The which-model-gets-which-seat **allocation ladder** (kit `telemetry/allocation-ladder.md`) stays kit-lab per PL-004 program-dataset ownership; fm **indexes ladder + model-matrix as one allocation view** (kit candidate 6 — the draft covered only the telemetry half) |
| D5 | Archive-rescue records (gated on owner E#44/E#45) | **MIRROR-BEFORE-ARCHIVE** — the one class where copying beats indexing, because the sources are about to freeze: product-forge self-review + owner-rulings timeline (chat-only owner merge grants 21:07Z/22:08Z exist durably ONLY there) + final-state pointer + 2 unratified PROPOSALs; **the already-ORDERed forge product moves are also archive-gate-blocking** — fm **ORDER 023/P1-1** (`products/games-web/` + `data/schema/game-state.schema.json` v1.0.1 + tests → websites Fleet Arcade or superbot-games per the ORDER's decision criterion; the repo's only running product) and **P1-2** (`products/games-web/docs/phase2-data-api-proposal.md` follows it — a cross-repo request *to* the superbot lane that, left in a DARK repo, is guaranteed never answered; forge candidates 5–6). The code move itself executes per the ORDER, outside this docs plan's scope — listed here because the archive click must not fire before it; sonnet5 differential-oracle writeup + release decision + `PROPOSED-CUSTOM-INSTRUCTIONS.md` (D2) — **fm ORDER P1-4 status: NEEDS RE-VERIFICATION, not "unexecuted"**: the draft's evidence ("zero cfgdiff/differential docs at kit HEAD") is **falsified** — substrate-kit @ `727f5db` git-tracks `docs/reports/2026-07-09-cfgdiff-differential-testing-method.md` + `docs/reports/2026-07-09-cfgdiff-v0.1.1-release-decision.md`, both referenced from `docs/operations/README.md` (fact-check 2026-07-14); the open question is only whether P1-4 meant porting a *different* sonnet5 succession writeup — check the ORDER text against those two files before treating anything as archive-blocking; opus4.8 KNOWN-WALLS + release recipe; fable5 PLATFORM-LIMITS + `custom-instructions-proposal.md` (D2) + open tag/release ⚑ asks (stale-recipe trap: fable5 ROADMAP still carries the corrected-away "route closed" verdict its own PR #14 fixed only in PLATFORM-LIMITS); kit `docs/succession/` superbot-coordinator pack + archived foreign heartbeat (kit candidate 5) |
| D6 | Fleet-sweep audit artifacts | **Disposition then INDEX** in an fm `docs/audits/` register — websites' fleet-cleanup audit is committed; pokemon's landed as PR #68; **plugin-hello's sits on an unmergeable-by-convention open PR #1**; sonnet5's sits on an unmerged branch. Two of four can never land without a sweep decision. **Home-split flag (websites candidate 6):** fleet audits could equally go to superbot `docs/eap/` under fm's own "program-facing truth → superbot" design rule — "that split itself needs one answer"; this plan picks fm `docs/audits/` as a decide-and-flag call (§7 item 7), not silently |
| D7 | Cross-lane routing records (venture WEBSITE-IDEA markers "for the manager to route", 12+ across 3 batches; SIM-REQUEST round-trips; idea-engine `ideas/fleet/`) | **INDEX** — routing ledger with marked→routed→consumed states; link-index only (superbot Q-0264.8 reference-don't-migrate) |
| D8 | Cross-repo product specs + fleet-generic research | **INDEX** — mineverse `docs/design/minigame-section-spec-2026-07-13.md` (a 4-repo-pinned SuperBot-2.0 spec living in one lane repo) stays author-canonical, fm indexes; venture `docs/research/monetization-jurisdictions/` mirror-or-move with stub (fleet-generic revenue knowledge) |
| D9 | fm session-card lesson corpus | **Internal distillation backlog** — ~129 ⟲ reviews / ~140 💡 ideas in fm `.sessions/` hold rules that never graduated (ack-latency metric, generated succession handoffs, worktree-enforcement preamble); periodic distillation pass into playbook/kit (fm note candidate 6) |

### Class E — Templates / environment

| # | Item | Action |
|---|------|--------|
| E1 | `setup-universal.sh` | **CONFIRM** fm `environments/templates/` canonical + adopter checksum/sync-stamp index (fable5's copy is byte-identical today — verified by diff — but silently forks the day fm updates); upstream sonnet5's tested deltas (always-exit-0 contract, pyproject glob) and opus4.8's defensive contract |
| E2 | Owner working profile | **One canonical** = superbot `docs/owner/maintainer-working-profile.md`; kit template becomes pointer + per-repo delta; fm `docs/owner-profile.md` regenerated-from. Also fixes trading's privacy-note contradiction at one home instead of N |
| E3 | Release-via-Actions recipe + generic `release.yml` | **MIRROR** → fm `docs/playbooks/release-via-actions.md` + workflow template — proven first-try twice (opus4.8 Actions runs 29035224581 / 29038899218), cited fleet-wide (fm owner-queue: "the route opus4.8 used"); the seat-dependence rider (fable5 PR #14) must travel with it |
| E4 | Gen-2 blueprint / conventions seed copies | **CONFIRM** fm `docs/gen2-blueprint.md` canonical; adopter copies get diverged/render stamps + delta lists (gba's copy claims "No CI workflows exist at seed" beside 4 live workflows; venture's conventions still grant a self-merge the classifier verifiably denies — venture inconsistency 1, HIGH) |
| E5 | Registry/seat-brief facts (required CI contexts, enabler presence, kit version, trigger state) | **Derive, don't transcribe** — mineverse refuted its hand-carried brief 3× in one day ("re-verify landing paths at boot — do not trust the brief"); fm regenerates briefs from adopters' trees + rules-probe logs; roster gains a heartbeat-age vs evidence-age split so frozen-archive heartbeats (games DARK ~37h while shipping #61–#113 — games inconsistency 1, HIGH; idle's blessed frozen archive) stop mis-rating live seats |

---

## 3. Proposed fm homes — consolidated target map

```
fleet-manager/
├── README.md                        C1 fix (custodian claim — currently contradicts Option A)
├── docs/
│   ├── roster.md                    C1 confirm (generated, 2h cron) + E5 evidence-age split
│   ├── evidence-index.md            D1/D2/D3 extend (eap rows, kit reports, feedback, errata)
│   ├── owner-queue.md               C2 confirm + sweep + OQ-slug index of lane ask-files
│   ├── CAPABILITIES.md              B1/B3 extend (venue-tagged mirrored findings + source SHAs)
│   ├── control-protocol.md          A1 new (MOVED-IN, version-stamped)
│   ├── trigger-health-spec.md       A2 new (MOVED-IN) + A12 wake-chain annex
│   ├── program-law-index.md         A3 new (index of kit PL-IDs)
│   ├── q-index.md                   C6 new (repo-qualified Q→link table)
│   ├── prompts/v3/                  A4/A5 extend (+ ender v3.5, dispatch kits, A15 brief lines)
│   ├── retro/QUESTIONS.md           A7 new canonical core
│   ├── conventions/outbox-rollover.md   A10 new (answers idea-engine ASK 004)
│   ├── playbooks/release-via-actions.md E3 new
│   ├── playbook.md                  A8/A9/A14 extend (merge-authority, review-authenticity,
│   │                                R-register formalization: cite R-IDs, never copy bodies)
│   ├── findings/                    B3/D2/D4/A9 extend
│   ├── succession/                  D5 extend (archive-rescue mirrors, kit coordinator pack)
│   ├── audits/                      D6 new register (+ private-content rule for pokemon-mod-lab)
│   ├── pipeline/                    C8 new: proposal-verdict.md + ask-register.md +
│   │                                number-registry.md (Q/SIM assignment) + kit-asks.md
│   └── lexicon/verdict-grammars.md  C14 new (pointer page)
├── registry/lanes.json              C3 new (generated by gen_roster.py)
├── registry/kit-versions.md         C4 new (generated from trees)
├── registry/pins.md                 C10 new (plugin + cross-repo contract pins, passive allowlist)
├── projects/manifest.json           C7 new (generated prompt-artifact manifest)
├── projects/<seat>/                 A5 extend
├── environments/templates/          E1 confirm + checksum index
└── telemetry/triggers-snapshot.json C9 confirm (index-of-record)
```

---

## 4. Source-of-truth rule per class

- **A — Doctrine: fm is the authored MASTER.** Version-stamped docs; repos carry pointer
  + local-delta appendix only. **Two carve-outs are kit-master:** program law (D-0002,
  CI-enforced) and control-bus/card **grammar constants** (substrate-kit
  `src/engine/grammar.py`) — fm holds an index, never a copy. The discipline to
  replicate is venture-lab's anti-candidate: "cite PL-IDs, never copy ruling bodies — a
  local copy is drift by construction."
- **B — Capability ledgers: split-master.** Each repo's `docs/CAPABILITIES.md` append
  log is the master **write surface for its own venue** (the discovery rule requires
  same-session local appends; walls are venue-scoped facts — "a flat CAN/CANNOT ledger
  is wrong somewhere by construction", mineverse note). fm's fleet manifest is the
  master **aggregate**: every mirrored finding carries venue + seat + source SHA. Repos
  embed the fleet section by kit-owned fence/pointer, never by authored copy.
- **C — Rosters/indexes: fm-master where GENERATED from ground truth** (roster,
  evidence index, lanes.json, kit-version table, pins, triggers snapshot, owner queue,
  pipeline ledgers); **fm index-of-pointers where the write surface is elsewhere**
  (Q register → superbot router; adopter registry → kit-lab; verdict/proposal ledgers →
  sim-lab / idea-engine outboxes; lane ⚑/OA blocks → lanes). Iron rule from the
  manifest lesson (9/10 rows wrong at supersession): **no second hand-maintained copy
  of any fact, ever** — a copy is either generated or a pointer.
- **D — EAP records: fm index-of-pointers with pinned SHAs**; corpora stay where they
  were lived (superbot `docs/eap/`, lane retros). **Exception:** archive-bound repos
  get provenance-stamped mirrors *before* the archive click freezes them (D5).
- **E — Templates: one authored master per ownership line** (fm: environments,
  blueprint, prompts, briefs; kit: planted-doc templates; superbot: owner profile).
  Copies carry sync-stamps + checksums and a drift checker compares. Seat-brief *facts*
  are always derived from trees/probe logs, never transcribed.

---

## 5. Migration order

### Slice 0 — first buildable slice (one fm session, fm-write-scope only, ~1 day)

All inside fm's own write authority; zero cross-repo pushes (the one superbot stub
routes via inbox ORDER). Every item is reversible and closes a measured drift:

1. **Fix fm's own front door** — README custodian/manifest claim (fm inconsistency 1) +
   current-state "In flight" sweep (#86/#178 listed in-flight though merged) +
   seat-digest step-3 lowercase pointer (fm inconsistency 2).
2. **evidence-index generator: add row classes** — superbot `docs/eap/*` per-file rows
   (closes the 0-links gap), kit `docs/reports/*` fleet evidence, gen2-feedback docs,
   retro errata (D1–D3).
3. **Emit `registry/lanes.json`** from `gen_roster.py` (C3) — retires the
   constant-in-a-script registry consumers repoint at and the dead-manifest derivations.
4. **Move in the trigger-health spec** (A2) + inbox ORDER to superbot for the stub.
5. **Seed `docs/q-index.md`** repo-qualified (C6) — immediately fixes the
   Q-0266/Q-0262.7 mislabel class.
6. **Owner-queue staleness sweep** (C2: plugin-seed, mineverse-pytest, C#20, KILL-SIG,
   OA-002 reconciliation) + fleet-triage re-verdict for opus4.8 (fleet-triage says
   ARCHIVE, consolidation plan says KEEP — two fm docs disagree, "the exact class fm
   exists to prevent") + **fable5 archive/relaunch disposition** (the lane has said
   "ready for archive + fresh session" for 4 days with no decision either way —
   record one in the fm roster/dispatch-log, fable5 candidate 7).
7. **Route the 2026-07-17 duplicate grading-fire disposition** into the owner queue
   (C9 — time-boxed: before Friday).
8. **Answer idea-engine ASKs 001–004** (or explicitly park each with a date) — A10's
   rollover convention answers ASK 004 and unblocks sim-lab's ~875KB outbox.
9. **Land this plan at fm `docs/planning/`** + index the frozen superbot seeds
   (fleet-centralization-plan / fleet-review 2026-07-11) as provenance + inbox ORDER
   to superbot for their supersession banners (§1 Self-application — the plan obeys
   its own same-PR dual-write guard).

### Phase 1 — capability machinery (fm + one kit ORDER)

B2 kit seed-pointer fix (one template change heals ~14 repos at next upgrade); B3
fleet-wide findings sync into the fm master (venue-tagged, source-SHA'd — start with
sim-lab, whose fm entry count is zero); B4 lane-side ledger folds via ORDERs (fixes the
empty seat-digest walls renders); C13 document + start consuming the seat-digest fence.

### Phase 2 — doctrine consolidation (fm + per-lane pointerization ORDERs)

A1 control-protocol v1, version-stamped → pointerize repo copies (batched, local-delta
appendices preserved); A4/A5 prompt registry v3.5 + C7 manifest.json; A7 retro core;
A10 rollover convention shipped; A6 fleet-vocab; A13 legacy-claims retirements; A14
R-register formalization; A15 dispatch-brief lines into templates.

### Phase 3 — pipeline ledgers (fm generators)

C8 proposal↔verdict crosswalk + ASK/SIM-REQUEST register + kit-asks tracker + Q/SIM
number-assignment registry; C4 kit-version table; C10 pin index + passive-repo
allowlist; D4 model-usage aggregation; D7 routing ledger; C14 lexicon page; E5 derived
seat briefs + roster evidence-age split.

### Phase 4 — archive rescue (gated on owner E#44/E#45 — prep now, execute at gate)

D5 mirrors from product-forge + the 3 codetool labs — incl. the gen-2
custom-instructions proposals (sonnet5 + fable5, D2) and **re-verifying kit ORDER
P1-4 against the two cfgdiff reports already tracked at kit `727f5db`** (the draft's
"unexecuted / zero cfgdiff docs" evidence was falsified at fact-check — port only
whatever the ORDER text names that those reports don't cover); confirm forge **ORDER
023/P1-1 + P1-2** (games-web move + phase-2 API proposal) execute before the archive
click, per the ORDER, outside this plan's own scope; D6 stranded-audit dispositions
(plugin-hello PR #1, sonnet5 branch); E1 template-delta upstreaming; E3 release
playbook; fable5 ROADMAP stale-recipe correction before any gen-2/gen-3 boot reads it.

### Phase 5 — owner-gated moves & rulings (router Q / structured choices, decided-and-flagged)

C11 fleet-grounding + product-catalog homes (Q-0274 is owner-directed — propose, don't
move); A3 program-law home ruling (**recommend: keep kit, fm indexes**); C5
roster-source unification; C12 fleet_status.py retire-or-consume; E2 owner-profile
canonicalization (kit template change); the games/idle **frozen-archive vs overwrite
heartbeat doctrine ruling** (prerequisite for trusting `control/status.md` fleet-wide —
two binding texts currently disagree about the same file).

---

## 6. Risks and guards

| Risk | Where it already bit (cited) | Guard |
|------|------------------------------|-------|
| **Mirror staleness** — the fm copy drifts from lane truth | fm owner-queue dead items (plugin-seed HIGH, mineverse-pytest, C#20, KILL-SIG); fm `projects/README.md` idle row citing a trigger DELETED 3 days prior (HIGH); seat briefs refuted 3×/day (mineverse note) | Prefer generated-or-pointer over copy; every mirror carries source SHA + regen date; extend the `check_roster_freshness.py` pattern (freshness bar + kill-switch header) to each new generated artifact; owner-queue expiry sweep fed by lane heartbeats |
| **Dual-write** — two authored homes for one fact | hand manifest vs roster (9/10 rows wrong); fm fleet-triage vs consolidation plan on opus4.8 (opposite verdicts inside fm itself); two owner-profile homes; PLATFORM-LIMITS vs CAPABILITIES splits; OA-002 open/resolved fork | One named writer per file, stated in the doc header; the losing copy gets a supersession banner **in the same PR** (the superbot #1974 pattern); kit `substrate-gate` grammar checks where the surface is kit-owned |
| **Pointer rot** — moved targets strand N pointers | lowercase `docs/capabilities.md` stub cited by 13+ repos, 2 days after the fold; dead-manifest derivations in idea-engine's 4 kit docs; control-protocol pointer predating the manifest move (fable5) | MOVED stubs are permanent, never deleted; pointer fixes happen at the **kit-template level** (one fix, fleet-wide at upgrade), never per-repo hand edits; add a link checker over fm indexes (raw-fetch 200 + not-a-stub check) |
| **Boot-time cross-repo dependency** — a seat that can't orient offline because doctrine moved out | pokemon-mod-lab (private; R22 visibility ritual is load-bearing at session start); every seat's walls read precedes probing | Centralized doctrine ships with a kit-refreshed local digest fence (pointer + minimal cached body); a boot-set read must never require a network fetch |
| **ID-namespace collisions** | fm "Q-0266" ≠ superbot Q-0262.7 (caught independently by two repos); shared Q-NNNN grammar across ~19 kit repos; duplicate "ORDER 007" under concurrent dispatch (pokemon renumbering precedent) | Repo-qualified IDs in all fm indexes (`superbot:Q-0262.7`); never renumber; fm-owned Q/SIM assignment registry (C8) so lanes stop parking on missing numbers; "next free number at HEAD, never concrete" stays law (fm playbook R19) |
| **Owner/kit authority boundaries** — analyst-side moves of gated surfaces | Q-0274 grounding is owner-directed; the CAPABILITIES seed fence + workflow files are kit-owned (kit regen clobbered host customizations 5× at idea-engine); CLAUDE.md-class rules are propose-only (superbot Q-0106) | Phase 5 isolates every gated move as a proposal (router Q / structured choice with a recommendation); kit-owned surfaces route via kit-lab ORDER, never local edits |
| **Append-only citation breakage** on outbox rollover | sim-lab ~875KB / idea-engine 459KB outboxes; `@SHA` + line-number citations everywhere | A10 convention mandates pointer stubs + pinned-SHA archive filenames **before** any file is rolled; verdict/proposal numbering is content-stable, never positional |
| **Private-content leakage** via centralization | pokemon-mod-lab is the fleet's one private repo (vendored Nintendo source) and **was world-readable for ~2 days while asserting PRIVATE** (the R22 incident); fm's roster already failed to read it (UNREADABLE at gen #36) | fm mirrors/indexes from pokemon-mod-lab are prose-only — never build artifacts, ROMs, or vendored source; the audits register states this rule explicitly; the roster read-token fix (fm #144) stays owner-queued, not worked around |
| **fm as a new drift source** — restated counts/asks | superbot's own night-review §7 + control/status ⚑ restating owner-queue items ("restatement is the drift class the repo itself names"); games ledger drift recurring 3× | fm indexes by pointer and **derives** every count a generator can compute; never hand-restates numbers; the lane KIT-ASK for a ledger-drift advisory checker is endorsed, kit-side |
| **Heartbeat/self-report lag poisoning generated indexes** | games DARK ~37h on a frozen heartbeat while shipping ~50 PRs (owner-facing night worklists misread it); idle kit-line 8 releases stale; pml roster row DARK/UNREADABLE overridden by the owner verbatim | C4/E5 derive from **trees** (`substrate.config.json`, workflows, rules-probe logs), not heartbeat text; roster splits heartbeat-age from evidence-age (last merge); the frozen-archive-vs-overwrite doctrine conflict gets an fm ruling (Phase 5) before `status.md` is trusted fleet-wide |
| **Rescue-window loss** — archive clicks freeze un-mirrored records | fm ORDER P1-4 status unresolved while sonnet5 awaits archive (execution evidence conflicting — see D5; re-verify against the ORDER text, don't assume either way); forge ORDER 023/P1-1 + P1-2 (games-web + API proposal) unexecuted in an archive-bound repo; forge's owner-rulings timeline (the only durable copy of two chat-only merge grants) in an archive-bound repo; fable5's succession pack "unconsumed" with dead CHANGELOG links | Phase 4 mirrors run **before** the E#44/E#45 gates execute; the consolidation plan's done-when ("final status points at them") is enforced by an fm checker row, not memory |

---

## 7. Cross-cutting decisions (decide-and-flag; owner can veto at the gate)

1. **Program law stays in substrate-kit** (fm indexes by PL-ID) — moving it fights
   CI-enforced D-0002 and every consumer pointer for zero custody gain.
2. **EAP narrative stays in superbot** (fm indexes row-level) — the measured gap is the
   index (0 links @ fm `eff4c7d`), not the home.
3. **Per-repo CAPABILITIES files remain the venue write surface** — centralizing
   *writes* makes the ledger wrong-somewhere-by-construction; centralize the
   *aggregate*.
4. **The fleet coordination protocol prose moves to fm** (not kit, not superbot): fm
   operates the bus and is sole writer of every inbox; grammar constants stay
   kit-owned. This is the one authored-doctrine MOVE with medium risk — ships
   version-stamped, pointer flips batched via ORDERs, local-delta appendices preserved.
5. **The R-register formalizes in fm**, mirroring the PL-register pattern — fm already
   owns the playbook; pokemon's restatement sprawl is the evidence.
6. **Slice 0 outranks everything**: every item is fm-write-scope, reversible, and
   closes a drift already burning owner attention — including two time-boxed items
   (the 07-17 trigger double-fire; the pre-archive rescue prep).
7. **Fleet audits register in fm `docs/audits/`, not superbot `docs/eap/`** — flagged,
   not silent: fm's own design rule ("program-facing truth → superbot") arguably points
   the other way, and the websites note says the split needs one answer. Rationale:
   sweep audits are manager-operational records (they drive ORDERs and dispositions),
   not program narrative; program-narrative *summaries* of an audit can still be
   indexed into the EAP corpus. Owner can veto at the gate.

---

## 8. Honest gaps

- **SHA pinning is partial.** Only superbot (`bbc524e4`), fleet-manager
  (`ff6361a`/`eff4c7d`), substrate-kit (`727f5db`), and superbot-next (`50814bb` —
  corrected 2026-07-14 after the draft's `abe80c0` pin failed to resolve) are
  pinned in the collation header; the other 15 repos are cited at "per-repo HEAD as of
  the dated note" (2026-07-11…13). Before executing any MOVE, re-pin the source path
  at execution-time HEAD.
- **§2 is an enumerated inventory (47 rows), but folding still hides nominations.**
  The 2026-07-14 fact-check + notes cross-check found eight lane nominations the draft
  had folded away or thinned; they are now restored in place (gen-2 custom-instructions
  proposals → D2/D5; forge ORDER 023/P1-1 + P1-2 → D5/Phase 4; fable5 archive/relaunch
  disposition → C2/Slice 0; the superseded superbot centralization seeds + this plan's
  own landing home → §1 Self-application/Slice 0 item 9; venture's OWNER-QUEUE roll-up
  → C2; the kit allocation ladder → D4; superbot-next's rebuild evidence corpus → D3;
  websites' non-wake continuous-mode doctrine → A12; the audits-home split → D6/§7.7).
  Residual risk: further sub-items inside class rows may still be under-enumerated —
  the executing session should re-read each cited note candidate before closing a row.
- **fm target paths in §3 are proposals**, not existing files — they follow fm's
  current layout (`docs/`, `registry/`, `projects/`, `environments/`,
  `telemetry/` per fm @ `ff6361a`) but the exact filenames are for the executing fm
  session to confirm against fm's docs-gate conventions.
- **Single-sourced facts: one confirmed, one falsified (2026-07-14 fact-check).** The
  "fm holds zero sim-lab capability entries" grep (@ `ff6361a`) was independently
  re-verified TRUE. The "kit ORDER P1-4 unexecuted / zero cfgdiff docs at kit HEAD"
  check was re-verified **FALSE** — two cfgdiff reports are tracked at kit `727f5db`
  (see D5); only the narrower "does P1-4 name a different artifact?" question remains
  open, to be settled against the ORDER text at execution.
- **Some point-in-time figures decay fast**: the sim-lab outbox grew 834KB → ~875KB
  between note and fact-check, and websites' prompt hand-pin grew 26 → 29 paths in one
  day. Treat every size/count in this plan as at-review-SHA, re-derive at execution.
- **Effort estimates exist only for Slice 0** (~1 fm session). Phases 1–5 are ordered
  by dependency and risk, not sized; the executing coordinator should size each phase
  when it is claimed.
- **Owner gates are assumed, not confirmed**: E#44/E#45 (archive clicks) and Q-0274
  (grounding home) are cited from the notes as owner-directed; their current state
  should be read from fm `docs/owner-queue.md` at execution time.
