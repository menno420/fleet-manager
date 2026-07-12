> **Status:** `reference`

<!-- v3.1 · 2026-07-12 · provenance: v3.0 plan (research PRs #93/#95 + owner baseline 2026-07-11) + the v3.1 QA-fix build (QA PRs #100 incident-replay / #101 question-rounds / #102 boot-sim; applied in PR #103) -->
<!-- char-count: planning doc, no paste budget applies -->

# Per-project prompts (artifact B + seat C blocks) — v3.1

v3.1 composition (supersedes the v3.0 hand-drafting recipe): every
**`<seat>-startup.md`** (artifact B) is **GENERATED** from `../universal-startup.md`
(A) by **`../tools/regen_b_files.py`** — slot fills + a FIRST WORK ORDERS insert
+ ONE scripted transform (A's self-referential "Unfilled {{slots}}" sentence is
dropped from every B — in a generated B every slot is filled) are the only
non-A-verbatim bytes; everything else is A-verbatim, and each B header
carries the sha1 of the A body it was generated from. **Never hand-edit a B
file** (drift class D-1, PR #100): edit A or the seat config in the script,
then rerun it. Each **`<seat>-custom-instructions.md`** carries the seat C
block; CONTROL BUS is core-owned in v3.1 (D-4 retired) — a seat block only
supplies the `{{STATUS_GRAMMAR}}` fill declared in its header.

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

## v3.1 budget table (real counts, regen-verified 2026-07-12; FILLED values)

Hard caps: startup ≤ 8,000 · assembled CI ≤ 8,000 — **all 20 within hard**.
**Assembled CI is counted with `{{SEAT_NAME}}` + `{{STATUS_GRAMMAR}}` FILLED**
(Codex PR #103 review: the raw-placeholder count under-measured every paste by
the fill delta and let 3 seats silently exceed 8,000 — never count a paste
with placeholders in it). Fitted target 7,500: the universal artifacts fit;
**every B file and assembled CI runs over fitted, flagged in its header** —
the QA fix volume (12 P0s, 3 BLOCKERs, 12 contradictions) does not fit under
7,500 without dropping safety rules, and the mission ranks safety over the
fitted target.

| Artifact | Chars | vs fitted 7,500 / hard 8,000 |
|---|---:|---|
| A universal-startup (body) | 6,373 | n/a (template; skeleton budget ≤ ~6,600) |
| C universal core (CORE-START/END) | 6,996 raw · 6,992–7,031 filled per seat | seat-block hard budget = 8,000 − FILLED core |
| D session-ender (body) | 3,411 | chat paste — console cap n/a; over its ~2,000 prose budget BY DESIGN (P0 ender fixes), flagged in-file |
| Seat | Startup B | Seat block C | Assembled CI (filled core + block) | Status |
| fleet-manager | 7,796 | 975 | 7,972 | under hard, over fitted — flagged |
| superbot | 7,993 | 984 | 7,994 | under hard, over fitted — flagged |
| websites | 7,967 | 951 | 7,943 | under hard, over fitted — flagged |
| self-improvement | 7,958 | 992 | 7,992 | under hard, over fitted — flagged |
| superbot-world | 7,966 | 966 | 7,997 | under hard, over fitted — flagged |
| game-lab | 7,997 | 971 | 7,984 | under hard, over fitted — flagged |
| ideas-lab | 7,952 | 980 | 7,992 | under hard, over fitted — flagged |
| venture-lab | 7,998 | 990 | 7,998 | under hard, over fitted — flagged |

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
(question-rounds R5-Q5). Known transients until cutovers complete (replay C-9):
the pre-merge gba/pml hourly wakes fire at :00/:30 every hour (Game Lab's
cutover deletes them), and the old ideas-lab failsafe (`0 */2`) squats the
self-improvement slot (Ideas Lab's cutover deletes it). Venture-lab's grading
BUSINESS cron (`0 9 * * 5`) does not collide. Trigger-delete ownership
tiebreak: retro-games trig_01Y99uDKNtKTz2EtRYPWZkGY belongs to **Game Lab's**
cutover; the fm delete list defers it (C-9's double-assignment resolved).

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

**§(a)/(b) coverage gaps — REAL v3.2 queue entries:**

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
