---
name: intake
description: "Turn a fragmented owner ask into a provenance-separated intent map — what he said, what the repo already decided, what you inferred, what is genuinely open — plus the goal, the non-goals, the success test and an INTENT STATUS verdict, before any planning starts."
---

# intake

Turn a fragmented owner ask about fleet-manager into a verified fuller picture
before building. Executable wrapper around the understand-and-reflect doctrine
(`CONSTITUTION.md` working agreement) — not new policy. Provenance: superbot
router Q-0254 (owner-directed 2026-07-07, graduated to the kit's
CONSTITUTION/collaboration-model templates the same day) plus the Q-0263.2
paste-ready-questions directive, and — from 2026-08-09 — the Phase 2 intent
architecture (`docs/planning/2026-08-08-agent-operating-environment-roadmap.md`
§ 4). Invoke on any non-trivial, non-mechanical owner ask — especially a
fragmented or associative one.

## What this does

The owner builds ideas iteratively and in fragments by design — a rough draft
now, more shape later — and relies on the agent to reason a partial idea forward
to its fuller form (`docs/owner-profile.md`). This skill runs that step as a
procedure: one inline restate that pays off twice — verification (a wrong
assumption stated now costs one correction; found after an hour of building it
costs the hour) and idea-expansion (the filled-in picture is itself new material
the owner reasons against and redirects).

**What changed in 2026-08-09, and why it is the whole point.** This skill used to
emit a single *"FULLER PICTURE (short prose)"* — one fluent paragraph fusing what
the owner said, what the repo already decided, and what the agent inferred. That
paragraph is the failure mode § 4.1 of the roadmap names: **three kinds of claim
that read exactly alike, so nobody can check the one that is wrong.** The map
below keeps them apart. A fluent paragraph is not the goal and never was.

## Invocation

/intake <the ask, or a pointer to it>

## Instructions

1. **CONSOLIDATE** — reduce the fragmented ask to its few MAIN IDEAS (usually
   1–3). Name each in one line. The owner thinks associatively on purpose;
   consolidation is your half of the contract. Idea order is not implementation
   order — capture side ideas, never derail on them.

2. **RETRIEVE — go and look; do not recall.** ESTABLISHED is a *retrieval* step.
   Read `docs/intent.md`, the program's OD table, `docs/decisions.md`, the
   relevant `docs/repos/<name>/`, and any convention the ask touches. This step
   exists because eye-filtering was **`MEASURED` at one miss out of 21** on the
   2026-08-08 intent batch: the purpose question was already half-answered in two
   records and the filtering pass missed it. Recall feels like retrieval and is
   not.

3. **MAP THE INTENT — seven parts, never fused into one paragraph.**

   | part | what it holds |
   |---|---|
   | **EXPLICIT** | what the owner actually said in *this* request |
   | **ESTABLISHED** | intent, decisions, constraints, non-goals already documented — each with its citation |
   | **DERIVED** | what you inferred, labelled as inference |
   | **OPEN** | outcome-changing questions that cannot safely be derived |
   | **GOAL** | one coherent statement of the intended outcome |
   | **NON-GOALS** | plausible nearby readings that are *not* intended |
   | **SUCCESS** | the result that would make him say "yes, that is what I meant" |

   **The OPEN column carries the same evidential burden as the others.** An entry
   there claims *he left something unresolved* — and an invented absence looks
   identical to a real one while wearing the same label. Measured 2026-08-08: a
   stray `22.` in an answer list became *"question 22, begun and left blank"* in
   three documents; there was no question 22. If you cannot point at the words
   that leave it open, it is not OPEN.

4. **CLASSIFY, THEN TEST.** Every unresolved item gets a class:

   - **LOW** — implementation detail. Decide it.
   - **MEDIUM** — reversible design choice. Decide it **and flag it**.
   - **HIGH** — changes product intent, scope, ownership, irreversibility, or the
     definition of success. **Ask.** Never resolve a HIGH silently.

   **A decided LOW or MEDIUM item reports under DECISIONS FLAGGED (or the run
   report), never under OPEN** — OPEN holds only what cannot safely be derived.
   Measured 2026-08-12 (§ 4.8 test, fm #851 § 4): three of five fresh maps
   parked decided items in OPEN because this step classified "every unresolved
   item" without saying where decided ones report.

   Then answer the sufficiency test out loud — *can I state the outcome, the
   relevant existing intent, the constraints, the non-goals and the definition of
   success, without silently resolving any HIGH?* — and print one of:

   ```
   INTENT STATUS: RESOLVED
   ```
   ```
   INTENT STATUS: NEEDS OWNER
   OPEN HIGH:
     - …
   ```

   Categorical on purpose. **No numeric confidence score** — a number here is
   fake precision, and the two-state verdict is what a later review refers back
   to. **There is no question budget.** Often the answer is zero questions and a
   structured restatement he corrects; sometimes it is ten. The stopping
   condition is this test, never a count — any number written here would be
   optimised toward instead of the thing it stands for.

5. **MAP TO METHOD** — map each main idea to known step patterns via the skill
   index (`docs/SKILLS-local.md` § "All 27 — the roster"): which existing
   skill/playbook/checklist covers it, which parts are genuinely new. Cite the
   exact skill or doc per idea, and check `docs/CAPABILITIES.md` before assuming
   any wall.

6. **POSSIBILITY SPACE** — when the ask starts from uncertain feasibility ("I
   don't know if this is even possible" is a normal starting point, not an edge
   case), surface what is achievable and by what approaches FIRST, before
   committing to a direction. Target: the most advanced capability reachable by
   the simplest, most efficient implementation.

7. **DECIDE-AND-FLAG** — LOW and MEDIUM are yours (recommendation + one-line
   rationale + a flag on the run report for MEDIUM). Route only HIGH to the
   owner, as a structured choice — options A/B(/C), a **bolded recommendation**,
   one-line rationale, answerable with one letter. Prefer stating your
   interpretation back over demanding a specification: *"my reading is that X is
   only an example and the broader goal is Y — right level, or am I generalising
   too far?"* Never an ask that requires him to parse, derive or transform
   anything (a drafting defect, not an owner task). **Ask immediately and keep
   working** — stop only when no next step exists without the answer. With no
   live owner, append to `docs/question-router.md` rather than skipping or
   guessing.

8. **EPHEMERAL OR DURABLE** — one line, and default to ephemeral. The map is
   working state; it does not belong in a canonical document. Only where
   **durable knowledge actually changed** does anything graduate:

   ```
   messy request → intent map → resolved intent → plan          (ephemeral)
   resolved DURABLE intent → documentation procedure → canonical source
   ```

   *"Maybe we should move X into Y, I'm not sure yet"* can be mapped perfectly,
   asked about and resolved without one word of it reaching `intent.md`.

A trivial or fully-unambiguous ask stays exempt: a one-line "doing X because Y"
suffices — the same calibration as the doctrine itself. A big or vague idea earns
a dedicated research pass (a delegated subagent, reviewed the same session) or
its own session, never an answer from memory alone.

## Report format

Print: **MAIN IDEAS** (numbered) · **INTENT MAP** (the seven parts, separately
labelled — never merged) · **INTENT STATUS** (`RESOLVED` or `NEEDS OWNER` + the
OPEN HIGH list) · **MAP TO METHOD** (idea → skill/pattern/new) · [**POSSIBILITY
SPACE** if triggered] · **DECISIONS FLAGGED** (MEDIUM) · **QUESTIONS FOR OWNER**
(HIGH only, structured choices, or `none`) · **DURABLE?** (one line).

Declared capabilities: read (the index, the ledger, the profile, the intent and
decision records).

## Replayed against real owner messages

Walked through **ten owner asks as the committed record preserved them** — real,
never synthetic, but **none of them raw**: nine are verbatim fragments *quoted and
segmented by an agent*, and the tenth is a correction rather than the message that
caused the error (§ 1.1 and § 2.2 of the walkthrough):
[`docs/findings/2026-08-09-intent-map-replay.md`](../../../docs/findings/2026-08-09-intent-map-replay.md)
— **0 clean catches · 1 partial · 1 correction-handled · 1 HIGH surfaced · 7
correct silences · 0 false alarms.**

**That is an author walkthrough, not the prescribed test.** Roadmap § 4.8
requires a **fresh agent** to produce the maps; the walkthrough's author wrote
this procedure and knew every outcome. Read § 4 of that file before citing any
of it — and § 2.2 for the case that cannot be run at all, because the owner
message that produced the estate's clearest misread was never preserved.

**The producer half of that test ran 2026-08-12** (fm #851): five fresh agents
over the same corpus against ask-time snapshot trees, scored by the running
session on a pre-registered rubric — the fresh-**scorer** half the record
requires is still outstanding —
[`docs/findings/2026-08-12-intent-map-fresh-agent-test.md`](../../../docs/findings/2026-08-12-intent-map-fresh-agent-test.md)
— **221/222 checked citations substance-correct · 0 invented OPEN · 0 silent
HIGHs · 0 false alarms · verdict PARTIAL** (one citation-overreach, one
ESTABLISHED miscount, eleven exact-range attribution imprecisions). The
walkthrough's one HIGH dissolved under fresh retrieval, so the HIGH-ask branch
is currently demonstrated by no committed case; the dominant defect class is
imprecise line-cites — when you cite, open the exact range and check it
carries the words.
