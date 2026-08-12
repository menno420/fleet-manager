# § 4.8 fresh-agent test — raw record

> **Status:** `reference` · 2026-08-12 · evidence folder for
> [`../2026-08-12-intent-map-fresh-agent-test.md`](../2026-08-12-intent-map-fresh-agent-test.md).
> Everything here is either verbatim (agent outputs, prompts) or executable
> (checker + TSVs). Read the finding first; this folder exists so its claims
> can be re-derived.

## Inventory

| file | what it is |
|---|---|
| [`prompt-A.md`](prompt-A.md) / [`prompt-B.md`](prompt-B.md) | The agent prompt templates, verbatim. `{SNAPSHOT_DIR}` was filled with the pinned snapshot path; `{PROCEDURE}` with the live `intake` SKILL.md body minus its YAML frontmatter and minus the "Replayed against real owner messages" section (the redaction the finding's § 1.1 declares). |
| [`agent-A1.md`](agent-A1.md) [`agent-A2.md`](agent-A2.md) [`agent-A3.md`](agent-A3.md) | Case A (nine-fragment instruction, pin `7fbc065`) — three independent fresh agents, outputs verbatim |
| [`agent-B1.md`](agent-B1.md) [`agent-B2.md`](agent-B2.md) | Case B (OD-6 correction, pin `f53d7ea`) — two independent fresh agents, outputs verbatim |
| [`verify_citations.py`](verify_citations.py) | The D1(a) checker: whitespace-normalised needle search within each cited range ±3 lines of the pinned tree |
| [`citations-A1.tsv`](citations-A1.tsv) [`citations-A2.tsv`](citations-A2.tsv) [`citations-A3.tsv`](citations-A3.tsv) [`citations-B.tsv`](citations-B.tsv) | One row per ESTABLISHED citation per agent: `agent · file · range · needle`. The needles were chosen by the scorer from each agent's stated claim. |

Reproduce the snapshots: `git archive 7fbc065 | tar -x -C pinA` and
`git archive f53d7ea | tar -x -C pinB` (no `.git` — history is structurally
absent). Re-run: `python3 verify_citations.py <pin-dir> <tsv>`.

## Adjudication of every non-PASS checker row

First-run output: A1 45/51 · A2 53/55 · A3 50/54 · B1 30/32 · B2 29/30
(+ all negative/count specials as recorded below). Every non-PASS row was
opened and adjudicated; **needle/harness artifacts are scorer errors, not
agent errors**, and are separated as such:

| agent · row | adjudication |
|---|---|
| A1 `audit 229-314 "zero buttons"` | **PASS on inspection** — the 60/66 figure recurs inside the cited § 4b range as table rows (`66 | 60 — 91%` and `60 / 66`); the scorer's needle used a phrasing the doc doesn't. |
| A1 `playtest 116-129 "loaded extensions"` | **PASS on inspection** — the table row reads `Extensions | **61 loaded**`; needle word-order artifact. |
| A1 `CAPABILITIES 879-887` · A1 `decisions 21-39` | **PASS after whitespace normalisation** — sentence-wrap artifacts in the first harness version, fixed and re-run. |
| A1 `vertex-first 3-8 "at least this month"` | **substance PASS · 1 attribution imprecision** — A1's quotation is the owner's verbatim words, which live at `:144`; lines 3-8 carry the doc's own restatement ("at least for the rest of this month"). Quote right, line wrong. |
| A1 `decisions 41-55 "publish by default"` | **substance PASS** — D-0012 is at 41-55; A1's wording is the estate's standard label for it (the verdict text reads "Assume anything this estate produces may be public…"). A label, not a misquote. |
| A2 `.sessions/…audit 74-88 "wrong claims"` | **PASS on inspection** — the range carries the run-it lesson verbatim ("run it, and see whether anything happens"); scorer needle wrong. |
| A2 · A3 `vertex-first 142-146 "googleSearch"` | **substance PASS · 1 attribution imprecision each** — the camelCase fact is real at `:106-109`; both agents cited the section-end range instead. Two agents, same wrong range. |
| A3 `program 109 "after its adapters…"` | **PASS on inspection** — phrase present at 109; the markdown bold inside it (`**after**`) broke the substring. Harness artifact. |
| A3 `audit 64-91 "CAPTURE-WORLD"` | **substance PASS · 1 attribution imprecision** — the 58-name content is in-range (the `58` needle passed); the `CAPTURE-WORLD LITERAL` label sits at `:44/:49/:96`, just outside ±3. |
| A3 `CAPABILITIES 179-194` | **the one citation-overreach** — the entry's fact (Gemini fabricated 18 "decisions") is true and correctly cited to `gemini-delegation.md:34-48` (verified at `:37-41`), but the appended `CAPABILITIES.md:179-194` range is the free-tier corpus-read capability entry and does not carry the incident. Worst row in the run; nothing invented. |
| B1 `program 3-6 "…should churn"` | **PASS on inspection** — verbatim at lines 3-6; the blockquote `>` prefixes broke the join. Harness artifact. |
| B1 · B2 `CONSTITUTION 123-128 "live in-session"` | **substance PASS · 1 attribution imprecision each** — the quoted exception clause lives in the 37-42 region (both agents also cited it there, PASS); 123-128 is the propose-don't-apply section without the clause. Doubled range, one half wrong. |

Specials: `pinA`'s `SKILLS-local.md` **exists** (87 lines) and has **no**
"All 27" section (A1/A2/A3's negative claim PASS — and the finding's first
push wrongly described the whole file as absent; Codex round 1, fixed).
`pinA` has **27** installed skill directories (A1/A2 said 27 PASS; A3 said
26 — counted as an ESTABLISHED factual miscount per round 1).
`pinB/docs/decisions.md` carries no pace entry (B1/B2's negative claim PASS).
`docs/execution-surfaces.md` **exists** in pinA — the scorer suspected this
citation was fabricated and was wrong (recorded in the finding § 3.1 as a
scorer false alarm).

## Round-1 additions: the exact-range pass and the column-set partition

**Exact-range attribution pass** (Codex round 1: ±3 tolerance must not blur
attribution): `verify_citations.py --exact` scores each row against the cited
range with no tolerance. Rows that pass ±3 substance but fail exact — i.e.
content one-to-four lines away from where the agent said:
`A1 fleet-account:23-26` (at `:22`) · `A2 CAPABILITIES:884-887` (at
`:881-882`) · `A2 playtest:172-176` (at `:171`) ·
`B1 decision-capture:34-35` (at `:36`) · `B1 CONSTITUTION:17-18` (starts
`:16`). Exact totals: A1 46/51 · A2 51/55 · A3 50/54 · B 57/62. These five
plus the six substance-pass adjudications = the finding's **11 attribution
imprecisions**.

**Column-set partition** (Codex round 1: the TSVs encode citations from the
whole reports, not only ESTABLISHED — so the metric must say so). Rows whose
citation appears outside the agent's ESTABLISHED section, derived from each
report's own structure:

- **A1 (7):** `SKILLS.md 25` · `SKILLS.md 31` · `SKILLS-local 55` ·
  `SKILLS-local 56` · `SKILLS-local 44-46` · `CONSTITUTION 24-27` (all
  MAP TO METHOD) · `playtest 267-271` (NON-GOALS) → ESTABLISHED 44
- **A2 (5):** `audit 12-14` (NON-GOALS) · `audit 69-70`, `playtest 201-239`
  (DERIVED) · `program 90`, `program 106` (MAP TO METHOD) → ESTABLISHED 50
- **A3 (8):** `program 136-140`, `program 28`, `CLAUDE 21-23` (NON-GOALS) ·
  `audit 356-360`, `program 90`, `program 106`, `gemini-delegation 111`,
  `execution-surfaces 1-21` (MAP TO METHOD); `SKILLS-local 42-56` is kept
  ESTABLISHED (it anchors the recorded-absences inventory attached there)
  → ESTABLISHED 46
- **B1 (8):** `SKILLS-local 34`, `SKILLS-local 51`, `intake SKILL 66`,
  `roadmap 372-374`, `CLAUDE 154-160` (MAP TO METHOD) · `program 170`,
  `owner-reflection 28-31` (DERIVED) · `roadmap 107` (OPEN) → ESTABLISHED 24
- **B2 (6):** `SKILLS-local 39`, `SKILLS-local 34`, `CLAUDE 154-160`,
  `program 151-152` (MAP TO METHOD) · `program 172`, `program 173`
  (DECISIONS FLAGGED) → ESTABLISHED 24

Final tally used by the finding: **222 rows (188 ESTABLISHED · 34 other) ·
221 substance-correct (ESTABLISHED subset 187/188) · 11 exact-range
attribution imprecisions · 1 citation-overreach · 1 ESTABLISHED factual
miscount · 0 fabricated facts · 0 invented OPEN entries.**
