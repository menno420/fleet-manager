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

- **E1 is assembled, revised against his own calls, and waiting on two things
  only he can do: Part 1, and sending.** *(2026-08-25, fm #946. The reservation
  was lifted live on 08-24; the "sends 2026-08-24" this line used to carry was
  his intention that day, not an event — it did not send.)* His send-day sentence
  — *"a revision pass and my own section added/edited"* — **was put to him rather
  than interpreted**: two operations, and the pass covers the whole document. He
  then chose **the literal one-page cap** (findings 1–3 and asks 1–5 only) and
  **cut the contested 97.5 % ratio**. Part 2 is **1,481 words**, from
  `python3 tools/render_eap_mail.py --count` rather than from prose — the figure
  had been wrong in all three places it was written. **A session still does not
  draft Part 1 or send it.**
- **D2 is the actionable program step. `OQ-FM-D2-TARGET` is STILL OPEN** — a
  2026-08-23 session marked it answered by OD-20 and withdrew that the same
  session (`@codex`, fm #937); his words set an estate-wide outcome, not a
  repository choice. **No session is blocked by it:** the
  [active-repo intent audit](findings/2026-08-23-active-repo-intent-audit.md) § 6
  gives a measured order — **`spider-swing` → `product-forge` → `estate-backups`
  → the `websites` date stamp**. **Settled among the RATED, 2026-08-24 (fm
  #940):** the census gap closed when `spider-swing` was judged, but five repos
  still read `unrated` (one read each) and any could displace this.
  `spider-swing` went to the top: its README contradicts its own ledger about the
  Play release, which is the one thread with an external clock. § 7 of the audit
  carries a turnkey fix brief for each; none of the fixes has been done. Separately measured:
  `superbot` has **no root README**, and **9 of 15 satellite READMEs never name
  this hub** ([back-link audit](findings/2026-08-23-front-door-audit.md)), which
  is a real return-path gap but **does not size D2** — presence is not truth.
  This is orientation work, so **OD-13** is satisfied rather than overridden.
- **The next Discord bot's shape is set (OD-19):** a small, review-oriented
  game-server bot **first**, built cog-portable so existing cogs can be added or
  lightly adapted — and **the bots stay separated**. Repository consolidation of
  the two `superbot` repos is the destination, not the next step.
  **UPDATE 2026-08-24: GCB-1 is resolved by creation** — the repo is
  `menno420/spider-bot`, live on Railway in the real Slingy Spider server the
  same day (v0.1.0 + Phase-0 hardening; [`ESTATE.md`](ESTATE.md) row +
  [`repos/spider-bot/`](repos/spider-bot/README.md)). `OQ-GCB-REVIEW-SCOPE`
  (the review-loop letters) stays open, now as spider-bot's next-phase
  direction.
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

- **Owner direction captured — and the session's own D2 conclusion withdrawn on
  review** (2026-08-23, fm #937). He asked for oversight into the active projects
  and gave back four pieces of direction that existed only in the chat — the loss
  mode the boot file records as entry 1b. **OD-19**: the next bot is a small
  **review-oriented game-server bot first**, **cog-portable** (existing cogs added
  on demand or *slightly* altered), and **the bots stay separated** — the two-repo
  consolidation is of repositories, not running bots. **OD-20**: no further repo
  cuts; the lever is legibility.
  **`OQ-FM-D2-TARGET` was marked answered by OD-20 and that was withdrawn the
  same session** — `@codex` returned **40 findings across five rounds — 39 conceded, 1 partial, 0 survived**, the sharpest
  being that an estate-wide outcome is not a repository selection. Also
  withdrawn: a "four most-worked repos" ranking derived from last-commit dates
  and contradicted by a 14-day merged-PR measurement already in this tree, and a
  claim that a README back-link is the *only* channel reachable in a satellite
  (the satellite's own `.claude/` loads).
  **What survives is one measurement:** `superbot` has **no root README**, and
  **9 of 15 satellite READMEs never name this hub**
  ([back-link audit](findings/2026-08-23-front-door-audit.md)) — a real
  return-path gap that does **not** size D2. The
  [active-repo intent audit](findings/2026-08-23-active-repo-intent-audit.md),
  written hours earlier and **not read before that finding was drafted**, remains
  the primary document and supplies D2's measured order. His laptop-as-AI-workstation
  thread is recorded in [`findings/2026-08-23-owner-direction.md`](findings/2026-08-23-owner-direction.md)
  § 4 — his current priority, recorded nowhere until now, and deliberately *not*
  an owner-queue entry since it is not an ask.
  E1 did **not** send on 2026-08-24; it is assembled and revised, and waits on
  his Part 1 and his compose (fm #946).

- **The E1 evidence pack — what the projects created, measured; and the review
  site stops calling a finished program live** (2026-08-23, fm #919 +
  websites #512). Owner directive: the mail goes today, *"but only after we have
  properly looked at everything the projects created."*
  **MEASURED across all 26 repositories: 8,000 pull requests opened all-time ·
  19 of 26 repositories created inside the EAP fortnight — all 19 within its
  first seven days, 17 of them in the first four · 4,535 session cards across 19
  repositories.**
  [The pack](findings/2026-08-23-eap-evidence-pack.md) carries every figure with
  the command that produced it, mapped to the six net-new sections the owner's
  own reflection names. **E1's owner-reservation was LIFTED 2026-08-24 (owner, live)**; the sweep and
  the assembled draft landed
  ([draft](planning/2026-08-24-final-eap-email-draft.md) ·
  [sweep](findings/2026-08-24-e1-source-sweep.md)). **He still sends it himself.**
  **Two corrections it exists because of:** (1) a method correction that was
  **itself corrected on 2026-08-24 and no longer says anything about
  `search/issues`** — the figures were re-measured off the `pulls?state=all`
  Link header, and that method stands, now corroborated by a second endpoint.
  The withdrawn diagnosis and its test:
  [the sweep](findings/2026-08-24-e1-source-sweep.md) § 4 N6.
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
E1 is assembled and revised against his own calls — Part 1 and the send remain
his alone (fm #946); D2 is the available track; its next-repo target awaits
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
