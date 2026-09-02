# 2026-09-02 — night fleet EAP mail evidence report (Fleet A + Fleet B)

> **Status:** `complete` — seventeen Codex rounds landed (the tally and the
> per-round record live on `docs/findings/data/workflows/05-CONTRACTS-night.md`'s
> EXTERNAL line, the one place they are kept), every finding fixed or
> explicitly disclosed. Round 17 answered on `8470c9d` with one card-sync
> finding and no report defect; the owner then stopped the loop live
> (*"a maximum of 3 review rounds at most, never more"*), and the landing
> session — a different model family — reviewed that head against the
> retained JSON itself, made two verified edits, and flipped this card with
> **no eighteenth round** (EXTERNAL line, flip-session entry; the cap itself
> lands as a denying hook in the follow-on PR — `docs/traps.md` TRAP-009,
> [D-0039]). Fleet A: 12
> survivors, 3 judged spines (unanimous on which spine won, not on every
> graft recommendation — see the report's § 7 correction, round 2). Fleet
> B: pilot 4 survivors, full
> fleet-manager-only run (`skipSatellite: true`) 3 survivors — 2 of the
> pilot's 4 did not survive the full run, by two different mechanisms, not
> one shared cause (only L08 depended on the cut superbot reader; L02's
> loss traces to the pilot's merge stage, not any cut — see the report's
> § 3, corrected round 15). Both
> fleets' critics converge: the primary source behind the pass's strongest
> false-done rows (`docs/findings/night-review-2026-07-10.md`) was never
> read by either fleet's READERS (verifiers reached it directly in some
> cases). **Read the report itself, not this summary** — Codex caught real
> inaccuracies in earlier drafts of this very summary-writing, twice.

- **📊 Model:** sonnet-5 · xhigh · research
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_014jGUwuZnmtEFUmXNerNyV8](https://claude.ai/code/session_014jGUwuZnmtEFUmXNerNyV8) · "Night fleet audit and EAP report"

## Mission

Continuation of fm #1009 — the owner's night-fleet brief: run the fleet-preflight-contracted
evidence pass (Fleet A, the 2026-09-01 pilot-validated script rerun unchanged)
plus a newly authored EAP false-done ledger fan-out (Fleet B), producing one
verified audit report for tomorrow's final EAP mail and the successor repo.
Owner asleep; no owner-facing decision made, only evidence assembled.

## What ran (see `docs/findings/data/workflows/05-CONTRACTS-night.md` for the full contract sheet)

1. **fleet-preflight run** — demand test measured this container's concurrency
   at **2** (not the pilot's 6), which redrove every size decision after it.
2. **Fleet A** (`04-eap-mail-evidence-pass.js`, unchanged except args) — 84
   agents, 7.84M tokens, 156.5 min, run `wf_bda232c1-cf5`. 12 survivors, 4
   non-survivors with reasons, 3 spines judged (unanimous winner), 1
   completeness critic (found real defects in the survivors — see the report).
3. **Fleet B pilot** (3 reader units) — 37 agents, 2.66M tokens, 38.4 min, run
   `wf_d0348386-8b6`. Ran concurrently with Fleet A by mistake — cost Fleet A
   wall-clock via shared slots, named honestly in the report rather than
   hidden. 4 survivors (false-done rows), 1 unresolved same-mechanism
   split-verdict.
4. **Fleet B full run**, scoped to the fleet-manager-only lane (32 superbot
   reader units cut first, per the night brief's own cut order) — run
   `wf_fb35b278-362`, 83 agents, 7.11M tokens, 146.7 min. 505 claims/332
   corrections → 150 merged → 30 ranked → 28 verified → **3 survivors**. Two
   of the pilot's four survivors did not carry into these 3 — **not a
   scaling or method result**: the two corpora are not nested, and L02 only
   existed because the pilot's merge stage violated its own no-manufacture
   contract (the report's § 3 has the two non-comparable outcomes; this
   sentence was corrected at the flip, Codex round 17's one finding): **L08**
   (self-arming routines) re-entered the claim pool
   and was actively refuted, reappearing as **FD-13**, refuted; **L02**
   (venture-lab's Stripe false-green) never re-entered the claim pool at
   all — it survives only as four unmatched `orphaned_corrections` entries,
   never merged, ranked, or verified. See the report's § 3 for the full
   correction (Codex review round 9, mechanism refined round 15: L02's
   claim was a merge-stage invention from an orphaned correction, not a
   reader or corpus-cut effect).
5. **CUT: Fleet C** (19-repo closeout audit) — not attempted; no wall-clock
   left at measured concurrency 2.

## Report

`docs/findings/2026-09-02-eap-mail-evidence-report.md` — corpus census,
verified findings drawing on verifier `corrected_claim` text (quoted
directly for most rows; synthesized from the row plus both lenses' records
where two lenses' corrections needed combining; quoted from the retained
original candidate where a `corrected_claim` was itself unusable — the
report's own front matter says which applies to which row; never the raw
merge wording alone), the false-done ledger, the prior-mail overlap map, the
owner's words, all three judged spines, and — most load-bearing — **both
fleets' completeness critics, summarized** (full detail in the raw JSON, not
reproduced in the report itself — the report says so explicitly), because
both found real unfixed defects in their own survivors (stale arithmetic,
drifted citation line anchors, one corrupted claim field, the owner's own
stated top priority for
this mail present in zero of the three spines). The report says plainly:
read § 5 before drafting anything from this.

## Verify

`python3 bootstrap.py check --strict` — exit 1 with only the born-red hold
before the flip (landing session, 2026-09-02), exit 0 after it. The pre-flip
edits were verified by the landing session directly against the retained
JSON and the cited files, plus one free-key Gemini pass over the diff
([D-0019]: the four source-anchored claims SUPPORTED, none CONTRADICTED,
five not judged because no excerpt was supplied for them — each of those
five was checked directly instead).

⚑ decide-and-flag: none — no owner decision was made tonight, only evidence
assembled, per the brief's own "no mail text drafted tonight" rule.

💡 Session idea: none new this session.

⟲ Previous-session review: fm #1009 (2026-09-01) landed the pilot cleanly and
handed off precisely — its contract sheet, script and owner-direction record
were exactly what this session needed to start without re-deriving anything.

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached this
session).
