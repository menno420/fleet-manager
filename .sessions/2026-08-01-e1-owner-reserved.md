# E1 is owner-reserved, not stalled — annotate the NOW pointer

> **Status:** `complete`

## Goal

Record the owner's live status on step E1 so a future session reads the five-day
silence correctly. Records-only.

## Scope guard

One annotation on the programme's NOW pointer. No step completed, no ledger row,
no other file.

## Previous-session review

**previous-session review:** the last substantive change here was #635, the
false `api.github.com` wall correction — the recurring failure class this estate
guards hardest. Nothing since but 70 automated roster commits. This card copies
its instinct: state the truth in the place a future session will actually read.

## What happened

The owner oriented a session in this repo for the first time since 07-26, and in
doing so supplied information the record could not contain: **intent going
forward**, which `docs/fleet-account-2026-07-26.md` §7 explicitly names as the
thing the documentation cannot answer.

On E1, live: *"I'm going to keep deferring the email until I actually have time
to do it with a dedicated session, most of the prework is already done and I
have a decent plan for how I will write it already, but this is something that
deserves an evening of my full attention and I won't rush it. I will probably
finish it within the next few days."*

He declined a drafted version twice. That is a decision, not a gap.

## Why this needed writing down

The NOW pointer has read E1 since 2026-07-26 with no annotation. A session
booting cold would see a five-day-old pointer, no progress rows, and a plan doc
with a seeded candidate list — and could reasonably start drafting the email.
That would waste its session and hand the owner something he has explicitly
said he does not want.

**A stale pointer and a reserved one look identical from the outside.** The
annotation makes them distinguishable, and points a work-seeking session at D2
instead.

## Also recorded, because it is the reason

Every evening since 07-26 has gone to **spider-swing** — created 2026-07-28,
absent from the fleet account, and the only asset in the estate carrying a live
external signal: a returning player across multiple builds and unprompted
difficulty feedback. Verified this session: 22 of 23 repos are under 26 days
old, and only four have been pushed in August — three of those are automation.
The estate is parked with its records intact, which is the state the programme
was built to produce. Deferring E1 is triage.

## Verification

`python3 bootstrap.py check --strict` → exit 0. Records-only; no code, no step
completed, so §7 gains no row and the NOW pointer does not move.

## Owner questions

None new. E1 stays owner-reserved; §6 remains empty.

## 💡 Idea

**A NOW pointer records what is next but not whether it is available.** Those
are different facts, and today they were indistinguishable — five days of
silence on an owner-priority step reads as a stall, and the only way to tell was
to ask him. A one-line availability marker on the NOW step (`open` /
`owner-reserved` / `blocked-on`) would make a cold session correct by default
rather than correct by luck. Deduped: the ledger grammar has no such field.
Small; worth proposing only if a second session actually trips on it.

## Next slice

**D2 — the fleet-manager truth pass**, per the ledger's own ordering. It is the
first repo in D2's queue and this session's orientation surfaced two concrete
inputs for it: the seat-era apparatus still speaks seat-language, and
roster-regen is producing ~20 automated PRs a day against a seatless fleet (D4).

- **📊 Model:** opus-5 · high · docs-only — annotate E1 as owner-reserved
