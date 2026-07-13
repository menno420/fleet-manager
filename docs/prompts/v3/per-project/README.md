> **Status:** `reference`

<!-- v3.6 · 2026-07-13 · provenance: owner final night order TASK 1 (v3.5 stage-2) — open-PRs-stay-open STANDING + Q-0272 reading path + Q-0273 venue model + Q-0274 grounding boot-read folded into all 9 startup DOCTRINE sections + CI dictionaries, and the NINTH SEAT (Curious Research) added; see the v3.6 changelog section below. Prior: v3.5 (ORDER 039 seat-task 5 — Q-0271 autonomy-rider + Q-0273 seed-skills fold into all 8 startup DOCTRINE sections + CI dictionaries; see the v3.5 changelog section below). v3.4 (prompt-currency audit (docs/research/2026-07-12-prompt-currency-audit.md, PR #118 lane) — 16-delta currency restamp of the v3.3 one-file-per-seat model; see the v3.4 changelog section below. Prior: v3.3 (owner spec 2026-07-12, overnight prompt rebuild — CI becomes a per-seat keyword dictionary; startups EXPAND, no char cap) · v3.2 (stateless correction) · v3.1 (research PRs #93/#95 + owner baseline + QA PRs #100/#101/#102, applied in PR #103) -->
<!-- char-count: planning doc, no paste budget applies -->

# Per-project prompts — v3.6 (per-seat Custom Instructions + expanded startups)

v3.6 (v3.5 **stage-2**, owner final night order TASK 1) **completes the fold
program**: OPEN-PRs-STAY-OPEN promoted to the STANDING default, the Q-0272
reading path, the Q-0273 venue model (`VENUE:hub`), the Q-0274 grounding
boot-read — and the **NINTH SEAT, Curious Research** (changelog below). v3.5
folded the Q-0271 AUTONOMY RIDER + the two Q-0273 seed skills into the v3.4
bodies. v3.4 was a currency restamp of the v3.3 composition (16
prompt-currency-audit deltas, 2026-07-12). The composition itself is the v3.3
owner spec (2026-07-12 — supersedes the v3.2 generated/assembled model):

- **`<seat>-custom-instructions.md`** = the seat's **complete Custom
  Instructions paste artifact, ONE AUTHORED FILE PER SEAT**: seat header +
  condensed five-section skeleton (Orientation · Landing path · Routine-fired
  session · Never-idle ladder · Capabilities/heartbeat/asks) + a **keyword
  dictionary** (fleet vocabulary → meaning → route) + a Routes footer. The
  v3.1/v3.2 core+seat-block **assembly is RETIRED** — nothing is assembled;
  the file is the paste. `../custom-instructions-core.md` is kept as routed
  **reference doctrine only** (the dictionaries' `CORE` alias). HARD cap
  8,000 chars (verified console wall) · aim ≤7,500; count the paste as
  pasted (Codex PR #103 lesson — no placeholders remain).
- **`<seat>-startup.md`** = the seat's **AUTHORED, EXPANDED coordinator
  brief** — no longer generated from `../universal-startup.md` (that template
  is kept as the v3.2 skeleton of record). The v3.2 procedure text is
  preserved byte-verbatim outside the documented v3.3 splices; the universal
  doctrine now rides **in the startup, verbatim and in full** (TRUTH +
  INJECTION GUARD, WORKER-RELAY, CONTROL BUS, GEN-3 HYGIENE v5, the
  owner-landed PERMISSIONS grant from `projects/UNIVERSAL.md`, all nine QA
  riders, the session ender inlined from `../session-ender.md`). **NO char
  cap — size is a NOTE, not a gate** (owner spec 2026-07-12).
- **Layer contract:** the Custom Instructions are the **compression
  dictionary** over the startup — every dictionary keyword's full behavior
  lives in the startup (or the repo doc the entry routes to); a CI entry and
  its source may never disagree. Keywords/expansions still lacking a durable
  routed home are tracked in **[`../planned-routes.md`](../planned-routes.md)**.
- **Drift guards** (run `python3 ../tools/regen_b_files.py` after ANY prompt
  edit; all fail the run): CI hard-cap gate · **ender sync D-10** (each
  startup's inlined ender byte-matches `../session-ender.md`) · **grant
  sync** (each startup's grant byte-matches `projects/UNIVERSAL.md`'s
  canonical block) · **doctrine identity** (the DOCTRINE section
  byte-identical across all 9 after normalizing the one status-grammar
  fill) · card-block identity · stamp/DRIFT-CHECK lines · failsafe
  extraction. Registry sync keeps `--check-registry` / `--write-registry`.
- **STATELESS RULE (D-9, unchanged):** neither layer carries volatile state —
  no concrete PR numbers, no SHA/CI colors, no trigger ids asserted as facts,
  no "do X now" items; prompts name WHERE current state lives; current work
  reaches a seat only through its WORK SOURCES ladder.

## Census inputs — AVAILABLE (write against them, not from memory)

- **Core census — PR #94**, `docs/research/2026-07-12-problem-census-core.md`.
- **Satellite census — PR #96**, `docs/research/2026-07-12-problem-census-satellites.md`.
- **QA audits (v3.1's fix source): PRs #100/#101/#102**,
  `docs/research/2026-07-12-qa-{incident-replay,question-rounds,boot-simulation}.md`.

All are dated snapshots — the v3.1 grammar for every baked specific is
**"verify at boot; expected X as of 2026-07-12, or later"** (boot-sim class b).

## The 9 seats (owner restructure 2026-07-11 + ninth seat 2026-07-13)

The 8 from v3.0: Fleet Manager · SuperBot 2.0 (superbot + superbot-next) ·
Websites · Self Improvement (substrate-kit) · SuperBot World (games + idle +
mineverse) · Game Lab (gba-homebrew + pokemon-mod-lab) · Ideas Lab
(idea-engine + sim-lab) · Venture Lab (venture-lab + trading-strategy).
**Seat 9 (v3.6, owner-created 2026-07-13 ~03:05): Curious Research**
(curious-research — the teaching-and-research gift seat; founding pair:
superbot docs/owner/curious-research-project-prompts-2026-07-13.md, conformed
to this registry's format in v3.6).

**Not seats:** product-forge (⚑ awaits owner disposition; if seated it becomes
seat 10 via this same recipe — stagger slot below), codetool-lab-* (DARK),
superbot-plugin-hello (helper, folded into SuperBot 2.0's F1).

## v3.6 size table (real counts, checker-verified 2026-07-13 — `../tools/regen_b_files.py`)

Same caps as v3.5 (CI HARD ≤ 8,000 chars AND bytes; bytes binding at these
margins; startups NO cap — size is a NOTE). The stage-2 folds added ~+310
bytes per CI; compensating wording compressions (shared + per-seat, NO rule
dropped — the fat details ride the startups per the layer contract) brought
every seat back under the wall.

| Seat | CI (chars) | CI (bytes) | Expanded startup (chars) | v3.5 CI was (chars/bytes) |
|---|---:|---:|---:|---:|
| fleet-manager | 7,966 | 7,993 | 32,749 | 7,909 / 7,992 |
| superbot | 7,966 | 7,993 | 32,475 | 7,914 / 7,985 |
| websites | 7,969 | 7,998 | 32,140 | 7,911 / 7,992 |
| self-improvement | 7,970 | 7,999 | 32,265 | 7,909 / 7,990 |
| superbot-world | 7,971 | 7,998 | 31,791 | 7,917 / 7,992 |
| game-lab | 7,969 | 7,999 | 31,628 | 7,917 / 7,996 |
| ideas-lab | 7,965 | 7,992 | 31,911 | 7,913 / 7,994 |
| venture-lab | 7,962 | 7,991 | 31,984 | 7,915 / 7,996 |
| curious-research | 7,967 | 7,998 | 32,961 | — (new seat) |

## v3.5 size table (HISTORICAL — superseded by the v3.6 fold above)

Same caps as v3.4 (CI HARD ≤ 8,000 chars AND bytes; bytes binding at these
margins; startups NO cap — size is a NOTE). The "v3.4 was" column is the
measured pre-fold baseline of 2026-07-13 (fleet-manager's CI had drifted
+26/+26 over the v3.4 table via post-restamp seat edits, e.g. R26).

| Seat | CI (chars) | CI (bytes) | Expanded startup (chars) | v3.4 CI was (chars/bytes) |
|---|---:|---:|---:|---:|
| fleet-manager | 7,909 | 7,992 | 30,916 | 7,893 / 7,976 |
| superbot | 7,914 | 7,985 | 30,642 | 7,922 / 7,993 |
| websites | 7,911 | 7,992 | 30,307 | 7,895 / 7,976 |
| self-improvement | 7,909 | 7,990 | 30,432 | 7,908 / 7,989 |
| superbot-world | 7,917 | 7,992 | 29,958 | 7,919 / 7,996 |
| game-lab | 7,917 | 7,996 | 29,795 | 7,917 / 7,996 |
| ideas-lab | 7,913 | 7,994 | 30,078 | 7,897 / 7,978 |
| venture-lab | 7,915 | 7,996 | 30,151 | 7,916 / 7,997 |

## v3.4 size table (HISTORICAL — superseded by the v3.5 fold above)

Hard cap: **Custom Instructions ≤ 8,000 chars AND ≤ 8,000 UTF-8 bytes**
(verified console wall; aim ≤7,500 — every seat runs over the aim BY DESIGN:
the owner's mandated keyword set outranks the fitted target, same call as
v3.2's safety-over-fitted). **Bytes are the binding basis at these margins**
(em-dashes and the RISK emoji are multi-byte): three seats sit ≤4 bytes under
the wall — any future CI addition needs a compensating trim in the same edit.
**Startups have NO cap** — sizes below are a NOTE, not a gate (owner spec
2026-07-12). The session ender is a chat paste (no console cap).

| Seat | CI (chars) | CI (bytes) | Expanded startup (chars) | v3.3 CI was (chars/bytes) |
|---|---:|---:|---:|---:|
| fleet-manager | 7,867 | 7,950 | 28,542 | 7,850 / 7,922 |
| superbot | 7,922 | 7,993 | 28,591 | 7,934 / 7,996 |
| websites | 7,895 | 7,976 | 28,256 | 7,925 / 7,997 |
| self-improvement | 7,908 | 7,989 | 28,328 | 7,918 / 7,988 |
| superbot-world | 7,919 | 7,996 | 27,854 | 7,924 / 7,986 |
| game-lab | 7,917 | 7,996 | 27,691 | 7,927 / 7,995 |
| ideas-lab | 7,897 | 7,978 | 27,974 | 7,855 / 7,925 |
| venture-lab | 7,916 | 7,997 | 28,047 | 7,926 / 7,994 |

## v3.3 size table (HISTORICAL — superseded by the v3.4 restamp above)

| Seat | CI (chars) | CI (bytes) | Expanded startup (chars) | v3.2 startup was |
|---|---:|---:|---:|---:|
| fleet-manager | 7,850 | 7,922 | 27,409 | 7,833 |
| superbot | 7,934 | 7,996 | 27,625 | 7,819 |
| websites | 7,925 | 7,997 | 27,310 | 7,838 |
| self-improvement | 7,918 | 7,988 | 27,473 | 7,927 |
| superbot-world | 7,924 | 7,986 | 26,999 | 7,868 |
| game-lab | 7,927 | 7,995 | 26,836 | 7,999 |
| ideas-lab | 7,855 | 7,925 | 27,144 | 7,770 |
| venture-lab | 7,926 | 7,994 | 27,186 | 7,841 |

Seat-first ratio: ~74–76% of each CI's non-blank chars are seat-specific on
the drafting-pass line-identity basis (~72.8–73.1% on the verifier's
paste-body line-identity measurement — both clear the ≥60% bar); the v3.2
assembled CI ran ~12% seat share, which is what the owner rejected. Counts
restate at every edit: run the checker, then update this table + each
file's own header.

## v3.2 budget table (HISTORICAL — the assembled-CI generation this table measured is retired; FILLED values)

Hard caps: startup ≤ 8,000 · assembled CI ≤ 8,000 — **all 20 within hard**.
**Assembled CI is counted with `{{SEAT_NAME}}` + `{{STATUS_GRAMMAR}}` FILLED**
(Codex PR #103 review: the raw-placeholder count under-measured every paste by
the fill delta and let 3 seats silently exceed 8,000 — never count a paste
with placeholders in it). Fitted target 7,500: the universal artifacts fit;
**every B file runs over fitted, flagged in its header** — the safety-rail
volume does not fit under 7,500 without dropping rules, and the mission ranks
safety over the fitted target. Seat-block C and assembled-CI figures are
**unchanged from v3.1** (the C artifacts were audited, not edited, in v3.2).

| Artifact | Chars | vs fitted 7,500 / hard 8,000 |
|---|---:|---|
| A universal-startup (body) | 6,567 | n/a (template; skeleton budget ≤ ~6,600) |
| C universal core (CORE-START/END) | 6,996 raw · 6,992–7,031 filled per seat | seat-block hard budget = 8,000 − FILLED core |
| D session-ender (body) | 3,411 | chat paste — console cap n/a; over its ~2,000 prose budget BY DESIGN (P0 ender fixes), flagged in-file |
| Seat | Startup B (v3.2) | Seat block C | Assembled CI (filled core + block) | Status |
| fleet-manager | 7,833 | 975 | 7,972 | under hard, over fitted — flagged |
| superbot | 7,819 | 984 | 7,994 | under hard, over fitted — flagged |
| websites | 7,838 | 951 | 7,943 | under hard, over fitted — flagged |
| self-improvement | 7,927 | 992 | 7,992 | under hard, over fitted — flagged |
| superbot-world | 7,868 | 966 | 7,997 | under hard, over fitted — flagged |
| game-lab | 7,999 | 971 | 7,984 | under hard, over fitted — flagged |
| ideas-lab | 7,770 | 980 | 7,992 | under hard, over fitted — flagged |
| venture-lab | 7,841 | 990 | 7,998 | under hard, over fitted — flagged |

The v3.0 constant "core 6,117" is RETIRED (D-8); the single source for the
core figure is this table + the core file's own markers, restated at every
core edit.

## Failsafe cron stagger table (canonical home — D-7; the manager arbitrates)

| Seat | cron | Slot | Provenance | Live state (audit, 2026-07-12 ~15:40Z) |
|---|---|---|---|---|
| self-improvement | `0 */2 * * *` | even :00 | v3.0, kept | live on slot ✓ |
| game-lab | `50 */2 * * *` | even :50 | **re-slotted to live 2026-07-12** (was `15 */2`; the live trigger already fires at :50 — table adopts it, no re-arm) | live on slot ✓ |
| fleet-manager | `30 */2 * * *` | even :30 | census-verified | live on slot ✓ |
| websites | `45 */2 * * *` | even :45 | baseline kept | assumed on slot (verify at next sweep) |
| superbot | `0 1-23/2 * * *` | odd :00 | v3.0, kept | ⚠ **NO live seat failsafe — arm to this slot** |
| superbot-world | `15 1-23/2 * * *` | odd :15 | v3.0, kept | ⚠ live at `0 */2` (squats even :00) — **re-arm to this slot** |
| ideas-lab | `30 1-23/2 * * *` | odd :30 | v3.0, kept | ⚠ live at `0 */2` (squats even :00) — **re-arm to this slot** |
| venture-lab | `45 1-23/2 * * *` | odd :45 | v3.0, kept | ⚠ live at `0 */2` (squats even :00) — **re-arm to this slot** |
| curious-research | `20 */2 * * *` | even :20 | **v3.6 (2026-07-13)** — the founding pair's owner-chosen free offset, adopted into the registry | armed at seat founding (verify at next sweep) |

Seat-10+ slots: `5/35` past the hour, plus even `:15` (freed by game-lab's
re-slot; even parity first; `:20` taken by curious-research, v3.6). **The fleet manager is the slot arbiter** — a
seat NEVER re-slots itself; a foreign trigger on your slot is reported in
status, and slot changes are a registry edit here (question-rounds R5-Q5).
**Live-trigger reconciliation (v3.4 delta 13, from the prompt-currency
audit's trigger census, ~15:40Z):** superbot-world, ideas-lab, and venture-lab
failsafes are ALL live at `0 */2` — a four-way collision with the
self-improvement slot — and superbot has NO live seat failsafe; the ⚠ rows
above are the collision-free re-slot. **Seat-side re-arm ORDERs are the
manager's follow-up work — this doc edit re-slots the registry only.** The
earlier snapshot-verified transients (pre-merge gba/pml hourly wakes,
retro-games trigger) remain gone. Venture-lab's grading BUSINESS cron
(`0 9 * * 5`) does not collide and is rebound-never-deleted (A step 4). Since
v3.2, NO trigger id is baked into any prompt — cutover ids come from
heartbeats + the telemetry snapshot (D-9).

## v3.0 KNOWN DEFECTS queue — v3.1 disposition

1. A over budget → **restructured**: A carries procedures; riders moved to the
   core (division-of-labor note in A's header); A body 6,496.
2. BOOT-1 orientation path hardcoded/dead → **fixed**: `{{ORIENTATION_PATH}}`
   slot + universal dead-pointer rule (skip, note, continue).
3. Missing FIRST_WORK_ORDERS slot → **fixed**: canonical insert point in the
   regen script (between BOOT and WORK LOOP).
4. BOOT-3 per-repo inbox read → **fixed**: "READ THE BATON, in EACH repo"
   (now also reads control/status.md — the succession baton, T7).
5. "(green expected)" vs expected-red seats → **fixed**: `{{EXPECTED_RED}}`
   slot; red outside the set = first slice.
6. PACEMAKER vs ender never-re-arm → **fixed** in A step 3b (ender exception,
   canonical, all 9 copies regenerated; C-5/D-3 retired).
7. pokemon-mod-lab required-check conflict → **carried**: game-lab W2 reads
   the LIVE required set (probe-PR fallback, GL-2).
8. Stale "enabler in 3/13 lanes" figure → superseded by per-seat merge notes
   specializing the core LANDING DOCTRINE.
9. superbot settings-grant HYPOTHESIS → **kept**, HYPOTHESIS-marked, now
   bounded by the doctrine's ONE-attempt rule (C-3 resolved).
10. trading squash precedent-not-guarantee → **fixed**: named a repo-local
    sole exception, ONE attempt, retired on first denial, never transfers
    (C-2 resolved).

## v3.1 residuals (not applied, with reasons)

- Question-rounds P2 "budget directive" and "rate-limit classify" are applied
  (core riders); P2 "calibration" applied (A). No P0/P1 rows were dropped.
- Incident-replay MEDIUM leftovers not encodable under the caps: I-38
  orientation-sprawl root cause (a superbot-repo docs problem, not a prompt
  line), I-44 CAPABILITIES/capabilities case-duplicate (**RESOLVED 2026-07-12
  — v3.4 delta 14**: lowercase folded into `docs/CAPABILITIES.md`, pointer
  stub left), I-58's remaining auto-merge race classes
  (trailing-commit race, GraphQL rate-limit, disarm false-success — need
  fresh evidence before prompting), I-66 subscription no-green-event note
  (partially covered by TOKEN BUDGET park-don't-poll), I-72 dry-backlog →
  disarm-ask conversion (owner-policy question, router material).
- Owner-queue gaps from PR #100 (I-37 websites toggle, I-43 env-teardown
  auto-disable, I-52 venture #51 HOT, I-55 gba/trading required-check clicks,
  I-67 routines email pack) are OWNER-QUEUE work, not prompt text — left for
  the fleet-manager seat's QUEUE SWEEP (its W2 already re-verifies asks).

## v3.1 KNOWN DEFECTS queue — ORDER 014 cross-check (v3.2 input)

Source for every entry: substrate-kit ORDER 014 deliverable
`docs/reports/2026-07-12-prompt-template-hardening-input.md` @ kit main
`8a544a6` (kit PR #256). Method: a kit report is a claim, not a fact — every
§(c) "the fleet prompts state this wrongly" item was verified against the
SHIPPED v3.1 files in this tree (grep + read, 2026-07-12). Note the kit's §(c)
audited the LEGACY prompts (`projects/substrate-kit/` @ e801da5c), which still
carry those defects on main — the v3.1 rebuild does not, verdicts below.

**§(c) corrections — v3.1 verdicts (5 checked, 0 real v3.1 defects):**

1. Retired failsafe trigger/session ids (`trig_016EfUawz6KxEYqUM6f1BqDw`,
   `session_01YMJrUDpcarFsqPZ2BeeiVB`) → **not affected — already correct**:
   zero occurrences anywhere under `docs/prompts/v3/`; baked trigger ids are
   banned by design (`../custom-instructions-core.md:81` "no trigger ids
   (those live in artifact B's volatile cutover slots only)") and the kit
   seat's cutover slot cites heartbeat pointers, not ids
   (`self-improvement-startup.md:24` "the 2-hourly failsafe (heartbeat
   #252/#253 ids)"). No fix needed.
2. meta.md stale facts (archived coordinator session named live; "Part 4
   failsafe NOT deployed"; "852 tests"; "20 templates") → **not affected —
   already correct**: none of the stale tokens appear in v3.1; the kit seat
   states current truth "every reachable adopter ≥ v1.12.1"
   (`self-improvement-startup.md:11`). No fix needed.
3. coordinator-prompt.md staleness (kit @ `7e600c6` / "proven (v1.7.0)";
   PACEMAKER "this chain, not your cron, keeps you running") → **not affected
   — already correct**: neither token appears; v3.1 states the corrected
   doctrine "Q-0265: chain = pacemaker, cron = dead-man failsafe"
   (`../custom-instructions-core.md:51`) plus the ender never-re-arm
   exception (`../universal-startup.md:22`). No fix needed.
4. lab-loop "👤 the loop cannot arm itself / owner console action" (falsified
   twice — agent-side create_trigger succeeded, kit PRs #195/#253) → **not
   affected — already correct**: v3.1 never repeats the claim; the daily is
   handled as disposition only ("the 06:00Z kit-lab DAILY = owner BUSINESS
   cron — KEEP", `self-improvement-startup.md:24`; "never yours to delete",
   `self-improvement-custom-instructions.md:11`) — an ownership/protection
   label, not an arming-capability claim. The kit-side lab-loop.md fix is the
   kit lane's follow-up (per the ORDER 014 doc itself). See entry 7 for the
   adjacent generic-rebind gap this check surfaced.
5. Model-class / environment-id display anomaly (registry shows Opus-class +
   `env_01WAB…` for all kit triggers; kit flags it display-artifact) → **not
   affected — already compliant**: no `env_*` id and no model id appears
   anywhere under v3/; the core already mandates "family-level model names
   only" (`../custom-instructions-core.md:45`) — exactly the mitigation the
   kit doc asks prompts to adopt. No fix needed.
6. instructions.md v2 → the kit found no wrong facts there; nothing to
   verify, no queue entry.

**§(a)/(b) coverage gaps — REAL v3.2 queue entries (ALL THREE CLOSED by the
v3.3 rebuild — see the v3.3 changelog below):**

7. **Fresh-session-per-fire binding rule missing; the generic BUSINESS-cron
   rebind text conflicts with it** — source: ORDER 014 §a.1 ("a standing loop
   must be fresh-session-per-fire so it survives session archive") + §b
   routines row. v3.1 line affected: `../universal-startup.md:24` (A step 4,
   regenerated into all 8 B files) "A BUSINESS cron (a scheduled deliverable)
   is rebound, never dropped: create its replacement bound to THIS session →
   verify → delete the old" — wrong for a fresh-session-per-fire deliverable
   (the live kit-lab daily, kit PR #253): rebinding it to the seat session
   would re-create the dies-with-the-seat class the kit doc names; today only
   the kit seat's hand-written "KEEP" note (`self-improvement-startup.md:24`)
   saves the one live instance. Proposed fix: one clause in A step 4 — a
   business cron armed fresh-session-per-fire is KEPT as-is, never rebound;
   plus the binding-choice sentence (self-bind = live-seat failsafe only,
   re-armed at every cutover; standing loop = fresh-session-per-fire). Then
   regen the 8 B files. Priority: **P2**.
8. **Heartbeat `kit:` exact line grammar not prompt-carried** — source: ORDER
   014 §a.4 ("the prompt must carry the exact line shapes or adopters
   regenerate the drift class every wave"; incident: pokemon-mod-lab's
   `- **kit:** vX` bold form is invisible to `KIT_LINE_RE`, kit
   `src/engine/grammar.py:120`) + §b grammar row (◐ partial). v3.1 line
   affected: `../custom-instructions-core.md:47` CONTROL BUS carries the
   one-writer + neutrality rules and a `{{STATUS_GRAMMAR}}` slot, but every
   seat fill is a write-mode only (e.g. "wholesale overwrite",
   `self-improvement-custom-instructions.md:5`) — the exact plain-form
   `kit: vX.Y.Z · check: green|red · engaged: yes|no` shape, the bold-form
   negative example, and the adopters.md version-deference rule ride no v3.1
   paste. Proposed fix: one core sentence in CONTROL BUS (or a widened
   `{{STATUS_GRAMMAR}}` convention): plain `kit:` line verbatim + "the
   bold-label form does not parse" + "fleet version truth defers to the
   generated docs/adopters.md, never hand-asserted". Priority: **P2**.
9. **Stale-MCP-PR-read cross-check not explicit** — source: ORDER 014 §a.3
   ("Never trust an MCP PR read alone for merge/CI state — cross-check via
   git fetch or the Actions runs"; ~25-min-stale reads, kit friction #15;
   guard status: prose-only, "MUST ride the prompts"). v3.1 nearest coverage:
   `../universal-startup.md:29` (diff the merge commit) + `:31` (never record
   "pushed"/"done" without exit 0 AND git ls-remote) +
   `../custom-instructions-core.md:62` (Q-0120 tool verdicts are leads) —
   pushes and merges are covered, but no line names PR-STATE READS as
   stale-prone. Proposed fix: one clause in the TOOL FACTS rider
   (`../custom-instructions-core.md:56`): "MCP PR-state reads can serve
   ~25-min-stale data — cross-check merge/CI state via git fetch or the
   Actions runs". Priority: **P3**.

**§(a)/(b) items verified already covered in v3.1 (no queue entry):** landing
path §a.2 — READY + never-self-arm/merge + enabler + deny-wins
(`../custom-instructions-core.md:51`), LANDING DOCTRINE (`:54`), born-red
card FIRST commit / flip LAST (`../universal-startup.md:25`), designed-HOLD +
legacy-alias-jobs red reading (`../custom-instructions-core.md:49`;
`self-improvement-startup.md:16`). Verify-don't-trust §a.3 core —
tree-beats-any-doc precedence (`../universal-startup.md:9`), verify-after-arm
via list_triggers (`:21`), account-wide paginate-to-exhaustion / "page 1 is
never the registry" (`:24`), checker's-bug clause
(`../custom-instructions-core.md:62`). Claims one-file + claim-before-build
§a.5 (`../universal-startup.md:25`; `../custom-instructions-core.md:58`).
Preflight fetch + hard-reset §a.5 (`../universal-startup.md:16` HARD-SYNC,
with the dirty-tree rescue-branch guard). Sequential trigger-call pacing §a.5
(`../custom-instructions-core.md:49` "ONE trigger-MCP call per worker"). The
§b rows marked "❌ missing" name KIT-TEMPLATE graduation work
(CONSTITUTION/landing-path/routines templates) — that is the Self Improvement
seat's lane, not a v3.1 prompt defect; only their fleet-prompt shadows
(entries 7–9) queue here.

## v3.6 changelog — stage-2 fold + the ninth seat (2026-07-13, owner final night order TASK 1)

**Version label: v3.6, not "v3.5 stage-2".** The registry's own rule decides
it: the stamp line is the DRIFT CHECK — any body-changing re-sync must bump
the generation so a stale paste is detectable by quoting the stamp. Stage-2
changes every startup body, so it takes the next number. (The former "v3.6 =
kit #279 seat-digest fences" pending item shifts to v3.7 — still blocked on an
unreleased kit.) Owner skim doc for the whole night's delta:
[`../CHANGES-v3.4-to-v3.5.md`](../CHANGES-v3.4-to-v3.5.md).

**Sources verified at superbot HEAD `c65750e` (2026-07-13):**
`docs/owner/fleet-direct-orders-2026-07-13.md` (the standing open-PRs rule) ·
`docs/fleet-reading-path.md` + `scripts/fleet_status.py` (Q-0272) ·
`docs/owner/fleet-night-orders-2026-07-12.md` §0b + router Q-0273 (venue
model) · `docs/owner/fleet-grounding.md` + router Q-0274 (grounding) ·
`docs/owner/curious-research-project-prompts-2026-07-13.md` (ninth-seat
founding pair).

1. **OPEN-PRs-STAY-OPEN → STANDING default** (all 9 startups, shared DOCTRINE
   AUTONOMY RIDER sentence, byte-identical): land on green where auto-merge
   arms; otherwise leave the PR OPEN and take the next slice — never
   merge-chase, never park-and-wait, open PRs are never blockers; follow-on
   work stacks on the open head with the base noted in the PR body; the owner
   sweeps open PRs from the hub venue. This supersedes v3.5 changelog item 5:
   the owner promoted the night rule to durable doctrine (direct orders
   2026-07-13), so it now clears the D-9 statelessness bar. CI hook: the
   BOOT TRIAD / AUTONOMY dictionary entry.
2. **FLEET READ (Q-0272)** (shared DOCTRINE paragraph): standing read-only
   authorization for every fleet repo (pml DARK), the
   `docs/fleet-reading-path.md` route, `fleet_status.py` as the live-state
   command, and the unchanged boundaries (MCP scoped to attached repos;
   writes in-repo; cross-repo work via manager ORDERs). CI hook: the Routes
   footer.
3. **VENUE MODEL (Q-0273)** (shared DOCTRINE paragraph): hub venue vs Project
   seats vs the PM seat; merge/destructive-shaped owner-queue items carry the
   `VENUE:hub` tag. CI hook: the six-field-ask sentence.
4. **GROUNDING (Q-0274)** as boot reading: the shared DOCTRINE names §0–§1 +
   YOUR seat's § + §10; each seat's Orientation route bullet carries its own
   § number (fm §2 · superbot §3 · world §4 · ideas §5 · venture §6 · kit §7
   · websites §8 · game-lab §9; curious-research predates its § and routes to
   its founding pair).
5. **NINTH SEAT — Curious Research:** `curious-research-startup.md` +
   `curious-research-custom-instructions.md`, the founding pair conformed to
   the registry format (shared blocks byte-identical, drift-checked; volatile
   night program NOT carried, per D-9); failsafe slot `20 */2 * * *` adopted
   into the stagger table; registered in the regen tool's SEATS block +
   `seat_digest_sync.py`'s seat map; registry dir `projects/curious-research/`
   generated at v1.
6. **Budget compressions, no rule dropped:** the stage-2 folds added ~+310
   bytes per CI; compensating wording compressions (shared set applied
   identically across the 9, plus small per-seat compressions — e.g.
   dictionary separators to ASCII hyphens, detail that rides the startups
   verbatim shortened to its keyword) brought all 9 CIs to ≤ 7,999 bytes.
   One factual refresh rode along: the superbot CI's `Q-0241 never-wait`
   entry no longer reads "superbot-next ONLY" (Q-0271 generalized never-wait
   fleet-wide; Q-0241 remains the rebuild's stronger rider).
7. **Registry re-synced** (`--write-registry`); every projects/<seat>/
   artifact version-bumped by one; curious-research artifacts start at v1.
   Top v3.7 item: the kit #279 seat-digest fence wiring (blocked, unreleased).

## v3.5 changelog — autonomy-rider + seed-skills fold (2026-07-13, ORDER 039 task 5)

**Source:** owner night-run directive ORDER 039 seat-task 5 (control/inbox.md) =
superbot `docs/owner/fleet-grounding.md` §2 goal 5 ("fold the autonomy rider +
the seed skills into the v3.4+ bodies"). Material verified at superbot HEAD
`cdb2680`: router Q-0271/Q-0272/Q-0273, the AUTONOMY RIDER canonical text
(`docs/owner/fleet-rearm-2026-07-12.md` §3 — Q-0271 named this fold: "destined
verbatim for the v3.4 instruction bodies"), and the two seed SKILL.md bodies
(`.claude/skills/chase-references/` + `.claude/skills/prep-owner-steps/`).

1. **AUTONOMY RIDER → the shared DOCTRINE section of all 8 startups**
   (byte-identical insert, doctrine-identity checked; compressed digest citing
   the canonical verbatim copy): owner absent = NORMAL; silence = consent =
   done — no review step for agent work; an OPEN PR is never a reason to stop;
   the OWNER-ONLY list (settings/rulesets · secrets/env/host · external
   publish + money · destructive prod-data · account/portal) is the sole
   legitimate park class — queue-and-continue, never wait-in-place;
   uncertainty routes as SIM-REQUEST; NEVER-WAIT ≠ BYPASS CI.
2. **SEED SKILLS doctrine block** (same insert): **chase-references** (resolve
   EVERY reference in an ask before acting; an unfound reference is a search
   task, never a skip; state the assembled picture back, Q-0254) +
   **prep-owner-steps** (lead with the deep link; every owner-entered blob as
   its own paste-ready block; batch clicks/pastes to ONE sitting; close with
   payoff + verification). Reference bodies: superbot `.claude/skills/`,
   canonical until the kit generalizes them (ORDER 034 lane).
3. **CI dictionary hooks, all 8:** BOOT TRIAD entry extended to "(Q-0270) /
   **AUTONOMY** (Q-0271) — owner away = NORMAL, queue-and-continue"; skills
   entry extended with "seeds Q-0273: **chase-references** +
   **prep-owner-steps** -> sb:.claude/skills/". Full behavior rides the
   startups per the layer contract; the split is recorded in
   [`../planned-routes.md`](../planned-routes.md) §B.
4. **Compensating budget trims** (pre-fold CIs sat 3–24 bytes under the 8,000
   wall): shared-entry wording compressions applied identically across the 8
   (e.g. "MCP PR-state reads" → "MCP PR reads", "structured choices carry a"
   → "structured choices:") plus small seat-section compressions — wording
   only, NO rule dropped; final counts in the v3.5 table (all ≤ 7,996 bytes).
5. **NOT folded — ORDER 039's open-PRs-stay-open night rule:** a night-mode
   rule, not durable doctrine; the registry is STATELESS (D-9) and has no
   mode-rider slot. It lives in the ORDER thread only. **SUPERSEDED in v3.6:**
   the owner promoted the rule to the STANDING default in the 2026-07-13
   direct orders (superbot docs/owner/fleet-direct-orders-2026-07-13.md) —
   folded as durable doctrine in the v3.6 changelog below.
6. **Registry re-synced** (`--write-registry`); every projects/<seat>/
   artifact version-bumped by one (stamps in the regen tool's SEATS block).
   Top v3.6 item remains the kit #279 seat-digest fence wiring (blocked,
   unreleased).

## v3.4 changelog — prompt-currency restamp (2026-07-12, same day as v3.3)

**Source:** the prompt-currency audit
(`docs/research/2026-07-12-prompt-currency-audit.md`, PR #118 — since merged
to main, `d38bafb`) — its §4
table is the authoritative delta list (16 deltas: 2 P0 · 11 P1 · 3 P2). v3.3
went stale within ~5 hours of landing (four seats' merge lines contradicted by
same-day enabler merges + two P0 defects in the park-green entry itself).
Disposition of all 16, applied in one restamp pass:

1. **[P0-1] park-green laundering qualifier** — all 8 CI dictionaries: "a
   DIFFERENT session may review-merge **on its OWN genuine review only —
   relayed/dispatched authority = laundering, denied**" (PR #113 denial class
   "cross-session permission laundering", n=2 with the 2026-07-11 fm #68/#88-89
   denials). Compensating budget trims applied to ALL 8 CIs (deltas 1/5/8/9/11
   together added ~+350 chars per CI; filler compressed, no rule dropped).
2. **[P0-2] fm landing path** — fm CI: "landing rides a fresh owner-provenance
   dispatch or owner click (this lane's recorded denials name relayed
   authorization — successor review-merge retired)"; fm startup MERGE
   MECHANICS restated to match (layer contract).
3. **[P1-3] PR #113 denial recorded** — appended to `docs/CAPABILITIES.md`
   append log (dated, denial class quoted, session id; done jointly with
   delta 14). The full verbatim denial text was never committed by the denied
   session — recorded as such; future denials must be committed verbatim at
   deny time.
4. **[P1-4] websites enabler live** — `websites-startup.md` MERGE MECHANICS +
   CI Merge clause rewritten to enabler-live semantics (arms claude/* at open;
   green PRs self-land; enabler merged websites #167).
5. **[P1-5] merge-on-green reference exists** — all-8 CI park-green tail:
   "(none committed yet)" → "(reference: sim-lab, live)"; ideas-lab CI +
   startup sim-lab line → "merge-on-green INSTALLED (ORDER 003) — zero agent
   merge calls"; `../planned-routes.md` §A merge-on-green row struck with the
   landing pointer.
6. **[P1-6] trading enabler canonical** — venture-lab CI + startup: "enabler
   INSTALLED and self-landing proven — canonical path; MCP squash exception
   RETIRED-superseded" (five self-landings via github-actions[bot] 2026-07-12).
7. **[P1-7] superbot-world SECURITY-BEFORE-SECRETS flipped** — CSRF landed
   (mineverse #42); open half = owner provisioning of the six OAuth/write
   secrets, now UNBLOCKED (startup :13 self-neutralizes, no edit — per audit).
8. **[P1-8] WALLS staleness rule** — all 8 CIs: "(quote; fresh entries never
   re-probe, >14d re-verify with one cheap attempt)" (kit v1.14.0 DISCOVERY
   step 5).
9. **[P1-9] six-field ask + RISK line** — all 8 CIs + startups: "+ RISK:
   ✅|↩️|⚠" (kit #272 owner-action grammar) + "structured choices carry a
   **bolded recommendation**, one-letter answerable".
10. **[P1-10] BOOT 4 verify-it-DELIVERS** — all 8 startups: fresh-session-per-
    fire delivery = UNVERIFIED-BROKEN until a SCHEDULED fire is proven
    (0-for-2 observed); wedge signature (`enabled ∧ next_run_at < now−15min`);
    manual-fire trap (fire_trigger advances last_fired_at, not next_run_at);
    failsafe wakes check the standing loop's last slot (blind window). The
    keep-don't-rebind rule itself is unchanged. Align wording with the kit's
    `routines.md.tmpl` when kit #287 releases.
11. **[P1-11] skills + /intake routed** — new **skills** dictionary keyword
    (→ `docs/SKILLS.md`) + owner-request route → `/intake` in all 8 CIs; a
    SKILLS & INTAKE bullet in all 8 startups. **PENDING half:** the
    `docs/ROUTINES.md` route waits on a kit release carrying kit #287 (merged,
    unreleased at restamp time) — tracked in `../planned-routes.md` §A.
12. **[P1-12] seat-digest regen wiring — BLOCKED, not applied** — kit #279
    (`substrate-kit:skills-digest`/`walls-digest` fences) is unreleased; do
    NOT wire `../tools/regen_b_files.py` to fences that don't exist at any
    adopter HEAD. Recorded as the top v3.5 item (also in the tool's header).
13. **[P1-13] failsafe stagger table reconciled** — see the re-slotted table
    above: game-lab re-slotted to its live `50 */2`; superbot-world/ideas-lab/
    venture-lab flagged ⚠ re-arm (all live at `0 */2`, colliding with
    self-improvement); superbot flagged ⚠ arm (no live failsafe). **Seat
    re-arm ORDERs are the manager's follow-up, not part of this restamp.**
14. **[P2-14] I-44 case-duplicate resolved** — `docs/capabilities.md`
    (lowercase, the old fleet manifest) folded into the kit-owned
    `docs/CAPABILITIES.md` (below the kit fence, own section); a pointer stub
    left at the lowercase path so old links resolve.
15. **[P2-15] LANDING-splice evidence n≥2** — all 8 startups' LANDING line
    citation upgraded: "(relayed = denied — recorded denials n≥2, fm
    docs/CAPABILITIES.md append log)" (delta 3's record is the second data
    point; no doctrine change).
16. **[P2-16] planned-routes CSRF-floor row — WATCH, no edit** (promotable to
    a websites durable doc once websites PR #159 lands).

**PR #121 v1.1-delta dedup** (game-lab consolidation plan, 8 candidates,
verified against HEAD before disposition): #1 canonical merge clause =
duplicate of delta 1 + the standing park-green/PERMISSIONS text; #4 isolated
clone per worker = already in v3.3 GIT HYGIENE ("workers run in FRESH
clones/worktrees"); #6 verify external-bot claims = already Q-0120; #8
verify-via-list_triggers-not-snapshot = already BOOT 4 + D-9 + verify-after-arm.
**Applied as an additional v3.4 delta:** #5 registry-meta restamp duty → fm
startup WORK SOURCES (b): a `projects/<seat>/meta.md` claim contradicted by
the seat's live heartbeat is drift — restamp it (meta-lag class; fm PR #116
precedent). **Deferred:** #2 pacemaker queue-behind-busy-session doctrine
(platform-behavior claim, not verifiable against repo state from this seat);
#3 WAIT-FOR-BASE pre-build pattern (seat-local workflow pattern, evidence
lives in gba session records — v3.5 candidate); #7 archive checklist
trigger-disarm rule (durable home is the consolidation plan/playbook; #121 has
since merged to main and is superseded by
`docs/planning/2026-07-12-repo-consolidation-plan.md`, which carries that
checklist).

**Registry:** every projects/<seat>/ artifact re-synced and version-bumped by
one (fm v6/v6/v6 · websites v6/v5/v5 · venture-lab v5/v6/v5 · the other five
v4/v4/v4); stamps in the regen tool's SEATS block.

## v3.3 changelog — seat-first keyword-dictionary CIs + expanded startups (owner spec 2026-07-12)

**Owner spec (live, 2026-07-12, overnight prompt rebuild):** the v3.2
assembled CI (core-dominant, ~12% seat share) is what the owner rejected;
v3.3 rebuilds the CI on the deployed v2 style — seat-first, the owner's
five-section skeleton — as a **compression dictionary/routing layer**, and
the startup prompts lose their char cap and **EXPAND to carry the universal
doctrine verbatim**. Applied in one integration pass:

1. **CI: one authored file per seat** (`<seat>-custom-instructions.md`
   replaced in place — the seat C blocks became the full artifacts). The
   core+seat-block assembly is retired; `../custom-instructions-core.md` is
   marked superseded-as-assembly-source and kept as routed reference
   doctrine (its rider block frozen @ 95b5c8f — the dictionaries' `CORE`
   alias). Every dictionary route target verified on disk at seat-repo
   HEADs 2026-07-12; stopgap routes tracked in
   [`../planned-routes.md`](../planned-routes.md).
2. **Startups: authored expanded files** (v3.2 procedure text byte-verbatim
   outside four documented splices: WORK-LOOP pointer, LANDING pointer,
   GEN-3+TRUTH pointer paragraph → full DOCTRINE section, stamp line). New:
   YOUR SEAT section (repos/stack, CI checks by exact name, per-repo MERGE
   MECHANICS, walls, CAPABILITIES discovery, full born-red card mechanics),
   ROUTINE-FIRED probe-landing-tools protocol (WS-1 fleet-wide), DOCTRINE
   in full (grant VERBATIM from `projects/UNIVERSAL.md`, nine QA riders),
   HEARTBEAT `kit:` line grammar + six-field asks, SESSION ENDER inlined.
   `../universal-startup.md` marked superseded-as-generation-source.
3. **BOOT TRIAD (Q-0270, owner directive relayed live 2026-07-12):** BOOT
   step 0 in every startup + a dictionary keyword in every CI — state model
   (family-level) + venue + ability envelope; autonomous sessions pre-route
   around known stall classes and park only on a REAL denial, never
   preemptively; owner-live sessions assume no special limitations (Q-0269).
4. **v3.2 defect queue CLOSED:** #7 fresh-session-per-fire (BOOT 4 EXCEPTION
   + ender step 3(b)), #8 `kit:` line grammar (HEARTBEAT section + CI kit
   gate entry), #9 MCP PR-read staleness (TOOL FACTS rider extension + CI
   TOOL FACTS clause).
5. **Ender v3.3** (`../session-ender.md`): step 3(b) fresh-session-per-fire
   clause; now also INLINED in every startup — D stays canonical, drift
   class **D-10** minted (checker verifies every inlined copy).
6. **Tooling** (`../tools/regen_b_files.py`): generation/assembly modes
   REMOVED (they would clobber the authored v3.3 files); default run = CI
   hard-cap gate + drift checks (ender D-10, grant vs UNIVERSAL.md, doctrine
   identity, card-block + triad identity, stamps, failsafe extraction);
   `--check-registry` / `--write-registry` kept — registry failsafe bodies
   now derive from each startup's own BOOT 3a text.
7. **Thorough boot verification preferred (owner doctrine, live 2026-07-12):**
   BOOT 2 in every startup now states it explicitly — current state moves
   fast, so a fresh-looking baton NARROWS the search but never substitutes
   for verification; re-verify every claim you act on at live HEAD, even
   when the handoff reads current. Checker-enforced as a shared block; a
   16-file sweep found NO skip-tempting wording to neutralize (both grep
   hits were pro-verification or unrelated).
8. **UNIVERSAL.md grant sha reconciled:** the true last-touch commit of
   `projects/UNIVERSAL.md` is **16161af** (v4, 2026-07-11; `e1848ff` is its
   PR #76 merge commit with identical content, `e801da5` is a later
   kit-bump commit that did not touch the file — both stale citations).
   v3.3 artifacts stamp `UNIVERSAL v4@16161af`; the core file's internal
   `e801da5` citation is part of the frozen v3.1 reference block and was
   left untouched.

## v3.2 changelog — stateless rebuild (owner correction 2026-07-12)

**Owner correction (live, 2026-07-12): startup prompts must never contain
volatile state** — no concrete PR numbers, no SHA/CI colors, no trigger ids
asserted as facts, no "do X now" execute items. Prompts direct agents to the
repo documents where current state lives. Applied to all 9 startup artifacts
(A + the 8 B files; D audited — already stateless, stamp bumped) in one pass:

1. **A template** (`../universal-startup.md` → v3.2): STATELESS sentence in
   the role brief; `{{OLD_TRIGGER_IDS}}` slot replaced by
   `{{OLD_TRIGGER_SOURCES}}` (fills name records, never ids); the LANDING
   "fm PR #99 / HYPOTHESIS n=1" citation and the GEN-3 "rider v5 @ 76d854d;
   grant v4 @ e801da5" SHAs dropped for durable pointers. Drift class **D-9**
   minted (stateless rule; enforced at regen review, header-documented).
2. **Every seat's FIRST WORK ORDERS → a WORK SOURCES ladder** — (a)
   `control/inbox.md` at HEAD, (b) the seat's named state docs (all verified
   to exist at that repo's HEAD 2026-07-12: fm docs/{owner-queue,roster,
   fleet-triage}.md · superbot-next docs/status/README-first.md ·
   websites docs/owner/OWNER-ACTIONS.md + docs/current-state.md · kit
   docs/adopters.md · per-repo control/status.md + docs/current-state.md for
   world/game-lab/venture/ideas — zero gaps found, so no heartbeat-fallback
   pointer was needed), (c) the standing mission.
3. **Durable rails KEPT** (mission, not state): game-lab track isolation +
   R22 + proof rails verbatim; "security fix on the auth/login path merges
   BEFORE anything secrets-adjacent" as a standing ORDERING rule (PR number
   removed); trading research-only rail verbatim; venture merge-path rail
   (evidence PR numbers removed).

**Relocations — still-valid now-actions filed as inbox ORDERs (verified at
the owning repo's HEAD first):**

| Owning repo | ORDER | Relocated action | Verification (2026-07-12) |
|---|---|---|---|
| superbot-mineverse | 003 | land the login-CSRF PR #42 (non-author review-merge, ONE attempt), then disposition #31, re-render CLAUDE.md | #42 OPEN, mergeable_state clean @ head `2557f1a`; #31 OPEN (codex, blocked) |
| superbot-idle | 003 | add pytest CI on PR+push; ⚑ owner mark required | `.github/workflows/` @ `c6a349d` = substrate-gate.yml + theme-gate.yml only — no pytest job |
| superbot-games | 005 | truth-stamp the heartbeat ONCE (archival correction) | status updated 2026-07-11T19:39:14Z claims 5 open parked PRs + HEAD `5d38593`; live: #50 MERGED 2026-07-11T20:25:22Z, main = `5ddfbee` |
| pokemon-mod-lab | 006 | add .gitignore (`*.gba`, `*.sav`, `baserom*`) | no `.gitignore` at origin/main `08d2611` |
| superbot-next | 014 | seed superbot-plugin-hello + flip ORDER 002 via status.md | repo EMPTY (API 409 "Git Repository is empty"); status @ 07:55Z: 002 acked, NOT in `done=` |
| superbot-next | 015 | render CLAUDE.md from .substrate/claude/ + fix AGENT_ORIENTATION dead pointer | no `.claude/CLAUDE.md` at `c03df80`; `docs/AGENT_ORIENTATION.md:10,:34` point at it; source exists at `.substrate/claude/CLAUDE.md` |
| websites | 012 | reconcile status/OWNER-ACTIONS vs live + re-render CLAUDE.md + bake-ask truth | status @ HEAD still lists #141 "awaiting owner squash-merge" — #141 MERGED 2026-07-11T20:24:48Z; `.claude/CLAUDE.md:40` says "Three… services" + `:47` two-suite verify while `review/` exists at `8f97654`; review-bake 2/2 runs FAILED incl. the first `schedule` fire 29184552812 @ 2026-07-12T07:38Z (v3.1's "cron NEVER fired" is itself stale) |
| websites | 013 | CSRF/Origin check + rate-limit on app/owner.py POST routes | `app/owner.py` @ `8f97654`: zero csrf/origin hits |
| venture-lab | 007 | re-verify + ⚑-escalate the open-PR dispositions (owner-only photo-exposure PR; parked launch-packet PR) | #51 OPEN ("Add files via upload", since 2026-07-11T18:24Z); #57 OPEN, label do-not-automerge, park-owner-merge |
| trading-strategy | 011 | land #64 (non-author review-merge) + #65 per doctrine; verify the weekly grading executor before 2026-07-17 | #64 OPEN, #65 OPEN; grading trigger `trig_015aNMg5…` present in fm telemetry snapshot + documented bound to the live Money-seat coordinator (PR #64 body) |
| substrate-kit | 015 | fix the AGENT_ORIENTATION.md.tmpl dead boot pointer class (+ gate-integrity verify-first rider) | tmpl:8-12,:32-36 @ `8a544a6` point at `.claude/CLAUDE.md`; superbot-next confirmed shipping without one |
| sim-lab | 003 | stand up a GITHUB_TOKEN merge-on-green workflow (landing path) | `.github/workflows/` @ `e857b24` = substrate-gate.yml only |

**Dead / already-done v3.1 items (no ORDER filed; evidence):** superbot F2 —
#196/#206 CLOSED-unmerged, #213/#217 MERGED (API-verified); venture #58
CLOSED-unmerged; ideas order 1 — `sims/verdict-012-doc-cite-checker-spec/`
exists @ sim-lab `e857b24` and the chain has moved on (PROPOSAL 011
sim-ready, verdict-013 landed): handoff closed; game-lab W1 card-convention —
`.sessions/README.md` with the model-line doctrine at HEAD in both repos;
game-lab W2 required-check click-asks — already durable in fm
docs/owner-queue.md (items 5/6); kit order 1 registry-truth — overtaken:
docs/adopters.md regenerated 2026-07-11T22:36:49Z from per-repo tree
evidence with DRIFT rows; fm parked stack — #88/#89/#91 terminal (not in
open PRs), #92 OPEN parked and recorded in control/status.md; v3.1 baked
cutover trigger ids (gba/pml hourly, retro-games, games ORDER-015, idle,
fm prior failsafe) — ALL absent from `telemetry/triggers-snapshot.json`
(783 triggers, 2026-07-12): nothing to delete; kit #220/#238 ratification
parks — OPEN, and already durably recorded in kit control/status.md ⚑ 14/15.
