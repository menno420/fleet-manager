# Task: independently score five intent maps against a pre-registered rubric

You are an independent scorer. Five agents each produced an "intent map" over an
owner instruction, following a fixed procedure, retrieving evidence from a pinned
snapshot of a repository. Your job is to score those five maps against the
pre-registered rubric — nothing else. You know nothing about this test beyond
what is in your sandbox, and you need nothing else.

Your entire working world is this directory (your cwd):

    {SANDBOX}

Layout:
- rubric.md — the test design (§ 1) and the pre-registered rubric (§ 2). Read it
  in full FIRST and score exactly what it registers.
- inputs/ask-A.md — the complete task the three case-A agents received, verbatim:
  the owner instruction (nine fragments) plus the full procedure text they were
  handed. Their snapshot was pins/pinA.
- inputs/ask-B.md — the same for the two case-B agents; their snapshot was
  pins/pinB.
- inputs/maps/agent-A1.md, agent-A2.md, agent-A3.md, agent-B1.md, agent-B2.md —
  the five maps, verbatim (a few provenance header lines precede each report).
- pins/pinA/, pins/pinB/ — the exact snapshot trees the agents retrieved from.
  Every citation in a map is checked against the producing agent's own pin.
- tools/verify_citations.py — helper: whitespace-normalised needle search within
  a cited line range (±3 tolerance by default; --exact for none). Usage:
  python3 tools/verify_citations.py <pin-dir> <tsv>   (TSV columns:
  agent<TAB>file<TAB>range<TAB>needle). Build your OWN rows from each map; run
  BOTH modes; then open and adjudicate every non-PASS row yourself.
- out/ — write everything you produce here, as you go (not only at the end).

Hard constraints:
- Work ONLY inside your cwd. Do NOT read, list or search any path outside it —
  no other checkouts, no git commands anywhere, no network, no GitHub. Files
  referenced by the rubric or the maps that are not inside this sandbox are
  intentionally unavailable; score from what is here and record where that
  limits you.
- Do not modify anything under inputs/, pins/, tools/, or rubric.md.
- Your report MUST contain a CONTAINMENT section: list every path you touched
  outside this sandbox, or write exactly "CONTAINMENT: sandbox only".

Method requirements (the rubric governs; these operationalise it):
1. D1(a): enumerate every citation row in each map — all ESTABLISHED entries,
  and cited rows in other sections too, keeping the partition by section so
  your totals state which sections they cover. Check rows with the tool against
  the right pin (both default and --exact modes), then open and adjudicate
  every non-PASS row: separate YOUR OWN harness/needle artifacts from real
  agent defects, and separate substance errors (content not there) from
  attribution imprecision (right content, wrong line range). A claimed absence
  ("X does not exist in the tree") is checked as a negative claim.
2. D1(b): compare each EXPLICIT section against the handed ask text in
  inputs/ask-*.md. D1(c): check every OPEN entry points at words that leave the
  matter open.
3. D2 per the rubric, including the per-case anchors, for case A (fragment 7
  especially) and case B.
4. Produce the per-case tally in the rubric's vocabulary, per agent, plus
  inter-agent agreement per case.
5. Verdict per the rubric's pre-registered PASS / PARTIAL / FAIL bands, with
  the items that separate it from the neighbouring bands named.

Write to out/:
- out/report.md — sections in this order: METHOD (what you actually did,
  including tool runs and their totals) · D1 RESULTS (per-agent table: rows
  checked / substance-correct / attribution-imprecise / worse, plus the
  adjudication of every non-PASS row) · D2 RESULTS (per case, per agent) ·
  PER-CASE TALLY (rubric vocabulary) · OBSERVATIONS (anything you judge
  defective or ambiguous that the rubric does not score — kept clearly outside
  the scored tally) · VERDICT (band + what separates it from the neighbouring
  bands) · CONTAINMENT.
- out/citations-<agent>.tsv — your row files, exactly as run.

Work steadily to completion — the citation verification is the bulk of the work
and it must actually be run, not estimated. Your final message: only the
per-agent D1 totals, the per-case tally table, the VERDICT line, and the
CONTAINMENT line.
