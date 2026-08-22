# 2026-08-22 — Hub truing after couch-legend's stable Android signing identity

> **Status:** `complete` — branch `claude/couch-legend-milestone-b-w6vwex`.
> Hub-side only. The session's substantive work is **couch-legend #14**
> (merged, `9e04b0d`), where its own born-red card carries the full close-out,
> the verify ledger, the unmeasured list and a five-round Codex trail.

- **📊 Model:** opus-5 · estate truing (one doc, two routes)

## What this is

Milestone B — DESIGN § 7's WORKING ANDROID HANDOFF list — is owner-gated, and
the session confirmed that by looking rather than assuming: no device report of
any kind exists on couch-legend, the newest activity being the #13 merge at
`2026-08-21 22:40:56Z`. So it worked the one slice of B that needs no phone.

**The problem it closed.** #13 measured that Gradle mints a fresh debug key per
CI run; this session re-verified that independently and extended it to **four**
runs, four distinct signer certificates. Every APK therefore refused to install
over every other one, and the only way through was an uninstall — which clears
the save. That blocks B rather than annoying it: B's device matrix means putting
several builds on one phone, and at one lost save per build the checklist's most
important question, *does a save survive a force-stop*, cannot be asked twice.

**Shipped here (hub only):**

- `docs/repos/couch-legend/README.md` — the Android thread heading flips to
  record B's signing slice as landed alongside A, and the body carries the
  four-certificate measurement, what it cost, how the fix was proven (**15
  successful APK builds over 8 workflow runs**, the signer certificate read
  directly on 5 of them — four job logs plus main's artifact parsed locally —
  and inferred from a green assertion on the other 10, which reddens the job on
  a mismatch), and the one-time
  uninstall anyone holding an older build must pay — **export the in-game save
  code first**.
- `.claude/hooks/doc-routes.json` — **both** couch-legend routes were stale in
  ways that would misdirect a session. The prompt route said milestone B was
  wholly owner-gated, which stopped being true; the tool route was staler still,
  naming the life-story implementation session as NEXT when that landed
  2026-08-21. Both now name the real next step.
- A follow-up commit qualified the entry point's claim after Codex caught the
  same overstatement in the product repo: builds are **signature-compatible**,
  the mismatch removed. Nothing has been installed on any device.

**Verify:** `python3 bootstrap.py check --strict` → **exit 0**;
`tools/check_doc_routes.py` → **exit 0**; `tools/check_no_false_walls.py` →
**exit 0**. Real exit codes, none read after a pipe.

## ⚑ For the owner

Three questions gate the rest of milestone B, unchanged and unanswered: does the
app cold-launch offline, are the chapter crossfades and drifting particles smooth
on real hardware, and **does a save survive a force-stop**. A fourth is cheap to
settle now: whether he wants the application id changed from
`com.menno420.couchlegend` — it costs a reinstall after an install exists.

## Codex trail (hub PR #887)

**Round 1, 2 findings, both conceded** — and both are the *same defect class the
product repo's review had already caught*, which is the point worth keeping.

- `[conceded]` **P2 — "Stop reporting inferred uninstalls as measured events."**
  The routes said every build "refused to install over the last and cost an
  uninstall, and therefore the save". Four certificates were measured; nothing
  was ever installed, so no build actually refused and no save was actually lost.
  Corrected in both routes and in the entry point: successive builds are
  **signature-incompatible**, and the refusal and the lost save are stated as the
  inferences they are. **This is the third venue the same overstatement reached**
  — couch-legend's `android/README.md`, then its `CAPABILITIES` entry, then here.
  Qualifying a claim in the doc you are editing does not qualify the copies you
  wrote of it elsewhere, and route `says` strings are the copy nobody greps.
- `[conceded]` **P2 — "Remove the stale dormant life-story state."** Inherited
  rather than introduced, and I trued the Android thread without re-reading the
  rest: both routes still called #4's Arc-1 scene packages *dormant* and the live
  game *untouched*, when #7 landed the stage schema that activates them and
  shipped the tuned curve as the engine default. Corrected.

Together they sharpen this card's `💡`: the previous-session review below faults
milestone A for truing one route of a pair, and round 1 caught **this** session
doing the same thing one layer down — truing the thread it came for while leaving
neighbouring claims in the same string stale.

## ⟲ Previous-session review

The milestone-A hub card set the shape this one follows, and its judgement to
keep the hub card thin — pointing at the product repo rather than duplicating the
close-out — held up well: the couch-legend card for this session ran to five
Codex rounds, and none of that belongs here. Its one gap is instructive: it trued
the Android thread but left the *tool* route's "NEXT: the Claude implementation
session" untouched, so the pair drifted apart. Routes come in pairs here by
design; truing one is truing half.

## 💡 Session idea

**A route's `says` is a claim with a shelf life, and nothing ages it.** The two
couch-legend routes had drifted by different amounts — one a day stale, one three
threads stale — because a session updates the doc it is reading and rarely greps
for the routes *about* that doc. `tools/check_doc_routes.py` validates that a
route's trigger appears in its docs, which is a structural check and cannot see
that a `says` describes a NEXT that already shipped. **Guard recipe:** the cheap
version is a checker that flags any `says` naming a PR number lower than the
target repo's newest merged PR, or containing "NEXT" alongside a date older than
the doc's own `true as of` line — anchors `tools/check_doc_routes.py` and the
`routes[].says` field in `.claude/hooks/doc-routes.json`.
