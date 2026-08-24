# 2026-08-24 — The clean-pass verdict body has TWO shapes; main teaches only one

> **Status:** `complete` — branch `claude/active-projects-overview-kiftou`,
> restarted from `origin/main` at `9bd48b4` (fm #938, merged). Born red on
> purpose: the card is the merge hold (TRAP-006/007). Flipped after
> `python3 bootstrap.py check --strict` returned a real exit 0, read from a
> redirect and never after a pipe, **and** after `@codex` answered on the head
> being flipped.

- **📊 Model:** opus-5 · high · docs-only

## previous-session review

⟲ fm #938 (`9bd48b4` on `main`): TRAP-007, the three card routes, and the round-2
corrections. Checked at `main` — present and correct, except for one instruction
it shipped that is **false**, which this session exists to fix.

## 💡 Session idea

fm #938 landed guidance — in `docs/traps.md` TRAP-007 and in all three card
routes — telling a session to establish that a clean `@codex` verdict covers the
current head by **parsing a `Reviewed commit:` line from the issue comment**.

**That line does not exist in a clean-pass comment.** It was asserted by the
reviewer, propagated by me without checking the actual comment body, and merged.

`MEASURED` 2026-08-24 against the real artifact — fm #938's own clean pass, the
comment created `2026-08-23T23:42:43Z`, 3,155 bytes:

- `'Reviewed commit:' in body` → **False**
- 40-char SHAs present in the body → **`0c1a033fc9c7…` (the reviewed head) and
  `5a3f0878e6…` (the merge preview)**, both only inside `blob/<sha>/…` URLs

The `**Reviewed commit:** \`287b206bb1\`` line is real but belongs to the
**review-object body**, which is the case that already carries `commit_id` and
needs no parsing at all. So the shipped instruction fails in exactly the case it
was written for: a session following it finds no such line and concludes **no
verdict exists** — the same false-negative that made this estate merge two PRs
mid-review.

## The correction, and the correction to the correction

**The first fix over-generalised in the opposite direction** — caught here before
push, by opening the canonical record instead of trusting my own measurement as
the whole truth.

`CAPABILITIES.md` § *"Codex's CLEAN verdict is an issue comment"* documents a
**different** clean-pass body, observed twice (websites #511, fm #924):
`Codex Review: Didn't find any major issues. Hooray!` **with** a
`**Reviewed commit:** <sha>` line. That is not refuted by fm #938 — it is a
second shape. Writing *"the clean comment has no `Reviewed commit:` line"* would
have been TRAP-004 exactly: a claim wider than the sample that produced it, and
the mirror image of the error being fixed.

**So both are recorded, and the rule handles both:**

| observed clean-pass comment | `Reviewed commit:` line? | head also findable as |
|---|---|---|
| `…Hooray!` — websites #511, fm #924 | **yes** | — |
| `Approved — no blocking findings` — fm #938 | **NO** | 40-hex SHA in `blob/<sha>/…` URLs |
| `Approved — no blocking findings` — fm #939 | **yes** | 40-hex SHA in URLs |

**Line presence is an INDEPENDENT variation — the headline does not predict it.**
#938 and #939 share a headline and differ on the line, which is why the table has
three rows rather than two and why no branch may key off the headline.

**Try `Reviewed commit:` first; when absent, extract every 40-hex string and test
whether the head is AMONG them** — presence, not position, since one SHA is the
merge preview. If none matches, re-request rather than guess.

A third behaviour is claimed and never seen: the vendor's own About-block says a
clean pass produces a 👍 **reaction**. `CAPABILITIES.md` leaves that unresolved
deliberately; nothing here closes it.

## What landed

- **`docs/traps.md` TRAP-007** — the two shapes as a table, the fallback rule, and
  a note naming what fm #938 shipped wrong.
- **All THREE affected routes** — `card-flip-before-push`, `card-flip-to-complete`
  and the pre-existing **`codex-verdict-poll`**, which carried the same
  single-shape instruction and was not written by this session's work at all.
- **`docs/CAPABILITIES.md`** — the second shape appended to the canonical section,
  and its cross-reference at `:425` corrected, since that line taught the parse
  rule as a requirement.

## `@codex` on this PR — 0 inline findings, and it tried to fix rather than review

Its verdict at head `3fc5d4f` carried **zero inline findings**. Instead it wrote
the change itself and committed it as **`68d9b09`** — which does not exist here:
`git cat-file -t 68d9b09` → **`fatal: Not a valid object name`**, and
`git branch -a --contains` errors on a malformed object name. Its own summary
says why: *"A pull request could not be created because this environment exposes
no `make_pr` tool, has no configured Git remote, and `gh` has no authenticated
GitHub host."* Stranded in its sandbox — the shape fm #936 already recorded, so
its test results are claims about a tree that does not exist here and none of its
counts were copied.

**Its suggestion was right and I had missed both spots**, in the very file this PR
was correcting. `docs/CAPABILITIES.md`'s endpoint summary still read
*"the clean verdict, naming Reviewed commit"*, and the bot-filtering paragraph
below it still said to match *"by the SHA in its `Reviewed commit:` line"* — both
teaching the single shape this PR exists to replace. Applied here by hand.

**And its verdict is itself the third data point:** that comment **did** contain a
`Reviewed commit:` line **and** named the head SHA. So the `Approved — no blocking
findings` shape is not uniformly line-less either — the variance is real and the
fallback rule is what makes the check robust, not a preference between shapes.
This detection ran through the new rule live: extract every 40-hex SHA, test
whether the head is among them → **True**.

## Round 2 — 3 findings, all conceded, and one corrects my own correction

I had asked for a third pass by someone who is not me, having missed the same
class twice in one file. It found three:

1. **`[conceded]` A standalone capability row still taught the single shape** —
   `CAPABILITIES.md:416` said *"Match the `Reviewed commit:` SHA on both
   surfaces."* Third miss in the same file, and the reason is worth stating: I
   was correcting the *prose sections* and never enumerated every instruction in
   the file. Codex also confirmed **no remaining single-shape instruction in
   `docs/traps.md`**.
2. **`[conceded]` The flip route contradicted itself.** Its first numbered check
   still said read both surfaces and *"match `commit_id`"* — and issue comments
   have no `commit_id`, as the same route's later text explains. A session
   following the checklist literally **rejects every clean verdict before
   reaching the fallback**. Now says match per surface.
3. **`[conceded]` — and this one corrects the correction.** My two-shape table
   modelled the observations as headline/body **pairs**, implying the headline
   predicts where the SHA appears. **It does not:** fm #938 and fm #939 share the
   `Approved — no blocking findings` headline and **differ** on whether a
   `Reviewed commit:` line is present. My own card recorded #939's line while the
   table still said that headline had none. **Line presence is an independent
   variation; never branch on the headline.** Recorded as a three-row table with
   the variation called out, in `traps.md`, `CAPABILITIES.md` and the routes.

**This is TRAP-004 twice in one PR, in opposite directions** — first a claim
wider than its sample (*"the clean comment has no such line"*), then a structure
implying a correlation the samples do not support. The fallback algorithm was
right throughout; the *explanation* around it kept overfitting to n=1.

## Round 3 — 4 findings, all conceded

1+2. **`[conceded]` I appended the fix without removing the wrong tail.** The
   capability row began with the corrected rule and **still ended** with *"Match
   the `Reviewed commit:` SHA on both surfaces"* — self-contradicting in one row,
   and re-raised as fresh evidence after I had already marked it conceded once.
3. **`[conceded]` This card's own table still implied the correlation** it argues
   against — two rows keyed on headline, while the text below recorded #939's
   line. Now three rows, with the independence stated here as in `traps.md`.
4. **`[conceded]` I edited a dated ledger row instead of appending.**
   `CAPABILITIES.md` § 5 (`:102-105`) is explicit: *"Re-verifications APPEND,
   never edit"*, because a row must keep representing what was known on its
   recorded date and `LAST-VERIFIED` is the freshness signal. I folded 08-24
   measurements into the 08-23 entry and left its `LAST-VERIFIED` at 08-23 —
   making the new verification read a day stale. **Reverted to its recorded state
   and appended a dated 2026-08-24 entry** that names what it supersedes.

## Round 4 — 1 finding, and it exposed a tension I created

The re-post was fair. **Rounds 1–3 pulled in opposite directions and I obeyed the
later one blindly:** findings #1/#2 said to remove the single-shape instruction
from the 2026-08-23 capability row; finding #4 said re-verifications APPEND and
must never edit a dated row. Reverting the row to satisfy #4 **restored the wrong
instruction** #1/#2 had flagged.

**Both rules are right and the resolution is neither edit nor silence:** the row's
*measurement* stays exactly as recorded — that is what append-never-edit
protects — and its *instruction* now carries an explicit **⚠ SUPERSEDED** marker
pointing at the 2026-08-24 entry. A dated record keeps its content; a reader is
still stopped from acting on a rule the estate has since disproved.

**Reading a review round as a checklist rather than as a constraint set is the
generalisable error here** — the fix for #4 broke #1 because I applied it without
re-checking what the earlier rounds had established.

## Verification

- `python3 bootstrap.py check --strict` → **real exit 0**, read from a redirect,
  never after a pipe.
- `tools/check_doc_routes.py` → exit 0, 65 routes, 0 errors.
- Every route mentioning `Reviewed commit:` now also carries the varies-shape rule
  — checked by enumerating the route file, not by assuming the edit applied.

## What is about to happen

Replace the parse rule in `docs/traps.md` and all three card routes with what the
artifact actually supports, and record the measurement so the next reader does not
have to re-derive it.
