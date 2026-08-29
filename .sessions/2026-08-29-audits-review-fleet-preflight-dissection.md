# 2026-08-29 — the audit round read whole, and the fleet-preflight dissection

> **Status:** `in-progress` — born-red. Walking the owner through what the
> 08-28/29 audits established, dissecting the untested `fleet-preflight`
> skill, and reconciling the round's two parallel corpora.

- **📊 Model:** withheld · max · docs-only
- **⚑ Model-slot note:** harness policy forbids a model identifier in a pushed
  artifact; effort and PL-004 task class are exact.
- **📍 Venue:** cloud-container

## Mission

Owner ask, from the continuation prompt: explain what the 2026-08-28/29 audits
actually found and which parts are useful to him, with the weak findings named
as weak; dissect `fleet-preflight` for improvements and for parts worth lifting
into other skills; land fm #973 on the way. His stated priority: *"I want to
make sure that the valuable parts of this session are not lost."*

## Shipped

- [`docs/findings/2026-08-29-fleet-preflight-dissection.md`](../docs/findings/2026-08-29-fleet-preflight-dissection.md)
  — the dissection (keep / fix / trim / lift, per target skill), the
  OD-26 compliance check, the acceptance plan, and **§9: the reconciliation
  the round owed** between the reuse map and the error audit — agreement on
  the delivery gap and on proposals-duplicate-existing-coverage from
  independent instruments; two tensions named, neither a contradiction.
- One index row in [`docs/findings/README.md`](../docs/findings/README.md).
- The owner walk-through itself is a chat deliverable in this session; its
  durable, non-derivative parts (the strong/weak reading, the reconciliation)
  are in the finding above rather than only in the conversation.

## fm #973 — deliberately NOT landed by this session

The continuation prompt said to land it. Verified live instead of acting on
the stored instruction: the authoring session was **still RUNNING** (status
WORKING, updated 20:16Z), mid-way through Codex round 2's six inline findings
— it had pushed its own correction (`a088cb5`, *"the judges caught the shape,
not the number"*) at 20:12:21Z. Two sessions driving one PR's close is the
collision class this estate documents, so this session stood off: no card
flip, no merge, no comment. No message channel to the authoring session
exists from this container (`ListAgents` empty; the CCR server carries no
session-to-session send tool here) — measured, not assumed.

**Outcome, verified ~40 minutes later:** the authoring session finished its
own close — #973 merged at `ac5de6a` with the round-2 fixes (the coverage
field restructured into `already_covered_positive`/`already_covered_answers`,
plus a committed `verify_panel_association.py`), and its #976, #977 and
follow-up #979 all landed. The stand-off cost nothing and avoided a two-writer
race on a branch its owner was actively pushing to.

## Verify

- Catalogue stats re-derived from the JSONL at `731c282`, not quoted from any
  document (284 rows · killed 7 all at `refuter_count: 2` · none-style
  coverage answers 93 of 284 by prefix cut).
- `python3 bootstrap.py check --strict` → real exit code, no pipe; born-red on
  this card until the flip below.

## ⟲ Previous-session review

Previous card:
[`2026-08-29-audit-catalogue-export.md`](2026-08-29-audit-catalogue-export.md)
(fm #973 — reviewed at `731c282` while still in flight; merged at `ac5de6a`
with two further round-2 commits this review predates).

**Held up on everything re-measured here:** its row counts (284/20), the
recovered panel fields, and the refuter tally (226/51/7) all re-derived
exactly from the JSONL. **What it missed, which Codex round 2 and this
session's own cut both caught:** its README read field *population* as
positive coverage — "every row was told what already covers it" — when 93 of
284 rows carry none-style answers. The card's near-miss section (155/122/7
typed from a subset) proved prophetic one layer up: the same evening, the same
file, a claim about a field asserted at a grain nobody had measured.

## 💡 Session idea

**Fixture the teaching examples the way instruments are fixtured.** The
dissection's F1: `fleet-preflight`'s own example predicate
(`SKILL.md:70`) misreads none-style coverage strings as coverage — the exact
defect class the section teaches against, shipped in the section that teaches
it. A skill that ships runnable teaching code could carry one known-positive
and one known-negative for its own example, exactly as its §2 demands of the
run's instrument. Cheap, self-applying, and it would have caught F1 at
authoring time. (An idea, not an action: skill edits wait for first real use
per the standing decision, and mechanisms wait for the revised plan per
OD-26 §14.)
