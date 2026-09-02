# 2026-09-02 — night fleet EAP mail evidence report (Fleet A + Fleet B)

> **Status:** `in-progress` — Codex round 2 (10 more findings) landed on
> `76834c8` and is fixed in the working tree below, but that fix is not yet
> reviewed on its own head (a review binds the SHA it ran on, TRAP-006/007)
> — pushing this commit with the card still `in-progress` keeps the
> born-red hold active while round 3 is requested and awaited. The flip to
> `complete` is a separate, later commit, once a round confirms clean on
> the exact head that ships it. Fleet A: 12 survivors, 3 judged spines
> (unanimous on which spine won, not on every graft recommendation — see
> the report's § 7 correction, round 2). Fleet B: pilot 4 survivors, full
> fleet-manager-only run (`skipSatellite: true`) 3 survivors — 2 of the
> pilot's 4 did not survive the full run; the two corpora are not nested
> (the full run cut the one superbot reader both depended on), so this is
> not clean evidence of scaling or verifier instability either way. Both
> fleets' critics converge: the primary source behind the pass's strongest
> false-done rows (`docs/findings/night-review-2026-07-10.md`) was never
> read by either fleet's READERS (verifiers reached it directly in some
> cases). **Read the report itself, not this summary** — Codex caught real
> inaccuracies in earlier drafts of this very summary-writing, twice.

- **📊 Model:** claude-sonnet-5 · xhigh · research
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
   of the pilot's four survivors (venture-lab Stripe false-green,
   self-arming routines) did **not** survive the larger corpus — kept in the
   report as a method finding, not smoothed away.
5. **CUT: Fleet C** (19-repo closeout audit) — not attempted; no wall-clock
   left at measured concurrency 2.

## Report

`docs/findings/2026-09-02-eap-mail-evidence-report.md` — corpus census,
verified findings quoted from verifier `corrected_claim` text (never the raw
merge wording), the false-done ledger, the prior-mail overlap map, the
owner's words, all three judged spines, and — most load-bearing — **both
fleets' completeness critics, summarized** (full detail in the raw JSON, not
reproduced in the report itself — the report says so explicitly), because
both found real unfixed defects in their own survivors (stale arithmetic,
drifted citation line anchors, one corrupted claim field, the owner's own
stated top priority for
this mail present in zero of the three spines). The report says plainly:
read § 5 before drafting anything from this.

## Verify

`python3 bootstrap.py check --strict` — to be run before the flip; expect the
born-red card hold as the only pre-flip red.

⚑ decide-and-flag: none — no owner decision was made tonight, only evidence
assembled, per the brief's own "no mail text drafted tonight" rule.

💡 Session idea: none new this session.

⟲ Previous-session review: fm #1009 (2026-09-01) landed the pilot cleanly and
handed off precisely — its contract sheet, script and owner-direction record
were exactly what this session needed to start without re-deriving anything.

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached this
session).
