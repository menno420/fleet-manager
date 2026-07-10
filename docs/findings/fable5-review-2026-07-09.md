# Fable-5 fleet review — 2026-07-09/10 (ultracode corpus review, 30 confirmed findings)

> **Status:** `reference`
>
> The synthesis record of tonight's Fable-5 ultracode fleet review. Method:
> the full fleet corpus (all 10 lanes' succession packages, prompts, findings,
> blueprint, playbook) was digested at HEAD, candidate findings were generated
> per dimension, and **every finding below survived an independent adversarial
> verification pass against the repos at HEAD** (fetch-before-read, playbook
> R2) — 30 of 30 confirmed `isReal`. Verify against repos before acting (R2
> applies to this doc too). Companion deliverables landed in the same PR:
> 10 PROPOSED gen-2 instruction packages in
> [`../proposals/instructions/README.md`](../proposals/instructions/README.md)
> and 3 captured ideas in [`../ideas/README.md`](../ideas/README.md).
>
> **Ownership note:** the blueprint amendments in §7 are **PROPOSALS ONLY** —
> this session did NOT edit `docs/gen2-blueprint.md`, `docs/playbook.md`, or
> `docs/owner-queue.md`. The next blueprint edit is owned by the CI-tier sim
> session; it should absorb §7 in one pass.

---

## 1. Executive summary (for the owner — plain language)

Tonight the fleet finished gen-1 and adopted the gen-2 "born-right" blueprint.
This review read everything the fleet wrote and checked every claim against
the actual repos. The headline: **the blueprint is sound, but a handful of
its merge-mechanics sentences don't match how GitHub actually behaves, and
the venture-lab instructions you're about to paste contain one of those
sentences.** Nothing is broken beyond repair — every problem below has a
one-edit fix, and none of them require you to do anything technical.

What matters most, in order:

1. **Don't paste the venture-lab instructions yet.** The finalized text tells
   the lane to use a merge path that GitHub will refuse on every one of its
   PRs (three separate confirmed findings agree). It's a one-paragraph fix; a
   corrected full package is already drafted in `docs/proposals/instructions/
   venture-lab.md`. Same for the launch click-list: owner-queue item 14 still
   tells you to *create* the venture-lab repo, but it already exists — you'd
   hit a name collision at step 1.
2. **The self-merge law needs a "what if the platform says no" line.** Your
   directive that lanes always land their own PRs is good policy, but the
   platform sometimes refuses anyway (it refused different lanes differently
   on the same day). Today a refused lane has no legal move. The fix is a
   short script: stop at the first refusal, leave the PR ready and green,
   flag you. Already written into all 10 proposed instruction packages.
3. **Nobody is assigned to read the post-merge review queue.** "Merge now,
   review later" only works if someone actually does the "later." A standing
   drainer (idea captured tonight) closes the loop.
4. **The fleet doesn't know what it costs to run.** The wake-cadence design
   was built during the free window that closes 2026-07-14. Before it closes,
   a small cost ledger (idea captured) gives you a real number to steer with.
5. **Seeding new lanes should be automated.** Ten-plus repos need the same
   birth kit; hand-seeding each one re-creates the divergence gen-2 exists to
   kill. A "seed-lane" tool (idea captured) makes every lane born from the
   same tested seed.
6. **Ten ready-to-review instruction packages** for every gen-2 lane now live
   in `docs/proposals/instructions/` — all marked PROPOSED, none deployed.
   Each one already has the fixes from this review baked in. Nothing changes
   until you paste.

---

## 2. Dimension: instructions (founding texts & prompts) — 9 findings

| # | Severity | Target | Finding (one line) | Disposition |
|---|---|---|---|---|
| F1 | high | venture-lab draft | "Arm auto-merge AT PR creation" collides with its own born-red card mandate; R21 (same night, same repo) documents the arm as structurally refused there; walking-skeleton done-when unreachable at launch | **Drift-fix D1** (pre-paste edit); fixed in proposed package |
| F4 | high | venture-lab draft MERGE AUTHORITY | Grant claims the wall "blocks only the direct self-merge call" and forbids every hold mechanism, but the classifier denies more than that and ignores relayed grants — a denied lane has no sanctioned behavior | **Drift-fix D1** + blueprint proposal **P3**; refusal script in all 10 packages |
| F13 | high | venture-lab draft vs R21/blueprint §1 | The paste-verbatim text contradicts the binding blueprint's own R21-aligned spec for it (arm primary vs REST primary) — it directs a documented-wall probe on every PR | **Drift-fix D1** (same one-file edit) |
| F17 | med | venture-lab draft | Blueprint deltas absent: spawn-liveness watchdog + worker hygiene (fresh clone per worker, 10-min child liveness) — exactly the fan-out shape venture-lab will run | Fixed in proposed package (WORKERS block); **D1** rider |
| F19 | med | opus4.8 PROPOSED-CUSTOM-INSTRUCTIONS ADD #2 | Lane's own proposal says "build sessions do NOT self-merge" — written blueprint-blind, now the direct opposite of fleet law; pasting deliverable 4 as-is founds a law-violating lane | **Relaunch rule R-a**: re-base every lane proposal on the blueprint at paste time; superseded by proposed codetool package |
| F21 | med | init-prompt-universal + venture-lab WAKE | Texts assert "a routine will wake you" as fact, but routine creation is an owner-only click never performed in gen-1 (7/9 lanes never acked; the owner's next prompt was the de-facto wake) | Conditional phrasing applied in all 10 packages; **D5** for deployed prompts; re-scope item 11's wall claim |
| F23 | med | venture-lab draft landing path | Same R21 contradiction, confirmed independently from the prompts ledger — the lane's prescribed path to "PR merged on green" fails on every real PR | **Drift-fix D1** (dedup of F1/F13) |
| F24 | med | websites proposed instructions | No measurable done-when and no between-orders standing default (delta 8 violation), and ORDER 005 — the lane's #1 trap — isn't in the mission text a waking session reads first | Fixed in proposed websites package (FIRST STANDING GOAL + standing default) |
| F28 | med | all gen-2 relaunch texts vs delta 8 | Only 2 of the committed lane proposals implement done-when + standing default; sonnet5's even has a [FILL] placeholder — the law would be violated at birth by most lanes | Blueprint proposal **P9** (paste-time 3-line lint); lint applied to all 10 packages; games-exploration = reference implementation |

## 3. Dimension: goals & done-when — 6 findings

| # | Severity | Target | Finding (one line) | Disposition |
|---|---|---|---|---|
| F16 | med | venture-lab MISSION | "First revenue" is owner-gated by the lane's own HARD RAILS, so the mission as stated has no agent-reachable terminal state | Fixed in proposed package (agent-reachable mission done-when sentence); **D1** rider |
| F20 | med | gen1-winddown prompt deliverable 7 | Completion marker rides a merge a classifier-blocked lane cannot perform; the deliverable-1 carve-out doesn't cover the marker — tracking fails silently for exactly the hardest-to-track lanes | **Drift-fix D4**: amend the marker clause; manager completion sweep checks open READY PRs too |
| F22 | med | venture-lab mission metrics | "First revenue" never quantified, "validated" undefined, no candidate kill criterion, no budget line — the lane can honestly run forever | Fixed in proposed package (mission milestone + per-candidate kill rule) |
| F25 | med | fleet-manager (the manager itself) | The manager holds every lane to delta 8 but has no mission sentence, no phase-2 done-when, no standing default of its own | **Drift-fix D6**: add a MISSION block (handoff top or `docs/MISSION.md`) — queued for the manager session |
| F26 | med | mobile-lab idea | Captured idea is a capability description, not a mission: no first app, no done-when, spend/tester rails unstated | Fixed in proposed mobile-lab package (fleet-status companion app; owner-QR-confirmed done-when; free-tier rail) |
| F27 | med | trading-strategy proposal | No validation threshold (candidate → finding undefined), no standing-default line, and relaunch is 100% gated on the pinned-research environment — unstated | Fixed in proposed trading package (walk-forward promotion rule; QUEUE.md standing default; env dependency first) |

## 4. Dimension: feedback-synthesis (lane feedback the blueprint hasn't absorbed) — 9 findings

| # | Severity | Target | Finding (one line) | Disposition |
|---|---|---|---|---|
| F2 | high | playbook R21(a) + blueprint §1 | "Arm structurally impossible on born-red repos" over-generalizes one late-arm incident; substrate-kit armed successfully ~dozens of times **inside the pending window** — the variable is arm timing (+ required-check config), not repo class; the Tier-2 rider would push production lanes onto session-alive polling | Blueprint/playbook proposal **P1** (reword + one live arm test during pending) |
| F5 | high | blueprint §1 + delta 1 | Third repo shape uncovered: on normal-CI repos the arm fails BOTH ways ("unstable status" while pending is NOT a failing-checks signal; "already clean" on green; fast checks → near-zero window); MCP-created PRs never trigger the enabler | Blueprint proposal **P4** (exploration's exact fallback clause + arm-yourself note + misleading-error warning) |
| F6 | high | blueprint §1 merge authority + delta 2 | No refusal branch for classifier POLICY denials (denied inconsistently per seat, same repo same day; retry is itself flagged); founding texts even forbid the fallback — a denied seat's terminal state is literally undefined | Blueprint proposal **P3** (first-denial-stop script: PR READY + green, refusal verbatim in status, ⚑ owner click, review-queue line) |
| F7 | high | blueprint §2 delta 3 (release path) | The "sanctioned" Actions release route is NOT uniform: fable5 denied twice (once with owner authorization on record) while opus4.8/kit shipped 9 releases through it | Blueprint proposal **P5** (seed generic release.yml + birth-time capability probe, result recorded in the lane's conventions; owner-manual tag ritual as fallback) |
| F8 | high | blueprint §2 delta 4 + §2a | Spawn-liveness watchdog unfollowable where no scheduler primitive exists (surface-dependent; sleeps blocked/exited early) | Blueprint proposal **P6** (watchdog gated on a boot-time verified scheduling tool; named substitute = event-driven checks + routines as the fleet's clock; keep "the routine IS the liveness design") |
| F9 | high | blueprint (distribution) | Two lanes could not read the blueprint they were ordered to align with (out-of-scope repo; verbatim Access-denied); ORDER 005 required rendering content no lane session can read | Blueprint proposal **P7** (every referenced doc committed/copied into the lane's repo, OR orders declare read-repos and the manager checks the allowlist at dispatch; mirror the §1–§2a excerpt into each seed) |
| F18 | med | blueprint §1 Model line | "Model on every card" is unsatisfiable on policy-restricted seats (two lanes hit it) — a lane must violate its founding text or harness policy every session | Blueprint proposal **P8** (opus4.8's amendment: model where policy allows, else the literal token "withheld per session policy"; owner keeps the lane→model map) |
| F29 | med | blueprint delta 9 + riding rule 3 | Heartbeat economics need numbers and wiring: fast lane must ship in SEED CI paired with the scoped status gate; "max one status PR per session"; born-red card already satisfies heartbeat-before-work | Blueprint proposal **P10** |
| F30 | med | blueprint §1 claims dir + delta 5 | Prose claims don't stop 90-second races, and a claims dir can't catch an order that names two executing lanes | Blueprint proposal **P11** (CI lint for unclaimed cross-lane touches + "ONE executing lane per shared-ground order" dispatch rule) |

## 5. Dimension: consistency & drift (wrong state on record) — 3 findings

| # | Severity | Target | Finding (one line) | Disposition |
|---|---|---|---|---|
| F3 | high | blueprint §2a vs §3 | Class-A "no-op wake = heartbeat, no PR" is impossible on the PR-required main §3 itself mandates (GH013 class); kit's D4 flagged it, unreconciled; venture-lab WAKE inherits it verbatim | Blueprint proposal **P2** (define the cheap heartbeat per ruleset reality: carve out an unprotected control lane, or state the cost as "fast-lane PR round" and delete "no PR") |
| F14 | high | owner-queue item 14 | Step 1 still tells the owner to CREATE the venture-lab repo; it exists (seeded `d065c68`, PR #1 already landed, live repo is PUBLIC not private as step 1 says) — a non-coder hits a name collision at step 1 | **Drift-fix D2** (owner-queue.md is out of scope for this PR — queued for the manager: strike/mark step 1 DONE, state which settings were applied at seeding, reconcile visibility, leave only the real remaining clicks) |
| F15 | high | handoff (websites, 2 places) | Handoff claims ORDER 005 pages are "building under re-dispatch"; websites wound down 20:23:31Z with 005 acked-but-UNEXECUTED — the successor's first-read asserts work in flight that nobody is doing | **Drift-fix D3 — FIXED IN THIS PR** (both handoff lines corrected; the order itself rides the gen-2 relaunch) |

## 6. Dimension: new ideas (verified, none previously captured) — 3 findings

| # | Severity | Idea | Disposition |
|---|---|---|---|
| F10 | high | **Review-queue drainer** — the post-merge review law has no one obligated to drain `review-queue.md`; without a drainer, "review is post-merge" silently degrades to "review is never" | Captured → [`../ideas/review-queue-drainer-2026-07-10.md`](../ideas/review-queue-drainer-2026-07-10.md) |
| F11 | high | **Lane-seeder automation** — 9 relaunches + new lanes each need the full §1 seed state; hand-seeding ×10 re-creates the divergence tax (three arms wrote three walls-doc formats) | Captured → [`../ideas/lane-seeder-automation-2026-07-10.md`](../ideas/lane-seeder-automation-2026-07-10.md) |
| F12 | high | **Fleet economics ledger** — the wake-cadence architecture was designed inside a free window closing 2026-07-14 with zero cost data; the owner has no number to steer with post-EAP | Captured → [`../ideas/fleet-economics-ledger-2026-07-10.md`](../ideas/fleet-economics-ledger-2026-07-10.md) |

---

## 7. Blueprint amendment PROPOSALS (for the next blueprint edit — owned by the CI-tier sim session)

**Do not apply piecemeal; absorb in one pass.** Sources: §4 table above,
verbatim verdict evidence in the review corpus.

- **P1 (F2):** Reword R21(a)/§1: arming fails once the born-red gate has
  *reported* failure; arm inside the initial pending window (kit-proven) or
  REST merge-on-green after the flip. Include one live arm test on a born-red
  PR during pending before finalizing (required-check config is a co-factor).
- **P2 (F3):** Define the sanctioned cheap no-op-wake heartbeat concretely:
  (a) unprotected status/control lane carved out of the ruleset, or (b) accept
  "fast-lane PR round (~7–30s CI)" as the stated cost and delete "no PR" —
  update §2a, riding rule 3, and every founding-text WAKE paragraph together.
- **P3 (F4+F6):** Add the scripted refusal branch to the merge-authority
  block: on the FIRST classifier denial never retry or reframe; leave the PR
  READY + CI green; record the refusal verbatim in status; flag the owner
  click; done-when degrades to "PR open, READY, green" + a review-queue line.
  Also fix R12's now-falsified "wall blocks only the direct merge call" and
  the founding texts' "never hold a PR" absolutism.
- **P4 (F5):** Amend §1 + delta 1 with the third shape: "arm at creation; if
  arming fails both ways (pending-reads-as-failing / already-clean — known
  wall), squash/REST-merge directly on green — record which path fired." Note
  MCP-created PRs never trigger an enabler workflow (arm yourself), and that
  the pending-state "unstable status" error is NOT a failing-checks signal.
- **P5 (F7):** Delta 3: seed every gen-2 repo with the generic `release.yml`
  (workflow_dispatch, contents:write) AND run a birth-time release-capability
  probe whose result (granted / owner-manual) is written into the lane's
  conventions file; document the owner-manual tag ritual as fallback; never
  present the Actions route as universally granted.
- **P6 (F8):** Delta 4: the spawn watchdog applies only where a scheduling
  tool is verified at boot; otherwise the founding text names the substitute
  (event-driven checks + manager ping cadence / owner routines as the clock)
  and forbids improvised sleep-timers (without colliding with R4's sanctioned
  short waits). §2a's "the routine IS the liveness design" stays primary.
- **P7 (F9):** Distribution rule: every doc a founding text or order
  references must be committed (or copied) into the lane's own repo, OR the
  order declares its read-repos and the manager checks the session allowlist
  at dispatch. Mirror the blueprint §1–§2a excerpt into each gen-2 seed.
- **P8 (F18):** Model line: "model per agent where session policy allows;
  otherwise the literal token *withheld per session policy* — never guess,
  never omit silently"; the owner maintains the lane→model mapping.
- **P9 (F28):** Add the delta-8 paste-time lint to §3 owner setup: (1) mission
  is one actionable sentence, (2) measurable agent-reachable done-when,
  (3) named between-orders standing default. Reference implementation:
  games-exploration's closing line.
- **P10 (F29):** Delta 9 numbers: fast lane ships in SEED CI wired to the
  scoped status gate; "max one status PR per session, batched into
  substantive PRs"; heartbeat-before-work is satisfied by the born-red card;
  direct-commit status lane sanctioned for one-writer control files.
- **P11 (F30):** §1/delta 5: seed a machine check (CI lint for cross-lane path
  touches without a claim + duplicate/stale-claim advisory) and the dispatch
  rule "an order touching shared ground names exactly ONE executing lane."

## 8. Drift-fix list (state corrections, smallest-edit-first)

| # | File | Fix | Status |
|---|---|---|---|
| D1 | `docs/prompts/venture-lab-draft.md` | Replace the GIT/PR bullet with the R21 repo-shape rule (REST primary on born-red/no-CI; never retry a refused arm); add the refusal script (F4), the agent-reachable mission done-when (F16/F22), and the WORKERS block (F17) — or supersede the draft with [`../proposals/instructions/venture-lab.md`](../proposals/instructions/venture-lab.md) | **QUEUED — must land before the owner pastes** (owner-queue item 14 step 3 says paste verbatim) |
| D2 | `docs/owner-queue.md` item 14 | Rewrite the click-list against seeded reality: step 1 DONE (`d065c68`), state which settings applied at seeding, reconcile the public-vs-private mismatch, keep only Project/environment/routine/boot | QUEUED (file out of scope for this PR) |
| D3 | `docs/handoff-2026-07-09.md` websites ×2 | "building under re-dispatched ORDER 005" → wind-down complete 20:23Z; 005 acked, UNEXECUTED, unclaimed; rides the gen-2 relaunch | **FIXED in this PR** |
| D4 | `docs/prompts/gen1-winddown-universal.md` deliverable 7 | Marker carve-out for merge-blocked lanes ("marker committed on a READY+green PR + ⚑ merge click counts as flipped"); manager sweep checks open READY PRs as well as `control/status.md` at HEAD | QUEUED |
| D5 | `docs/prompts/init-prompt-universal.md` | Routine promises → conditional ("if no wake within 2× cadence, assume no routine armed — flag ⚑, operate self-terminal"); re-scope owner-queue item 11's "no agent API surface" wall to the surfaces actually probed | QUEUED |
| D6 | manager mission (handoff top or `docs/MISSION.md`) | Give the manager its own delta-8-compliant mission + phase-2 done-when + standing default (F25 wording is ready to paste) | QUEUED |
| R-a | relaunch checklist rule | Every lane's proposed instructions are re-based on the blueprint at paste time (most were written blueprint-blind — F19's opus4.8 ADD #2 is the proof case); the 10 packages in `docs/proposals/instructions/` are already re-based | Adopted by the proposals README |

---

*Corpus: scratchpad `fable-review/` digests + `confirmed-findings.json`
(30 findings, all verdicts `isReal: true` with full verification notes).
Finding numbers F1–F30 are 1-indexed over that array; the 10 proposal
packages cite the same numbers.*
