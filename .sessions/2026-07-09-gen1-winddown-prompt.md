# 2026-07-09 — gen-1 wind-down universal prompt (fleet-wide gen-1 → gen-2 refresh)

> **Status:** `complete`

📊 Model: Claude Fable 5 (claude-fable-5) · worker session · docs/coordination

## Declared at open (born-red)

Owner-directed 2026-07-09 evening: the fleet-wide gen-1 → gen-2 refresh
(blueprint §4 natural-boundary migration). This PR ships:

1. `docs/prompts/gen1-winddown-universal.md` — ONE universal paste-ready
   wind-down prompt for every gen-1 Project (7 succession deliverables +
   done-when).
2. Owner-queue item: paste the prompt into each gen-1 Project (raw link,
   WHAT/WHERE/HOW/WHY/UNBLOCKS per R16/R17).
3. `docs/prompts/README.md` index row.
4. `docs/handoff-2026-07-09.md` in-flight note.
5. Playbook **R20** — a mid-flight scope addition to a running session is not
   delivered until acknowledged (provenance: PR #8 merged 19:31Z with the
   19:23Z Task-4 comment unread).

## Done (all five, this PR)

- Prompt authored to match the venture-lab-draft voice (fenced paste-verbatim
  block, standing-ritual register): guidance-not-orders preamble, the 7
  succession deliverables (finish/park with owner-gated terminal carve-out ·
  project review incl. how the Project FELT · lessons→next-boot first-10-min
  doc · proposed Custom Instructions keep/drop/add vs blueprint §1–§2 ·
  tested exit-0 environment spec with env var NAMES only · gen-2 feedback
  committed lane-side · control/status.md ready marker), and an explicit
  done-when. Deployment record lists the 9 target lanes + the manager's
  post-deploy sweep.
- Owner-queue item 15 with the raw-file link and R16/R17 fields; prompts
  README row; handoff in-flight bullet; playbook R20 appended in R18/R19
  format with the WHY.
- Friction (R8 realized): `enable_pr_auto_merge` at PR creation failed on
  GraphQL rate exhaustion — fallback per brief: foreground CI poll + REST
  merge-on-green.

## 💡 Session idea

**Ack-required dispatch wrapper:** R20 makes "unacknowledged = undelivered"
policy, but nothing *checks* it — a tiny `tools/check_unacked.py` (given a PR
number or inbox path, diff scope-addition timestamps against the session's
last read/ack evidence at HEAD) would let the manager sweep for evaporated
mid-flight additions mechanically instead of discovering them post-merge, the
exact way PR #8's Task-4 comment was lost. Cheap: both timestamps already
exist in the GitHub API.

## ⟲ Previous-session review

The ping-ack/gen-2 session (PR #8) was strong: it turned an asserted design
(§2a cadence) into a measured one and finalized two paste-ready artifacts —
this session reused its venture-lab voice wholesale, which is the template
system working. Its genuine miss is R20's own provenance: it merged at 19:31Z
with a 19:23Z Task-4 scope comment unread — not carelessness but a real gap
(no convention obliged it to re-poll its own PR thread). Improvement shipped
this session: R20 makes the delivery rule explicit (ack or re-dispatch), and
the session idea above proposes the mechanical check.
