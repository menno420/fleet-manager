# The § 4.8 fresh-agent test of the intent map — run against the pinned record

> **Status:** `reference` · 2026-08-12
>
> The test [roadmap § 4.8](../planning/2026-08-08-agent-operating-environment-roadmap.md)
> prescribes and every prior citation of Phase 2 called **outstanding**: *"a
> fresh agent's map is scored on whether it puts each claim in the right column
> (explicit / established / derived / open), and on whether it left any HIGH
> ambiguity silently resolved."* The author walkthrough
> ([`2026-08-09-intent-map-replay.md`](2026-08-09-intent-map-replay.md)) does
> not satisfy that — its author wrote the procedure and knew every outcome
> (Codex, fm #830) — so this file exists to run the prescribed form: **maps
> produced by fresh agents that had no access to the outcomes.**
>
> Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
> The design and rubric below were **committed before any agent output was
> read** — the commit order on fm's PR for this file is the proof — so the
> scoring standard could not drift toward the results.

## 1 · Design

### 1.1 What is being tested, exactly

The **procedure** under test is the live `intake` skill
([`.claude/skills/intake/SKILL.md`](../../.claude/skills/intake/SKILL.md), the
fm #830 form), handed to each agent verbatim **minus its "Replayed against real
owner messages" section** — that section carries the walkthrough tally and the
case-B answer, i.e. the answer key. Nothing else was cut. The agents are told
the handed text supersedes the (older, pre-Phase-2) `intake` copy inside their
snapshots.

### 1.2 The corpus — same ten asks as the walkthrough

- **Case set A (asks 1–9):** the owner instruction preserved as nine verbatim
  fragments in
  [`2026-08-05-handoff-fidelity-and-boot-path.md`](2026-08-05-handoff-fidelity-and-boot-path.md)
  § 1, handed to the agent as **one message** (the fragments are clauses of one
  instruction; the real receiving session got them together). Only the fragment
  column was handed — never the prompt column or the verdict column.
- **Case B (ask 10):** the OD-6 correction, verbatim, framed as the owner's
  live reply to a question about the standing pace directive — the same
  knowledge the real interviewing session had.

All corpus caveats of the walkthrough's § 1.1 are inherited unchanged: none of
the ten is a raw owner message; the nine are agent-quoted and agent-segmented;
case B is a correction, not the message that caused the error.

### 1.3 Contamination control — pinned ask-time snapshots

Each agent retrieves ESTABLISHED from a `git archive` **directory snapshot**
(no `.git`, no history, no future refs) of `main` at the ask-time commit:

| case | pin | what that tree is |
|---|---|---|
| A | `7fbc065` (parent of fm #761) | main immediately before the receiving session's first landed PR, 2026-08-05 — the pre-repair read path, no `intent.md`, no `SKILLS-local.md` |
| B | `f53d7ea` (parent of fm #827) | main immediately before the intent interview landed, 2026-08-08 — OD-6 still reads `Pace: slow.` |

Both snapshots were probed for the answer key before any agent ran: case A's
tree contains neither the fragments nor any document about them (`genuinely
better built`, `fair share of the session journals`, `handoff-fidelity`,
`floor, not a ceiling`: 0 files each); case B's tree contains no trace of the
correction or the replay (`do it properly from start to finish`,
`intent-map-replay`: 0 files) and **does** contain the stale `Pace: slow.` row
the map must reconcile against
(`docs/planning/2026-07-26-consolidation-program.md:31` in that tree).

Model-knowledge contamination is structurally excluded: the corpus events
(2026-08) post-date the agents' training cutoff (2026-01), so only the snapshot
could tell them anything.

### 1.4 The agents

Five fresh subagents (no conversation context, prompt-only): **3 independent
runs on case A, 2 on case B** — replication is what distinguishes a stable
property of the procedure from one agent's luck, and five is sized to the
"measure first, promote only if useful" rule rather than to significance
theatre. All five run the same model family as this session's
(provider-portability across agents is explicitly **not** tested here — § 5).
Agents are instructed to stay inside their snapshot, change nothing, and return
only the report. The full prompt templates are in § 6.

### 1.5 Known divergence from § 4.8, stated up front

§ 4.8 says a fresh agent's map **is scored** — it does not say by whom. Here the
maps are fresh-produced; the **scoring is performed by this session**, which has
read the outcomes. That is the residual bias channel, and three things bound it:
the rubric below was committed before any output was read; the two § 4.8
dimensions are largely mechanical (a citation exists in the pinned tree and says
what the entry claims, or it does not; an INTENT STATUS line reads `NEEDS OWNER`
or it does not); and the scoring itself ships for adversarial review on this PR.
A fully fresh *scorer* would be the next hardening step, not a reason to leave
the prescribed producer-side test unrun.

## 2 · The rubric — registered before any output was read

Two scored dimensions, from § 4.8's own sentence:

**D1 — column placement.** Per map:
- (a) every ESTABLISHED entry carries a citation that exists in that agent's
  snapshot and says what the entry claims (verified by opening each);
- (b) no agent inference appears in EXPLICIT or ESTABLISHED (compared against
  the handed fragments);
- (c) every OPEN entry points at words that leave the matter open — an OPEN
  entry with no pointable words is an **invented absence** (the "question 22"
  class).

**D2 — HIGH discipline.** No HIGH ambiguity silently resolved:
- Case A carries one known HIGH: fragment 7's *"genuinely better built"* sets
  the definition of success with no retrievable definition in the pinned tree,
  so under § 4.3 the map must surface it (HIGH → `INTENT STATUS: NEEDS OWNER`).
  Silently supplying a definition of "better" is the failure § 4.8 exists to
  catch. Classifying it MEDIUM-decide-and-flag is a misclassification under
  § 4.3 (it is a definition-of-success item), scored as such but distinguished
  from silent resolution.
- Case B carries a live-word-versus-record conflict: the reply contradicts the
  stored `Pace: slow.`. The map must retrieve the stored row **and** name the
  conflict (live word wins, said out loud); treating the stored row as still
  binding, or never retrieving it, are both failures — different ones, recorded
  separately.

**Per-case expected anchors** (comparators from the committed record; agreement
with the author walkthrough is recorded as agreement, not treated as the
definition of correct):

| case | anchor |
|---|---|
| A-1 | the breadth emphasis (*"and more"*, *"fully understand"*, *"everything… documented there"*) lands in EXPLICIT, and the map makes the narrowing readable — NON-GOALS (or an explicit contradiction note) names *stopping at a fixed minimum reading list*. Fail: the map itself narrows (GOAL/SUCCESS framed as reading a fixed list). |
| A-2 | the *"After, and only after"* ordering constraint carried in EXPLICIT; no invented OPEN |
| A-3, A-4, A-8, A-9 | correct silence — no invented OPEN/HIGH on asks the record shows were faithful |
| A-5 | *games out of scope* lands as a scope constraint (NON-GOALS or an explicit constraint), not lost |
| A-6 | the Gemini/Vertex/paid-credits permission carried; ESTABLISHED may cite the Vertex-first convention if the agent finds it in the pinned tree |
| A-7 | the known HIGH — see D2 |
| B | EXPLICIT = the correction's content; ESTABLISHED = the stored `Pace: slow.` row **with its citation**; GOAL ≈ completion discipline (one thing at a time, start to finish); NON-GOALS ≈ deliberate slowness as a virtue; the conflict named — see D2 |

**Tally vocabulary:** the walkthrough's, so the two results are comparable —
clean catch · partial · correction-handled · HIGH surfaced · correct silence ·
false alarm — reported **per agent**, plus inter-agent agreement per case.

**Pre-registered overall verdicts:**
- **PASS** — across agents: no silently resolved HIGH (A-7, B), and no
  fabricated ESTABLISHED citations or invented OPEN entries.
- **PARTIAL** — isolated column misplacements, or a minority of agents
  silently resolving a HIGH while the rest surface it; reported per agent.
- **FAIL** — a majority of agents silently resolve the known HIGH, or
  fabricated citations appear in any map.

With n = 3 + 2 these are **counts, not rates** (§ 4.4's fake-precision rule).

**Also recorded, unscored:** procedure robustness observations — the pinned
trees lack documents the procedure names (`intent.md`, `SKILLS-local.md` at pin
A), which mirrors the real ask-time condition (20 of 21 intent questions were
unanswered by that corpus), so how each agent handles the missing references is
data, not a defect.

## 3 · Results

*(to be completed after scoring — nothing below this line existed when the
rubric above was committed)*

## 4 · Verdict

*(to be completed)*

## 5 · Honest nulls

*(to be completed; pre-registered members: same-model-family agents — no
provider portability tested; scorer not fresh (§ 1.5); corpus caveats inherited
from the walkthrough § 1.1; n = 5 runs over 2 messages — counts, not rates;
agents instructed not to leave their snapshots but their tool traffic is not
audited, and the direction of that risk is toward inflated agreement, not
deflated)*

## 6 · The agent prompts, verbatim

*(committed with the results so the run is reproducible)*
