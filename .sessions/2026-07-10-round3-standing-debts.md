# 2026-07-10 — Round-3 brief §1 task 1: routines correction + six standing-debt ORDERs

> **Status:** `complete`

📊 Model: Fable 5 · fleet worker (round-3 brief §1, task 1) · start 2026-07-10T11:58Z (`date -u`)

## Declared at open (born-red)

Executing ROUND-3 BRIEF §1 task 1 (superbot
`docs/planning/round3-launch-pack-2026-07-10.md`). About to land in this PR:

1. **(a) SECOND routines correction** — `docs/capabilities.md` + `docs/gen2-blueprint.md`
   §2a: replace "mechanism/recipe pending" with the verified reality — agent-armed
   routines WORK via the claude-code-remote scheduling tools (`create_trigger` /
   `send_later` family), SEAT-DEPENDENT (same per-seat inconsistency class as the merge
   classifier). Evidence: owner screen recordings 11:01Z + 11:04Z — two ACTIVE
   "Created by Claude" routines (trading-strategy 4-hourly, run 10:09; kit-lab hourly,
   runs 12:28/12:28/12:30). Non-Project-surface walls kept VERBATIM.
2. **(b) Six standing debts** from launch-pack §1 appended as ORDERs 001–006 in
   `control/inbox.md`, each with a named next-session owner + done-when (the
   program-review §5.1 doctrine fix).
3. **Debt 5 EXECUTED NOW** — `docs/findings/ping-test-2026-07-09.md` websites
   "❌ NO ACK" row corrected (websites DID ack: PR #44, merged 19:35:59Z, +1h39m
   landed→ack); ORDER 005 marked done.
4. **Debt 6 EXECUTED NOW** — seat-contamination caveat (overnight-review finding 6)
   folded into `docs/experiments/` (README standing caveat + harness-x-model judge
   note); codetool-lab-fable5 release-wall contradiction fixed via a separate small PR
   in that repo; ORDER 006 marked done with pointers.
5. **(c)** `docs/owner-queue.md` — Idea Engine Project item added (launch-pack §5
   routine text pointer); venture-lab = Product Forge after the §4.9 click noted;
   decision items repointed at the launch pack's §4 sheet.
6. **(d)** `docs/dispatch-log.md` — round-3 intake recorded: standing-autonomous-core
   design + the gen-3 gate (no lane relaunch until the owner sees the consolidated
   gen-3 delta report).

Landing: born-red card holds substrate-gate red; flips `complete` as the deliberate
last commit; REST merge-on-green (R21 — born-red shape, no arm attempt).

## Done (close-out) · end 2026-07-10T12:08Z (`date -u`)

All declared deliverables landed (work commit f050fd3 + this flip) on PR #20;
companion PR: **codetool-lab-fable5 #14, MERGED a6cf1a9**.

- **(a)** `docs/capabilities.md` (CAN entry rewritten: mechanism verified —
  claude-code-remote `create_trigger`/`send_later` family, SEAT-DEPENDENT;
  recipe included; WALLED bullet's still-walled clauses kept VERBATIM, plus
  the per-device rider on the owner-console Routines pane) +
  `docs/gen2-blueprint.md` (changelog line; §2a rider mechanism VERIFIED with
  the 11:01Z/11:04Z evidence; §2a ack-count correction 2/9 → 3/9).
- **(b)** `control/inbox.md` — ORDERs **001–006** appended (P1–P11+D4/D5/D6+
  init-prompt rewrite+MISSION.md → next doctrine session; manifest re-stamp +
  generated-roster proposal → next rollup session; review-queue auto-append +
  drainer → next doctrine session; fleet economics ledger BEFORE 2026-07-14 →
  next session of ANY kind, P0; ping-test row fix → DONE; codetool
  reconciliation + seat-contamination fold → DONE), each with owner +
  done-when; header amended with the §5.1 manager-side-append doctrine.
- **Debt 5 executed:** `docs/findings/ping-test-2026-07-09.md` — websites row
  corrected (✅ ACK late, 19:24:41Z discovered / 19:35:59Z on main via
  websites PR #44; landed→ack +1h38m54s) + "§ Correction (2026-07-10)"
  section + conclusion 1 corrected to 3/9 final.
- **Debt 6 executed:** `docs/experiments/README.md` § Standing caveats
  (builder-seats-only scoring; family-level identity at moment of work;
  "model unverifiable" verdict; capability-confound check) +
  `docs/experiments/harness-x-model-2026-07-09.md` judge-note append
  (verification step only; frozen rubric untouched); codetool-lab-fable5
  PR #14 corrected PLATFORM-LIMITS item 4 in place (verbatim denials KEPT,
  verdict → seat-dependent, opus4.8's v0.1.0/v0.2.0 releases cited) + item 8
  scheduler rider.
- **(c)** `docs/owner-queue.md` — new item 0 (create the Idea Engine Project
  on superbot; launch-pack §5 routine-text pointer; venture-lab = Product
  Forge after the §4.9 click, also noted on item 2's rider); decision items
  1/4/6/8 trimmed to stubs pointing at the launch pack's §4 decision sheet;
  item 7 recipe marked VERIFIED (two lanes already armed).
- **(d)** `docs/dispatch-log.md` — "2026-07-10 — midday (ROUND-3 INTAKE)"
  section: six-debts-as-ORDERS, second routines correction, the standing
  autonomous core design (4 permanent ~2-hourly Projects + loop shape), and
  the gen-3 gate (no lane relaunch until the owner sees the consolidated
  gen-3 delta report).

NOT touched (deliberate): `control/status.md` — the manager coordinator owns
the heartbeat overwrite and parallel round-3 lanes may be writing it (R9);
this card + PR #20 + the inbox are this lane's visible record.

Gate: `python3 bootstrap.py check --strict --require-session-log
--session-log <this card>` — the only reds before this flip were the expected
born-red markers (this section clears them).

## 💡 Session idea

**Negative claims about sibling lanes carry a `verify-by:`** — every NO-ACK /
"lane did not X" row in a manager report should embed the exact query that
produced it (the commits-API call, the PR search), so re-verification is one
command instead of a method re-derivation. The websites false NO-ACK survived
two ⚑ flags precisely because checking it meant re-doing the sweep from
scratch; a one-line verify-by would have made the fix a 2-minute act the first
time it was flagged. Cheap to adopt: a template line in the findings-doc
convention, enforceable later by a checker that greps ❌ rows for `verify-by:`.

## ⟲ Previous-session review

The routine-wall correction session (#19) did the hard part right — it kept
the verbatim error texts while narrowing the wall, and its improvement
suggestion (capability walls must name the *surface tested*) was validated
within hours: the mechanism turned out to be exactly the tool family
(`create_trigger`/`send_later`) that IS present on some seats and absent on
others, i.e. a seat property, not a platform property. What it could have done
better: it left "recipe pending" as a passive wait — an active one-call probe
(`create_trigger` from its own seat, outcome recorded either way) would have
resolved the mechanism same-session instead of waiting for owner screen
recordings. Concrete workflow improvement: when a wall flips to "works
somewhere", the correcting session immediately attempts the capability once
from its own seat and records the outcome — turning "recipe pending" from a
flag into a probe.
