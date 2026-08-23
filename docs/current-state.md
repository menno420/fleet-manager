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
> **Trimmed 2026-08-22 under OD-17: 6,212 words of old content down to 853, and
> the file itself now ~1207** (the kit's word instrument, which is what the
> orientation budget gates; `wc -w` reads lower). The gap between the two is new
> prose — this notice, the archive pointers, and the backfilled entries — so
> *853* is retained old content, not the final size. The merge log's older
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

- **The E1 evidence pack — what the projects created, measured; and the review
  site stops calling a finished program live** (2026-08-23, fm #919 +
  websites #512). Owner directive: the mail goes today, *"but only after we have
  properly looked at everything the projects created."*
  **MEASURED across all 26 repositories: 8,000 pull requests opened all-time ·
  19 of 26 repositories created inside the EAP fortnight — all 19 within its
  first seven days, 17 of them in the first four · 4,551 session cards across 19
  repositories.**
  [The pack](findings/2026-08-23-eap-evidence-pack.md) carries every figure with
  the command that produced it, mapped to the six net-new sections the owner's
  own reflection names. **E1 itself remains owner-reserved — no session drafts
  or sends it.**
  **Two corrections it exists because of:** (1) the obvious method is wrong —
  a first sweep via `search/issues` returned **2,783** PRs and was false
  (`superbot` read 0 against a newest PR of #2450); the search index does not
  cover most of this account, the same defect R5 measured for `search/code`.
  Re-measured via the `pulls?state=all` Link header with positive controls that
  reproduce. **Unchecked, the mail would have carried a figure 5,217 too low.**
  (2) **0 of 7 live pages on the public review site said the program had ended**,
  and `/fleet/` rendered *"15 live lanes"* with mirrored heartbeats 33 days after
  the seats were terminated — on the surface the mail points at, addressed to the
  vendor who ended the program. Fixed in websites #512 (era framing only; no
  number, chart or citation changed).
  **TRAP-006 registered** — the born-red card is the merge hold, and fm #915
  defeated it by flipping before push: opened 08:24:29Z, auto-merged 08:25:06Z,
  **0 reviews**. Routes added; the register is now **6 traps / 61 routes** — two routes, not one, because Codex caught that a single route matching both the card write and the push is consumed by the write, leaving the push (the trap's actual moment) silent. Reproduced 1-then-0 against the old design, 1-then-1 against the split.

- **R5 EXECUTED — the estate's first archives: nine repositories, 26 → 9
  archived, 0 deleted** (2026-08-23, fm #912). The step OD-3 described on
  2026-07-26 had never run on anything; it has now run on `superbot-games`,
  `superbot-idle`, `superbot-mineverse`, `trading-strategy`, the three
  `codetool-lab-*` repos, `Substrate-kit-app` and `proxybench`. Pre-archive
  writes landed and were verified live **first** (README notice + description on
  all nine, `proxybench` #1 closed, the labs marked FINISHED and UNMAINTAINED);
  the archives were confirmed by fresh live re-read, not by the API's 200. The
  **three gated rows were not touched** and are still open R5 work when GCB-1 /
  R2 lift. **Three capability firsts recorded:** the archive `PATCH` works
  agent-side; a `git+https://…` install still works against an archived repo
  (`cfgdiff 0.1.1`, real exit 0); a write to one returns 403 *"Repository was
  archived so is read-only."* **And one finding bigger than the step:**
  `search/code` covers only **7 of 26** repositories in this account — all 26 probed, measured
  before any archiving, so archiving is not the cause — which invalidates the
  *method* behind the recorded `Substrate-kit-app` dependency sweep and bars it
  from supporting the deletion call the table defers.
  **Still open, deliberately not stalled on:** whether archiving stops scheduled
  Actions — baseline (`superbot-idle`, last run `2026-08-23T05:42:49Z`) and a
  one-call check are recorded in the disposition table § 4.

- **Every repository has a disposition — keep 14 · archive 12 · delete 0**
  (2026-08-22, fm #906):
  [the table](planning/2026-08-22-repo-dispositions.md). All 26 re-derived from
  each repo's own state; 13 of 14 keeps are reworks, `superbot` neither
  (frozen, fresh successor). ~~**Not executed — the archive list is the
  owner's**~~ — **answered 2026-08-22 and EXECUTED 2026-08-23 for the nine
  ungated rows** (see the R5 entry above); `superbot-next`/`superbot-plugin-hello`
  remain gated on GCB-1 and `product-forge` on R2.

- **The first pre-archive write executed** (2026-08-22, fm #907 + mineverse
  #145 `fc7c349`): the SuperBot-World MASTER told the next session to delete a
  trigger — forbidden, and the trigger no longer existed. Corrected in place;
  siblings searched, zero other instances. Also withdrawn here: the dependabot
  merge recommendation, whose deploy filter was never read.

- **R3 ✅ releases-before-archive — all three code-tool labs archivable**
  (2026-08-22): cfgdiff v0.1.1, envdrift v0.1.0/v0.2.0 tagged + released;
  program §7.

- **The verification half of the repo pass — a dead quality gate fixed on
  `websites`, eight of nine kept repos green** (2026-08-22, websites #511
  `d2bba01`): program §7. The fix's dispatch path is **not yet verified** —
  it only runs when main HEAD carries zero `quality` runs.

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
deleted.** The list above was also **backfilled** the same day: four 2026-08-22
rows already in the program's §7 ledger had never reached this file, two of them
recorded as omitted *because the boot set was at 7000/7000*. Creating headroom
and leaving them out would have preserved the exact gap the trim was for.
The program's §7 ledger remains the fuller record; this section is the recent
window.

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
