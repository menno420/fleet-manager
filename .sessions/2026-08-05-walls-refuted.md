# 2026-08-05 · hub — refute three "verified walls" with one reversible probe

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/fleet-superbot-state-audit-24ra4p`

💡 Session idea: the ledger's own WALLED section said *"re-probe once a
direct-PAT session is live."* Every session since 2026-07-22 has been one. The
probe took ninety seconds and refuted three entries — the instruction to test
was sitting inside the record it would have corrected.

## Previous-session review

This session spent the day finding documents that had already concluded and
stood in for a measurement. This is the same shape in the capability ledger:
three rows recorded as walls, one of them endorsed as *"genuinely still true"*,
none of them re-tested after the access model changed.

## Scope

Owner directive, live: *"Branch deletion should never be a wall, the github PAT
has full scope and --noproxy removes any 403."* Probe the whole class that
claim covers, not just the row he named, and append the result.

## What landed

- `docs/CAPABILITIES.md` — an append-log entry refuting three rows in the
  "Walls — verified blocked" section, voiding the "genuinely-still-true walls"
  endorsement that cited branch deletion, and recording the owner's statement
  that both tokens are full unrestricted account-scoped.

## Measured

One reversible probe against `menno420/fleet-manager`:

| Recorded as | Actual |
|---|---|
| Tag push / release create — "HTTP 403 from the git proxy" | `POST git/refs` tag → **201** · `POST releases` → **201** |
| Branch deletion — "403 on every path (git push `:branch` and API)" | create → **201** · `DELETE` → **204** |

Cleanup verified: release `DELETE` 204, tag `DELETE` 204, both refs then
`GET` → 404. A merged branch was separately deleted in `substrate-kit` the
same session → 204.

**The rows were not merely stale — one was endorsed.** Line ~644 lists branch
deletion among *"the genuinely-still-true walls"*, which is exactly the shape
that stops a session re-testing: not an old claim, a *renewed* one.

**`CONSTITUTION.md` has been right the whole time** — *"204 via the direct-token
path (only the proxied path 403s)"*. Two binding documents contradicting each
other, and the wrong one carried the endorsement.

## Verification

- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- `python3 bootstrap.py check --strict` → **exit 0**, run **post-commit**.
- Probe reversible by construction; every created ref deleted and its absence
  confirmed by a 404 rather than assumed.

**Honest nulls.** The probe covered the **API** path only. `git push --tags`
and `git push :branch` over the configured remote were **not** tested, so the
seed row's "git push `:branch`" clause is unrefuted on its own terms — though
the API half of the same sentence is false. Tag/release creation was tested on
`fleet-manager`; repos with different rulesets may behave differently, and
`superbot`'s protected `main` was not probed.

## ⟲ Previous-session review

The whole day has produced one shape repeatedly: a document that had already
concluded standing in for a measurement. The read-list, the dependabot
dismissal, the two-week PR protected by a "open BY DESIGN" note, and now three
walls with a "still true" endorsement. In every case the check was under two
minutes and the stopping force was prose.

## 💡 Session idea

**Make the ledger's own re-probe instructions executable.** The WALLED entry
said *"re-probe once a direct-PAT session is live"* — a correct, specific,
cheap instruction that sat unexecuted for three weeks because nothing turns a
sentence into a task.

Entries that name their own retest could carry it as a runnable line, the way
skills already carry `grounds`. Then `check_stale_walls`, which already flags
these rows by age, could print the exact command beside each one instead of
only the age. The finding here is not that the walls were wrong — it is that
the ledger **knew how to find out** and had no way to make that happen.
