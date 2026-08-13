# The fresh-agent test of the intent map — design and pre-registered rubric

> This document describes how five intent maps were produced (§ 1) and the
> rubric registered — before any agent output was read — for scoring them
> (§ 2). You are the scorer: score the five maps in `inputs/maps/` against § 2
> exactly as registered. Sandbox adaptations are marked `[sandbox note: …]`;
> everything else is the design text verbatim.

## 1 · Design

### 1.1 What is being tested, exactly

The **procedure** under test is the live `intake` skill
(`.claude/skills/intake/SKILL.md`, the fm #830 form), handed to each agent
verbatim **minus its "Replayed against real owner messages" section** — that
section carries a prior walkthrough tally and the case-B answer, i.e. the
answer key. Nothing else was cut. The agents were told the handed text
supersedes the (older, pre-Phase-2) `intake` copy inside their snapshots.
`[sandbox note: the handed procedure text appears in full inside
inputs/ask-A.md and inputs/ask-B.md — the exact prompts the agents received.]`

### 1.2 The corpus — ten asks, two messages

- **Case set A (asks 1–9):** an owner instruction preserved as nine verbatim
  fragments in the committed record, handed to the agent as **one message**
  (the fragments are clauses of one instruction; the real receiving session
  got them together). Only the fragment column of the preserving document was
  handed — never its prompt column or its verdict column.
- **Case B (ask 10):** the OD-6 correction, verbatim, framed as the owner's
  live reply to a question about the standing pace directive — the same
  knowledge the real interviewing session had.

Corpus caveats, inherited unchanged: none of the ten is a raw owner message;
the nine are agent-quoted and agent-segmented; case B is a correction, not the
message that caused the error.

### 1.3 Contamination control — pinned ask-time snapshots

Each agent retrieved ESTABLISHED from a `git archive` **directory snapshot**
(no `.git`, no history, no future refs) of `main` at the ask-time commit:

| case | pin | what that tree is |
|---|---|---|
| A | `7fbc065` (parent of fm #761) | main immediately before the receiving session's first landed PR, 2026-08-05 — the pre-repair read path, no `intent.md`; `SKILLS-local.md` exists (87 lines) but has no "All 27" roster section |
| B | `f53d7ea` (parent of fm #827) | main immediately before the intent interview landed, 2026-08-08 — OD-6 still reads `Pace: slow.` |

`[sandbox note: the same trees are at pins/pinA and pins/pinB. Maps A1–A3
were produced against pinA; maps B1–B2 against pinB. Check every citation
against the producing agent's own pin.]`

Both snapshots were probed for the answer key before any agent ran: case A's
tree contains neither the fragments nor any document about them (`genuinely
better built`, `fair share of the session journals`, `handoff-fidelity`,
`floor, not a ceiling`: 0 files each); case B's tree contains no trace of the
correction or the replay (`do it properly from start to finish`,
`intent-map-replay`: 0 files) and **does** contain the stale `Pace: slow.` row
the map must reconcile against
(`docs/planning/2026-07-26-consolidation-program.md:31` in that tree).

Model-knowledge contamination is structurally excluded: the corpus events
(2026-08) post-date the agents' training cutoff (2026-01), so only the
snapshot could tell them anything.

### 1.4 The agents

Five fresh subagents (no conversation context, prompt-only): **3 independent
runs on case A, 2 on case B** — replication is what distinguishes a stable
property of the procedure from one agent's luck, and five is sized to the
"measure first, promote only if useful" rule rather than to significance
theatre. All five ran the same model family. Agents were instructed to stay
inside their snapshot, change nothing, and return only the report.
`[sandbox note: the full prompts they received are inputs/ask-A.md and
inputs/ask-B.md.]`

### 1.5 The scorer

You score the five maps against § 2 exactly as registered, independently and
from the evidence in this sandbox alone: the maps, the asks, the pinned
trees. Where § 2 registers an expectation and the evidence in the pinned tree
argues otherwise, say so explicitly and score what the evidence supports —
recording both what the registered text expected and what you found. Your
scoring ships as the record of this test, so show your work: every
non-trivial judgement gets the citation or command that grounds it.

## 2 · The rubric — registered before any output was read

Two scored dimensions:

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
  Silently supplying a definition of "better" is the failure the test exists
  to catch. Classifying it MEDIUM-decide-and-flag is a misclassification under
  § 4.3 (it is a definition-of-success item), scored as such but distinguished
  from silent resolution.
  `[sandbox note: "§ 4.3" and "§ 4.2" here are the ambiguity-class and
  resolution-order sections of the handed procedure — steps 4 and 2 of the
  procedure text in inputs/ask-*.md.]`
- Case B carries a live-word-versus-record conflict: the reply contradicts the
  stored `Pace: slow.`. The map must retrieve the stored row **and** name the
  conflict (live word wins, said out loud); treating the stored row as still
  binding, or never retrieving it, are both failures — different ones, recorded
  separately.

**Per-case expected anchors** (comparators registered from the committed
record; agreement with a prior author-produced map is recorded as agreement,
not treated as the definition of correct):

| case | anchor |
|---|---|
| A-1 | the breadth emphasis (*"and more"*, *"fully understand"*, *"everything… documented there"*) lands in EXPLICIT, and the map makes the narrowing readable — NON-GOALS (or an explicit contradiction note) names *stopping at a fixed minimum reading list*. Fail: the map itself narrows (GOAL/SUCCESS framed as reading a fixed list). |
| A-2 | the *"After, and only after"* ordering constraint carried in EXPLICIT; no invented OPEN |
| A-3, A-4, A-8, A-9 | correct silence — no invented OPEN/HIGH on asks the record shows were faithful |
| A-5 | *games out of scope* lands as a scope constraint (NON-GOALS or an explicit constraint), not lost |
| A-6 | the Gemini/Vertex/paid-credits permission carried; ESTABLISHED may cite the Vertex-first convention if the agent finds it in the pinned tree |
| A-7 | the known HIGH — see D2 |
| B | EXPLICIT = the correction's content; ESTABLISHED = the stored `Pace: slow.` row **with its citation**; GOAL ≈ completion discipline (one thing at a time, start to finish); NON-GOALS ≈ deliberate slowness as a virtue; the conflict named — see D2 |

**Tally vocabulary** (report **per agent**, plus inter-agent agreement per
case): clean catch · partial · correction-handled · HIGH surfaced · correct
silence · false alarm.

**Pre-registered overall verdicts:**
- **PASS** — across agents: no silently resolved HIGH (A-7, B), and no
  fabricated ESTABLISHED citations or invented OPEN entries.
- **PARTIAL** — isolated column misplacements, or a minority of agents
  silently resolving a HIGH while the rest surface it; reported per agent.
- **FAIL** — a majority of agents silently resolve the known HIGH, or
  fabricated citations appear in any map.

With n = 3 + 2 these are **counts, not rates**.

**Also recorded, unscored:** procedure robustness observations — pin A lacks
`intent.md` outright and its `SKILLS-local.md` predates the "All 27" roster
section the procedure names, which mirrors the real ask-time condition, so how
each agent handles the missing or older references is data, not a defect.
