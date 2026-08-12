# Agent A2 — case A (nine-fragment instruction), pin `7fbc065` — verbatim report

> **Status:** `reference`
>
> Raw output of fresh agent A2, reproduced exactly as returned (2026-08-12).
> 134,415 subagent tokens · 32 tool uses · 620 s. The agent's one line of
> preamble is preserved as returned.

All retrieval done — I have verified citations for every fragment against the snapshot. Producing the intent map.

MAIN IDEAS

1. **Orient in depth, in strict order** — fully absorb fleet-manager through its required reading order (and beyond) first; only then attach the superbot repo and absorb it the same way: its reading order, its important docs, a fair share of its session journals, down to how the help system, cogs, and helper files work together.
2. **Dual-repo bot assessment feeding the rebuild plan** — assert old superbot's proper baseline (own-judgement, file-level "right state" calls, games excluded for now) and, for superbot-next, determine which parts are genuinely better built; use Gemini advanced-model reviews (Vertex-first, deep-research-on-paid-credits allowed) and verify anything unsure.
3. **An intermediate deliverable with routing** — a comprehensive committed document in fleet-manager plus a plain-language chat summary, ending in next recommended actions: which agents next, what they should review, how they should act. Explicitly not the final planning/mapping session.

INTENT MAP

**EXPLICIT** — what the owner said in this request:
- Read all required-reading-order files "and more"; fully understand fleet-manager; he asserts everything the session should know "is documented there" (frag 1).
- Hard sequencing: add the superbot repo "after, and only after" fleet-manager is fully read and understood (frag 2).
- In superbot: reading order first, then all other important docs, then "a fair share of the session journals" (frag 3).
- Understand the help system, how the cogs are built, how the helper files are used, how everything works together; "assert the proper baseline"; use its own judgement on which files are in the right state (frag 4).
- Games out of scope "for now" (frag 5).
- Use Gemini for reviews with advanced models — "preferably through vertex", but direct use of "gemini's deep research from my own paid credits" is also allowed (frag 6).
- For the superbot-next repo, the most important thing: find which parts are "genuinely better built" (frag 7).
- Not the final planning or mapping session; most documentation is true, but always verify what isn't sure (frag 8).
- Deliverable: a comprehensive document in the fleet-manager repo + a chat summary, with next recommended actions — the next agents to use, what they should review, how they should act (frag 9).

**ESTABLISHED** — already documented in the snapshot (all citations verified by reading):

| # | What the record already holds | Citation (snapshot paths under `…/scratchpad/pinA/`) |
|---|---|---|
| E1 | The rebuild-review frame this instruction executes: owner "is disbanding or rebuilding the project and plans multiple independent reviews — several sessions, several AI models, both repositories — feeding one plan executed cog by cog, with a server bot carrying no game features as the first milestone" | `docs/findings/2026-08-05-superbot-next-live-audit.md` lines 8–14; same phrasing in the index row, `docs/findings/README.md` line 33 |
| E2 | Prior standing directive OD-1: "superbot-next is the bot's future; live testing gates the cutover. Old superbot is already frozen as the behavioral oracle (recorded 2026-07-17)" — now in tension with E1; the live owner outranks stored text | `docs/planning/2026-07-26-consolidation-program.md` line 26; precedence rule `.claude/CLAUDE.md` lines 99–103 |
| E3 | superbot: "FROZEN as behavioral oracle 2026-07-17 — 'no new feature work'; production bot stable on Railway"; superbot is deployed and live now (`reliable-grace`/`worker` SUCCESS 2026-08-05); superbot-next "has never been deployed"; both repos are writable (`archived=false`) despite the closeout's read-only claim | `docs/fleet-account-2026-07-26.md` line 146; `docs/findings/2026-08-05-playtest-discord-and-superbot-value.md` lines 125–143 |
| E4 | Games-out is already the recorded first milestone: "The stated first goal is a bot that runs a server with no game features" — keep ≈15 operator-spine subsystems, exclude ≈19 game subsystems; playtest doc's Tier-3 "noise" list matches | audit `§5`, lines 316–351; playtest doc lines 172–176 |
| E5 | What is already measured as genuinely better in superbot-next: boots/connects/serves (1,327 dispatch targets, 640 real buttons/161 panels), migrations/outbox/poll-supervisor clean, and "the layered architecture … is genuinely better-founded than superbot's accumulated patches" | audit `§4`, lines 209–227; `§3` table lines 144–161 |
| E6 | What is already measured as photographed, not working: the `CAPTURE-WORLD LITERAL` convention (4 labelled files; Cog Manager's 58 hardcoded module names); 533/533 golden parity certified refusals/photographs/absences; the help tree is 60/66 zero-button panels — "the navigation graph is the product, and it was not ported"; owner quote "the only command anyone ever needs is `!help`… always 2 taps away" | audit `§1` lines 44–58, `§2` lines 120–138, `§4b` lines 229–314 (owner quote 238–241) |
| E7 | Reviewer-handoff method already written: give each reviewer the boot recipe (not just the repo), set the audit target explicitly (module-level literals in `sb/domain/` that should be runtime reads), ask each the harness question ("what would this test suite fail to notice?"); reproduction recipe ~5 min | audit `§6` lines 353–372, `§8` lines 402–425 |
| E8 | Why "read then verify" is the standing lesson: the audit session's five wrong claims all traced to "read the code and skipped both repositories' required boot files"; correction: "run it, and see whether anything happens"; owner had overridden a prior anti-superbot-next recommendation with a reason (superbot carries architectural debt; superbot-next was meant as a clean functional clone) | audit `§7` lines 374–400; `.sessions/2026-08-05-superbot-next-live-audit.md` lines 15–20, 74–88 |
| E9 | Vertex-first is a binding owner directive (2026-08-05, "at least for the rest of this month"): default Vertex; paid key "only when Vertex has actually failed… say so in the session card"; full verified recipe (Railway → SA JSON → OAuth → `aiplatform.googleapis.com`, `googleSearch` camelCase); example call is `gemini-3.1-pro-preview` | `docs/conventions/vertex-first-for-gemini.md` lines 3–8, 39–45, 47–115, 142–146; `.claude/CLAUDE.md` lines 56–63 |
| E10 | D-0011: the paid Gemini key is "free for sessions to spend" without asking, capped at its €10 prepaid balance (auto-reload off); D-0012: publish by default, credentials never | `docs/decisions.md` lines 21–39, 41–55 |
| E11 | "Advanced models" access: `gemini-3.1-pro-preview` 429s on the free key ("paid quota only"); free tier is 250k input tokens/min — corpus reads must chunk; delegation contract: "delegate the reading, never the record", every claim citation-verified file+line+quote; free-tier submissions may train → public repos only (both bot repos are public; only pokemon-mod-lab is private) | `docs/findings/2026-08-05-gemini-delegation.md` lines 18–48, 120–122; `docs/reading-path.md` line 17 |
| E12 | "Deep Research" is documented only as a Gemini-app feature (tier allowances; takes uploaded files as sources); no API recipe for it exists anywhere in the snapshot | `docs/providers/gemini.md` lines 443–455 |
| E13 | Fleet-manager's required reading order at this moment: `.claude/CLAUDE.md` read path (program → fleet-account → owner-queue) + live-vs-historical map; plus current-state's "Read this if you read nothing else" → `owner-reflection-2026-07-21.md` | `.claude/CLAUDE.md` lines 17–31; `docs/current-state.md` lines 213–218 |
| E14 | Cross-repo mechanics: read-only sibling access is standing-authorized; "attach + clone remains the path for deep/audit work in a sibling"; "writes stay in this repo"; raw reads need no `add_repo`; the only recorded `add_repo` wall is wake-session-scoped (classifier-denied ~1-in-2), not owner-live sessions; both bot repos were cloned successfully 2026-08-05 | `docs/reading-path.md` lines 11–27; `docs/CAPABILITIES.md` lines 884–887 and 695–700; playtest doc line 114 |
| E15 | Verify-first doctrine: "Verify before fold; verify with real exit codes"; program rule "the live surface beats any doc"; owner-profile: verify "against repos (git evidence), never against agent reports (playbook R2)"; owner epistemics: "Decide, don't default to asking" | `.claude/CLAUDE.md` lines 36–38; program `§4` lines 128–129; `docs/owner-profile.md` lines 11, 15; `docs/owner-reflection-2026-07-21.md` line 130 |
| E16 | Deliverable conventions: fleet-manager is the records custodian / working memory; findings are dated docs in `docs/findings/` with an index row, committed "so nothing lives only in an archivable chat"; owner is a non-coder — plain language, decisions pre-chewed | `README.md` lines 3–6; `docs/findings/README.md` lines 1–8; `docs/owner-profile.md` line 11 |
| E17 | Prompt/handoff method for "the next agents": routing row "Writing ANY session/handoff prompt → `prompt-preflight` (+ `continuation-prompt` or `implementation-prompt`)" | `.claude/CLAUDE.md` line 83; `docs/SKILLS-local.md` lines 44–46 |
| E18 | Rails that bound this session: OD-3 archive-never-delete; OD-6 slow pace; hard rail "never touch the `worker` service (the LIVE Discord bot) or the two Postgres DBs"; "No production-bot changes outside R7's owner-paced ladder"; E1 (EAP email) is owner-reserved — a session must not touch it | program lines 28, 31, 98, 139–140, 66–72 |

*Named by the procedure but missing in this snapshot (recorded, moved on):* `docs/intent.md`; the `docs/repos/<name>/` Layer-2 tree (so no `docs/repos/superbot/`); `docs/planning/2026-08-08-agent-operating-environment-roadmap.md`; `docs/SKILLS-local.md` has no "All 27 — the roster" section (the roster here = 14 kit rows in `docs/SKILLS.md` + 13 local rows in `docs/SKILLS-local.md`; 27 skill directories are installed in `.claude/skills/`). The superbot repo's own reading order, journals, cogs and helper files are outside the snapshot entirely — every claim about them below is deferred to post-attach verification.

**DERIVED** — inferences, labelled as such:
- "The superbot repo" (frag 2) = `menno420/superbot`, the old live bot: frag 4's vocabulary (cogs, help system, helper files) describes its architecture — superbot-next "has no cogs at all — its subsystems are compiled manifests" (audit lines 69–70) — and frag 7 then names superbot-next separately. Both repos end up read; the old bot is the primary deep read.
- This session is one of E1's "multiple independent reviews"; its document is input to "one plan", which is exactly what frag 8's "not the final planning or mapping session" restates.
- "Assert the proper baseline" = establish old superbot as the reference baseline in its OD-1 behavioral-oracle role, at file level: which files reflect the real live behavior worth preserving versus accumulated drift/dead weight — recorded as an assessment, not as edits to a frozen repo (see M1).
- "Helper files" = superbot's utils/services layer (the snapshot's only superbot-side anchors: `services/command_routing.py`, `utils/db/command_access.py` in the playtest doc, lines 201–239). Fleet-manager's own `docs/helper-policy.md` is generic kit policy about helper functions, not the referent.
- "Gemini for reviews… advanced models" = Pro-class models via the verified Vertex recipe (free key 429s on Pro, E11), with `delegate-read`'s citation-verification contract for corpus reads; "verify things that aren't sure" extends E8's run-it lesson — local boots on the test token per the audit's §8 recipe are in scope as verification (see M3).
- "Deep research from my own paid credits" = the direct (non-Vertex) paid Gemini path — D-0011's prepaid key — granted as an owner exception to Vertex-first's "only when Vertex failed" clause for deep-research-class work (see M2). No programmatic Deep Research recipe exists in the snapshot (E12), so the surface must be probed, not assumed.
- "A fair share of the session journals" = the kit's `.sessions/` cards in the superbot repo (fleet-manager's own convention; superbot's actual journal surface is verified after attach).
- This live instruction supersedes the program's NOW pointer for this session (E1 is owner-reserved; the fallback "take D2" is displaced by a direct owner ask — precedence, `.claude/CLAUDE.md` lines 99–103).
- "Most of what's documented is true, tho… verify" also licenses treating dated records as provenance-ranked: the snapshot itself holds a doc claim disproved by the live API (the "permanently read-only" closeout vs `archived=false`, E3).

**OPEN** — unresolved items, each pointing at the words that leave it open, with class and disposition:
- O1 (LOW — decided): frag 2 says "add the superbot repo" (singular) while frag 7 assigns work on "the superbot next repo" without an explicit "add". Open: attach one repo or both. Decided: attach/clone both read-only — frag 7 cannot be executed otherwise, and attach+clone is the documented deep-audit path (E14).
- O2 (MEDIUM — decided + flagged, M1): "assert the proper baseline… find which files are in the right state" names no write target. Open: record-only assessment vs corrective writes in superbot. Decided: record-only.
- O3 (MEDIUM — decided + flagged, M2): "directly use gemini's deep research from my own paid credits" — which billing identity "my own paid credits" names (D-0011's prepaid AI-Studio key vs the Vertex €251 credit), and whether a callable Deep Research surface exists at all (E12).
- O4 (LOW — decided): "a fair share of the session journals" sets no quantity. Decided: delegate the whole journal corpus to Gemini under the citation-verification contract (E11) and read the load-bearing cards directly — exceeds any "fair share" at near-zero cost.
- O5 (LOW — decided): "next recommended actions: the next agents to use…" — recommend only, or also launch them? The word is "recommended". Decided: recommendations plus paste-ready prompts via the prompt skills (E17); do not spawn or schedule sessions.
- O6 (LOW — decided): games out "for now" states no end condition. Decided: record as scoped-out-until-owner-says in the deliverable; no change to the program's OD table.

**GOAL** — After provably deep orientation in fleet-manager, attach and deeply study the superbot estate (old superbot first, then superbot-next), assert old superbot's proper baseline — file-level right-state judgements, games excluded — determine which parts of superbot-next are genuinely better built, using Gemini advanced-model reviews (Vertex-first, deep-research allowance) and verifying anything unsure, and land one comprehensive document in fleet-manager plus a plain-language chat summary that routes the next review agents (who, reviewing what, acting how) — as one input to the owner's multi-review rebuild plan.

**NON-GOALS** — plausible nearby readings that are *not* intended:
- Deciding disband-vs-rebuild, or which repo "wins" — the reviews feed that decision; this session does not make it (E1, frag 8).
- Producing the final rebuild plan or map (frag 8, verbatim).
- Executing consolidation/cutover steps R4/R7, code changes to either bot repo, or any touch of the production bot (`worker` service / Postgres DBs — E18).
- Any game-subsystem work or evaluation depth beyond noting the exclusion (frag 5, E4).
- Archiving or deleting anything (OD-3, E18); drafting/sending the owner-reserved E1 email (E18).
- Re-deriving what the 2026-08-05 audits already measured — the audit exists "so those reviewers start from measurements instead of re-deriving them" (audit lines 12–14).

**SUCCESS** — The owner reads a committed, indexed fleet-manager document showing: the session walked both reading orders in his stated order; old superbot's baseline asserted with per-file/per-area right-state judgements and stated provenance (measured vs inferred); a genuinely-better-built verdict per superbot-next part, distinguishing working from photographed (E6's method); Gemini Pro reviews via Vertex within the documented contract, any paid-key deep-research use said out loud; games untouched; no writes outside fleet-manager — and a chat summary in plain language ending in next-agent routing complete with boot recipe, audit target, and harness question per reviewer (E7). He recognizes it as one strong input to his multi-review plan, not a presumptuous final answer.

Sufficiency test, out loud: the outcome, the relevant existing intent (E1–E8), the constraints (E9–E11, E14, E18), the non-goals, and the definition of success are all statable above without silently resolving any HIGH — the only unresolved items are LOW/MEDIUM and are decided-and-flagged.

INTENT STATUS: RESOLVED

MAP TO METHOD

| Main idea | Existing skill / pattern (cited) | Genuinely new |
|---|---|---|
| 1 — Deep orientation, then attach | The read path itself (`.claude/CLAUDE.md` lines 17–31; `docs/current-state.md` lines 213–218); `chase-references` (routing row, `.claude/CLAUDE.md` line 85) to resolve every named file; attach+clone mechanics per `docs/reading-path.md` §0/§3; `delegate-read` (`docs/SKILLS-local.md` line 55) for the ~330-card journal corpus here and superbot's after attach. No wall: cloning both bot repos verified 2026-08-05 (playtest line 114); the sole `add_repo` wall row is wake-venue-scoped (`docs/CAPABILITIES.md` line 695). | Nothing new — pure execution of documented paths. |
| 2 — Baseline + genuinely-better assessment | `analysis` (read-only deep dive, installed); the audit's §6 audit-target + §8 boot recipe as the reusable method; `capability-probe` (`.claude/CLAUDE.md` line 89) before any "can't" — including probing whether a Deep Research API surface exists (E12); Vertex recipe (`docs/conventions/vertex-first-for-gemini.md` §§1–4) for Pro-model reviews; `delegate-read` contract for corpus-scale reads (public repos only — both bot repos qualify, E11); `deep-research` skill (installed) if external-source research is needed. | A file-level "right state" rubric for the old bot — nearest existing patterns are D2's fresh-session truth-pass test (program line 90) and R1's claims-vs-code conformance template (line 106), but neither covers per-file baseline judgement of a frozen oracle; this session defines it. |
| 3 — Deliverable + routing | Findings-doc convention (`docs/findings/README.md` lines 1–8) — dated doc + index row; D-0012 publish-by-default (`docs/decisions.md` lines 41–55); `decision-capture` for chat-only decisions (`.claude/CLAUDE.md` line 84); `prompt-preflight` + `implementation-prompt`/`continuation-prompt` for the next-agent prompts (line 83); `owner-brief` register (plain language, one-letter choices) for the chat summary; `session-close` to land it (line 92). | The per-reviewer routing table (agent × repo × focus × method), assembled from the audit's §6 triad — new assembly, existing parts. |

DECISIONS FLAGGED

- **M1 (from O2)** — Baseline assertion is record-only: judgements land in the fleet-manager document; zero writes to either superbot repo this session. Rationale: "writes stay in this repo" (`docs/reading-path.md` lines 24–25) and superbot is a frozen behavioral oracle (E3); if the owner wanted corrective commits, that is a one-line correction later.
- **M2 (from O3)** — Read "gemini's deep research from my own paid credits" as an owner-granted exception to Vertex-first's "only when Vertex failed" clause, drawing D-0011's prepaid key for deep-research-class calls, capped at its balance, said out loud in the session card; Vertex remains the default for everything else. Rationale: live owner outranks the stored convention (`.claude/CLAUDE.md` lines 99–103) and D-0011 pre-authorizes exactly this spend; the surface is probed first since no API recipe exists in the snapshot (E12).
- **M3** — Local boots of either bot on the test token (per audit §8, local Postgres, clean SIGTERM shutdown as done 2026-08-05) count as in-scope verification under "always verify things that aren't sure"; production surfaces (`worker`, its DBs) stay untouched per the hard rail (E18). Rationale: the estate's own recorded lesson is that reading alone produced five wrong claims (E8).

QUESTIONS FOR OWNER

none — no unresolved item classifies HIGH; the instruction itself resolves sequence, scope, method, epistemics, and deliverable, and the fuzzy edges are explicitly delegated ("use its own judgements"). Nothing is appended to `docs/question-router.md`. The M1–M3 flags travel in the run report for one-glance correction.

DURABLE?

Ephemeral — this map is working state; the one graduation candidate is M2's deep-research spend allowance (a `decision-capture` entry amending the Vertex-first convention once the owner sees the flag), and the session's real durable output is the comprehensive findings document the instruction itself orders.
