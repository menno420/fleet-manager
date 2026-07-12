# fleet-manager · status

updated: 2026-07-12T18:55:00Z — trigger-health remediation wake (PR #135): fresh snapshot, PASS 6/6, BEFORE failures self-resolved.

phase: **prompt program COMPLETE through v3.3.** Owner-corrected generations: v3.2 stateless (#108) → registry sync (#110) → **v3.3 three-layer (#111 @ `98d0f68`)**: expanded startup prompts (~27k), keyword-dictionary Custom Instructions ≤8,000 chars dual-basis, BOOT TRIAD (superbot Q-0270), boot-verification doctrine, `docs/prompts/v3/planned-routes.md`, drift checks incl. registry match 24/24.

health: green

kit: v1.7.0 · check: green · engaged: yes

coordinator: **LIVE — session_01FMJoC5uC6WSUTosceTGcmo (continuous operation).**

routine: failsafe **trig_01BKpsyoBzp1K1ob9H3iu1gM** cron "30 */2 * * *" live (verified earlier today, 2026-07-12); pacemaker send_later chain active; arming path = worker-relay recipe (spawned worker calls send_later / create_trigger, binds to parent session).

registry: projects/\<seat\>/ — all 8 standing seats serve **v3.3 @ `48650f8` stamps**; control website reads projects/ on main live (websites `app/projects.py`, 180s cache).

sweep: **midday staleness sweep (PR #113, ~11:17–11:25Z): 6 FRESH / 2 STALE seats** (superbot-world 3/3 STALE — worsened; game-lab new STALE via pokemon-mod-lab). Trigger snapshot re-captured: **832 triggers** (28 enabled: 9 crons + 19 one-shots) → `telemetry/triggers-snapshot.json`; roster regenerated **gen 14**. Full report: `docs/research/2026-07-12-staleness-sweep-midday.md` (9-item needs-attention shortlist).

trigger-health: **remediation wake (PR #135): PASS 6/6, exit 0** (evaluated 18:44Z against the fresh export). Fresh 941-record snapshot (10 pages, captured_at 2026-07-12T18:25:51Z, 0 dupes) committed with top-level `captured_at` per the ORDER 020 recipe (telemetry/README.md). The 11:12Z BEFORE failures all self-resolved between 11:12Z and the 18:25Z capture — no `send_message` recovery needed: game-lab failsafe `trig_01JD1t7rD5jUCqkJQJaNCi3E` live (last_fired 16:50:26Z, next 18:50Z); both dead chains (`session_014Z1fPG7Wa6VHprJqLcux4f`, `session_01SphTJEnN1PYjYZhHNWoJik`) have future ticks armed. LANES gained a game-lab registry-only row (`gen_roster.py`); roster regenerated gen-19. FLAG: I1 blind spot — `trig_011XAWqPeksS8LBrS5G9RvVc` (superbot autonomous dispatch, cron, next_run_at 10d past) is skipped because the export omits the `enabled` field on disabled routines and `gen_roster.trigger_wedged` (scripts/gen_roster.py:409) treats absent-`enabled` as disabled — correct for a user-paused routine, but the checker cannot distinguish "paused" from "enabled-field missing", so a truly-enabled record lacking the field would be silently unflagged (917/941 records lack `enabled`).

## Walls

Walls (summarized): agent-initiated merges of peer PRs are denied in auto mode; permission-guard edits require live user intent in the acting session; standalone sleep blocked; direct push to main blocked (GH013).

## Landed / parked

Landed today (2026-07-12), by PR:

- **#88/#89/#91** — restructure chain.
- **#97** — coordinator heartbeat (status.md overwrite).
- **#92** — permission grants port (.claude/settings.json).
- **#93–#96** — research wave (platform capabilities, problem census core + satellites, prompt architecture).
- **#100–#102** — QA passes.
- **#98** — prompts v3 draft; **#103** — v3.1 + codex fixes.
- **#99/#104/#109** — roster regens.
- **#105** — staleness sweep (first 8-seat registry sweep).
- **#106/#107** — owner-queue re-stamp + kit ORDER 014 triage.
- **#108** — prompts v3.2 (stateless startup artifacts).
- **#110** — registry sync (projects/ regenerated from v3.2).
- **#111** — prompts v3.3 (three-layer generation) @ `98d0f68`.
- **substrate-kit:** ORDER 014 delivered (kit #254/#256) + ORDER 015 filed.
- **12 relocated ORDERs** merged across 10 lane repos (v3.2 relocation program).

Open: this session's PR only (#133 — ORDER 020 trigger-health check; #113 merged). No other open PRs in fleet-manager.

## Orders

- inbox 001–018 all DONE.
- **ORDER 020 DONE (PR #133)** — per-wake trigger-health check: `scripts/check_trigger_health.py` (R26, 6 invariants, nonzero exit on FAIL) + roster "Trigger health" column/section (`scripts/gen_roster.py`) on the Actions regen substrate + `captured_at` snapshot convention (`telemetry/README.md`) + wake-prompt wiring (v3 per-project + registry copies). DONE flip appended to inbox per grammar.
- ORDERs 019 / 021 / 022: Websites-seat orders — not this repo's to execute; tracked via the roster/heartbeat sweep.
- owner-directed overnight prompt-rebuild program (2026-07-11): COMPLETE through v3.3 (see phase line).

next-2: (1) monitor lane boots on the v3.3 prompts; (2) kit skills-program alignment for `docs/prompts/v3/planned-routes.md`.

## ⚑ needs-owner

Pointers only (details in `docs/owner-queue.md`):

- owner-queue C#34–C#36 — pastes now serve v3.3.
- owner-queue E#37 — forge disposition.
- OQ-FM-ACTIONS-PR-PERMISSION — Actions PR-permission toggle.
- venture-lab exposure item (see owner-queue).
