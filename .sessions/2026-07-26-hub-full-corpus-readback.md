# 2026-07-26 · hub — full-corpus read-back: the fleet account, from the documentation itself

> **Status:** `complete`

- **📊 Model:** fable-5 · high · docs-only

Time: 2026-07-26 (evening) · venue: owner-live hub chat · branch
`claude/repo-consolidation-plan-jl7z6x` (continuing after #543 merged)

💡 Session idea: when the builder of a system was autonomous and the owner
directed at arm's length, **neither party holds ground truth — the docs are the
only shared memory**. So before consolidation (a move that erases structure),
the right artifact is a *derived account*: what the record says happened,
citations kept, "record claims" separated from "verified live", contradictions
listed — written so the owner can diff it against his own recollection. The
account is a verification instrument pointed at the documentation itself.

## previous-session review

Same session, two PRs back: #543 landed plan v2 after the owner's first
correction (docs not read). He then corrected twice more: **idea-engine +
sim-lab stay active** (v2 had them as archive material — wrong), and asked for
a full re-review with genuine understanding, ending in broad questions if
needed. Also: model switched opus-5 → **fable-5** this turn.

## What this commit does (docs-only)

- **`docs/fleet-account-2026-07-26.md`** (new) — the read-back: timeline
  (2025-08 → tonight), the operating system, repo-by-repo terminal states from
  each repo's own closeout, money, tonight's live-verified situation, six
  found contradictions, and the seven questions the record cannot answer.
- **`docs/planning/2026-07-26-consolidation-plan-v2.md`** — §7b addendum:
  **OD-4** (ideas/sim active → 7 surfaces, their V-cycle demoted to
  conformance-only) + facts from the read-back that bear on the plan.

## How this was read (method, for the next session)

Shallow-cloned **all 21 sibling repos** (private ones over direct egress with
the PAT — `GIT_CONFIG_GLOBAL=/dev/null` + `x-access-token:$GITHUB_PAT@`,
bypassing the proxy rewrite). Read fm's core narrative corpus in full
(eap-story · retrospective · closeout · reflection · queue · triage ·
playbook · constitution · RESUME · findings), superbot's owner layer (the
9,965-line question-router's all-278 ruling index, fleet-grounding,
8-seat-structure, current-state banner), and **every repo's PROJECT-CLOSEOUT**
(11 exist; sim-lab's heartbeat is its closeout-equivalent). Live-verified
tonight: 12 open PRs fleet-wide (nothing stuck), all 8 deployed surfaces 200,
14 phone-controller releases, shiftlife committing today, trigger snapshot
17-enabled at close vs 1-enabled on tonight's registry page 1.

## Findings worth keeping (the ones that change decisions)

- **`superbot` froze as the behavioral oracle on 2026-07-17** by recorded
  decision — v1/v2's "stop landing work in old superbot" was already policy.
- **Q-0266** made consolidation the *planned* phase 2 of the founding doctrine
  ("volume-first … consolidate later") — today's work is scheduled, not
  corrective.
- **The classifier-scare pattern**: a wrong wall ("agents can't merge") was
  recorded, copied, amplified across sessions, then falsified 2026-07-18.
  The de-wall doctrine (attempt once, never inherit walls) exists because of
  it — and it is the reason `check_no_false_walls` gates this repo's CI.
- **idea-engine/sim-lab have two eras**: fleet ideation (566 idea files, 13
  sections — unreviewed by the owner) and the post-fleet math loop (261
  proposals / 274 verdicts, 4-gate reproduction). Different assets; the README
  alone would mislead a reader into expecting only the first.
- **venture-lab's pre-registered T+14 kill-clock dates to 2026-07-26 (today)**
  — the packet (`launch/kill-clock-decision-packet.md`) awaits the owner's
  call; 0 organic sales measured (Gumroad metrics are owner-visible only).
- **Unverified tonight and worth a sweep:** whether the 10 standing failsafe
  crons enabled at the 07-21 snapshot were actually wiped by the closers
  (registry page 1 shows only a fresh send_later; deeper pages unpaged).

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
python3 scripts/check_docs_links.py
```
