# 2026-07-26 · hub — OD-10/11/12 recorded; the mail layer read on owner direction

> **Status:** `complete`

- **📊 Model:** fable-5 · high · docs-only

Time: 2026-07-26 (late night) · venue: owner-live hub chat · branch
`claude/repo-consolidation-plan-jl7z6x` (restarted from main after #547)

💡 Session idea: the last unexplained repo (`proxybench`) turned out to be
explained by **email, not by any repo doc** — a cold vendor email → the
owner's probing replies → a benchmarking harness for exactly that vendor's
claims. Lesson for the D-track: a repo's "why" sometimes lives outside git
entirely; the truth pass should ask "does the front door say why this
exists?" and, when the answer lives elsewhere, write the one-paragraph origin
into the repo rather than leaving future sessions to archaeology.

## previous-session review

Same session, one PR back: #547 landed the program + boot-file refresh (D1).
The owner then answered all three §6 forks in the hub chat and directed a
read of the mail layer (the vendor correspondence + the thread that explains
proxybench). Both read this pass; program updated.

## What this commit does (docs-only)

- **`docs/planning/2026-07-26-consolidation-program.md`** —
  - **OD-10**: Ideas Lab is **on-demand** — idea-engine sources the next
    feature when work runs dry; every new/improved feature runs through a
    dedicated sim-lab simulation (4-gate method).
  - **OD-11**: Venture — **let it sit**: live listing stays, no kill-clock
    action, no publish wave; the owner works the products angle himself,
    later, at his pace.
  - **OD-12**: `proxybench` — **no action**; origin recorded (built with a
    session mostly as a joke, in response to a proxy vendor's cold email
    about venture-lab; it benchmarks exactly that vendor's claims).
  - §6 forks → *(none open)*; target table + §7 ledger updated.

## The mail layer (chat-side detail; program stays generic)

Read in full on the owner's direction: the vendor-program thread (the 07-08
intro review · the 07-12 scale-up report · the vendor ack · the 07-16
classifier-crisis pair + attachment resend) and the proxy-vendor thread
(cold inbound 07-21 → the owner's sourcing/logging/consent probing → trial
credentials never actually arrived). The owner's own dream-sentence from the
07-12 email is the D-track's north star and worth preserving verbatim:
*"I can say one word and a session knows the full job… less a coding tool
but more a way for someone like me to run a software project by describing
it."*

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
python3 scripts/check_docs_links.py
```
