# Agent A1 — case A (nine-fragment instruction), pin `7fbc065` — verbatim report

> **Status:** `reference`
>
> Raw output of fresh agent A1, reproduced exactly as returned (2026-08-12).
> 150,184 subagent tokens · 32 tool uses · 551 s.

MAIN IDEAS

1. **Sequenced baseline read.** Orient fully on fleet-manager first (required reading order "and more"), and only then attach the old `superbot` repo and deep-read it — reading order, important docs, a fair share of the session journals — to understand how the bot works as a system (help system, cogs, helper files, the whole) and to judge, on own judgement, which files are in the right state: "assert the proper baseline."
2. **superbot-next verdict.** For the rebuild repo, the priority is identifying which parts are *genuinely* better built (vs. captured/photographed), with games out of scope for now.
3. **Method + deliverable.** Use Gemini for reviews (advanced models, Vertex-preferred, deep research on the owner's paid credits allowed); trust the record mostly but verify what isn't sure; land a comprehensive document in fleet-manager plus a chat summary ending in routed next actions (which agents next, what they review, how they act) — explicitly not the final planning/mapping session.

INTENT MAP

**EXPLICIT** — what the owner said in this request (nine fragments):
- Read all required-reading-order files "and more"; fully understand fleet-manager; "everything that it possibly wants to or should know is documented there" (f1).
- "After, and only after" full fleet-manager understanding, add the superbot repo (f2).
- Read superbot's files "starting in the required reading order, all other important docs, a fair share of the session journals" (f3).
- Understand "how the help system works, how the cogs are built, how the helper files are used, how everything works together"; "assert the proper baseline"; "use its own judgements to find which files are in the right state" (f4).
- "games should remain out of scope for now" (f5).
- "properly make use of its ability to call on gemini for reviews… advanced models, preferably through vertex but it's also allowed to directly use gemini's deep research from my own paid credits" (f6).
- "for the superbot next repo the most important things are to find out which parts are genuinely better built" (f7).
- "this should not be the final planning or mapping session… most of what's documented is true, tho it should always verify things that aren't sure" (f8).
- Deliverables: "a comprehensive document in the fleet manager repo and a summary in the chat, with its next recommended actions: the next agents to use, what they should review, how they should act" (f9).

**ESTABLISHED** — already documented (citations relative to the snapshot root `/tmp/claude-0/-home-user-fleet-manager/74ebad96-6a53-5ef0-a4f6-08462898ab02/scratchpad/pinA`):
- Two bot repos with fixed roles: `superbot-next` is the bot's future, live testing gates cutover; old `superbot` frozen as **behavioral oracle** since 2026-07-17 — `docs/planning/2026-07-26-consolidation-program.md:26` (OD-1); one-bot-one-repo target `:44`; bot consolidation R4 `:109`, owner-paced cutover ladder R7 `:112`.
- The owner's current bot plan, written 2026-08-05: he "is disbanding or rebuilding the project and plans multiple independent reviews — several sessions, several AI models, both repositories — feeding one plan executed cog by cog, with a server bot carrying no game features as the first milestone" — `docs/findings/2026-08-05-superbot-next-live-audit.md:8-14`. This instruction is one of those reviews.
- Games exclusion is already scoped: milestone one ≈ 15 operator-spine subsystems; ~19 game subsystems excluded — same doc `:316-351` (§5); game surface ≈25 of 61 loaded extensions is "noise" for a QA server — `docs/findings/2026-08-05-playtest-discord-and-superbot-value.md:171-180`.
- "Genuinely better built" has a seeded answer and a defined test: what holds up (layered architecture "genuinely better-founded", 640 real buttons/161 panels, clean migrations/outbox/poll supervisor) — audit `:209-227` (§4); the defect class to test against is `CAPTURE-WORLD LITERAL` / "static data presented as live system state" `:44-115` (§1); golden parity cannot see refusals, photographs, absences `:119-138` (§2); the navigation graph is the product and 60/66 help panels have zero buttons `:229-314` (§4b).
- The read-the-boot-files-first discipline responds to a recorded failure: "this session read the code and skipped both repositories' required boot files," producing five wrong claims the owner caught — audit `:374-394` (§7). Reviewer protocol already written: boot recipe, audit target, harness question — `:353-372` (§6), recipe `:402-425` (§8).
- fleet-manager's required reading order exists: `.claude/CLAUDE.md:17-25` (program → fleet account → owner queue), live-vs-historical map `:27-31`; `docs/AGENT_ORIENTATION.md:8-12` (CLAUDE.md → current-state → orientation router); `docs/current-state.md:213-218` ("read this if you read nothing else": the owner reflection).
- Cross-repo reading/attaching is standing-authorized: `docs/reading-path.md:11-27` (§0; "attach + clone remains the path for deep/audit work in a sibling"); `docs/CAPABILITIES.md:879-887` ("Nothing restricts a session to the repo it was launched for"; raw reads need no `add_repo`). Dated wall applies only to *wake* sessions (`docs/CAPABILITIES.md:695-700`).
- superbot ground facts on record: live in production (Railway `reliable-grace`/`worker`, SUCCESS 2026-08-05), 61 loaded extensions (`disbot/config.py:111`), 84 cog files; superbot-next never deployed — `docs/findings/2026-08-05-playtest-discord-and-superbot-value.md:116-129`; both repos `archived=false` (writable; the closeout's "permanently read-only" is wrong) `:135-143`; cog routing built-but-never-enforced in both `:196-229`; session journals/cards were invented in superbot (06-05/06-07) — `docs/fleet-account-2026-07-26.md:40-46`; its key orientation docs named at `:23-26` (`docs/owner/maintainer-question-router.md`, `docs/owner/fleet-grounding.md`, `docs/current-state.md`).
- Gemini method is already decided: **Vertex-first is a binding owner directive** (2026-08-05, "at least this month") — `docs/conventions/vertex-first-for-gemini.md:3-8`, rule + paid-key fallback stated in the card `:37-45`, verified route `:47-115`; **paid key free to spend, capped at its balance, "Pro-model review" a named use** — `docs/decisions.md:21-39` (D-0011); delegation contract (every claim file+line+verbatim quote, tree-verified) — `docs/findings/2026-08-05-gemini-delegation.md:34-48`; free tier 250k tokens/min, `gemini-3.1-pro-preview` paid-quota-only `:18-24`; Deep Research documented only as a Gemini *app* feature (free/paid app tiers) — `docs/providers/gemini.md:443-455`; grounded-call instrument discipline — `docs/findings/README.md:30` (URL-accuracy benchmark row).
- "Verify what isn't sure" is standing doctrine: "A record is a claim; the live surface is the proof" — `CONSTITUTION.md:49-60`; the doc corpus "may contain agent-written distortions" — `docs/fleet-account-2026-07-26.md:8-12`; verification, not more shipping, is the highest-value work — `docs/owner-reflection-2026-07-21.md:215-218, 227-230`.
- "Use its own judgements" is a standing instruction: decide, don't default to asking; infer unstated intent — `docs/owner-reflection-2026-07-21.md:125-139`; decide-and-flag rails — `CONSTITUTION.md:63-98`.
- Deliverable home + defaults: fleet-manager is the records home — `README.md:3-6`; dated findings docs are the convention "so nothing lives only in an archivable chat" — `docs/findings/README.md:1-8`; publish by default, credentials never — `docs/decisions.md:41-55` (D-0012); understand-and-reflect (fragments, not specs) — `CONSTITUTION.md:18-23`.
- **Named-but-missing in this snapshot** (recorded per procedure): `docs/intent.md` — does not exist; `docs/repos/<name>/` — does not exist; the 2026-08-08 roadmap the procedure cites — does not exist (`docs/planning/` ends at 2026-07-26); `docs/SKILLS-local.md` has no "All 27 — the roster" section (it lists 13 local skills; `docs/SKILLS.md` carries the kit rows; the installed `.claude/skills/` tree holds 27).

**DERIVED** — inferences, labelled as such:
- "The superbot repo" (f2) = old `menno420/superbot`; f3–f4's vocabulary (cogs, help system, session journals) is old-bot architecture, and OD-1 makes it the oracle. superbot-next is also in scope but via f7's narrower question, seeded by the existing 08-05 audit rather than a second read-everything pass. (Inference from wording, position, OD-1.)
- f3's reading list applies to superbot, not fleet-manager — it sits between "add the superbot repo" (f2) and old-bot internals (f4). (Positional inference; the elisions could hide a connective.)
- "Assert the proper baseline" = pin ground truth against which the rebuild is judged: the live oracle's actual behavior and as-used UX (navigation-first, `!help` two-taps — audit §4b), plus which repo files/docs truthfully describe it. (Inference from OD-1 + audit purpose.)
- "Helper files" = superbot's shared modules (`services/`, `utils/` — e.g. `services/command_routing.py`, `utils/db/command_access.py`, the only helper-file examples the snapshot cites, in the playtest finding §4). The term is defined nowhere in the snapshot. (Inference.)
- "Advanced models" = Pro-class Gemini (the Vertex recipe's example is `gemini-3.1-pro-preview`; the free delegation path runs Flash). (Inference from vertex doc + delegation finding.)
- "My own paid credits" = the two funded pools on record: the €251.37 Vertex prepaid credit and/or the D-0011 €10 paid-key balance. (Inference; the fragment doesn't name a pool.)
- The comprehensive document lands as a dated `docs/findings/` reference doc via a normal born-red PR; "next agents" recommendations cover both next Claude sessions (with prompts) and the other-model reviews the owner planned. (Inference from conventions + audit purpose.)
- Posture toward both bot repos this session is find-not-fix: writes land in fleet-manager only; booting/driving the bots per the audit's §8 recipe is measurement, not modification. (Inference from f8 "not the final planning or mapping session" + the deliverable being a document.)

**OPEN** — outcome-changing questions the words leave open:
- O1 (MEDIUM): Depth split across the two repos — f2 says "add the superbot repo" (singular); f7 addresses "the superbot next repo" separately. Whether f3's full reading program (journals and all) also applies to superbot-next is unresolved; f3's ellipsis may have elided it.
- O2 (LOW): "a fair share of the session journals" — "a fair share" quantifies nothing.
- O3 (MEDIUM): "directly use gemini's deep research from my own paid credits" — no route named; the snapshot documents Deep Research only as a Gemini-app feature (`docs/providers/gemini.md:443-446`), with no API recipe on record, and two distinct paid pools exist.
- O4 (LOW→MEDIUM): "games should remain out of scope for now" — out of scope for the rebuild plan only, or also for this session's review depth? "for now" scopes time, not the boundary.
- O5 (MEDIUM): "which files are in the right state" — right relative to what: the live deployed bot, the documented claims, or the rebuild's needs? The phrase does not say.

**GOAL** — After orienting on fleet-manager in its required order, produce a verified baseline of the superbot estate — how the old bot genuinely works as a system (help/navigation, cogs, helpers, the whole), which of its files are in the right state, and which parts of superbot-next are genuinely better built (games excluded) — checking uncertain claims and reviewing the work with advanced Gemini models Vertex-first, then land a comprehensive document in fleet-manager plus a chat summary that routes the next reviews (which agents, what they review, how they act), as one early pass in the owner's multi-review rebuild program.

**NON-GOALS** — plausible nearby readings not intended:
- Producing the final rebuild plan or architecture decision (f8 excludes it explicitly).
- Building or fixing anything in either bot repo: no cog rework, no cutover steps (R7), no deploying superbot-next (`docs/findings/2026-08-05-playtest-discord-and-superbot-value.md:267-271` — "Do not deploy superbot-next"), no production-bot changes.
- Reviewing or planning game features (f5).
- Re-deriving history the record already distils, or re-verifying everything — "most of what's documented is true"; verify the unsure only (f8; `.claude/CLAUDE.md:22-23`).
- Blocking on the owner: judgement calls are the session's (owner-reflection standing instruction).
- Letting Gemini write the record: it reviews and reads; claims return citation-verified; the session authors the document (delegation contract).

**SUCCESS** — The owner returns to find the session demonstrably oriented in order (fleet-manager first, then superbot from its own reading order and journals); a comprehensive fleet-manager document asserting the baseline — how the bot works, which files are in the right state with each judgement grounded and uncertain claims verified or honestly marked, and which superbot-next parts are genuinely better built versus photographed; evidence that advanced-model Gemini review via Vertex was actually used; and a short chat summary ending in concrete next steps — which agents next, what each reviews, how each should act — with games untouched and no premature final plan. The test: he says "yes, that is the baseline; the next sessions can start from it."

INTENT STATUS: RESOLVED

Sufficiency test, out loud: the outcome, the relevant existing intent (OD-1, the 2026-08-05 rebuild-review program, server-first milestone), the constraints (order, games out, Vertex-first, verify-the-unsure), the non-goals, and the success definition are all statable from the record above; the five unresolved items are effort-allocation or route choices, reversible and flagged — none changes product intent, scope-as-stated, ownership, irreversibility, or the definition of success, so no HIGH is being silently resolved.

MAP TO METHOD

(Note: the procedure's index citation — `docs/SKILLS-local.md` § "All 27 — the roster" — does not exist in this snapshot; mapping uses the snapshot's `docs/SKILLS.md` table, `docs/SKILLS-local.md` local table, and the installed `.claude/skills/` tree of 27.)

- **Idea 1 — ordered orientation + superbot deep read:** covered by the boot read path (`.claude/CLAUDE.md:17-31`; `docs/AGENT_ORIENTATION.md:8-12`), cross-repo attach/clone authorization (`docs/reading-path.md:11-27`; `docs/CAPABILITIES.md:879-887`), `chase-references` (resolve every named file before acting), `analysis` (read-only deep-dive stance, `docs/SKILLS.md:31`), and `delegate-read` for the journal corpus (`docs/SKILLS-local.md:55`; contract in `docs/findings/2026-08-05-gemini-delegation.md`). Genuinely new: superbot's own required reading order lives inside that repo, not in this snapshot — discover it at attach time (entry pointers: `docs/fleet-account-2026-07-26.md:23-26`).
- **Idea 2 — superbot-next better-built verdict:** covered by the audit's own reviewer protocol — boot recipe (§8), explicit audit target ("every module-level literal in `sb/domain/` that should be a runtime read"), and the harness question (§6) — plus the static-vs-live test (§1) and the reachability test (§4b), all in `docs/findings/2026-08-05-superbot-next-live-audit.md`; `capability-probe` before declaring any wall (`CONSTITUTION.md:24-27`). Partly new: a per-part "genuinely better built" verdict format — §4's keep-list is the seed, no existing checklist.
- **Idea 3 — Gemini reviews:** covered by `docs/conventions/vertex-first-for-gemini.md` (binding route + verified recipe), D-0011 (`docs/decisions.md:21-39`, spend pre-authorized), `delegate-read`/`tools/gemini_delegate.py` (citation-verified delegation), and the instrument discipline from the URL-accuracy benchmark (`docs/findings/README.md:30`). New: no in-snapshot API recipe for Gemini's Deep Research product (`docs/providers/gemini.md:443-455` documents an app feature) — see M2.
- **Idea 4 — deliverable + routing:** covered by the `docs/findings/` dated-doc convention (`docs/findings/README.md:1-8`) landed with kit discipline (`session-close`; `python3 bootstrap.py check --strict`), `owner-brief` for the chat summary (`docs/SKILLS-local.md:56`), `prompt-preflight` + `implementation-prompt`/`continuation-prompt` for the next-agent prompts (`docs/SKILLS-local.md:44-46`), and `decision-capture` for any decisions born in-session. This intake itself: `docs/SKILLS.md:25`.

DECISIONS FLAGGED

- **M1 (O1) — depth split:** deep-read old `superbot`; give superbot-next the targeted better-built assessment seeded by the 08-05 audit, not a second full read. Rationale: f3–f4 use old-bot vocabulary and OD-1 makes the old bot the oracle; widen later if the read exposes gaps.
- **M2 (O3) — "deep research" route:** default to Vertex Pro + `googleSearch` grounding as the working equivalent; capability-probe for a Deep Research API before recording any wall; paid key only where Vertex fails, stated in the session card. Rationale: Vertex-first is binding and D-0011 pre-authorizes the spend, so no owner ask is needed on either branch.
- **M3 (O4) — game depth:** catalogue game subsystems (names, counts, state) but do not review them in depth. Rationale: milestone one excludes them and "for now" defers rather than deletes — an inventory keeps the door open.
- **M4 (O5) — "right state" referent:** judge files against the live behavioral oracle plus the honest-docs bar (a file is in the right state when it truthfully describes or serves the running bot). Rationale: OD-1 and the source-wins doctrine already fix truth's reference point.
- (LOW, decided without flag: journal coverage = stratified sample across eras plus a delegated full sweep; the comprehensive document lands as a dated `docs/findings/` doc.)

QUESTIONS FOR OWNER

none — no OPEN item is HIGH. The four MEDIUM decisions above ride the run report as vetoable flags; were any to harden into a genuine fork mid-session, it would be appended to `docs/question-router.md` as a structured A/B choice while work continues.

DURABLE?

Ephemeral — this map is working state; the durable outputs are the session's own deliverable document (f9) and any decisions it produces, which graduate via `decision-capture`, not this map.
