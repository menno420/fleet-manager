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
> (Codex, fm #830) — so this file exists to run what could be run of the
> prescribed form: **maps produced by fresh agents that had no access to the
> outcomes.** That is the producer half; the recorded bar also requires a
> fresh **scorer**, which this run does not have (§ 1.5).
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
| A | `7fbc065` (parent of fm #761) | main immediately before the receiving session's first landed PR, 2026-08-05 — the pre-repair read path, no `intent.md`; `SKILLS-local.md` exists (87 lines) but has no "All 27" roster section *(this cell originally said the file was absent — wrong, Codex round 1; the agents themselves had it right)* |
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

### 1.5 This is the producer half of § 4.8, not the whole test

The roadmap's § 4.8 sentence says a fresh agent's map **is scored** without
naming the scorer — but the estate's own acceptance record is explicit:
*"A fresh agent must produce **and score** the maps"*
([`2026-08-09-intent-map-replay.md:166`](2026-08-09-intent-map-replay.md)), and
the fm #830 review disposition likewise requires a fresh-agent **scorer**
(`.sessions/2026-08-09-intent-architecture-phase-2.md`, round-1 row 3). Here
the maps are fresh-produced and the **scoring is performed by this session**,
which had read the outcomes — so this run discharges the **producer half only**,
and the **scorer half remains outstanding** *(it ran 2026-08-13 — two blind
scorers, PARTIAL confirmed:
[`2026-08-13-intent-map-fresh-scorer.md`](2026-08-13-intent-map-fresh-scorer.md))*.
(The first push of this finding
claimed "the prescribed producer-side form" as if that were the prescribed
test; Codex round 1 refuted it from the two records above — conceded.)
Three things bound the scorer bias in the half that did run: the rubric below
was committed before any output was read; the checks are largely mechanical (a
citation is in the pinned tree carrying the claimed words, or it is not; an
INTENT STATUS line reads `NEEDS OWNER` or it does not); and the scoring ships
for adversarial review on this PR. § 3 records where scorer judgement still
leaked in anyway — and every leak found so far ran in the *scorer's* error
direction, not the agents'.

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

**Also recorded, unscored:** procedure robustness observations — pin A lacks
`intent.md` outright and its `SKILLS-local.md` predates the "All 27" roster
section the procedure names *(this sentence originally listed `SKILLS-local.md`
as missing too — wrong, Codex round 1)*, which mirrors the real ask-time
condition (20 of 21 intent questions were unanswered by that corpus), so how
each agent handles the missing or older references is data, not a defect.

## 3 · Results

All five agents completed and returned a full seven-part map with an
`INTENT STATUS` line in format (raw outputs preserved verbatim in
[the evidence folder](2026-08-12-intent-map-fresh-agent-test/README.md)).
Runs took 8–12 minutes and 98k–166k subagent tokens each (~655k total).

### 3.1 D1 — column placement, measured

Every citation encoded from the five reports was re-checked against that
agent's pinned snapshot by a whitespace-normalised needle search (the evidence
folder's `verify_citations.py` + `citations-*.tsv`), in **two passes** — a
±3-line **substance** pass, and an exact-range **attribution** pass added in
Codex round 1, which had refuted the first push's single-pass tally: a ±3
tolerance converts small wrong ranges into machine-PASSes that then never
reach adjudication. Every row failing either pass was adjudicated by opening
the region. Two corrections from the same round: the checked rows span the
whole reports (ESTABLISHED plus DERIVED / NON-GOALS / MAP-TO-METHOD
citations), so the metric is reported per column-set rather than mislabelled
"ESTABLISHED citations" as first pushed; and A3's skills miscount is counted
as an ESTABLISHED factual error, not a footnote.

| agent | rows | of which ESTABLISHED | substance-correct | attribution-imprecise (exact-range) | worse |
|---|---|---|---|---|---|
| A1 | 51 (+2 negative/count checks) | 44 | 51 | 2 | — |
| A2 | 55 | 50 | 55 | 3 | — |
| A3 | 54 (+2) | 46 | 53 | 2 | **1 citation-overreach + 1 factual miscount** (below) |
| B1 | 32 (+1 negative) | 24 | 32 | 3 | — |
| B2 | 30 (+1 negative) | 24 | 30 | 1 | — |
| **total** | **222** | **188** | **221** | **11** | **2** |

So: **all-report citations 221/222 substance-correct; the ESTABLISHED subset
is 187/188** (the overreach is an ESTABLISHED row), plus one non-row
ESTABLISHED factual error; the 34 non-ESTABLISHED rows are 34/34. The eleven
attribution imprecisions (all in ESTABLISHED rows): the six adjudicated from
the substance pass — an owner quote verbatim at `vertex-first:144` attributed
to `:3-8` (A1); `googleSearch` at `vertex-first:106-109` cited `:142-146` (A2
and A3 — same wrong range independently); a label two lines outside its cited
range (A3); a clause cited to two ranges of which one doesn't carry it (B1 and
B2, same doubled range) — plus the five the exact pass exposed: claims at
`fleet-account:22`, `CAPABILITIES:881-882`, `playtest:171`,
`decision-capture:36`, `CONSTITUTION:16`, each cited one-to-four lines away.
The per-agent partition of rows into column-sets is derived in the evidence
folder's README, from each report's own section structure.

**Enumeration coverage, named after round 2 caught its limit:** the TSV rows
are scorer-enumerated from each report, not mechanically exhaustive, and Codex
round 2 found one citation the enumeration omitted — A1's ESTABLISHED quotes
`disbot/config.py:111`, a superbot-repo path that cannot resolve inside the
fleet-manager snapshot. Adjudicated **non-defect with the reason recorded**:
the pinned source A1 cites carries that exact pointer verbatim
(`playtest…:120` — *"| Extensions | **61 loaded** (`disbot/config.py:111`) |"*),
so A1 reproduced its cited source's own cross-repo reference — materially
unlike A3's overreach, where the appended range does not carry the fact. The
row is enumerated in the evidence folder with that adjudication; a
fully-mechanical row extractor is part of the cite-check candidate in § 4.

The two entries worse than imprecise, both A3's, both in ESTABLISHED:

- **The citation-overreach.** A3's E16 states a true fact (Gemini once
  returned 18 fabricated "decisions"), cites it correctly to
  `findings/2026-08-05-gemini-delegation.md:34-48` (verified: `:37-41`), **and
  appends a second citation — `docs/CAPABILITIES.md:179-194` — that does not
  carry the incident** (that range is the free-tier corpus-read capability
  entry). The fact is real and once-cited; the supplementary citation is
  wrong. Classified as the worst member of the attribution family rather than
  fabrication — nothing was invented — raw data kept for re-adjudication.
- **The factual miscount.** A3's ESTABLISHED inventory says the snapshot has
  "26 installed entries" under `.claude/skills/`; it has 27. First pushed as a
  footnote outside the tally; Codex round 1 was right that a wrong count in
  ESTABLISHED is an ESTABLISHED defect — counted.

Also mechanical: **0 invented OPEN entries** — scoped precisely: every OPEN
row in all five maps quotes real words that leave something open, so the
"question 22" class (an OPEN entry pointing at nothing) did not occur.
**Column discipline inside OPEN is a different question and the rubric did
not score it** — Codex round 1 named the gap, and counting it: the procedure
defines OPEN as *outcome-changing questions that cannot safely be derived*,
yet three of the five maps also parked self-classified LOW/decided items
there (A1 ×2, A2 ×3, A3 ×3; B2's two OPEN rows carry MEDIUM dispositions
inline; B1 modeled the strict form — `OPEN: none`, candidates examined and
closed). Two readings coexist: those entries violate § 4.1's column
definition, or they follow the procedure's own step 4, which says *"every
unresolved item gets a class"* without saying where classified-and-decided
items are reported. That ambiguity is a **procedure defect surfaced by the
test**, recorded in § 4; the instances are counted here either way.
**0 inferences dressed as EXPLICIT or ESTABLISHED** (EXPLICIT sections quote
the handed fragments; every inference sits in DERIVED, labelled). A suspected
fabrication that wasn't: A3 cites `docs/execution-surfaces.md`, which I
believed post-dated pin A — it exists in the pinned tree. The checker was
wrong, not the agent; kept because a scorer's false alarm is data about
scoring too.

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

**PARTIAL, by the pre-registered bands** — and after Codex round 1 recounted
it, less near the PASS edge than first pushed. What separates it from PASS:
one citation-overreach, one ESTABLISHED factual miscount, and eleven
exact-range attribution imprecisions (§ 3.1) — isolated ESTABLISHED-discipline
defects, the band's "isolated column misplacements" — plus the OPEN-column
discipline question § 3.1 counts. What separates it from FAIL: 0 silently
resolved HIGHs, 0 invented facts or OPEN entries, 221/222 all-report and
187/188 ESTABLISHED citation substance, 0 false alarms, high inter-agent
stability.

**And the verdict's scope is the producer half.** The estate's recorded bar
for § 4.8 is a fresh agent that produces **and scores**
(`2026-08-09-intent-map-replay.md:166`; the fm #830 disposition) — this run
discharges the producing half and leaves the scoring half open, so nothing
here marks the prescribed test complete (§ 1.5; Codex round 1, conceded).

What the producer half establishes that the walkthrough could not:

1. **The map's provenance separation survives fresh hands.** Five agents who
   never saw the outcomes kept EXPLICIT / ESTABLISHED / DERIVED / OPEN
   distinguishable — with the one countable softness being where
   decided-LOW/MEDIUM items are parked (§ 3.1), which traces to an ambiguity
   in the procedure's own step 4 as much as to the maps.
2. **Retrieval-based resolution outperformed the author's own map once** —
   fragment 7's HIGH dissolves under the retrieval the procedure itself
   mandates. The § 4.8 fear (a fresh agent silently resolving what the author
   knew to ask) did not materialise; the observed failure direction is
   consistently the *scorer's* (§ 3.1's false fabrication alarm and mislabeled
   metric, § 1.3's wrong pin inventory, § 3.3's hindsight anchor — three of
   the four found by the adversarial reviewer, one by the checker's positive
   control).
3. **The residual defect class is mechanically checkable.** Twelve of the
   thirteen D1 defects are one kind — a citation range that does not carry
   the claimed content — exactly what `tools/gemini_delegate.py` already
   verifies for delegated reads; a cite-check pass over a map's rows would
   have caught 12/12 of them (not the miscount). Recorded as a candidate
   mechanism under the promotion rule (§ 6 of the roadmap): observed and
   measured here; **not built** — one run is not "test against real cases"
   for the checker itself.
4. **One procedure defect:** step 4 classifies "every unresolved item" but
   the report format gives decided items no column, so agents park them in
   OPEN (§ 3.1). A one-line clarification in `intake` (decided LOW/MEDIUM
   report under DECISIONS FLAGGED, never OPEN) would close it; left for the
   round that amends the skill, since this PR already touches its replay
   note.

## 5 · Honest nulls

- **The scorer half of § 4.8 has not run** (§ 1.5) *(closed 2026-08-13: it ran
  blind ×2 and confirmed the band —
  [`2026-08-13-intent-map-fresh-scorer.md`](2026-08-13-intent-map-fresh-scorer.md))*
  — the estate's recorded bar
  is produce **and** score, and this session's scoring, however bounded
  (pre-registered rubric with commit-order proof, mechanical checks, committed
  raw outputs, adversarial review on this PR), is not a fresh agent's. Codex
  round 1 demonstrated the residue concretely: four scorer-side errors in the
  first push of this very file.
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
