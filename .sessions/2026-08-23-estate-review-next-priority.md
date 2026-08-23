# 2026-08-23 — Estate review: what is most important to work on next

> **Status:** `complete`

- **📊 Model:** opus-5 · high · review/verify

## 💡 Session idea

Owner ask, verbatim: *"review the feet manager and tell me what you think is
currently the most important thing to work on"*. A judgement question, so the
deliverable is a recommendation with its evidence — not a change. This card
exists because the measurements below were taken here and would otherwise live
only in the chat transcript, which this repo's own read path has already lost a
plan to once (boot file, entry 1b).

**No repository content was changed this session.** The only tree delta besides
this card is `.substrate/guard-fires.jsonl`, the expected telemetry append from
running the gate.

## previous-session review

⟲ fm #914 (`b881f29`, HEAD): the guard-fires delta from the R5 verification
runs. Checked at `main` — present, and the branch for this session sits exactly
at `origin/main` (`git rev-list --left-right --count origin/main...HEAD` → `0 0`).
Nothing to repair.

## What was verified live (not read off a doc)

- **Estate state matches the records.** `GET /user/repos` → **26 repositories,
  9 archived, 0 deleted**; the nine are exactly R5's ungated list, and the three
  gated rows (`superbot-next`, `superbot-plugin-hello`, `product-forge`) are
  untouched and still active.
- **The superbot automation churn is genuinely stopped.** ~60 auto-merged
  `chore(dashboard): refresh generated data` PRs ran to 2026-08-14T11:13Z and
  stop at sb #2446; the `ci-rerun-watchdog` / `pr-conflict-guard` schedules stop
  at `2026-08-20T23:02Z`, matching sb #2450's merge at `23:17Z`. Only
  `Postgres backup (daily)` still fires. Both retirements did what they claimed.
- **`python3 bootstrap.py check --strict` → real exit 0** on `main`, read
  directly, never after a pipe.

## The finding — the trap-delivery gap

The estate built a moment-of-action delivery mechanism and pointed almost all of
it at reference material rather than at its own recurring execution mistakes.

| measurement | value | how |
|---|---|---|
| doc-routes installed | **55** | `doc-routes.json` |
| …mentioning "pipe" or "exit code" | **0** | `grep -ic` on the route file |
| …mentioning "badge" | **0** | same |
| …mentioning merge-conflict reading | **0** | same |
| session cards restating the exit-code-after-a-pipe trap | **26 of 389** | `grep -ril` over `.sessions/` |
| files containing `TRAP · TRIGGER · WHY · REQUIRED PREVENTION` | **1** | the roadmap that *designs* it (§ 5.4) |
| `.session-journal.md` here | **27 lines, 0 content** | pure placeholder headings |

And the practice demonstrably works where it was actually done — the same file
in sibling repos: **superbot 802 lines / 689 content · websites 125 / 85 ·
substrate-kit 74 / 52 · couch-legend 26 / 0 · fleet-manager 27 / 0.** The hub
that roadmap § 7 names as where estate methods get *proven* has the empty one.

**The corroborating case is in yesterday's own record**, not inferred: the R5
card (fm #912) says of an inherited lesson *"This is the previous card's carried
lesson landing again."* It had to be carried by hand from one card to the next
because no register exists. That is success criterion #2 —
*"the same class of mistake is never corrected twice"* (`intent.md` § 2) —
failing in the estate's most recent card.

This is the shape `findings/2026-08-08-why-rules-dont-bind.md` already measured
(116 committed statements across 66 files, **0** of 16 incidents caught): the
trap gets *restated*, never *delivered*.

## The recommendation

**Execute program step D3 as roadmap § 5.4** — harvest the recurring traps from
the corpus the estate already owns (389 cards · 52 findings · 101 audited
defects), register them in the structured form, and route the top ones through
the `route_docs` hook that is already built and measured working.

Why this one: it is simultaneously **D3** (Track D, priority 1 under OD-7) and
the concrete first slice of **roadmap Phase 3**, which **OD-13** is currently
pointing every session at — so it needs no new authorisation, is gated on
nobody, and fixes the one success criterion the estate is measurably failing.
The trap to avoid while doing it is producing statement #117: the value is the
lifecycle (mistake → trap entry → route → checker), not the document.

**Runner-up, and why it loses:** Phase 3 in full (`/documentation`, the procedure
registry, review-from-intent). Roadmap § 6's promotion rule explicitly warns
against *good idea → mandatory infrastructure everywhere*; § 5.4 is the slice
with real observed failures behind it.

## Context flagged to the owner, not acted on

- **Work has gone lopsided.** Merged PRs over the last 14 days: **fleet-manager
  86 · spider-swing 2** (`search/issues`, per repo). Spider Swing is the only
  asset with a live external signal, and its Play critical path has not moved
  since 2026-08-05. Some of the 86 was directed execution (the archives, the
  Railway cost cut) — but `intent.md` § 5's non-goal is *"an apparatus that needs
  maintenance sessions of its own"*.
- **The throughput constraint is owner-gated decisions:** eight open entries in
  the queue's current-decisions section, plus GCB-1 and the two Play items.
  `OQ-FM-D2-TARGET` is the root one — until D2 has a target, OD-13 is the
  standing fallback and every session routes back into the hub.
- **Time-sensitive:** E1 (his, by his own ruling — he said 08-22 he wanted it
  done *"today or tomorrow"*), and the archived-repo cron check due after
  2026-08-24 ~06:00Z (one call, recipe in the R5 card).

**Not done here, deliberately:** no trap register was written and no route added.
He asked what is most important, not for it to be built; which of the two moves
above he wants is his call.

## Verify

- `python3 bootstrap.py check --strict` → **exit 0**, read directly, never after
  a pipe.
- Telemetry delta: `git diff --numstat .substrate/guard-fires.jsonl` →
  **297 added / 0 deleted**; all 297 appended lines parse as JSON; zero conflict
  markers in the file.
