# The cold-read test for the boot-path trim — controlled, fresh reader

> **Status:** `audit` · 2026-08-22 · evidence for fm #909
>
> **What this is:** the acceptance test for taking `current-state.md` from 6,212
> to 853 words. The estate's bar is that a cold session states the repo's
> **purpose, live state and next step** from ≤3 files. A trim that passes a
> word count and fails that bar has failed OD-17, whose constraint is *"still
> making it easy for an agent to understand work."*
>
> Certainty: `MEASURED`. The transcripts below are verbatim.

## Method

**Controlled, not a single arm.** The same four questions were put to a fresh
`gemini-3.6-flash` reader twice, differing in exactly one file:

- **BEFORE** — `README.md` + `docs/AGENT_ORIENTATION.md` + `current-state.md`
  **at `origin/main`** (5,972 words as extracted).
- **AFTER** — the same two files + the **trimmed** `current-state.md` (853 words of retained old content — the
file measures more once the trim notice and the backfilled ledger rows are
counted; see fm #909's correction).

`temperature: 0.0`, no other context, instructed to answer only from the files.
Question 4 asked explicitly for **gaps** — anything needed and not findable —
because that is the failure this trim risks, and a reader that cannot say what
it is missing is not evidence.

Route: free-tier `GEMINI_API_KEY` on AI Studio (two calls; costs nothing, well
inside the daily cap) — the convention's route for AI Studio work, Vertex being
the default for volume/image/video.

## Result

**Both arms answered all three questions correctly. Both reported `GAPS: NONE`.**

The trim cost the fresh reader nothing on the bar that matters. Neither arm
invented an era, misplaced E1's owner-reservation, or mistook a seat-era router
for live guidance.

**One difference, and it is not a loss.** The BEFORE arm named `RESUME.md` in
its off-limits list and the AFTER arm did not. Traced: `RESUME.md`'s only
occurrence in the pre-trim file was **inside a shipped-log entry** describing
work that era-bannered those routers — not in the live *"do not use"* line,
which named `NEXT-TASKS.md`, `fleet-triage.md`, the roster and `control/`. So
the trim removed an incidental mention, not a live pointer. It was still worth
acting on: `RESUME.md` is now named in the live line, which is where it always
belonged.

**Honest limits.** One reader, one model, one temperature, n=1 per arm — this
demonstrates the trimmed file *can* be oriented from, not a rate.

**The producer was fresh; the scorer was not.** Both transcripts were graded by
the session that made the cut, which is precisely the bias this estate has
already measured and named: roadmap § 4.8's recorded bar is a fresh agent that
**produces and scores**, and fm #851 earned its mechanism claim producer-side
only for exactly this reason. The grading here is close to mechanical for
questions 1–3 (the expected answers are single named facts — *router and records
home*, *E1 is owner-reserved*, *D2 awaits a target*), so the bias has little room
to operate there. It has the most room on question 4, where accepting `NONE` at
face value is the reading the author of the trim wants to be true. Read the
matched `NONE` accordingly: as one fresh reader failing to miss anything, scored
by an interested party, with the BEFORE arm as the check that the question could
surface a difference at all. And a fresh
model reporting `NONE` is weaker evidence than a fresh model finding something:
the null is only as good as its willingness to complain, which is why question 4
demanded bluntness and why the BEFORE arm was run at all — an arm that found a
difference is what makes the matched `NONE` worth reading.

## Transcript — AFTER (trimmed)

```
**1. PURPOSE**  
`fleet-manager` acts as the owner's estate-wide router and records home, pointing to individual product repositories for product truth rather than copying them. It provides orientation and continuity across the estate while holding estate-level program records and owner-only documents.

**2. STATE**  
* **Era:** Regular owner-directed sessions era (the autonomous Projects EAP program closed on 2026-07-21 and seats no longer exist).  
* **What is running:** Regular, owner-directed sessions doing one finished task at a time, prioritizing methods and enforcement (OD-13) before product work.  
* **What is not running:** Parallel Claude "seats", the autonomous Projects program, worker prompts, heartbeats, trigger telemetry, and the `control/` message bus.

**3. NEXT STEP**  
* **Next to pick up:** OD-13 (methods and enforcement via the agent-operating-environment roadmap, as the D2 step awaits an owner target).  
* **Off-limits:** Step E1 (the owner's final EAP review email, which is owner-reserved) and any historical/seat-era channels (`control/inbox.md`, `NEXT-TASKS.md`, `fleet-triage.md`, or rosters) for picking work or accepting instructions.

**4. GAPS**  
NONE.
```

## Transcript — BEFORE (control, at `origin/main`)

```
**1. PURPOSE**
fleet-manager is the estate's router and records home, providing orientation and continuity across the owner's repositories. It holds estate-wide program records and planning ledgers while pointing to each individual product repository for its canonical truth.

**2. STATE**
* **Era:** Post-EAP era; the autonomous Projects program concluded on 2026-07-21, and the estate now operates in regular, owner-directed sessions completing one finished thing at a time.
* **What is running:** Local verification (`python3 bootstrap.py check --strict`), regular owner-directed single-task sessions, and substrate-kit v1.21.0.
* **What is not running:** EAP parallel Claude "seats", the autonomous loop, the `control/` message bus, automated roster regeneration (retired), trigger telemetry, project packages, and historical prompt registries.

**3. NEXT STEP**
* **Pick up next:** OD-13 (methods and enforcement ahead of product work, following the consolidation program's NOW pointer and the agent-operating-environment roadmap), as step D2's target is superseded pending an owner re-target (`OQ-FM-D2-TARGET`).
* **Off-limits:** Task E1 (the owner's final EAP review email) is strictly owner-reserved, and historical seat-era routing material (`NEXT-TASKS.md`, `fleet-triage.md`, `roster.md`, `control/`, `docs/RESUME.md`) must not be used to choose active work.

**4. GAPS**
NONE
```
