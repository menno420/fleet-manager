# 2026-07-17 — fresh-start-cleanup (EAP wind-down hub cleanup)

> **Status:** `complete`
> **Branch:** claude/fresh-start-cleanup

Intent: owner-authorized "fresh-start" cleanup of the fleet-manager hub ahead of the
EAP read-only cutoff (2026-07-21) and the Projects recreation. Records/oversight PR only
— no runtime code. Lands on green via `merge-on-green.yml`; this session does NOT
self-arm or self-merge (CONSTITUTION merge rail, updated in this PR).

## What happened

- **(1) CONSTITUTION.md — merge doctrine fixed.** Rewrote the "An open PR is never a
  reason to stop" autonomy rail: removed the `Open READY → arm auto-merge → it lands
  itself` expectation (the exact `agent arms auto-merge / flips-ready on green` action the
  Anthropic permission-classifier has denied since 2026-07-15, which froze finished PRs as
  drafts fleet-wide). Replaced with: open PRs READY and let the server-side
  `merge-on-green.yml` squash-merge on green — **no** agent-side ready-flips or REST/MCP
  merges. Rest of the working agreement untouched.
- **(2) docs/current-state.md — accurate snapshot.** Replaced the ~3-day-stale "In flight"
  block (PR #182, EAP audit fan-out, final-email straggler sweep — all long terminal) with
  the true post-wind-down state: 0 open PRs, fleet backlog cleared 2026-07-17, EAP cutoff
  corrected to **2026-07-21 17:00 PT**, recreation imminent, scaffolding retired. Added a
  retirement note to the Stability-baseline section.
- **(3) docs/owner-queue.md — slimmed 109KB → 28KB.** Corrected the stale 2026-07-14 EAP
  date to 2026-07-21 throughout; slimmed to a genuinely-open **Active** set (secrets incl.
  `ROSTER_READ_TOKEN`/`BAKE_PAT`; settings walls; product/external asks; standing decisions;
  objection-only; seat design forks; hygiene) + a **Superseded-by-wind-down** index (ids
  kept, nothing lost) + the preserved historical Resolved/Archive log.
- **(4) docs/NEXT-TASKS.md — created.** Clean task set for the recreated manager: the
  recreation-window immediate tasks (owner actions, orphan-trigger sweep, apparatus
  keep-vs-retire) + the overnight-menu first-build trio S3/S5/S9 (fleet-triage staleness
  advisory · docs link-drift sweep · CAPABILITIES wall-age flagger).
- **(5) Scaffolding deprecation-bannered (files kept, workflows NOT deleted):**
  `control/README.md`, `control/outbox.md`, `control/status.md`, `docs/roster.md` carry a
  `RETIRED 2026-07-17` banner; `telemetry/triggers-snapshot.json` got a `_retired` marker
  key. `control/inbox.md` is append-only/one-writer by CI gate, so it was marked via a
  final well-formed **ORDER 049** (a prepended banner would have red-flagged the inbox
  append-only gate) — verified green with the exact CI command.
- **PR** opened READY; lands on green via `merge-on-green.yml`. Session did NOT self-merge.

## Verification

- `python3 bootstrap.py check --strict` → all checks passed (exit 0).
- `python3 bootstrap.py check --strict --status-only --inbox-base <base>` → inbox
  append-only + ORDER grammar green (exit 0).
- `python3 scripts/check_roster_freshness.py` → OK (roster `generated-at` 2026-07-17,
  within the 4h bar; banner prepended above the untouched stamp).

## Enders

- **📊 Model:** Claude Opus 4.8 · high · docs-only
- **💡 Session idea:** ship `scripts/check_owner_queue_size.py` — a stdlib-only advisory
  that reds when `docs/owner-queue.md`'s Active section exceeds N items or when a
  resolved-marked slug (`✅`/`⛔`/RESOLVED/SUPERSEDED) still sits above the
  Resolved/Archive fence, so the queue can never silently re-bloat back to the ~68-slug
  interleaved state this cleanup just untangled. Turns "the queue needs a curation pass"
  into a checker that fires the moment it's due. (Dedup-grepped `docs/ideas/` +
  `scripts/` — `check_owner_queue.py` probes cited-PR state but not size/curation drift.)
- **⟲ Previous-session review:** the overnight incidents/telemetry wakes kept the ledger
  and roster genuinely fresh (roster gen #78 at 10:21Z the same morning) — good custody
  right up to the wind-down. What they missed: current-state.md's "In flight" block and
  owner-queue.md kept accreting dated snapshots without ever collapsing terminal items, so
  by 2026-07-17 both misrepresented a 0-open-PR repo as mid-flight. System improvement:
  the self-initiated idea above (an owner-queue size/curation checker) plus the same
  discipline for current-state — a stale-"In flight" advisory — would make "the snapshot
  drifted" a CI signal instead of a thing the next human has to notice.
