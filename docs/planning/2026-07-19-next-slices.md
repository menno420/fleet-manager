# Next executable slices — night-shift idea groom (2026-07-19)

> **Status:** `plan` — drafted 2026-07-19T07:26Z (PR #349), per the owner's universal
> continue prompt (~07:45Z posted intent: when executable work is drained, PLAN).
>
> Snapshot of its drafting moment: re-verify volatile claims (PR states, live trigger
> ids) at HEAD before building (playbook R2). Source ideas: the 💡 blocks of the
> 2026-07-18/19 `.sessions/` cards, each already dedup-checked at capture time.

## What this is

The night shift (2026-07-18T21Z → 2026-07-19T06:30Z) recorded ~8 session ideas across
its cards. This pass grooms them into a **ranked queue of next executable slices** for
the fleet-manager seat — recommendation-first, honest about which ideas do NOT earn a
slice. The top 3 become the standing "next slice" queue in the `control/status.md`
baton.

## Ranked — build in this order (fm-seat, docs+tooling lane)

### 1. `scripts/check_lane_liveness.py` — seat-chain stall detector · **S/M**

- **What:** given a lane repo + its failsafe cron spec, read the repo's last main
  commit + heartbeat `updated:` stamp and count consecutive failsafe windows with
  zero landed output → OK/WARN/STALL verdict.
- **Why now:** tonight's websites silence (no commits after 21:52Z, ORDER 036 unacked
  across the 23:45Z/01:45Z/03:45Z windows) was only caught by a ~06Z human-style read
  and became `OQ-WEBSITES-036-STALL` ~4h late. This mechanizes exactly that sweep
  (06Z-morning card 💡). Highest value: it guards the *fleet's* liveness, not just an
  fm artifact, and the 036 watch is still open — the checker would monitor it from
  the next wake.
- **Shape:** stdlib, advisory-only, standalone (never merge-blocking), provenance +
  kill-switch header — same tier as the S3/S5/S9 trio.

### 2. Regen-window skip detector in `check_roster_freshness.py` · **S**

- **What:** parse the cron out of `.github/workflows/roster-regen.yml` and report
  *missed scheduled windows since generated-at* alongside age (`OK but 2 window(s)
  skipped since gen #N`).
- **Why now:** the 00:40Z AND 02:40Z regen windows both silently dropped tonight
  (03Z card 💡) — the second consecutive-skip night — and the only pre-4h-bar catch
  was a human heartbeat read. Complements parked PR #344 (odd-hour second cron):
  #344 reduces drop impact, this makes drops announce themselves at every wake
  regardless of whether #344 lands.
- **Shape:** small edit to an existing verified checker; advisory line, exit
  behavior unchanged.

### 3. Seat-provenance-aware I8 remedy in `check_trigger_health.py` · **S**

- **What:** when I8 (duplicate cron) fires, rank the duplicates by seat provenance
  (`job_config` session binding / `created_at` vs the lane's latest cutover stamp)
  and emit a provenance-ranked delete recommendation, falling back to "verify live,
  human decides" when bindings are unreadable.
- **Why now:** the checker's generic "keep the OLDEST" heuristic gave the *wrong*
  answer on the live SBW pair this very night — the 06:15Z escalation
  (`OQ-SBW-DUP-FAILSAFE`) had to invert it by hand to "delete the older
  `trig_01XJJ88pQaQFRSpVAviCfAZe`" (06Z-snapshot card 💡). A remedy line that can
  contradict the correct escalation is worse than none.
- **Shape:** contained edit to the I8 branch; recommendation text only.

## Below the line — real, but not next (build after 1–3 if capacity remains)

- **Write-side fence emitter** (`--emit-fence` on `verify_routine_state.py`) · S —
  closes the WRITE side of the routine-claims fence so heartbeat writers paste
  generated JSON instead of hand-typing trig-ids (routine-claims-fence card 💡).
  Genuine, but the read-side verifier already catches a typo'd fence loudly (exit 2 /
  DRIFT), so the failure it prevents is annoying, not silent. Queue behind 1–3.
- **`check_capabilities_grammar.py`** · S — lint the CAPABILITIES append-log bullets
  against their declared five-field grammar so the S9 wall-ager parses contract, not
  heuristics (capability-heartbeat card 💡). Worthwhile hygiene; no live friction
  this week — the ledger's entries have parsed fine. Queue behind 1–3.

## Dropped / parked — honestly not earning a slice now

- **`post_capture_deltas` snapshot grammar** (wake-oversight card 💡) — **DROPPED as
  superseded.** Its motivating friction (mid-session trigger changes only recordable
  as free-text `capture_notes`) has since been largely closed by the routine-claims
  fence (PR #335/#339 lineage): the fence records the seat's claimed state
  machine-readably at heartbeat time and `verify_routine_state.py` diffs it against
  any export, with the capture-lag honesty note covering the gap window. The residual
  value (deltas for *sibling* seats' triggers between full exports) is small next to
  a ~1900-record grammar change. Revisit only if capture-lag DRIFT misreads recur.
- **`gen_hub_queue_baton.py`** (universal-continue-prompt card 💡: aggregate per-repo
  incomplete-actions into the consolidated owner-steps/baton) — **PARKED as
  premature.** It consumes per-repo incomplete-actions files that most seats do not
  yet uniformly produce; built now it would aggregate mostly-empty inputs. The
  Continue-prompt rollout has to land fleet-wide first. Keep the idea; re-rank when
  ≥3 lanes actually emit the files.
- **Auto-supersede for red bake PRs** (sweep-records card 💡) — **ROUTED, not fm
  work.** The bake workflow lives in menno420/websites; this is a websites-lane
  change riding the ORDER 036 follow-up (the same lane fix stream as websites #434).
  fm's part is only the watch already in the baton (`OQ-WEBSITES-036-STALL`).

## Standing queue (mirrors the status.md baton)

1. `check_lane_liveness.py` (new advisory checker) — **DONE, PR #350**
2. roster regen-window skip detector (edit `check_roster_freshness.py`) — **DONE, PR #352**
3. I8 provenance-ranked remedy (edit `check_trigger_health.py`) — **DONE, PR #353**

**Queue drained 2026-07-19 (~09:3xZ).** Next = the below-the-line items (fence
emitter · capabilities-grammar linter) or a fresh groom on the next planning pass.

---

## Re-groom — 14Z cycle (2026-07-19T14:16Z, PR #364)

The 07:26Z queue **and** its below-the-line items are all landed: #350
(lane-liveness) · #352 (regen-skip) · #353 (I8 provenance) · #356 (fence
emitter, `emit_routine_claims.py`) · #358 (capabilities grammar linter). This
pass harvests the 💡 blocks recorded SINCE the 07:2x groom (cards:
lane-liveness, morning-records, regen-skip-detector, i8-provenance,
roster-cron-resilience, 10z-snapshot, fence-emitter, capabilities-linter) and
re-ranks. Eight candidates; three earn slices.

### Ranked — build in this order

1. **Volatile-field drift check in `verify_routine_state.py`** (fence-emitter
   card 💡) · **S** — diff the fence's informational `next_run_at`/`last_fired`
   against the export's record for the claimed failsafe id (INFO/WARN, with the
   capture-lag honesty note). **Why top:** this very cycle the fence sat stale
   (claimed last_fired 08:32:09Z vs export 12:32:22Z — two firings behind) and
   was only fixed because a snapshot slice happened to bump it; the read-side
   verifier said `OK` throughout. The exact staleness the emitter prevents on
   the write side is still invisible on the read side; a WARN would surface it
   at every check run. Contained edit to a verified checker.
2. **I8 reads the owning lane's `routine-claims` fence** (i8-provenance card
   💡) · **M** — when I8 finds a duplicate group, fetch the owning repo's
   `control/status*.md` fence (the same shallow-git path `gen_roster.py` uses)
   and, when exactly one duplicate id matches the fence's claim, name the
   keeper outright. **Why 2:** the SBW pair is in its second escalation cycle;
   today's remedy still ends in "verify live, human decides". SBW's own
   heartbeat fence claiming its current failsafe id would collapse the remedy
   to a definite delete recommendation. Cross-repo read, hence M.
3. **`check_label_hygiene.py`** (morning-records card 💡) · **S/M** — sweep
   fleet repos for parking-class labels: flag any OPEN PR carrying one (loud —
   directive violation) and any repo where the definition persists/re-appears
   (the websites `host-automerge-extras.yml` re-creation trap). **Why 3:**
   mechanizes the owner's 2026-07-19 nothing-stuck directive, which today was a
   one-off hand sweep; pairs with the open `OQ-LABEL-DEFS-DELETE` hub item.

### Dropped / parked — honestly not earning a slice now

- **`covers:` machine-readable seat coverage** (lane-liveness card 💡) — real
  gap (Game Lab constituents unattributable) but an enhancement to a checker
  that just shipped and is advisory; let liveness run a few days first.
- **Regen `--probe-runs` run-history prober** (regen-skip card 💡) — parked:
  #344's odd-hour second cron just landed and is observably firing (gen #104/
  #105); the disjunction the probe resolves matters mainly when drops recur.
  Re-rank if the skip detector WARNs again post-#344.
- **Registry-growth trendline / purge-forecast** (10z-snapshot card 💡) —
  telemetry nicety; the per-capture delta note covers the need while growth is
  linear (~60/4h). Revisit if capture pagination cost becomes a friction.
- **Kit-graduation of the CAPABILITIES checker pair** (capabilities-linter card
  💡) — routed, not fm work: it is a substrate-kit lane change; propose via the
  kit's channel when its next wave opens.
- **`gen_hub_queue_baton.py`** (roster-cron card 💡, re-recorded) — stays
  PARKED per the 07:26Z groom reasoning (inputs not uniformly produced yet).

### Standing queue (mirrors the status.md baton)

1. volatile-field drift check in `verify_routine_state.py` — **NEXT SLICE**
2. I8-reads-lane-fence (definite-keeper remedy)
3. `check_label_hygiene.py` (nothing-stuck mechanized)
