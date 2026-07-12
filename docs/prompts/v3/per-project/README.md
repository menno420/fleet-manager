> **Status:** `reference`

<!-- v3.1 · 2026-07-12 · provenance: v3.0 plan (research PRs #93/#95 + owner baseline 2026-07-11) + the v3.1 QA-fix build (QA PRs #100 incident-replay / #101 question-rounds / #102 boot-sim; applied in PR #103) -->
<!-- char-count: planning doc, no paste budget applies -->

# Per-project prompts (artifact B + seat C blocks) — v3.1

v3.1 composition (supersedes the v3.0 hand-drafting recipe): every
**`<seat>-startup.md`** (artifact B) is **GENERATED** from `../universal-startup.md`
(A) by **`../tools/regen_b_files.py`** — slot fills + a FIRST WORK ORDERS insert
are the only per-seat bytes; everything else is A-verbatim, and each B header
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

## v3.1 budget table (real counts, regen-verified 2026-07-12)

Hard caps: startup ≤ 8,000 · assembled CI ≤ 8,000 — **all 20 within hard**.
Fitted target 7,500: the universal artifacts fit; **every B file and assembled
CI runs over fitted, flagged in its header** — the QA fix volume (12 P0s, 3
BLOCKERs, 12 contradictions) does not fit under 7,500 without dropping safety
rules, and the mission ranks safety over the fitted target.

| Artifact | Chars | vs fitted 7,500 / hard 8,000 |
|---|---:|---|
| A universal-startup (body) | 6,496 | n/a (template; skeleton budget ≤ ~6,600) |
| C universal core (CORE-START/END) | 6,996 | leaves ≤ 1,004 seat-block hard budget |
| D session-ender (body) | 3,300 | chat paste — console cap n/a; over its ~2,000 prose budget BY DESIGN (P0 ender fixes), flagged in-file |
| Seat | Startup B | Seat block C | Assembled CI | Status |
| fleet-manager | 7,798 | 975 | 7,971 | under hard, over fitted — flagged |
| superbot | 7,958 | 991 | 7,987 | under hard, over fitted — flagged |
| websites | 7,969 | 951 | 7,947 | under hard, over fitted — flagged |
| self-improvement | 7,960 | 992 | 7,988 | under hard, over fitted — flagged |
| superbot-world | 7,968 | 1,002 | 7,998 | under hard, over fitted — flagged |
| game-lab | 7,999 | 971 | 7,967 | under hard, over fitted — flagged |
| ideas-lab | 7,954 | 980 | 7,976 | under hard, over fitted — flagged |
| venture-lab | 8,000 | 1,004 | 8,000 | AT hard cap exactly, over fitted — flagged |

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
