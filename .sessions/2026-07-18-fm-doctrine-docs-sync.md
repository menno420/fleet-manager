# 2026-07-18 · fleet-manager doctrine docs sync (#308/#309/#311)

> **Status:** `complete`

About to happen: sync `docs/current-state.md` + any flagged living-doc lines to
the owner's #308/#309/#311 wording (agents merge their own green PRs directly;
merging is normal agent work; never document limitations); make
`check_no_false_walls` pass.

- **📊 Model:** Opus 4.8 · medium · docs-only

## What shipped (Did)
- **docs/current-state.md** — rewrote the merge/landing statements to the #308/#309
  model: the stability-baseline landing note, the "Current state" open-PR bullet, and
  the "Review rhythm" section now say **agents land their own and sibling green PRs
  directly** (MCP/REST `merge_pull_request`, draft→ready flip, or arm auto-merge) as
  normal, non-owner-gated work, with `merge-on-green.yml` reframed as a
  belt-and-suspenders backstop lander. A one-off platform refusal is **transient** —
  attempt once, record the exact error, escalate to the hub chat if it persists, never
  to the owner-queue. Snapshot already dated 2026-07-18 (today).
- **docs/owner-queue.md** — corrected the present-tense false-wall clause in
  `OQ-FM-APPARATUS-SIZING` ("agent-side merge is classifier-denied, so this IS the
  landing path") → merge-on-green kept as a backstop enabler alongside direct agent
  merges.
- **CONSTITUTION.md — untouched** (the guard that would flag it is not planted here);
  flagged for the owner in the PR body that its branch-deletion line ("genuine wall
  (403)") reads more restrictive than #309's verified ledger (branch deletion = CAN,
  204 via the direct-PAT path; only the *proxied* path 403s).
- **Guard gap flagged:** `tools/check_no_false_walls.py` — referenced by #309's ledger
  and `.claude/CLAUDE.md` as a *required* substrate-kit CI guard — **is not planted in
  this repo** and no workflow invokes it; ran the false-wall scan manually instead.
- Left dated historical wall/incident entries in `docs/CAPABILITIES.md` and
  `docs/fleet-triage.md` as historical record (the treatment #308 gave venture's
  superseded entries), correcting only present-tense standing doctrine.
- Verify: `check_owner_queue` EXIT=0 · `check_docs_links` CLEAN (256 files) ·
  `bootstrap check --strict` EXIT=0 (born-red HOLD by design).

## 💡 Session idea
Plant the missing `tools/check_no_false_walls.py` for real (stdlib-only, advisory→
required): a checker that greps this repo's **living docs** (current-state, owner-queue,
CAPABILITIES, fleet-triage, roster) for present-tense wall phrasing — "classifier-denied",
"agents cannot merge", "owner-side merge", "not classifier-gated" — while **exempting
dated historical entries** (a leading `YYYY-MM-DD` on the line/row) so incident records
survive. #309 already *promises* this guard exists and is required; wiring the real thing
into `substrate-gate.yml` closes the gap between the promise and the enforcement, so the
next false wall reds its PR instead of relying on a manual scan like this one.

## ⟲ Previous-session review
PR #306 (`docs/owner-steps-2026-07-18.md`) consolidated every fleet-wide owner-only
step into one payoff-ordered list — genuinely useful hub work. What it missed, visible
only in hindsight of #308/#309 the same morning: a large share of "owner must
merge / ready-flip PR N" steps it routed to the owner are now **agent-ownable**, so the
roll-up over-queued the owner. **System improvement:** the owner-steps aggregator (and
`check_owner_queue.py`) should filter out *mergeable-green* PRs — those are agent work,
not owner steps — which is the same anti-false-wall principle this session applied to
the prose, now applied to the queue-generation logic.

## ⚑ Self-initiated
Flagged (did not fix, out of scope): CONSTITUTION.md branch-deletion line vs #309 ledger
tension (in PR body for owner reconciliation); the absent `check_no_false_walls.py` guard
(session idea above); the pre-existing `seat-digest-stale` advisory (regen is
`python3 bootstrap.py seat-digest`, a derived render of CAPABILITIES/skill-index — left
for a follow-up since it pulls in #308/#311 bytes I didn't author).
