# 2026-07-13 — R27 detection amendment (first-execution lessons)

> **Status:** `complete`
> **Branch:** `claude/r27-detection-amendment` · PR #155
> 📊 Model: fable-5

## What happened

Folded tonight's first live R27 execution (2026-07-13 ~02:36Z, pokemon-mod-lab
— rung 1 dispatched, then withdrawn as a verified false positive; pml PR #60
closed-with-reason) into `docs/playbook.md` as a **DETECTION** sub-note on R27:

- idle detection must read heartbeats AND inbox state across `main` AND all
  open PR heads (open-PRs-stay-open posture → freshest heartbeat can live on
  an unmerged head; main-only sweeps manufacture false DEAD-WAKE positives —
  newest-heartbeat-wins now cited explicitly);
- check the CURRENT trigger registry for seat-consolidation before declaring
  a wake dead (pokemon → Game Lab shared-seat failsafe `trig_01LZ37j6…`,
  verified firing);
- check in-flight appends on OPEN PR heads before assigning a "next free
  ORDER number" (the ORDER 007 collision with pml PR #58);
- a rebuttal from the target seat is a Q-0120 LEAD: verify each claim at live
  GitHub; all-confirmed → withdraw with a one-line reason.

Also restamped `control/status.md` (`updated:` → 03:05Z) and recorded in
next-3: R27 first execution = false positive on pokemon-mod-lab, withdrawn
after verification; lesson folded into R27; residue = stale branch
`claude/fm-r27-wake-repair` in pml awaiting owner delete (403-walled).

Diff: `docs/playbook.md` + `control/status.md` + this card.
`bootstrap.py check --strict`: green except the designed born-red hold.

## 💡 Session idea

Extend `scripts/gen_roster.py` idle detection to resolve **newest heartbeat
across main + all open PR heads** per lane (it currently pins only the
default-branch HEAD via `ls_remote_head`, line 619 — exactly the main-only
sweep the new DETECTION sub-note forbids). That converts tonight's lesson
from a doc rule into an enforcing check ("enforce, don't exhort"): the roster
substrate itself would have shown pokemon-mod-lab alive. Dedup-checked:
scripts/ has no multi-head heartbeat resolver; docs/ideas/ has no entry.

## ⟲ Previous-session review

The R27-execution worker's verify-then-withdraw discipline was the right
call executed well: it treated the target seat's rebuttal as a Q-0120 lead
rather than noise, re-verified every claim at live GitHub, and withdrew rung
1 with a closed-with-reason PR instead of doubling down — a false positive
that cost minutes, not a night. The improvable half is upstream: the false
positive existed because detection swept main only, and the withdrawal left
residue (the 403-walled stale branch) that had to be owner-queued by hand.
Concrete workflow improvement: the session-idea above — make the multi-head
sweep mechanical in the roster generator so rung 1 can't fire on a
main-only shadow again.
