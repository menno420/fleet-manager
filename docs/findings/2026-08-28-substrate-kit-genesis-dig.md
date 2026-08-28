# The substrate-kit genesis dig — three eras of one practice, measured

> **Status:** `audit` · 2026-08-28 (overnight) · OD-24 review round, **session 1**
>
> **What this executes:** OD-24 §6 **steps 1–2 only** — harvest drift incidents
> from the committed record, classify every gap. **Nothing is fixed here** (step
> 3+ belongs to later sessions of the round), no packet GOs (OD-23's hold
> stands), and §10's dispositions are **recommendations awaiting the owner's
> word** — nothing was archived or deleted tonight.
>
> **Method.** Whole-population mechanical sweeps over superbot's 969 dated
> session cards and fleet-manager's 428; live GitHub API history for every date
> anchor; 14 parallel reader lanes over the genesis/peak/extraction/post-close
> record (~2.2M subagent tokens, 368 tool calls); adversarial verification of
> the load-bearing claims. superbot was read **raw-fetch only** (an API tarball
> of `main` — the frozen repo was never cloned, never written). Citations to
> superbot/substrate-kit files are against that 2026-08-28 snapshot, written
> `superbot:<path>` / `kit:<path>`. Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
> Coverage, including what was sampled rather than read, is stated in §9 —
> and §9 opens with a self-correction this method caught in its own first pass.

## 0 · The answer in one paragraph

The practice the owner remembers was born in superbot between 2026-05-29 and
2026-06-12, out of his own doc-truth audit and his personal question-batches to
each session; it became self-sustaining on a **dated, committed event**
(2026-06-09, the reflection interview made standing), peaked during the EAP as
the enforced half of a two-part system, and was **extracted into the kit only in
its enforceable form** — the kit was founded on the *measured failure* of the
notebook half ("the door, not the notebook") and its own benchmark predicted,
nine days before the program closed, exactly the regression the owner later
observed. Post-close, **the ritual's gated form did not decay — the loop
behind it did**:
card discipline held at ~100% presence everywhere it was gated, while the
conveyor from cards into ideas-ledgers, journals, promoted rules and kit
releases stopped, because the things that drove it — seat-prompt enders, owner
check-ins, a standing executor — ended with the program and nothing mechanized
replaced them. "Too many files" is real, measured, and **write-side** (budget
freezes, index decay, maintenance attention); it is not what killed the loop.

## 1 · The three-era timeline (anchor dates `MEASURED` via API 2026-08-28 unless noted)

**Era 0 — pre-history.** superbot first commit 2025-08-10; ~9 months dormant;
revived 2026-05-13 (PR #10, first `claude/` merge). May 2026: 1,206 commits,
~500 PRs — velocity **without** the practice.

**Era 1a — the interview era (owner-fed), 2026-05-29 → 06-09.**

- **The ~PR-400 anchor is the audit program.** PR #393 (2026-05-29): the
  owner-requested full audit — *"Every source file under `disbot/` (510), every
  migration (51), every doc (43), and the test tree … read in full by a fan-out
  of 22 scoped auditors."* Five P1 PRs opened within 17 minutes that night;
  **PR #400** (merged 2026-05-30T06:34Z) is **P1-12: "stale docs that actively
  mislead future agents"** — the exact concern the journal machinery mechanized
  a week later. His "~PR 400" memory anchors the *concern* correctly; the
  journal file itself is a ~PR-520 event (PRs #513–#533 merged on its creation
  day).
- **2026-06-05T21:27Z** — `.session-journal.md` created (`08dbf6d9`), landing
  as **one bullet in an agent's bug-fix PR (#528)**: *"cross-session working
  memory … maintainer preferences, recurring fixes, my own mistakes-to-avoid,
  and candidate rules that graduate into CLAUDE.md at a periodic review."* The
  file was agent-initiated tooling; the **practice** was owner-driven.
- **How he actually fed it:** chat-side question batches, transcribed by agents.
  10 of the 12 birth-window cards (2026-06-06/07, all 12 read) record in-session
  owner Q-batches — a 16-question batch in 4 waves (PR #561), a **60-question
  batch** (Q-0013, 06-08), a 36-question vision capture. **Zero owner-typed
  comments exist on any PR in the window** — established twice: an all-time
  `commenter:menno420` search (92 hits enumerated, footer-filtered), then an
  adversarial whole-population re-sweep (`MEASURED` 2026-08-28): every
  in-window issue comment repo-wide (2, both Claude-posted with footers),
  **0 inline review comments, 0 review bodies, 0 commit comments** — the
  earliest owner review anywhere is PR #1035, 06-18. "Owner-typed" is
  load-bearing (his account did post two machine-generated comments). The
  interviews lived in chat and
  survive only as agent transcriptions and router entries. He also repeatedly
  interviewed the *apparatus*: *"maintainer asked for an honest opinion of this
  journal, then — based on it — to improve it and make future sessions keep it
  that way"* (06-06).
- **2026-06-07** — one day: the maintainer-question-router (`893c5794`, 12:19Z)
  — his answers preserved **verbatim**, ~96 rulings in its first four days —
  and the `.sessions/` card convention (`94293b89`, 13:42Z). The journal's
  Session Log moved to cards **by design** the same day (kills the
  merge-conflict class); the journal became guidebook-only.
- **2026-06-09 — the self-sustainment event, dated twice.** Commit `c23601af`
  (23:03Z): *"docs: make the end-of-session reflection interview a standing
  protocol"* — and the journal's own words: *"The maintainer used to ask these
  manually in chat nearly every session; standing since 2026-06-09."* His
  memory ("I personally interviewed each session; later it kept itself going")
  is **CONFIRMED as mechanism, with the handover date**. Note who authored the
  convention: Q-0061 was an **agent recommendation the owner ratified** — the
  same authorship pattern OD-24 §3 names for walls.

**Era 1b — self-sustaining, 2026-06-09 → 07-07.** The ⟲-review ramp,
whole-population by ISO week: 0/12 (W23, predates Q-0102) → 45% → 82% → 97% →
**98%** (W27). 701 cards in June alone; every ⟲ section in a 56-card sample was
substantive (predecessors corrected with evidence; *"No new idea forced"* when
honest); 💡→shipped-code closures on record (the `hub_children` idea, the
bug-book guard). The enforcement stack arrived in one dense window: Q-0089
one-idea (06-10) · Q-0102 ⟲ review (06-12) · Q-0103/0104 enders (06-12) ·
Q-0123 auto-merge (06-13) · **Q-0133 born-red gate (06-14)** · Q-0194
friction→guard (06-22, owner: *"catching these should not depend on the owner
spotting them"*). Smoothness was **engineered, and repaired same-day** — the
owner had already watched one practice silently die and be revived (Q-0052,
06-09: *"that's how it used to be previously, but somewhere along the way that
stopped"*): the interview cadence **was** the repair loop.

**Era 2 — EAP + extraction, 2026-07-07 → 07-21.** Kit repo created
2026-07-07T21:39:56Z; subtree extracted 07-08 (kit PR #1); v1.0.0 on 07-09; **26
releases to v1.20.2 in 13 days** (weekly commits 284 → 237 → 98). Practice
scaled to ~19 repos. superbot's journal last updated **2026-07-15**; the router's
last entry (Q-0275) is **the same day** — the two owner-facing memory mechanisms
died together, two days before the freeze (07-17), four before the close
(07-21). July card discipline **rose** (⟲ presence 92% vs June's 77%).

**Era 3 — stepped-back, 07-22 → now.** One kit release in six weeks (v1.21.0,
08-13); **zero kit pushes since 2026-08-14** (`pushed_at`, live API) while the
kit's fm-side worklist grew to 34 rows; fm's card ritual held ~100% while its
ideas conveyor stopped at 08-11; the owner's first recorded "kit is not doing
its job" statement is 2026-08-26 (OD-21). Details in §5.

## 2 · The control condition — what the owner-fed loop actually was

The record shows a **two-part system**, and only one part was ever mechanized:

| part | what it was | carried by |
|---|---|---|
| **the ritual** | born-red card · enders (💡, ⟲, doc-audit) · flip-last | CI gate (Q-0133) + checker (`check_session_log`) + seat-prompt enders |
| **the loop** | interview → card Context-delta → REVIEW pass every ~3-5 sessions mines the deltas → owner-ratified promotion into CLAUDE.md/hooks → next session boots into the promoted rule; ideas groomed down a lifecycle (*"every idea ends implemented or discussed"*, superbot:Q-0015) | **the owner's questions, his check-ins, and prose obligations** — no machine ever verified any of it *(narrowed 2026-08-28, [re-read](2026-08-28-router-band-reread.md) §1.2: the loop's CADENCE was machine-fired — superbot:Q-0107's auto-firing reconciliation trigger; the substance was prose)* |

Of the 22 core rulings this dig read in full, **~5 were machine-enforced; all
four ancestors of the kit's next-agent contract (Q-0089 idea · Q-0102 review ·
Q-0104's judgment half · Q-0254 restate-back) were prose**, backed at most by
advisory reminders — and the one CI touchpoint (Q-0133) checks the Status token,
never the enders' content (`superbot:docs/owner/maintainer-question-router.md:5112-5117`).
Mechanism-building peaked mid-June; **no July ruling (Q-0241→Q-0273, all eight
read) introduces a single new checker** — July scaled obligations as prose while
the born-red gate was stamped `RETIRING 2026-07-17` in CLAUDE.md.

The genesis-era purpose, in his words (the reference point §6 judges against):
Q-0015 (06-08): *"it's not intended to be 100% autonomous … that is a deliberate
step so this project stays managable and reviewable. The goal … is to make each
step more productive … so an agent knows where to start and where to stop and
what its role is in the process."* And the system-level charter
(`superbot:docs/collaboration-model.md`): *"The bot is the substrate; the real
artifact is this workflow itself — the docs, the journal, the hooks, the
tooling, and the decision router that let any agent pick up the project and
work correctly with little human steering"* · *"what a session writes down is
literally what the next agent will remember"* · session-close writes are *"the
highest-leverage act of the session."* The doc-volume trade was **defended at
genesis**: *"This is why there are 'a lot of' docs. The reading cost is a
deliberate investment."*

## 3 · When practice was at its best — shown, not asserted

Criterion (stated, since "best" is a judgement): running unattended **and**
catching failures **and** feeding lessons forward, with the least owner input.
Candidates, all `MEASURED` in the record:

- **2026-07-08** — the Waves 1–3 campaign: 7/7 claim-first, 7/7 born-red, 7/7
  enders complete, and a **full unprompted friction→guard chain in git**
  (#1846 card-flag → #1854 idea → #1855 enforcing CI gate) with no owner
  involvement (`superbot:docs/eap/campaign-self-audit-2026-07-08.md:101-125`).
- **2026-07-09** — the wind-down audit: 21/21 incidents verified against live
  GitHub by 32 adversarial agents, **zero fabrication**; five real inaccuracies
  found, one in the auditor's own lane
  (`superbot:docs/eap/fleet-winddown-audit-2026-07-09.md:18-37`).
- **The night of 07-09→10** — the self-auditing loop closed end-to-end
  unattended: a guard shipped mid-band dogfooded by the next session; a checker
  shipped 03:43 caught real staleness by morning; 116 PRs, zero stuck; the
  review's own line: *"Drift is being found by machinery, not by the owner"*
  (`superbot:docs/eap/fleet-overnight-review-2026-07-10.md:16-113`).
- **The verdict: 2026-07-12→13** — the first fully-doctrined unsupervised night
  at scale, **absorbing a live platform failure**: the scheduler degraded
  ~01:07–02:08Z and the Q-0265/R26/R27 failsafe doctrine bridged it with zero
  seat deaths (contrast 07-12: 9 dropped ticks, 2 dark seats); ~190+ PRs across
  12 repos; ~22 of ~25 tally claims exact-verified, the 3 mismatches caught by
  the substrate's own review; honest nulls as headlines (*"nothing tonight is a
  finding, and that null is the deliverable"*)
  (`superbot:docs/eap/night-review-2026-07-13.md:16-45`).

Same-corpus loop closure: mineverse found the kit's born-red fail-open, routed
it upstream, the kit fixed it in v1.15.0, mineverse re-consumed it — **bug →
finding → kit fix → re-consumed in ~30h** ([`../eap-story.md`](../eap-story.md)
§8; the upstream half independently confirmed in
`superbot:docs/eap/night-review-2026-07-13.md:232-233`).

**Two caveats the record itself carries.** (1) The peak's evidence is a
**closed Claude loop** — *"author = gatekeeper = merger … the only reviewer any
claim ever meets is its claimant"*; the sole true outsider was Codex
(`superbot:docs/eap/eap-program-review-2026-07-10.md:139-140`). (2) **The decline
mechanism was already operating during the peak**: the EAP's own evaluation
journal went silent 07-10 — at the program's biggest night — diagnosed
contemporaneously as *"Same class: exhorted, not enforced"*; 8 of 10 instruction
packages sat undeployed; post-merge review had *"degraded to no review"*
(`superbot:docs/eap/eap-program-review-2026-07-10.md:101-135`). The peak and the
decline coexisted in the same week, split exactly along the enforced/unenforced
line.

## 4 · Lost in extraction — what the kit shipped vs what superbot lived

The founding plan (`superbot:docs/planning/kit-lab-founding-plan-2026-07-07.md`,
821 lines, read whole) contains **no journal-preservation objective**. The kit
was founded from the notebook's measured failure — cold-start A/B **FAIL twice**
(*"ON read 3.1–3.3× more and wrote nothing back. Refuted claim: readable
orientation docs are a cost without mechanized write-back"*) — with the thesis
stated in its own words: **"the kit's thesis is now *the door, not the
notebook*."** What each lived practice became (`MEASURED` against
`kit:src/engine/`, all 37 checkers enumerated):

| superbot lived practice | what the kit ships | enforcement |
|---|---|---|
| born-red card + flip-last | status-token gate + PL-011 ENGAGED gate | **CI, merge-blocking** — the practice that did not decay |
| card grammar + enders present | marker needles (`💡` char; `"previous-session review"` substring) | merge-blocking **presence only** — and the auto-draft plants the satisfying headings itself |
| ⟲ review **substance** | `CARD_HINT_REVIEW` — one hint string; `check_card_residue` (the one substance instrument, 07-16) | **advisory-only, self-declared UNVERIFIED, never graduated** — its docstring documents the sham-card hole verbatim |
| 💡 idea **lifecycle** (dedup · groom · "ends implemented or discussed") | template prose + `check_ungroomed_ideas` | **warn-only, "NEVER exit-affecting"**; the B4 frontmatter validator never shipped to adopters |
| `.session-journal.md` guidebook (living, corrected-in-place) | planted 5-section skeleton | **zero** — 0 of 37 checkers reference it; the one checker that touches the path exists to **exempt** it (`check_template_sync` `LIVE_TRAFFIC_DESTS`); absent from every boot list |
| question-router (his verbatim rulings; the DISCUSS/ask channel) | planted `question-router.md` template ("Maintainer answer (verbatim)" blocks); PL register (law) | PL grammar checked **on the kit repo only**; no engine checker validates an adopter's router; **the ask-side shipped as a template fm never used post-close** *(corrected in verification — an earlier draft said "no kit descendant")* |
| the reflection interview + REVIEW/mining pass + owner-ratified promotion | the MINING half shipped: `engine/loop/reflections.py` (v1.0.0) mines 💡/⚑ card lines into a 5-entry buffer, injects them at boot, Stop-hook nags when unmined | mining is **advisory, one-liners, session-confirmed** — the **interview and owner-ratified-promotion halves are absent**; the kit's `interview/` module fills template slots, not retrospectives *(corrected in verification — an earlier draft said "absent entirely")* |
| friction→guard | PL-007 + `rationalize` skill + friction-issue transport | law + tooling; nothing checks a guard was created |
| understand-and-reflect (Q-0254) | `intake` skill + CONSTITUTION bullet (ported same day, 07-07 — the one ruling with a dated extraction event) | prose/skill, unenforced |
| honest negatives | PL-012 + four wall-guard checkers | enforced **in the inverse direction only** (stops writing walls; nothing stops suppressing a negative) |

Two structural choices sealed it: the daily culture was **explicitly demoted**
— *"The kit's own opinionated defaults (markers, badge taxonomy, born-red
doctrine) are house style, not program law"* (`kit:docs/program/README.md:19-21`;
founding decision D-7) — while program law preserved the **autonomy mechanics**
(never-wait, decide-and-flag, ENGAGED, enforce-don't-exhort). And **the word
"initiative" appears in none of the kit's purpose statements** — grep over
`kit:README.md` + `PROJECT-CLOSEOUT.md` + `rulings.md` returns zero — although
OD-24 §2 gives it as the reason the kit exists.

**The kit knew.** Its bench delivered the verdict on 2026-07-12, nine days
before close: **1 PASS / 8 FAIL at 9 scored rows; the one demonstrated benefit
is steering/continuity; the enforcement *pull* is a measured null** — *"the
kit's completion ritual exerted no pull"*, the ON arm *"explicitly declined"*
write-back (`kit:bench/results/cold-start/2026-07-12-run10/report.md:20-74`,
re-verified from `index.json` tonight). The grounded-skills self-measurement
(07-19) returned a second negative: fleet skill-grounding **fell 12%→10%**,
*"improvisation proxy ≈ 90% fleet-wide"*. Its own journal was *"still all
placeholder stubs after a 17-PR run"* (07-09). And the verdict was
**structurally droppable**: `PROJECT-CLOSEOUT.md` — the designated durable
record — carries no mention of 1-PASS/8-FAIL or the enforcement-pull null; a
session booting from the closeout never meets the kit's own science. superbot
itself never adopted the kit (*"the origin repo is the only active repo not on
the substrate it exports"*), and the kit's heartbeat self-reports
`engaged: no` (`kit:control/status.md`).

## 5 · The regressions since — each with its citation

**First, what did NOT regress** (the correction that reframes OD-21): the card
ritual's form held everywhere it was gated. fm July 266/267 cards carry the
review section, August **161/161 at this PR's final tree** (160/161 when
measured mid-dig — the one miss was this session's own then-unfinished card,
completed before landing); a mechanical empty-section detector over all 161
August cards found **zero** empty review sections; the 96%→60% "⟲ decline" in the first sweep was **glyph
notation, not practice**. superbot's four post-freeze cards keep full
discipline, and the single most rigorous predecessor-correction in the whole
sample is post-freeze (the 56th reconcile pass refuting the 55th against a
saved prompt at a named line, 2026-08-10). "Form held" is more than
non-emptiness: an adversarial residue probe over all 161 August cards found
**0 surviving drafted-hint texts** (the sham-card fingerprint the kit's own
`check_card_residue` hunts), so the sections were authored, not
draft-residue (`MEASURED`, verification pass). Two honest narrowings from
the same pass: sessions still **carry the 💡 marker** (161/161 at the final
tree; 160/161 at measurement, the miss being this card)
but a fresh disjoint 27-card sample found ~11% of the slots holding no idea
at all (dispatch text, mission restatement — the marker-needle hole §4
describes, present in fm too); and August's review register visibly shifts
in a minority toward verification/linkage entries ("Nothing to repair" in
11/161, 10 of them from 08-13 on) — still checkable, never generic praise,
but "substantive" is doing lighter work in August than in June.

The regressions, dated:

1. **The ideas conveyor stopped at the close — and its tail died 08-11.**
   15 of 18 fm `docs/ideas/` files date from the EAP fortnight, *"when a seat
   was ordered to file them"*; **3 post-close** against 163 post-close cards
   (OD-21, `MEASURED`, verified tonight: no idea file after
   `consume-the-open-pr-signal-2026-08-11.md`, and no grooming act in any card
   after 08-10 — a whole-population keyword grep over all 161 August cards,
   spot-checked in verification, not a full read). The demand side is namable: **every per-project
   custom-instructions file in the v3 registry (9 of 9, re-measured tonight)
   carries the ender line "Enders: ONE genuine idea; prev-session review;
   heartbeat; flip."** — the close deleted that line from existence.
   The nag that remained was **de-channeled by policy**: `ungroomed_ideas`
   routed off the agent path 2026-08-06 (foundation §5: *"Not merely un-gated —
   unseen"*). superbot's post-freeze cards diagnose the same class from the
   other side: *"the self-improvement backlog has no executor"* · *"~40
   reconcile-* tooling fragments, all blocked on the same no-executor gate"*
   (`superbot:.sessions/2026-08-03-reconcile.md`, `2026-08-10-reconcile.md`).
2. **The journal never lived anywhere the kit planted it — a pre-close gap,
   not post-close decay.** `.session-journal.md` byte-identical to the template
   in **11 of 14** adopters (OD-21); fm's copy has **one commit in its entire
   history — the adoption plant** (fm #2, 2026-07-09, v1.4.0; API-measured
   tonight after a shallow-clone artifact was caught); already *"an empty
   template"* on superbot-next **during** the EAP (2026-07-12 problem census
   U3); program step **D3 ("fill the empty journal guidebooks", Track D
   priority 1) appears in 0 of the 50 §7 ledger rows** — never run. The three
   written adopter journals (`spider-swing` · `substrate-kit` · `websites`,
   the census's 3-of-14) — plus superbot's origin journal (802 lines/689
   content, outside the adopter denominator) — are where a session chose to
   write, not where a mechanism asked.
3. **The kit itself stalled mid-worklist.** Release cadence was already broken
   by 08-06 (ADVISORY_CENSUS sat unreleased on `main` *"sixteen days after the
   last release"* — fm #833); one post-close release (v1.21.0, 08-13) closed 7
   defects and the wave that shipped it grew the worklist **5 → 22 → 34 rows**
   (fm #853/#855/#879), none consumed since; **zero kit pushes since
   2026-08-14**; `kit:docs/NEXT-TASKS.md` frozen at 07-17 telling the next
   session to distribute **v1.18.0**; the kit tree routes to its fm-side
   worklist **nowhere** (`MEASURED` 2026-08-21) — its successor worklist's home
   exists only inside one session card's deferral note. Meanwhile the kit was
   still being **adopted** (couch-legend, 08-21, owner-directed) — 34 known
   defects and all.
4. **Nothing rescinded kit work; it was displaced.** OD-13 (methods first)
   stands unamended; from 08-14 onward **five §7 rows carry the same formula
   verbatim** (re-counted tonight: ledger lines 289, 298, 299, 300, 304) —
   *"OD-13 tension named, not silently resolved: his live directive picked
   product work for this session"*. The kit stopped by displacement, with the
   tension honestly logged each time.
5. **The ask-channel died with no successor.** Router and journal both last
   written 2026-07-15. Post-close fm has the OD table and `owner-queue.md`
   (asks **to** him) — but nothing shaped like the standing end-of-session
   interview or the DISCUSS queue (questions **from** him at the moment of
   action) existed until the owner-comments contract (08-27), which is
   write-side only until Move 3.
6. **Drift incidents in the stepped-back window** (the OD-24 §6 step-1
   harvest, fm side; each verified in its card): the **flip-before-review
   family** *(narrowed 2026-08-28,
   [re-read](2026-08-28-router-band-reread.md) §1.3: superbot:Q-0180's ratified June
   design ACCEPTED the merge-vs-review race given a consumption loop —
   superbot:Q-0174 — so the owner-precedented defect is the missing consumption
   loop, not merge timing itself)* — fm #828 (merged 22 s after review request, 08-08), then ×5 on
   2026-08-23 alone (#915 auto-merged 37 s after open, 0 reviews; #920, #922,
   #925, #937) **with the rule already written and TRAP-006 registered the
   same morning** — *"The register entry is correct; my execution of it is what
   keeps failing"*; inference laundered as owner decision (`OQ-FM-D2-TARGET`
   "answered", withdrawn same session, 08-23); owner words evaporating —
   *"caught in the act for the third time this month"* (08-26); a shipped
   mechanism that was factually wrong (`Reviewed commit:` line that does not
   exist, fm #938→#941); the orientation-headroom advisory firing unread for
   weeks (*"one of 124 advisories held off the gate channel … indistinguishable
   from silence"*, 08-22); a route extension that was *"a null change dressed
   as a mechanism"* because both matching routes were already consumed (08-23).
7. **Apparatus died waiting for a fleet that no longer existed.** The roster
   regen deadlocked 08-06 with recovery designed for *"the next manager wake"*
   (retired 08-07, owner: *"Yes retire the roster, I don't need it"*);
   curious-research **de-adopted** the kit (−41,399 lines, 08-07);
   `registry/kit-versions.md` sat 27 days stale declaring v1.15.0 current;
   spider-bot ran 20 production commits in two days with **no card protocol at
   all** (08-26); the frozen superbot's automation restarted the production bot
   **344 times in one billing cycle** until sb #2446/#2450 retired the
   schedules (08-14/08-20).
8. **The write-side budget bit the records.** fm's boot-read set saturated at
   **7000/7000 words**; two sessions **skipped recording shipped rows** because
   any row would red the gate (fm #892, 08-22); 70% of the mandatory read was
   merge log until OD-17 trimmed it. The kit's own gate ran at **87–90%
   advisory noise** until 08-06/08-13 (*"1:9 signal to noise, and the noise was
   wrong"*).

## 6 · Intent deltas — judged against his recorded words

1. **The kit's purpose statements preserved the autonomy half of his purpose
   and never named the initiative half.** He built
   it *"so agents become more autonomous and think more for themselves and take
   more initiative"* (OD-24 §2); the kit describes itself as an
   **agent-memory substrate** whose *"claims … are enforced by checks"*
   (`kit:README.md`, `PROJECT-CLOSEOUT.md`). The autonomy half is genuinely
   there — *"work correctly with little steering"*, the PL autonomy rails —
   but the word *initiative* appears nowhere in its purpose statements (a
   word-presence test, stated as such), and the initiative-shaped practices
   (ideas lifecycle, journal contribution, CONSTITUTION's generative rung —
   itself unenforced prose) are exactly the ones shipped as "house style."
   **Judged: the central drift, present from founding, and the review round's
   real charter** — OD-21's *"does not properly do it's job"* is the kit doing
   precisely the job its founding plan scoped, which was narrower than the job
   he built it for.
2. **His own intent moved, and the kit tracked the July version.** Genesis:
   *not* 100% autonomous, *"managable and reviewable"* (Q-0015, 06-08) —
   *(narrowed 2026-08-28, [re-read](2026-08-28-router-band-reread.md) §1.1:
   superbot:Q-0083 declared full self-driving the END-STATE two days later, inside the
   genesis era)*. July:
   *"let fable decide"* (superbot:Q-0240), *"never wait … silence = consent"* (superbot:Q-0241) —
   his directives, canonicalized as PL-002 *(narrowed, re-read §1.5: superbot:Q-0241's
   own scope clause bound never-wait to the REBUILD program, ask-first brakes
   left standing for production)*. Post-close he re-centered on
   verification (the 07-21 reflection: *"the wall is verification, not
   capability"*) and now on initiative-with-hygiene (OD-24). **Judged: not a
   bad drift in itself — it is his prerogative and each step is recorded — but
   the kit canonicalized the *autonomy* half of July, and on the verification
   side grew its own register (PL-014, 08-01 · PL-015, 08-06 — post-close
   verification law) **without ever wiring a mechanized external check**: the
   closed-loop caveat — author = gatekeeper = merger — survived the whole
   program, and Codex on PRs is the one external check added, post-close, by
   his instruction *(narrowed in verification — an earlier draft said "never
   grew the verification half"; narrowed again 2026-08-28,
   [re-read](2026-08-28-router-band-reread.md) §1.6: superbot:Q-0258 made Codex the
   standing review-lane drainer MID-program, 07-10, and superbot:Q-0117 had directed an
   independent reviewer already on 06-12 — the closed loop survived despite
   an owner directive, and he himself retired that gate as unused friction,
   superbot:Q-0197)*.
3. **What did not drift:** born-red, verify-first, honest negatives,
   friction→guard-as-law — all deepened post-close (traps register, injection
   hooks, adversarial-review vocabulary, the 08-08 error-ledger mechanisms).
   The genesis line *"every session is expected to leave [the system] a little
   better than it found it"* (`superbot:docs/collaboration-model.md:33-37`) is
   OD-24 §1's hygiene mandate, twenty days early — his current direction is a
   **return**, not a departure.
4. **One authorship symmetry worth naming:** the reflection interview, the
   walls he keeps, and the review convention were all **agent-proposed,
   owner-ratified** (Q-0061; his own correction in OD-24 §3). The genesis loop
   already ran on the doctrine he stated on 08-28: ratification legitimizes,
   authorship is irrelevant.

## 7 · The gap classification (OD-24 §6 step 2)

Classes: **absent** (no instruction/mechanism exists) · **unrouted**
(instruction exists, never arrives at the moment of action) · **unenforced**
(arrives or is known, nothing holds it) · **missing-procedure** (no defined way
to do the thing at all). Fix families per OD-24: write / route / hook·gate /
build-procedure — always through roadmap §6 (observe → prototype → measure →
promote), never idea → mandatory infrastructure.

| # | gap (evidence in §§4–5) | class | fix family (recommendation only) |
|---|---|---|---|
| 1 | ideas conveyor: cards → ledger graduation has no demand since the seat enders died; nag deliberately unseen since 08-06 | **unenforced** (write-side exists; nothing asks at close) | **hook·gate**: the legibility plan's **Move 1** (`♻ Carried forward` marker, mechanical value-vs-diff check) — already designed, kit-venue, awaiting GO; a rollout wave, not just a release |
| 2 | journal contribution: planted file, zero checkers, absent from boot lists, exempted from drift-check | **unenforced + unrouted** (the file is never even pointed at) | fold into Move 1's `journal` value; separately decide whether the journal *should* survive as a per-repo surface or be superseded by traps.md-style routed records — a round question for the owner |
| 3 | reflection interview / REVIEW-mining / promotion loop | **split** *(reclassified in verification)*: the mining half shipped (`engine/loop/reflections.py`) and is **unrouted/unenforced** (advisory, nothing routes sessions to it); the interview and owner-ratified-promotion halves are **missing-procedure** | **route** the shipped miner first, then **build-procedure** for the interview/promotion halves as a hub prototype (§6 promotion); the seven questions still exist verbatim in `superbot:.sessions/README.md` |
| 4 | ask-channel (owner rulings at the moment of action; the router's DISCUSS lane) | **unrouted/unused** *(reclassified in verification — the kit plants a shaped `question-router.md` template fm has held, unused, all post-close)* | **route** first (point the close at the planted router); **build-procedure** for the live loop: OD-21's website comment lane (Move 3) is its designed successor; owner-comments (08-27) covers the write side today |
| 5 | kit worklist unreachable from the kit tree | **unrouted** | one pointer file in the kit tree — smallest fix in this table |
| 6 | no executor/re-raiser for parked worklists (kit rows, superbot idea fragments, D3) | **absent** (structural: nothing wakes for a backlog) | **route vs build-procedure is the owner's fork**: route (a standing re-raise surface he sees — owner-brief already exists) or build-procedure (scheduled kit sessions) — his call, not a session's |
| 7 | flip-before-review keeps recurring with the rule written | **unenforced + unrouted** (routes consumed before the moment; nothing blocks the flip) | hook/gate family: make the flip commit itself the checked moment (TRAP-006/007 register already specifies the predicate) — prototype, measure |
| 8 | owner-words capture (3 losses in one month, self-predicted recurrence) | **absent** (mechanism unbuilt, named in the 08-26 card) | build-procedure: a close-time "owner said → recorded where?" check; prototype on hub |
| 9 | reflective-substance verification (sham-card hole) | **unenforced by design** (`check_card_residue` advisory, UNVERIFIED) | graduate per its own docstring *only after* reliability measurement (PL-008) |
| 10 | write-side budget vs record-keeping (7000/7000 freeze) | **missing-procedure** (no overflow path existed until OD-17 invented one) | OD-17's tier split is the fix pattern; Move 2's digest is the standing answer |
| 11 | orientation/retrieval pain (find-cost across 19 repos; advisory burial) | **unrouted** at estate scale | **route** (compression is routing): **Move 2 (the per-repo digest)** — already planned; this dig adds no second fix |
| 12 | kit defects found only by adoption-diff reviews (author-only-reader) | **missing-procedure** (no non-author read exists inside the kit's own loop) | the v1.21.0 card names it: verification by an instrument someone else wrote; Codex-on-kit-PRs is already the de facto procedure — record it as the kit's norm |

**Distribution:** the harvested incidents skew overwhelmingly
**unenforced/unrouted** — the estate's own injection thesis (116 statements, 0
catches, twice measured) at kit scale — and verification pushed it further in
that direction: two rows first classed *absent* turned out to be shipped
apparatus nothing routes to (the reflection miner, the planted router).
Genuinely **absent** are the interview and owner-ratified-promotion halves,
the executor, and owner-words capture — which is why "write another
instruction" is the one fix family this table never recommends.

## 8 · The rival-hypothesis verdict

**Lead (owner): "too many files to read and maintain."** Verdict: **real,
measured, and not the driver of the decline.** What the record supports:

- **For (write/maintain side, `MEASURED`):** the 7000/7000 boot-budget freeze
  suppressed record-keeping for two sessions; every hand-kept index decayed
  (findings index 25/42; planning 12/15; the router grew to **668,746 bytes
  against a 1,500-byte never-used archive**, its reconciliation cadence widened
  20→30 as volume grew); fleet-manager out-merged
  spider-swing by an order of magnitude in every measured 14-day window —
  against intent.md §5's own non-goal (the intent audit retains the
  **ordering only**: its published pairs — 99·2, the second-hand 86·2, the
  08-24 re-measure — could not be reconciled across windows, so no single
  pair is quoted here as measured). The owner's recall
  framing (*"too much information for an agent to remember"*) is real on this
  axis.
- **Against (as decline cause):** the decline's **timing and selectivity**
  don't track file count — file volume grew before AND after the close, while
  the gated practices held ~100% and only the ungated loop died at the
  boundary; read-side orientation **succeeded when walked** (10/10 fresh-agent
  cold-start routing tests, 08-21; *"It works; I oriented in one pass"*,
  08-07); the record's own causal vocabulary for every practice failure is
  *"exhorted, not enforced"*, *"handed to a session that had already ended"*,
  *"plants docs once"* — never volume; and the EAP-era answer to maintain-cost
  was **generation + checkers, never fewer files** (the 33.5h-stale hand
  manifest → generated roster) *(narrowed 2026-08-28,
  [re-read](2026-08-28-router-band-reread.md) §1.4: superbot:Q-0214 shows the owner
  picked delete-with-tombstones — a bounded corpus by construction — as the
  kit's retention posture on 07-02; whether the kit shipped it is a round
  question)*. The legibility plan's §3 split (compliance is
  not the problem; **finding** is) is confirmed and extended: the pain is also
  write-side budget, and the full-read audit's diagnosed mechanism is
  **append-without-retract inside internally-coherent documents** — a
  retraction/routing defect, not a count defect.

**Rivals (a) close-removed-structure + (c) "never-arrived" — the injection
thesis, in the estate's vocabulary: SUPPORTED, as one mechanism.** The owner
was live on **at least 24 of the 38 post-close days** (`MEASURED`: enumerated
from the OD table, decisions.md, CAPABILITIES.md owner-live venue entries,
owner-queue.md and the §7 rows; independently re-derived in verification with
six spot-checks — a wider docs sweep raises the floor to **28/38**, and one
weak day, 07-30, a real-world playtest event, is excluded) — "stepped back"
was a mode change (product directives and corrections continued; purpose
supply stopped, deliberately: *"I wanted to find out how well the agents would
currently work with the subtrate kit"*). What actually vanished at 07-21 was
the **mechanized demand structure**: the seat enders (9 of 9 per-project
custom-instruction files, re-measured tonight),
the wake routines, the interview cadence. Ideas decline dates exactly to that
boundary; the practice held wherever a gate replaced the prompts. This is the
injection thesis at estate scale, and the kit's own bench had already measured
it: steering survives shipping; **pull does not ship in prose**.

**Rival (b) upgrades-overwrote-amendments: narrow contributor, not the cause.**
One recorded destruction class — the **hand-run** skill-install `cp` loop (5 of
7 amendments silently reverted, full-read audit finding 5; the kit's own
`upgrade` writes only consumer-untouched docs) — plus the generator's re-apply
tax on gate carve-outs (recurred fm #833 → idea-engine #899; fixed upstream in
v1.21.0). No recorded case touches journals or ideas; the 11/14 byte-identical
journals are *"never written, or written and reverted; the hash cannot tell
them apart"* — and no upgrade-revert case is on record.

**A fifth rival, surfaced by verification and weighed here: the decline was
partly the PLANNED phase.** Q-0266 (owner, 2026-07-10, body read in full
tonight): *"we can then consolidate later into only a few dedicated projects
that slowly maintain what we created"* — populate → consolidate → maintain,
with the idea-burst this finding uses as its baseline being the *ordered*
output of the populate phase. This **confounds the timing pillar** of the
(a)+(c) verdict: lower August volume is partly the planned phase 2. What it
does not explain is the **selectivity** (gated practices held ~100% while
ungated ones died — a phase change lowers volume, not compliance shape) or
the maintenance decay (phase 3 is *"slowly maintain"*, and the §5 record is
of maintenance NOT happening: D3 unrun, worklists unconsumed, indexes dead).
The fusion verdict stands on selectivity; its timing pillar is shared with
this rival.

**Rival (d) era/model changes: no support.** No document attributes any decline
to a model change; both families ran post-close; the one honest limit stands
(the 08-08 audit lists "one model" among its unmeasured variables). Null, not
proof of no effect.

## 9 · Coverage — read fully · sampled · skipped (and one self-correction)

**The self-correction first, because it is the method working:** the first
mechanical sweep reported fm's ⟲ presence falling 96%→60% and this dig briefly
held a "craters at the close" reading (1/10 glyphs in post-close July). The F1
lane's phrase-level re-measure over **all** 428 fm cards (and a re-check of the
same 10 cards tonight: 10/10 phrase, 10/10 idea, 1/10 glyph) showed the metric
measured **notation style**, not practice. The corrected claim — form held,
loop died — is what §5 carries. A sample-shaped number nearly became a total;
the whole-population re-measure caught it (TRAP-004's class, caught in-flight).

- **Read fully (main loop + lanes):** fm's six mandatory reads + deep-read set;
  the prior-audit baseline the owner named (findings/audits READMEs,
  why-rules-dont-bind, what-the-substrate-caught, both kit-defect worklists,
  checker-classification, foundation-continuation, the full-read audit README +
  all 1,785 findings lines, active-repo intent audit, eap-story,
  eap-retrospective, legibility plan, both owner-direction records, OD table +
  §7 ledger + shipped log whole); superbot's `.session-journal.md` +
  archive (whole) + `.sessions/README.md` + `CLAUDE.md` +
  `collaboration-model.md` + `agent-decision-authority.md` + router header,
  Q-0001–Q-0062 and Q-0273–Q-0275 in full + 22 named rulings in full + the
  12 birth-window cards + all 4 August cards + eval log + 5 EAP reviews whole;
  the kit's README, PL register (all 15 blocks), templates, skills, closeout,
  current-state, bench run-10 + index, changelog v1.21.0 section whole, founding
  plan (821 lines); all 969+428 card files were **opened programmatically** for
  marker counts (whole populations).
- **Sampled (labelled `SAMPLE` wherever used):** superbot June cards 56/701
  (systematic every-23rd + keyword); July cards 31/264 (every 9th + 1
  targeted); fm August cards 40/161 (every 6th + keyword + 3 targeted); router
  bodies Q-0063–Q-0272 headers-only (210 of 275); changelog v1.0.0–v1.20.2
  header paragraphs (26/26 headers, not bodies); PR archaeology 16/70 bodies in
  the #379–#448 window + all 92 owner-commenter hits + 12 comment threads;
  kit engine modules by targeted region (the checker census is a whole-listing,
  the bodies sampled).
- **The verification pass, tallied:** 21 deterministic re-checks (20 PASS; the
  one FAIL corrected two counts in place) + 6 adversarial verifiers — **1
  CONFIRMED, 5 PARTIAL, 0 REFUTED outright**; every correction is applied
  above and marked *(corrected/narrowed in verification)* where it changed a
  claim. The sharpest catch: the headers-only sampling of router bodies
  Q-0063–Q-0272 **dropped a load-bearing owner directive (Q-0266)** that bears
  directly on §8 — its body was then read in full tonight and weighed as the
  fifth rival. ~~That band remains the finding's thinnest coverage.~~
  **Closed 2026-08-28 (session 2): the whole band was re-read
  bodies-in-full —
  [the router band re-read](2026-08-28-router-band-reread.md), which
  narrows seven claims in this finding (its §1 names each).**
- **Skipped (named, not silent):** 645 June + 233 July superbot cards and ~121
  fm August cards beyond greps; superbot PR inline-review threads beyond 4
  spot-checks; kit docs subdirectories (audits/gen2/ideas/operations/planning/
  recipes/reports/retro/reviews) except `program/rulings.md` and the named
  reports; `superbot:docs/planning/projects-eap-*` (older EAP planning corpus —
  noted un-inventoried); satellite repos other than superbot/kit (OD-21's
  estate-wide numbers are cited, not re-measured); **satellite-side references
  for §10 are unmeasured** — every referenced-by fact is fm-side only; pre-06-05
  chat history (does not exist in any repo — the "~PR 400" question is answered
  from committed traces only).

## 10 · Document dispositions — recommendations ONLY (owner's morning letters execute; nothing moved tonight)

Lifecycle per [`../intent.md`](../intent.md) §8b: live → superseded → evaluate
residual value → archive if useful → delete if genuinely valueless. Scope
(decided-and-flagged, per the intent map): the kit-practice lineage set this
dig read — superbot's practice/EAP docs, the kit's doc surface, fm's EAP/seat
and kit-finding records. Three general facts shape every row: (1) **superbot is
frozen** — its rows are keep-by-construction (read-only archaeology; any
banner-edit there is a write the freeze forbids); (2) every superbot EAP doc is
already indexed by fm's `evidence-index.md`, itself cited from a six-read doc —
deletion anywhere breaks that chain; (3) the retrieval fix for this corpus is
**Move 2's digest (compression), not more banners** — several rows below say
"digest-covers" instead of proposing a new pointer.

| document / set | recommendation | the one reason |
|---|---|---|
| `superbot:.session-journal.md` + archive | **keep** (frozen) | the practice corpus itself — §§1–2's primary evidence; 65,927 B of lived guidebook |
| `superbot:docs/owner/maintainer-question-router.md` | **keep** (frozen) | the densest owner-voice corpus in the estate; the kit's PL register cites its Q-numbers as provenance |
| `superbot:docs/owner/` remainder (31 files) | **keep** (frozen) | 8 self-bannered RETIRED; 2 orphans with reuse value the round may want (`cross-agent-trust-ledger.md`, `gpt-5-6-sol-codex-eval-2026-07-10.md` — per-model eval suite, an OD-13 seed) |
| `superbot:docs/eap/` (30 files) | **keep** (frozen) | 2 are ACTIVE E1-thread consumables (`2026-07-18-followup-email-draft.md`, `permission-classifier-findings-consolidated-2026-07-16.md`); the rest is the peak's evidence base |
| `kit:docs/program/rulings.md` · `kit:docs/adopters.md` · `kit:docs/AGENT_ORIENTATION.md` | **keep — live** | PL register is named in fm's boot file; adopters.md is the registry any future wave needs |
| `kit:docs/NEXT-TASKS.md` | **archive-recommend** (kit-side edit, round session) | actively false — tells the next session to distribute v1.18.0; supersede with a pointer to the fm worklist (gap #5's fix) |
| kit docs top-level remainder (~15 small binding/template docs) | **keep** | adopter-facing surface of a live kit; `house-style.md` is fm-orphaned but is D-7's canonical home |
| fm `docs/eap-story.md` · `docs/eap-retrospective.md` | **keep** | the two canonical narratives; fleet-account (six-read) distils and cites them |
| fm `docs/eap-final-night-worklists-2026-07-13.md` · `eap-final-recon-2026-07-14.md` · `eap-owner-checklist-2026-07-14.md` | **extract-then-archive** | all three carry the estate's only future-dated obligation — the **~2026-09-09** trading R5-C gate (due in 12 days) — plus possibly-undistilled owner-checklist rows; move the gate to `owner-queue.md` first, then archive *(narrowed 2026-08-28, [re-read](2026-08-28-router-band-reread.md) §1.7: superbot:Q-0249 set a second ~09-07 dated obligation — the AI-spend cap window — presumably mooted by the close, the mooting never recorded)* |
| fm `docs/eap-audit-collection.md` | **archive** | tracking instrument for a fan-out that completed 2026-07-14; not on any live path |
| fm `docs/eap-final-email-draft-2026-07-14.md` | **archive** (supersede-by note) | superseded by `planning/2026-08-24-final-eap-email-draft.md`; keep as correspondence lineage until E1 sends |
| fm `docs/roster.md` · `control/` (minus `claims/`) · `telemetry/` · `projects/` · `docs/prompts/` (minus the 3 live files) | **keep as bannered RECORD** (already done) | all self-declare historical; re-litigating them is churn; Move 2 digests them out of the read path |
| fm `control/claims/` | **keep — contested, rule separately** | kit still wires `claims_dir` (audit D46); disposition belongs to the kit round, not a doc sweep |
| fm `docs/findings/2026-08-13-substrate-kit-v1210-followups.md` | **keep — live, the round's step-3 input** | the unconsumed 34-row worklist; zero kit pushes since 08-14 make it the standing successor *(consumption began 2026-08-28: rows 13/17/18 fixed by kit #587, row 35 added — the worklist's own tail carries the record)* |
| fm `docs/findings/2026-08-09-substrate-kit-defects.md` · `2026-08-13-v1210-phase2-review.md` · `2026-08-14-v1210-phase3-review.md` | **keep** | consumed but they are the defect→fix audit trail v1.21.0's changelog cites |
| fm `docs/findings/2026-08-09-independent-guard-review.md` | **keep** (already indexed) | adversarial-verification record backing the defects worklist; the findings README routes it — no action *(a round-1 draft said "index-route"; Codex round 2 caught that both rows already exist)* |
| fm `docs/findings/2026-08-07-what-the-substrate-caught.md` | **keep** (already indexed) | directly on the round's question; the findings README routes it — no action |
| **deletions** | **none recommended tonight** | under OD-3-as-amended, deletion needs "served its purpose + no residual value"; every candidate examined either sits in a frozen repo, feeds the open E1 thread, carries the 09-09 gate, or is lineage evidence this round is actively consuming. The honest lever for this corpus is Move 2 compression, not removal. |

## 11 · What the round's next session should fix first (recommendation, not execution)

1. **The one-file unrouted fix:** a pointer in the kit tree to its fm-side
   worklist (gap #5) — smallest possible change, kit venue, no promotion
   question, and it un-strands the round's own step 3. **DONE 2026-08-28,
   session 2 (kit #587).**
2. **Then the worklist's own stated order:** the false negatives first (rows
   13, 17, 18 — the checker failing at its one job), per the fix order restated
   2026-08-21. **DONE 2026-08-28, session 2 (kit #587; the worklist's next
   lead is the work-destroyers 26/29/33, and its row 35 carries the review's
   deferred residuals).**
3. **Name, don't build, the conveyor fix:** Move 1's `♻ Carried forward`
   marker is the designed answer to gaps #1/#2 and it is **held** with the
   rest of the plan — the round should put it to the owner as the first GO
   candidate, with this finding as its evidence base, rather than invent a
   second mechanism.
4. **A targeted re-read of router bodies Q-0063–Q-0272** (the band this dig
   sampled headers-only — verification proved it can hide load-bearing owner
   directives; one session, read-only, superbot stays frozen). **DONE
   2026-08-28, session 2:
   [the router band re-read](2026-08-28-router-band-reread.md).**
5. **And put one question to him with the morning letters** (recorded here per
   ask-and-keep-working): whether the journal survives as a per-repo surface
   (gap #2's second half) — the evidence says the guidebook function migrated
   to routed records (traps.md, Layer-2 threads) everywhere it worked, and the
   kit's planted skeleton has never once been adopted by mechanism alone.

**Layer-2 handoff:** `docs/repos/substrate-kit/README.md` — review-round thread
updated to point here and at §10.
