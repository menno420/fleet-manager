# 2026-08-06 · hub — I broke main, the gate that would have caught it wasn't wired

> **Status:** `complete`

- **📊 Model:** opus-5 · high · runtime bugfix

Time: 2026-08-06 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: `docs/CAPABILITIES.md` has said since 2026-07-31 that
`check_no_false_walls.py` *"appears in no workflow — treat the discipline as
self-enforced."* Today self-enforced turned out to mean unenforced, and the
thing it failed to catch was **conflict markers on `main`.**

## What happened

A compound command ran `git commit --no-edit 2>/dev/null` on a **conflicted**
merge. That commit failed with *"cannot commit with unmerged paths"*, the
`2>/dev/null` swallowed the message, and the next clause — `git add -A && git
commit` — staged the conflicted files, markers and all. Pushed, PR'd, merged.

**Impact:** `.claude/hooks/doc-routes.json` stopped parsing, so `route_docs.py`
took its fail-open path and **the doc-routing hook went silent for every session
booting from `main`.** Failing open is the correct design — a hook must never
block work — and it is precisely what made the breakage invisible.

Same defect species as the clamping displacement estimator corrected earlier
today: **an error suppressed into silence is indistinguishable from success.**

## Two gates existed. Neither ran.

| gate | verdict |
|---|---|
| `tools/check_doc_routes.py --strict` | **exits 1 on unparseable JSON — would have caught it exactly.** Wired into no workflow. |
| `bootstrap.py check --strict` | **returned 0** with conflict markers sitting inside `docs/CAPABILITIES.md` |

And I ran both by hand *before* the merge, on a tree where the conflict was not
yet staged. Green, then pushed, then broken. **A pre-merge gate result says
nothing about the post-merge tree** — which is the whole reason CI exists and
the reason running it locally is not a substitute.

## What landed

- **The repair** — `menno420/fleet-manager#795`, markers removed, `main` parses
  again, hook live (20 routes).
- **The wiring** — `.github/workflows/substrate-gate.yml` gains a
  `repo checkers` step running `check_doc_routes.py --strict` and
  `check_no_false_walls.py --strict`. Both are cheap, deterministic and
  judgement-free, which is exactly the tier § 5 of the foundation doc says
  belongs on a hard gate. The heuristic tail stays off the agent's path.
- **The Deep Research exception** — see below.

## Deep Research: the +€7.39 was correct spend, not a routing mistake

The billing snapshot showed real money rising from €0.49 to €7.88 in a day, and
I wrote it up as spend to be explained. The owner supplied the cause: **Deep
Research**, which **is not available through Vertex at all and is not served on
the free key either.** The paid AI Studio key was the only path in existence.

Recorded as a **documented exception** rather than left implicit, because the
obvious inference from a real-money jump — *"a session took the expensive route
again"* — is wrong here, and would send a future session hunting a habit that
does not exist. The `gemini` route now triggers on `deep research` and carries
it.

## Verification

- `git grep '^<<<<<<< '` across the tree → **no markers**
- `python3 -c "json.load(...)"` on `doc-routes.json` → **parses, 20 routes**
- `origin/main` re-checked after merge → **clean, parses, hook live**
- `python3 tools/check_doc_routes.py --strict` → **exit 0**
- `python3 tools/check_no_false_walls.py --strict` → **exit 0**
- workflow YAML parses; the new step is present in the step list
- `python3 bootstrap.py check --strict --require-session-log --simulate-added-card`
  → recorded at close

## Honest nulls

- **The new CI step is unproven against a real failure.** It has never been
  observed going red on a genuine defect; the next broken route table is its
  first real test.
- **`bootstrap.py check --strict` passing on a tree containing conflict markers
  is not investigated here.** It is a kit-side observation, worth a look, and
  nothing in this change addresses it.
- ~~**Whether `substrate-gate` is a *required* check on `main` is still
  unread**~~ — **RESOLVED the same session, and the null was itself a false
  wall.** I wrote that the rules API is "owner-UI state", repeating the kit's
  `check --strict` NOTE (*"403-walled to agents"*) as fact **without testing
  it**. `GET /rules/branches/main` returns **200**. `main` carried a
  `pull_request` rule and **zero** required checks — so the CI step I had just
  added was red-but-not-blocking, exactly as feared. On the owner's decision,
  `PUT /rulesets/18725475` (read-modify-write, preserving the `pull_request`
  rule and empty `bypass_actors`) added `substrate-gate` as a required check;
  **200**, re-verified from the independent effective-rules endpoint. Red now
  blocks the merge.

  Worth sitting with: the last sentence of the session was a wall I had not
  tested, on the day whose whole lesson was that suppressed and untested
  failures look like success. **The doctrine binds its author no better than a
  stranger** — third demonstration in two days.

- **The kit still ships that false wall.** `bootstrap.py check --strict` prints
  the `403-walled to agents` NOTE on every run in every adopter repo. Correcting
  it is a substrate-kit change and is **not** done here.

## ⟲ Previous-session review

Four cards today, and the shape has not changed: a requirement filed where the
reader never looks, a recipe missing its sampling parameter, a funding model
compressed until a free key disappeared — and now a checker that existed,
worked, and ran nowhere. **The estate's failures are not missing knowledge. They
are correct things placed where nothing reaches them.** This one is the cleanest
instance, because the fix is four lines of YAML and the doc had already named
the gap eight days earlier.
