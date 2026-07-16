# 2026-07-16 — r26-trigger-tooling (routine R26 wake)

> **Status:** `in-progress`

Intent: ship scripts/assemble_triggers_snapshot.py (PR #253's session idea — one-command R26 snapshot assembler), re-run the full list_triggers export to re-check the I8 duplicate-cron pairs from the 00:55–01:03Z failsafe cutover, refresh telemetry/triggers-snapshot.json + the fleet-triage I8 verdict, and rewrite the control/status.md heartbeat.

## What happened

- **(A) Assembler shipped:** `scripts/assemble_triggers_snapshot.py` —
  stdlib-only, matches the `check_trigger_health.py` conventions (provenance
  header, argparse, `--selfcheck` offline assertions per the repo's
  script-test convention). Input: raw `list_triggers` page dumps (argv paths
  in pagination order, or stdin); output: the committed snapshot shape,
  gated through `gen_roster.validate_export` before writing. Fails loudly
  (exit 1) on partial pagination (last page still advertising
  has_more/next_cursor) and on zero records. `--selfcheck`: PASS
  (0 failures). Shakedown on the live 20-page export: clean on the first
  run — no fixes needed.
- **(B) I8 re-check (read-only):** fresh FULL `list_triggers` export
  2026-07-16T01:44–01:49Z, 20 pages saved verbatim to the session
  scratchpad, 1964 records / 17 enabled →
  `telemetry/triggers-snapshot.json` (captured_at 01:49:00Z) via the new
  assembler. **Verdict: the doubles are REAL, no longer a capture-window
  artifact.** FM old `trig_01LgMqjbBHsNTWMe6T3vaWmk` ABSENT (successor
  `trig_01UNjDKaaiGuUTvyfQGLKLrn` sole FM failsafe, next 02:32Z); Websites
  `trig_01VRT9F6jYNXym3nn18vVQQK`, Venture Lab
  `trig_01GeQiMM3nHMQTyuLMsWj7q3`, SuperBot World
  `trig_01RwQK2cBpgvY2xc2LZPSNtQ` all still PRESENT+ENABLED beside their
  successors; plus a fourth pair the prior export predated (SuperBot 2.0
  `trig_01UC7wiV3n5Vgs3RpSQt4gWz` old + `trig_01E86nBnXqesQTwm6WA4mSUD`
  new, 01:07Z). `check_trigger_health.py`: **PASS — 8/9 green, 1 WARN
  (I8 ×4: superbot-2.0 · superbot-world · venture-lab · websites)**,
  exit 0. Verdict + per-id detail recorded in docs/fleet-triage.md
  § 2026-07-16 I8 re-check. No trigger created/modified/fired/deleted.
- **(C) Heartbeat:** control/status.md rewritten wholesale — observed
  failsafe state, PR #253/#254/#255 pointers, newest CAPABILITIES wall +
  owner-queue #68 pointers, next-2 baton (morning owner report · sim-lab
  watch / I8 disposition).
- **Drift fix-on-sight:** deleted the stale claim file
  `control/claims/claude-night-audit-records.md` — its PR (#254) merged at
  `7970520` but the claim was left behind, showing a false collision signal
  to parallel sessions.

## Enders

- 💡 **Session idea:** make I8's remedy **binding-aware** instead of blanket
  keep-oldest. This wake exposed the tension live: `check_trigger_health.py`
  I8 says "keep the OLDEST-created id (the one docs cite)" — but for a
  rebind-then-delete cutover pair the intended keeper is the NEWEST id (the
  successor bound to the live coordinator session); a future session
  following the printed remedy verbatim would delete the live failsafe and
  keep one bound to a dead session. Fix shape: when a duplicate group's
  records carry `persistent_session_id`s, prefer the id whose binding
  matches the most recent creation AND cross-check against the id
  control/status.md cites; print "cutover pair — keeper is the successor"
  instead of keep-oldest when created_at gap > ~12h. Dedup: grepped
  docs/ideas/ + recent cards for I8/keeper/binding — nothing covers it.
- **📊 Model:** Fable 5 (Claude 5 family) · medium · build+verify
  (R26 routine tooling + registry re-check)
- ⟲ **Previous-session review** (fm #254, night-audit-records card): the
  audit's verdict table with per-seat evidence citations is the strongest
  form a night audit has taken so far, and honestly recording the 7/7
  classifier denials instead of routing around them was right. What it
  missed: it never deleted its claim file
  (control/claims/claude-night-audit-records.md) after #254 merged — this
  session found it live during the overlap check and had to verify against
  open PRs to learn it was stale. Concrete workflow improvement: add a
  claims-vs-open-PRs staleness probe (a claim whose branch has no open PR
  and whose scope PR merged = stale, delete on sight) to the wake ladder or
  bootstrap check, so a forgotten claim can't outlive its PR by more than
  one wake.
