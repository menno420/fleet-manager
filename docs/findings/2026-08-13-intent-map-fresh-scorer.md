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

<!-- RESULTS -->

## 3 · The divergence table — blind scoring vs the committed § 3

<!-- DIVERGENCE -->

## 4 · Verdict

<!-- VERDICT -->

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
