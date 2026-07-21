# 2026-07-21 · fm final-closer — FINAL CLOSER prompt lands in the v3 registry (program end today)

> **Status:** `complete`

About to happen (declared born-red): records worker slice for the coordinator
seat. Land the fleet's FINAL CLOSER paste prompt at
`docs/prompts/v3/final-closer.md` (v1.0, owner pastes it to each project
today — the autonomous-session program ends at 2026-07-22T00:00Z and every
session becomes permanently read-only), link it from the v3 registry index
(`docs/prompts/v3/README.md`), and stamp a one-line note in
`control/status.md`. Docs-only; no trigger-MCP calls; no code.

- **📊 Model:** fable-5 · high · docs-only — registry prompt + index link + heartbeat note

## What shipped (PR #425)

- `docs/prompts/v3/final-closer.md` — v1.0 FINAL CLOSER (program end),
  `> **Status:** \`reference\`` badge matching the sibling paste artifacts
  (session-ender.md / universal-continue.md). Six steps under a strict
  priority order (closeout doc → records true-up → routine wipe →
  in-flight work): land-or-park every PR, `docs/PROJECT-CLOSEOUT.md`
  handover for owner + fresh future session, records true-up (with the
  public-repo confidentiality rule), routine wipe to ZERO with no
  failsafe carve-out (list_triggers verified to exhaustion), SEAT CLOSED
  heartbeat + verified-merged closeout PR, final chat recital.
- `docs/prompts/v3/README.md` — indexed as item 6 in "How to found a
  seat" (failsafe stagger table renumbered to 7), matching the
  session-ender/universal-continue link convention.
- `control/status.md` — heartbeat stamp bumped to 2026-07-21T16:54Z with
  the note: final-closer landed; program ends 2026-07-22T00:00Z; fleet
  close underway.

Gate adjustments: none needed — the tasked file content already carried the
`reference` badge the docs gate expects for prompt artifacts.

## Enders

- **💡 Session idea:** close-out day — no new idea beyond the closer
  itself; the honest slot-filler rule (Q-0089 bar: no manufactured
  filler) applies. The closer prompt is this session's genuine forward
  contribution.
- **⟲ Previous-session review (PR #424, 16Z cycle records slice):** solid
  consolidation — it landed the 16:00:18Z snapshot plus kit-wave 5/7
  status and disposed of #419 cleanly, keeping the heartbeat's
  wholesale-overwrite grammar intact so this session's stamp bump was a
  two-line edit. Miss/improvement: its baton did not anticipate the
  program-end deadline now governing the fleet (announced after its write
  time, so an honest miss, not a fault); the workflow improvement it
  points at is exactly what this PR ships — a registry-level close
  artifact so end-of-run doctrine lives in one canonical paste file
  rather than per-seat improvisation.
- **Doc audit:** everything durable is in its home — the prompt file, the
  index link, the heartbeat note, this card. No chat-only facts. Claim
  `control/claims/claude-fm-final-closer.md` deleted in this flip commit.
- **Guard-fires:** `.substrate/guard-fires.jsonl` delta committed with
  this flip (19 records appended by the strict run; do-not-revert).
