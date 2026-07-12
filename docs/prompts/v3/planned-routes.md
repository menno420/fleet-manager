# prompts v3.3 — planned routes (keywords/expansions with no durable home yet)

> **Status:** `plan`
>
> v3.3 rebuild follow-up ledger (integration PR, 2026-07-12; drafted by the
> v3.3 CI drafting pass). Every route used in the 8 shipped v3.3 Custom
> Instructions exists on disk TODAY (verified in the local seat-repo clones @
> 2026-07-12 HEADs) — with one tracked half-exception: the superbot-2.0
> ORDER-grammar route resolves in superbot-next only (the superbot repo has
> no control/README.md; the CI names the resolving repo inline, and the §A
> row below tracks the durable fix). This file tracks (a) keywords whose CURRENT route is a
> stopgap that should be replaced by a durable home, and (b) content
> deliberately NOT given a CI dictionary entry because its v3.3 home is the
> EXPANDED STARTUP — listed so nothing falls between the two layers. Work an
> item → strike its row with a pointer to the PR that homed it (append-style
> edits; never silently delete a row).

## A. Stopgap routes that need a durable home

| Keyword(s) | What the expansion should say | Current (real) stopgap route | Proposed durable home | Seats needing it |
|---|---|---|---|---|
| deny-wins / one-attempt, INJECTION GUARD, backpressure / budgets, claim (CLAIMS rider detail), GIT HYGIENE, TOOL FACTS, TRUTH bar (+TIMESTAMPS), Q-0120, ratification park, outbox/Q-0264 CONTROL BUS text | The full rider texts these entries compress | `CORE` = fm `docs/prompts/v3/custom-instructions-core.md` (kept in v3.3 as reference doctrine — superseded as a CI assembly source, its rider block frozen @ 95b5c8f; the expanded startups now also carry the texts verbatim) | (a) UNIVERSAL v4→v5 hoist (owner sitting; bundle staged at fm docs/proposals/universal-v5-hoist-bundle-2026-07-11.md), or (b) a kit-shipped docs/doctrine/fleet-riders.md distributed on the next release | all 8 |
| ~~merge-on-green~~ **STRUCK 2026-07-12 (v3.4 delta 5)** | ~~The GITHUB_TOKEN merge-on-green workflow itself (reference implementation)~~ LANDED: sim-lab ORDER 003 executed — the workflow is INSTALLED and live (sim-lab #50; self-landings #50–#52); the v3.4 CI route now reads "(reference: sim-lab, live)" | was: prose only in UNIV ("none committed yet") | homed: sim-lab `.github/workflows/` (the live reference); remaining installs are seat work — websites is superseded (enabler #167 live) | still enabler-less: fleet-manager, game-lab (both repos), superbot-2.0 (superbot-next), superbot-world (games/idle) |
| routine-fired / cutover keyword cluster → docs/ROUTINES.md | The fired-session/cutover doctrine's routed doc home (wedge signature, manual-fire trap, blind-window check — the v3.4 BOOT-4 text's durable expansion) | v3.4 startups BOOT 4 EXCEPTION + BOOT 3a (prompt-carried only) | route a CI keyword + startup pointer to each repo's docs/ROUTINES.md **when a kit release ships kit #287** (merged, UNRELEASED at v3.4 restamp — do not route to a file adopters don't have) | all 8 |
| kit: line (heartbeat grammar) | The exact plain-form `kit:` line grammar + why bold breaks KIT_LINE_RE | kit:src/engine/grammar.py (code, not doc); v3.3 startups now carry the rule in HEARTBEAT | a grammar section in each repo's control/README.md — v3.2 defect #8's routed-doc half | all 8 |
| ORDER grammar / outbox for the superbot repo | control-bus grammar readable from inside superbot | the CI entry routes to "control/README.md per repo" — resolves in superbot-next only; superbot control/ has NO README | add superbot control/README.md (kit upgrade or manual) | superbot-2.0 |
| WALLS / DISCOVERY for the superbot repo | superbot's own capabilities/walls ledger | .session-journal.md quick reference (real, but pre-kit) | create superbot docs/CAPABILITIES.md when superbot upgrades to a kit release | superbot-2.0 |
| TOOL FACTS raw-text / stub-200 / quota-vs-scope, per-repo copies | one-paragraph appends so each repo's CAPABILITIES ledger carries the tool walls locally | CORE + the expanded startups only | append to every seat repo docs/CAPABILITIES.md | all 8 |
| model line — the "no secrets in any repo" half | secrets rule with local enforcement pointer | .sessions/README.md model-line doctrine (covers the model half only); v3.3 startups carry the full rule in TRUTH | CAPABILITIES/CONSTITUTION append per repo | all 8 |
| CSRF floor | the full CSRF/Origin-check floor with examples | websites control/inbox.md CSRF ORDER thread + the v3.3 websites startup's ⚠ CSRF FLOOR line (an inbox is a poor durable home) | websites docs/CAPABILITIES.md or a docs/conventions.md | websites |

## B. Deliberately NOT in the CI — homed in the EXPANDED STARTUP

qa-map rows homed **ES**; the CI stayed silent (or one-clause) on these to
hold the 8,000 budget. The expanded startups CARRY them (verified, all 8, in
the v3.3 integration PR) — this table records the split so a future CI trim
or startup edit doesn't orphan a row:

| Item | qa-map row | Note |
|---|---|---|
| redirect rule (owner redirect pre-empts NEXT slice; budget directive binds durably) | 13 | dropped from CI in final budget pass; startups § WORK-LOOP RIDERS |
| GEN-3: ONE trigger-MCP call per worker | 24 | startups § GEN-3 HYGIENE + inlined ender step 3; also rides D |
| GEN-3: cleared env (`env -u`) + smoke gate for spawned CLIs | 25 | was the HIGH loss risk — CI carries nothing; startups § GEN-3 HYGIENE |
| empty-vehicle merge check (diff the merge commit) | candidates A | startups § LANDING + inlined ender step 1 |
| calibration recital | candidates B | startups closing line |
| verify by event type (universal form) | qa 64/A LANDING | CI keeps it only inside the business-cron entry of websites / self-improvement / venture-lab; other 5 seats rely on the startup § LANDING |
| OWNER OVERRIDE reversible-path rule | 7 | startups § QA RIDERS (ES-only per qa-map) |
| conflicting-own-PR full procedure, ENV-DEGRADED full ladder | 18, 19 | CI has the one-line GIT HYGIENE compress; full text = startups § GIT HYGIENE |
| worker-stall once/twice ladder full text | 15 | CI one-line in backpressure/budgets; startups § WORK-LOOP RIDERS |
| fresh-session-per-fire business-cron clause (v3.2 defect #7 — CLOSED in v3.3) | 35 | startups BOOT 4 EXCEPTION + ender step 3(b); CI one-clause in the business-cron entry (3 seats) |
| MCP-PR-read staleness (v3.2 defect #9 — CLOSED in v3.3) | 37 | startups § TOOL FACTS extension; CI one-clause in TOOL FACTS |

## C. Fact-sheet corrections found while verifying routes (2026-07-12)

- superbot-idle PLATFORM-LIMITS.md is at the repo ROOT (like sim-lab), NOT
  docs/ — the seat fact sheet said docs/; the CI uses the verified root path.
- sim-lab has NO control/claims/ dir — the ideas-lab claim route points at
  idea-engine control/claims/ only.
- trading-strategy docs/conventions.md confirmed absent — the venture-lab CI
  carries the dead-pointer warning rather than the route.
