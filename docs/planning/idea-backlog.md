# Session-card idea backlog — GENERATED

> **Status:** `audit`
>
> **GENERATED — do not hand-edit; regenerate with `python3 scripts/gen_idea_backlog.py`.** NOT SOURCE OF TRUTH — the
> source cards (`.sessions/*.md`) and the planning docs' groom
> sections win. Groomed-detection is a token-overlap heuristic
> (Q-0105 unverified tier — see the script header).
>
> generated-at 2026-07-19T20:17:45Z
>
> 45 idea block(s) across 244 card(s) · 4 ungroomed · 4 ungroomed older than 2d.

| Card date | Source card | Idea | Groom status |
|---|---|---|---|
| 2026-07-19 | `2026-07-19-fm-volatile-drift.md` | close the volatile-refresh loop: emitter `--from-export` + verifier prints the paste-ready fix | groomed → `overnight-menu-2026-07-17.md` |
| 2026-07-19 | `2026-07-19-fm-roster-cron-resilience.md` | `scripts/gen_hub_queue_baton.py` — derive the night-watch "hub queue" baton line live inst… | groomed → `2026-07-19-next-slices.md` |
| 2026-07-19 | `2026-07-19-fm-regen-skip-detector.md` | regen run-history probe (`--probe-runs`) to name the drop's cause | groomed → `2026-07-19-next-slices.md` |
| 2026-07-19 | `2026-07-19-fm-r30-check.md` | `r30_merge_check --post` — write the merge record automatically | groomed → `2026-07-19-next-slices.md` |
| 2026-07-19 | `2026-07-19-fm-planning-groom.md` | a `gen_idea_backlog.py` harvester. This planning pass had to hand-grep ~25 session cards f… | groomed → `2026-07-19-next-slices.md` |
| 2026-07-19 | `2026-07-19-fm-morning-records.md` | + the 2026-07-18/19 cards'  sets (lane-liveness, tripwire-checker, idea-harvester, regen-w… | groomed → `2026-07-19-next-slices.md` |
| 2026-07-19 | `2026-07-19-fm-lane-liveness.md` | machine-readable seat coverage (`covers:` field on registry-only LANES entries) | groomed → `2026-07-19-next-slices.md` |
| 2026-07-19 | `2026-07-19-fm-label-hygiene.md` | workflow-sourced park-label vocabulary | groomed → `2026-07-19-next-slices.md` |
| 2026-07-19 | `2026-07-19-fm-i8-provenance.md` | consult the owning lane's heartbeat `routine-claims` fence directly | groomed → `2026-07-19-next-slices.md` |
| 2026-07-19 | `2026-07-19-fm-fence-emitter.md` | volatile-field drift check in `verify_routine_state.py` | groomed → `2026-07-19-next-slices.md` |
| 2026-07-19 | `2026-07-19-fm-capabilities-linter.md` | graduate the CAPABILITIES checker pair (S9 `check_capabilities_wall_age.py` + this grammar linter) into substrate-kit as kit-owned checkers | groomed → `overnight-menu-2026-07-17.md` |
| 2026-07-19 | `2026-07-19-fm-adopt-r30.md` | `scripts/r30_merge_check.py` — mechanize the R30 3-point verification | groomed → `2026-07-19-next-slices.md` |
| 2026-07-19 | `2026-07-19-fm-18z-cycle.md` | wake-without-work detector | groomed → `2026-07-19-next-slices.md` |
| 2026-07-19 | `2026-07-19-fm-14z-cycle.md` | classifier-safe naming convention for local-only writer scripts | groomed → `2026-07-19-next-slices.md` |
| 2026-07-19 | `2026-07-19-fm-06z-snapshot.md` | seat-provenance-aware I8 remedy in `check_trigger_health.py` | groomed → `2026-07-19-next-slices.md` |
| 2026-07-19 | `2026-07-19-fm-06z-morning.md` | consecutive failsafe windows with zero landed output | groomed → `2026-07-19-next-slices.md` |
| 2026-07-17 | `2026-07-17-fresh-start-cleanup.md` | ship `scripts/check_owner_queue_size.py` — a stdlib-only advisory that reds when `docs/own… | groomed → `overnight-menu-2026-07-17.md` |
| 2026-07-16 | `2026-07-16-trigger-snapshot-pm.md` | teach `check_trigger_health.py` I8 DUPLICATE-CRON a *cutover-window* grace: when two enabl… | groomed → `overnight-menu-2026-07-17.md` |
| 2026-07-16 | `2026-07-16-sweep-stale-claim.md` | give the claims checker a `claims-terminal-lane` signal — resolve each claim's backticked … | groomed → `overnight-menu-2026-07-17.md` |
| 2026-07-16 | `2026-07-16-recreation-runbook-0716.md` | A `scripts/check_orphan_triggers.py` that diffs a fresh `list_triggers` export against the… | groomed → `overnight-menu-2026-07-17.md` |
| 2026-07-16 | `2026-07-16-r26-trigger-tooling.md` | binding-aware | groomed → `2026-07-19-next-slices.md` |
| 2026-07-16 | `2026-07-16-pr-audit-0716.md` | ship `scripts/classify_open_prs.py` — a stdlib-only classifier that, given a directory of … | groomed → `2026-07-19-next-slices.md` |
| 2026-07-16 | `2026-07-16-morning-wake-triage.md` | 2.6 MB per commit | groomed → `overnight-menu-2026-07-17.md` |
| 2026-07-16 | `2026-07-16-fm-wake-jul16.md` | ship `scripts/assemble_triggers_snapshot.py` — the R26 export is currently ~20 hand-driven… | groomed → `overnight-menu-2026-07-17.md` |
| 2026-07-15 | `2026-07-15-wake-1126z-queue-sweep.md` | I9 heartbeat-vs-registry coherence invariant | **ungroomed** ⚠ >2d |
| 2026-07-15 | `2026-07-15-triggers-snapshot-refresh-2.md` | the final-page inline gap above is a standing footgun for every snapshot refresh — a small… | groomed → `2026-07-14-central-docs-plan.md` |
| 2026-07-15 | `2026-07-15-session-ender-handoff.md` | ender-coherence guard | groomed → `2026-07-14-central-docs-plan.md` |
| 2026-07-15 | `2026-07-15-roster-regen-0810.md` | `scripts/seat_delta.py --since <ISO>` — the re-sweep slices (04:01Z, 05:39Z, 08:12Z today … | groomed → `overnight-menu-2026-07-17.md` |
| 2026-07-15 | `2026-07-15-retire-c61.md` | owner-queue asks born from a *seat-state* wall (STANDBY, trigger-less, quiet) should carry… | groomed → `overnight-menu-2026-07-17.md` |
| 2026-07-15 | `2026-07-15-registry-v3-5-synthesis.md` | index-generation sync guard | groomed → `overnight-menu-2026-07-17.md` |
| 2026-07-15 | `2026-07-15-queue-a63-next-triage.md` | parked-rail probe | groomed → `2026-07-19-next-slices.md` |
| 2026-07-15 | `2026-07-15-owner-queue-kit-go.md` | silently-stalled-seat probe | groomed → `2026-07-19-next-slices.md` |
| 2026-07-15 | `2026-07-15-oversight-wake-1659.md` | delta-export mode | groomed → `overnight-menu-2026-07-17.md` |
| 2026-07-15 | `2026-07-15-oversight-wake-0715b.md` | `revisit-by:` token for dated fleet-triage verdicts | groomed → `overnight-menu-2026-07-17.md` |
| 2026-07-15 | `2026-07-15-oversight-wake-0715.md` | `check_owner_queue.py` now probes PR state live but the *session* venue always degrades to… | **ungroomed** ⚠ >2d |
| 2026-07-15 | `2026-07-15-merge-on-green-verify-0715.md` | ship a minimal CI gate when the target repo has zero workflows | groomed → `2026-07-14-central-docs-plan.md` |
| 2026-07-15 | `2026-07-15-lanes-regen-fix.md` | generation-parity guard — teach `scripts/check_roster_freshness.py` (or the strict gate) t… | **ungroomed** ⚠ >2d |
| 2026-07-15 | `2026-07-15-fleet-oversight-evening.md` | seat-staleness checker with seat-side-signal classification — a `scripts/check_seat_stalen… | groomed → `overnight-menu-2026-07-17.md` |
| 2026-07-15 | `2026-07-15-cr-disposition-sweep.md` | teach `scripts/gen_roster.py` (or a small sibling `scripts/reboot_sweep.py`) a `--since <t… | groomed → `2026-07-19-next-slices.md` |
| 2026-07-15 | `2026-07-15-card-modelline-groom.md` | teach the kit's model-line grammar a first-class `unstated` effort token (recognized missi… | groomed → `overnight-menu-2026-07-17.md` |
| 2026-07-14 | `2026-07-14-eap-final-ender.md` | make dormancy machine-detectable at wake time — teach the v3 startup/failsafe prompt templ… | **ungroomed** ⚠ >2d |
| 2026-07-14 | `2026-07-14-checklist-refresh-2.md` | `check_trigger_health.py` should accept a `--refresh-cmd-hint` or the wake procedure shoul… | groomed → `2026-07-14-central-docs-plan.md` |
| 2026-07-13 | `2026-07-13-central-docs-review.md` | the stamp-discipline checker (`check_stamp_discipline`) treats every `D-NNNN` token as an … | groomed → `2026-07-14-central-docs-plan.md` |
| 2026-07-12 | `2026-07-12-external-research-prompt.md` | the external-briefing compression done here by hand (research corpus → one self-contained … | groomed → `2026-07-12-repo-consolidation-plan.md` |
| 2026-07-10 | `2026-07-10-registry-gap-closure.md` | registry drift checker | groomed → `2026-07-19-next-slices.md` |
