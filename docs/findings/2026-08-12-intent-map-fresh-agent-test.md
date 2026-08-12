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

All five agents completed and returned a full seven-part map with an
`INTENT STATUS` line in format (raw outputs preserved verbatim in
[the evidence folder](2026-08-12-intent-map-fresh-agent-test/README.md)).
Runs took 8–12 minutes and 98k–166k subagent tokens each (~655k total).

### 3.1 D1 — column placement, measured

Every ESTABLISHED row in every map was re-checked against that agent's pinned
snapshot by a whitespace-normalised needle search over the cited range ±3
lines (the evidence folder's `verify_citations.py` + `citations-*.tsv`), and
every non-matching row was adjudicated by opening the region:

| agent | rows checked | substance-correct | line-attribution imprecisions | worse |
|---|---|---|---|---|
| A1 | 51 (+2 negative/count checks) | 51 | 1 (an owner quote verbatim at `vertex-first:144`, attributed to `:3-8`) | — |
| A2 | 55 | 55 | 1 (`googleSearch` is at `vertex-first:106-109`, cited `:142-146`) | — |
| A3 | 54 (+2) | 53 | 2 (same `googleSearch` range; a label 2 lines outside its cited range) | **1 citation-overreach** (below) |
| B1 | 32 (+1 negative) | 32 | 1 (a clause cited to two ranges; only one carries it) | — |
| B2 | 30 (+1 negative) | 30 | 1 (same doubled range as B1) | — |
| **total** | **222** | **221** | **6** | **1** |

The one row worse than imprecise: A3's E16 states a true fact (Gemini once
returned 18 fabricated "decisions"), cites it correctly to
`findings/2026-08-05-gemini-delegation.md:34-48` (verified: `:37-41`), **and
appends a second citation — `docs/CAPABILITIES.md:179-194` — that does not
carry the incident** (that range is the free-tier corpus-read capability
entry). The fact is real and once-cited; the supplementary citation is wrong.
Classified as the worst member of the attribution-imprecision family rather
than fabrication — nothing was invented — with the raw data kept so a reviewer
can re-adjudicate.

Also mechanical: **0 invented OPEN entries** (every OPEN row in all five maps
quotes the words that leave it open — the "question 22" class did not occur);
**0 inferences dressed as EXPLICIT or ESTABLISHED** (EXPLICIT sections quote
the handed fragments; every inference sits in DERIVED, labelled); one
countable miscount (A3: "26 installed entries" under `.claude/skills/`; the
snapshot has 27). A suspected fabrication that wasn't: A3 cites
`docs/execution-surfaces.md`, which I believed post-dated pin A — it exists in
the pinned tree. The checker was wrong, not the agent; kept here because a
scorer's false alarm is data about scoring too.

### 3.2 D2 — HIGH discipline, and the headline divergence

**No agent silently resolved a HIGH.** But the corpus's one *expected* HIGH
went the other way from the walkthrough, and it is the most informative result
in the file:

- **Fragment 7** (*"which parts are genuinely better built"*). The author
  walkthrough scored this HIGH → `NEEDS OWNER`, on the stated ground that
  *"no retrieved record defines it."* **All three fresh agents resolved it
  `RESOLVED` — out loud, from the pinned tree** — citing
  `findings/2026-08-05-superbot-next-live-audit.md`: § 4's keep-list ("the
  layered architecture … is **genuinely better-founded** than superbot's
  accumulated patches", `:209-227`, verified), § 1's `CAPTURE-WORLD LITERAL`
  defect class, § 2's parity-cannot-see-photographs, § 4b's
  navigation-graph-is-the-product with the 60/66 table (verified in-range).
  The ask-time corpus **did** carry operational content for "genuinely better
  built" — the instruction's phrase echoes that audit's own vocabulary — so
  the walkthrough's premise is contradicted by retrieval, not by opinion.
  Under § 4.2 (*"resolve from evidence wherever possible"*) an out-loud,
  evidence-cited resolution is the procedure working. Each agent additionally
  surfaced the residual reading choices (record-only vs corrective writes,
  deep-research route, games depth) as MEDIUM decide-and-flag rows rather than
  absorbing them.
- **Case B.** Both agents retrieved the stale `Pace: slow.` row at its exact
  location, named the live-word-versus-record conflict explicitly, resolved by
  precedence with the stored row quoted — and **independently converged on the
  repair the estate actually shipped** (dated OD-6 restatement + the boot-file
  "Slow and structured" gloss fix, near-verbatim the fm #827 language),
  without access to it. B2 additionally found two OD-6 mis-citations in the
  pinned tree the walkthrough never mentioned.

### 3.3 Per-case tally, walkthrough vocabulary

| case | A1 | A2 | A3 | B1 | B2 |
|---|---|---|---|---|---|
| fragment 1 | partial | partial | partial | — | — |
| fragments 2–6, 8, 9 | 7 correct silences | 7 correct silences | 7 correct silences | — | — |
| fragment 7 | evidence-resolved (diverges from author) | same | same | — | — |
| case B | — | — | — | correction-handled | correction-handled |
| false alarms | 0 | 0 | 0 | 0 | 0 |

**Fragment 1 scored `partial` against the pre-registered anchor, and the
anchor itself deserves the critique:** all three agents carried the breadth
emphasis correctly (EXPLICIT quotes *"and more"*; GOAL/SUCCESS all read
full-comprehension — "provably deep", "read fully before touching superbot" —
so none reproduced the narrowing), but none placed *"stopping at a fixed
minimum reading list"* in NON-GOALS the way the author's map did. The author
knew the downstream failure when writing that NON-GOAL; a fresh agent mapping
the instruction alone has no textual signal that this specific misreading is
the salient one. The anchor encodes hindsight. Scored as registered, with
that bias named.

**Inter-agent agreement is high**: 3/3 and 2/2 on every INTENT STATUS, on the
fragment-7 evidence base, on the old-superbot-as-primary-referent inference,
and on case B's conflict and repair; the MEDIUM sets overlap heavily.

## 4 · Verdict

**PARTIAL, by the pre-registered bands — and near the PASS edge.** What
separates it from PASS: one citation-overreach (§ 3.1) plus six attribution
imprecisions — isolated ESTABLISHED-discipline defects, the band's "isolated
column misplacements". What separates it from FAIL: everything else — 0
silently resolved HIGHs, 0 invented facts or OPEN entries, 221/222 citation
substance, 0 false alarms, high inter-agent stability.

What the test establishes that the walkthrough could not:

1. **The map's provenance separation survives fresh hands.** Five agents who
   never saw the outcomes kept EXPLICIT / ESTABLISHED / DERIVED / OPEN
   distinguishable, under citation discipline that checks out at 221/222.
2. **Retrieval-based resolution outperformed the author's own map once** —
   fragment 7's HIGH dissolves under the retrieval the procedure itself
   mandates. The § 4.8 fear (a fresh agent silently resolving what the author
   knew to ask) did not materialise; the observed failure direction is the
   *scorer's*, not the agent's (§ 3.1's false fabrication alarm, § 3.3's
   hindsight anchor).
3. **The residual defect class is mechanically checkable.** All seven D1
   defects are of one kind — a citation range that does not carry the quoted
   content — which is exactly what `tools/gemini_delegate.py` already verifies
   for delegated reads. A cite-check pass over a map's ESTABLISHED rows would
   have caught 7/7. Recorded as a candidate mechanism under the promotion
   rule (§ 6 of the roadmap): observed and measured here; **not built** — one
   run is not "test against real cases" for the checker itself.

## 5 · Honest nulls

- **The scorer is not fresh** (§ 1.5). Bounded by the pre-registered rubric
  (commit order proves it), mechanical checks, committed raw outputs, and
  Codex review of this PR — but a § 4.8 run with an independent scorer remains
  the stronger form.
- **The HIGH-ask branch is now untested by this corpus at all.** The
  walkthrough had one HIGH case; § 3.2 dissolves it. No case in the committed
  record currently exercises "HIGH survives retrieval → agent must ask". That
  sub-null is *wider* after this test, not narrower, and a future corpus needs
  a genuinely underivable case.
- **Same model family throughout** — provider portability (roadmap § 1) is
  untested here.
- **n = 5 runs over 2 messages. Counts, not rates.**
- **Corpus caveats inherited whole** from the walkthrough § 1.1: none of the
  ten inputs is a raw owner message; the nine are agent-quoted and
  agent-segmented; case B is a correction, so it tests reconciliation, not
  prevention.
- **Agent containment is instructed, not audited.** Every citation in every
  map resolves inside the pinned trees and all five reported the
  pin-appropriate absences (no `intent.md`, no roadmap at pin A, no roster
  section), which is consistent with containment; tool traffic was not
  captured. The risk direction: an agent that peeked would look *more* like
  the known outcomes, i.e. agreement here is the quantity at risk, and the
  headline divergence (§ 3.2) argues against peeking.
- **The handed procedure carried two dated event-pointers** (step 2's "one
  miss out of 21 on the 2026-08-08 intent batch"; step 3's "question 22"
  example) — pointers to an adjacent event for pin B, but to none of the
  scored outcomes: neither the correction's content, nor OD-6's restatement,
  nor the pace subject appears in the handed text.

## 6 · The run, reproducibly

Committed beside this file in
[`2026-08-12-intent-map-fresh-agent-test/`](2026-08-12-intent-map-fresh-agent-test/README.md):
the two agent prompt templates verbatim (`prompt-A.md`, `prompt-B.md` — the
`{SNAPSHOT_DIR}`/`{PROCEDURE}` slots filled exactly as described in § 1), the
five raw agent reports, the citation checker and its four TSVs, and the
adjudication of every non-PASS row. Snapshots are reproducible from the pins:
`git archive 7fbc065` / `git archive f53d7ea`.
