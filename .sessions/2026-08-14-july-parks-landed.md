# 2026-08-14 — the owner's answers landed: both July parks merged, registry reconciled

> **Status:** `complete` — branch `claude/v1-21-0-phase3-gba-tcvym8` (restarted
> from `ada3820`), records-only: this card, the §7 row and the queue
> resolution. The work it records happened on sim-lab #344, trading-strategy
> #160/#163 and kit #586 and is complete at this card's birth (the fm #856 /
> kit #584 precedent for a small records PR carrying its card complete; no
> separate review round — the recorded work was gate-verified in each repo's
> own venue).

- **📊 Model:** fable-5 · high · docs-only

## previous-session review

Same session, previous PR (fm #858, merged `ada3820`): its claims held —
nothing to correct. The two forks it ended on were answered by the owner live
(AskUserQuestion, 2026-08-14): **no adopter yet** (the v1.21.0 rollout stays
owner-paced; superbot-games and pokemon-mod-lab wait for his word), and
**land BOTH July parks**.

## Shipped (records only — the work lives on the PRs)

- **sim-lab #344 merged @ `f54ec219`** — the required `substrate-gate` was
  already green and the PR clean; `main` IS the squash, 0 open PRs there.
- **trading-strategy #160 merged @ `6cf2e93`** — first the three resident
  capability overclaims holding its required gate red were narrowed in place
  on the branch: `docs/current-state.md:389` (green PRs merge by the owner's
  review pass **or a session he directs** — merging is normal agent work; the
  repo's no-self-armed-auto-merge policy survives untouched),
  `CONSTITUTION.md:166` (the scheduler rule restated positively — the
  v1.20.2 checker reads **any** agents-subject negation as a wall, so
  "must not arm" re-fired the same pattern "do not arm" did), and
  `docs/review-queue.md:8` (#37's July denial dated as the momentary venue
  state it was; the re-check ask itself unchanged). Then merged on its own
  green gate (substrate-gate + pytest).
- **trading-strategy #163 merged @ `b5eba03`** — landing #160 created a
  fresh tree-vs-self-report DRIFT (heartbeat still `kit: v1.17.0`);
  reconciled at the source per the registry protocol, one line → `v1.20.2`.
- **kit #586** — registry regenerated: trading-strategy reads v1.20.2 three
  ways (tree · pin · self-report), honestly stale vs v1.21.0 and
  owner-skipped until its archive decision; pokemon-mod-lab readable
  (v1.15.0) over the direct-egress authed path; superbot-games' 3-file DRIFT
  unchanged — its own upgrade session's item. 9 current · 3 stale.
- **owner-queue:** `OQ-JULY-PARKED-PRS` ✅ RESOLVED same day (both answers +
  merge SHAs recorded in place).

**Account-wide open `claude/*` PRs: 0** — the state `[D-0017]` names as
normal, for the first time since the July parks were created.
**⟲ Corrected minutes after merge (same session): that flat "0" was wrong
at write time.** fm #859 — a parallel owner-live controller-app session's
records PR — was created 10:18:59Z, ten minutes before this card's commit,
and the "0" was composed from the 09:2xZ sweep plus the two landings rather
than re-measured. The precise truth: **0 PARKED `claude/*` PRs** (the class
the ask and the ruling are about) and **1 in flight by a live session** —
which is exactly the open state `[D-0017]` licenses. Same defect class the
estate's own audits name: a gloss composed over a stale measurement instead
of computed fresh.

Venue notes (facts about paths, not walls): the currency tool's API probes
403 through the session proxy — the known proxied-REST quirk; direct egress
cleared it — and its unauthenticated raw read served a stale pre-restamp
copy of the heartbeat, the cached-vs-current defect already filed upstream
on kit #583.

## Verify

- Every merge above probed against the tree (branch-HEAD raw reads: sim-lab
  `main` = the #344 squash; trading-strategy `main` KIT_VERSION 1.20.2 · pin
  1.20.2 · heartbeat v1.20.2), never a PR-object read alone.
- fm gate on this branch: `python3 bootstrap.py check --strict` → exit 0
  (the added-card lane gates on this born-complete card);
  `tools/check_no_false_walls.py --strict` → exit 0 CLEAN. Real exit codes,
  no pipes.

Layer-2 handoff: null (no `docs/repos/<name>/` folders exist for sim-lab or
trading-strategy; their PR threads and the §7 row carry the handoff)

💡 **trading-strategy's next kit hop starts clean:** with the heartbeat
reconciled and the resident overclaims narrowed, a future v1.21.0+ upgrade
there is a pure vendor+pin+regen hop — no doc archaeology left. Worth naming
in the archive-decision conversation: the repo is now cheap to keep current
OR to freeze honestly.
