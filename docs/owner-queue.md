# Owner queue

> **Status:** `living-ledger` — the ONE deduplicated list of things waiting on the owner.
> **Slimmed 2026-07-17.** The pre-cleanup ~68-slug queue is preserved in git history and in
> the **Resolved / Archive** sections below; this rewrite keeps only the **genuinely-open**
> owner asks, a **closed / no-action** index (ids kept — nothing lost), and the historical
> resolved log. Item ids are stable `OQ-` slugs (content-derived): an item keeps its slug
> through rewrites and its move to Resolved.

## Context

This is the current surface for decisions and manual actions that genuinely
require the owner. The consolidation program's NOW pointer, not this queue,
chooses session work. `owner-actions-2026-07-17.md` and `NEXT-TASKS.md` are
seat-era records and must not be used as live action lists.

The fleet-manager D2 pass verified the local asks at the top of this file. It
did **not** re-verify the inherited cross-repo entries or their external
services; that would exceed this repo-only pass. Verify any inherited item in
its owning repository or live service immediately before acting. Full prior
detail lives in git history and in each item's original body. Historical
lineage of the gen-2 launch that seeded the earliest queue items:
[`launch-readiness-2026-07-10.md`](launch-readiness-2026-07-10.md).

---

## Program closed — how to read this queue now (2026-07-21)

The autonomous session period ended 2026-07-22T00:00Z; the seats that used to
execute the agent-side halves of these items are gone. Every remaining item
below is **self-contained** (WHAT/WHERE/HOW/VERIFY) and stays valid: execute
them from the **hub chat venue or any fresh session** (plus your own clicks for
the owner-only ones) whenever convenient — none expires. The final reconcile
pass (this write, fm seat close PR #427) verified each Active item against live
GitHub/the 16:00:18Z trigger snapshot; per-item close notes are appended below.
Master handover + priority order: [PROJECT-CLOSEOUT.md](PROJECT-CLOSEOUT.md) §3.

## Current owner decisions — verified from fleet-manager on 2026-08-10

> **The substrate-kit round's questions have a sitting of their own
> (2026-08-28), and three of them were never in this file.** `MEASURED` today
> against `origin/main`: this queue carried **134 `OQ-` references and no
> entry** for the round's three standing letters — **Move 1's GO**, **the
> journal question**, and **the §10 disposition confirmations** — although
> every session card since 2026-08-28 recorded them as *"unanswered"*. They
> lived only in audit findings, which are `RECORD`-tier and not a surface the
> owner reads. **Two of the three are now proper entries here:** Move 1's GO as
> **`OQ-KIT-MOVE1-GO`** below, and the **journal question** — first closed on
> the grounds that his roadmap § 5.4 answered it, then re-opened when Codex
> review established § 5.4 never mentions `.session-journal.md` — as
> **`OQ-KIT-JOURNAL-SURVIVES`**. The **§10 confirmations** turn out to be
> agent-executable and need no entry; they are dispositioned in § 5 of
> [the OD-24 open-questions agenda](planning/2026-08-28-od24-round-open-questions.md),
> which is the input to the review-and-discussion session he asked for. The
> two `OQ-KIT-*` entries below are the half that *was* queued (both narrowed
> the same day — see their notes). Answers given in the sitting come back here
> as entry updates; the agenda feeds this queue, it does not replace it.

- **`OQ-SUPERBOT-SUCCESSOR-SCOPE` 🟡 OPEN — one question decides the successor's
  size; the other five have defaults the work can proceed under.** (added
  2026-09-04, the SuperBot rebuild review.) The full statement of each, with the
  evidence behind it and the default this plan proceeds on if you say nothing,
  is [`planning/2026-09-04-superbot-rebuild/12-owner-decisions.md`](planning/2026-09-04-superbot-rebuild/12-owner-decisions.md).
  **The one that is genuinely blocking design-lock is the first:**
  **(A) One server, or many?** Is the successor a tool for *your* server, or a
  product other servers install? Both readings are consistent with everything
  you have said on record. It is not a question about ambition — it decides
  whether the whole ~40-panel per-guild setup surface exists at all, which is
  the single largest simplification available anywhere in the plan.
  *Default if unanswered:* **many servers, one guild at a time** — chosen on
  asymmetric cost (per-guild scoping is cheap to build in and expensive to
  retrofit), not on a guess about scale. A one-sentence answer either way is
  worth more here than anything else you could give this plan.
  **(B) Does the successor promise to replace the live bot?** *Default: no —
  it coexists, and the live bot is never a migration deadline.*
  **(C) Third repository, or grow `spider-bot`?** *Default: a third repository;
  your 2026-09-04 statement narrowed `spider-bot` to the Slingy Spider AI
  operations bot, which is a different product.*
  **(D) The middle feature set** — starboard, karma, tickets, counting,
  logging. *Default: optional modules, off by default, none in slice one.*
  **(E) Import nothing?** *Default: yes — no production data migration, ever,
  in any slice.*
  **(F) AI authority on day one?** *Default: AI proposes, deterministic code
  decides, from the first commit — the pipeline your 2026-09-04 spider-bot
  decision already describes.*
  **VERIFY:** an answer to (A) is enough to unblock design-lock; the other five
  can ride along or be left on their defaults. Nothing here needs a click — it
  is six sentences at most.

- **`OQ-FM-FRESH-START-CONFIRMS` ✅ FULLY ANSWERED 2026-08-30 — all three words
  given; nothing owed.** The name landed later the same day as [D-0026]:
  **`estate`**, on his own weighing plus his assent to the recommendation. (added 2026-08-30, the redirect sitting; answered the
  next morning in the structure sitting — his words are quoted in the
  [design home](planning/2026-08-30-fresh-start-redirect.md) § *Answered*.)
  **(1) Hard cutover — ✅ answered, *"Agreed"***, on the split form: the *write
  cutover* is absolute the day the new hub passes acceptance, while the GitHub
  archive flag may lag without creating coexistence.
  **(2) The carry-cut — ✅ answered**, with his principle stated: *"we should be
  very strict about how historical records or finished work should be
  documented … I don't think it's a good idea to leave historical and current
  work in the same files."* Three verbs, not two — carry whole · distill ·
  archive only. Seeding scope also settled: *"mostly from fleet-manager and
  superbot,"* the newer repos contributing to router/summary sections only.
  **(3) The new hub's name — ✅ `estate` ([D-0026]).** *"I think
  'estate' might be a good call, I was personally considering calling it
  'structure' but I feel like that name would make it a bit ambiguous to
  discuss."* Recorded first as a leaning, then settled the same day when he
  assented to the recommendation that `estate` be the name — the form of that
  assent (a blanket yes to a five-item list) is stated in [D-0026]'s provenance
  so it stays correctable.
  His structure sketch (same doc, § Addendum) was also worked in that sitting —
  all four of its questions answered; what remains open is listed in the design
  home's § *Still open after this sitting*.
- **`OQ-KIT-MOVE1-GO` ⏸ ANSWERED 2026-08-28 — HELD, and it is a STAGE, not a deferral.**
  Owner, live in the OD-24 discussion sitting (§ 7 of [the sitting record](findings/2026-08-28-od24-sitting-answers.md)): offered
  three GO shapes and a hold, he chose **hold — still planning**. Minutes later,
  unprompted, he gave the exit condition: *"I am currently running 3 parrallel
  ultracode session to map most of all the repos, once this mapping is all done
  we should use this information to come up with a revised pan. Only after that
  will we move to execution of the 'GO'"* — so **do not re-put this to him until
  the mapping is done and the plan revised**; re-asking sooner asks him to skip
  his own stage. Nothing Move-1-shaped may be built meanwhile, under any other
  name. *(Original ask below, kept for its evidence base.)*
- **`OQ-KIT-MOVE1-GO` (original body) — GO or hold on Move 1, the end-of-session contribution
  line — and if GO, how far does it reach?** (added 2026-08-28, the OD-24
  round's session 4 — **this ask is three sessions old and had no queue entry
  until now**, which is why it reads as unanswered in every card since
  2026-08-28 while never appearing in the surface you actually read.)
  **WHAT:** one word — GO or hold — and if GO, one letter for reach:
  **(a)** fleet-manager only, as a measured prototype · **(b)** prototype **plus**
  a kit release · **(c)** the whole chain including the adopter hops.
  **WHERE:** the hub chat, or the round's sitting;
  [the agenda](planning/2026-08-28-od24-round-open-questions.md) § 2 · C states
  it with its evidence. **WHY-IT-MATTERS:** Move 1 is the designed answer to
  the round's gap #1 — when a session finishes, nothing currently asks what it
  left for the next one, which is precisely the habit that stopped when you
  stepped back. It is built, evidenced and held by your own *"no execution yet,
  because I still have more to plan"* (OD-23, 2026-08-28); nothing since lifts
  that hold. **UNBLOCKS:** the round's whole build track, and the § 2 · B answer
  governs whether that line may ever *block* a session's close.
  **VERIFIED-NEEDED:** none — the hold is your own words, quoted above.
- **`OQ-KIT-JOURNAL-SURVIVES` ✅ ANSWERED 2026-08-28 — DELEGATED to us, with a function named.**
  Owner, live (§ 5 of [the sitting record](findings/2026-08-28-od24-sitting-answers.md)): *"Your call, if the router records are
  functional in the same way thats good enough. But I think the session journals
  would definitely add some value so we can easily find out what went wrong each
  session."* **The decision taken under that delegation: the journal
  SURVIVES in the role it already has — a lean per-repo guidebook — and his
  function is served by RETRIEVAL over the session cards that already exist, not
  by a second record.** `.session-journal.md:5-7` defines the file as *"a
  guidebook, **not a log**"* and routes per-session logs to
  `.sessions/<date>-<slug>.md`; those cards already record what went wrong in
  detail. His word is *"**easily** find out"* — so what is missing is not capture
  (fm holds **433** dated cards at this head, the kit 343 — re-derived; the 431
  carried from the agenda's § 7 is wrong) but any way to scan them. **That is
  retrieval, and retrieval is routing** — the fix family his own cost function
  ranks above building. **Nothing is built, nothing enforced, no new file.**
  *(Two earlier cuts each proposed a re-scoped journal and each lost a
  load-bearing leg to Codex review on fm #964: first "trap records are
  estate-scoped, not per-repo" — refuted by roadmap § 5.3–5.4, marked `OWNER`,
  which makes per-repo traps the intended design; then a lifecycle argument that
  never asked whether the cards already serve the function. They do.)*
  **The open design question a build session inherits:** how anyone gets a
  scannable view across a repo's cards — index, digest, query, or the kit's
  existing reflection miner routed at last.
- **`OQ-KIT-JOURNAL-SURVIVES` (original body) — does the per-repo `.session-journal.md` survive
  as a surface, or is it superseded by routed trap-style records?** (added
  2026-08-28, session 4 — the second of the three letters that had no entry.)
  **WHAT:** one sentence — **(a)** keep it and enforce it · **(b)** retire it,
  routed trap/idea records carry the function · **(c)** keep it unenforced and
  stop calling it a contract. **WHERE:** the sitting;
  [the agenda](planning/2026-08-28-od24-round-open-questions.md) § 2 · E2.
  **WHY-IT-MATTERS:** the kit plants the file in every adopter, no checker
  references it, and the dig measured it byte-identical to its template in 11
  of 14 repos — so it is currently a contract nothing keeps.
  **⚠ Nearly closed in error:** a session judged this answered by the roadmap's
  § 5.4; Codex review on fm #961 established § 5.4 defines a recurring-*trap*
  lifecycle and never mentions the journal (grep, zero hits), and the genesis
  dig calls the disposition *"a round question for the owner"* verbatim.
  **UNBLOCKS:** gap #2's fix family, and Move 1's `journal` value.
  **VERIFIED-NEEDED:** none.
- **`OQ-KIT-PROMPT-DOCTRINE` ✅ ANSWERED 2026-08-28 — PRESENCE DECIDES.**
  Owner, live (§ 3 of [the sitting record](findings/2026-08-28-od24-sitting-answers.md)), choosing *"Never while I'm away; freely
  when I'm present"*. **The conflict was real and he resolved it by drawing a
  line neither rule drew — presence.** *(A first cut said the two "were never in
  conflict"; Codex fm #964 caught that as rewriting the older statement — Q-0128
  says "ever again, no matter what it is for", and the re-read recorded the
  conflict correctly.)* From 2026-08-28 the presence rule governs; Q-0128 stands
  as the **superseded** broader phrasing. So a kit-planted brake **may prompt only when a human is in the
  session** — **his** presence specifically, not any maintainer's. Unattended it
  **must not wait**, and what it does instead is **not settled by his answer**:
  for anything the confirm-before-sending-or-deleting line covers it **refuses**
  (that rule survives untouched); elsewhere the fail-open/fail-closed choice is
  left open rather than assumed.
  **`delete_trigger` stays PREVENTED in every venue**, attended or not; fm's
  never-delete-a-trigger decision and the denying guard hook are untouched. Presence must be computed from the
  venue, not guessed. *(Original ask below.)*
- **`OQ-KIT-PROMPT-DOCTRINE` (original body) — which rule governs kit-planted brakes: your
  "no confirmation prompts ever" or the re-ratified confirm-first line?**
  (added 2026-08-28, the OD-24 round's session 2 — surfaced by
  [the router band re-read](findings/2026-08-28-router-band-reread.md) §4.)
  **WHAT:** one sentence choosing which governs when a kit gate would pause
  for confirmation. Both rulings are yours: superbot:Q-0128 (06-13, *"I
  never want to see such a prompt asking me for my confirmation ever again,
  no matter what it is for"* — destructive-op trade-off accepted) and OD-24
  §3's re-ratified standing line (*confirm before sending or deleting*).
  **WHERE:** the hub chat; a reply to the round's letters folds it in.
  **WHY-IT-MATTERS:** the review round's hook/gate fixes must know whether a
  brake may ever surface interactively. **UNBLOCKS:** the round's gap-#7
  flip-gate design and any kit-planted brake. **VERIFIED-NEEDED:** none —
  both rulings are quoted verbatim in the re-read.
  **⚠ NARROWED 2026-08-28, same day, before he ever saw it — this entry was
  posed without checking for a later statement, and there is one.**
  `.claude/hooks/README.md:483-486` carries him live on **2026-08-09**, two
  months after the Q-0128 line above: *"Delete triggers are the only thing
  that gives me an approval prompt in automode, this will stall your session
  untill I get back. Always prevent using them."* That is the same subject,
  later, and **narrower**: he names the one call that actually raises a
  prompt and asks for it to be prevented — not for confirmation as such to
  be abolished. **It sharpens this entry; it does not answer it** — the
  2026-08-09 line says nothing about whether a *send* or a *delete* may still
  ask first, which is exactly what Q-0128 and OD-24 § 3 disagree about. So the
  fork stays open, restated with three concrete options as **§ 2 · B2** of
  [the round's open-questions agenda](planning/2026-08-28-od24-round-open-questions.md).
  *(A first version of this note said the fork "largely dissolves" and routed
  the residue to the agenda's § 2 · B — a different subject, blocking a flip
  rather than interrupting him. Codex review on fm #961 caught it before he
  saw either.)* Put the sharpened fork to him, not the original two-way one.
- **`OQ-INTENT-WRITE-UP` — write your intent, against the questions prepared for
  you.** (added 2026-08-28, the intent elicitation sitting — your own ask:
  *"I'd like to spend a good while thinking and writing about these things."*)
  **WHAT:** answer as many of the open-ended prompts in
  [`planning/2026-08-28-owner-intent-questions.md`](planning/2026-08-28-owner-intent-questions.md)
  as you feel like — any order, any length, skip what does not spark. Four
  parts: the estate above any single repo · a reusable set for any repo ·
  specific ones per repo · how you want to work. **`"I don't know yet"` is a
  real answer** and is worth recording rather than being guessed at later.
  **WHERE:** anywhere you like — chat, a file, notes. A session turns it into
  the records without changing your words. **WHY-IT-MATTERS:** the estate
  records *state* exhaustively and *purpose* almost nowhere; `intent.md` is the
  only real intent document and it covers **1 of 28 repos**. The Layer-2 shape
  you ratified on 2026-08-08 included a `goals.md` slot that was **deferred** —
  this fills it. **UNBLOCKS:** per-repo intent records in your words, and the
  revised plan having a stated foundation rather than an inferred one.
  **THE FOUR MOST VALUABLE, if you only get to a few:** what you wish you could
  hand over completely but currently can't trust · what a good run of Slingy
  Spider feels like (that description IS the core-feel spec, and nothing in the
  repo contains it) · the most annoying thing an agent does, specifically and
  pettily · what you actually want to make with `creator-kit`.
  **VERIFIED-NEEDED:** none.
- **`OQ-KIT-RENAME` — the kit's published name: you ruled it changes, and the
  name is the one thing only you can supply.** (added 2026-08-28, the OD-24
  discussion sitting — §§ 11 + 15 of
  [the sitting record](findings/2026-08-28-od24-sitting-answers.md).)
  **WHAT:** one word. `kit:README.md:9` still reads *"`substrate-kit` is a
  placeholder name"* and defers the published name to you; you chose **"Change
  it now while it's still cheap"** over keeping it, then chose **"I'll pick the
  name later"** over three candidates offered in the estate's naming style
  (`agent-substrate` · `groundwork` · `session-kit`). So the directive stands
  and only the name is missing. **WHERE:** hub chat, one word.
  **WHY-IT-MATTERS:** 21 releases have shipped under a self-declared
  placeholder, and the rename gets more expensive with every adopter added.
  **WHY IT IS NOT OURS:** you were offered the chance to delegate it and did
  not — no session may pick a name on your behalf.
  **UNBLOCKS:** the rename itself (a build-session job with real blast radius:
  the GitHub repo name, adopters' vendored path references, the generated
  `docs/adopters.md`, and every fleet-manager document naming the repo — it
  should not ride the same PR as a doc sweep). **VERIFIED-NEEDED:** none.
- **`OQ-EAP-SPEND-WINDOW-MOOT` ✅ CLOSED 2026-08-28 — not currently relevant, by his own read.**
  Owner, live (§ 17 of [the sitting record](findings/2026-08-28-od24-sitting-answers.md)): *"There hasn't really been much API use
  lately, so this is currently not relevant"*. The window passes **without a
  decision, because its premise does not hold** — there is no meaningful spend to
  average. kit `PL-005` (observe-first budgets; caps deferred, not adopted)
  stands unchanged, **no cap is adopted, and no meter was ordered** — the option
  offering one was available and not taken, so a session must not build one off
  this answer. Re-opens on his own named condition: API use going up again.
  Prerequisite discharged the same session — `[D-0011]`'s self-contradiction is
  reconciled in [`decisions.md`](decisions.md). *(Original ask below.)*
- **`OQ-EAP-SPEND-WINDOW-MOOT` (original body) — record whether the ~09-07 spend-cap
  decision window is mooted.** (added 2026-08-28, same source, §1.7.)
  **WHAT:** one sentence — superbot:Q-0249 (07-06) deferred AI-spend caps to
  *"the average of a couple of months"* (window lands ~2026-09-07); the
  program close presumably mooted it, but the mooting was never recorded and
  a dangling dated obligation is the owner-words-loss class the round
  tracks. **WHERE:** hub chat, one line. **WHY-IT-MATTERS:** the genesis
  dig's §10 called the ~09-09 trading gate the estate's only future-dated
  obligation; this is the second. **UNBLOCKS:** closing the record.
  **VERIFIED-NEEDED:** none.
  **⚠ REFRAMED 2026-08-28, same day — the premise was wrong and the real
  question is better.** Q-0249 is **not** an unrecorded dangling obligation:
  it was promoted to program law on 2026-07-07 as substrate-kit
  `docs/program/rulings.md` **[PL-005] "Observe-first budgets — telemetry
  before caps"**, carrying his full quote and the method (caps *deferred, not
  adopted*; instrument spend, then decide from the measured average). What is
  actually true, and worth one line from him: **no meter ever ran** — the
  telemetry feed carried no cost field and stopped 2026-07-13 — so the
  "decide from the average" step cannot execute and there is nothing to moot.
  The reframed ten-second ask is § 2 · H of
  [the agenda](planning/2026-08-28-od24-round-open-questions.md): leave it
  uncapped, or set a cap.

- **`OQ-ESTATE-ARCHIVE-LIST` ✅ ANSWERED 2026-08-22 · ✅ EXECUTED 2026-08-23 —
  the nine ungated repositories are archived** (added 2026-08-22, OD-18 table
  fm #906; answered live the same day; executed as program step **R5**, fm #912).
  **WHAT WAS DONE, and it is verified rather than reported:** the § 4
  pre-archive writes landed first — a README notice *and* an updated GitHub
  description on all nine, `proxybench` #1 closed, the three labs marked
  FINISHED and UNMAINTAINED — each confirmed by a live re-read *before* any
  archive call. Then the nine were archived one at a time and confirmed by a
  fresh `GET /user/repos`: **26 repositories, 9 archived, 0 deleted.** Nothing
  was deleted, and **the three gated rows were not touched** — `superbot-next`
  and `superbot-plugin-hello` still wait on GCB-1, `product-forge` on R2, exactly
  as the reading below said they would.
  **IF THE READING WAS WRONG, it costs one call to undo** — archiving is
  reversible and every read path was tested working afterwards, including the
  labs' documented `pipx`/`pip install git+https://…` (measured: `cfgdiff 0.1.1`,
  exit 0, installed *from* the archived repo). Nothing further is asked of the
  owner here.
  **HIS WORDS, verbatim:** *"use the continuation prompt skill so the next
  session can execute the archive."*
  **THE READING, stated so it can be checked rather than assumed:** that is
  taken as approval of the **nine ungated repositories** below. The other
  three are gated on **conditions, not on his preference** — `superbot-next`
  and `superbot-plugin-hello` on GCB-1, `product-forge` on R2 — so this
  approval does **not** release them; they move when their gate opens, not
  before. If the reading is wrong he says so and it is undone: archiving is
  reversible, which is the whole reason this was safe to answer in one line.
  **Original ask, kept for provenance:**
  **WHAT:** approve (or edit) the twelve-repo archive list in
  [`planning/2026-08-22-repo-dispositions.md`](planning/2026-08-22-repo-dispositions.md)
  § 2: `superbot-games`, `superbot-idle`, `superbot-mineverse`,
  `trading-strategy`, the three `codetool-lab-*` repos, `Substrate-kit-app` and
  `proxybench` — plus **three that are gated, not free-running**:
  `superbot-next` and `superbot-plugin-hello` **only after GCB-1** (the new bot's
  repo is confirmed and the architecture donor is no longer being harvested), and
  `product-forge` **only after R2** (phone-controller has graduated). A yes to
  this entry is a yes to the nine ungated ones and to the three *when their gate
  opens* — it does not release them early. Deletion is recommended for
  **nothing**. **WHY-IT-MATTERS:** the archive step
  has been described since 2026-07-26 and has never run on any repository —
  measured again on 2026-08-22, 26 repos and zero archived — so every parked
  repo is still structurally identical to an active one, which is exactly the
  noise OD-17 names. Approving this takes the active estate from 26 to 14.
  **WHY IT IS SAFE — with the certainty each half actually has:** archiving makes
  a repo read-only while it stays public, and it is reversible — both **stated in
  GitHub's documentation**, so a wrong row is undone rather than paid for. That
  the `pipx install git+https://…` paths keep working is **`REASONED`** from the
  code staying readable, not stated by GitHub and never tested against an
  archived repo (`ESTATE.md` says so too); the first archive settles it in one
  command. And whether archiving stops **scheduled Actions** is **`UNVERIFIED`** —
  the docs do not say, so do not count the crons as cleaned up until one archive
  has proved it either way. **WHAT
  HAPPENS THEN:** an agent runs R5, doing the § 4 pre-archive writes first (they
  need the repo writable) and archiving one at a time. **WHAT IS NOT ASKED:**
  nothing about your five keeps that are yours — `venture-lab`, `shiftlife`,
  `gba-homebrew`, `pokemon-mod-lab`, `curious-research` all stay as they are.
  **HOW:** reply with a yes, or name the rows you want moved.

- **`OQ-GBA-NEXT-PICKS` — 🎮 gba-homebrew: the letter pick + playtest verdicts
  that would resume the game lab (added 2026-08-21, fleet review fm #878).**
  **WHAT:** gba's own closeout (`docs/PROJECT-CLOSEOUT.md` § c–d) leaves two
  genuinely owner-only items that were in no live `OQ-` entry until now: the
  **A1/A3 next-game letter pick** (the Tinderhand / Starloom pre-plans are
  complete slice ladders, ready to execute on your letter) and the **four
  playtest verdicts** on shipped games. **WHY-IT-MATTERS:** the repo is one
  letter away from having real agent-executable work; nothing multi-session
  moves without it. **NOTE for the executing session:** the required
  `NDS ROM build` check reds on cold-cache PRs (BlocksDS 1.21.1 pin
  unrecoverable; migration branch `claude/nds-toolchain-1-22-3` retained) —
  fixing or re-scoping that is the real first technical step of any resume.
  **HOW:** letters in the hub chat. **VERIFIED-NEEDED:** owner-only —
  product/creative picks.

- **`OQ-PML-EMERALD-LETTER` — 🎮 pokemon-mod-lab: the B/A/Q letter — the one
  ask that unblocks the whole repo (added 2026-08-21, fleet review fm #878).**
  **WHAT:** pml's closeout (§ c, Priority 1) gates everything multi-session on
  one letter: **B** = keep deepening the QoL+ preset · **A** = start the
  Emerald Hard slices · **Q** = playtest first (the Q1–Q3 feel-patch verdicts
  are the secondary ask). *"Nothing multi-session moves until the owner
  picks."* This ask existed only inside the private repo's closeout — a
  session answering "what waits on the owner" from this queue alone would
  have missed it. **HOW:** one letter in the hub chat. **VERIFIED-NEEDED:**
  owner-only — product direction. *(The kit hop for pml stays owner-paced
  per `OQ-KIT-V1-21-RELEASE`.)*

- **`OQ-GCB-REVIEW-SCOPE` — 🤖 what must the review bot actually DO? Answering this
  unblocks the roadmap re-sequencing and the first slice's definition — **not** the
  whole track: `GCB-1` is a second, separate owner gate and repository creation
  still waits on it (2026-08-23, owner live).**
  **UPDATE 2026-08-24 — the GCB-1 clause above is RESOLVED; this ask is not.**
  The repository exists: `menno420/spider-bot`, created and deployed **live**
  the same day in owner-directed sessions outside fleet-manager (name
  owner-chosen over the plan's `superbot-community` default) — v0.1.0 tester
  funnel + human-only roster + AI chat, Phase-0 hardening (78-test harness +
  informational CI) landed hours later. What remains owner-only is exactly
  this entry's question: which review/testing scopes (the A–D mix below) the
  bot grows toward — now as spider-bot's next-phase direction rather than a
  pre-creation gate. Registration: the [`ESTATE.md`](ESTATE.md) row +
  [`repos/spider-bot/`](repos/spider-bot/README.md).
  **WHY THIS IS NEW:** `GCB-1` asks whether to create the repository and under
  what name. It does **not** carry this, and OD-19 introduced it: *"first there
  should be a smaller review oriented bot for the game server."*
  **WHAT IS BLOCKED:** [`delivery-roadmap.md`](planning/2026-08-21-game-community-bot/delivery-roadmap.md)
  orders the AI spine at Phase 1, community/safety through Phase 4, and the
  game-testing loop at **Phase 5**. If your review bot is that loop, the
  executable order contradicts OD-19 and needs re-sequencing before Phase 0.
  **A session must not answer this for you** — "review oriented" is one phrase,
  and picking its contents would be manufacturing product intent
  ([`intent.md`](intent.md) § 8b).
  **OPTIONS, pick any mix or write your own:** **(A) playtest capture** — sessions,
  runs, clips, who tested what · **(B) bug/feedback intake** — structured reports
  from testers into something you can triage · **(C) build handoff** — announce a
  build, collect who installed it, chase the ones who didn't · **(D) feedback
  triage** — cluster and rank what testers said.
  **HOW:** letters in the hub chat, e.g. "B and D first".
  **UNBLOCKS:** re-sequencing the roadmap, and the first slice's exit gate.
  **NOTE the separation constraint is already settled** (OD-19) — this asks only
  what the *first* bot does, not whether the bots merge. They do not.

- **`OQ-BOT-DB-BTD6-PRUNE` — ⚑ the bot DB is 97.5 % accumulated BTD6
  ingestion history (last activity 27 min before the probe) — prune
  approval + the loop question (2026-08-20).**
  **WHAT:** the keep-bot-only worklist's slice-5 sizing (read-only, measured —
  [`findings/2026-08-14-railway-websites-audit.md`](findings/2026-08-14-railway-websites-audit.md)
  § 8) refuted the "XP / server-logging" suspects: the 949 MB database is
  **three `btd6_*` tables (~925 MB)** — `btd6_source_snapshots` 668 MB /
  286,489 rows · `btd6_ingestion_runs` 135 MB / 289,944 rows · `btd6_facts`
  122 MB — **averaging one run per ~26 s over the 2026-05-27→08-20 span**
  (count ÷ endpoints; steady-vs-burst unmeasured); **newest row stamped
  27 min before the sizing run** (last observed activity). All bot user
  data combined is
  ~10 MB. This history is the ~2 GB dumps, most of the DB's 831 MB resident
  RAM ($8.39/cycle), and the weekly backup's wire weight. **OPTIONS (pick per
  line):** **(P) prune history** — keep the most recent N days of
  `btd6_source_snapshots` + `btd6_ingestion_runs` (recommend N=30; facts
  kept), after a fm #867-style restore-verified dump to `estate-backups`;
  a session executes on your letter + N. · **(L) the loop** — should the bot
  still be ingesting BTD6 sources at this volume at all? A cadence/stop change
  is a `worker` config/code change, which the hard rail reserves for your
  explicit directive — nothing was touched. **HOW:** e.g. "P 30" and/or an L
  answer, in the hub chat. **RISK:** P is preceded by a verified dump;
  L is reversible config. **UNBLOCKS:** the last cost line the audit left
  standing (§ 5.2's durable half). (2026-08-20)

- **`OQ-RG-ORPHAN-VOLUMES` — 🧹 reliable-grace holds 4 volumes for its 1
  Postgres (2026-08-20).** **WHAT:** `postgres-botsite-volume` survived its
  service's 08-16 dump-and-delete, and two suffixed strays
  (`postgres-volume-OMuK`, `postgres-volume-700u`) sit beside the live
  `postgres-volume` — orphaned volumes outlive `serviceDelete`. Hygiene, not
  cost (estate disk is $0.27/cycle). Hard-rail adjacency (the project is the
  bot's home) is why no session deletes these on inference. **OPTIONS:**
  **A) delete the three orphans** (the botsite one's contents are already
  archived restore-verified on `estate-backups`; the strays predate the
  audit and mount nothing) · B) leave as-is. **HOW:** one letter; a session
  runs `volumeDelete` by exact id, live `postgres-volume` untouched either
  way. (2026-08-20)

- **`OQ-GEMINI-NOTEBOOKS` — 🧪 you want to start creating notebooks in Gemini
  (added 2026-08-23, owner live).** **HIS WORDS, verbatim:** *"what I want to do
  is start creating notebooks in gemini to help me with certain things and just
  to explore that feature."* **THE READING, stated so it can be corrected:** two
  goals at once and they want different handling — *"help me with certain
  things"* is a tool need with real subjects behind it, and *"just to explore
  that feature"* is deliberate play with no deliverable owed. A session should
  not collapse the second into the first by demanding a use-case before he is
  allowed to poke at it. **✅ PRODUCT ESTABLISHED 2026-08-23 — he sent a screenshot, and the guess was
  wrong.** It is **Notebooks inside Gemini Apps** — a `Notebooks` section in the
  app's own sidebar with `Nieuwe notebook`, splash reading *"Maak kennis met
  notebooks · Til je projecten naar een hoger niveau | **Mogelijk gemaakt door
  Gemini Notebook**"*. **`Gemini Notebook` IS NotebookLM, renamed** — its own
  splash says so verbatim: *"NotebookLM heet nu Gemini Notebook. Nieuwe naam.
  Hetzelfde geweldige product."* So this is **one product with two entry
  points**: the standalone Gemini Notebook surface, and a `Notebooks` section
  inside the Gemini app *"mogelijk gemaakt door Gemini Notebook"*. His account
  shows **PRO** on both. UI is Dutch.
  **Corrected same day, and the correction is the point:** this entry first said
  *"NOT NotebookLM"* — an inference drawn from one screenshot's wording before
  the second screenshot showed the rename banner. He supplied the evidence that
  overturned it. Third instance today of the same shape (see
  [`findings/2026-08-23-active-repo-intent-audit.md`](findings/2026-08-23-active-repo-intent-audit.md)
  § 3): **his live knowledge beat an agent's reading, again.**
  **THREE CONSTRAINTS READ OFF THAT SCREEN, and the first one bites:**
  1. **Max 300 sources** (*"Upload maximaal 300 bronnen"*) — read off the Gemini
     Apps splash on a PRO account; whether the standalone surface or a different
     tier differs is **not** established here. The `idea-engine`
     corpus is **566 files** and does not fit one notebook.
     **⚠️ CORRECTED 2026-08-23, same day — do NOT concatenate to fit.** This
     entry first said *"any bundle must consolidate (concatenate by theme)"*.
     **That advice destroys the feature the upload exists for.** This product's
     value is a citation resolving to a specific source; merge fifty idea files
     into one themed blob and every citation resolves to the blob, so the
     grounding is exactly as coarse as the merge. **Partition instead of
     compressing:** the limit is per notebook, so 566 files becomes **2–3 themed
     notebooks**, each under 300, with file-to-source staying 1:1 and citations
     exact. *Honest edge:* that 300 is **per notebook** rather than per account
     is read from where the number appeared — in a notebook's own feature list —
     and was **consistent, not confirmed**. **✅ CONFIRMED 2026-08-23** from
     Google's own Gemini Notebook FAQ, which states **"Up to 50 sources per
     notebook"** and **"100 notebooks per account"** (free tier): the source cap
     is **per notebook**, and the number of notebooks **is** itself capped. Both
     open questions are answered in *shape*. What stays open is only the **PRO
     numbers** — that page carries the free tier only, so the **300** remains
     your splash reading (`OWNER`, not `MEASURED`) and is still not established
     for the standalone surface. Full reference:
     [`providers/gemini-notebook.md`](providers/gemini-notebook.md).
     **Selection stays legitimate** — picking the best 300 of 566 is lossy but
     keeps citations precise; concatenation is the option that does not.
     **Sizes re-derived live 2026-08-23, and one corrects an earlier plan:**
     `idea-engine/ideas/` holds **742 blobs — 580 `.md`, minus 14 README/index =
     566 idea files**, which reconciles the estate's long-standing "566" against
     the raw tree count (the remainder is 157 `.py` plus indexes).
     **⚠️ CORRECTED TWICE, and the second correction is the measured one.**
     fm #934 (via `@codex`) spotted that `superbot` 249 · `fleet` 221 ·
     `venture-lab` 103 · `superbot-games` 86 sum to **659**, not 566 — a real
     inconsistency. It then *inferred* the cause ("overlapping consumer
     references") and wrote that inference into the records as a finding.
     **fm #936 measured it, and the inference was wrong.** The live tree
     (1,373 blobs) grouped on `ideas/<consumer>/` returns **249 · 221 · 103 · 86
     — exactly the recorded figures** — and those directories are exclusive by
     construction. The mismatch was a **denominator error**: `566` is `.md` minus
     14 README/index files; `659` is *all* files (157 `.py` included) in only the
     four largest of **fourteen** consumer dirs, and 659 ⊂ 742 total under
     `ideas/`. **Your original seams were right all along.**
     **✅ BUILT 2026-08-23 (fm #936):** 779 sources + 3 indexes = **782** across
     **3 notebooks** (300 / 292 / 190), split on those seams with `superbot`
     whole in #1 and `fleet` whole in #2, no file merged or split. One download:
     [`idea-engine-notebook-bundle.zip`](https://github.com/menno420/fleet-manager/releases/tag/notebook-bundle-idea-engine-2026-08-23)
     — make one notebook per folder. 594 files held back (`.sessions/` 504 above
     all, a different corpus), each named with its reason. **`curious-research`, by contrast, is 126 files total
     (75 markdown): `guides` 49 · `projects` 22 · `ideas` 15 · `research` 14 ·
     `docs` 7 · `site` 6 · `arm` 2. It fits in ONE notebook** — the partition
     advice above applies to `idea-engine` only, and an earlier suggestion to
     split `curious-research` into themed notebooks was unnecessary.
  2. **Custom instructions are supported** (*"Stel aangepaste instructies in"*) —
     read off the splash's third bullet. *That this can carry a standing brief is
     an inference from the feature name, not a tested behaviour.*
  3. **The privacy split is asymmetric and worth stating plainly:** source files
     added in Gemini Apps are **not** used to train the models, but
     *"gesprekken met je notebook in Gemini Apps worden opgeslagen volgens je
     instellingen voor Activiteit bewaren"* and are used **to improve the AI
     models**. Sources in are protected; the conversation is not. Sources can
     still be added with Activiteit bewaren off.
  **THE OBVIOUS FIRST NOTEBOOK, from his own recent chats on that screen** —
  Laser Cutting, Hobby CNC Milling, Hobby Servo Robot Arm, Fusion 360: that is
  **`curious-research`'s** exact domain (the Dutch workshop notebook — 3D
  printing, robot arm, Arduino). It is also a **keep, parked by his own words**
  and therefore safe to feed a notebook without disturbing live work.
  **WHY-IT-MATTERS / where the estate can actually help:** if it is NotebookLM,
  the estate is unusually well-stocked with corpora that are painful to read and
  ideal to ground a notebook on — the 566-file idea corpus (`idea-engine`), the
  389 session cards + 52 findings here, the EAP evidence pack, and the archived
  repos' closeouts, which are now read-only and therefore stable sources.
  **WHAT AN AGENT CAN DO WITHOUT HIM:** prepare export bundles — flatten a
  corpus into upload-ready files with provenance kept — so his first notebook is
  a paste, not a project. **WHAT ONLY HE CAN DO:** the account-side steps
  (creating notebooks, uploading, any paid tier), since this is his Google
  identity. **CREDENTIALS NOTE, so nobody probes blind:** this estate's Gemini
  API access is documented at
  [`conventions/vertex-first-for-gemini.md`](conventions/vertex-first-for-gemini.md)
  and [`providers/gemini.md`](providers/gemini.md) — **but Gemini Notebook (ex-NotebookLM) is a
  consumer surface behind his Google login, and whether it is reachable by any
  API this estate holds is UNVERIFIED.** Note the rename means older estate notes
  and any external recipe may still say "NotebookLM" — same product, do not treat
  the two names as different things. Do not assume it is, and do not
  record a wall if it is not; check first. **Working assumption until measured:
  an agent prepares files, he uploads them.**
  **✅ BUILT 2026-08-23 — the offer was put to him AND the bundle built in the
  same turn** (fm #934), because the build needs nothing from him and a "yes"
  should cost an upload rather than a wait. **His step is now one download:**
  [`curious-research-notebook-bundle.zip`](https://github.com/menno420/fleet-manager/releases/tag/notebook-bundle-curious-research-2026-08-23)
  — unzip, drag everything in `sources/` into a new notebook. Download verified
  end-to-end (sha256 identical, `testzip` OK).
  **126 files in → 110 sources out** (109 + a generated index), **17 held back**
  with a stated reason each, **0 merged**. All 75 `.md` are byte-identical to the
  repo. Built by [`../tools/build_notebook_bundle.py`](../tools/build_notebook_bundle.py),
  which is corpus-agnostic so `idea-engine` reuses it.
  **Three findings from building it, two of which would have degraded the
  notebook:** (1) `index.html` is **not** a render of `guide.md` — they are
  self-contained animated explainers whose step-captions live in a JS array, per
  the repo's own `visual-explainers` skill, so they are kept but text-extracted
  rather than uploaded as ~4 KB of minified CSS/JS each; (2) five directories are
  **redirect tombstones**, named as such by `curious-research`'s own
  `guides/README.md` ("Compatibele oude paden") — uploading them would let the
  notebook answer *"use vulling instead"* and reintroduce the divergence that
  merge removed, so they are held back (the one exception,
  `how-a-pr-flows/guide.md`, carries real content and is kept); (3) a **leading
  dot makes a source invisible** to the upload picker and to select-all — caught
  only because `ls` and `ls -A` disagreed.
  **What is still yours:** creating the notebook and uploading, since it is your
  Google identity — and, if you want them, the two PRO numbers above, which are
  a glance at the UI. **The release is a data bundle, not a software release;
  it is deletable in one call once the notebook exists.**

- **`OQ-E1-FINAL-EAP-EMAIL` ▶ DRAFTED IN FULL AND STAGED 2026-09-03 (fm #1017) — what is left is his: read, edit, add the recipients, send.**
  Shape A (owner, 2026-09-02, [§ 5b](findings/2026-09-02-owner-direction.md)):
  Part 1 proposed from the beat table and his answers (beat 3, the verdict
  paragraph, is his alone), Part 2 kept at the 1,686 words he chose plus two
  one-clause patches and one addendum — the Projects-versus-sessions answer in
  his terms, with the three false-done rows as the evidence that verification
  is the deciding line. Block: **2,299 words** by `--count` after the evening rewrite (his edits in fm #1019 + the independent review), addendum 488 of body plus 75 of its source bullets, Part
  1 696 words in his own words. **Staged as a Gmail draft in his own mailbox, no recipients:**
  Drafts → *"Claude Code Projects EAP — the final review, six weeks on"* (id
  `r-9208017789511753451`). WHAT (after the evening rewrite): read it again, add what he wants to add, answer the one-word calls in [the draft's § 2](planning/2026-08-24-final-eap-email-draft.md) (a–e, subject, the optional fourth item, length, and the evening's five: public-soon · thesis · hours · permissions · counts), add the recipients — the
  EAP alias in **To** and the three cc addresses, all in the July thread's
  headers — and send from a fresh compose (not a reply). WHY-IT-MATTERS:
  two promises to a named person on 2026-07-21, the record for both sides.
  VERIFIED-NEEDED: the API half of the Gmail-draft route is measured (create +
  list-back); **his half — that he sees and can edit it in Gmail — is recorded
  only when he says so**, in words. After sending: the send record in § 3 of the
  draft (date, subject, `Message-Id`), then this entry closes.
- **`OQ-E1-FINAL-EAP-EMAIL` (superseded body) ▶ RE-BRIEFED 2026-08-28 — "soon", and its content brief just WIDENED.** *(Superseded by the 2026-09-03 entry above; kept for its record.)*
  Owner, live (§ 19 of [the sitting record](findings/2026-08-28-od24-sitting-answers.md)). He first selected *"Leave it — not now"*,
  then revised it unprompted minutes later — **the revision governs**: *"About
  the mail, that really is something to work on soon, and I think that all the
  audits I'm doing right now will provide valuable information, not only about
  the EAP itself but generally about how agents work, whih would be a valuable
  addition to the mail"*. **Three changes:** (1) timing — *soon*, not dormant;
  (2) a **new INPUT, explicitly NOT a gate** — the mapping audits' output is
  meant to go into it, making the mail a third consumer of that work; but he did
  **not** say it must wait for the mapping to finish, and *"soon"* says
  otherwise, so **fold in whatever exists at the time and do not park it**
  *(a first cut wrote "wait" here; Codex fm #964 caught it contradicting the same
  answer's "soon")*; (3) **scope widened** — it now carries what those audits show
  *generally about how agents work*, not only the EAP. **Consequence for the
  one-page question: it cannot be settled yet**, because he has just added to the
  content. Do not restructure to one page against the old brief.
- **`OQ-E1-FINAL-EAP-EMAIL` (original body) — write and send the final EAP review email
  (owner-reserved, your pace).**
  **▶ UN-DEFERRED BY THE OWNER, 2026-08-24 (live) — this supersedes the deferral
  below.** HIS WORDS: *"today I want to work on and possibly finish the final EAP
  mail… go through the fleet manager and my email, find out everything we already
  told them and found out, then see what more you can prepare for me and how we
  should complete the email in such a way that this is actually a new valuable
  source for anthropic."* **Done this session:**
  [the source sweep](findings/2026-08-24-e1-source-sweep.md) (the fifteen-row
  ledger of what the prior mails already argued, the never-sent 07-18 findings,
  seven month-after findings examined — **six standing**, N6 tested against a live API and withdrawn — today's re-measured figures) and
  [the assembled draft](planning/2026-08-24-final-eap-email-draft.md) (the mail
  between COPY markers, **seven** overturnable decisions, **seven** pre-send
  calls). **✅ ASSEMBLED AND MERGED 2026-08-24 (fm #943)** — six adversarial
  review rounds, **62 findings, all conceded, 0 survived**, five of them
  vendor-facing errors caught in rounds 5–6 alone.
  **▶ 2026-08-25 — THE REVISION PASS RAN AGAINST YOUR OWN CALLS. WHAT IS LEFT IS
  PART 1 AND SENDING.** The one open question was put to you before any edit, and
  you answered it and two of the seven pre-send calls:
  - *"a revision pass and my own section added/edited"* = **two operations, and
    the pass covers the whole document** — § 1 and § 2, not only the COPY block.
    This is the sentence fm #945 recorded as a P1 for a session having filled it
    in; it was asked, not assumed, and **your answer was wider than the guarded
    reading, not narrower**.
  - **The length (§ 2 item 6): the literal cap.** Findings 1–3 and asks 1–5 only;
    findings 4–5, asks 6–14 and the optional finding 6 are out.
    **2,097 → 2,299 words** as of 2026-09-03 — the cap took it to 1,686 and Shape
    A's addendum (2026-09-02, fm #1017) added the rest. *(The count is method-dependent and that was never
    stated, which is why it drifted: the draft said 2,082, this entry said 2,127, the file
    measured 2,151 — and **none of the three was right**, because the method was
    never stated and both obvious methods count punctuation or bullet glyphs as
    words. The mail as pasted was **2,097** before his cut, **1,686** after it on
    2026-08-25, and is **2,299** with the 2026-09-02 addendum and patches
    (fm #1017) — 2,097 is the before-cut baseline, not the send length. One command settles it:
    `python3 tools/render_eap_mail.py --count`, and
    `python3 tools/check_eap_figures.py` checks this entry still agrees with it.)*
  - **The 97.5 % (§ 2 item 2): cut the ratio, keep the shape.** The mail quotes
    the audit's own uncontested rows instead — **949 MB store · 925 MB in three
    ingestion-history tables · ~10 MB across every other table combined** — and carries no
    percentage at all. The prose-versus-rows contradiction in the audit is left
    **unresolved**; no session picked a side.
  **Five consequences of the cap are surfaced in § 2, each one line to overturn:**
  the venue asymmetry (ask 8, *"the strongest single argument in the estate"*) is
  gone; the prior-mail pointer that § 1 decision 2 requires moved onto the July
  findings link; the month-after spine is three findings rather than five;
  **1,686 words is about three pages** (2,299 with the 2026-09-02 addendum) — but **one page IS reachable**, by
  restructure rather than subtraction. Measured: **487 words at one sentence per
  block, 667 at two, 853 at three.** But the 471 is a **floor, not a draft** —
  printed out, it keeps no scale numbers and no evidence under any finding. A
  readable one-pager has to be written rather than extracted and lands nearer
  667, trading away forensic detail that is already public at the mail's four
  links. *(This entry said "no route reached one page"; that was only ever
  true of cutting things — nobody had tried changing the shape.)* and **eight words were added — the only content
  added to the outbound mail** — accounting for the seven repositories created
  after the program closed, which the scale paragraph had left unexplained
  (→ *"cut it"*). **Items 1, 3 and 4 are now moot** — ask 12, the
  €30 and the July counts all lived in the cut material.
  **What remains yours and only yours: writing Part 1 — a beat table, never
  drafted prose — and sending it.** No session sends it. **Then three values
  close this entry:** the sent date, the exact subject, and the Gmail
  `Message-Id`, into the staged row in § 3 of the draft — because § 0 of the
  correspondence record measured that **four EAP-thread messages are no longer
  retrievable from Gmail — three of them your own sent mail** (07-08, 07-12,
  07-16 01:52) **and one the vendor's 07-14 reply to you** — thread A holds two messages where five were
  recorded, over five probe runs and two positive controls, one lane including
  trash. That is a *retrievability* measurement, not a finding that they were
  destroyed; the record states no cause and says none should be inferred. Either
  way the mailbox cannot be the archive of record.
  **HIS SEND-DAY PLAN, stated 2026-08-24 late, VERBATIM and not decomposed:**
  *"tomorrow morning I will start fresh and create and send the email after a
  revision pass and my own section added/edited."*
  **What that settles:** he sends it himself, tomorrow morning, from a fresh
  session, and **something is revised or edited before it goes.** That is
  strictly more than the line above assumed — so read that line as *"the minimum
  outstanding"*, not as the full list.
  **What it does NOT settle, and a session must not fill in** (`@codex`, fm #945,
  P1 — an earlier version of this entry did exactly that): the sentence names
  **no target for the revision pass** and does not say whether *"a revision pass"*
  and *"my own section added/edited"* are two operations or one description of
  the same one. **Do not record or act on a Part 2 decomposition.** If it matters
  to what you do next, **ask him** — one question, at the start, cheaper than
  guessing.
  **The safe reading, which is all a session needs to start:** be ready to edit
  the assembled draft wherever he directs, and do not assume the only outstanding
  item is Part 1.
  ~~**⏸ DEFERRED BY THE OWNER, 2026-08-23 (live, late) — this supersedes the
  "today" stamp below.**~~ HIS WORDS, verbatim: *"The email aswell but that's
  something I still want to wait a little bit with because I still feel like we
  can do some more organizing."* **THE READING:** the evidence pack is not the
  blocker and is not stale — the **organising** is what he wants further along
  first. So no session should nudge him toward sending it, and no session should
  treat the pack's existence as a reason to. It un-defers when he says so.
  **What "more organizing" plausibly points at, offered as candidates and not as
  his answer:** the per-repo front-door work (two landed 2026-08-23 —
  `idea-engine` #900, `sim-lab` #360 — and `product-forge` + `estate-backups`
  are still thin), and the D2 target question `OQ-FM-D2-TARGET`, which is the
  root blocker on the whole plan.
  ~~**⬆ 2026-08-23 — you said today.**~~ The evidence half is done and waiting:
  [`findings/2026-08-23-eap-evidence-pack.md`](findings/2026-08-23-eap-evidence-pack.md)
  — the numbers measured today, each with its command, organised against the six
  net-new sections your own reflection names. Headline figures you did not have
  before: **8,000 pull requests opened all-time across 26 repositories · 19 of
  the 26 created inside the EAP fortnight (all 19 within seven days, 17 in the
  first four) · 4,535 session
  cards across 19 repositories**, and the consolidation number is finally
  *closed* rather than intended (**9 archived 2026-08-23, 0 deleted**). The
  review site was also repaired first (websites #512): **0 of 7 of its live
  pages said the program had ended**, and `/fleet/` showed *"15 live lanes"* 33
  days after the seats were terminated — it is the surface this mail points at.
  Nothing here drafts the mail; that stays yours. **WHAT:** program step E1 — the one clear
  review of the whole EAP plus the numbered wish list, written by you and sent
  from a **fresh compose**, not the existing Gmail thread. **WHERE:** method +
  sources: [`planning/2026-07-26-final-eap-email-plan.md`](planning/2026-07-26-final-eap-email-plan.md);
  evidence base:
  [`findings/2026-08-09-eap-correspondence-record.md`](findings/2026-08-09-eap-correspondence-record.md).
  **HOW:** your own evening — you declined drafts twice (*"this is something
  that deserves an evening of my full attention and I won't rush it"*,
  2026-08-01); no session drafts, sends, or restarts it. **WHY-IT-MATTERS:**
  two verbatim promises of a final review are on the record and no vendor
  agenda ever arrived, so the content is entirely yours. **UNBLOCKS:** closing
  track E; once sent, the parked capability-pack email (below, which targets
  the **old** thread) gets its superseded note per the program's E1 done-when.
  **VERIFIED-NEEDED:** owner-only by your own ruling. *(Added 2026-08-11: the
  audit found E1 in the program but absent from this queue entirely.)*

- **`OQ-FM-D2-TARGET` ✅ ANSWERED 2026-08-28 — `spider-swing`, the measured order ratified.**
  Owner, live (§ 18 of [the sitting record](findings/2026-08-28-od24-sitting-answers.md)), selecting *"Ratify the measured order —
  spider-swing first"*. **Verified before recording**, because this entry is
  where the inference-as-owner-decision failure happened once already: the
  [intent audit](findings/2026-08-23-active-repo-intent-audit.md) § 6 does put
  `spider-swing` first — its PROVISIONAL marker was discharged 2026-08-24 and
  `spider-swing` **displaced `product-forge`** at the top. Full order:
  **`spider-swing` → `product-forge` → `estate-backups` → the `websites` date
  stamp**. **Naming the target does not start the work** — OD-13's methods-first
  gate and his mapping → revised plan → execution sequencing both still govern.
  The audit's caveat survives ratification: five repos remain unrated and any one
  could displace the order. *(Original ask below.)*
- **`OQ-FM-D2-TARGET` (original body) — Which repository is D2's next target, and does
  spider-swing enter the program at all?**
  **⚠ A 2026-08-23 session marked this ANSWERED, and it was withdrawn the same
  session** (`@codex`, fm #937). He said *"there's not much we can do except for
  making sure that each repo has proper documentation and is linked and explained
  in the fleet-manager for easy discovering"* — recorded as **OD-20**. That states
  a **desired estate-wide outcome**. It does **not** select a repository, and it
  does not say D2's one-repo fresh-session test should become an all-repo sweep.
  Reading it as an answer was `REASONED` inference recorded as an owner decision —
  the one thing this queue exists to keep apart. **The question below is unchanged
  and still yours.**
  **NO SESSION IS BLOCKED WHILE THIS SITS.** The
  [active-repo intent audit](findings/2026-08-23-active-repo-intent-audit.md) § 6
  derives a grounded order from measured failures instead of a guess, and as of
  2026-08-24 every unarchived repo has been swept (five still `unrated`, so the
  order is settled among the rated) — **`spider-swing` →
  `product-forge` → `estate-backups` → the `websites` date stamp** (after
  `idea-engine` and `sim-lab` were fixed the same day). `spider-swing` was the
  one repo that had never been judged and it went straight to the top. That is
  executable now and needs no letter from you; your answer would override it.
  **WHAT:** decide what D2's next repository actually is, and whether spider-swing
  enters the program at all.
  **WHERE:** [`planning/2026-07-26-consolidation-program.md`](planning/2026-07-26-consolidation-program.md)
  `:62` (the NOW pointer), `:102` (D2's order), `:45` (§2's target picture), plus the
  three echoes at [`current-state.md`](current-state.md) `:40`, `:193`, `:534`.
  **WHY IT MATTERS:** the pointer read `D2 — shiftlife truth pass`, and you said
  live on 2026-08-10 that shiftlife is not active and that spider-swing and the
  superbot repos are the important ones. That statement is **now recorded as
  OD-15** and the NOW pointer is marked superseded (fm #840) — at the time the
  audit ran it existed nowhere in the repository, which is why every document
  agreed and all of them routed the next session to a dormant repo. What remains
  open is only the choice below. Independently of your statement: spider-swing
  is in **none** of §2's eight target rows and nowhere in D2's order, while `:86` of
  the same file records that every evening since 07-26 has gone to it — the order
  encodes 2026-07-26 activity and the repo was created 2026-07-28, so advancing the
  pointer can never reach it. **UNBLOCKS:** the next session picking real work.
  **VERIFIED-NEEDED:** owner only — a session cannot derive the target from the tree,
  which is the whole finding. Evidence:
  [`audits/2026-08-10-full-read/findings.md`](audits/2026-08-10-full-read/findings.md)
  § "Start here", item 1.

- **`OQ-ONEDRIVE-HUB` ✅ RESCOPED 2026-08-28 — no longer a sync question; no
  letter owed** (added 2026-08-26 evening, OD-22). The visibility need that
  motivated it is answered differently: you directed a **local section inside
  fleet-manager** — deeper than a repo pointer, lean, the main happenings
  included — kept by hub-local sessions, so a cloud session reads that instead
  of the hub itself
  ([`findings/2026-08-28-owner-direction.md`](findings/2026-08-28-owner-direction.md)
  §§ 2–4, 7; OD-23). What survives is unhurried hub housekeeping — whether the
  hub itself wants git versioning/backup — blocking nothing; decide it
  whenever, or never. **The residual that could re-open it (`@codex`,
  fm #954): the pages give sight, not file access** — work meant to continue
  in the cloud lands in a repo before the handoff, and if a genuine handoff
  ever depends on artifacts that live only in the hub, the a/b/c options
  below are the recorded transfer candidates. **Original ask, kept for provenance:** you called the
  OneDrive / local-disk hub *"basically a repo of its own … kinda like the
  local version of fleet-manager"* and wanted the two centralised better;
  PKT-B3 carried the trade — **(a)** hub as a private git repository (risk to
  test once: OneDrive sync × git friction) · **(b)** folder shared read-only ·
  **(c)** `journal.md` copied per sitting — with recommendation (a), now
  withdrawn as a sync path. *(The un-slugged "how does `Hub/journal.md` reach
  this repo" question in [`activity/README.md`](activity/README.md) settles
  the same way: the lean fm pages carry the account.)*

- **`OQ-FM-AGENTS-BOOT` ✅ ANSWERED 2026-08-28 — yes, estate-wide.** Owner,
  live: *"Agents.md should indeed be everywhere."* Execution is PKT-B4's ×N
  rows, still sequenced (the four audit-failure repos after their Wave C
  fixes) and **held until your GO on plan execution** (*"no execution yet"*,
  same sitting). One design question your yes reopens is parked for the
  substrate-kit **review round** (OD-24 — the sitting itself happened
  2026-08-28 and left it parked): hand-write the 19 files (PKT-B4 as
  recorded) or teach the kit to plant and maintain them
  ([`findings/2026-08-28-owner-direction.md`](findings/2026-08-28-owner-direction.md)
  §§ 5, 7). **Original ask, kept for provenance — decide whether to add a
  minimal root `AGENTS.md`:**
  **UPDATED 2026-08-26 evening: the per-repo packet exists and one word starts
  it** — [the execution packets](planning/2026-08-26-estate-execution-packets.md)
  § 5 PKT-B4 (a ~15-line pointer per repo: its own read path, the hub
  back-link, the activity + owner-comments pointers; the four audit-failure
  repos sequenced after their fixes). **UPDATED 2026-08-26 — he leaned toward yes, and the scope is estate-wide, not
  this repo.** Owner, live: *"a dedicated agents.md is still probably a good
  idea."* `MEASURED` the same day across the account: **0 of 19 non-archived
  repositories carry one.** **And the argument for it changed** — the
  justification below reads *"loaded no repository instructions"*, which he
  corrected: *"you say it boots blind, but thats not true."* `@codex` demonstrably
  reads the tree deeply without one (evidence:
  [`../findings/2026-08-26-owner-direction.md`](findings/2026-08-26-owner-direction.md) § 3).
  So the case for `AGENTS.md` is **saving the first hunt and declaring a read
  path**, never remedying blindness — and it is worth deciding once for the
  estate rather than per repo.
  **WHAT:** now that the no-boot-file D2 test is preserved, decide whether a
  native instruction file should point non-Claude surfaces at the same
  surface-neutral cold route: `README.md` → `docs/current-state.md` → the
  consolidation program. **RECOMMENDATION: ADD**, but only as a short pointer;
  do not duplicate the boot file or its rules. **WHY:** the measured ChatGPT
  Work session loaded no repository instructions and had to discover the route
  manually. A native pointer would remove that avoidable first hunt without
  changing the three-file acceptance contract. **WHERE:** repository root.
  **VERIFY:** a new no-context session reports the same purpose, live state and
  next action without being told which file to open. **NOT DONE HERE:** adding
  it during the measurement would have changed the surface being tested, and
  the owner explicitly reserved the choice.

- **`OQ-KIT-V1-21-RELEASE` ◐ HALF-ANSWERED 2026-08-28 — the CUT is timed; the ADOPTERS are not.**
  **UPDATE 2026-09-04:** a third PR now rides `main` unreleased — [kit
  #590](https://github.com/menno420/substrate-kit/pull/590) (`8a83c73`), the
  K1–K5 adoption-profile work the accepted build order puts before the
  `estate` seed. It
  does **not** unlock the cut on its own: his timing answer sequences the
  charter rewrite and the doc-surface sweep first, and neither has landed. The
  smallest action that would release it, when he wants it, is one
  `workflow_dispatch` of `release.yml` with the version input, after
  `scripts/cut_release.py --write --rebuild-dist` bumps the three version homes
  and opens the CHANGELOG section.
  Owner, live (§ 12 of [the sitting record](findings/2026-08-28-od24-sitting-answers.md)): *"Cut when the next fix batch lands"* — so
  kit #587 and #588 wait on `main` and ride out with the charter rewrite and the
  doc-surface sweep in **one** release rather than their own cut. **Still his and
  still open:** which remaining adopters take the hop (`pokemon-mod-lab`
  owner-held at v1.15.0 · `superbot-games` *"no adopter yet"* · `trading-strategy`
  archived). The question named them; his answer addressed **timing only**, and
  reading a timing answer as an adopter answer would be an inference recorded as a
  decision. *(Original ask below.)*
- **`OQ-KIT-V1-21-RELEASE` (original body) — Call the remaining v1.21.0 rollout targets, at
  your pace.** *(Rewritten 2026-08-14: this entry's original action — open the
  dedicated release session — was completed 2026-08-13: v1.21.0 cut, published,
  and adopted here plus the seven repos you named in phases 2–3; record at
  program §7. The slug stays for continuity; only the genuinely open half
  remains below.)* **WHAT:** decide when (and whether) the remaining adopters
  get the v1.21.0 hop — per the phase-3 record: `trading-strategy` (you skipped
  it pending its archive decision), `pokemon-mod-lab`, `superbot-games`, and
  any other registry row still marked stale. **WHERE:** the adopter registry in
  substrate-kit (latest regen kit #586, after the trading-strategy heartbeat
  reconcile — the parallel 2026-08-14 session's `OQ-JULY-PARKED-PRS` entry
  below) and the `upgrade-distribution` skill, one repo per run. **HOW:** name a repo in any
  session — each hop is one skill invocation on the recorded pattern.
  **VERIFY:** the registry regen after each hop shows the row current.

*(An `OQ-FORGE-CODEX-INSTALL` entry existed here for ~40 minutes on 2026-08-14
and was removed the same session, before ever reaching you: the Codex app IS
active on product-forge — its first-ever review there answered in 416 s
request→review against fm's 335 s baseline, and the session mistook never-used
for not-installed. Removed rather than kept because a queued ask you can't act on
sends you hunting for a settings change that is already true; the full
correction record is in product-forge #49's card and `review-queue.md`. One
real residue for R2: when the app graduates to a fresh `phone-controller`
repo, THAT repo will genuinely need adding to the Codex app's repository
access — the graduation session must flag it then.)*

- **`OQ-JULY-PARKED-PRS` — ✅ RESOLVED same day (owner answered live
  2026-08-14: L for both; both landed and tree-verified).**
  **sim-lab #344** squash-merged @ `f54ec219` — its required gate was
  already green; `main` is the squash, 0 open PRs there.
  **trading-strategy #160** squash-merged @ `6cf2e93` after the three
  resident capability overclaims holding its gate red were narrowed in
  place on the branch (`current-state.md:389` · `CONSTITUTION.md:166` ·
  `review-queue.md:8`), gate + pytest green by their real conclusions; the
  heartbeat `kit:` line was reconciled at source the same hour (#163 @
  `b5eba03` — landing #160 had created a fresh tree-vs-self-report DRIFT)
  and the kit registry regenerated (kit #586): the row reads v1.20.2 three
  ways, honestly stale vs v1.21.0, still owner-skipped until the archive
  decision. **VERIFIED:** 0 **parked** `claude/*` PRs account-wide
  *(corrected same hour: this line first read "count is 0" off the 09:2xZ
  sweep, wrong at write time — fm #859, a parallel owner-live session's
  in-flight records PR, was already open; in-flight-by-a-live-session is
  the state the ruling licenses, and the parked count this ask was about
  is 0)*.
  He also answered the paired adopter question: **neither superbot-games nor
  pokemon-mod-lab yet** — the v1.21.0 rollout stays owner-paced.
  *Original ask, for the record: land-or-close on the two July parks, one
  letter each, raised because they sat against the nothing-waits-in-an-open-PR
  ruling; recommendation was #344 L / #160 C-or-L (asked live 2026-08-14,
  fm #858).*

## Inherited cross-repo owner asks — status as recorded

> These entries preserve their last recorded status and instructions. They are
> not a 2026-08-10 verification of another repository or external account.
> Re-check the owning surface before acting.

- **`OQ-PLAY-ACCOUNT` — ✅ DONE (owner-confirmed 2026-08-05). Developer account created, verified and paid.**
  Kept here rather than archived because the four items below all depend on it and the
  dependency reads wrong without it. Nothing further is needed on this one.

- **`OQ-PLAY-CLOSED-TEST` — (VENUE: recruiting 12 people, then 14 days of waiting) The requirement that actually sets the launch date (2026-08-05).**
  WHAT: because your account will be a **personal** account created after 2023-11-13,
  Google requires a **closed test with at least 12 testers opted in continuously for
  14 days** before you may even *apply* for production access. The application is then
  reviewed in **about 7 days**. That is a **three-week floor**, and having the game
  finished does not shorten it.
  THE TRAP: the 14 days must be **consecutive**. A tester who opts out and back in
  resets — time does not accumulate. All 12 must still be opted in at the moment you
  apply. Recruit **more than 12** so one person leaving does not restart the clock.
  WHERE: Play Console → Testing → Closed testing; testers join by Google account email
  or a Google Group.
  HOW: 12 real Google accounts — friends, family, a Discord, anyone with an Android
  device. They must accept the invite; they do not have to play.
  WHY IT IS YOURS: recruiting people and managing the tester list. Everything technical
  for this is already built — the debug APK path exists today and the bundle path
  landed in PR #162.
  **CORRECTED 2026-08-05 (second pass):** two things this entry originally got wrong.
  (1) **Internal testing does NOT count** — verified verbatim: *"You must run a closed
  test before you can apply to publish your app to production."* Internal testing is
  faster and reviewless but buys zero progress on the clock; use it only to check the
  bundle installs. (2) **The store listing blocks this.** A release cannot roll out to a
  closed track until the store listing, App content page and pricing are all complete,
  so `OQ-PLAY-LISTING` is now **on the critical path, ahead of this**, not after it.
  ALSO: the number is **12**, not 20. A separate model answer confidently said 20 while
  claiming to quote the page — 20 was the old requirement. See
  [`findings/2026-08-05-gemini-url-accuracy-benchmark.md`](findings/2026-08-05-gemini-url-accuracy-benchmark.md).
  SOURCE: [answer/14151465](https://support.google.com/googleplay/android-developer/answer/14151465)
  and [answer/9859348](https://support.google.com/googleplay/android-developer/answer/9859348),
  both fetched 2026-08-05.
  **RECRUITING ROUTE, verified 2026-08-05 (third pass):** you do **not** have to
  collect email addresses. Closed testing accepts a **Google Group**, and a Google
  Group can be set so *"Anyone can join"* — a person adds themselves from the open
  web with no invitation and no approval from you. Point that group at the closed
  track and the flow becomes: share one link → they join → they install. Internal
  testing cannot do this (it takes email lists only), which is why the track you
  published to today still needs addresses typed in by hand.
  **AND OPEN TESTING IS NOT AN ALTERNATIVE:** *"Open testing is available when you
  have production access"* — production access is what the closed test unlocks, so
  the open track cannot come first. The Google Group route is the **only** way to
  get a self-serve link before production.
  SOURCE: [answer/9845334](https://support.google.com/googleplay/android-developer/answer/9845334)
  and [groups/answer/2464926](https://support.google.com/groups/answer/2464926),
  both fetched 2026-08-05.

- **`OQ-PLAY-APP-ID` — ✅ RESOLVED 2026-08-05 (recorded here 2026-08-21, fleet
  review fm #878 — this entry sat open for 16 days after you completed it).**
  The ID is **`com.menno420.slingyspider`** — chosen, set, and burned in: a
  signed AAB (version code 64) built by `android-release.yml` was published by
  you under that ID on Play's **internal testing** track on 2026-08-05
  (spider-swing `docs/current-state.md` § "What measurement has settled").
  Internal testing needs no listing and buys **zero** progress on the
  12-tester clock — the open Play asks are now `OQ-PLAY-LISTING` (critical
  path) and `OQ-PLAY-PRIVACY-POLICY`, then the closed test. *(Original body —
  ID rules, Console form notes — removed per amended OD-3: the decision it
  guided is made and irreversible; sources remain in
  [`findings/2026-08-05-google-play-submission-requirements.md`](findings/2026-08-05-google-play-submission-requirements.md).)*

- **`OQ-PLAY-UPLOAD-KEY` — ✅ RESOLVED 2026-08-05 (recorded here 2026-08-21,
  fleet review fm #878).** The upload keystore exists and works: the vc64
  bundle that reached the internal track was **signed** by
  `android-release.yml`, and that workflow signs only when the keystore
  secrets exist (without them it builds an UNSIGNED bundle and says so) —
  so the secrets are set (same ledger evidence as `OQ-PLAY-APP-ID`; the
  refuse-to-run gate is on the `RELEASE_PACKAGE_ID`/`RELEASE_APP_NAME`
  variables, also satisfied).
  Still yours, standing: keep the keystore backed up somewhere that is not
  the repository (loss is recoverable via Play app signing reset, but the
  reset costs days). *(Original how-to body removed per amended OD-3 — the
  key exists; keytool instructions for a key that exists are noise.)*

- **`OQ-PLAY-PRIVACY-POLICY` — (VENUE: 20 minutes) Publish a privacy policy URL — required even though the game collects nothing (2026-08-05).**
  WHAT: Play requires a **live, public privacy policy URL for every app**, and the
  "we collect nothing" case is **not** an exemption. Verbatim from Google: *"Even
  developers with apps that do not collect any user data must complete this form and
  provide a link to their privacy policy."* You must also complete the **Data safety
  form** — for this game the honest answer to every question is "no data collected"
  — and the **content rating (IARC) questionnaire** and **target audience
  declaration**, both mandatory.
  WHERE: any public URL. GitHub Pages on a repository you own is free and sufficient.
  HOW: a short honest page — the game stores progress only on the device, sends
  nothing anywhere, has no accounts, no ads, and no analytics. Say that plainly and
  give a contact email.
  WHY IT IS YOURS: it is a legal statement published under your name, and it needs
  hosting you control. A session can draft the text if you want — ask.
  SOURCE: [answer/10787469](https://support.google.com/googleplay/android-developer/answer/10787469)
  and [answer/9859655](https://support.google.com/googleplay/android-developer/answer/9859655),
  fetched 2026-08-05.

- **`OQ-PLAY-LISTING` — ⬆ PROMOTED TO CRITICAL PATH (VENUE: an hour, mostly capture) Store listing text and images (2026-08-05).**
  **Re-ordered 2026-08-05:** this was filed as a late item and that was wrong. A release
  cannot roll out to a **closed** testing track until the store listing, App content page
  and pricing are complete — so the icon, feature graphic and screenshots block the
  12-tester clock rather than following it. Do this before recruiting testers, not after.
  **Copy is drafted for you** — app name, three short-description options and a full
  description, all measured against the real limits, in spider-swing
  `docs/product/play-store-listing.md`. What remains genuinely yours is the images:
  screenshots must be **real capture** on a device (the `android-debug` workflow already
  builds an installable APK on every push to `main`), because generated imagery invents
  interface and physics.
  WHAT: the listing needs, with exact limits verified 2026-08-05 — app name **30
  characters**, short description **80**, full description **4,000**; app icon
  **512×512** 32-bit PNG **with** alpha, ≤1024 KB; feature graphic **1024×500** JPEG or
  24-bit PNG **without** alpha; **at least 2** screenshots to publish, at most 8 per
  device type.
  THE GAME-SPECIFIC ONE: to be eligible for Play's recommendation surfaces a game needs
  **at least three 16:9 landscape screenshots at 1920×1080 or larger**. Spider Swing is
  natively 16:9 landscape, so these are straight captures at a larger window — no
  redesign, no cropping.
  HARD RULE: screenshots must be **real capture**. Generated imagery invents UI and
  physics — one generated clip in this estate put three ATTACH buttons in a single
  frame. Generated art is fine for the feature graphic; never for anything implying
  "this is how it plays".
  WHY IT IS YOURS: the copy is product voice and the screenshots need runs worth
  showing. A session can produce the captures and draft the copy once you confirm the
  name — ask, and say which moments you want on screen.
  SOURCE: [answer/9866151](https://support.google.com/googleplay/android-developer/answer/9866151)
  and [answer/9859152](https://support.google.com/googleplay/android-developer/answer/9859152),
  fetched 2026-08-05.

- **`OQ-SWINGY-NAME` — ✅ RESOLVED 2026-08-05. The name is **Slingy Spider**.**
  "Swingy Spider" was checked and is **taken** by two same-genre products (itch.io by
  Garrett Goodwin; Amazon Appstore by Tim Mendez) — ruled out. "Slingy Spider" is free
  on Google Play by exact-phrase search, was generated unprompted by a friend watching
  gameplay on 2026-07-30, and endorsed by a second on 2026-08-03. Full evidence and the
  three retracted objections: spider-swing `docs/product/name-status.md`.
  **STILL OPEN — trademark only:** BOIP (Benelux, your home registry) and EUIPO, Nice
  Class 9 (software) and Class 41 (entertainment). Unrelated to store availability.
  Superseded original ask below, kept for the record:
  **(VENUE: ten minutes, your accounts) Confirm "Swingy Spider" is available before it hardens (2026-08-05).**
  WHAT: the working name **Spider Swing** is already taken, and you named
  **"Swingy Spider"** as the likely publishing name. Nothing is committed to it yet
  beyond a trailer title card, which is the cheapest possible moment to change course.
  WHERE: Google Play console search, the Apple App Store, and a domain registrar.
  HOW: search both stores for the exact phrase and near-misses; check
  `swingyspider.com` and `.app`. If it survives all three, say so and it lands in
  `docs/decisions.md` as a decision rather than staying a chat aside.
  WHY IT IS YOURS: it is a naming and branding call, and the store searches need
  your accounts. The repo name `spider-swing` can stay either way — internal and
  store names diverging is normal.
  UNBLOCKS: store listing prep, cover art lettering, and any marketing artefact
  that carries the name.

- **`OQ-GEMINI-TIER` — (VENUE: one evening, your account) Run the one-clip test before paying for a Gemini tier (2026-08-03).**
  WHAT: the research is done and the recommendation is conditional, so the decision needs one
  cheap experiment first. On the free tier, with the visual-QA Gem in place, send **one clip
  per message** for a handful of clips and check whether distance, region and run attribution
  all come back attached to the right clip. If they do, the batch failure was a context
  ceiling that the protocol already fixes and there is nothing to buy. If single clips still
  drift, the ceiling is real and **AI Plus at $4.99/mo** (32k → 128k context) is the smallest
  purchase that changes capability rather than quota.
  WHERE: the Gemini app, your own account.
  HOW: build the Gem from [`research/2026-08-03-gemini-visual-qa-gem.md`](research/2026-08-03-gemini-visual-qa-gem.md)
  (three paste blocks), then run its four-point acceptance test — the fourth point, asking a
  repository-history question mid-review, is the one that catches the expensive failure.
  VERIFY: read your own plan page for the real prices; Google-owned pages and press coverage
  disagreed on AI Pro's storage and AI Plus's price when this was written.
  WHY IT IS YOURS: it is a spending decision and it needs your device and account. Full
  reasoning + sources: [`research/2026-08-03-gemini-paid-tiers.md`](research/2026-08-03-gemini-paid-tiers.md).

- **`OQ-SHIFTLIFE-CI` — (VENUE: 2-min click) DE-ESCALATED: CI came back by itself; the click is now prevention, not repair (2026-07-25).**
  WHAT: shiftlife CI failed with `startup_failure` on every fresh run through the middle of
  2026-07-25 — best evidence was exhausted private-repo Actions minutes (the billing meter is
  unreadable with the fleet PAT, 403). **It recovered on its own around 13:55Z** and has stayed
  healthy since: PR #15 and PR #16 both ran `quality` + `substrate-gate` to green and merged
  under the normal gate. The interim local-gate protocol is RETIRED. Why it recovered is not
  observable from here (your click, quota replenishment, or a platform incident passing) — so
  this is recorded neutrally rather than claimed as fixed.
  WHERE: github.com, ingelogd als menno420.
  HOW (optioneel, voorkomt herhaling): Settings (account) → **Billing and plans** → *Plans and
  usage* → tab **Actions**: zet onder **Spending limits** een klein Actions-budget (bijv.
  **$10/maand**). Zonder limiet kan hetzelfde opnieuw gebeuren, en dan staat de bouw weer stil.
  ALTERNATIEF: maak `menno420/shiftlife` publiek (repo → Settings → General → Danger zone →
  Change visibility) — Actions is dan gratis/ongemeterd; het plan zei "privé tot launch", dus
  dit is jouw afweging (er staan geen geheimen in de repo; tokens leven op Railway).
  VERIFY: niets te doen — de seat bewaakt het vanzelf en meldt het als CI opnieuw wegvalt.
  RISK: ✅ klein bedrag met harde limiet, elk moment aanpasbaar. Niets doen mag ook.
- **`OQ-SHIFTLIFE-PRO-DRIFT` — (VENUE: 1-min decision, geen haast) Een Pro-functie is per ongeluk gratis geworden — jouw plan, jouw keuze wat er nu in het plan staat (2026-07-26).**
  WHAT: bij een controle van het product tegen het goedgekeurde plan bleek dat **verlof-advies**
  ("vraag deze 4 dagen aan → 12 dagen samen vrij") gratis is uitgeleverd, terwijl het plan die
  vraag onder **Pro** zet (§3, Pro-punt 4 *Deep statistics*: "als ik de 3e t/m 10e vrij neem,
  welke overlap-weekenden blijven over?"). Tegen het charter is het een **test-3** functie
  (gemak/inzicht), geen test-1 (de kernvraag "wanneer werk ik, en wanneer zijn we samen vrij?"
  werd al beantwoord zonder deze functie) — dus het had achter Pro **mogen** staan.
  **Het gevolg is onomkeerbaar in de code:** charter-regel 4 (geen regressie) zegt dat een
  functie die gratis is uitgeleverd nooit meer achter de betaalmuur mag. De functie blijft dus
  gratis. Dat is een prima uitkomst — het is een sterk verhaal richting gebruikers — maar het
  was **mijn beslissing en niet de jouwe**, en het is er één over geld. Dat hoor je te weten.
  WHERE/HOW: niets technisch te doen. Alleen: wil je dat het plan wordt bijgewerkt zodat
  verlof-advies officieel bij de gratis kern hoort (aanbevolen — dan klopt het document weer),
  of wil je dat het als afwijking gemarkeerd blijft staan? Eén zin in de hub-chat is genoeg.
  WHY: het plan zegt dat elke wijziging die monetisatie raakt moet benoemen welke charter-test
  hij doorstaat. Dat is bij die PR niet gebeurd. Het proces is hersteld (het staat nu vast in
  `docs/current-state.md` van shiftlife); dit item bestaat zodat jij de laatste stem hebt.
  RISK: ✅ geen. Niets doen betekent: verlof-advies blijft gratis, plan blijft afwijken.
- **`OQ-SHIFTLIFE-PHASE0` — two owner asks: beta names (real-world) + Expo account (5 min) — sync is DONE, the product is beta-ready pending on-phone QA (2026-07-25).**
  WHAT: ShiftLife state — working app (onboarding in 30s, day editor, Samen tab, partner
  management, local persistence), calendar export, live Postgres-backed share server at
  `https://shiftlife-api-production.up.railway.app`, AND the **multi-device sync plan complete
  (5/5 slices)**: partner invites work — live-proven with a two-device simulation against
  production (A publishes → invite → B joins and edits → A sees B's edit; single-use codes;
  "Vernieuw beveiliging" lock-change for a lost phone). Every shiftlife PR merged
  green, each slice verified live before merge — phase-1 polish since then added a custom
  rooster-builder, verlof/ziek incl. multi-day ranges, the 🌴 "samen vrije periodes" badge and
  a friendly state for when a live link is revoked. The free core now scores **7 of 8 items
  done, 1 half** against the plan — tracked per-item, with the module and test behind each
  row, in shiftlife `docs/plan-conformance.md`. (Deliberately no PR count here: it goes stale
  within a day, and the per-item scorecard is the number that actually means something.) That
  checklist found and fixed a real gap on the day it was written — plan item 1 asks for
  **cursusdagen** and no screen could create one, though the engine had handled them for
  months — and the follow-ups found the same shape twice more, in code that hand-copied a list
  of values instead of deriving it. The ONLY
  thing between this and a real beta is a human tap-through. Two asks remain owner-only —
  and **(b) is no longer only QA: it is now the single thing blocking a named plan item**,
  since reminders (item 6) is the last free-core gap and a notification cannot be proven
  without a phone:
  **(a) D4 beta families** — 5–10 binnenvaart households where at least one person works a
  rotation (7/7, 14/14, 21/21 or irregular); a WhatsApp "yes" is enough; drop names in hub
  chat whenever.
  **(b) Expo account for on-phone QA** — the app is demo-able on your own phone: (1) install
  the "Expo Go" app (App Store / Play Store), (2) create a free account at expo.dev, (3)
  expo.dev → Account settings → Access tokens → create a token (name it e.g. `fleet`) and
  paste it in hub chat — the seat then publishes the app and sends you a QR to scan; you can
  revoke the token right after, any time.
  WHERE: (a) your own network; (b) phone + expo.dev, ~5 minutes.
  WHY: (a) real households are the phase-1 exit criterion (plan §7); (b) every screen so far
  is container-verified (tests + bundles) — the first human tap-through is the QA the fleet
  cannot do itself, and it is also simply the fun moment: your app, on your phone.
  UNBLOCKS: (a) phase-1 exit; (b) on-phone QA + the beta build path + **the last free-core
  item**: `expo-notifications`, the permission flow, and a notification actually firing —
  the decision layer for reminders is built and 15 tests green, so the token is the only
  remaining piece (D5 store accounts stay later, phase-2/3).
  VERIFY: (a) names in hub chat → mirrored into shiftlife `docs/current-state.md`; (b) QR
  sent in hub chat + first tap-through feedback recorded.
  RISK: ✅ none — informal asks; the Expo token is revocable one click after use.
  Provenance: plan fm PR #486 → GO 2026-07-24 → birth `d18aa30` → D-design (shiftlife#1) →
  app shell (#2) → data entry (#3) → ICS export (#4) → api (#5) → deploy (#6) → wiring (#7)
  → consolidation + sync design (#8).
- **`OQ-SBW-DUP-FAILSAFE` — (VENUE: hub) delete one of the two enabled "SuperBot World failsafe wake" crons.**
  WHAT: two enabled crons with identical name + schedule (`15 1-23/2 * * *`) are waking two parallel
  SuperBot World seats every 2h — `trig_01XJJ88pQaQFRSpVAviCfAZe` (created 2026-07-17T22:11Z) and
  `trig_01DbcKVWxn6RJPhfyRkgTg6m` (created 2026-07-18T17:08Z); both fired ~05:15Z (~3s apart), both
  next 07:15Z, confirmed at two consecutive snapshot captures (00:06:22Z + 06:15:10Z — the 00:06Z
  watch item's escalation tripwire fired). **Recommendation: delete
  `trig_01XJJ88pQaQFRSpVAviCfAZe` (the older, 07-17-created one; the 07-18 one is the current
  seat's cutover-armed failsafe)** — one letter answers this (Y = delete the recommended id).
  WHERE: hub chat trigger tools (`list_triggers` → *silence the duplicate*).
  HOW *(rewritten 2026-08-11 under `[D‑0015]` — a **session** must never call `delete_trigger`;
  the hook denies it, and the recorded steps here predated that rule)*: paste-ready —
  (1) `list_triggers` and verify BOTH ids exist enabled; (2) a session runs
  `update_trigger trig_01XJJ88pQaQFRSpVAviCfAZe enabled:false` (the D‑0015 stop — no prompt,
  reversible), OR you delete that id yourself from the console; (3) `list_triggers` again and
  confirm exactly one **enabled** "SuperBot World failsafe wake" remains.
  WHY: both fire every 2h (~2–3s apart), waking two parallel SBW sessions — double token burn plus
  a two-writer collision risk on the SBW seat's repos/state.
  UNBLOCKS: clean single SBW wake chain.
  VERIFY: the next fm triggers snapshot shows exactly one enabled "SuperBot World failsafe wake"
  (I8 WARN clears in `check_trigger_health.py`).
  RISK: ✅ reversible (re-create from the SBW startup prompt). Honest note: fm doctrine forbids
  this seat deleting a sibling lane's trigger id from its own venue — hence the hub routing.
  Provenance: fm records slice 2026-07-19 (PR #347), escalation record in `docs/fleet-triage.md`.
  *Status 2026-07-19T08:38Z (fm PR #351): unchanged — still open, unaffected by the morning
  nothing-stuck executions (label/merge sweep touched PRs, not triggers).*
  *Status 2026-07-19T18:0xZ (18Z records slice) — **THIRD escalation cycle**: both ids STILL
  enabled in the 2026-07-19T17:57:56Z capture; observed double-fires today
  09:15Z / 13:15Z / 15:15Z / 17:15Z (~seconds apart each window), next double-fire 19:15Z.
  The hub delete has now survived three capture cycles unexecuted. Related live signal:
  `check_lane_liveness.py` (18:05Z) verdicts all three SBW-seat constituent lanes STALLED
  (superbot-games Seat A ~9h15m · superbot-idle ~10h39m · superbot-mineverse ~10h39m) —
  the duplicate wakes are burning double tokens while the lane itself lands nothing.*
  *Status 2026-07-19T21:4xZ (22Z records slice, PR #381) — **FOURTH escalation cycle**: both ids
  STILL enabled in the 2026-07-19T21:34:18Z capture; the predicted 19:15Z double-fire happened,
  and so did 21:15Z (in-snapshot last_fired 21:15:27Z / 21:15:30Z, ~2.4s apart); next double-fire
  23:15Z. Recommendation update (I8 remedy flip, 2026-07-19 SBW lesson): keep-oldest is NOT the
  rule — verify each id's bound session against the SBW seat's live heartbeat and keep the one
  bound to the CURRENT session (likely the newest, `trig_01DbcKVWxn6RJPhfyRkgTg6m`, i.e. delete
  `trig_01XJJ88pQaQFRSpVAviCfAZe` — unchanged from the standing recommendation, now
  heartbeat-verified rather than age-based). Liveness delta: games Seat A + mineverse recovered
  to LIVE by 21:40Z; superbot-idle (Seat B) is the sole STALLED lane, WAKING-IDLE 7 fires since
  its last landed output (07:26Z) — the double burn now concentrates on a lane landing nothing.*
  *Status 2026-07-20T01:2xZ (01Z records slice, PR #385) — **FIFTH escalation cycle**: both ids
  STILL enabled in the 2026-07-20T01:10:16Z capture; the predicted 23:15Z double-fire happened
  (in-snapshot last_fired 23:15:27Z / 23:15:29Z, ~1.9s apart); both next 01:15Z — already due at
  capture+5min, so the 01:15Z window double-fired past the capture edge. Recommendation
  unchanged (heartbeat decides the keeper; likely keep the newest,
  `trig_01DbcKVWxn6RJPhfyRkgTg6m`, i.e. delete `trig_01XJJ88pQaQFRSpVAviCfAZe`). Liveness
  context: superbot-idle (Seat B) still the sole STALLED lane, WAKING-IDLE now 8 fires since its
  last landed output (07-19T07:26Z, ~17h51m) — the double burn continues on a lane landing
  nothing overnight.*
  *Status 2026-07-20T04:1xZ (05Z records slice, PR #387) — **SIXTH escalation cycle**: both ids
  STILL enabled in the 2026-07-20T04:02:52Z capture; the predicted 03:15Z double-fire happened
  (in-snapshot last_fired 03:15:16.9Z / 03:15:20.8Z, ~3.9s apart); both next 05:15Z. **Keeper
  recommendation strengthened by in-export heartbeat evidence:** the newest id
  (`trig_01DbcKVWxn6RJPhfyRkgTg6m`) binds `session_0148fC4UXupaNEDPeYjBR3fX`, which also holds
  a pending 05:23Z self-continuation one-shot — a live seat; the older id's session shows no
  such signal. Unchanged ask: delete `trig_01XJJ88pQaQFRSpVAviCfAZe`. Liveness context:
  superbot-idle (Seat B) still the sole STALLED lane, WAKING-IDLE now 10 fires since its last
  landed output (07-19T07:26Z, ~20h43m).*
  *Status 2026-07-20T09:1xZ (morning records slice, PR #393) — **SEVENTH escalation cycle**: both
  ids STILL enabled in the 2026-07-20T07:20:20Z capture; the predicted 07:15Z double-fire happened
  (in-snapshot last_fired 07:15:31.4Z / 07:15:34.8Z, ~3.4s apart); both next 09:15Z. **Context
  change: the SBW lanes have all recovered WITHOUT this delete** — superbot-idle's stall broke
  04:20:38Z (idle PR #174, verdict STALLED→LIVE at the 09:09Z liveness run), superbot-games landed
  inventory-bridge #180–182, mineverse heartbeats current. The delete is therefore now a **pure
  burn-stop** (two wakes per 2h window, ~double token burn), no longer blocking any lane recovery
  — smaller urgency, same one-letter ask. Recommendation unchanged: delete the older
  `trig_01XJJ88pQaQFRSpVAviCfAZe`, keep `trig_01DbcKVWxn6RJPhfyRkgTg6m` (heartbeat-verified live
  seat binding).*
  *Status 2026-07-20T11:5xZ (11:30Z records slice, PR #395) — **EIGHTH escalation cycle**: both
  ids STILL enabled in the 2026-07-20T11:37:48Z capture; the predicted 11:15Z double-fire
  happened (in-snapshot last_fired 11:15:40.6Z / 11:15:46.9Z, ~6.3s apart); both next 13:15Z.
  Still a pure burn-stop; recommendation unchanged: delete the older
  `trig_01XJJ88pQaQFRSpVAviCfAZe`, keep `trig_01DbcKVWxn6RJPhfyRkgTg6m`.*
  *Status 2026-07-20T15:5xZ (15:30Z records slice, PR #399) — **NINTH escalation cycle**: both
  ids STILL enabled in the 2026-07-20T15:38:36Z capture; the predicted 15:15Z double-fire
  happened (in-snapshot last_fired 15:15:38.5Z / 15:15:44.3Z, ~5.7s apart); both next 17:15Z.
  Still a pure burn-stop; recommendation unchanged: delete the older
  `trig_01XJJ88pQaQFRSpVAviCfAZe`, keep `trig_01DbcKVWxn6RJPhfyRkgTg6m`. Related new signal:
  the pair's second seat lane, superbot-idle (Seat B), went QUIET→STALLED at this cycle's
  liveness run (07:37Z last commit, 4 fires since) — the double-wake is no longer provably
  harmless to that lane.*
  *Status 2026-07-21T03:1xZ (00:42Z night records slice, PR #410) — **TENTH escalation cycle**:
  both ids STILL enabled in the 2026-07-21T00:42:48Z capture; the predicted 23:15Z double-fire
  happened (in-snapshot last_fired 23:15:15.5Z / 23:15:19.7Z, ~4.2s apart); both next 01:15Z —
  by this ~03:1xZ write the 01:15Z window has cadence-inferred fired too, and 03:15Z is
  imminent (cycles continue every odd-hour :15). Still a pure burn-stop; recommendation
  unchanged: delete the older `trig_01XJJ88pQaQFRSpVAviCfAZe`, keep
  `trig_01DbcKVWxn6RJPhfyRkgTg6m`. Liveness context: superbot-idle (Seat B) still STALLED
  (last landed output 07-20T07:37Z, 8 fires since at the 03:14Z run).*
  *Status 2026-07-21T08:3xZ (08:18Z morning records slice) — **ELEVENTH escalation cycle**:
  both ids STILL enabled in the 2026-07-21T08:18:22Z capture; the predicted 07:15Z
  double-fire happened (confirmed in-export); next 09:15Z (cycles continue every odd-hour
  :15). Still a pure burn-stop; recommendation unchanged: delete the older
  `trig_01XJJ88pQaQFRSpVAviCfAZe`, keep `trig_01DbcKVWxn6RJPhfyRkgTg6m`. Liveness context:
  superbot-idle (Seat B) still STALLED (last landed output 07-20T07:37Z, 12 fires since at
  the 08:28Z run); superbot-games Seat A joined it QUIET→STALLED this cycle.*
  *Status 2026-07-21T16:1xZ (16Z records slice) — **TWELFTH escalation cycle** (the 12:21Z
  cycle's record was lost with PR #419, closed unmerged — gate red, see triage): both ids
  STILL enabled in the 2026-07-21T16:00:18Z capture; both next 17:15Z confirmed in-export;
  the 15:15Z window double-fired per the coordinator's live observation (this export's
  record shape carries no last_fired for the pair, so the in-snapshot ~seconds-apart proof
  of prior cycles isn't available — cadence + both-enabled + shared 17:15Z next make the
  double-fire the only consistent reading). Still a pure burn-stop; recommendation
  unchanged: delete the older `trig_01XJJ88pQaQFRSpVAviCfAZe`, keep
  `trig_01DbcKVWxn6RJPhfyRkgTg6m`. Liveness context (16:10Z run): superbot-idle (Seat B)
  still STALLED (16 fires since its 07-20T07:37Z last output); superbot-next +
  superbot-mineverse joined STALLED this cycle; venture-lab recovered STALLED→LIVE.*
  *Program-close note (2026-07-21 seat close): **likely MOOT after 2026-07-22** — the
  SBW seat's own final-closer wipes both ids at its close. New check that replaces the
  old one-letter ask: after 2026-07-22, `list_triggers` to exhaustion; if either id
  survives, delete it (post-close, ANY surviving trigger is dead weight — the
  keep-the-newer nuance no longer applies). Folded into the post-close trigger sweep,
  [PROJECT-CLOSEOUT.md](PROJECT-CLOSEOUT.md) §4 checklist item 1.*

- **`OQ-KIT-WAVE-REMNANTS` — (VENUE: hub) land the 4 remaining kit-wave v1.17.0→v1.20.1
  upgrade legs (3/7 merged overnight).**
  WHAT: the 20:1xZ Q-0264 nudges converted 3 of 7 legs to MERGED overnight (idea-engine
  #740 20:18Z · superbot-games #183 22:24Z · superbot-mineverse #138 20:33Z). Remnants,
  each with its prepared next step:
  (1) **trading-strategy #160** — hub-side fixes COMPLETE in the local working tree
  (`/home/user/trading-strategy`, gate passes); the commit/push step got per-call platform
  denials in two venues on 2026-07-21 (transient venue state per doctrine, not a wall);
  the **push-prepared-tree step is paste-ready for the hub chat** (commit the prepared
  tree, push to the PR branch).
  *Status 2026-08-14: the DISPOSITION question (land vs close under the
  nothing-waits-in-an-open-PR ruling) now lives at `OQ-JULY-PARKED-PRS` above — the
  resume recipe below stays valid only if the answer is L.*
  (2) **venture-lab #282** — per-call platform denials in three venues on 2026-07-21
  (fleet memory record; transient venue state per doctrine, not a wall); hub-side
  re-attempt.
  (3) **websites #452** — lane fix commit landed (`c67057f`, ORDER 039) but the PR is
  conflicted with no CI on head; needs a **rebase**.
  (4) **superbot-next #602** — set **lane-owned** (seat scored LIVE again at 07:18Z this
  cycle; leave to the lane, no hub action unless it re-stalls).
  WHERE: hub chat (items 1–3); none for item 4.
  CONTEXT, honest: the coordinator **stood down on the cross-repo fix/merge class
  ~07:2x–07:4xZ after owner intervention** — these steps are prepared-and-parked, not
  in-flight; they execute only on owner word (see the stand-down record in
  `docs/fleet-triage.md` § 2026-07-21 08:18Z).
  VERIFY: all 7 kit-wave PRs terminal (merged/closed); sibling repos report kit 1.20.1.
  RISK: ✅ reversible (PR-lane work). Provenance: 08:18Z morning records slice.
  *Status 2026-07-21T16:1xZ (16Z records slice) — **KIT-WAVE NOW 5/7 MERGED; remnants
  #160 + #602 only.** Live-GH-verified midday facts (originally recorded by the 12:21Z
  cycle whose PR #419 closed unmerged): **websites #452 MERGED 06:57:59Z** (`b2f5013`) —
  the rebase item is DONE, drop it; **venture-lab #282 MERGED 12:51:30Z** (head `a73c4f0`,
  hub fix worker landed it) — the classifier-wall escalation is MOOT, drop it (the
  substrate-kit heartbeat candidate block ages out at its next update; allowlisted in
  `.substrate/check-exceptions.yml` meanwhile). Also: **substrate-kit v1.20.2 released
  09:44:49Z**, and both surviving remnants were re-vendored to v1.20.2:
  (1) **trading-strategy #160** re-vendored (head `f1c5284`); red = 3 resident doc lines
  (`current-state.md:389`, `CONSTITUTION.md:166`, `review-queue.md:8`). Honest caveat: the
  hub-prepared local fixes at `/home/user/trading-strategy` are **stale vs the re-vendored
  branch** — the 3 target lines are unchanged, so the prepared steps stay valid **after a
  rebase** of that working tree onto `f1c5284`.
  (2) **superbot-next #602** re-vendored (head `2755fdb`); 4 reds narrowed to 2 resident
  lines (`current-state.md:101` + `:118`); stays lane-owned.*
  *Program-close note (2026-07-21 seat close, both PRs re-verified live OPEN/blocked at
  ~17:07Z): the "lane-owned" routing for #602 is void — no lane seats remain. Both
  remnants are now plain fresh-session work: clone → check out
  `claude/kit-upgrade-v1.20.1` → fix/allowlist the named resident lines (3 in
  trading-strategy · 2 in superbot-next) → push → merge on green. The
  `/home/user/trading-strategy` prepared tree was container-local and is gone; the fix
  content re-derives in minutes from the line list. Full resume recipes:
  [PROJECT-CLOSEOUT.md](PROJECT-CLOSEOUT.md) §3 items 1–2.*

- **`OQ-WEBSITES-LABEL-MACHINERY` — (VENUE: owner-live) remove the websites
  `host-automerge-extras.yml` label re-creation machinery (residual of the resolved
  `OQ-LABEL-DEFS-DELETE`).**
  WHAT: the 9 `do-not-automerge` label DEFINITIONS are verified deleted fleet-wide
  (see the 18Z Resolved entry below), but websites `host-automerge-extras.yml` on main
  (from websites PR #324; create call verified via raw read 2026-07-19T16:16Z, ~line 79)
  still **auto-re-creates + auto-applies** the label on workflow-touching `claude/*`
  PRs — so in websites the label WILL re-appear until the workflow's carve-out behavior
  is removed.
  WHERE/WHY owner venue (dated basis, 2026-07-19): a manager-relayed removal dispatch
  was classifier-gated **twice on 2026-07-19** by the platform auto-mode
  guardrail-removal provenance check (denials recorded in `docs/fleet-triage.md`
  § "R30 landed" — transient venue state per doctrine, not a wall) — so the edit
  currently rides the owner's live venue: a dispatch made with the owner
  present/confirming, or the owner's own session.
  HOW it lands once open: under playbook **R30** (fm PR #367;
  `docs/workflow-pr-merge-policy.md`) the resulting workflow-diff PR is
  **agent-merged** after the 3-point head-SHA check (`scripts/r30_merge_check.py`,
  fm PR #372) — no owner merge click needed; only the dispatch provenance is the
  owner's.
  VERIFY: a workflow-touching websites `claude/*` PR no longer gets the label
  auto-applied; standing tripwire `python3 scripts/check_label_hygiene.py`
  (re-appearance of the definition = the machinery fired again).
  RISK: ✅ reversible (workflow edit in a PR). Provenance: owner nothing-stuck
  directive ~2026-07-19T08:00Z; re-scoped out of `OQ-LABEL-DEFS-DELETE` by the 18Z
  records slice.
  *Program-close note (2026-07-21 seat close): unchanged and still open — run the
  removal from a fresh session with the owner present (the dispatch just needs the
  owner-live venue); the PR lands normally once open. [PROJECT-CLOSEOUT.md](PROJECT-CLOSEOUT.md) §3 item 4.*

### (A) GitHub merges — one click each
**EMPTY** — 0 open PRs in fleet-manager needing a click, and the last cross-repo workflow
carve-out (product-forge #29) was **merged by the hub 2026-07-19T07:41:57Z** under the owner's
nothing-stuck directive (`OQ-FORGE-29-WORKFLOW-MERGE` → Resolved below).
*Standing note (R30, 2026-07-19):* the workflow-diff carve-out class **no longer routes
here at all** — playbook R30 (fm PR #367, `docs/workflow-pr-merge-policy.md`) makes
workflow-touching PRs agent-merged after the policy's 3-point head-SHA check (Codex-clean
at head · all checks green · whole-file secret+egress scan); only a policy **STOP**
(e.g. a patch-less/oversized diff) routes a workflow PR to this queue. Any remaining
fleet-wide merges/ready-flips live in
[owner-actions-2026-07-17.md](owner-actions-2026-07-17.md), not here. fm
[#344](https://github.com/menno420/fleet-manager/pull/344) **MERGED 2026-07-19T09:22:03Z**
(owner resolved its conflict; `OQ-FM-ROSTER-CRON-RELIABILITY` → Resolved below).

### (B) Secrets & GitHub settings (owner-only walls)

- **`OQ-FM-ROSTER-READ-PAT` — `ROSTER_READ_TOKEN` secret. ☠ MOOT 2026-08-07 — do not create.**
  The ask was **conditional on retaining roster autogen**, and the sizing ruling went the other
  way: *"Yes retire the roster"* (`OQ-FM-APPARATUS-SIZING`, ✅ RESOLVED below — its close-out
  names this slug mooted). Both roster-regen cron lines are removed, so nothing would ever read
  the secret. *(Until 2026-08-11 this entry still read "currently under the sizing review; see
  NEXT-TASKS.md" — a review resolved 66 lines below in this same file, and a pointer at a doc
  this file's own §Context forbids using as a live list.)* Original ask preserved: a
  fine-grained READ-ONLY PAT (pokemon-mod-lab only, Contents:read) as a fleet-manager Actions
  secret, so the private lane's roster row could read honestly instead of UNREADABLE.
- **`BAKE_PAT` (websites repo — cross-repo).** A `menno420/websites` Actions secret whose absence
  blocks the websites nightly fleet-data bake / #380-class auto-merge. **Not a fleet-manager
  secret** — listed here only because owner-actions-2026-07-17 §6/D4 references it. Provision on
  the websites repo if the bake is wanted.
- **`OQ-POKEMON-ROM-REQUIRED-CHECK` — pokemon-mod-lab: add required check `ROM builds`.**
  https://github.com/menno420/pokemon-mod-lab/settings/rules → main ruleset → Require status
  checks → add context `ROM builds` (keep substrate-gate). Closes a live gate hole (a red ROM
  build can merge today). Pair with the protect-main item below.
  **⚠ CONFLICTING EVIDENCE, unresolved (2026-08-21, fleet review fm #878):**
  pml's own 2026-07-21 records claim protection is already live (`rom-builds` +
  `substrate-gate` required; "direct push to main is ruleset-blocked", closeout § e),
  but the API refuses to read it — `GET /repos/menno420/pokemon-mod-lab/rules/branches/main`
  and `/branches/main/protection` both return **403 "Upgrade to GitHub Pro or make this
  repository public to enable this feature"** — branch protection/rulesets are
  plan-gated on free-plan **private** repos. If that gate applies, the repo-side claim
  cannot currently be true. One owner look at the Settings UI settles it; neither
  record was rewritten on inference.
- **`OQ-POKEMON-PROTECT-MAIN` — protect pokemon-mod-lab `main`** (the fleet's only unprotected
  default branch). Settings → Rules → Rulesets → new ruleset on `main` (match what websites has).
  ↩️ reversible. Do at the same sitting as the ROM required-check.
  **⚠ Same plan-gate caveat as the entry above (2026-08-21):** the API says the feature
  needs Pro or a public repo, so this may be un-doable as written while pml stays
  private on the current plan — the UI check that settles the entry above settles
  this one too.
- **`OQ-NEXT-MERGE-QUEUE` — superbot-next: enable merge queue OR drop require-up-to-date** for
  `docs/**` + `control/**`. https://github.com/menno420/superbot-next/settings/rules → main
  ruleset. Kills the update-branch dance on the 6-check ruleset. Not-blocking; chronic time sink.
- **`OQ-KIT-P10-REQUIRED-CHECKS` — ✅ RESOLVED (overtaken; verified live 2026-08-28,
  the OD-24 round's session 3).** The live effective rules on kit `main`
  (`GET /repos/menno420/substrate-kit/rules/branches/main`, direct-PAT) require exactly
  one status check — **`kit-quality`** — with strict-up-to-date `false`: both halves of
  this ask are done. No click needed. **The residue is agent work, not an ask:** the two
  `legacy-alias-*` jobs in kit `ci.yml` (whose own comment says "delete after P10
  lands") are now deletable in a kit build session —
  [the truth pass](findings/2026-08-28-kit-tree-truth-pass.md) § 5. *Original ask:
  swap required checks to `kit-quality`, up-to-date OFF; retires the legacy alias jobs.*
- **`OQ-GBA-ROM-RULESET` — ✅ RESOLVED (overtaken; verified live 2026-08-21, fleet review
  fm #878).** The ruleset exists and is **active**: `main-branch-protection` (id 18745286)
  on gba `main`, requiring **two** contexts — `NDS ROM build` and `ROM builds`
  (`GET /repos/menno420/gba-homebrew/rules/branches/main`, direct-PAT). Done work; no
  click needed. **The residue is a trap, not an ask:** the required `NDS ROM build`
  check reds on every cold-cache PR (BlocksDS 1.21.1 pin unrecoverable) — see
  `OQ-GBA-NEXT-PICKS` § NOTE. Do not "fix" that by touching the ruleset without the
  owner's word.
### (C) Product / external (cross-repo, owner-only — real accounts/keys)

- **`OQ-CL-LOOKS-PASS` — ✅ RESOLVED (done by you; verified from the tree 2026-08-21, the
  kit-seed session).** The looks pass this entry waited on landed the morning of 2026-08-21
  as couch-legend **#3** ("Style Couch Legend as the Lucid Chronicle" — its contract doc
  declares the direction owner-approved and the treatment *finalized by this looks pass*)
  plus **#4** (the first three Arc-1 scene packages, owner-approved, deliberately dormant
  until the stage schema lands). That is exactly this entry's VERIFIED-NEEDED condition
  ("any ChatGPT-Work commit landing"). The Layer-2 folder is re-threaded
  ([`repos/couch-legend/README.md`](repos/couch-legend/README.md)) and the **Claude
  implementation session is UNBLOCKED** (stage schema + tuning adoption + arc-1 content;
  checklist: couch-legend `docs/sim/2026-08-20-life-story-balance.md` § 7 + #4's handoff
  notes). No click needed.

- **`OQ-CL-FEEL-PASS` — couch-legend: play the life story and feel-check the tuned late
  game.** OPEN (2026-08-21, the implementation session). WHAT: the § 7 implementation landed
  (couch-legend #7 — adopted tuning, 18 chapters, the first three painted scenes, chapter
  turns); every number is sim-evidenced but no human has felt the adopted curve. WHERE:
  <https://menno420.github.io/couch-legend/>. HOW: just play — the opening three chapters
  arrive inside the first half hour; take one Wake & Bake; for the late game, import a late
  save code if you want to skip ahead. WHY-IT-MATTERS: DESIGN § 9.5's trade (late cycles pay
  in story cadence, not compounding speed) is yours to veto, and the sim's closest rail is
  the arc-3 post-reset warm-up (44.8 m of the 45 m bound) — exactly where drag would be felt
  first. UNBLOCKS: arc-3 content sizing; whether the Clarity spend shop (§ 8.1) gets
  designed. ↩️ reversible (tuning is one constant + pins, with the sim as the instrument).
  VERIFIED-NEEDED: your verdict on (a) the chapter-turn moment, (b) late-game rebuild feel.

- **`OQ-CL-CHATGPT-REPASTE` — couch-legend: one paste refresh of the ChatGPT project
  instructions.** OPEN (2026-08-21, the kit-seed session). WHAT: the kit seed
  (couch-legend #5) made three lines of the pasted instructions stale — "no kit
  apparatus", "the one gate", "after green ci" — and the committed fence is already
  corrected. WHERE: the "Couch Legend" ChatGPT project → Instructions field. HOW:
  replace the whole field with the current fence from
  [`prompts/chatgpt-couch-legend-project-instructions.md`](prompts/chatgpt-couch-legend-project-instructions.md)
  (one copy-paste). WHY-IT-MATTERS: a ChatGPT session told the repo has no kit will
  meet bootstrap.py/CONSTITUTION.md and may "clean them up" or distrust its own
  instructions. UNBLOCKS: nothing hard — the gate passes card-less PRs, so ChatGPT
  work lands fine meanwhile; this closes a truth gap, not a block. ↩️ reversible.
  VERIFIED-NEEDED: your word that the field is refreshed (agents cannot read ChatGPT
  project settings).

- **`OQ-VENTURE-STRIPE-KEYS` — venture-lab: Stripe TEST keys.** Paste `sk_test_…`
  (`STRIPE_SECRET_KEY`) + `whsec_…` (`STRIPE_WEBHOOK_SECRET`) into
  `candidates/membership-kit/server/.env` (never committed). Unblocks the only unverified leg of
  the payment path for all 3 products.
- **`OQ-VENTURE-PUBLISH-CLICKS` — venture-lab: publish products on gumroad.com** — per-product
  scripts in `docs/launch/**/owner-actions.md`. **Two corrections (2026-08-21, fleet review
  fm #878):** stripe-webhook-test-kit $29 — listed here among "3 to publish" — went **LIVE
  2026-07-12** and has been the estate's one live SKU ever since (venture-lab
  `docs/current-state.md`); and the whole publish wave is **suspended by OD-11**
  ("let it sit", 2026-07-26) — this entry is inert until you lift that, not a pending click.
- **`OQ-VENTURE-GOTCHA-ARTICLE` — venture-lab: publish the Stripe-webhook gotcha article**
  (`docs/launch/stripe-webhook-test-kit/gotcha-article.md`) on Dev.to/Hashnode. Starts the 14-day
  validation clock candidates #4/#5 wait on.
- **`OQ-WEBSITES-RAILWAY-POSTGRES` — websites: add Railway PostgreSQL** to project
  superbot-websites, copy `DATABASE_URL` into service **botsite**. Unblocks public `/submit`.
- **`OQ-WEBSITES-PAT` — websites: a token for control-plane, one recipe, two tiers.** STILL OPEN
  (the mint is yours; wiring is a session's). **NOTE 2026-08-26: the same sitting
  can mint the SECOND token Move 3's comment loop needs** — a fine-grained PAT
  on fleet-manager with **Contents R/W AND Pull requests R/W** (the loop lands
  comments via branch + PR because main's ruleset requires PRs, so Contents
  alone writes the branch and then stalls at the PR call — `@codex` fm #951)
  for `app/writeback.py`'s new fm target; the deployed token's scope is
  `UNVERIFIED` (its docstring says read) and the packet is
  [the execution packets](planning/2026-08-26-estate-execution-packets.md)
  § 5 PKT-D3. Purpose: lift the 60/h anonymous GitHub rate limit
  on the readiness board's polling. **Minting is UI-only — measured 2026-08-16** on your ask
  (*"use my account pat to mint one? Please try that"*): `POST /user/personal-access-tokens` →
  404, `GET` same path → 404, legacy `POST /authorizations` → 404, against positive controls
  same token/minute (`GET /user` → 200, `POST /user/repos` → 201); GitHub's own docs describe
  creation as Settings-UI steps only. **The path:**
  `https://github.com/settings/personal-access-tokens/new` → name `control-plane-readiness-poller`
  → expiration 1 year → then PICK ONE TIER (this entry used to prescribe both at once —
  corrected):
  **Tier 1, recommended now — rate limit only:** Repository access **"Public repositories
  (read-only)"**, zero permission boxes. Blast radius if leaked: public-data reads. The `/owner`
  re-run-CI button stays inert (it needs actions:write and can wait).
  **Tier 2, only if you want the `/owner` re-run button live:** All repositories (or the fleet
  set) + Contents:read, Actions:read+write — the scope the original 07-15 entry named. Bigger
  token; only worth it when that button matters.
  Paste the `github_pat_…` in the hub chat; a session wires it into Railway (`variableUpsert`
  on control-plane) and redeploys.
- **`OQ-GBA-LUMEN-RELEASE` — ✅ RESOLVED (overtaken; verified live 2026-08-21, fleet review
  fm #878).** The Release exists: tag `lumen-drift-v1.3`, **published 2026-07-18T20:07Z**
  (`GET /repos/menno420/gba-homebrew/releases`, direct-PAT; gba's own closeout § b records
  the same). This entry asked for work that had been done for a month.

### (D) Standing decisions

- **`OQ-CL-LICENSE` — couch-legend: pick a license, or say "none on purpose".** OPEN
  (2026-08-20, the adoption session). WHAT: the new public repo `menno420/couch-legend`
  ships without a LICENSE file, so it defaults to all-rights-reserved — nobody may legally
  reuse the code, which may or may not be what you want (D-0012 governs *disclosure*, not
  reuse rights, so publish-by-default does not answer this). HOW: one word in the hub chat —
  e.g. **"MIT"** (recommended for the code; the art and story stay yours and a session
  records that split in the README) or **"no license on purpose"** — and a session commits
  it same-day. UNBLOCKS: nothing technical; legal clarity only. VERIFIED-NEEDED: not
  attempted — licensing is ownership, not an agent call.

- **`OQ-FM-APPARATUS-SIZING` ✅ RESOLVED 2026-08-07 — the owner answered: retire the roster.**
  Verbatim, in the hub chat: *"Yes retire the roster, I don't need it."* Executed the same
  session, and it went **further than the recommendation on file**, which was reduce-to-daily.
  What landed: both `roster-regen.yml` cron lines removed and `roster-freshness.yml`'s
  `pull_request` trigger removed (both keep `workflow_dispatch`, OD-3); `docs/roster.md`
  era-bannered `historical` with what it was for kept in view; the dead `roster-freshness`
  entry dropped from `merge-on-green.yml`'s `workflow_run` list; PR #808 closed unmerged with
  its cause recorded.
  **What forced the decision beyond noise:** the regen had *deadlocked*. It opened its PR with
  `github.token`, GitHub suppresses workflow runs for that actor, `substrate-gate` therefore
  never reported, and `main` requires it — 18 consecutive failed runs, a permanently
  unmergeable PR, and a red `freshness` on every `claude/*` PR. The workflow's own header knew
  the token behaviour and compensated by parking the PR for *"the next manager wake"*; that
  wake was the autonomous fleet, which closed 2026-07-21. The last generation's own verdict
  summary read **31 rows: 18 DARK · 7 n/a · 3 STALE-BY-DESIGN · 1 STALE · 1 PRIVATE ·
  1 UNREADABLE · 0 LIVE** *(this line said "21 DARK / 3 UNREADABLE" until 2026-08-11 — a
  pattern-matched distribution `roster.md:21-22` had already named as wrong; corrected from
  the file's generated summary, the fix `.sessions/2026-08-07-codex-caught-four.md` said
  durable history must not re-carry)* — the instrument working perfectly, reporting hourly
  that nobody is home.
  **The other verdicts in this item stand and are unchanged:** KEEP `merge-on-green.yml`, KEEP
  `substrate-gate.yml`, KEEP the S3/S5/S9 advisory checkers, HOLD `control/` + `telemetry/` as
  history. `scripts/gen_roster.py` and `scripts/check_roster_freshness.py` are untouched and
  still runnable. **Moots `OQ-FM-ROSTER-READ-PAT`** — that secret was conditional on retaining
  roster autogen. Original body below, for the record.

- **`OQ-FM-APPARATUS-SIZING` (superseded body) — right-size fleet-manager's own apparatus (NEXT-TASKS item 3).**
  WHAT: Decide which fleet-manager self-apparatus workflows/docs to **KEEP** vs **RETIRE/right-size**
  now that the fleet is a smaller set — a right-sizing pass on the self-apparatus.
  WHERE: `.github/workflows/**` (`merge-on-green.yml`, `substrate-gate.yml`, `roster-freshness.yml`,
  `roster-regen.yml`) + the `control/` message-bus (`inbox.md`/`outbox.md`/`status.md`) + the
  roster/telemetry autogen (`docs/roster.md`, `telemetry/triggers-snapshot.json`,
  `telemetry/model-usage.jsonl`) in this repo.
  HOW / recommendation (per actual workflow — a verdict each):
  - **KEEP `merge-on-green.yml`** — the repo's server-side backstop lander (verify-then-squash-merge);
    a useful belt-and-suspenders enabler even though agents also merge their own green PRs directly
    (MCP/REST `merge_pull_request`, fm #308/#309). Do not touch.
  - **KEEP `substrate-gate.yml`** — kit-owned merge gate (session-card / hygiene hold); load-bearing,
    regenerated by `bootstrap.py` on upgrade, never hand-retire.
  - **KEEP `roster-freshness.yml`** — the roster-freshness PR gate (fails a PR on a stale roster
    stamp); cheap, advisory-shaped, keeps the roster honest if regen is retained.
  - **KEEP the three new advisory checkers (S3/S5/S9)** — `scripts/check_owner_queue.py` /
    `check_roster_freshness.py` / `check_docs_links.py` and the S3/S5/S9 drift/staleness checkers;
    stdlib-only, zero coupling to the retired autonomous apparatus, load-bearing for records hygiene.
  - **HOLD / right-size `roster-regen.yml`** — the heaviest self-poll autogen (cron `40 */2 * * *`,
    every 2h → ~12 roster regens/day). A smaller fleet does not need 2-hourly regeneration.
    **Recommended: reduce the cadence** (e.g. daily `40 6 * * *`, keeping `workflow_dispatch` for
    on-demand) rather than delete — reversible, keeps the regen path alive. Delete only if the roster
    itself is retired.
  - **HOLD `control/` message-bus + `telemetry/` snapshots** — the ORDER relay is already retired
    (`control/inbox.md` is historical); keep the files as history, retire only the (now-absent)
    autogen that wrote them. No live workflow regenerates them, so no action beyond leaving them
    historical — revisit only if a real multi-seat fleet returns.
  WHY: the fleet is smaller now; the ORDER-relay + roster autogen was built for the full fleet and
  is over-built for a smaller one. Keep the load-bearing merge/gate/checker
  path; trim the over-built self-poll autogen.
  UNBLOCKS: a lean, intentional manager apparatus; less autogen noise (fewer roster-regen
  runs/PRs) without losing the landing path.
  VERIFY: after execution, the kept workflows (`merge-on-green` / `substrate-gate` /
  `roster-freshness`) still run + green; the reduced `roster-regen` fires on its slower cadence (or
  on `workflow_dispatch`) and the roster stamp stays inside `roster-freshness`'s threshold.
  RISK: ⚠️ — EXECUTION touches `.github/workflows/**`; the **RECORD here is ✅ reversible**. The
  DECISION (keep vs right-size) stays an owner call. *R30 note (2026-07-19):* once decided, the
  workflow-diff PR itself is normal agent work end-to-end — built and **agent-merged** under
  playbook R30 (fm PR #367, `docs/workflow-pr-merge-policy.md`, 3-point head-SHA check) — no
  owner merge click. *(Conditional cross-ref: `OQ-FM-ROSTER-READ-PAT` is only needed if
  roster autogen is retained; a `roster-regen` retire would moot it.)*
  *Program-close note (2026-07-21 seat close): the decision sharpens post-close —
  `roster-regen.yml` keeps firing ~hourly with no seats left to report, so the
  recommended reduce-to-daily (or disable) is now the sensible default; see
  [PROJECT-CLOSEOUT.md](PROJECT-CLOSEOUT.md) §3 item 5 / §4 checklist item 2.*
- **`OQ-CONSOLIDATION-DELETE-VS-ARCHIVE` ✅ RESOLVED 2026-07-26 — owner answered A (archive, never
  delete).** Answered in the hub chat 2026-07-26 ("Archive, don't delete"), recorded as **OD-3** in
  [`planning/2026-07-26-consolidation-plan-v2.md`](planning/2026-07-26-consolidation-plan-v2.md).
  This closes the standing contradiction between the 2026-07-10 "delete no repos — they are the
  fleet's memory" ruling and the 2026-07-12 "delete the test repos" ask: **the 2026-07-10 ruling
  stands.** Archive is read-only, hidden from the active list, free, and reversible in one click.
  **UNBLOCKS — and this is now time-ordered, not optional:** archiving **freezes the tag-push path
  forever**, so `OQ-CFGDIFF-RELEASE-DECISION` (cfgdiff v0.1.1, codetool-lab-sonnet5) and
  `OQ-ENVDRIFT-RELEASE-DECISION` (envdrift v0.1.0/v0.2.0, codetool-lab-fable5) must be
  **tagged + Released BEFORE** their repos are archived. Both are finished, documented CLIs
  sitting at **zero releases**. `codetool-lab-opus4.8` stays unarchived regardless (live mdverify
  install URLs). Agent-doable via the direct-token path; no owner click needed for the releases
  themselves. Superseding plan: v2 above (v1 = `planning/2026-07-26-fleet-consolidation-plan.md`;
  the 2026-07-12 plan is `historical`).
- **`OQ-RAILWAY-PROJECT-SPLIT` — websites Railway duplication.** Services exist in BOTH
  `reliable-grace` (live) and `superbot-websites` (parallel copy). Decide the canonical home; the
  Anthropic email links the reliable-grace URLs, so **keep them reachable** while that reference
  stands, then consolidate into `superbot-websites` and retire the duplicates. A drift hazard
  while both deploy. **UPDATE 2026-08-14:** the reachability constraint **lapsed 07-21**
  (correspondence concluded; program W1 note, verified 07-26), the canonical home is already
  decided (**`superbot-websites`** — websites #407 + the cutover plan), and the full cost/usage
  decision packet is now
  [`findings/2026-08-14-railway-websites-audit.md`](findings/2026-08-14-railway-websites-audit.md):
  the duplicates are a measured share of the $30.73 Aug bill. What remains owner-side is W1's
  per-service retirement go (stop → watch → delete), per the cutover plan's execution gate.
  **✅ EXECUTED 2026-08-14 (owner go, live; fm #863).** All three duplicates deleted
  (`review-f027` · `superbot-app` old botsite · `superbot-dashboard` old dashboard), the freed
  names reclaimed onto the canonical `superbot-websites` services (both old URLs now serve the
  new sites, verified live), `reliable-grace` reduced to `worker` + its two Postgres. Execution
  record: [findings/2026-08-14-railway-websites-audit.md](findings/2026-08-14-railway-websites-audit.md) § 7.
- **`OQ-RAILWAY-SHIFTLIFE-SCOPE` — ⚑ one-letter call: does "keep only bot things" cover shiftlife?**
  WHAT: your 2026-08-20 direction (*"the only things we should keep is the things that are
  actually related to the bot etc"*) named mineverse for removal; shiftlife (your app's live
  sync API + its database, real data) is the one surface where the reading is genuinely
  ambiguous, so no session touches it on inference. OPTIONS: **A) keep shiftlife
  (recommended — it is a product, not bot-web estate; removal takes the app's sync offline)**
  · B) remove it too, after a restore-verified dump to `menno420/estate-backups` (the fm #867
  pattern). HOW: one letter. WHY-IT-MATTERS: prevents a silent HIGH resolution either way;
  UNBLOCKS: the last scoping line of
  [planning/2026-08-20-railway-keep-bot-only-worklist.md](planning/2026-08-20-railway-keep-bot-only-worklist.md).
  (2026-08-20)
- **`OQ-RG-POSTGRES-BOTSITE` — ⚑ one-letter call: the now-orphaned old-botsite database.**
  WHAT: `reliable-grace/postgres-botsite` served ONLY the old botsite (wiring verified), which
  is deleted; the DB idles at ~$0.30/cycle. It is one of the two Postgres DBs W1's hard rail
  protects, so its disposition needs your explicit word — the blanket "execute the plan" go was
  deliberately not read as covering it. OPTIONS: **A) dump its contents to a durable
  PRIVATE home — a Release asset on a PRIVATE repo, or a dump handed to you directly —
  verify the dump restores, then delete the service (recommended — data preserved durably,
  cost gone)** · B) leave it running as-is. HOW: one letter in the hub chat; a session
  executes either in minutes. **CORRECTED 2026-08-14 (second pass, measured):** this entry
  first said "a Release asset on `superbot`" — wrong, because `superbot` is PUBLIC
  (`GET /repos/menno420/superbot` → `"private": false`) and a public repo's release assets
  are world-downloadable; user-submitted data must not land there. Also measured closing
  the orphan chain: worker's 32 variable values contain zero `postgres-botsite` references,
  and the DB has NO public TCP proxy — it is unreachable from outside `reliable-grace`.
  WHY-IT-MATTERS: last loose end of the Railway consolidation; UNBLOCKS: nothing else — purely
  cost/hygiene. (2026-08-14, fm #863)
  **✅ EXECUTED 2026-08-16 — owner ruled A, live.** Dumped over a temporary TCP proxy from a
  GitHub Actions runner (this container's egress is web-ports-only — 80/443 connect, Railway's
  high-port proxies don't; measured, ledger entry), the
  dump **restore-verified in-run** (full `pg_restore` into a scratch postgres:16 + row-count
  diff), archived as a Release on the new PRIVATE `menno420/estate-backups`
  (`postgres-botsite-final-2026-08-16`; sha256 `da3207d7…` / `7ad3e90a…`), then the temp proxy,
  the service, and the one-shot `PGB_DSN` secret all deleted; `reliable-grace` now holds exactly
  `Postgres` + `worker` (listing re-read). **The database was empty AT DUMP TIME — established
  from the dump's COMPLETE content, not a statement sample**: the archived plain dump re-read
  from the release asset (sha256-matched) is 26 lines, and every one of its 12 non-comment
  lines is pg_dump session-setup (`SET` / `set_config` / the restrict wrapper) — **zero
  statements of any other kind** (0 CREATE/ALTER/COPY/GRANT/COMMENT/INSERT), and pg_dump emits
  a CREATE for every object it dumps, so the snapshot held no tables, views, sequences,
  functions, types, or extensions in any schema. The live pre-delete count loop (zero `public`
  tables) agrees. Whether anything was *ever* written between 07-12 and the dump is
  `REASONED`-only (no consumer existed; a written-then-dropped past is not excludable from a
  snapshot). The archive preserves the empty state for the record.
- **`OQ-SB-BACKUP-ARTIFACT-VISIBILITY` — ⚑ the production bot-DB backups sit on a PUBLIC repo.**
  WHAT: the daily/weekly `backup-db.yml` dumps upload as GitHub Actions **artifacts on
  `menno420/superbot`, which is public** (`"private": false`, measured 2026-08-14) — and GitHub
  serves a public repo's workflow artifacts to **any logged-in GitHub user** (platform-documented
  read-access rule; not independently probed from a second account). The full production
  database — user data included — has been downloadable that way since the workflow's June
  creation. Pre-existing, NOT introduced by the consolidation; surfaced by the owner-review
  hook's question about dump visibility. OPTIONS: **A) move backups to a private home** (a
  private repo's artifacts/releases, or Railway-side once the plan allows) · B) make `superbot`
  private (bigger call — public URLs, the oracle role) · C) accept as-is, recorded. WHY-IT-MATTERS:
  quiet data exposure compounding daily; UNBLOCKS: nothing — risk hygiene. (2026-08-14)
  **✅ RULED 2026-08-16 — owner, live: "Accept" (option C).** Recorded as accepted; no pipeline
  change. Re-open only if the repo's visibility or the data's sensitivity changes.
- **`OQ-CR-SLICER-ANSWER` ✅ RESOLVED 2026-08-07 — the answer is **Bambu Studio**, and it
  arrived without the ask ever being put.** The question (one word: Cura / PrusaSlicer /
  OrcaSlicer / Bambu Studio) was open from 2026-07-15. It is answered by the hardware:
  the maker runs a **Bambu Lab A1 mini** and an **A1 with AMS Lite**, relayed by the owner
  and recorded in `curious-research/CLAUDE.md` (*"So his slicer is **Bambu Studio** — name
  its real menus, not 'your slicer'"*), with `guides/bambu-studio/` shipped 2026-08-07
  (curious-research PR #61). The follow-up guide this item was blocking therefore already
  exists. Kept as a closed entry rather than deleted, per the queue's ids-are-stable rule.
  **Worth noting as a queue-hygiene datapoint:** it stayed open ~23 days after the fact that
  closes it landed in another repo — an owner ask can be resolved by work that never looks
  at the queue, so a truth pass should sweep for this class rather than wait to be told.

### (E) Objection-only / parked (no click unless vetoing)

- `OQ-GAMES-S5-LATE-VETO` — games §5 late-veto, silence=proceed already operating.
- `OQ-R6-MOBILE-LAB-VETO` — ORDER 018 R6 mobile-lab decision, open indefinitely; veto = strike it.
- `OQ-TRADING-OOS-OPTIN` — trading OOS protocol is OPT-IN, never self-executes; file an ORDER only
  if wanted.
- `OQ-STANDING-OBJECTION-NOTES` — kit P4 daily loop self-armed · kit releases cut agent-side ·
  superbot-next D-0064–D-0069 decide-and-flag. Veto any by saying so.

### (F) Seat design decisions — deferred to the seats

These are genuine product/design forks the **SuperBot World / SuperBot 2.0 seats**
inherit; no owner click is blocking now.
- `OQ-IDLE-GENERATOR-PURCHASE` — superbot-idle: add the missing generator-purchase growth verb
  (rec A: geometric cost curve, SIM-pinned).
- `OQ-IDLE-CONTENT-DEPTH` — superbot-idle: depth direction after the upgrade→prestige spine
  (rec A: timed-events scoping).
- `OQ-NEXT-CURATION-RATIFICATIONS` — superbot-next: one-pass ratify the DROP-list (60) +
  settings-prune + D-0083 anchor (reversible pre-cutover, Q-0241 lane).
- **`OQ-IDEA-ROUTING-OWNER-ONLY` — Ideas-Lab items that are owner-only (not auto-routable).**
  The verified 2026-07-18 idea-routing pass
  ([idea-routing-2026-07-18.md](idea-routing-2026-07-18.md)) routed the buildable candidates
  (A–H) to their target lanes; these remaining Ideas-Lab items need an owner decision/action
  and cannot be auto-routed: **V011** review-service deploy · **venture-lab money-gated** items
  (×11, real accounts/keys) · **makerbench** · **trading** (owner-by-design) · **Ideas-Lab
  seat revival**. No agent click lands these — record-only until the owner acts. RISK: ✅.

- **`OQ-KIT-552-BENCH-REVIEW` — ✅ RESOLVED (PR merged 2026-08-04; entry closed 2026-08-14).**
  kit #552 was squash-merged 2026-08-04T16:56:54Z (API-verified; the label sits inert on the
  closed PR), so the bench pin this entry described is terminal and sweeps have nothing to
  skip. **The exemption class it recorded — a `do-not-automerge` PR waiting for owner review
  indefinitely — is retired under the owner's 2026-08-14 nothing-waits-in-an-open-PR ruling
  (decisions ledger, cited from the program's §7 review row):** an owner-wait lives inside a
  session; an unanswered fork closes the PR with its branch retained and the ask landed where
  `main` can see it. Original body, for the record: *(record only, no action urged)
  substrate-kit PR #552 is `do-not-automerge` BY DESIGN — an owner-review bench pin (the
  deliberate-merge carve-out), not a stuck PR; recorded so PR sweeps stop re-flagging it as
  stray. Provenance: 2026-07-20 morning sweep (fm PR #393).*

### (G) Hygiene (whenever — cosmetic; branch deletes work agent-side via the direct-token path, parked here only as low-priority)

- Stale-branch deletes: websites ×4 (`claude/harden-verify`, `claude/rework-dashboard`,
  `claude/wire-github-token-docs`, `manager/control-plant`) · gba `claude/brineward-wind` ·
  pokemon-mod-lab `track-a/session-019`, `track-a/session-024`, `claude/eloquent-newton-qaf1ii` ·
  fleet-manager `claude/consolidation-plan-v34`. (`OQ-WEBSITES-STALE-BRANCHES`,
  `OQ-STALE-BRANCH-DELETES-0713`.)
- Spent-chat archive in claude.ai (dead trading gen-1 session, wound-down gen-1 lane chats).
- Release clicks gated on `OQ-CONSOLIDATION-DELETE-VS-ARCHIVE=A`: cfgdiff v0.1.1
  (codetool-lab-sonnet5) · envdrift v0.1.0/v0.2.0 (codetool-lab-fable5) tag+Release before archive.

---

## Closed / no action — ids kept

These once-active items are moot; ids retained so nothing is lost, full bodies in git history.

- **Restructure / trigger-cutover / env re-paste** — superseded; the fleet was not restructured:
  `OQ-RESTRUCTURE-PROJECTS`, `OQ-RESTRUCTURE-INSTRUCTIONS-PASTE`,
  `OQ-RESTRUCTURE-TRIGGER-CUTOVER`, `OQ-ENV-SETUP-REPASTE`, `OQ-PASTE-WAVE`.
  Superseded by [project-recreation-runbook.md](project-recreation-runbook.md).
- **DARK-seat re-wakes** — not re-woken: `OQ-GAMES-DARK-REWAKE-OR-REASSIGN`,
  `OQ-GBA-DARK-REWAKE`, `OQ-FORGE-DARK-NO-ACTION-CONFIRM`, `OQ-KIT-SUBROWS-WINDDOWN-CONFIRM`,
  `OQ-GAMES-S5` re-wakes.
- **Apparatus cron trims** — folded into the apparatus sizing decision (`OQ-FM-APPARATUS-SIZING`):
  `OQ-SUPERBOT-CRON-TRIM`, `OQ-WEBSITES-FM-CRON-TRIM`.
- **Fleet-wide doctrine rulings** — moot: `OQ-HEARTBEAT-DOCTRINE-RULING`,
  `OQ-CODEX-GATE-VS-SUSPEND-RULING`.
- **Overnight dispatch** — superseded: `OQ-THIN-LANE-DISPATCH-2026-07-16`
  (remaining legs were classifier-walled · 2026-07-16).
- **Time-boxed / window-expired** — deadlines passed: `OQ-TRADING-0717-DOUBLE-GRADING-FIRE`
  (before 2026-07-17 09:00Z; impact ~zero — grade_paper is a no-op until ~August),
  `OQ-SITTING-0714-DECISIONS` (2026-07-14 window closed; any live game/product sub-decisions —
  playtest verdicts, gba Track B, websites cutover — carry forward via the active seats).
- **Mooted by consolidation** — `OQ-FORGE-SETTINGS-RESIDUE`, `OQ-FORGE-PAGES`,
  `OQ-FORGE-DISPOSITION`, `OQ-ITCH-LUMEN-PUBLISH`.
- **Seat env credentials (re-provision if the seat resumes)** — `OQ-NEXT-API-KEY`,
  `OQ-NEXT-HERMES-EGRESS-CREDS` (re-add to the superbot-next env if that lane resumes).
- **Cosmetic / optional** — `OQ-TRADING-ARCHIVE-SESSION`, `OQ-CODEX-FLAPPING` (YAML half already
  resolved; flapping-quota mitigation only).

---

## Resolved 2026-07-24 (hub chat GO — phase 0 executed same-session)

- **`OQ-APP-PLAN-GO` — RESOLVED: owner GO** (hub chat 2026-07-24: "use my PAT to create a new
  repo, seed it with the substrate-kit and then continue building this app"); defaults D1–D5
  taken, no overrides voiced. Executed same-session: private repo `menno420/shiftlife` created
  over the direct-PAT path and seeded (kit 1.20.1 enforcement-wired, all slots answered, strict
  gate exit 0) + phase-0 scaffold pushed (birth commit `d18aa30`): domain engine 27/27 green,
  product law, design directions, quality CI. Successor ask: `OQ-SHIFTLIFE-PHASE0` (Active above).

## Resolved 2026-07-21 (00:42Z night records slice — retire condition verified in the 00:42:48Z export, Q-0120; fm PR #410)

- **`OQ-SI-CHAIN-DEAD` — (VENUE: hub first, then owner) Self Improvement seat wakes but never
  resumes — chain DEAD since 07:53Z, 4+ failsafe fires with zero landed output.** *(Escalated
  2026-07-20T15:5xZ, 15:30Z records slice, PR #399 — the 11:30Z watch's tripwire fired:
  substrate-kit lane verdict QUIET→STALLED at the 15:52Z liveness run.)*
  WHAT: `session_01VsWWnVdwbvkGAW4kAmQzmt`'s work-loop chain has zero pending ticks since its
  07:53Z one-shot fired (confirmed at BOTH the 11:37:48Z and 15:38:36Z captures); its failsafe
  cron `trig_01194PdaWChtHGNKASURxdLx` ('Self Improvement failsafe wake', `2 */2 * * *`) IS
  firing (in-export last_fired 14:04:29.8Z, next 16:02Z), so the seat is being woken every 2h
  and each wake produces neither a chain re-arm nor a landed commit/heartbeat (substrate-kit
  lane STALLED, last signal 07:45Z). NEW failure class — "failsafe-fires-but-no-rearm": the
  dead-man's *catch* works, its *recovery leg* doesn't.
  WHERE/HOW (recommendation first): (1) **Hub coordinator** — read the seat session's recent
  transcript (`list_events session_01VsWWnVdwbvkGAW4kAmQzmt`) to see what the 4 wake turns
  actually did (error? refusal? instant end?), then `fire_trigger trig_01194PdaWChtHGNKASURxdLx`
  with an explicit resume text naming the stall. (2) **Owner**, if the next capture still shows
  no landed output: open the Self Improvement Project seat and inspect/restart it — a seat whose
  turns silently no-op is not recoverable by more wakes.
  WHY: substrate-kit is the fleet's foundation lane (7 adopters) and the current kit-wave has
  red legs pending; a dead Self Improvement seat also means nobody owns the kit-side follow-ups.
  *Status 2026-07-20T16:2xZ (declared-idle slice, PR #400) — **resolving: halt was a deliberate
  honest-idle, not a dead recovery leg.** The SI seat responded to the manager's post-16:02Z
  nudge (coordinator-reported ~16:1xZ): chain re-armed. Its own heartbeat had declared the idle
  in plain text all along (Baton, updated 07:45:00Z: "Agent-buildable kit slices are drained
  through v1.20.1 + #555…") — the escalation fired because the liveness checker could not read
  a declared idle. **Process fix landed this slice (PR #400):** `check_lane_liveness.py` now
  scores a STALLED/QUIET lane with a fresh dated idle declaration as `IDLE-DECLARED`
  (exit-neutral; undated declarations keep the escalation hint) — ground-truth run 16:16Z
  scored substrate-kit IDLE-DECLARED. **RETIRES once the next triggers snapshot shows a fresh
  pending SI one-shot** (a `run_once_at` bound to `session_01VsWWnVdwbvkGAW4kAmQzmt` due after
  16:1xZ) — verify at the next snapshot cycle, then move this item to Resolved.*
  *RESOLVED 2026-07-21T03:1xZ (00:42Z night records slice, PR #410) — retire condition MET,
  verified in-export (Q-0120): the 2026-07-21T00:42:48Z capture holds a fresh pending SI
  one-shot `trig_01MXe8mtyEYMsr67Dbj3gQh4` (`send_later 2026-07-21T00:48Z #cbc4b3`, created
  2026-07-20T23:47:45Z, run_once_at 00:48:00Z — pending at capture) bound to
  `session_01VsWWnVdwbvkGAW4kAmQzmt`, plus the failsafe armed (next 02:02Z). The chain re-armed
  after the ~16:1xZ nudge and was still self-continuing at 23:47Z; liveness now scores
  substrate-kit IDLE-DECLARED (the PR #400 process fix reading its dated declaration).*

## Resolved 2026-07-19 (18Z records slice — verified by `check_label_hygiene.py` ground truth, Q-0120)

- **`OQ-LABEL-DEFS-DELETE` — RESOLVED (deletions verified executed).** The 9
  `do-not-automerge` label DEFINITIONS queued for hub deletion (websites ·
  substrate-kit · fleet-manager · superbot · gba-homebrew · idea-engine ·
  venture-lab · superbot-games · superbot-next) are **GONE**: ground-truth run 1
  of `scripts/check_label_hygiene.py` (landed fm PR #370) at 2026-07-19T16:15Z
  measured **19/19 fleet repos, 0 hold-class definitions, 0 applications to OPEN
  items** — i.e. the deletions were executed between the 08:38Z queue write
  (fm PR #351) and 16:15Z (hub venue or owner), and the checker run IS the
  "re-run after deletions → 0 definitions" verification the item specified.
  The item's residual websites caveat (`host-automerge-extras.yml`
  auto-re-create/auto-apply machinery, still live on main at 16:16Z) is NOT
  covered by the deletions and is re-scoped to its own Active item
  **`OQ-WEBSITES-LABEL-MACHINERY`** above (owner venue; two 2026-07-19
  classifier gates on the relayed dispatch; lands under R30 once open).
  Standing tripwire for label re-appearance: `python3 scripts/check_label_hygiene.py`.

## Resolved 2026-07-19 (10Z records slice — websites status read live via raw fetch, Q-0120; fm PR #355)

- **`OQ-WEBSITES-036-STALL` ✅ RETIRED 2026-07-19 (lane revived — 036 acked + discharged)** —
  the info-only stall note (fm PR #346; annotated PR #351) hits its own retire condition:
  websites `control/status.md` (live raw fetch 2026-07-19T10:36Z, stamp **09:17:59Z**) shows
  `orders: acked=001-036 done=001-020,022-036` with **036 discharged — "BAKE_PAT landing path
  proven, ASK-0008 finalized via merged PR #439"**; lane clearly alive (first movement
  07:26:23Z / #436, then #439 + #440 merged — main tip `f8caa03` — and #441 in flight;
  ORDER 034 also done: botsite `/submit` durable-intake verified live 08:27:36Z). The
  discharge is the lane's own declaration per its status grammar — the ORDER's bake path is
  proven and the seat holds any residual data-refresh work in its own baton, so nothing
  remains hub-side. No action taken against the lane; note retired on evidence.

- **`OQ-FM-ROSTER-CRON-RELIABILITY` ✅ RESOLVED 2026-07-19 (fix live on main — owner merged #344)** —
  the watch's verdict was already reached (drops recur: 00:40Z 3 nights running, +02:40Z on
  07-19); the one-line fix, fm [#344](https://github.com/menno420/fleet-manager/pull/344)
  (second odd-hours cron), **merged 2026-07-19T09:22:03Z, merge commit `b6f01d2`** after the
  owner resolved its conflict. Verified live at origin/main:
  `.github/workflows/roster-regen.yml` now carries BOTH schedule lines — `cron: "40 */2 * * *"`
  and `cron: "40 1-23/2 * * *"` (net hourly coverage; one dropped window is covered by the
  adjacent hour). **Delivery-proof condition:** first odd-hour-window proof = a roster gen
  stamped within ~1h of an odd :40 window. Not yet observable at close (read 09:2xZ; latest
  regen on main is gen #100 at 07:08Z from the even-hour line; the first post-merge odd window
  is 09:40Z) → **fix live, delivery proof pending the next odd-hour window** — tracked as a
  baton watch in `control/status.md`, not an owner ask. The CCR-routine migration fallback
  stays documented in the workflow header if drops persist even at hourly coverage.
  **PROOF ACHIEVED 2026-07-19 (10Z records slice, fm PR #355):** roster-regen `schedule`
  run #83 fired **2026-07-19T10:09:02Z** (success) and delivered **gen #101** (merged
  10:09:34Z, commit `b95d398`) — within ~1h of the first post-merge odd :40 window (09:40Z,
  ~29 min GitHub schedule delay) and *before* the next even window (10:40Z). Attribution to
  the odd-hours line is clean: the Actions run list shows **no run between 07:08:39Z and
  10:09:02Z**, i.e. the 08:40Z even window itself skipped and the odd line's delivery covered
  it — exactly the adjacent-hour coverage #344 was built for. Baton watch retired.
  Companion slug `OQ-FM-ROSTER-CRON-SECOND-LINE` (the queue row #344 carried in its own diff)
  is **closed here too** — the owner's conflict resolution kept main's queue text, so that row
  never landed; this entry is its terminal record.

## Resolved 2026-07-23 (owner-live hub session — controller-app directive, same-day)

- **`OQ-FORGE-SLICE4-LAND` ✅ RESOLVED 2026-07-23 (hub-executed same session — no owner click
  needed)** — the phone-controller Slice-4 series landed **directly**: mid-session the owner
  turned off automode and `add_repo` brought product-forge into scope, so the staged handoff's
  own patches were pushed as branch `claude/controller-app-android-apk-j7tv10` →
  [product-forge #33](https://github.com/menno420/product-forge/pull/33) (all checks green:
  capability-core incl. `:hid-core:test`, assemble-app, substrate-gate) → **squash-merged
  2026-07-23, sha `ccb1e98`** (workflow-touching diff merged on green under the live
  directive; precedent #29) → tag `phone-controller-v0.4.0` (REST path; proxied git tag-push
  403s — path quirk, routed around) → android-release run 30044359167 **success** →
  **[Phone Controller v0.4.0](https://github.com/menno420/product-forge/releases/tag/phone-controller-v0.4.0)
  verified live with `phone-controller-0.4.0.apk` (2.1 MB) + `.sha256` attached.** The
  handoff dir (`projects/product-forge/handoff/2026-07-23-phone-controller-slice4/`) stays
  as provenance, README flipped `landed`. Remaining owner asks live forge-side: ⚑ OA-004
  (two-device playtest) · ⚑ OA-005 (optional stable-signing secrets).

## Resolved 2026-07-19 (morning executions ~07:40–08:10Z, owner nothing-stuck directive — state read live via the GitHub MCP, Q-0120; fm PR #351)

- **`OQ-FORGE-29-WORKFLOW-MERGE` ✅ RESOLVED 2026-07-19 (hub-executed — no owner click needed)** —
  [product-forge #29](https://github.com/menno420/product-forge/pull/29) **squash-merged directly
  via MCP 2026-07-19T07:41:57Z**, merge sha `20be7493a7c4d96b3b61e1f2f023ed77ad015e27`;
  `android-ci.yml` verified present on product-forge main. Executed under the owner's live
  ~08:00Z nothing-stuck directive (verbatim in `docs/fleet-triage.md` § "owner nothing-stuck
  directive"). The hub queue's last workflow carve-out is cleared.

## Resolved 2026-07-19 (03:0xZ night wake, fm PR #343 — state read live via the GitHub MCP at the 02:33Z stall-catch, Q-0120)

- **`OQ-POKEMON-98-WORKFLOW-MERGE` ✅ RESOLVED 2026-07-19 (overtaken by events — no owner click
  needed)** — [pokemon-mod-lab #98](https://github.com/menno420/pokemon-mod-lab/pull/98) was
  **CLOSED unmerged 2026-07-18T23:18:04Z as superseded by
  [#107](https://github.com/menno420/pokemon-mod-lab/pull/107)**: the QoL count-guard this row
  existed to unblock landed there in corrected 18-flag form (closing comment on #98 records the
  supersession). The workflow-carve-out merge click is therefore moot; the hub queue drops to
  product-forge #29 (`OQ-FORGE-29-WORKFLOW-MERGE`, still open + green above). Evidence:
  `control/status.md` § "02:33Z failsafe stall-catch (2026-07-19)".

## Resolved 2026-07-18 (fleet PR sweep 21:05–21:15Z — state read live via the GitHub MCP, Q-0120)

- **`OQ-GBA-DRAFT-PILE` ✅ RESOLVED 2026-07-18 (overtaken by events — remaining work is lane-side,
  no owner click)** — the 13-PR born-red pile is **gone** (merged/closed); the only survivors are
  gba-homebrew [#177](https://github.com/menno420/gba-homebrew/pull/177) /
  [#178](https://github.com/menno420/gba-homebrew/pull/178), both **ready-flipped + auto-merge
  armed 2026-07-18T11:26Z**, blocked only by the **by-design substrate-gate red** on main (#151
  doc orphans). Clearing that gate is gba-lane work, not an owner click, so the item leaves the
  Active queue. Evidence + disposition: fleet-triage § "2026-07-18 · fleet PR sweep
  (21:05–21:15Z)".

## Resolved 2026-07-17 (agent-side — wake chain restored via native MCP scheduling)

- **`OQ-FM-WAKE-CHAIN-ARM` ✅ RESOLVED 2026-07-17 (agent-side; owner action no longer needed)** —
  wake chain restored agent-side via native MCP scheduling; failsafe
  `trig_01Bo7dZxM9xz2hwR36L424Z8` armed (cron `30 */2 * * *`, enabled, next 2026-07-17T22:36Z,
  coordinator-bound dead-man, persist_session:true) + pacemaker restored. The earlier ask assumed
  a hard wall that was actually the Bash-fallback path + a nondeterministic classifier — native
  scheduling via worker ToolSearch works (see `docs/CAPABILITIES.md` 2026-07-17 UPDATE). UNBLOCKED:
  I4 MANAGER-FAILSAFE.

## Resolved 2026-07-17 (owner execution close-out ~09:17–10:19Z; swept fm PR #281 — state read live per-PR via the GitHub API, Q-0120)

*The 2026-07-16 PR-landing-audit trio, executed by the owner as owner-actions-2026-07-17 §1–§3 this morning. Each PR state below was re-verified live via `get_pull_request` on 2026-07-17 before this sweep.*

- **OQ-WEBSITES-359-MANUAL-MERGE ✅** *(was A#69)* — websites #359 was NOT merged by hand; it was **CLOSED-unmerged** 2026-07-17T09:23:17Z (`merged: false`, was `mergeable_state: blocked`), **superseded** by today's identical-payload bake [#380](https://github.com/menno420/websites/pull/380) which MERGED 2026-07-17T10:19:30Z (merged_by menno420, admin-override — the §5 disposition, not the original "merge #359" ask). Net: the stale-bake concern is cleared; #359 dropped, #380 carries the refresh.
- **OQ-POKEMON-87-CONFLICT-DISPOSITION ✅** *(was A#70)* — owner took **D1 rec = CLOSE** (option B): pokemon-mod-lab [#87](https://github.com/menno420/pokemon-mod-lab/pull/87) CLOSED-unmerged 2026-07-17T10:17:04Z (`merged: false`, `mergeable_state: dirty` — the real control/status.md conflict, superseded by the newer dormancy commits on main). The seat's only stuck PR is cleared; seat-dormancy record stands on main.
- **OQ-READY-FLIP-TRIO-0716 ✅** *(was A#71)* — trio disposed 2026-07-17:
  - gba-homebrew [#153](https://github.com/menno420/gba-homebrew/pull/153) **MERGED** 2026-07-17T09:17:04Z (merged_by menno420) — the DO-FIRST flip; repaired main's substrate-gate red. Its ~27 parked arc PRs still need agent rebases onto this fix (game-lab lane work — see fleet-triage 2026-07-17 note).
  - superbot-idle [#145](https://github.com/menno420/superbot-idle/pull/145) **MERGED** 2026-07-17T09:19:07Z (merged_by menno420) — control stale-claims sweep landed.
  - superbot-games [#149](https://github.com/menno420/superbot-games/pull/149) **CLOSED-unmerged** 2026-07-17T10:17:01Z (`merged: false`, was draft + `do-not-automerge`) — the D3 rec was rebase+merge, but the **owner outcome was CLOSE** (the draft mirror of idle #142 discarded; the reconcile-race guard rides the idle-side fix). Trio net: 2 merged, 1 closed.

## Resolved 2026-07-16 (maintenance wake ~01:1xZ, fm PR #253 — state read live via the GitHub API, Q-0120)

- **OQ-FM-PR227-MERGE ✅** *(was A#63)* — fleet-manager
  [#227](https://github.com/menno420/fleet-manager/pull/227) (lanes.json
  generation-parity fix + roster-regen.yml staging fix) MERGED by the owner
  (merged_by menno420) 2026-07-15T22:47:58Z, head `6d53047` — the
  workflow-diff owner-merge-only rail made this click the sole landing path
  (ORDER 047 leaves technical rails standing; the ask named the wall, not
  ratification). Flagged by this wake's `check_owner_queue.py` run
  (`merged-citation` on the cited PR) and verified live. UNBLOCKS delivered:
  `registry/lanes.json` now stages with every roster-regen cron commit
  (Gen #65 regen ran clean post-merge, roster PR #250).

## Resolved 2026-07-15 (evening oversight wake ~20:3xZ, fm PR #245 — state read live via the GitHub API, Q-0120)

- **OQ-ROLLOUT-INSTALLER-CLICKS ✅** *(was A#68; self-declared RESOLVED
  17:0xZ by fm PR #241, moved to this section by the evening wake — the
  4 `resolved-not-swept` check_owner_queue flags close with this move)* —
  the owner merged all five merge-on-green installer PRs
  2026-07-15T15:29:41–15:29:52Z (each `merged_by menno420`; workflow file
  verified at each repo's live main):
  opus4.8 [#24](https://github.com/menno420/codetool-lab-opus4.8/pull/24)
  15:29:44Z (main `61efaa9`) ·
  fable5 [#17](https://github.com/menno420/codetool-lab-fable5/pull/17)
  15:29:47Z (main `e7ca47c`) ·
  product-forge [#25](https://github.com/menno420/product-forge/pull/25)
  15:29:50Z (main `1efbb3b`) ·
  pml [#89](https://github.com/menno420/pokemon-mod-lab/pull/89)
  15:29:52Z (main `ec63823`) ·
  plugin-hello [#3](https://github.com/menno420/superbot-plugin-hello/pull/3)
  15:29:41Z (main `abd9133`).
  Since PROVEN live in **four** of five (fable5 probe #18 16:54:14Z · pml
  probe #90 15:30:22Z · opus4.8 probe #25 15:30:46Z · product-forge probe
  #26 15:30:14Z — each `merged_by github-actions[bot]`; the last two
  flipped by the evening wake). Coverage headline **18/19 — 17 PROVEN**;
  full table: fleet-triage § 2026-07-15 A#68 note + evening-wake update.
  Residual (hub-side recommendation, on the fleet-triage plugin-hello
  row, NOT an owner click): plugin-hello's automation is INERT — zero CI,
  zero check runs = NOT-ready by design; needs a minimal CI gate
  (agent-doable) or accept-as-inert.

## Resolved 2026-07-15 (queue sweep, 11:4xZ — state read live via the GitHub API, Q-0120)

- **OQ-FABLE5-PR16-MERGE ✅** *(was A#62)* — codetool-lab-fable5 #16 MERGED
  by the owner (merged_by menno420) 2026-07-15T10:54:19Z, head `ba88daa`
  (hygiene: 11 tracked `.pyc` files removed + top-level `.gitignore` added;
  ORDER 026 / consolidation ORDER P1-5). The B#42 archive click
  (OQ-CONSOLIDATION-ARCHIVE-FABLE5) is now gated only on the E#46 envdrift
  letter — its HOW line updated this sweep.

## Resolved 2026-07-12 (owner-live session — Railway/API executed directly)

- **websites `ANTHROPIC_API_KEY` ✅** — set on the LIVE review service
  (`reliable-grace`/review, serving review-production-f027; owner-approved,
  service redeployed 2026-07-12 ~16:0xZ) AND on the parallel
  `superbot-websites`/review service. The websites-order (ORDER 019) B-section
  blocker is pre-cleared; the on-site AI assistant has its key.
- **mineverse web host ✅ (the non-portal 4/6 of OQ-MINEVERSE-ENV-VARS)** —
  Railway project `superbot-mineverse` created, `web` service deployed
  read-only degraded at `https://web-production-97636.up.railway.app` (CLI
  one-shot; auto-deploy verified working same day — item 38 struck), 3 vars
  set (signing key · redirect URI · client id). Remainder split: 2 portal
  steps stay owner (item 17), the write pair stays agent-side (FLAG 2).
- **mineverse sign-in: OWNER PORTAL STEPS COMPLETE ✅ (evening, same day)** —
  the owner registered the redirect URI (proven: Discord's consent screen
  renders on /auth/login) after the OAuth-app reuse (item 17 update). The
  first live sign-in then failed at token exchange — root-caused to
  discord.com/Cloudflare 403ing urllib's default User-Agent (valid
  id+secret; curl UA 200 vs python UA 403 on the same endpoint) — fixed in
  mineverse PR #45 (UA header + server-side error logging). Nothing further
  is owner-side for sign-in; #45's merge auto-deploys and the owner retries.
- **roster-freshness BRIDGED ✅** — `fleet roster regen bridge`
  (`trig_011LrFY1k5cUHRYH6zwTvPvn`, `50 */2 * * *`, fleet-manager env,
  fresh-session) lands parked roster PRs + refreshes the triggers snapshot;
  RETIRED same day: the owner clicked the toggle and the bridge trigger was deleted after live verification (runs 29202721367, PRs #129/#131).

## Resolved 2026-07-11 (P3 curation sweep, ~20:1xZ — every state below re-verified LIVE per PR, Q-0120)

The whole (A) merge group plus the UNIVERSAL-clause trail item, all clicked by
the owner (merged_by menno420 in every case; states read live via the GitHub
API this sweep, not from reports):

- **OQ-GAMES-PR27-MERGE ✅** — superbot-games #27 MERGED 2026-07-11T14:56:05Z,
  merge `50f6774` (Q-0267 theme-readiness delta on main).
- **OQ-GAMES-PR32-MERGE ✅** — superbot-games #32 MERGED 2026-07-11T14:56:17Z,
  merge `f9c2f7a` (survival sim harness + Q-0087 bands in CI).
- **OQ-GAMES-PR38-MERGE ✅** — superbot-games #38 MERGED 2026-07-11T14:56:26Z,
  merge `2f1e7cd` (D&D story design; the story-game code lane is unblocked —
  the walking skeleton in fact already landed as games #48 → `b835f59`).
- **OQ-KIT-PR181-RATIFY ✅** — substrate-kit #181 MERGED (= ratified)
  2026-07-11T14:56:40Z, merge `f7aa633` (T5 re-scope v2; kit's own ledger
  recorded the ratification at `5d4978e`).
- **OQ-UNIVERSAL-MERGE-CLAUSE ✅** *(old items 16 → 13 — the HOT
  owner-provenance item)* — the corrected §2.4 merge-authority clause is LIVE:
  PR #76 MERGED by the owner 2026-07-11T15:26:47Z (merge `e1848ff`,
  UNIVERSAL.md v4 at both locations, cmp-verified during ORDER 017); ORDER 017
  executed fleet-wide via PR #77, MERGED by the owner 2026-07-11T18:40:12Z
  (merge `39b888a`). Trail: #47 merged 14:55:53Z (`5625e3b`,
  intent-signal-only); the §2.4 block was staged by #68 (merged 11:48:30Z,
  `c5e264f`). Successor ask: the paste wave (OQ-PASTE-WAVE) is now
  click-ready.

## Resolved 2026-07-11 (verified)

- **superbot-games #34 MERGED** 13:40:40Z (merge `5147a23`) and **#36 MERGED**
  13:40:50Z (merge `325c567`); **games ORDER-004 self-review LANDED** (games
  PR #47 → main `201f8dd`, 13:41:25Z). The "5 parked PRs" item is now the 3
  merge clicks at A#1–3.
- **pokemon-mod-lab PRIVATE confirmed stuck** (API `private: true` + lane R22
  re-verify 14:07:05Z @`f69ab95`).
- **kit P4 daily-loop half of old item 5 — self-armed agent-side** (kit
  self-review @`2aa7a51`); the P10 half is carried as B#10.
- **Codex hard-cap claim RETIRED → flapping** (evidence at C#20).
- **trading OOS "veto window" framing RETIRED → opt-in** (reframed at E#31).

## Parked (valid, no rush)

- **Account-wide visibility review** — all 13 repos public at the 2026-07-10
  night review; pokemon-mod-lab now private, the rest — including
  fleet-manager (this owner queue is on the open internet) — remain public.
  Decide per-repo public/private; pairs with the §4.9 repo-settings sweep.
- **superbot-next grants** — intents toggles · sacrificial Discord account ·
  capped API key (band 7); folds into the band flow (superbot-next
  `control/status.md` ⚑). *(The API-key half is now the active C#16.)*
- **websites product questions** — domains · /submit Postgres (now active
  D#24) · /admin OAuth+home · restyle · cutover (websites
  `docs/owner/OWNER-ACTIONS.md`, each with a recommended default).
- **Anthropic email pack** — the 2026-07-14 email was sent; the **next** email
  (capability self-knowledge) is drafted paste-ready at
  [anthropic-email-pack.md](anthropic-email-pack.md) — review + send on the
  existing Gmail thread. It folds in the four routines platform bugs (runs
  not inspectable · Runs-panel vs Routines-screen disagreement · arming
  seat-inconsistency · model attribution inconsistent across surfaces;
  evidence: `CAPABILITIES.md` § routine self-arm rider).
- **PyPI trusted-publishing registration** (~2 min) — token-less kit releases.
- **codetool-lab-fable5 (envdrift) v0.1.0 + v0.2.0 tags + Releases** —
  tag-push 403; owner click at Releases → Draft: v0.1.0 @ `73ef38d`, v0.2.0 @
  `13a84e5`. (Provenance of the earlier opus4.8 mislabel correction:
  `projects/codetool-lab-{fable5,opus4.8}/meta.md`; opus4.8's mdverify
  Releases are LIVE.) *(2026-07-12: the release-or-not decision is now
  ACTIVE at E#46, OQ-ENVDRIFT-RELEASE-DECISION — this stays as the click
  surface for the historical tags if E#46 = A.)*
- **codetool archive toggles ×3 (paired DECISION)** — all three repos
  `"archived": false` (API-verified 2026-07-10); recommendation: **wait until
  the gen-3 succession question settles, then archive** (archiving makes the
  repos read-only). *(2026-07-12: PROMOTED — superseded by the consolidation
  plan's sequenced clicks: sonnet5 + fable5 archive at B#41/B#42 after
  Phase 1 + E#45/E#46; opus4.8 stays UNARCHIVED (KEEP-QUIET, mdverify
  release host — per the plan it is NOT one of the three archives; the third
  is product-forge, B#40).)*
- **cfgdiff v0.1.1 release — two clicks (codetool-lab-sonnet5):** (1) PyPI
  pending publisher (owner `menno420`, repo `codetool-lab-sonnet5`, workflow
  `release.yml`, environment `pypi`); (2) `git tag -a v0.1.1 0b1eb60 && git
  push origin v0.1.1` — do NOT tag v0.1.0 at `0260aae` (predates release.yml).
  Tag push is a credential-layer 403 on that seat. *(2026-07-12: the
  release-or-not decision is now ACTIVE at E#45,
  OQ-CFGDIFF-RELEASE-DECISION — these two clicks are the HOW if E#45 = A.)*
- **Paper-doll PNG pack for mining** — art asset, whenever.

### Safe to delete / archive (housekeeping, consolidated 2026-07-10 · 18:31Z wake)

Everything here is verified spent — deleting/archiving loses nothing (all
state is committed in the repos). Do in one sitting whenever convenient.

- **Spent chats (archive in claude.ai):** OLD kit-lab coordinator chat
  (cutover VERIFIED — old trigger deleted, fresh seat live) · dead trading
  gen-1 "ORDER 001 successor" session (= C#19) · wound-down gen-1 lane chats
  generally (succession packages on main; chat context spent by design).
- **Stale branches (agent branch-delete works — 204 via the direct-token path;
  only the proxied path 403s — so these are agent-doable now, not owner-only):** codetool ×2 —
  `claude/status-heartbeat-001` (opus4.8), `test/push-check` (sonnet5) ·
  superbot-games ×2 — `mining/adopt-substrate-kit` (closed-unmerged-deliberate)
  and `mining/grid-encounters` (**verify tip is merged before deleting**) ·
  websites ×4 (= B#11).
- **fleet-manager stale branch (agent branch-delete works — 204 via the direct-token
  path; only the proxied path 403s — agent-doable now, not owner-only):**
  `claude/consolidation-plan-v34` @ 30a48fa — accidental resurrection of PR
  #122's merged head during a parallel merge-back; nothing unique on it (its
  content landed via #122's merge commit fda3182/8f92faa).
- **NOT yet safe:** codetool repo archive toggles ×3 (paired decision above);
  anything holding an open READY PR.

## Resolved 2026-07-11 (earlier — ORDER 010 relay slice)

- **Item 0 (Idea Engine Project):** seat heartbeat/repo trace landed —
  idea-engine `control/status.md` @ `835b260`, phase STEADY; roster gen #4 row
  (fm PR #59, merge `b0639a9`): failsafe `0 */2` armed, chain HOT. Retired per
  the item's own retire condition.
- **Item 9 (product-forge repo + Project), halves 1+2 — overtaken by events:**
  repo exists with the deploy workflow on main (forge PR #13, HEAD `6f5cfad`);
  seat booted and heartbeating (`control/status.md` @ `77f5231`, continuous
  mode + failsafe `0 */2`). Residue: the settings sub-click (now B#9) and
  Pages (now D#26).
- **sim-lab OA-002 (Codex integration):** Codex environments exist for ALL 12
  active fleet repos (owner update 2026-07-11 ~00:2xZ, inbox ORDER 014). Quota
  refusals are RETRY-LATER, never a wall.
  - *Reconciliation (2026-07-14, Slice 0 item 6 / INC-04 — the fm↔sim-lab
    state fork):* the two repos conflated **integration-ENABLED** (done —
    the resolution above stands) with **usage-QUOTA-capped** (still real:
    sim-lab `control/status.md` holds ⚑ OA-002 open with 6+ @codex questions
    pending on quota flaps). Split verdict: enabled = RESOLVED here;
    quota-throughput = OPEN, tracked sim-lab-side (its ledger is the write
    surface) + the flapping evidence at `OQ-CODEX-FLAPPING`. Cross-link:
    sim-lab inconsistency 4.
- **fleet-manager Codex env ask (PR #26):** resolved by the same fleet-wide
  enablement; @codex now PRIMARY on this repo's review-queue rows.
- **Games mapping item 14, Seat B repo-creation click — DONE:**
  `menno420/superbot-idle` exists (public, seeded, pushed
  2026-07-11T00:15:40Z) — the react-by-action on the §5.3 name; remaining veto
  window is E#29.

## Resolved 2026-07-10 (later additions)

- **trading-strategy PR #37 (final P5 holdout report) — MERGED by the owner
  2026-07-10T20:56:34Z** (merged_by menno420, API-verified). Program terminal
  state is ON MAIN: holdout SPENT, report FINAL, 0/13 clears significance.

## Resolved 2026-07-10 (Q-0262 owner-rulings batch, reconciled by the 18:31Z wake)

The owner answered the round-3 decision sheet wholesale (superbot router
Q-0262; routed as inbox ORDER 008 + lane orders):

- **kit F-5 ruling = Reading A** (Q-0262.1) — kit ORDER 011, executed (kit
  #127/#128; headline 1 PASS / 3 FAIL; B1 run-5 unblocked).
- **trading P5 holdout unlock = GRANTED** (Q-0262.2) — trading ORDER 008
  @ `fd5e9fe`; executed; terminal report merged (see above).
- **superbot-next flag-13 disposition = ACCEPTED** (Q-0262.3) — next ORDER
  009, applied in next #105.
- **Core seat 6 = the superbot hub Project** (policy 4) — owner may veto.
- **pokemon concept = QoL+** (Q-0262.7) — effective when the games program
  boots post-core (it since booted; QoL+ is the live concept).
- **The 8 undeployed instruction packages stay undeployed** until the gen-3
  blueprint delta lands, then re-base + deploy in one sitting (policy 3 —
  doctrine at blueprint §4; the deploy sitting is now C#15, held on B#13).
- Fleet policies folded into doctrine same day (fm PR #33): family-level model
  names ONLY (blueprint §1); kit OWNER-ACTION grammar wins by definition
  (playbook R17 rider).

## Resolved since the last rewrite (2026-07-09 → 2026-07-10 morning)

- **🚨→✅ pokemon-mod-lab flipped to PRIVATE** (URGENT item, night-review Q16)
  — done by the owner, re-verified via API; the account-wide visibility review
  moved to Parked.
- Fleet environments created — gen-2 lanes booted in them overnight.
- venture-lab + game-lab launch click-lists executed; gen-1 wind-down pasted
  and completed fleet-wide.
- Merge session done: kit #26 + #49 MERGED ~00:10Z, games #5 MERGED 00:00:58Z.
- Gen-1 wind-down prompt, external ChatGPT campaign, and Anthropic-email items
  consolidated (campaign closed with gen-1; email pack parked above).
