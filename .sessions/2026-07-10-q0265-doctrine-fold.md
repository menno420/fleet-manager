# 2026-07-10 — Q-0265 continuous-mode doctrine fold (manager-only rider, part-4 brief §2b)

> **Status:** `in-progress`

📊 Model: fable-5 (family-level, per Q-0262 model-line policy) · start 2026-07-10T20:30Z

## Declared at open (born-red)

Doctrine-fold worker for the fleet-manager coordinator, executing the Q-0265
MANAGER-ONLY rider (superbot `docs/planning/round3-dispatch-part4-brief-2026-07-10.md`
§2b: "the manager folds Q-0265 into the gen-3 blueprint delta + your doctrine ORDERs so
every future seat is born continuous"). Doctrine read at superbot origin/main
`6f283b91` (router Q-0265 block + part-4 brief §2b). About to land, in this PR:

1. **`docs/gen2-blueprint.md`** — changelog entry: the continuous-mode operating
   model (Q-0265) supersedes one-slice-per-wake for production seats.
2. **`docs/prompts/init-prompt-universal.md`** — dated continuous-mode rider
   (born-continuous pattern: work loop, ~15-min `send_later` chain pacemaker where
   available, cron = failsafe wake, backpressure brake, honesty guard); the verified
   arming recipe stays as-is.
3. **`control/inbox.md`** — ORDER 011: the manager seat itself adopts continuous
   mode (failsafe-wake trigger rewording + `send_later` continuation chain); marked
   `in-progress` — a parallel worker is executing it right now.
4. **`control/status.md`** — heartbeat as the deliberate last commit.

Sibling PRs in the same fold job: superbot #1962 (gen-3 deployment standard §2
amendment) + a websites routine-prompt v2 PR.

## Close-out

Landed as declared, three commits on this branch:

1. Born-red card (this file).
2. Doctrine folds — blueprint changelog entry (continuous-mode operating model,
   Q-0265, supersedes one-slice-per-wake for production seats) +
   init-prompt-universal dated rider (work loop · ~15-min `send_later` chain
   pacemaker where available · cron demoted to "<seat> failsafe wake" · backpressure
   brake · Q-0089 honesty guard · free window through 2026-07-14; verified arming
   recipe untouched) + inbox ORDER 011 (manager adopts continuous mode; status:
   in-progress, parallel worker executing).
3. Heartbeat (status.md doctrine-fold record + notes updated: next actions
   ORDER 003 → 007 → 009 → 010 via the continuation chain) + this card flip.

💡 Session idea: the Q-0265 fold now lives in three places (superbot gen-3 standard,
manager blueprint, init-prompt rider) plus six per-seat amendments — a single
`docs/prompts/continuous-mode-rider.md` canonical block that the other homes quote by
link would make the NEXT operating-model change a one-file edit instead of a
three-repo fan-out. Dedup: not in docs/proposals/ or the blueprint changelog.

⟲ Previous-session review: the ~19:50Z critical-finding job (PR #34) was exemplary on
evidence discipline (verbatim probe of `create_trigger`'s schema before claiming "no
model arg") — but it filed ORDER 010 to ride "the staleness sweep" without naming
which wake; under continuous mode (this fold) standing riders should name their
execution hook explicitly, since "the next sweep" is no longer a unique 2-hourly event.
