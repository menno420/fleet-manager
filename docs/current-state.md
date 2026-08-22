# fleet-manager — Current State

> **Status:** `living-ledger`
>
> **Cold-orientation contract, refreshed 2026-08-10:** this is the second file
> in the repository's three-file front door. It carries **live hub state**, not
> the program history. Source and merged repository state always win. The
> historical hub closeout remains at
> [`PROJECT-CLOSEOUT.md`](PROJECT-CLOSEOUT.md), but it is no longer a boot
> instruction or a current-state source.
>
> **Trimmed 2026-08-22 under OD-17, 6,212 → 853 words.** The merge log's older
> entries and the seat-era sections this file already carried as *preserved, not
> current* now live in
> [`current-state-shipped-log.md`](current-state-shipped-log.md) — moved, not
> deleted, and word-conserved. What stayed is what the header always promised:
> live hub state.

## Live state

### Purpose

fleet-manager is the estate's **router and records home**. It provides
orientation and continuity, holds the program and owner-only records that
belong at estate level, and points to each repository's own truth. It does not
copy product architecture or internal product state. Canonical intent:
[`intent.md`](intent.md) § 1.

### Operating era

- The autonomous Projects program is closed. Work now happens in regular,
  owner-directed sessions, one finished step at a time.
- The generated roster, `control/` message bus, trigger telemetry, project
  packages, and seat prompt registry are historical records. They do not answer
  what the estate is doing now.
- Per-repo orientation lives under [`repos/`](repos/README.md), while each
  repository remains canonical for its own product truth.
- Claude Code's boot file is `.claude/CLAUDE.md`. ChatGPT Work does not load it
  automatically; the surface-neutral door is
  [`../README.md`](../README.md) → this file → the consolidation program.

### Work state

- **E1 remains owner-reserved.** The final EAP email is written and sent by the
  owner; a session does not draft or send it.
- **D2 is the actionable program step**; its shiftlife target is SUPERSEDED
  (OD-15; re-target pending at `OQ-FM-D2-TARGET`). Until the owner names the
  next repository, the standing answer to "what should a session pick up" is
  **OD-13** — the program's NOW pointer carries the detail.
- fleet-manager vendors substrate-kit v1.21.0 (fm #853)
- A root `AGENTS.md` remains an owner decision (`OQ-FM-AGENTS-BOOT`).

### Live operating mechanisms

- Local verification is one command: `python3 bootstrap.py check --strict`.
  It appends expected telemetry to `.substrate/guard-fires.jsonl`; retain that
  delta.
- The branch claim and landing order live in
  [`.claude/skills/session-close/SKILL.md`](../.claude/skills/session-close/SKILL.md):
  born-red card first, ready PR, exact-head review before the flip, card complete
  last.
- On ChatGPT Work, local git owns the working tree and the GitHub connector owns
  remote mutations. The measured route is recorded in
  [`execution-surfaces.md`](execution-surfaces.md).

## Recently shipped (newest first)

- **Fleet-wide estate review — [`ESTATE.md`](ESTATE.md) built** (2026-08-21,
  fm #878): 26 repos read from source; three Tier-1 entry points, 11
  route pairs, owner-queue corrections;
  [the finding](findings/2026-08-21-fleet-estate-review.md).

- **The Railway keep-bot-only worklist EXECUTED, all slices terminal**
  (2026-08-20/21; fm #868 → this): crawler DoS ended; mineverse + review
  off Railway (Pages export serves; estate 3 projects / 8 services);
  pollers retired; bot DB sized — 97.5 % `btd6_*` ingestion history
  (`OQ-BOT-DB-BTD6-PRUNE`). Evidence:
  [audit § 8 addendum](findings/2026-08-14-railway-websites-audit.md).
  Open: `OQ-RAILWAY-SHIFTLIFE-SCOPE` · `OQ-WEBSITES-PAT` · `OQ-RG-ORPHAN-VOLUMES`.

- **couch-legend — the life story LANDED (#7: adopted tuning · save v2
  `lifeHigh` · 18 chapters, 3 scenes live); Android shell next**
  (2026-08-21): [`repos/couch-legend/README.md`](repos/couch-legend/README.md).

- **phone-controller Slices 18–22 (v0.22.0) shipped** (2026-08-14→20,
  pf #49–#53; 21/22 = the owner's keyboard+foldable ask, design-first):
  §7 rows + [`repos/product-forge/README.md`](repos/product-forge/README.md).

- **Railway estate audited + consolidated — €30 bill attributed, W1 executed,
  churn stopped, orphan DB archived+deleted** (2026-08-14→16, fm #861→#863,
  #867; open: `OQ-WEBSITES-PAT`):
  [audit + execution record](findings/2026-08-14-railway-websites-audit.md).

- **substrate-kit v1.21.0 — cut, published, adopted** (2026-08-13, kit #581
  + fm #853): program §7.

- **§ 4.8's fresh-scorer half ran — blind scorers confirm PARTIAL ×2, the
  produce-and-score bar is met** (2026-08-13, fm #852):
  [the finding](findings/2026-08-13-intent-map-fresh-scorer.md) carries the
  scorer-independent zeros, the four named bends in the prior scoring, and
  the scorer-relative imprecision counts.

- **Roadmap § 4.8's producer half ran — the scorer half followed, fm #852**
  (2026-08-12, fm #851):
  [the test finding](findings/2026-08-12-intent-map-fresh-agent-test.md) — five
  fresh agents, ask-time snapshot trees, rubric committed before any output was
  read, scored by the running session (the recorded bar is produce **and**
  score). **221/222 checked citations substance-correct · 0 invented OPEN · 0
  silent HIGHs · 0 false alarms · verdict PARTIAL** (one citation-overreach,
  one miscount, eleven exact-range imprecise line-cites). The walkthrough's one
  HIGH dissolved under fresh retrieval — the ask-time tree already answered
  it — so the HIGH-ask branch is now demonstrated by no committed case, and
  the dominant defect class (imprecise cites) is mechanically checkable.

**Older entries — the full log, 37 more reaching back to the first roster
generations — moved off the boot path 2026-08-22 (OD-17) and preserved in
[`current-state-shipped-log.md`](current-state-shipped-log.md). Nothing was
deleted.**

## Next action / where to read next

**Current:** the authoritative next action is the consolidation program's NOW
pointer in
[`planning/2026-07-26-consolidation-program.md`](planning/2026-07-26-consolidation-program.md).
E1 remains owner-reserved; D2 is the available track; its next-repo target awaits
the owner (OD-15 superseded shiftlife, 2026-08-10).

Use
[`findings/2026-08-05-foundation-continuation.md`](findings/2026-08-05-foundation-continuation.md)
for the certainty legend and foundation-before-rebuild principle. Its numbered
worklist is a dated finding, not a competing NOW pointer. For the owner's
working principles, read
[`owner-reflection-2026-07-21.md`](owner-reflection-2026-07-21.md).

Do not use `NEXT-TASKS.md`, `fleet-triage.md`, `RESUME.md`, the roster, or
`control/` to pick current work. They describe the seat era and are bannered
accordingly.

## Review rhythm

**Current:** sessions verify against repository state, never against an agent
summary alone ([`playbook.md`](playbook.md) R2). The owner directs work in the
live chat and acts on genuinely owner-only entries in
[`owner-queue.md`](owner-queue.md); the retired `control/inbox.md` is not an
order channel. Follow the exact landing order in
[`../.claude/skills/session-close/SKILL.md`](../.claude/skills/session-close/SKILL.md).
