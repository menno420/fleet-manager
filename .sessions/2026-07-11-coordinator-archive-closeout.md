# 2026-07-11 — coordinator archive close-out (chat archive prep)

> **Status:** `complete`

📊 Model: Claude Fable 5 (claude-fable-5) · archive close-out slice · night (~01:0xZ)

## Declared at open (born-red)

Owner directive (2026-07-11 ~00:5xZ): the coordinator chat is about to be
ARCHIVED — prepare the repo so a successor session boots cold from committed
state alone. ONE PR:

1. `docs/succession/coordinator-handoff-2026-07-11.md` — the successor's
   one-read state doc: LIVE seats + trigger ids (incl. this session's failsafe
   `trig_014odnv5h1tkJAFRhix3tGLq`, bound to the soon-archived chat), the
   PENDING-OWNER list, the ORDER 015 reconcile note, THE PERMISSIONS FOLD
   REBUILD RECIPE (the built fold dies with this container — recipe is the
   only survivor), known-walls pointers.
2. `projects/fleet-manager/reboot-prompt.md` (v1) — paste-ready successor
   boot prompt: read order → TRIGGER CUTOVER FIRST (F-1 rebind-then-delete)
   → continuous loop → pending-owner pointer.
3. This card with full enders.
4. Heartbeat LAST: phase → CLOSING for archive; routine line explicit that
   the failsafe stays bound to the archived session until successor cutover.

Landing: born-red card → content → heartbeat + flip `complete` last →
substrate-gate poll → REST squash on green (R21). No live triggers touched —
the successor performs the cutover (F-1).

## Done (this PR — #55)

- **`docs/succession/coordinator-handoff-2026-07-11.md`** — the one-read
  successor state doc: §1 live seats + wake table (fm failsafe id
  `trig_014odnv5h1tkJAFRhix3tGLq` marked BOUND-TO-ARCHIVED-CHAT; leftover chain
  one-shots = harmless, ignore); §2 the session arc (#26 → #55, all in git);
  §3 PENDING OWNER (venture-lab boot · plugin-hello push · attended
  permissions re-land · games §5 veto window · paste wave held on the fold);
  §4 the PERMISSIONS FOLD REBUILD RECIPE (verbatim block from `c23223f` →
  13 instructions.md citing it → 6 retry passages re-based to deny-wins →
  v1→v2 bumps → <7,500-char bodies → expect the guard, owner-attended,
  deny-wins); §5 ORDER 015 reconcile note (seats SELF-BOOTED — remaining
  scope = registry centralization, not authoring); §6 walls (sim-lab tag-push
  403; git-proxy stale-clone-pack → always verify FETCH_HEAD == ls-remote);
  §7 the successor's work ladder.
- **`projects/fleet-manager/reboot-prompt.md` (v1 · 2026-07-11)** — paste-ready
  successor boot: read order → TRIGGER CUTOVER FIRST (create new failsafe with
  the failsafe-prompt.md text → verify via list_triggers → THEN delete
  `trig_014odnv5h1tkJAFRhix3tGLq` → arm the ~15-min chain) → continuous loop →
  pending-owner pointer. Paste block measured **1,846 chars** (<2,000).
- **PR #47 state verified live at close** (~01:00Z): open at its born-red card
  only (`a4b736b`) — the fold content never reached it; disposition recorded
  in handoff §3.3 (re-land vehicle in an attended session, or close with
  reason). Left open deliberately: it is the owner's §3 item, not an
  abandonable session PR of this seat.
- **Heartbeat LAST** — phase → CLOSING for archive; routine line explicit that
  the failsafe stays bound to the archived session until successor cutover;
  orders footer 015 open-reconciled; ⚑ = the pending-owner five.

## Enders

💡 **Session idea — commit-or-die rule (guard-held artifacts):** any artifact a
guard refuses to land must be reduced, THE SAME SESSION, to a committed rebuild
recipe (exact source SHA + target list + transform steps + expected re-denial
path) — because worktrees and scratchpads die with the container, a held
artifact that only exists there is already lost; the recipe is the only form
that survives. This session lived it: the twice-held permissions fold survives
only as handoff §4. Candidate playbook rule at next doctrine contact
(decide-and-flag; kit-side candidate too — every fleet repo has guards).

⟲ **Previous-session review (the coordinator session as a whole, #26 → #54):**
honest strength — verify-against-git discipline held under speed: the roster
generations, the review-queue verdicts, and the owner-signal probes were all
built from repo/API ground truth with walls recorded honestly (the "reactions
not agent-visible" line directly prevented misreading owner silence a slice
later). Honest miss — workers repeatedly parked on background pollers
(sleep-loop monitors awaiting CI) and cost the coordinator manual nudges,
sometimes a whole slice's latency; the fix is now standard practice and rides
this card as the recipe: dispatch prompts must say ACTIVE-POLL — bounded
foreground checks (poll → act → return), never an open-ended background wait.

**Docs-audit line:** chat-only facts now captured durably — the permissions
fold rebuild recipe (was: only in the dead worktree + chat), the cutover ids +
bound-to-archived-chat state of `trig_014odnv5h1tkJAFRhix3tGLq` (was: chat +
trigger registry only), the ORDER 015 self-boot reconcile reading, and the
pending-owner five (handoff §3, owner-queue pointers intact). `bootstrap.py
check --strict`: green except this card's expected born-red hold at open (flip
= this commit) and the pre-existing advisory owner-action warning.
