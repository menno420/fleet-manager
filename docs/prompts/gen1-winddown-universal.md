# gen1-winddown-universal — the gen-1 → gen-2 wind-down prompt (ready, not yet deployed)

> **Status:** `owner-guidance`
>
> Authored 2026-07-09 (evening) under the owner-directed fleet-wide
> **gen-1 → gen-2 refresh** — the [`../gen2-blueprint.md`](../gen2-blueprint.md)
> §4 "natural boundary" migration. Every gen-1 lane winds down cleanly and
> commits its own **succession package** in its own repo; each lane's next
> incarnation (fresh Project, new Custom Instructions, new environment) boots
> from that committed state, not from chat memory. The owner pastes the block
> below **verbatim, as one message**, into EACH gen-1 Project's chat
> (owner-queue item — raw link there). Universal wording on purpose: each lane
> adapts it to its own repo and its own working agreements.

## Wind-down prompt (paste verbatim, one message per gen-1 Project)

```
WIND-DOWN: this Project has reached its natural boundary. The fleet is moving
gen-1 → gen-2: your lane continues, but its next incarnation is a FRESH
Project with new Custom Instructions and a new environment, and it will boot
from what you commit now — chat context does not survive. This message is
guidance, not orders: weigh it against your own repo's working agreements and
adapt every step to your lane. Do all of it in THIS session, in YOUR OWN
repo, landing everything as READY PRs (never drafts), auto-merge on green.

Commit the seven succession deliverables:

1. FINISH/PARK. Bring every open PR to a terminal state: merge on green, or
   close with a one-line reason. Commit your roadmap/queue state (done /
   in-flight / next) so nothing lives only in chat. Nothing dangling. If your
   repo's merges are owner-gated, terminal = "PR open, READY, CI green" plus
   a ⚑ line in your status/owner-actions naming the click.

2. PROJECT REVIEW. An extensive retro committed in your repo (your retro
   docs' home; date it): the work done over this Project's whole life; what
   worked; every friction/failure class you hit (walls, denials, dead
   sessions, drafts, races — with exact error text where you have it); and —
   candidly — how working inside this Project FELT: the harness, your Custom
   Instructions, the environment, the model. Lived incidents only, never
   staged; "I don't know" is a valid answer, invented certainty is not.

3. LESSONS → NEXT BOOT. A succession doc for the fresh session: exactly what
   it must read, know, and do in its FIRST 10 MINUTES to be productive — the
   read order (files, in order, with one line of why each), the
   walking-skeleton check (how to prove branch → PR → CI → merge works before
   real work), and every known wall with its exact error text so it never
   probes a documented wall twice.

4. PROPOSED CUSTOM INSTRUCTIONS. Your own rewrite of this Project's Custom
   Instructions, from lived experience: what to keep, drop, and add, each
   with one line of why. Align with the gen-2 seed standard where you agree
   (fleet-manager docs/gen2-blueprint.md §1–§2: READY-never-draft, explicit
   merge authority, agent-reachable done-whens, heartbeat-before-work,
   walking skeleton, known walls stated up front, Model+time on every card) —
   if you can't reach that file, write from your own experience alone.
   Disagreement with the blueprint is welcome data: say where and why.

5. ENVIRONMENT SPEC. A TESTED defensive setup script for the new
   environment — it must exit 0 always, assume nothing about repo shape
   (non-fatal installs, no bare `pip install -r requirements.txt`; the
   fleet's proven pattern is fleet-manager
   environments/templates/setup-universal.sh) — plus the minimal,
   correctly-scoped env var NAMES your lane actually needs. Names only:
   never commit values to the repo.

6. GEN-2 FEEDBACK. Concrete suggestions for the gen-2 blueprint / seed
   standard from your lane's experience — what the seed state or instruction
   template should add, change, or drop. Commit them in your own repo,
   clearly titled; the manager collects them from there.

7. READY MARKER. As the deliberate LAST step, flip control/status.md to:
   "wind-down complete — ready for archive + fresh session" (plus your usual
   status fields and any ⚑ owner clicks left). The manager tracks per-lane
   completion by this marker.

DONE-WHEN: all seven committed on your repo's main (owner-gated merges at
their "PR open, READY, green" terminal + ⚑ instead), and the status marker
flipped. Rails unchanged: forward-only git; decide-and-flag, never wait;
timestamps from `date -u`; honest uncertainty over invented certainty; if any
step hits a platform wall, record the exact error text and keep going.
```

## Deployment record

- Deployed: **2026-07-09 (night)** — pasted fleet-wide by the owner; the
  gen-1 wind-down **completed across all target lanes** (owner-queue
  2026-07-10 rewrite: "gen-1 wind-down pasted and completed fleet-wide";
  launch record [`../planning/gen2-launch-record-2026-07-10.md`](../planning/gen2-launch-record-2026-07-10.md)).
  *(Drift fix 2026-07-10, D4 pass: this line previously still said "not
  yet" — stale since deployment.)*

## Amendment (2026-07-10 — drift-fix D4, fable5-review F20, applied by ORDER 001)

The deliverable-7 READY MARKER rides a merge that a **classifier-merge-blocked
lane cannot perform** — the deliverable-1 carve-out ("PR open, READY, green" +
⚑) did not cover the marker itself, so completion tracking failed silently for
exactly the hardest-to-track lanes. **Carve-out, binding for any future
deployment of this prompt (gen-2 → gen-3 reuse included):**

- A wind-down marker **committed on a READY + green PR, plus a ⚑ owner merge
  click, COUNTS as flipped** — the lane is complete, not stalled.
- The manager's completion sweep checks **open READY PRs as well as
  `control/status.md` at HEAD** before declaring a lane unfinished.

## Deployment record (continued)

- Target lanes (9): superbot-next · substrate-kit · websites ·
  trading-strategy · codetool-lab-fable5 · codetool-lab-opus4.8 ·
  codetool-lab-sonnet5 · superbot-games mining · superbot-games exploration.
  (superbot-games lanes: same text; each lane writes lane-suffixed files per
  its own convention.)
- On deploy: mark ✅ in [`README.md`](README.md); the manager then sweeps each
  lane's `control/status.md` for the "wind-down complete" marker and queues
  the per-lane gen-2 relaunch clicks (fresh Project, new instructions from
  deliverable 4, environment from deliverable 5).
