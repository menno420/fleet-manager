# 2026-08-22 — Owner status brief: what has been going on, and what is worth doing next

> **Status:** `complete` — branch `claude/project-status-next-steps-hlj7p3`.
> Born red; flipped after `python3 bootstrap.py check --strict` returned a real
> exit 0 on this tree, read directly and not after a pipe.

- **📊 Model:** opus-5 · medium · research

## What this is

The owner asked what has been happening lately and what the most valuable next
steps are. Status-shaped, so the routing table sends it to `owner-brief`; the
answer was delivered in the hub chat, not committed as a document — a brief is
addressed to one reader at one moment and dates immediately, and the estate
already carries every fact it draws on.

**The brief itself changed nothing.** Two tracked deltas follow from it: the
telemetry appended by the one local gate to `.substrate/guard-fires.jsonl`
(retained per `docs/current-state.md` § Live operating mechanisms), and one
correction the read surfaced and this session decided rather than queued —
below.

## What was read (the cold-orientation contract)

`README.md`'s six mandatory reads in order, then the live surface: open pull
requests across the eight repos the brief names, last-push dates per repo, the
full-read audit's headline-seven status block, the owner queue's live section,
and the two newest session cards.

## What the read established

- The audit's **headline seven are now all closed**, and a boot-read-path page
  said otherwise. `docs/audits/2026-08-10-full-read/findings.md` reads 7 CLOSED
  / 0 OPEN (`sed -n '168,177p' … | grep -c '**CLOSED**'` → **7**), while
  `docs/current-state.md:227` still carried the 2026-08-11 reading, **1 closed,
  6 open**. Fixed here as a dated status note, not an edited number: it is a
  shipped-log entry that was true when written, so rewriting it would erase a
  correct record to fix a wrong impression. The wider list keeps three honestly
  OPEN on the kit track (D44/D45/D47).
- **The local gate is green** on `main` at `a525dd5`: `python3 bootstrap.py
  check --strict` → exit 0, read directly, not after a pipe.
- **Zero open pull requests** in fleet-manager, couch-legend, websites,
  substrate-kit and product-forge. The estate's open-PR population is entirely
  dependabot: eight on `superbot`, oldest 2026-08-10, one on `spider-swing`.

## ⚑ For the owner — two findings the brief carries

**1 · The owner-decision queue is the estate's bottleneck, not any agent
capability.** Eleven items wait on him, and several are single letters that each
unblock a whole repository (`OQ-PML-EMERALD-LETTER`, `OQ-GBA-NEXT-PICKS`,
GCB-1). Counted from `docs/owner-queue.md` § "Current owner decisions" plus the
per-repo gates the Layer-2 entry points name.

**2 · Recorded priority and actual attention have diverged, and the brief says
so rather than resolving it silently** (`intent.md` § 6). `OWNER`, 2026-08-10
(OD-15): spider-swing and the superbot repos are the important ones. `MEASURED`
2026-08-22 against the GitHub API: spider-swing's newest `main` commit is
2026-08-13 and the repository last pushed 2026-08-17; the superbot work since
has been planning only (OD-16's pre-repository plan). The sessions in between
went to couch-legend, phone-controller and the Railway consolidation — each
owner-directed live, so this is drift in emphasis, not a violation. It is
consequential only because `OQ-PLAY-LISTING` gates a **three-week floor**
(12 testers × 14 continuous days, then ~7 days of review) that has not started
since 2026-08-05.

## The finding the gate produced — the boot-read set has no headroom left

Correcting the count above was a **one-word** edit, and it turned the gate red:
`[orientation-budget] boot-read set totals 7031 words, over the 7000-word
orientation budget`. That is not a fact about my edit. Measured with the
checker's own counter (`orientation_word_count`) against `HEAD` and against the
working tree:

| tree | `AGENT_ORIENTATION.md` | `current-state.md` | total | budget |
|---|---|---|---|---|
| clean `main` @ `a525dd5` | 788 | 6211 | **6999** | 7000 |
| after a 1-word correction | 788 | 6212 | **7000** | 7000 |

**`main` was sitting one word under a hard cap — and the instrument was saying
so the whole time.** My first reading of this was that the condition was
invisible because a threshold only fires once crossed. That was wrong, and
checking it before writing it down is what caught it: the kit ships a headroom
gauge armed by default (`headroom_warn_ratio` 0.95, defaulted at read time so
omitting it from the config does **not** disable it), and on clean `main` it
emits verbatim — `boot-read set at 6999/7000 words — 1 words of headroom
(>=95% of budget; trim before the cliff)`.

So the defect is not a missing warning. **It is a correct warning nobody
reads.** That advisory is one of **124 held off the gate channel**, never
exit-affecting, and visible only by running `check --advisories` as a separate
command — which the one taught local gate (`check --strict`) does not do. The
estate's own rule is that *a firing instrument is information*; here the
instrument fired accurately, every session, and the condition still reached one
word of headroom. A signal that is never exit-affecting and lives behind a
second command is, in practice, indistinguishable from silence.

The next session that records anything on the live ledger inherits a red gate it
did not cause.

The cause is structural, not incidental: `current-state.md` carries an
append-only **"Recently shipped"** log (45 entries) plus a preserved seat-era
baseline inside a **word-capped boot document**, so it grows monotonically
toward a fixed ceiling while the two halves that could be trimmed are both
explicitly marked preserved-not-current.

**Not fixed here, deliberately.** Three real options exist — trim the shipped
log to a window and let the program's §7 ledger hold the rest · demote the
seat-era baseline out of the boot-read set · raise the budget — and every one of
them changes how the front door reads. A briefing session rewriting the
mandatory read path without the owner seeing it is the scope creep this repo's
own rules warn against, so it is raised rather than taken: the correction lands
at exactly 7000/7000, green, and the condition is now visible instead of latent.

## 💡 Session idea

**An owner ask can sit in the queue with a large agent-executable half hidden
inside it.** `OQ-PLAY-PRIVACY-POLICY` says in its own body *"a session can draft
the text if you want — ask"*, and `OQ-PLAY-LISTING` says the copy is already
drafted and *"a session can produce the captures and draft the copy once you
confirm the name"* — and the name was confirmed 2026-08-05 (`OQ-SWINGY-NAME`).
Both items have nonetheless sat whole since 2026-08-05, because the queue's unit
is the **ask**, not the **residue after the agent half is done**. The queue
grades items by venue and time, never by how much of each is actually his.
**Guard recipe:** a checker over `docs/owner-queue.md` that flags any live entry
whose body contains an agent-executable offer (`a session can …`) while the
entry's precondition is already recorded resolved — anchor the `OQ-` heading
grammar the existing `scripts/check_owner_queue.py` already parses.

**A second recipe, from the budget finding above — and it is not the one I first
wrote.** The gauge exists and works; what fails is delivery. 124 advisories
behind an opt-in command is a corpus, not a signal, and the one *approaching a
hard gate* is the one that cannot afford to sit in it. **Recipe:** promote the
narrow class of advisories that predict a *gate* failure — headroom at ≥95 % of
a budget that reds at 100 % — out of the advisory stream and into `check
--strict`'s printed output, still never exit-affecting. The distinction is
between an advisory that reports a *quality* opinion and one that reports *you
are one word from a red build*; only the second has a deadline. Anchors:
`check_orientation_headroom` (`bootstrap.py:7755`) and the `ADVISORY_CENSUS`
routing in `src/engine/guards.py`. This is kit-side, so it belongs on the kit's
worklist rather than in a local amendment.

## ⟲ Previous-session review

The 2026-08-22 signing-identity card's `💡` — *"a route's `says` is a claim with
a shelf life, and nothing ages it"* — proved itself immediately and in my favour:
booting into this repository fired five Layer-2 doc routes, and every one of them
was current, including both couch-legend routes that session had just trued. The
orientation cost of this brief was materially lower because that work was done
the day before. Its judgement to keep the hub card thin also held.

One gap, and it is exactly the class that card names one layer up. It trued
both couch-legend routes and the Layer-2 entry point, and left the **Layer-1**
ledger a cold session reads third untouched: `docs/current-state.md` §
"Recently shipped" still opens on the 2026-08-21 estate review with no row for
either Android milestone. Truing the surface you came for while the surface
above it keeps the old claim is the same half-job as truing one route of a
pair — only the stale copy is now the one on the mandatory read path. Not
fixed here (the Android rows are that thread's to write, and I did not read
those merges); the neighbouring stale count on the same page, which this
session did measure, was.
