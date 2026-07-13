# 2026-07-13 — Land the owner's FINAL night order (ORDER 040) + Websites dispatch (041) + backup ladder (R27)

> **Status:** `complete`

**Task (worker slice, coordinator-directed):** append the owner's final night
order VERBATIM to `control/inbox.md` as ORDER 040 (standing, P0-tonight); dispatch
TASK 2 to the Websites seat as ORDER 041; condense TASK 3 (manager-backup ladder:
DISPATCH → REVIVE → BACKUP-BUILD) into `docs/playbook.md` as R27; restamp
`control/status.md` to NIGHT-RUN (ORDER 039 + 040) with the backup ladder ARMED.
No trigger calls this slice.

branch: claude/night-final-order

📊 Model: fable-5 (worker seat, night run)

## Shipped (PR #152)

- **ORDER 040** (`control/inbox.md`, standing, P0-tonight): the owner's final night
  order recorded byte-for-byte in a fenced block (unicode spot-checked: `Q-0271…Q-0274`,
  `six-field ⚑`, `CENTRALIZE → SYNTHESIZE`, `§0b`, `~2×` all intact), with the
  manager annotation that the v3.5 stage-1 fold (Q-0271 rider + seed skills) already
  shipped pre-order as PR #151 @ 728dc07 — TASK 1 completes the generation.
- **ORDER 041** (`control/inbox.md`, new, P1, Websites seat): TASK 2 dispatch —
  browsable per-seat prompt version history (v3.3→v3.4→v3.5, view/diff/copy) sourced
  ONLY from the fm registry as the single source of truth; version-aware drift row;
  same data on /prompts, seat pages, owner console as views of ONE source.
- **R27** (`docs/playbook.md` PROTOCOL): MANAGER-BACKUP LADDER — idle-lane detection
  each wake (heartbeat >~2× cadence stale · no fresh commits/PRs · no armed wake),
  rungs DISPATCH → REVIVE → BACKUP-BUILD-at-next-wake ("manager-backup for <seat>" PR
  bodies, lane conventions, one slice per worker, hand-back-on-wake); roster records
  per-lane idle-state + rung fired; owner-authorized exception to OVERSIGHT-ONLY for
  the idle-lane case only; provenance ORDER 040, owner live 2026-07-13.
- **Status restamp** (`control/status.md`): updated 01:32Z; mode NIGHT-RUN
  (ORDER 039 + 040); next-3 = v3.5 completion in flight · ORDER 041 dispatched ·
  backup-ladder ARMED (sweep #1 @01:12Z: all 12 lanes active — no rung fired yet).
- Verify: `bootstrap.py check --strict` red ONLY on the designed born-red hold;
  `check_owner_queue.py` CLEAN.

## 💡 Session idea

**ORDER-sequence linter for the inbox.** Tonight's "verify next free = 040" was a
manual eyeball (`grep '^## ORDER'` + tail) — the exact step a parallel appender can
race: two writers can both read 039 as latest and both append an ORDER 040, and
nothing would catch the duplicate until a human reads the file. Cheap enforcing guard
(friction → guard, superbot Q-0194): a `scripts/check_order_sequence.py` run by the
kit gate that asserts ORDER headers in `control/inbox.md` are unique and that new
numbers are strictly increasing (DONE-flip re-mentions exempt via the `· update`
marker). Deduped: `scripts/` has owner-queue / roster-freshness / trigger-health
checkers but nothing that validates inbox ORDER numbering; no such idea in
docs/proposals/.

## ⟲ Previous-session review

Previous session = v3-rider-fold (#151): strong judgment call — it deliberately did
NOT fold the night-only open-PRs-stay-open rule into the stateless registry, and
hours later the owner's final order (TASK 1) promoted exactly that posture to a
*standing default*, proving the mode-vs-doctrine distinction was worth holding.
Improvement it surfaces: the stage-1 fold shipped without a kept/changed skim page,
so the owner-facing "what changed" now has to be reconstructed at TASK 1 completion —
partial prompt-generation folds should ship their v(N)→v(N+1) skim note *with* stage
1, not defer it to the completing session; the registry restamp checklist should
carry that line.

## Walls

None hit — no platform denials this session. (Not merge-attempted by design: no
self-merge per coordinator instruction; the merge-on-green sweep lands PR #152.)
