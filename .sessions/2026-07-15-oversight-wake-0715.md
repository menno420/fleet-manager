# 2026-07-15 · oversight wake (14:58Z)

> **Status:** `in-progress`

- **📊 Model:** Fable · high · tooling+docs

About to: routine oversight wake — extend scripts/check_owner_queue.py to flag dirty (merge-conflicted) parked PRs, re-probe the five rollout installer PRs (A#68), roster freshness check/regen if >3.5h, fm #227 mergeable_state re-check (A#63), heartbeat + enders.

## What happened

- **Inbox at HEAD:** no executable open ORDER for this seat — ORDER 017 stays
  GATED on owner-queue item 16; ORDER 024 stays GATED on the E#44
  consolidation-plan approval. Standing orders (029/032–040) are doctrine /
  other-seat lanes. Moved to the batonned self-initiated rung.
- ⚑ **Self-initiated (baton from wake 0715c): check_owner_queue.py check 1b —
  dirty parked PRs.** `fetch_pr_state` now carries `mergeable_state` (API
  only; the HTML session fallback carries none and degrades to a NOT
  MEASURED note, exit-0). A merge-actionable item citing an OPEN PR with
  live `mergeable_state=dirty` fires `FLAG [dirty-parked-pr]` — unless the
  item text already acknowledges the conflict (mentions dirty/conflict),
  which downgrades to a note: the checker catches *silent* rot, not
  already-surfaced state. `unknown` (GitHub recomputing) is also a note,
  never a flag. Selftest extended: KNOWN_STATES pins fm #227 dirty (ground
  truth: live API read this wake, matching the A#63 amendment) and the
  known-bad fixture gained item 2 (`OQ-FIXTURE-FM-PR227-PARKED-ROT`).
  Selftest PASS (4/4 flags incl. the new one; known-good clean). Live run
  vs docs/owner-queue.md: CLEAN exit 0 (sessions report mergeable_state NOT
  MEASURED honestly — the Actions regen run is the reliable venue, same
  split as check 4). Fixture-authoring lesson recorded below (⟲).
- **A#68 re-probe (read-only, live API):** all five installer PRs still
  OPEN, none merged — opus4.8 #24, fable5 #17, product-forge #25, pml #89,
  plugin-hello #3 — each `mergeable_state=clean`. One honest STATUS line
  added to the A#68 row; no churn, the five clicks remain valid as written.
- **Roster:** Gen #60 generated 14:23Z by the roster-regen cron — 0.7h old
  at this wake's check (15:04Z), under both the 3.5h dispatch bar and the
  4h checker bar. No regen. `check_roster_freshness.py` OK exit 0. (The
  dispatch's "Gen #59 @ 12:03Z" was overtaken by the 14:23Z cron run.)
- **fm #227 (A#63):** live `mergeable_state=dirty` (first poll read
  `unknown` while GitHub recomputed; re-poll confirmed dirty) — exactly
  what the A#63 row already records, so no row change. Not merged, not
  rebased, not commented — read-only per dispatch.
- **Close checks:** check_roster_freshness OK exit 0 ·
  check_owner_queue CLEAN exit 0 (upgraded version, live queue) ·
  check_trigger_health PASS 9/9 exit 0 (I4 failsafe green; snapshot basis
  11:50Z, 3.2h, under bar) · bootstrap check --strict red ONLY on this
  card's own born-red hold (designed), advisories fixed (claim bullet
  format, model-line payload).

## Enders

- 💡 **Session idea:** `check_owner_queue.py` now probes PR state live but
  the *session* venue always degrades to the HTML fallback (api.github.com
  proxy-walled) which carries no mergeable_state — add a tiny
  `--from-snapshot telemetry/pr-states.json` mode so the Actions regen run
  (where the API works) can export the measured states, letting session
  wakes consume last-measured mergeable_state with an honest age stamp
  instead of NOT MEASURED. Same snapshot pattern check_trigger_health
  already proves. (Grepped docs/ideas-equivalents: no existing capture —
  playbook/backlog carry no snapshot-export item for owner-queue probes.)
- ⟲ **Previous-session review:** the 14:xxZ merge-on-green-verify wake
  (PR #233) did a genuinely strong evidence sweep (13/19 PROVEN with
  citations, honest "landed NOTHING" headline) and its baton — "extend
  check_owner_queue to read mergeable_state" — was concrete enough to
  execute this wake without re-derivation; its card's `📊 Model:` line,
  however, used a two-field payload the telemetry harvest records NOTHING
  from (bootstrap advisory fired on it this wake). **Workflow improvement:**
  fixture authoring for acknowledgment-downgrade checks has a self-trap —
  the fixture item describing "the checker must fire on dirty" itself
  contained the ack trigger word three separate ways (prose, flag name,
  slug) and took three passes to de-trip; the durable lesson (now in the
  fixture's own VERIFIED-NEEDED note): when a check downgrades on
  text-acknowledgment, the known-bad fixture text must be written *without
  the trigger vocabulary anywhere*, including ids.

> **Status closing note:** PR #239 stays open for merge-on-green / the
> owner — this session never merges, per dispatch.
