# 2026-08-04 · hub — inhabiting vs observing: minting PL-013 and citing it here

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only — program-law mint + consumer citation

Time: 2026-08-04 · venue: owner-live hub chat · branch
`claude/provider-capability-reference-tz4fb1` (restarted from main post-#714)

💡 Session idea: **the estate had the evidence for its own founding claim and
no statement of it.** Everything this session measured — a non-integrated
session drifting off a convention it could read, a 41-item queue collapsing
into one call, an art pipeline that survived across sessions only because it
was committed — pointed at one proposition that appeared nowhere in the kit:
*read access is not integration; being subject to a repo is what makes its
rules bind.* The owner supplied the sentence (*"claude code and gpt work both
'live' inside the repos. Regular sessions can only view them from the
outside"*), and it turned three separate findings into instances of one law.

The generalisable form: **a body of findings that all point the same way is a
missing ruling, not a finished investigation.** The signal is repetition across
unrelated tasks — art pipelines, batch failures, tiling advice — and the fix is
to mint the law once where every repo can cite it, not to restate it in each
finding.

## previous-session review

`2026-08-04-hub-art-finding-corrections.md` (PR #714, merged) landed the owner's
corrections and surfaced the sharpest line of the day — *readable is not
binding* — as a detail on a session card. That was the wrong home: it is
program law, not a card note. This session promotes it. **The lesson: when a
correction produces a sentence better than the document it corrected, the
sentence needs its own home.**

## Scope

Mint the ruling in substrate-kit (its rationale is a claim about what the kit
is for), then cite it here per the register's cite-never-copy rule. Not a
program step; NOW (E1) untouched.

## What landed

- **substrate-kit PR #569** — `[PL-013] Inhabiting beats observing` minted in
  `docs/program/rulings.md`, with three binding consequences: readable is not
  binding (enforcement is the active ingredient); decomposition is an
  environment property, not a prompt property; diverge cheaply, converge
  expensively. Templates cite the new PL-ID; `dist/bootstrap.py` regenerated.
  Verified: `pytest` 2081 passed (exit 0), `check_program_law.py` OK (exit 0).
- **fleet-manager** — `docs/collaboration-model.md` cites PL-013 alongside the
  other PL-IDs; the art finding now opens by naming the law it produced.

**The kit's own guard fired correctly and is worth recording as a capability,
not a friction:** `check_program_law.py` refused the PR for lacking the
`do-not-automerge` label — *"law changes sit for owner review, never
auto-merge (the kit#22 lesson)"* — after a bot had armed auto-merge. That is
PL-013 demonstrating itself: a rule that would have been ignored as prose was
enforced because the session was subject to it.

## Honest nulls

- **PL-013 is owner-ruled, not measured.** Its evidence is one estate's
  findings; nothing here tests the counterfactual (a 41-item queue run *inside*
  an integrated environment).
- **The kit PR is held for owner review by design** — it carries
  `do-not-automerge` and is not merged at session close. That is the correct
  terminal state for a law change, not an unfinished PR.
- **A truncation bug cost a file mid-session.** `open(p,'w')` truncates before
  the inner `open(p).read()` in the same expression; the findings doc went to 0
  bytes and was restored from HEAD. Recorded because the shape recurs: a
  read-after-open-for-write in one line is silent data loss. Use the Edit tool
  for committed files.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
