# 2026-07-12 — Fleet consolidation + seat reset plan (game-lab seat, proposal)

> **Status:** `complete`

📊 Model: fable-5 · start 2026-07-12T~15:50Z · plan-author worker dispatched by
the game-lab coordinator seat (owner-ordered consolidation program)

## Declared at open (born-red)

Owner-ordered "fleet consolidation + reset" proposal. Inputs: two independent
read-only fleet surveys (A: inventory/products; B: activity/stalls) plus an
adversarial verification pass (corrections binding), all executed
2026-07-12 ~15:23–16:00Z. Deliverable:
`docs/proposals/2026-07-12-consolidation-and-reset-plan.md` (+ a
`docs/proposals/README.md` index for docs-gate reachability), parked READY for
owner sign-off with a codex review requested on the PR. This PR is a PROPOSAL —
nothing in it self-executes; it is never merged by this session.

Expected inputs for a takeover session: the three source reports live in the
dispatching coordinator's scratchpad (survey A, survey B, adversarial
verification), summarized with citations inside the deliverable itself.

## Close-out

Shipped `docs/proposals/2026-07-12-consolidation-and-reset-plan.md`: verified
19-repo fleet map with the verifier's binding corrections folded in
(superbot-next golden-parity red on main; superbot-games status stale vs live
PRs; fable5 zero tags despite its own status claims; superbot-plugin-hello
load-bearing via the superbot-next `plugins.lock.json` pin), disposition
matrix (KEEP / KEEP-INFRA / HARVEST-THEN-ARCHIVE / ARCHIVE-AFTER-CHECKLIST /
PENDING-OWNER-DECISION — **no deletion recommended**; the 2026-07-10 "delete
no repos" ruling vs today's "delete the test repos" ask is surfaced as a Stage
B owner gate with a ≥7-day Stage G cooling-off), stall report with the ≤07-13
decision bundle at the top + the 9 stranded green PRs + red-leg fix
assignments + secrets/toggles, RESET ORDER template + per-seat dispatch list
with the manager-authority note (inbox writes need owner-granted proxy or the
fleet-manager seat), the 8 instruction v1.1 deltas, and execution stages A–G.
Also added `docs/proposals/README.md` (index; docs-gate reachability).
Reconciliation with fleet-manager #118/#119 recorded in both the doc and the
PR body. PR parks READY + green with a codex review requested; per the merge
clause this session never merges it.

## 💡 Session idea

The delete-vs-archive contradiction was only caught because the adversarial
verifier went looking for *prior owner rulings* — neither survey did. Add a
standing "precedent check" step to every owner-facing proposal template: grep
the fleet (superbot docs/, fleet-manager owner-queue/decisions) for earlier
owner rulings on the same nouns before recommending anything, and cite them in
a mandatory "prior rulings" section.

## ⟲ Previous-session review

The dispatching program's survey phase did the independence discipline right
(two surveyors + a verifier, no coordination) — the verifier caught a real
conflict (superbot-next CI) and a dangerous label (TEST-SCRATCH). What it
could have done better: both surveys quoted repo status.md files as activity
truth without checking live PR state; the drift class was already documented.
Workflow improvement: survey prompts should require `list_pull_requests` per
repo, not status.md quotes, for anything feeding a disposition decision.
