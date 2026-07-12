# 2026-07-12 — Prompts v3.1: apply QA fixes (boot-sim, incident-replay, question-rounds)

> **Status:** `complete`

📊 Model: fable-5 · finalize worker dispatched by coordinator (Wave 4, owner-directed overnight rebuild) · start 2026-07-12 (born-red at open)

## Declared at open (born-red)

Build prompts v3.1 on `claude/prompts-v3-1`: apply every required fix from the
three QA audits (#100 incident-replay, #101 question-rounds, #102 boot-sim) to
the v3.0 set in `docs/prompts/v3/` (PR #98 @ 8056b7e), regenerate all 8 B files
from the fixed A, recount every char budget (fitted ≤7,500 / hard 8,000), and
park the PR READY+green for coordinator confirmation.

## Shipped (close-out) — PR #103

- **Universal artifacts rebuilt (v3.1):** `universal-startup.md` (A, body
  6,496c — boot reordered 1 sync → 2 baton → 3 arm → 4 cutover → 5 claim+slice,
  retiring circularity C-11; scoped trigger deletion T1; pacemaker ender
  exception C-5; PRECEDENCE ladder T3; WAKE-DEAD path; spawn-liveness I-69;
  canonical FAILSAFE WAKE text fixed for C-10/C-12 and stamped D-2/D-3);
  `custom-instructions-core.md` (core 6,996c — INJECTION GUARD T6, CONTROL BUS
  core-owned + outbox writer + append-race T5/D-4, LANDING DOCTRINE unifying
  the self-arm contradictions C-1..C-4/T4, TOOL FACTS closing BLOCKERs
  I-63/I-78 + I-64 stub-200, WORK-LOOP/GIT/CLAIMS riders, TOKEN+RE-RUN,
  Q-0120 + Q-0105); `session-ender.md` (D, 3,300c — heartbeat commits on the
  session PR BEFORE the flip, failsafe left armed as the successor's F-1
  bridge resolving C-6, BUSINESS crons never closed R6-Q15, pending-checks +
  parked-landing-path + REPORT-to-PR-body rules).
- **All 8 B files REGENERATED** from post-fix A by the new
  `docs/prompts/v3/tools/regen_b_files.py` (slot fills + FIRST WORK ORDERS
  insert only; sha1 content stamp per file; D-1 drift class retired). All
  boot-sim seat fixes applied (FM/SI/SB/SW/GL/WS/VL/IL sets), cutover ids
  reconciled against the armed registry (C-7/C-8/C-9 with the retro-games
  delete ceded to Game Lab).
- **All 8 C seat blocks rebuilt** ≤ the new core budget; per-repo merge notes
  now SPECIALIZE the core doctrine (recorded-practice carve-outs), never
  contradict it.
- **Budgets recounted** (per-project/README.md v3.1 table): every file ≤ 8,000
  hard (venture-lab B and assembled CI at exactly 8,000); all seat files over
  the 7,500 fitted target, flagged in-header — the QA fix volume does not fit
  under fitted without dropping safety rules.
- **⚑ Flagged structural decisions (owner-vetoable, reversible):** GEN-3 RIDER
  v5 + PERMISSIONS v4 embedded as stamped DIGESTS citing their canonical
  verbatim sources (@76d854d / @e801da5) — full-verbatim + the QA riders cannot
  both fit the console cap; kit-lab 06:00Z daily kept (SI-2, "keep" branch);
  ender keeps the failsafe armed as the successor bridge (F-1 over the v3.0
  close-it text).
- **Not applied (recorded in per-project/README.md § residuals):** boot-sim
  U-5 (READY-only-where-gate, latent for all current seats); question-rounds
  R1-Q9's wrong-Project-paste stop clause (the READ-ONLY writable-set rule
  covers the harm; venture files sit at exactly 8,000); incident-replay MEDIUM
  leftovers I-38/I-44/I-45/I-46/I-58-partial/I-65-tag-push/I-66/I-72-disarm.
- Codex review: pending — usage-limit reply 2026-07-12 03:1xZ; coordinator
  re-pokes 06:00Z.

## Walls hit

None new. Pre-existing: roster-freshness 4h bar (expected-red class) and the
owner-action-fields advisory on control/status.md (known, non-blocking).

💡 Session idea: `tools/regen_b_files.py` already computes every B budget —
a 15-line CI step (or bootstrap checker) that reruns it in `--check` mode and
fails on drift between committed B files and the A+config regeneration would
make the D-1 "never hand-edit" rule enforcing instead of exhortative
("enforce, don't exhort", Q-0132).

⟲ Previous-session review: the three QA sessions (#100/#101/#102) produced
exceptionally actionable fix tables — every row carried a target artifact and
a one-line fix, which is what made a one-session v3.1 build possible. The gap
they shared: none of the three totaled the CHAR COST of its own fixes, so the
fitted/hard budget collision (the dominant constraint of this session — ~7
compression rounds) was discovered at build time. Improvement: QA fix tables
for capped artifacts should carry a chars-added estimate column and a running
sum against the cap, so the drafting session starts with the trade-off
explicit.
