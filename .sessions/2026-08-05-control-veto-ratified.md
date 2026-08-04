# 2026-08-05 · hub — the control/ resolution, owner-ratified

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only — close the ⚑ flag the owner declined
  to veto

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1` (restarted from main post-#723)

💡 Session idea: **a decide-and-flag item needs a closing edit, not just a
closing sentence.** The flag was raised in the tree and answered in chat; had
this session ended there, the tree would still read "⚑ flagged for veto" while
the veto window had in fact closed — and a future session would either
re-litigate a settled call or treat a live flag as decoration. The pattern
worth keeping: **the same surface that carries the flag carries its
resolution**, stamped with who settled it and when.

## previous-session review

`2026-08-04-hub-final-three-skills.md` (PR #723, merged) landed the last three
routed-to skills. En route this session also merged the two open substrate-kit
PRs the owner asked to be reviewed — #565 (PL-014, a measured claim carries its
instrument) and #552 (T5 headless guard-observability step) — both verified
green against current main locally before merge (2116 tests, all gates exit 0),
kit `main` re-verified green after.

## Scope

Owner: *"You can follow your recommended action on the veto."* The recommended
action was that the resolution stands. This card records the veto declined and
stamps the four venue notes accordingly. No behaviour changes — the notes
already directed sessions away from `control/`; only their status changes from
*pending veto* to *ratified*.

## What landed

- The four venue notes (`prep-owner-steps`, `release`, `scope-backlog-item`,
  `session-close`) now read **owner-ratified 2026-08-05, veto declined**
  instead of ⚑ pending. Substance unchanged: `control/` stays seat-era
  historical here, the session card and PR description carry claims/status and
  baton/records, and `control/README.md`'s OWNER-ACTION field contract remains
  valid as a format reference.

## Honest nulls

- **The ratification is of the resolution, not of each skill's rewritten
  flow.** The notes remain notes on top of kit-shipped text; the underlying
  skills still describe `control/` writes in their bodies. Folding the guidance
  into the steps themselves is kit-side work and is not attempted here.
- The four notes have not been exercised by a session that actually needed a
  `control/` write since they landed yesterday.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
