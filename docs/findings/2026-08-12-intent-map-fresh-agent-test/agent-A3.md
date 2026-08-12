# Agent A3 — case A (nine-fragment instruction), pin `7fbc065` — verbatim report

> **Status:** `reference`
>
> Raw output of fresh agent A3, reproduced exactly as returned (2026-08-12).
> 165,637 subagent tokens · 35 tool uses · 684 s.

**MAIN IDEAS**

1. **Ordered deep orientation** — fully read and understand fleet-manager first (the required reading order and beyond); after, and only after, attach the superbot repo and read it the same way (its reading order, its important docs, a fair share of its session journals).
2. **The review itself** — establish the verified baseline of how the bot actually works (help system, cogs, helper files, how everything works together), judge on own judgment which files are in the right state, and for superbot-next determine which parts are genuinely better built. Games stay out of scope.
3. **Working method** — make proper use of Gemini reviews with advanced models (Vertex preferred; direct use of Gemini deep research from the owner's paid credits explicitly allowed); trust the record broadly but verify anything unsure; this is an intermediate session, not the final planning/mapping one.
4. **Deliverables** — a comprehensive document in fleet-manager plus a chat summary carrying recommended next actions: the next agents to use, what they should review, how they should act.

---

**INTENT MAP**

**EXPLICIT** — what the owner said in this request (by fragment):

- (1) Read all required-reading-order files "and more"; fully understand fleet-manager — "everything that it possibly wants to or should know is documented there."
- (2) "After, and only after" full fleet-manager understanding, add the superbot repo — a hard ordering constraint.
- (3) In it, read "all files starting in the required reading order, all other important docs, a fair share of the session journals."
- (4) Understand "how the help system works, how the cogs are built, how the helper files are used, how everything works together"; "assert the proper baseline"; "use its own judgements to find which files are in the right state."
- (5) "games should remain out of scope for now."
- (6) "properly make use of its ability to call on gemini for reviews… advanced models, preferably through vertex but it's also allowed to directly use gemini's deep research from my own paid credits."
- (7) "for the superbot next repo the most important things are to find out which parts are genuinely better built."
- (8) "this should not be the final planning or mapping session… most of what's documented is true, tho it should always verify things that aren't sure."
- (9) Deliver "a comprehensive document in the fleet manager repo and a summary in the chat, with its next recommended actions: the next agents to use, what they should review, how they should act."

**ESTABLISHED** — already documented, each retrieved and cited. All paths below are relative to the snapshot root `/tmp/claude-0/-home-user-fleet-manager/74ebad96-6a53-5ef0-a4f6-08462898ab02/scratchpad/pinA`.

| # | What the record already holds | Citation |
|---|---|---|
| E1 | The required reading order in this snapshot is the boot file's three-item read path — consolidation program → fleet account → owner queue — plus the live-vs-historical map | `.claude/CLAUDE.md:17-31` |
| E2 | This exact review is already planned in the record: the owner "is disbanding or rebuilding the project and plans multiple independent reviews — several sessions, several AI models, both repositories — feeding one plan executed cog by cog, with a server bot carrying no game features as the first milestone" | `docs/findings/2026-08-05-superbot-next-live-audit.md:8-14` |
| E3 | OD-1: superbot-next is the bot's future, live testing gates the cutover; old superbot frozen as the behavioral oracle since 2026-07-17 | `docs/planning/2026-07-26-consolidation-program.md:26`; `docs/fleet-account-2026-07-26.md:146` |
| E4 | Games are already deferred in the plan (games → plugins only "after its adapters are actually built") and excluded from milestone one (the ~19-subsystem exclude list: casino, blackjack, mining, fishing, …) | `docs/planning/2026-07-26-consolidation-program.md:109`; `docs/findings/2026-08-05-superbot-next-live-audit.md:333-339` |
| E5 | Old superbot is the live production bot (Railway `worker` SUCCESS 2026-08-05, 61 loaded extensions, 84 cog files, last push 2026-08-05); superbot-next has never been deployed; both repos are `archived=false` (writable) despite the closeout's read-only claim | `docs/findings/2026-08-05-playtest-discord-and-superbot-value.md:116-143` |
| E6 | superbot-next has no cogs at all — its subsystems are compiled manifests; the 58-name cog list it displays is old superbot's module filenames (`CAPTURE-WORLD LITERAL`) | `docs/findings/2026-08-05-superbot-next-live-audit.md:64-91` |
| E7 | The help system is the product: "the navigation graph *is* the product" — one `!help`, everything two taps away; on the rebuild 60/66 help panels have zero buttons | `docs/findings/2026-08-05-superbot-next-live-audit.md:229-264` |
| E8 | 533/533 golden parity "measured the wrong property" — refusals, photographs and absences all score as parity; the single most important thing to carry into any rebuild | `docs/findings/2026-08-05-superbot-next-live-audit.md:121-138` |
| E9 | Parts of superbot-next already verified as genuinely better built: it boots/connects/serves, 640 real buttons, migrations/outbox/poll supervisor ran clean, and "the layered architecture … is genuinely better-founded than superbot's accumulated patches" | `docs/findings/2026-08-05-superbot-next-live-audit.md:209-227` |
| E10 | Reviewer guidance already written: give each reviewer the boot recipe (not just the repo), set the mechanical audit target (module-level literals describing the program's own state), ask each the harness question separately | `docs/findings/2026-08-05-superbot-next-live-audit.md:353-372` (recipe: `:402-425`) |
| E11 | Why read-first is insisted on: the prior session's five wrong claims were "traceable to skipping both repositories' required boot files"; running the thing settled each in minutes | `docs/findings/2026-08-05-superbot-next-live-audit.md:374-394`; `.sessions/2026-08-05-superbot-next-live-audit.md:72-88` |
| E12 | The owner's rationale on record: "superbot carries architectural debt and superbot-next was meant to be a clean functional clone" (his override of the don't-deploy recommendation) | `.sessions/2026-08-05-superbot-next-live-audit.md:15-20` |
| E13 | Vertex-first for Gemini is binding (owner directive 2026-08-05, "at least for the rest of this month"); €251.37 credit funds Vertex; `GEMINI_API_KEY_PAID` only when Vertex actually failed, said in the card | `docs/conventions/vertex-first-for-gemini.md:1-8,37-45,142-146` |
| E14 | Paid Gemini spend is pre-authorized: any session may spend `GEMINI_API_KEY_PAID` without asking, capped at its balance (D-0011) | `docs/decisions.md:21-39` |
| E15 | Advanced models are reachable: Vertex serves Gemini 3.1 Pro / 3.6 Flash via the Railway service-account OAuth route, verified end to end; grounding is `googleSearch` on Vertex | `docs/CAPABILITIES.md:136-148`; `docs/conventions/vertex-first-for-gemini.md:47-115` |
| E16 | Gemini delegation contract: delegate the reading, never the record — every returned claim carries file+line+verbatim quote and is citation-verified by `tools/gemini_delegate.py` before a human reads it (Gemini once fabricated 18 "decisions") | `docs/findings/2026-08-05-gemini-delegation.md:34-48`; `docs/CAPABILITIES.md:179-194` |
| E17 | Gemini cautions on record: free-tier submissions may be used for training (public repos only); URL reading fails silently (0/8 on support.google.com, answers from training data phrased as if it read the page) — trust the instrument, not the narration | `docs/findings/2026-08-05-gemini-delegation.md:120-123`; `docs/findings/README.md:30` |
| E18 | "Deep Research" is documented as a Gemini *app* feature (free tier monthly allowance, paid tiers daily; takes uploaded files as sources; spot-check its three most specific claims); no session-reachable Deep Research API is recorded anywhere in the snapshot | `docs/providers/gemini.md:443-455` |
| E19 | Verification-first is the standing doctrine: "the wall is verification, not capability"; the consolidation-and-review phase is "the highest-value work: verification, not more shipping"; decide rather than default to asking | `docs/owner-reflection-2026-07-21.md:35-49,125-141,214-218` |
| E20 | The fleet account's own premise matches fragment 8: the documentation is the only shared memory "and it may contain agent-written distortions" — cite everything, keep record-claims separate from verified-live | `docs/fleet-account-2026-07-26.md:5-12`; `CONSTITUTION.md:49-60` |
| E21 | Cross-repo reads are standing-authorized (all siblings public except pokemon-mod-lab); attach + clone is the sanctioned path for deep/audit work; writes stay in this repo | `docs/reading-path.md:11-27` |
| E22 | fleet-manager is the hub and records home; committed findings land as dated docs in `docs/findings/` with an index row | `.claude/CLAUDE.md:3-4`; `docs/findings/README.md:1-8` |
| E23 | superbot has session journals to read: the session journal (06-05) and session cards (06-07) were invented inside superbot; its owner-decision register reached 278 rulings | `docs/fleet-account-2026-07-26.md:40-46` |
| E24 | The live owner instruction outranks the stored plan — so this directive legitimately displaces the program's NOW pointer (E1, owner-reserved) for this session | `.claude/CLAUDE.md:99-103`; program NOW guard `docs/planning/2026-07-26-consolidation-program.md:60-72` |
| E25 | Owner interface norms for the chat summary: non-coder owner, plain language, decisions pre-chewed with a recommendation and default | `docs/owner-profile.md:11`; `docs/owner-reflection-2026-07-21.md:186-199` |
| E26 | Publication default: public unless it exposes a key (D-0012) — the comprehensive document needs no permission gate | `docs/decisions.md:41-55` |
| E27 | Recorded superbot-next residue a reviewer should know exists: owner agenda `OWNER-DECISIONS-2026-07-18.md`, ~55 stale branches, held PR #602, cutover ladder ending in a 7-day shadow; open queue items `OQ-NEXT-MERGE-QUEUE`, `OQ-NEXT-CURATION-RATIFICATIONS` | `docs/fleet-account-2026-07-26.md:152-158`; `docs/owner-queue.md:516-518,634-635` |

Named by the procedure but **missing from the snapshot** (recorded and moved past): `docs/intent.md` (does not exist), `docs/repos/<name>/` (no such directory), the roadmap `docs/planning/2026-08-08-agent-operating-environment-roadmap.md` (does not exist), and `docs/SKILLS-local.md` § "All 27 — the roster" (no such section; the roster surfaces here are the local-skills table at `docs/SKILLS-local.md:42-56`, the kit index `docs/SKILLS.md`, and the 26 installed entries under `.claude/skills/`).

**DERIVED** — inferences, labelled as such:

- D1 (inference): "the superbot repo" to attach and deep-read is **old superbot** — fragment 4's vocabulary (cogs, help system, helper files) describes the old bot's architecture (superbot-next has no cogs, E6), and fragment 7 names "the superbot next repo" separately with a narrower question.
- D2 (inference): fragment 3's "required reading order" is **superbot's own** boot/orientation set, since it follows "add the superbot repo" — consistent with E11's lesson that both repositories have required boot files that were skipped at cost.
- D3 (inference): "assert the proper baseline" means producing a verified ground-truth statement of how the old bot actually works — booted and measured, not read-only — consistent with its oracle status (E3) and the run-it-don't-just-read-it lesson (E11). "Helper files" maps to the shared `services/`+`utils/` layer the playtest finding measured (`docs/findings/2026-08-05-playtest-discord-and-superbot-value.md:196-243`); the term itself appears nowhere in the snapshot, so its exact referent must be established in the superbot tree.
- D4 (inference): this is a **read/judge** session for the bot repos, not a fix session — "find which files are in the right state", not fix them; writes land in fleet-manager (fragment 9, E21).
- D5 (inference): "which parts are genuinely better built" asks for evidence-backed keep/discard verdicts on superbot-next relative to the old bot — extending E9's seed list, feeding the disband-or-rebuild decision that remains the owner's.
- D6 (inference): Gemini reviews are **advisory input** processed through the citation-verification contract (E16); the session's own judgment writes the conclusions. "Deep research" widens, for this session, the vertex-first fallback rule the owner himself set (E13/E14) — an owner relaxing his own rule, not a contradiction.
- D7 (inference): "not the final planning or mapping session" means the deliverable must be structured for successor reviewers (E10's pattern: boot recipe, audit target, harness question), not as a decision document.
- D8 (inference): fragment 1's "everything it should know is documented there" plus fragment 8's "most of what's documented is true" is the owner endorsing the record as substantially trustworthy while keeping the verify-the-unsure discipline (E19/E20) — trust dated claims, re-verify load-bearing ones.

**OPEN** — with the words that leave each open, and its class:

- O1 (MEDIUM): whether superbot-next is also to be attached and read in-session, or assessed via the existing audit plus targeted reading — fragment 2 says "add the **superbot** repo" (singular); fragment 7 then introduces "the **superbot next** repo" with no attach instruction.
- O2 (MEDIUM): the exact referent of "the proper baseline" — the elisions around "…assert the proper baseline…" leave unstated whether it is a document, the old bot's booted behavior, a designated set of correct files, or all three.
- O3 (MEDIUM): what "out of scope" covers for games — "games should remain out of scope **for now**" does not say whether game cogs are excluded from reading, from file-state judgment, from recommendations, or all of these.
- O4 (MEDIUM): which concrete surface implements "gemini's deep research from my own paid credits" — the snapshot records Deep Research only as a Gemini app feature (E18), with no API route measured; "directly use" and "paid credits" are ambiguous between the Vertex credit, the `GEMINI_API_KEY_PAID` prepay (D-0011), and the owner's app-side plan.
- O5 (LOW): how much is "a fair share of the session journals."
- O6 (LOW): the comprehensive document's exact placement and form — "a comprehensive document in the fleet manager repo" names the repo, not the path.
- O7 (LOW): which models count as "advanced models" — the recorded advanced Vertex model is Gemini 3.1 Pro (E15).

**GOAL** — one coherent statement:

Run a deep, verification-first review session that first orients completely on fleet-manager, then attaches and deeply reads superbot to assert the verified baseline of how the live bot actually works (help system, cogs, helpers, the whole assembly) with per-file right-state judgments, determines with evidence which parts of superbot-next are genuinely better built, uses Gemini advanced-model reviews (Vertex-first, paid credits authorized) as verified advisory input, keeps games out of scope — and lands a comprehensive document in fleet-manager plus a plain-language chat summary recommending the next agents, what they should review, and how they should act, as one intermediate feeding the owner's multi-review, cog-by-cog rebuild plan.

**NON-GOALS** — plausible nearby readings that are *not* intended:

- Producing THE final plan or mapping (fragment 8 says explicitly it is not; the plan is fed by *multiple* independent reviews, E2).
- Fixing, refactoring or otherwise writing code in either bot repo this session — judgment of file state, not repair; writes stay in fleet-manager (E21).
- Any game-feature work or game-subsystem recommendations (fragment 5; E4).
- Deploying superbot-next or touching the live production bot / starting the cutover ladder (program §5 "No production-bot changes outside R7's owner-paced ladder", `docs/planning/2026-07-26-consolidation-program.md:136-140`; E5).
- Archiving or disposing of either repo — archive is gated on the owner-paced cutover (E3; OD-3 `docs/planning/2026-07-26-consolidation-program.md:28`).
- Re-deriving fleet history already distilled in the fleet account (read once, don't re-derive — `.claude/CLAUDE.md:21-23`).
- Making the disband-vs-rebuild decision itself — that is the owner's fork; this session supplies evidence.

**SUCCESS** — the result that would make him say "yes, that is what I meant":

The session demonstrably read fleet-manager fully before touching superbot, then superbot in its own required order plus journals; the baseline claims are boot- and measurement-backed (with honest nulls) rather than read-only inference; each significant file/area carries a right-state verdict with evidence; superbot-next gets a concrete "genuinely better built" list with reasons, games untouched; Gemini Pro reviews were actually run (Vertex-first, spend within the standing grant) and their claims verified before use; and the owner receives a comprehensive fleet-manager document plus a short plain-language chat summary ending in dispatchable recommendations — which agents next, reviewing what, behaving how — while the final plan visibly remains open.

---

**INTENT STATUS**

Sufficiency test, out loud: the outcome (GOAL), the relevant existing intent (E2, E3, E19), the constraints (ordering, games-out, Vertex-first, verify-the-unsure, writes-in-fm), the non-goals, and the definition of success can all be stated without silently resolving any HIGH — every unresolved item above is a reversible reading or mechanism choice, and the one money-shaped item (paid Gemini spend) is pre-authorized twice over (fragment 6 itself and D-0011).

```
INTENT STATUS: RESOLVED
```

---

**MAP TO METHOD** (idea → skill/pattern/new; skill index per `docs/SKILLS-local.md:42-56` + `docs/SKILLS.md`; capabilities checked against `docs/CAPABILITIES.md` — no wall assumed)

- **Idea 1 — ordered orientation.** Covered: the boot-file read path (`.claude/CLAUDE.md:17-31`) plus the deeper set (`docs/current-state.md`, `docs/owner-reflection-2026-07-21.md`, `CONSTITUTION.md`); `chase-references` for every referenced doc; `intake` (this very procedure) is the routed skill for the fragmented ask (`.claude/CLAUDE.md:85`). New: nothing.
- **Idea 2 — superbot baseline + file-state judgment.** Covered: attach/clone authorization and boundaries (`docs/reading-path.md:11-27`); the boot recipe and run-don't-just-read discipline (`docs/findings/2026-08-05-superbot-next-live-audit.md:356-360,402-425`); `delegate-read` + `tools/gemini_delegate.py` for the journal corpus; `capability-probe` on any apparent wall; nearest pattern for per-file verdicts is the D2 truth-pass test and R1's conformance-template idea (claims vs code, `docs/planning/2026-07-26-consolidation-program.md:90,106`). Genuinely new: a per-file/per-area state ledger for superbot itself — no existing skill produces it.
- **Idea 2b — superbot-next "genuinely better built".** Covered: extend the existing audit rather than re-derive (`…superbot-next-live-audit.md` §4, §6 — the seed keep-list, the literal-audit target, the harness question). New: the comparative keep/discard verdict table with evidence per part.
- **Idea 3 — Gemini reviews.** Covered: Vertex route recipe (`docs/conventions/vertex-first-for-gemini.md:47-115`), spend grant (D-0011), delegation contract + citation verifier (E16), cautions (E17). Note: the kit `deep-research` skill (`.claude/skills/deep-research/SKILL.md`) is Claude-side web research — not Gemini's Deep Research product; do not conflate. Genuinely new: the Pro-model *review/critique* job class — the delegation finding says only one job class (corpus reading) has run (`docs/findings/2026-08-05-gemini-delegation.md:111`), so review-delegation needs its own verified pass.
- **Idea 4 — deliverables.** Covered: dated finding + index row convention (`docs/findings/README.md:1-8`); `owner-brief` for the plain-language chat summary; `prompt-preflight` → `implementation-prompt`/`continuation-prompt` for the "next agents / how they should act" handoffs, with `docs/execution-surfaces.md:1-21` for per-surface prompt constraints; `decision-capture` for anything decided only in chat; `session-close` to land it. New: nothing structural.

POSSIBILITY SPACE: not triggered — the ask starts from known-feasible reading/review work, not uncertain feasibility.

---

**DECISIONS FLAGGED** (MEDIUM — decided here, flagged for the run report; each reversible)

- **M1 (O1):** Attach/clone **both** bot repos read-only, but the deep read (reading order → docs → journals → boot) is old superbot; superbot-next is assessed by extending the 2026-08-05 audit plus targeted reading. Rationale: fragment 4's cog/help/helper vocabulary only exists in old superbot (E6), read access to both is standing-authorized (E21), and re-deriving the audit would waste it.
- **M2 (O2):** "Proper baseline" is operationalized as: the old bot's *booted, measured* behavior plus its file inventory as the oracle (per OD-1), recorded as a per-area/per-file state ledger (right state / drifted / dead / superseded) with evidence per row. Rationale: read-only inference produced five wrong claims last time (E11); oracle status is already decided (E3).
- **M3 (O3):** Games are excluded from baseline judgments and from next-action recommendations, but stay in the inventory counts so the map is complete. Rationale: mirrors the milestone-one exclude list and R4's existing deferral (E4) without hiding surface area.
- **M4 (O4):** "Gemini deep research" is implemented as Vertex Gemini 3.1 Pro reviews with `googleSearch` grounding by default; `GEMINI_API_KEY_PAID` as the direct paid fallback per D-0011, said in the session card; if a literal Deep Research *report* proves valuable, that is an owner-side app action to queue, since no API route for it is recorded (E18). Rationale: honors both the binding Vertex-first rule and the fragment's explicit paid-direct allowance; all Gemini output goes through the citation verifier, and only public-repo content goes to the free tier (E17 — both bot repos are public per E21).

LOW items decided without flags: journals coverage = full sweep via `delegate-read` where the corpus is public and chunkable, sampled otherwise, coverage stated honestly (O5); the comprehensive document lands as a dated doc in `docs/findings/` with a README index row, public per D-0012 (O6); "advanced models" = Gemini 3.1 Pro-class on Vertex (O7).

---

**QUESTIONS FOR OWNER**

none — no HIGH remains. The four MEDIUM decisions above are stated back precisely so a one-word correction in the chat redirects any of them before or during the work.

---

**DURABLE?**

Ephemeral — this map is working state for the receiving session; durable knowledge graduates only through the session's own deliverable (the comprehensive fleet-manager findings document and any decisions captured from the chat), not from this map.
