# 2026-07-20 · fm build slice — liveness checker honors declared-idle heartbeats

> **Status:** `complete`

About to happen (declared born-red): teach `scripts/check_lane_liveness.py` to
honor a DECLARED idle. Ground truth motivating it (today): the Self Improvement
seat closed its wake chain deliberately at 07:53Z per its honesty guard — its
substrate-kit heartbeat's Baton reads "Agent-buildable kit slices are drained
through v1.20.1 + #555" (updated 07:45:00Z) — and the 15:52Z liveness run still
scored the lane STALLED, triggering the OQ-SI-CHAIN-DEAD escalation and a
manager nudge. An honest idle should read differently from a silent stall.
Plan: scan the heartbeat text the checker ALREADY fetches (same transport, zero
new reads; "not measured" walls unchanged) for an idle declaration
(case-insensitive: "backlog dry" / "honest idle" / "idle-declared" /
"standing down" / backlog-slices-queue…drained — grounded on the real
substrate-kit grammar above); a STALLED/QUIET lane WITH a fresh declaration
(dated by the declaring heartbeat's `updated:` stamp, within one cadence window
of the lane's newest signal) becomes verdict `IDLE-DECLARED` — exit-neutral,
`--strict` does not fail on it, headline lists it separately. Undated
declaration → `IDLE-DECLARED (undated …)` and the STALLED escalation hint
stays. Selfcheck extended; Q-0105 provenance note; ground-truth run quoted.
Then: OQ-SI-CHAIN-DEAD owner-queue update (SI responded to the 16:0xZ nudge —
halt was deliberate honest-idle; retire condition noted), one-line triage
addendum, `control/status.md` bump. Claim
`control/claims/claude-fm-declared-idle.md` (deleted in the flip commit).
Decide-and-flag rationale: S, pure-logic extension of a verified checker over
data it already reads; reversible. No trigger-MCP calls from this venue.

- **📊 Model:** fable-5 · high · feature build — extend verified checker (Q-0105 provenance tier)

## What shipped (PR #400)

- `scripts/check_lane_liveness.py` — **`IDLE-DECLARED` verdict** (Q-0105
  provenance block, kill-switch included). `find_idle_declaration` scans the
  control/status*.md texts `read_heartbeat` ALREADY carries (zero extra
  fetches; walls unchanged → NOT MEASURED) for the case-insensitive grammar
  `backlog dry | honest idle | idle-declared | standing down |
  (backlog|slice(s)|queue|lane(s)) …≤60 chars, same sentence… drained` — the
  last alternative grounded on the REAL committed substrate-kit grammar (the
  dispatch said "backlog dry"; the heartbeat actually says "Agent-buildable
  kit slices are drained through v1.20.1 + #555", Baton, updated 07:45:00Z).
  Pure `apply_idle_declaration` ladder: STALLED/QUIET base + dated-fresh
  declaration (declaring heartbeat's `updated:` stamp within 1 cadence
  window of the lane's newest signal) → `IDLE-DECLARED`, exit-neutral
  (`--strict` passes); **undated** → `IDLE-DECLARED (undated — STALLED hint
  stands)`, still fails `--strict` and stays in the STALLED headline bucket
  (an undatable claim cannot clear an escalation); **stale-dated** (superseded
  by later activity) never converts, annotated. Headline gains a separate
  `IDLE-DECLARED:` bucket; the matched line is quoted under the table
  (truncation marked at 200 chars). Ledger/diff: `VERDICT_RANK[IDLE-DECLARED]
  = 1` so STALLED→IDLE-DECLARED classifies as recovery. Selfcheck 41 → 69
  pins (grammar positives incl. the verbatim live kit line, 4 negatives,
  finder dated/undated/none/truncation, full apply ladder, rank ordering).
- `docs/owner-queue.md` — `OQ-SI-CHAIN-DEAD` status addendum: halt was a
  deliberate honest-idle (heartbeat had declared it); SI re-armed after the
  ~16:1xZ nudge (coordinator-reported); **retire condition: next triggers
  snapshot shows a fresh pending SI one-shot bound to
  `session_01VsWWnVdwbvkGAW4kAmQzmt`**; this slice cited as the process fix.
- `docs/fleet-triage.md` — one-line addendum on the 15:30Z entry's
  escalation bullet pointing at the OQ retire condition.
- `control/status.md` — `updated:` → 16:20Z; 16:2xZ slice section; Baton
  otherwise unchanged.
- Claim `control/claims/claude-fm-declared-idle.md` (born-red commit,
  deleted in this flip commit).

## Ground-truth runs (2026-07-20, verbatim excerpts)

Run 1 — `--repos substrate-kit` at 16:16:36Z (table row + headline + quote):

```
| substrate-kit | 2026-07-20T07:45Z | heartbeat control/status.md | ~8h31m | 2h (seat cron (Self Improvement seat)) | 4.3 | enabled | WAKING-IDLE (4 fires since last output) | IDLE-DECLARED |

STALLED: none · IDLE-DECLARED: substrate-kit · WAKING-IDLE: substrate-kit · asleep: none · DARK: none · not measured: 0

idle declaration — substrate-kit: "Agent-buildable kit slices are drained through v1.20.1 + #555. The honest next slice is: land #555 on green, then WATCH the 8 open adopter PRs — they are resident-lane merges the hub cannot make. If residents stay dormant (no merge / no resident activity across the next wake or two), ESCALATE to the hub venue (fleet-manager) so the owner sees the stalled adoption, rather than the hub silently pushing to resident-owned PRs (barred by Q-0261.3). Remaining non-resident work is owner-gated (⚑ below)."
```

(exit 0 — pre-truncation build; run 2 shows the marked 200-char truncation.)

Run 2 — full fleet `--strict` at 16:16:57Z, headline verbatim:

```
STALLED: superbot-idle (Seat B) · IDLE-DECLARED: substrate-kit · WAKING-IDLE: substrate-kit, superbot-idle (Seat B) · asleep: none · DARK: none · not measured: 0

idle declaration — substrate-kit: "Agent-buildable kit slices are drained through v1.20.1 + #555. The honest next slice is: land #555 on green, then WATCH the 8 open adopter PRs — they are resident-lane merges the hub cannot make. If r …[truncated]"
```

`strict-exit=1` — honest: superbot-idle (Seat B) is genuinely STALLED with no
declaration (last commit 07:37Z, 4 fires since, nothing declared); substrate-kit
alone no longer trips `--strict`. At 15:52Z (pre-fix, PR #399) substrate-kit
scored STALLED; now IDLE-DECLARED — exactly the ground truth this slice exists
to encode. Selfcheck: `selfcheck OK (69 pins)`.

## Enders

- **💡 Session idea (dedup-checked vs docs/planning/ + docs/, no prior hit):**
  *idle-but-burning downshift advisory* — an `IDLE-DECLARED` lane whose
  failsafe keeps firing 2h wakes is now a KNOWN token leak (the lane said
  "nothing to do" and we keep waking it anyway — substrate-kit's 4 fires
  since 07:45Z today were exactly this). The checker (or wake procedure)
  should flag `IDLE-DECLARED + WAKING-IDLE` as "idle-but-burning: consider
  cadence downshift or failsafe pause until new orders", turning the honest
  idle into a cost saving instead of just a silenced alarm. Worth having:
  distinct from WAKING-IDLE (which flags unexplained burn); this flags
  *explained* burn with a concrete remedy.
- **⟲ Previous-session review (PR #399, 15:30Z records slice):** strong
  discipline — it escalated exactly on its pre-stated tripwire
  (substrate-kit QUIET→STALLED) with in-export evidence, and the NEW
  failure-class naming ("failsafe-fires-but-no-rearm") was genuinely useful.
  What it missed: it treated the 07:45Z heartbeat as a *timestamp* only —
  the very Baton it dated the stall by contained the idle declaration in
  plain text, so the escalation shipped without reading the lane's own
  words. System improvement (built this slice): the checker now reads the
  words; procedural residue for wake procedures — quote the lane's Baton in
  any escalation you write, so a human reviewer sees the lane's self-report
  next to the verdict.
- **Doc-audit:** everything from this session has a durable home — checker
  behavior in the script docstring + Q-0105 block; fleet-state deltas in
  owner-queue (retire condition) + triage addendum + status.md slice
  section; run evidence on this card + the PR body. `bootstrap.py check
  --strict` clean at flip apart from advisories predating this slice
  (seat-digest-stale, 12 CAPABILITIES dateless-wall warnings — both
  pre-existing on main, not this slice's to fix; noted as follow-ups).
- **Guard-fires:** `.substrate/guard-fires.jsonl` delta from this session's
  check runs committed with the flip (telemetry ledger doctrine — never
  revert).

