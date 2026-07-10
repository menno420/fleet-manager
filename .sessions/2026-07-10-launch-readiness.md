# 2026-07-10 — Launch-readiness compiler (Q-0261 finalize-first checklist)

> **Status:** `complete`

📊 Model: compiler worker for the coordinator's launch-readiness deliverable (seat-based; model line intentionally generic — no model identifiers in this PR)

## Declared at open (born-red)

Compiler worker for the fleet-manager coordinator's launch-readiness deliverable
(owner dispatch, Q-0261 finalize-first relaunch). Five research reports (context
scout · fm+kit · superbot+superbot-next · product lanes · game+codetool lanes,
swept ~15:10–15:40Z at each repo's HEAD) are the source material. About to land
TWO files:

1. **`docs/launch-readiness-2026-07-10.md`** — the ONE committed checklist of
   everything to answer/click/fix/dispatch before each Project relaunches under
   the Q-0261 finalize-first order: fleet-wide items stated once
   (routine-vs-archive decision, kit-version table, settings-API wall), one
   section per seat/repo in Q-0261 order with a one-line verdict each, and a
   final routing table mapping every AGENT-DOABLE item to a boot or an ORDER,
   plus per-class totals. Citations (file@SHA / PR / commit) preserved from the
   research reports on every carried claim.
2. **`docs/owner-queue.md`** — deduped update: the genuinely new owner-only
   items from this research added in the existing six-field format (product-forge
   repo+Project, sixth-seat naming, kit OA8 setup-script paste, settings-sweep
   additions, codetool archive/cfgdiff clicks parked); no valid existing item
   removed.

Landing: born-red card holds the gate red; doc + queue commit next; gate run
(`python3 bootstrap.py check --strict --require-session-log --session-log
<this card>`) before the flip; flip last; PR ready (not draft); REST
squash-merge on the branch's substrate-gate Actions run going green (poll
workflow runs, not commit statuses).

## Done (close-out)

Declared scope landed exactly on PR #30 (born-red `1c09231` → deliverable
`bf8e435` → this flip):

- **`docs/launch-readiness-2026-07-10.md`** (badge `reference`): header with
  purpose/method + the two standing caveats (Q-0261 material branch-only on
  superbot `claude/loving-brown-4ichgw` @ `9b35fc46` / PR #1948 — merging it is
  the round's first agent action; settings-API wall, verbatim); fleet-wide
  section (DECISION F-1 routine-vs-archive with the re-arm-then-delete
  recommendation, kit-version table vs v1.7.0 @ `93c7bdb`, settings wall);
  13 seat/repo sections in Q-0261 order, each with a one-line verdict
  (manager READY-live · kit BLOCKED-ON-10 with OA8+rebind boot-gating ·
  superbot-next BLOCKED-ON-4 + ORDER 008 agent boot-gate · Idea Engine ·
  Product Forge PRE-BIRTH BLOCKED-ON-3 · sixth seat BLOCKED-ON-1 with
  hub-superbot recommendation · websites/trading/venture/games/pokemon/gba/
  codetool×3); routing table (42 items riding boots + 5 routed ORDERs) and
  per-class totals: **38 OWNER-CLICK / 11 DECISION / 47 AGENT-DOABLE**.
- **`docs/owner-queue.md`**: active items 9–12 added (product-forge seed set,
  sixth-seat naming, kit OA8 paste flagged boot-gating, settings-sweep
  superbot-next set with flag-13 moved out of Parked); Parked gains the
  codetool archive-toggle ×3 + paired decision, cfgdiff v0.1.1 two-click
  release, and stale-branch pair; amendment note added at top. Existing items
  untouched.
- Gate: `python3 bootstrap.py check --strict --require-session-log
  --session-log <this card>` run pre-flip — only reds were the expected
  born-red markers (badge + the two enders this section supplies).

## 💡 Session idea

**Give verdict lines a machine-greppable grammar and let the manager's wake
diff them.** This checklist coins `READY / BLOCKED-ON-<n> / N/A-ARCHIVED` with
n = OWNER-CLICK + DECISION count, and the immediate lesson from compiling five
reports was that the per-seat verdict is the only line the coordinator actually
needs at wake time — everything else is drill-down. If each lane's
`control/status.md` carried a standing one-line `readiness:` field in exactly
this grammar (re-graded at each heartbeat), the manager's wake sweep could diff
launch-readiness across the fleet with one grep instead of re-dispatching a
5-worker research round; the next full sweep then only re-verifies lines that
changed. Cheap to adopt: one field in the heartbeat template, enforced by the
same kit heartbeat check that already validates the `kit:` line.

## ⟲ Previous-session review

The 14:36Z wake-heartbeat session (PR #28) did exactly what a first
standing-wake pass should: it verified the routine by the firing itself rather
than trusting the arming record, and its ender-sweep verdict taxonomy
(ENDER-VERIFIED/…/N/A-CLOSED) directly inspired this doc's verdict grammar.
What it missed — visible only now with the five reports side by side — is that
its sweep graded *enders* but not *inbox execution lag*: venture-lab's three
unexecuted ORDERs and superbot-games' unacked P0 were already sitting there at
14:36Z and the wake record doesn't surface them. Concrete improvement: the
standing wake prompt's sweep step should grade each repo on BOTH axes — ender
state AND oldest-unacked-ORDER age — since the second axis is where this
research found every real boot risk.
