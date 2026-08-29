# 2026-08-29 — the audit's own banner counters, corrected

> **Status:** `complete` — the two counters are corrected and every sibling copy
> re-grepped. **No review was requested and the reason is stated below**, so
> there is no outstanding verdict for the flip to outrun (TRAP-007). A two-number
> documentation correction to a merged finding; cleared to proceed by OD-26 §14
> (*"document corrections do not [wait for the revised plan]"*).

- **📊 Model:** withheld · high · docs-only
- **📍 Venue:** cloud-container

## Mission

[The agent-error audit](../docs/findings/2026-08-29-estate-agent-error-audit.md)
landed across fm #967 and #968. Its status banner still reports the state it had
**before its own final review round**: *"nine sections; 28 Codex findings across
three rounds"*. Measured at `origin/main`:

| claim | banner said | actual |
|---|---|---|
| review findings | 28 across three rounds | **37 across four** (fm #967 R1 9 + R2 11; fm #968 R1 8 + R2 9) |
| sections | nine | **ten** — `grep -c '^## '` = 10 (§0 through §9) |

The card and the findings index already carry 37/four; **only the banner was
left behind** — which is the audit's own **TRAP-008 candidate** (*a correction
that leaves its own copies standing*), committed for the fourth time by the
document that proposes it. Found by verifying main after the merge rather than
by another review round.

## Why no review was requested

The change is two integers, both verifiable by `grep -c` against the same file.
fm #968's closing disposition argued that further rounds were generating stale
copies rather than closing them (P1s per round 2 → 5 → 0 → 0, count flat);
requesting a fifth round for two numbers would contradict that on the same day.
**If that reasoning is wrong, this is the change to point at** — it is small,
reversible, and entirely mechanical.

## Verify

- `python3 bootstrap.py check --strict` → real exit code, no pipe.
- Post-merge re-grep of every count claim across the finding, the index and both
  cards, so the sibling copies are checked rather than assumed.

## ⟲ Previous-session review

Previous card:
[`2026-08-29-audit-od26-reconcile.md`](2026-08-29-audit-od26-reconcile.md)
(fm #968, merged `bd255e8e`).

**Held up.** Its 17 findings were all conceded and its non-convergence call was
argued from data (P1 severity per round) rather than asserted.

**What it missed, and this card closes:** it updated the findings index to
37/four and left the finding's own banner at 28/three, in the same commit. The
session had just written a disposition explaining that each round's fixes were
creating the next round's stale copies — and then created one. That is the
strongest single instance of TRAP-008 in the whole corpus, because the author
was holding the pattern in mind at the moment of committing it.

## 💡 Session idea

**A counter is a derived value stored as prose, and this estate keeps getting it
wrong.** Every instance in this two-day sequence — 216 vs 172, 1,431 vs 1,437,
nine vs ten sections, 28 vs 37 findings, 7,214 vs 7,341 — is a number a command
could produce, written by hand instead.

The mechanical part is decidable: for a small set of declared patterns
(`N sections`, `N findings`, `N of M repos`), a checker recomputes the value
from the artifact it describes and fails when the prose disagrees. Section
counts are `grep -c '^## '`; finding counts are already in the PR thread.

**Why an idea and not an action:** it is a new gate lane in every adopter, which
OD-24 §3 says an agent does not introduce on its own initiative, and OD-26 §13
puts mechanisms behind the revised plan. It belongs in the same plan-input pile
as the audit's §9, measured against the same corpus first.
