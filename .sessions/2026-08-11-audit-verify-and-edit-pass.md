# 2026-08-11 · hub — verify the full-read audit's verdicts, then work its defect list

> **Status:** `in-progress`

- **📊 Model:** fable-5 · high · review/verify — re-run the headline-seven status
  table, then fix the verified live-surface defects at their sites and record
  each closure in findings.md with the command that proves it

Time: 2026-08-11 · venue: scheduled continuation session · branch
`claude/fleet-manager-verify-defects-cb6gxk` (restarted from `ba34aef` =
`origin/main` after fm #845 merged)

## Previous-session review

⟲ fm #839/#840/#842/#845 produced and corrected the full-read audit: 833/833
files read with coverage proved, 345 findings adversarially refuted to
101 defect / 205 harmless, the headline seven re-measured to 1 closed / 6 open.
Nothing was fixed — that session read, reported and recorded, and said so. This
session is the edit pass it left behind.

## What is about to happen

1. **Verify, not trust:** run all seven re-check commands from findings.md's
   status table; any command that fails to reproduce its verdict is a new
   finding for the same file.
2. **Fix the six open headline defects at their sites** (CAPABILITIES walls
   rows · init-prompt badge+deploy sentence · E1 link + queue entry ·
   SKILLS-local re-apply table · false-wall checker docstring · link-checker
   scan set), plus the live-surface defect band around them (boot file D1–D3,
   owner-queue D6–D8, decisions D9, SKILLS files D12–D15, hooks/skills
   D16–D22, tools D23–D29 where doc-safe).
3. **Record each closure in findings.md with the proving command**; leave
   everything not taken honestly OPEN.
4. Land on green: ready PR, `@codex review` and wait, flip last.
