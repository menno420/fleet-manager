# fleet-manager · status

updated: 2026-07-12T11:37:32Z — midday staleness sweep landed (PR #113).

phase: **prompt program COMPLETE through v3.3.** Owner-corrected generations: v3.2 stateless (#108) → registry sync (#110) → **v3.3 three-layer (#111 @ `98d0f68`)**: expanded startup prompts (~27k), keyword-dictionary Custom Instructions ≤8,000 chars dual-basis, BOOT TRIAD (superbot Q-0270), boot-verification doctrine, `docs/prompts/v3/planned-routes.md`, drift checks incl. registry match 24/24.

health: green

kit: v1.7.0 · check: green · engaged: yes

coordinator: **LIVE — session_01FMJoC5uC6WSUTosceTGcmo (continuous operation).**

routine: failsafe **trig_01BKpsyoBzp1K1ob9H3iu1gM** cron "30 */2 * * *" live (verified earlier today, 2026-07-12); pacemaker send_later chain active; arming path = worker-relay recipe (spawned worker calls send_later / create_trigger, binds to parent session).

registry: projects/\<seat\>/ — all 8 standing seats serve **v3.3 @ `48650f8` stamps**; control website reads projects/ on main live (websites `app/projects.py`, 180s cache).

sweep: **midday staleness sweep (PR #113, ~11:17–11:25Z): 6 FRESH / 2 STALE seats** (superbot-world 3/3 STALE — worsened; game-lab new STALE via pokemon-mod-lab). Trigger snapshot re-captured: **832 triggers** (28 enabled: 9 crons + 19 one-shots) → `telemetry/triggers-snapshot.json`; roster regenerated **gen 14**. Full report: `docs/research/2026-07-12-staleness-sweep-midday.md` (9-item needs-attention shortlist).

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

Open: **PR #113 only** — midday staleness sweep (research doc + 832-trigger snapshot + roster gen 14 + this heartbeat); #112 merged at `d4989c9` 11:06Z. No other open PRs in fleet-manager.

## Orders

- inbox 001–018 all DONE.
- owner-directed overnight prompt-rebuild program (2026-07-11): COMPLETE through v3.3 (see phase line).

next-2: (1) monitor lane boots on the v3.3 prompts; (2) kit skills-program alignment for `docs/prompts/v3/planned-routes.md`.

## ⚑ needs-owner

Pointers only (details in `docs/owner-queue.md`):

- owner-queue C#34–C#36 — pastes now serve v3.3.
- owner-queue E#37 — forge disposition.
- OQ-FM-ACTIONS-PR-PERMISSION — Actions PR-permission toggle.
- venture-lab exposure item (see owner-queue).
