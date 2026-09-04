# 2026-09-04 — Couch Legend's long-form redesign: the route update

> **Status:** `complete` — the route is updated; couch-legend #19 merged as `4934955`.

- **📊 Model:** Opus 5 · xhigh · docs-only
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01FAkSXD7ZQ7E7XzysZmLRbF](https://claude.ai/code/session_01FAkSXD7ZQ7E7XzysZmLRbF) · "Couch Legend game design and architecture"

## Previous-session review

The three commits that landed on `main` while this session ran (#1022–#1024)
are substrate-kit records and telemetry; a `git log --name-only` over
`caa6cd2..origin/main` shows nothing touching couch-legend, so nothing in that
movement changes what this card records. That check is the fleet-preflight
BASE contract's scheduled re-read, run before writing rather than after.

## 💡 Session idea

The hub's job here is exactly one thing: make sure the next session working
Couch Legend does not have to rediscover that the eighteen chapters were
measured, found to be sixteen repeats, and answered. The two store-policy
findings are the part that generalises beyond one repo, so they go in the
route rather than only in the product's DESIGN.md.

## What is about to happen

The product work is [couch-legend #19](https://github.com/menno420/couch-legend/pull/19).
This side of it is the estate router's half: the couch-legend entry point
gains the long-form-redesign thread, with the measured before/after, the
rails, the open owner gate, and the two store-policy facts that any
cannabis-themed product in this estate would otherwise get wrong.

## What changed

`docs/repos/couch-legend/README.md` — a new lead thread. Nothing else; the
hub does not copy product truth, and everything mechanical stays in the
product repo's `docs/DESIGN.md` §§ 11–12.

## Close-out

The product work merged as couch-legend
[#19](https://github.com/menno420/couch-legend/pull/19) → `4934955`. This route
now carries the measured before/after, the review record, and the two
store-policy facts that generalise past one repo.

**One correction worth carrying:** the thread first said 17 of 18 chapters
introduce a mechanic. That was the product repo's own instrument overcounting —
it treated a stronger value of an existing effect shape as a new mechanic — and
Codex caught it in the third review round. The honest figure is **14 introduce,
3 deepen, 17 deliver something new**. It was corrected in all four places it
had been published, this route included.

**A process note for the next session working a kit adopter:** the local gate
and the CI gate are not the same command. `python3 bootstrap.py check --strict`
passed while CI's added-card lane
(`check --strict --added-card <card>`) failed on an off-taxonomy PL-004 task
class. Run the added-card form locally before pushing a card.
