> **Status:** `reference`

<!-- v3.3 · 2026-07-12 · provenance: owner spec 2026-07-12 (overnight prompt rebuild — CI becomes a per-seat keyword dictionary; startups EXPAND, no char cap; see the v3.3 changelog section below). Prior: v3.2 (stateless correction) · v3.1 (research PRs #93/#95 + owner baseline + QA PRs #100/#101/#102, applied in PR #103) -->
<!-- char-count: planning doc, no paste budget applies -->

# Per-project prompts — v3.3 (per-seat Custom Instructions + expanded startups)

v3.3 composition (owner spec 2026-07-12 — supersedes the v3.2 generated/
assembled model):

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
  byte-identical across all 8 after normalizing the one status-grammar
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

## The 8 seats (owner restructure 2026-07-11)

Unchanged from v3.0: Fleet Manager · SuperBot 2.0 (superbot + superbot-next) ·
Websites · Self Improvement (substrate-kit) · SuperBot World (games + idle +
mineverse) · Game Lab (gba-homebrew + pokemon-mod-lab) · Ideas Lab
(idea-engine + sim-lab) · Venture Lab (venture-lab + trading-strategy).

**Not seats:** product-forge (⚑ awaits owner disposition; if seated it becomes
seat 9 via this same recipe — stagger slot below), codetool-lab-* (DARK),
superbot-plugin-hello (helper, folded into SuperBot 2.0's F1).

## v3.3 size table (real counts, checker-verified 2026-07-12 — `../tools/regen_b_files.py`)

Hard cap: **Custom Instructions ≤ 8,000 chars** (verified console wall; aim
≤7,500 — every seat runs over the aim BY DESIGN: the owner's mandated keyword
set outranks the fitted target, same call as v3.2's safety-over-fitted).
UTF-8 bytes also gated ≤ 8,000 for all 8 by the checker (belt-and-braces;
the fleet budget basis is characters). **Startups have NO cap** — sizes below are a NOTE, not a
gate (owner spec 2026-07-12). The session ender is a chat paste (no console
cap).

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

| Seat | cron | Slot | Provenance |
|---|---|---|---|
| self-improvement | `0 */2 * * *` | even :00 | v3.0, kept |
| game-lab | `15 */2 * * *` | even :15 | baseline kept |
| fleet-manager | `30 */2 * * *` | even :30 | census-verified |
| websites | `45 */2 * * *` | even :45 | baseline kept |
| superbot | `0 1-23/2 * * *` | odd :00 | v3.0, kept |
| superbot-world | `15 1-23/2 * * *` | odd :15 | v3.0, kept |
| ideas-lab | `30 1-23/2 * * *` | odd :30 | v3.0, kept |
| venture-lab | `45 1-23/2 * * *` | odd :45 | v3.0, kept |

Seat-9+ slots: `5/20/35/50` past the hour (even parity first). **The fleet
manager is the slot arbiter** — a seat NEVER re-slots itself; a foreign trigger
on your slot is reported in status, and slot changes are a registry edit here
(question-rounds R5-Q5). Known transients until cutovers complete (replay C-9;
**re-verified 2026-07-12 against `telemetry/triggers-snapshot.json`**): the
pre-merge gba/pml hourly wakes and the retro-games trigger are **ABSENT from
the snapshot** (already gone — nothing left to delete); the old ideas-lab
failsafe (`0 */2`, squatting the self-improvement slot) is **still present**
(Ideas Lab's cutover deletes it, after confirming the prior coordinator chat
is archived). Venture-lab's grading BUSINESS cron (`0 9 * * 5`) does not
collide and is rebound-never-deleted (A step 4). Since v3.2, NO trigger id is
baked into any prompt — cutover ids come from heartbeats + the telemetry
snapshot (D-9).

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
  line), I-44 CAPABILITIES/capabilities case-duplicate (repo cleanup, routed
  to the fm seat's sweep), I-58's remaining auto-merge race classes
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
