# The § 4.8 fresh-scorer half — blind re-score of the five committed intent maps

> **Status:** `reference` · 2026-08-13
>
> [fm #851](2026-08-12-intent-map-fresh-agent-test.md) ran the producer half of
> roadmap § 4.8: five fresh agents produced intent maps, and the running
> session — which had read the outcomes — scored them (verdict PARTIAL). The
> estate's recorded bar is a fresh agent that produces **and scores**
> ([`2026-08-09-intent-map-replay.md:166`](2026-08-09-intent-map-replay.md);
> the fm #830 disposition), so the scorer half is what this file runs: **two
> independent scorers with no access to the conversation, the adjudications,
> or any fm #851 summary re-score the five committed maps against the
> pre-registered rubric.** The deliverable is a comparison, not just a
> re-score — divergence between blind scoring and the committed § 3 scoring
> measures the prior scorer's outcome-knowledge bias, and *"the prior scoring
> was wrong"* was an admissible result.
>
> Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).
> Everything in § 2 is `MEASURED` against the raw scorer reports committed in
> [the evidence folder](2026-08-13-intent-map-fresh-scorer/README.md); § 3's
> adjudication layer is this session's and is labelled outcome-aware.

## 1 · Design

### 1.1 Structure — two blind scorers over all five maps

The committed § 3 scoring was one scorer over all five maps, so the blind
condition matches it: **each scorer scores all five maps**, keeping the only
varied factor outcome-knowledge. **Two** scorers run independently so that
fresh↔fresh agreement bounds scoring noise: if S1 and S2 disagreed with each
other as much as with the committed scoring, divergence would be noise, not
bias, and this file would have to say so. Both ran the same model id as the
producers and the prior scorer (`claude-fable-5`) — provider portability is
untested here, as in the producer run.

### 1.2 The input set — and what was withheld

Each scorer got a hermetic sandbox: the five raw maps verbatim · the two
producer ask-prompts verbatim (the maps are unscorable without the handed ask
and procedure text; they carry no adjudications) · the finding's §§ 1–2
design-and-rubric text with three redactions (below) · both pinned snapshot
trees rebuilt from the committed pins (`git archive 7fbc065` / `f53d7ea`) ·
`verify_citations.py` verbatim (reusable per the fm #851 decision — scorers
built their **own** rows). Nothing else, and no statement anywhere that a
prior scoring exists.

**Redacted out of the handed §§ 1–2:** § 1.5 entirely (it frames the prior
scoring arrangement and states the observed error direction), replaced by a
neutral scorer charge; and the two Codex-round parentheticals (§ 1.3's pin-A
cell, § 2's unscored-note sentence), each of which records what "the agents
had right" — outcome data. The corrected pin-A *facts* (SKILLS-local.md
exists, 87 lines, no roster section) were kept: they are properties of the
pinned tree the scorers could and did verify directly, not scoring outcomes.

**Withheld and physically absent from the sandboxes:** the finding's §§ 3–6,
the evidence README (every adjudication), the prior `citations-*.tsv` (they
encode the prior scorer's needle choices and known enumeration gaps), the
replay walkthrough, handoff-fidelity's prompt/verdict columns, and every
fm #851 summary surface.

### 1.3 Contamination control — probed, one leak measured, launch path changed

Full record: [`leak-probes.md`](2026-08-13-intent-map-fresh-scorer/leak-probes.md).
The short version: the mechanical grep of the assembled sandboxes was clean
after adjudication; but the **default launch path leaked** — a probe subagent
quoted the live boot file's entry 1b verbatim, producer verdict included, and
a working-tree neutralization of that line did **not** reach a second probe,
because subagents receive a `CLAUDE.md` snapshot captured at session start
(`MEASURED` — the on-disk edit was verified present while the probe still
received the original). So the scorers did not run as harness subagents at
all: they ran as **separate headless `claude -p` sessions rooted inside their
sandboxes**, a surface probed to carry no fleet-manager context and loading
no fleet-manager hooks. The classifier escalated both launches to the owner,
who approved them (one prompt per scorer).

### 1.4 The OPEN-column question, decided before launch

The OPEN-column-discipline criterion (three of five maps parking decided
LOW/MEDIUM items in OPEN) was added **post-hoc** in fm #851's Codex round 1 —
it is not in the pre-registered § 2 rubric. It was **not** handed to the
scorers: handing it would import the prior scorer's needle choice, the same
class the prior TSVs were withheld for. Scorers instead got a free
OBSERVATIONS section for anything the rubric does not score; whether a blind
eye independently finds the OPEN-parking is itself divergence data (§ 3).

## 2 · What the blind scorers returned

Both completed (exit 0), both attested `CONTAINMENT: sandbox only`, and both
reports were screened for knowledge only the live tree could supply — none
found, and each report *disagrees* with the committed scoring in places, which
is the behaviour a peeker would not produce.

| | committed § 3 (outcome-aware) | S1 (blind) | S2 (blind) |
|---|---|---|---|
| rows enumerated | 222 | 272 | 258 |
| substance-correct | 221/222 | 272/272 | 258/258 |
| attribution-imprecise | 11 | 4 | 8 |
| "worse" rows | 1 overreach + 1 miscount | 0 (+2 count errors noted) | 0 (+2 count errors noted) |
| invented OPEN · false alarms · fabrications | 0 · 0 · 0 | 0 · 0 · 0 | 0 · 0 · 0 |
| fragment-7 cell | evidence-resolved (not counted against agents) | partial ×3 | partial ×3 |
| A-1 cell | partial ×3 | partial ×3 | partial ×3 |
| case B | correction-handled ×2 | correction-handled ×2 | correction-handled ×2, "clean" |
| **verdict** | **PARTIAL** | **PARTIAL** | **PARTIAL** |

**Fresh↔fresh agreement is near-total**, which is what licenses reading
fresh↔prior divergence as signal rather than noise: S1 and S2 independently
returned the same band, the same PASS-separator (the registered A-7 anchor
unmet by all three case-A agents, explicitly *not silent*), the same two count
errors, the same case-B cleanliness, 0 fabrications each — and **each
independently derived, from the pin alone, the committed finding's own § 3.2
headline**: that the registered premise ("no retrievable definition in the
pinned tree") is contradicted by pinA's 2026-08-05 audit, whose § 4 uses
near-owner phrasing ("genuinely better-founded") with a discriminating test.
S2 went one further and named why the § 1.3 probe missed it: searching for the
*fragment strings* is a contamination check, not a definition-absence check.
Their divergences from each other are enumeration-sized only (272 vs 258 rows;
4 vs 8 imprecisions — overlapping sets, different needles).

## 3 · The divergence table — blind scoring vs the committed § 3

Rows ordered by what they say about the prior (outcome-aware) scorer.
Adjudications in the right column are this session's, **outcome-aware**,
grounded in the pinned trees wherever the question is mechanical.

| # | dimension | committed § 3 | blind S1 / S2 | adjudication |
|---|---|---|---|---|
| 1 | overall verdict | PARTIAL | PARTIAL / PARTIAL | **Confirmed, 3/3 scorings.** |
| 2 | what drives PARTIAL | citation-discipline defects; fragment 7 scored as the procedure *working* | the registered A-7 anchor unmet 3/3 (non-silent, evidence-excused), plus citation nits | **Real divergence in composition.** All three scorings agree on the facts (resolution was out-loud, citation-true, and the pin genuinely holds a seed definition); they differ on what the *registered* rubric then scores. The blind scorers applied the registered anchor as written; the prior scorer — who had itself established the dissolution narrative — created an unregistered "evidence-resolved" category and did not count f7 toward the verdict. Direction of prior bias: toward the agents / its own headline. |
| 3 | the f7 residual | § 3.2: *"Each agent additionally surfaced the residual reading choices … as MEDIUM decide-and-flag rows"* | both: the **definitional** residual (is the audit's operationalisation what the owner means by "genuinely better built"?) was flagged by **0/3** — the MEDIUM rows the maps carry are operational (write posture, deep-research route, games depth) | **Prior overstatement, confirmed against the maps.** The flagged residuals exist but are not the definitional one; S2's phrasing of what was missed ("adopting the audit's test as the definition — veto if you meant something else" would have cost one line) is exact. |
| 4 | D1(b) EXPLICIT purity | *"0 inferences dressed as EXPLICIT"* | both: all three A-maps attach a derived referent to fragment 3 **inside EXPLICIT** ("Read superbot's files…" / "In superbot:" / "In it,"), each also declaring the same inference in DERIVED | **Prior zero too clean — mechanically verified** (the handed fragment 3 names no repo). Mitigation is real (the DERIVED declarations), so both blind scorings grade it a labelling gloss, not smuggled inference — but a blind eye found it twice and the outcome-aware eye scored a clean zero. |
| 5 | the prior's worst-defect row (A3 E16's appended `CAPABILITIES.md:179-194`) | "citation-overreach … does not carry the incident. Worst row in the run" | both enumerated the row, needled it on the entry's *contract clause* (`gemini_delegate`), and **passed** it | **The prior call does not survive blind re-scoring.** The pinned range's tail carries E16's principal claim verbatim ("Delegated output is only usable through the citation verifier in `tools/gemini_delegate.py`"); only the parenthetical incident is out-of-range, and that half is separately and correctly cited to `gemini-delegation.md:34-48`. Re-graded: a compound-entry attribution imprecision at most, not the run's worst defect. One of the two rows separating the committed 221/222 from a clean sweep was the *scorer's* severity, not the agent's error. |
| 6 | count errors | A3 "26 installed" (vs 27) — counted; **A2 "14 kit rows" — missed** | both found A3's *and* A2's (actual: 10 rows — re-verified this session against pinA) | **Prior miss, found twice blind.** |
| 7 | attribution-imprecision count | 11 | 4 / 8 | **The count is scorer-relative (4–11 for the same five maps); the class finding is stable.** A shared core recurs across scorings (A1 `fleet-account` off-by-one · A2 `playtest:171` · A2 `CAPABILITIES:881` · B1's two offsets); the prior-only rows (`googleSearch` ×2, the doubled B-ranges, "at least this month") were exonerated by both blind scorers under entry-level support — notably, the strict per-range standard behind those rows was imposed by Codex round 1, and neither blind scorer chose it unprompted; the blind-only rows (A3 `fleet-account:39`, B2's churn off-by-one) are new finds of the same small-offset class. |
| 8 | OPEN-column discipline (post-hoc criterion, withheld from scorers) | counted: A1 ×2 · A2 ×3 · A3 ×3 · B2 inline | S1: not flagged; S2: flagged **B2 only** (its observation 8, unprompted, recommending exactly the fix this PR ships in `intake`) | **Partial independent convergence.** The criterion is real — a blind eye re-found its clearest instance — but its full A-map salience was review-round-specific, which supports having kept it out of the handed rubric. |
| 9 | defects nobody had | — | A1's no-deploy quote trimmed of its "for this" scope (S1 **and** S2, independently) · interpretive asides inside ESTABLISHED rows (S2: A2's E2, B1's OD-3 aside) · A1's undefined "LOW→MEDIUM" class label (S1) | **New, verified against the maps and pins.** Two blind eyes finding new true defects in maps scored twice before is the strongest argument in this file for scorer freshness as a standing practice. |
| 10 | unanimous ground | 0 fabricated citations · 0 invented OPEN · 0 false alarms · 0 *silent* HIGHs · case B correction-handled 2/2 · A-1 partial ×3 | same / same | **The load-bearing § 4.8 quantities are scorer-independent.** Every scoring, blind or outcome-aware, lands the same zeros on the failure classes the test exists to catch. |

## 4 · Verdict

**The committed PARTIAL is CONFIRMED at band level by two blind scorers — and
the § 4.8 bar (a fresh agent produces AND scores) is now met on both halves**
(producer: fm #851; scorer: this run). With that confirmation comes the bias
measurement the comparison was for:

1. **The prior scoring was substantially right and wrong in four named
   places** — two lenient toward the agents/its own narrative (rows 2–3), one
   too clean (row 4), one over-harsh against an agent (row 5), plus one miss
   (row 6). Net direction: the outcome-aware scorer under-scored the one
   dimension where it had authored the exculpatory story (fragment 7) and
   over-scored severity where strictness had been reviewer-imposed (rows 5,
   7). That is a measured, specific shape of outcome-knowledge bias — not
   enough to move the band, enough to change what the PARTIAL *means*.
2. **Scorer enumeration is itself scorer-relative** — 222 vs 258 vs 272 rows,
   imprecision counts 4–11 — in both directions: the blind scorers found true
   defects the prior missed, and the prior's per-range strictness produced
   rows both blind scorers decline. Any future single-number citation-accuracy
   claim from one scorer should be read with this spread in mind.
3. **The stable core is exactly the § 4.8 failure surface**: fabrications,
   invented OPENs, false alarms, silent HIGHs — 0 across all three scorings.
   The Phase 2 intent-map mechanism's claim now rests on fresh production
   *and* fresh scoring, and what it earns is unchanged in substance from
   fm #851's reading: provenance separation survives fresh hands; the
   dominant real defect class is small attribution offsets; and the registered
   A-7 branch was mis-premised, so **the HIGH-survives-retrieval branch is
   still demonstrated by zero committed cases** — a null now endorsed
   independently by both blind scorers (S2: a clean A-7 signal needs a pin
   that genuinely lacks the seed).

## 5 · Honest nulls

- **Containment is instructed and self-attested, not enforced** — the live
  checkout holding all outcomes stayed readable by a disobedient scorer
  process; each report's CONTAINMENT attestation and a post-hoc screen for
  impossible knowledge are the checks that ran ([`leak-probes.md`](2026-08-13-intent-map-fresh-scorer/leak-probes.md) § 6).
  The producer run's § 5 null, inherited and sharper.
- **n = 2 scorers.** Counts, not rates. Two agreeing blind scorers bound the
  noise story but do not measure scorer variance in any distributional sense.
- **Same model family and id throughout** — producers, prior scorer, blind
  scorers. A different-provider scorer is the untested next rung.
- **The § 3 adjudication layer is outcome-aware** — where the blind scorers
  and the committed scoring disagree, the classification of *who is right* was
  made by this session, which has read everything. Mechanically checkable
  disagreements are settled by the pinned trees; judgement calls are labelled.
- **The sandbox path string names the repo directory**
  (`-home-user-fleet-manager`), a residual identity hint; the scorers'
  reports show no use of it.

## 6 · The run, reproducibly

Committed in [`2026-08-13-intent-map-fresh-scorer/`](2026-08-13-intent-map-fresh-scorer/README.md):
the handed rubric verbatim (`rubric-handed.md`), the scorer prompt template
(`scorer-prompt.md`, `{SANDBOX}` slot), the leak-probe record
(`leak-probes.md`), both raw scorer reports verbatim (`scorer-1.md`,
`scorer-2.md`), and both scorers' own citation TSVs. Snapshots reproduce from
the pins: `git archive 7fbc065` / `git archive f53d7ea`. The launch command
shape is recorded in `leak-probes.md` § 4.
