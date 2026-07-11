# Retro — coordinator seat, 2026-07-11 (booted 01:04Z → archived evening)

> **Status:** `reference` — lessons learned from the 2026-07-11 coordinator
> seat (session `session_012o8pySy5K3AV6JWoPKryZL`), written at archive by the
> close-out worker from the coordinator's wrap-up brief, each lesson checked
> against committed evidence where possible (Q-0120). Companion docs:
> `docs/succession/coordinator-handoff-2026-07-11-evening.md` (state),
> `docs/retro/archive-ready-2026-07-11.md` (archive confirmation).

## 1. `send_later` self-binds to the CALLING session

A pacemaker armed via `send_later` from a worker/subagent binds to *that*
session, not the coordinator's. The correct recipe: `create_trigger` with
`run_once_at` and `persistent_session_id` = the coordinator session.
Evidence: the tool's own contract ("delivered back into THIS SESSION") +
the final pacemaker `trig_014GNxy1L67tyiU1FuZrm2Z5` (verified live at
close-out: a `create_trigger` one-shot bound to the coordinator session, not
a `send_later`). Now codified in `reboot-prompt.md` v2 step 2d.

## 2. Classifier merge-wall anatomy — four denial shapes

Observed across the seat's tenure (reported by coordinator; the #68 shape is
committed evidence, the taxonomy is the coordinator's synthesis):

1. **Self-approval** — the PR author's own session merging its green PR
   (verbatim on fm #68: "[Self-Approval]/[Merge Without Review]",
   `docs/findings/enabler-install-verification-2026-07-11.md`).
2. **Relayed authorization** — a fresh session citing the owner's permission
   secondhand; never clears the wall (fm #68 investigation, PR #71 record;
   superbot-games fresh-session attempts named it explicitly — reported by
   coordinator, unverified).
3. **Shared-token-no-APPROVE** — same underlying token identity on both
   sides of the "review", so no independent approval exists (reported by
   coordinator, unverified).
4. **Content-correlation** — denial tracking the attempting session's
   merge-doctrine-saturated context rather than the PR itself (the PR #71
   investigation's verdict for why #68 kept denying: metadata / repo state /
   timing were ruled out because **#69 and #70 sailed through the identical
   pipeline while #68 parked** — verified, all three merged on main).

Operating consequence (already doctrine): park-green + non-author review
comment + owner click; in-session human authorization is the only reliable
clearer; deny-wins — never retry around a denial.

## 3. Dispatch-only sessions exist — verify toolsets before assigning work

Some sessions in the fleet run with dispatch/coordination toolsets and no
repo tools (or no MCP). Assigning one a repo task wastes a full round-trip.
(Reported by coordinator, unverified.) Rule of thumb now in reboot-prompt v2
step 3: verify a session's toolset before assigning it repo work.

## 4. The PR #47 empty-vehicle lesson: a merged PR is only intent

fm #47 was owner-merged (14:55Z, `5625e3b`) but carried ONLY its born-red
session card (`a4b736b`) — the built payload had died with its container, so
the merge shipped nothing. The payload had to be rebuilt and landed via #76
(`e1848ff`) / #77 (`39b888a`). Verified: `control/status.md` PR #76 slice
record + all three merge commits on main. **Lesson: verify the payload
actually landed (diff the merge, don't trust the merge event)** — a green
merged PR proves process, not content.

## 5. Cron jitter + "never fired on schedule" watch discipline

Two distinct failure smells that look alike:

- **Jitter is normal:** live fires land minutes after the slot (failsafe
  `30 */2` last fired 18:37:07Z at roster gen #9 — 7 minutes late). Do not
  file jitter as a defect.
- **Never-fired is a defect signal:** `roster-regen.yml` (`40 */2`) has THREE
  runs, all `workflow_dispatch`, ZERO `schedule` events (verified via the
  Actions API at close-out). A cron that has literally never produced a
  `schedule` run needs a watch with a named next slot (22:40Z) and run-list
  evidence either way — not an assumption that "it probably ran".

The discipline: when watching a schedule, name the exact next slot in the
heartbeat/handoff and check the run list *by event type*, not by whether the
output looks fresh (manual runs mask a dead cron).
