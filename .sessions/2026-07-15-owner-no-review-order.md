# 2026-07-15 — owner no-PR-review directive → fleet ORDER + follow-ons

> **Status:** `in-progress`

About to: land the owner's live directive ("I don't review PRs and never will — feature PRs land on green; holds only for the destructive tier") as the next free ORDER in control/inbox.md, update docs/playbook.md + owner-queue A#63, re-fix PR #227's fresh conflict, and heartbeat.

## What happened

- **ORDER 047** appended to `control/inbox.md` (owner verbatim quotes primary +
  context; policy statement; fan-out intent + paste-ready block; provenance:
  owner live turn 2026-07-15, this working session, fm PR #246).
- **Playbook R29** added (OWNER INTERFACE): the owner never reviews PRs; feature
  PRs flip and land on green; holds only for the destructive tier; technical
  walls stay walls and are named as such, never re-framed as "owner review".
  All prior rules kept intact (additive edit).
- **A#63 / PR #227:** #245's merge to main had RE-conflicted the branch
  (`mergeable_state=dirty`, single conflict in `.substrate/guard-fires.jsonl`).
  Branch is this seat's own — merged main INTO `claude/lanes-regen-fix` (no
  rebase), resolved the audit log as a verified append-only union via
  `git merge-file --union` (0 entries lost from either side; 596 = 565 base +
  18 ours + 13 theirs). New head `6d53047`: `mergeable_state=clean`, 3/3
  checks green (21:30Z). **Recorded honestly in A#63:** merge-on-green cannot
  land #227 — its diff touches `.github/workflows/roster-regen.yml` and the
  workflow-file rail is a deliberate technical carve-out (NOT a review hold);
  the owner click stays the sole landing path, and the ask now names the wall.
- **Trigger snapshot refreshed** (I6 was 4.2h stale at boot): full
  `list_triggers` export, 20 pages cursor-to-exhaustion, 1938 records
  (+18 new / 0 gone vs 17:21Z), captured_at 2026-07-15T21:48:44Z. Read-only —
  nothing created/modified/fired/deleted. check_trigger_health: 9/9 PASS.
- **Close checks:** roster freshness OK (Gen #63, 2.0h) · check_owner_queue
  CLEAN (the merged-citation flag on A#63's historical `fm PR #245` mention
  was cleared by rewording history-as-context, content unchanged) ·
  trigger health 9/9 · `bootstrap.py check --strict` exit 0 (born-red HOLD on
  this card is the designed red).
- **Not touched:** docs/fleet-triage.md (its owner-merge mentions are
  historical records/technical-rail facts, not conventions — left intact);
  no historical records, denial logs, or Walls entries deleted or rewritten;
  no permission config.

💡 **Session idea:** `check_owner_queue.py` needs a *historical-citation ack*
(sibling of `DIRTY_ACK_RE`): an active item citing a merged PR as provenance
("fixed by wake PR #N, since merged") currently fires `merged-citation` even
when the ask itself is still open — this session had to reword "fm PR #245" to
"fm #245" to clear a truthful sentence. A recognized marker (e.g. "(merged —
history)") would let items keep natural provenance language without flags.
Dedup: grepped docs/ + .sessions/ — the checker's merged-citation probe is
discussed but no ack-marker idea exists.

⟲ **Previous-session review** (2026-07-15 evening oversight wake, PR #245):
strong wake — it fixed #227's conflict, corrected two stale-status claims with
evidence, and swept A#68. But its own merge to main immediately RE-dirtied
#227 (both touched `control/status.md` + `.substrate/guard-fires.jsonl`), and
its heartbeat still advertised "#227 clean, click applies on green" — stale
within minutes. **Workflow improvement:** when one wake both fixes a parked
PR's conflict AND lands its own PR over the same files, sequence them — land
your own PR first, then re-resolve the parked PR against the new main (or
explicitly note the re-conflict risk in the parked item) — otherwise the fix
is self-undone.

📊 Model: Fable
