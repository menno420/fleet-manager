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

- **E1 is DRAFTED IN FULL AND STAGED (2026-09-03, fm #1017) — both parts, in
  a Gmail draft in his own mailbox with no recipients; what is left is his:
  read, rewrite Part 1 (beat 3 above all), answer the one-word calls in the
  draft's § 2, add the recipients, send.** Shape A of 2026-09-02: Part 2 at the
  1,686 words he chose plus two one-clause patches and the 453-word
  Projects-versus-sessions addendum carrying the three false-done rows;
  block 2,323 words by `--count`. *(The paragraph below is the 2026-08-25
  state, kept.)*
  **E1 was assembled, revised against his own calls, and waiting on two things
  only he can do: Part 1, and sending.** *(2026-08-25, fm #946. The reservation
  was lifted live on 08-24; the "sends 2026-08-24" this line used to carry was
  his intention that day, not an event — it did not send.)* His send-day sentence
  — *"a revision pass and my own section added/edited"* — **was put to him rather
  than interpreted**: two operations, and the pass covers the whole document. He
  then chose **the literal one-page cap** (findings 1–3 and asks 1–5 only) and
  **cut the contested 97.5 % ratio**. Part 2 is **2,323 words** (1,686 after his cap; the
  2026-09-02 addendum and two patches added the rest, fm #1017), from
  `python3 tools/render_eap_mail.py --count` rather than from prose — the figure
  had been wrong in all three places it was written. **A session still does not
  draft Part 1 or send it.** **The evidence base for Part 2's widening landed
  2026-09-02 (fm #1010):**
  [`findings/2026-09-02-eap-mail-evidence-report.md`](findings/2026-09-02-eap-mail-evidence-report.md)
  — two overnight fan-outs (12 verified Fleet A findings, a 3-row false-done
  ledger, three judged spines), evidence only, no mail text; its § 5 (what the
  critics found wrong) and § 10 (the handoff) are the load-bearing sections
  for whichever session next works the mail with him. It went through
  seventeen Codex rounds; the three-round cap that followed is
  [`traps.md`](traps.md) TRAP-009 (its decision is stamped there).
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
- **Cross-session visibility now has a surface: [`activity/`](activity/README.md)**
  (2026-08-26, fm #947). Owner ask: *"how well does a cloud session understand
  what the local sessions have been doing?"* `MEASURED` answer: barely — in the
  seven calendar days to 2026-08-26 the estate wrote **74 cards across six
  non-archived repositories** and a fleet-manager cloud session could reach
  **54**, all its own — the other **20** were unreachable from here; **0 of
  418** dated cards here recorded which machine ran them; and
  `creator-kit` had existed for a day without reaching `ESTATE.md`. Two lanes
  now: a **derived** index regenerated by `python3 tools/estate_activity.py
  refresh` (every repo's cards, plus an **invisible-work** section naming
  repositories that moved and left no card), and a **hand-written** lane for
  work that touches no repository at all — the laptop, ChatGPT, Drive — which
  is the half nothing can derive. Cards gained an optional `📍 Venue:`
  token; **coverage started at 0 of 74** and absence prints as `unstated`,
  never a guess. The derived lane also reads **open PR branches**, so a
  born-red card in flight is visible before it merges — which is the half that
  makes it a coordination surface and not just a history. On demand, not
  scheduled.
- **The legibility plan has its execution decomposition (2026-08-26 evening):**
  [the estate execution packets](planning/2026-08-26-estate-execution-packets.md)
  — per-repo work packets for the two boot venues (OD-22: fleet-manager in the
  cloud, the OneDrive/local-disk hub locally; satellites never boot). First
  sitting: PKT-C1 (spider-swing's front-door fix); must-not-slip: A1/A2 (gate
  the next-agent contribution). The owner accepted it provisionally — *"not
  read every word yet"* — **and as of 2026-08-28 every packet is held until
  his explicit GO** (OD-23: *"no execution yet, because I still have more to
  plan"*; the substrate-kit sitting happened later the same date — **OD-24**
  — and did **not** lift the hold).
- fleet-manager vendors substrate-kit v1.21.0 (fm #853)
- **Fleet Manager now owns the durable owner-comment contract** (2026-08-27):
  [`owner-comments/`](owner-comments/README.md) carries public, exact-wording
  JSON records; every ESTATE row has a stable routed README; one generated root
  index gives the control plane cheap counts. `tools/owner_comments.py check`
  and its regression suite are in the required preflight. Consumption moves a
  record into preserved history and updates both indexes in the same diff,
  never deleting it. The authenticated website UI/writeback is a separate
  `websites` change; no local queue or pending PR counts as durable.
- **`AGENTS.md` is decided: yes, estate-wide** (owner, 2026-08-28 —
  `OQ-FM-AGENTS-BOOT` answered). Rollout is PKT-B4's ×N rows, sequenced and
  held until his GO on plan execution; whether the kit should plant/maintain
  the files instead of hand-writes is parked for the substrate-kit **review
  round** (OD-24 — the sitting itself happened 2026-08-28 and left it parked).
- **The local/cloud sync direction is recorded (2026-08-27→28, OD-23):** the
  goal is **venue handoff** — a device-bound task started locally must be
  continuable by a fresh cloud session. Hub-local sessions will keep
  fleet-manager's local-surface pages (lean, the main happenings included,
  public-safe) once he gives GO; local sessions follow the full card
  discipline with work routed by scope (repo → its own card · estate-level →
  here · machine/personal → the hub). `OQ-ONEDRIVE-HUB` is rescoped to
  optional hub housekeeping. Execution is explicitly held; the substrate-kit
  conversation happened the same night (**OD-24**). Record:
  [`findings/2026-08-28-owner-direction.md`](findings/2026-08-28-owner-direction.md).
- **The agent-autonomy and session-hygiene direction is recorded (2026-08-28,
  OD-24):** every session leaves the surfaces it actually touched **better
  than it found them** (hygiene detector/skill/hook prototypes on the laptop
  hub first, per the promotion rule); **initiative is a duty** — improve what
  you notice, small fixes inline, large finds recorded; **walls exist by
  owner ratification only** (authorship irrelevant; unratified walls must not
  accumulate); skills/hooks chain across the session boundary and stay
  kit-portable per model; and the **substrate-kit review round is directed**
  with a four-step method. Nothing GOs the held packets. Record:
  [`findings/2026-08-28-owner-direction-agent-autonomy.md`](findings/2026-08-28-owner-direction-agent-autonomy.md).
  **The round's session 1 ran overnight the same date (fm #956)** — §6 steps
  1–2 executed: the genesis dig's three-era history, twelve classified gaps
  (dominant: unenforced/unrouted), the rival-hypothesis verdict, and the
  dispositions table (recommendations only, zero deletions):
  [`findings/2026-08-28-substrate-kit-genesis-dig.md`](findings/2026-08-28-substrate-kit-genesis-dig.md).
  **Session 2 ran the same day (fm #959 + kit #587 MERGED):** §11 items 1–2
  built in the kit's venue — the kit tree now routes to its fm worklist
  (`kit:docs/NEXT-TASKS.md` superseded, gap #5 closed) and the
  false-negative family (worklist rows 13/17/18) is fixed on kit `main`,
  each reproduced against the published asset first, through a pre-push
  adversarial round plus three Codex rounds (5+6 conceded-and-fixed; R3's
  4 deferred as worklist row 35 under the review cap; fixes unreleased —
  the cut stays owner-paced) — and §11 item 4's audit ran:
  [the router band re-read](findings/2026-08-28-router-band-reread.md)
  (208 body sections, seven dig claims narrowed and routed in place, a
  carrier census of standing owner rules — five absent from every fm
  document — with its two new owner asks queued). His morning letters were checked
  first and remain unanswered; everything owner-gated stayed gated.
  **Session 3 ran the same day (fm #960 + kit #588):**
  [the kit-tree truth pass](findings/2026-08-28-kit-tree-truth-pass.md) —
  all 187 doc-surface files judged at kit `a9acc41` with adversarial
  verification, **both owed checks answered** (PL-002 preserves Q-0241's
  rebuild-only scope at the canonical block; Q-0214's delete-with-tombstones
  retention substantially shipped as the v1.0.0 economy engine, unconfigured
  and trace-free on the kit's own corpus at HEAD), kit `docs/current-state.md`
  + `control/status.md` reconciled in the kit's venue (kit #588 MERGED on
  green), the 23-file wrong-action set catalogued as §5 recommendations, and
  `OQ-KIT-P10-REQUIRED-CHECKS` retired by a live rules read. ~~The letters
  were re-checked and remain unanswered.~~
- **The round's DISCUSSION SITTING ran with the owner present (2026-08-28,
  session 4, fm #964) — every letter that was ASKED is answered, and one answer
  re-ranks the round (OD-26).** *(Still open, so "answered" is not read as
  "finished": the kit's name, the v1.21.0 adopter half, agenda § 2 · G's
  card-deletion question — deliberately not asked, due after the report-only
  census — and the BTD6 loop.)* Twelve answers recorded as each arrived:
  [`findings/2026-08-28-od24-sitting-answers.md`](findings/2026-08-28-od24-sitting-answers.md).
  **The headline:** asked which ways the kit still fails — the question no
  session had put to him — he gave **one root cause**, not a list: *"they are
  all related to the same root cause, which is mostly that agents don't take
  enough initiative to leave the repos in a better shape"*. Three audits had
  produced twelve gap classes; the divergence is one of **altitude**, and the
  round had already found it (dig § 6.1) and organised around the gap table
  anyway. **Two things he said on no agenda govern what happens next:** the
  **cost function** — *stalling is "not necessarily bad"; **redoing** the same
  things is the waste*, so the test for any mechanism is *does it stop a
  re-derivation?* and **routing outranks building** — and a **three-stage
  order**, *map (3 parallel sessions running now) → revised plan → execution*,
  which makes this round's output **an input to a plan, not a work queue** and
  the Move 1 hold a **stage with an exit condition** rather than something to
  re-ask. **Answers:** June rules mostly still stand · nothing may **block** a
  session calling work done (build the consumption loop, no gate) · a brake may
  prompt **only when he is present** (`delete_trigger` never) · **Move 1 HELD** ·
  the end-of-session interview is asked **by something, filtered**, and that is
  **not** a GO for Move 1 · **AGENTS.md hand-written per repo** · the journal
  **survives as the guidebook it already is** — his named function (*"easily find
  out what went wrong each session"*) is already captured by the session cards,
  so the gap is **retrieval** across them, not a second record · leftovers drain via **a standing surface
  he reads**, scheduled unattended draining **refused** · spend caps **not
  currently relevant** · the kit's **charter is rewritten to say initiative** ·
  the kit **is renamed** but he supplies the name later · the next release is
  **cut when the next fix batch lands** · **D2's target is `spider-swing`**
  (`OQ-FM-D2-TARGET` **CLOSED** — open since 08-23, once falsely closed by
  inference) · the final EAP mail moved from *"leave it"* to **"soon"** with a
  **widened brief**. **`OQ-KIT-PROMPT-DOCTRINE` and `OQ-EAP-SPEND-WINDOW-MOOT`
  also closed; `OQ-KIT-RENAME` added.** The Gemini paid-key budget decision's
  self-contradiction is reconciled in [`decisions.md`](decisions.md) — the
  agenda's stated prerequisite to the spend question.
  **Session 5 is named from his own words** — he drew the boundary himself
  (*"Records work can go now"*): a kit-venue **records** session (charter
  rewrite + the truth pass's 23-file sweep), then the release. Everything
  owner-gated stayed gated.
- **The cold-boot context cost is measured, and the owner has ruled it worth
  paying (OD-25, 2026-08-28).** He ran this session (fm #962) as a deliberate
  experiment — *"to find out exactly how much context a cold boot would
  consume"* — and the answer matched his prior: **157.3k**, from 69.7k at
  session init through 127.6k after the six mandatory reads *plus the first live
  surfaces* (+57.9k) to 157.3k after further live-state investigation (+29.7k).
  **`OWNER` · `NOT-VERIFIABLE`, not `MEASURED`** — these are owner-console
  readings and the legend reserves `MEASURED` for a reproducible command; a
  session cannot instrument its own window from inside, so this record
  reproduces his readings rather than verifying them. The 127.6k checkpoint is
  **combined**, so the +57.9k is not the six reads' isolated cost and must not
  be quoted as it — that reading was never taken. **Composition at 157.3k:**
  messages 99.9k · system tools 18k · MCP 14.6k · system prompt 11k · memory
  9.6k · **skills 5.9k**, rows that sum to 159.0k against the stated 157.3k —
  a 1.7k gap the record names rather than smooths, so proportions hold and
  per-row subtraction does not. Skills are a small single-digit percentage
  either way, so skill size is not the thing to optimize. **His ruling bounds OD-17:** offered the figure as an
  optimization target he declined it — the boot cost buys *"an agent that knows
  what's going on without the need for me to explain everything again"*, and
  *"the memory my agents have … is the most valuable thing we have now"*. Token
  count is not a defect; duplicated or mechanically derivable context is. Also
  recorded for the first time: his **context operating policy** (sessions run
  300–500k for small/medium work and 500–800k after a large task; automatic
  compaction at ~750k *"uses a lot of usage"*, so he hands off deliberately at
  ~500k via the continuation prompt) — the estate ships `continuation-prompt`
  and has never carried its **trigger condition**, which is the same *unrouted*
  class the OD-24 round is cataloguing. `500k` is **not** fixed as doctrine.
  Record: [`findings/2026-08-28-context-budget-and-orientation-cost.md`](findings/2026-08-28-context-budget-and-orientation-cost.md).
- **The skill/rule reuse map is measured, and the container — not the material —
  is the problem (2026-08-28).** Owner ask: *"find out exactly what we already
  have that is good skill material and … what previous sessions struggled
  with."* A 79-agent fan-out read 1,002 of the estate's 3,836 session cards.
  **The spine is the delivery-mechanism ranking**, one corpus: gate-enforced
  **95–97 %** of 3,836 cards, and a template-carried ritual is completely
  countable (**598/969**) because its text is written by construction. **There is no
  COMPLETE skill-invocation telemetry** — 46 recorded invocations exist and are
  observable, but no exhaustive count does — so an earlier quantified ranking
  of the three is **withdrawn** (`@codex` R4/R5). **Idea consumption was published wrong twice and is now
  bounded** — a "10 : 1 ratio" (denominator never established) and then "four
  repos at zero, one is `idea-engine`" (a directory-name mismatch: it holds
  **566** idea files in `ideas/` — the same figure OD-4 has carried
  independently — and `sim-lab` **268** verdict directories in `sims/`, making
  them the estate's **best** converters, not its worst). Corrected reading:
  **wide variance, not uniform failure** — purpose-built conveyors convert near
  1 : 1 while `fleet-manager`, the hub, sits at **0.04** (433 cards, 18 idea
  files).
  OD-21's diagnosis is supported by the citation evidence in the record, **not** by
  a conveyor count. **Why skills are the wrong container:** on one corpus,
  gate-enforced **95–97 %** of 3,836 cards and template-carried **598/969**,
  both completely countable; **skill use is unobservable in this estate**, so
  the earlier three-way ranking is withdrawn and the surviving argument is that
  a mechanism leaving no record cannot be shown to work even when it does. **And the kit cannot deliver a skill anyway** — it
  stages and never installs (`SKILLS-index.md.tmpl:30-40`, *"nothing live"*);
  **4 of 19** repos have a populated `.claude/skills/`. **0 of 27 fm skills
  reference the guard layer and 0 of 71 routes point at the four rule
  surfaces.** **Reframed against OD-26**: this is **stage-one mapping input**, one of the
  three parallel ultracode mapping sessions he named (§ 13: *mapping → revised
  plan → execution*), so its four moves are **candidate inputs, not a
  sequence** — the pre-sequencing it first carried was withdrawn. Re-scored
  against his two criteria (§ 20 *does it stop re-derivation?* · § 4 *does it
  make a session leave the repo better?*), **the ranking inverts**: routing the
  rulebook was cheapest and is weakest on re-derivation; *consume the cards* is the only
  move scoring directly on both — **and it is the estate's own Move 1 in another
  shape, which OD-26 § 7 holds** (*"no adjacent mechanism may be built that is
  Move 1 in another shape; the hold is on the function"*). The record scored it
  highest and recommended it hardest while it was already held; it is now marked
  DO-NOT-BUILD and retained as evidence *for* the held function. The moves are
  lettered A–D to stop colliding with the estate's Move 1. Nothing is executed. Record:
  [`findings/2026-08-28-skill-and-rule-reuse-map.md`](findings/2026-08-28-skill-and-rule-reuse-map.md).

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

- **The estate activity log — a cloud session can now see what ran on the
  laptop** (2026-08-26, fm #947). `docs/activity/` + `tools/estate_activity.py`,
  wired into the boot table, `MAP.md`, `README.md`, the card protocol, the
  session-close skill and two doc-routes. Measurement:
  [`findings/2026-08-26-cross-session-visibility.md`](findings/2026-08-26-cross-session-visibility.md).
  **Three gaps, three fixes:** no aggregation (the cards existed and were
  unreachable from the router whose job is routing) · no venue on any card ·
  and work outside every repository leaving nothing at all, which is what his
  question was actually about. **`@codex` returned 46 findings over five rounds —
  35 `[conceded]`, 1 `[partial]`, 10 `[survived]`** (the survivors all
  re-emissions of fixes already in the tree). Three were P1, two were arithmetic
  in this very entry (the reachable split was 43/31 and is 54/20; the card
  baseline counted the directory README), and the sharpest pair **contradicted
  each other on one predicate** — an open born-red PR must not report itself as
  unexplained movement, and must not excuse every other push either. Rounds 3
  and 4 then found the same three bugs twice in a second near-parallel code
  path, so that path was **removed rather than patched**. **`creator-kit` registered the same
  PR** —
  created 2026-08-25, absent from an index whose header promised *"every
  repository the account holds"*; the baseline was 27 and the account held 28.
  **Four non-archived repositories still have no card protocol**, so no session
  in them can ever appear in the derived lane — `curious-research`, `estate-backups`,
  `spider-bot`, `superbot-plugin-hello`; `spider-bot` is the notable one, live
  in production with **20 commits** in two days and no `.sessions/` at all
  (corrected 2026-08-26 after merge; the figure first published here was *8*,
  which was the requested page size, not a count).

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
  his Part 1 and his compose (fm #946) — and since 2026-09-03 it is drafted in
  full and staged as his Gmail draft (fm #1017).

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
E1 is drafted in full and staged as his Gmail draft (fm #1017) — the rewrite
of Part 1 and the send remain his alone; D2 is the available track; its next-repo target awaits
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
