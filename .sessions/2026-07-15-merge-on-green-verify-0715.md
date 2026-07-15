# 2026-07-15 — merge-on-green-verify-0715 (rollout verification recording: 19-repo sweep · triage · queue reconcile)

> **Status:** `complete`

- **📊 Model:** Fable (Claude 5 family) · docs-only

## What happened

WRITE phase of the 14:xxZ fleet-manager oversight wake (PR #233, branch
`claude/merge-on-green-verify-0715`, delegated coordinator pen for
control/status.md). Recorded the merge-on-green rollout verification sweep
(four read-only workers, 14:00–14:10Z, all 19 fleet repos) — every claim
below cited from those sweeps, nothing invented.

- **Findings doc** —
  `docs/findings/merge-on-green-rollout-verification-2026-07-15.md`
  (Status `audit`): 19-row per-repo table (mechanism at main@HEAD with
  blob/commit SHA + install date/PR · gates · bot-merge evidence ·
  verdict). **Headline: 13/19 PROVEN · 5/19 INSTALLER-PR-OPEN · 1/19
  MISSING.** Today's 13:41–13:57Z rollout wave landed nothing on any main
  — all five installer PRs (opus4.8 #24 · fable5 #17 · product-forge #25
  · pml #89 · plugin-hello #3) self-parked on the workflow-file
  owner-merge-only rail; superbot #2111 was a routine enabler-armed merge,
  not an install. Cross-cutting gaps recorded: superbot PAT attribution
  (merged_by never shows the bot there, by design), branch-prefix
  allowlist holes (superbot-next #491/#492 + superbot `bot/*` heads merged
  manually), plugin-hello inert-without-CI, sonnet5 skipped, fm #227
  conflict-dirty despite green checks. Linked from the findings README
  index + current-state (docs-gate reachability).
- **fleet-triage** — new dated section "2026-07-15 · merge-on-green
  verification + reboot-gap re-sweep (14:00–14:10Z)": five installer-PR
  landing-path rows; sonnet5 no-automation/archive-candidate row;
  reboot-gap re-sweep verdicts consistent with the 12:51–12:54Z class —
  games (11:41:04Z, ~26h) + idle (11:32:05Z, ~26.5h) **DARK, reboot gap
  continues** (manager relay commits 03:38Z are not seat-side signal),
  mineverse (18:59:20Z, ~19h) **STALE**, hub **FRESH via HEAD-activity
  fallback** (merge #2111 12:54:46Z, 2 intentional open PRs).
- **owner-queue reconcile** — A#63 (OQ-FM-PR227-MERGE) amended: fm #227
  now `mergeable_state=dirty` (roster cron merge #231 / Gen #59, 12:04Z);
  one-click fails until a future fm session merges main in + regens; item
  kept open. New **A#68 OQ-ROLLOUT-INSTALLER-CLICKS** (five paste-ready
  merge links; plugin-hello CI caveat noted). **B#8
  OQ-TRADING-ALLOW-AUTOMERGE resolved** — proven live (#128 merged
  2026-07-15T03:38:26Z by github-actions[bot]). **#54
  OQ-VENTURE-SANDBOX-REPO resolved** — UNBLOCKS satisfied in production
  (#203 bot-merged 04:10:06Z; no sandbox needed). #58
  OQ-PML-ENABLER-INSTALL amended — the decision materialized as installer
  PR #89; its click folded into A#68.
- **Heartbeat** — control/status.md wholesale overwrite (delegated pen,
  neutral facts): rollout headline, queue actions, reboot-gap one-liner,
  roster Gen #59 fresh (no regen), registry untouched, next-2-tasks.

## Close checks

- `check_roster_freshness.py` exit 0 — "OK — generated-at
  2026-07-15T12:03Z, 2.3h old (threshold 4h)".
- `check_owner_queue.py` exit 0 — "CLEAN — no merged/closed citations,
  slugs intact (queried 7 record(s))" (first run flagged my own A#63
  amendment's "PR #231" context cite — rephrased to "cron merge #231" so
  the probe doesn't read a satisfied ask; the flag was the checker working
  as designed on my wording, not drift).
- `check_trigger_health.py` exit 0 — "VERDICT: PASS — all 9 invariants
  green" (I4 MANAGER-FAILSAFE PASS on `trig_01LgMqjbBHsNTWMe6T3vaWmk`,
  next 12:32Z-slot basis 11:50Z snapshot, 2.5h old).
- `bootstrap.py check --strict` exit 1 — red ONLY on this card's designed
  born-red HOLD ("This red is the designed hold, not a defect"); 4
  guard-fire telemetry records committed with the session per the check's
  own instruction.

## Walls hit

- None blocking. check_owner_queue's live probes hit expected read walls
  on two A#68 rows (product-forge #25 / pml #89: api 403 + html fallback
  errors) — recorded by the checker itself as NOT MEASURED notes, exit
  still 0.

## Enders

- 💡 **Session idea:** the kit's merge-on-green installer should **ship a
  minimal CI gate when the target repo has zero workflows** — plugin-hello
  got an inert installer (PR #3): the repo has no `.github/` at all, and
  the sweep treats zero check runs as NOT-ready *by deliberate design*, so
  the install is a no-op by construction. Pair the two (installer detects
  zero workflows → adds a trivial always-green sanity check alongside, or
  refuses with a loud "needs CI first" note in the PR body) or the rollout
  ships dead weight that reads as automation. Dedup: grepped
  `docs/ideas/` + `docs/` — no existing idea covers installer/CI pairing;
  evidence: findings doc plugin-hello row + cross-cutting gap 3.
- ⟲ **Previous-session review** (oversight-wake-0715b, PR #232): clean
  rungs throughout — its A#63 re-verify, 18-row SHA-cited sweep, and
  honest backlog-dry call were exemplary. What it missed: its "A#63 = one
  owner click" heartbeat note went stale **within the hour** — the roster
  cron's #231 (12:04Z) had *already* advanced main past #227's 09:16Z base
  when the 12:58Z heartbeat shipped, and the wake's live probe read only
  open/closed state, not mergeability. Concrete improvement:
  `check_owner_queue.py`'s PR probe should also read `mergeable_state` and
  flag `dirty` on parked/cited PRs — a queued "one click" that will fail
  is exactly the satisfied-but-open drift class the checker exists to
  catch (carried on this wake's heartbeat next-2-tasks).

## Follow-ups (not done here — out of scope)

- A#68: five owner installer clicks (plugin-hello needs a CI workflow too).
- A#63: fm #227 conflict resolution (future fm session: merge main in +
  regen), then the owner click.
- Next wake: re-probe the installer PRs; extend check_owner_queue with the
  `mergeable_state` probe.
