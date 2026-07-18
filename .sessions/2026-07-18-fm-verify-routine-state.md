# 2026-07-18 · fm verify-routine-state (new tool: one-command routine-state proof)

> **Status:** `complete`

Build `scripts/verify_routine_state.py` — a stdlib one-command proof that the heartbeat's
claimed routine state (armed failsafe id/cron, deleted predecessors) matches a real
`list_triggers` export, born from today's hung-arm + 6.1h-stale-snapshot friction where
proving chain state took a 20-page hand pagination.

- **📊 Model:** fable-family · high · feature build

## What shipped

- `scripts/verify_routine_state.py` (new, PR #335) — parses `control/status.md`'s routine
  block for its claims (armed failsafe id + cron, claimed-DELETED ids), diffs them against
  any `list_triggers` export, and reports pending seat-bound pacemaker one-shots. Accepts
  ALL three export shapes — committed snapshot (`{"captured_at","data"}`), page-dump
  array, and a FLAT array of records (the PR #334-review flat-array friction, now
  smoothed). Checks: C1 claimed failsafe present + enabled + cron matches; C2 unclaimed
  enabled seat-named cron = duplicate/orphan DRIFT; C3 claimed-DELETED still enabled =
  DRIFT; INFO pending ticks. Exit 0 OK / 1 DRIFT / 2 unreadable. Q-0105 provenance header
  (unverified + kill-switch) and `--selfcheck` offline assertions (the repo's scripts
  convention; no `tests/` dir exists, none invented).
- `docs/playbook.md` R26 — one-sentence companion-proof pointer (the verify-tooling index;
  `docs/SKILLS.md`/`docs/ROUTINES.md` are kit-generated, so not hand-edited).
- `.substrate/guard-fires.jsonl` — telemetry delta committed with the session.

## Ground-truth runs (verbatim verdict lines)

Against the committed pre-cutover 20:42:05Z snapshot + the 21:15Z heartbeat — DRIFT,
**correctly** (capture predates the failsafe cutover; the two flags are exactly the
snapshot's own `capture_notes` post-capture deltas):

```
[DRIFT] C1 claimed failsafe `trig_01GK4mjoKBP3yCabn9ux1MB2` ABSENT from the export
[DRIFT] C3 claimed-DELETED `trig_01Bo7dZxM9xz2hwR36L424Z8` 'Fleet Manager failsafe wake' is still ENABLED in the export
VERDICT: DRIFT — 2 mismatch(es) between the heartbeat's routine claims and the export. Capture predates 'now' — if the claims are NEWER than the 2026-07-18T20:42Z capture this may be capture lag, not live drift: refresh the export (list_triggers, ALL pages) and re-run for live truth.  (exit 1)
```

Same records fed as a FLAT ARRAY → identical DRIFT verdict (shape acceptance proven on
real data, exit 1). Synthetic post-cutover export (old failsafe removed, claimed new one
added) →

```
[OK   ] C1 claimed failsafe `trig_01GK4mjoKBP3yCabn9ux1MB2` present + enabled, cron `30 */2 * * *` matches
[OK   ] C3 claimed-DELETED `trig_01Bo7dZxM9xz2hwR36L424Z8` — absent from export
VERDICT: OK — heartbeat routine claims match the export (2 claim(s) verified).  (exit 0)
```

`--selfcheck` → `selfcheck: PASS (0 failure(s))`.

## Gates

- `python3 bootstrap.py check --strict` → the only red pre-flip was the by-design born-red
  session-gate HOLD on this card; EXIT 0 expected at this flip. The two advisory
  model-line warnings fire on a prior merged card (`2026-07-18-fm-wake-oversight.md`),
  never exit-affecting, not this PR's diff.
- PR #335 (`claude/fm-verify-routine-state`), lands on green.

## 💡 Session idea

The heartbeat's routine block is prose, so `verify_routine_state.py` must parse claims by
regex grammar — fragile against wording drift. Teach the heartbeat a tiny
**machine-readable routine-claims fence** (a `routine-claims` YAML/JSON block in
`control/status.md` written at heartbeat time: armed ids + crons, deleted ids, pacemaker
session) so the verifier — and future tooling — reads a contract instead of prose; the
prose stays for humans. Dedup-checked: prior "machine-readable" ideas cover seat
version-stamps (`fm-meta-restamp-v37` card) and the current-state dated header
(`fm-current-state-refresh` card), not the routine block; and this is neither the
auto-supersede nor the post-capture-deltas idea (both already recorded).

## ⟲ Previous-session review

#334 (fm-sweep-records) was a clean oversight-records slice: MCP-verified sweep evidence,
an honest owner-queue re-score to RESOLVED, and its ⟲ review surfaced the flat-array
export friction — which THIS slice implemented, a nice closed loop. What it could have
done better / system improvement: that friction observation lived only inside the card's
⟲ prose, so it reached a builder solely because the coordinator hand-carried it into this
dispatch; review-surfaced tool gaps should be routed into a durable pickup point
(`docs/ideas/` or `docs/NEXT-TASKS.md`) in the same session, so the loop closes without a
human/coordinator relay.

## 📋 Doc-audit

Durable homes updated in-session: the script itself (provenance header carries the why +
proof run), playbook R26 pointer, this card (verbatim ground-truth outputs, as the PR body
promises). Claim `control/claims/claude-fm-verify-routine-state.md` released in this flip
commit. No chat-only residue. Carried-forward observation from #334's audit remains open
(stale claim file `control/claims/claude-fm-wake-2026-07-18.md` on main — future
stale-claim cleanup slice, not this PR's scope).
