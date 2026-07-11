# 2026-07-11 — gen_roster.py mechanization (work-ladder item 8)

> **Status:** `in-progress`

📊 Model: Claude (Fable family, fable-5) · start 2026-07-11T~05:2xZ · lane
worker dispatched by successor coordinator cse_012o8pySy5K3AV6JWoPKryZL

## Declared at open (born-red)

Scope: mechanize the R25 roster regeneration as **`scripts/gen_roster.py`**
(the owed follow-up from ORDER 009 / roster gens #1–#4, handoff §7 ladder
item 8): ingest a `list_triggers` JSON export (`--triggers triggers.json`,
documented schema, loud fail on mismatch), fetch each lane repo's
`control/status*.md` heartbeat over git transport with the MANDATORY
ls-remote verify loop (stale-clone-pack doctrine), regenerate `docs/roster.md`
in the established gen-N format + a `--check` drift mode. Stdlib + git
subprocess only. Verify against the real gen #4 before landing; the
deliverable is the TOOL — a machine gen #5 ships only if the diff is clean
and meaningful. Heartbeat `control/status.md` as the batch's last step; flip
this card `complete` as the final commit; REST squash-merge on green (R21).
