# 2026-07-26 · hub — plan v2: verification-led consolidation (owner corrected v1)

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-07-26 · venue: owner-live hub chat · branch
`claude/repo-consolidation-plan-jl7z6x` (restarted from main after #541 merged)

💡 Session idea: the owner's two asks — *"consolidate the repos"* and (recorded
five days earlier) *"the highest-value work is verification, not more shipping"* —
are **the same project, and the dependency runs one way**: you cannot safely fold
a repo you have not read. So the conformance pass is not a prerequisite *to* the
merge, it **is** the merge prep. That collapses what looked like two competing
priorities into one sequence, and it is why v2 leads with `superbot-next` rather
than treating verification and the cutover as rivals.

## previous-session review

Same session. #540 landed plan v1; #541 landed the CI companion. The owner then
said, correctly, that I had not read the repo's own docs. I had read ~500 lines
of ~30,000 — roster, 80/930 lines of the owner queue, parts of the closeout, some
READMEs — and built v1 on the GitHub API census instead. This card records the
correction.

## What this commit does (docs-only)

- **`docs/planning/2026-07-26-consolidation-plan-v2.md`** (new) — the live plan.
- **`docs/planning/2026-07-26-fleet-consolidation-plan.md`** — v1 → `historical`
  with a SUPERSEDED banner naming exactly what it got wrong; its census evidence
  is explicitly retained and reused.
- **`docs/owner-queue.md`** — `OQ-CONSOLIDATION-DELETE-VS-ARCHIVE` **RESOLVED = A**
  (open since 2026-07-12), with the time-ordering that falls out of it.
- **`docs/planning/README.md`** — index rows.

## What v1 got wrong, and the doc that said so

| v1 | The record | Source |
|---|---|---|
| "Most valuable: consolidate the bot" (= ship more) | "the highest-value work: **verification, not more shipping**" | `owner-reflection-2026-07-21.md` |
| Archive websites' control-plane | "He reviews through what he can see… build things he can inspect" — it is the review surface | same |
| Derived a structure from scratch | Owner already grouped the fleet into **8 standing Projects** (2026-07-11) | `fleet-triage.md` |
| Asked 3 blocking questions | "**Decide, don't default to asking**" — and 2 of the 3 were already open OQ items with recorded recommendations | `owner-reflection` + `owner-queue.md` |

`current-state.md` literally says *"Read this if you read nothing else:
owner-reflection-2026-07-21.md"*. I walked past the pointer.

## The reframe v2 rests on

**Minimize review surfaces, not repos.** The owner measured his own ceiling:
*"no realistic amount of oversight tooling would let one person truly run more
than ~10 projects; even 8 was heavy."* Consequences that change the answer:
`gba-homebrew` + `pokemon-mod-lab` cost **one** surface (always reviewed
together, copyright forbids merging) — merging them would save nothing; 13
archived repos cost **zero**; and an unread repo costs **more** than one, because
you do not know what is in it. Target: **6 review surfaces**, not 8, because 8
was already heavy.

## The instrument — and the drift is not hypothetical

`shiftlife/docs/plan-conformance.md` already is the "contains vs claims" pass the
owner asked for, and it exists because **"ten self-directed slices once drifted
from [the plan] without anyone noticing, and it took a deliberate audit to find
three missing free-core items"** — in the *newest, healthiest, most-attended*
repo in the fleet. Its honesty bar is the model: *"no notification has ever
fired."* Generalize it: every repo gets `docs/conformance.md` before it is folded
or archived; re-verify against code, name the module and the test per row, and
treat a wrong row as worth more than a tidy table.

Independent confirmation found during v1's census, before any of this was read:
`superbot-games` claims plugin-readiness but ships no `pyproject.toml` and no
`manifest.py`. Claim outran code — found by accident, which is the whole argument.

## Also recorded

- **Live revenue exists** and v1 never mentioned it: Stripe Webhook Test Kit,
  $29 on Gumroad since 2026-07-12, purchase path owner-verified end-to-end
  (`eap-retrospective.md` §1.8). venture-lab is a real money lane, not a folder.
- **Release-before-archive is now time-ordered**, not optional — archiving
  freezes tag-push forever, and cfgdiff + envdrift sit at zero releases.
- `OQ-FM-APPARATUS-SIZING` already held per-workflow verdicts; where it and the
  CI companion doc differ, **the queue item wins** (older, more precise).

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
