# Third-party verification of fm #835

> **Status:** `reference` · 2026-08-10 · fm #836 · claims below are `MEASURED`
> unless marked otherwise
>
> **Scope:** fm #835 reviewed fm #833/#834 and Codex reviewed fm #835. This is
> the third pass, and it exists for one reason: **#835's final commit
> `c9694f21` changed a required-CI checker four times after the review-loop cap
> and nobody examined it.** Re-reading a reviewer's own evidence adds nothing;
> running cases the reviewer did not write does.

## What was re-run, and what it returned

Each command its own process, its own exit code, on a detached worktree of
merged `main` (`dd8b1a5`) — never `$?` after a pipe.

| claim in fm #835 | what ran here | verdict |
|---|---|---|
| all five gates green on merged main | the five commands, separately | **survived** — `0 / 0 / 0 / 0 / 0`; change guard 16/16, trigger guard 69/69 |
| `substrate-gate` passed | PR #835 check-runs | **survived** — `substrate-gate` success, `merge-on-green` success |
| the A/B harness now exercises all seven defects | `python3 tools/ab_kit_scan.py` | **survived** — nine rows: seven defects plus two controls, exit 0 |
| ten Codex findings, all dispositioned | `/pulls/835` reviews + review threads | **survived** — 3 reviews on exact heads `6388db4c` / `0027cb0e` / `32243046`, 10 threads, every one resolved with a reproduction and a fixing SHA |
| the negation-scope hole is fixed | own fixtures, old checker vs new | **survived** — table below |
| the guard's deny leg is exact on the tool name | subprocess probe | **survived** — `permissionDecision: deny`, process exit 0 |

### The fix, reproduced against both versions

Fixtures written here, not taken from #835. Old checker loaded from
`git show 0ab4d07:tools/check_no_false_walls.py`.

| fixture | old (`0ab4d07`) | new (`dd8b1a5`) |
|---|---:|---:|
| bare wall — positive control | 1 caught | 1 caught |
| `does not reproduce because …` | **0 — the hole** | **1 fixed** |
| `does not reproduce since …` | **0 — the hole** | **1 fixed** |
| `does not mean …` — valid correction | 0 clear | 0 clear |
| `not as if …` — valid repudiation | 0 clear | 0 clear |

### The cliff arithmetic, checked rather than accepted

fm #835 reports the exact transition at token-end distance **45/46**, where fm
#833 reported a coarse 44/48. Both are right and the sharper one is derivable:
`\bnot\b` only matches when the whole token sits inside
`window[sig_start-48:]`, so `not`-start ≥ `sig_start-48` and therefore
`not`-end ≥ `sig_start-45`. End-distance ≤45 clears; ≥46 flags. The #833 figures
were measured from a different anchor, and #835 reconciles them explicitly
rather than overwriting them.

## The monotonicity property — the reason this fix is safe

`_negation_lead` returns `prefix[max(clause_start, len(prefix)-48):]`; the
replaced line was `prefix[max(0, len(prefix)-48):]`. Since
`max(clause_start, X) ≥ max(0, X)` and both slices end at `len(prefix)`, the new
lead is a **suffix of the old**. `NEG_TOKEN_RE.search` is existential over that
slice, so *new clears ⟹ old clears*; contrapositive, *old flags ⟹ new flags*.
The change can therefore only flag more, never less.

**That derivation constrains one code path, and the path is the only one that
moved.** `lead` feeds exactly one test. The META, anti-wall and quoted
exemptions are all evaluated over `window`, which #835 did not touch — and
listing every deletion in the 199-line diff confirms it: the **only** deleted
executable line in the file is
`lead = window[max(0, sig_start - 48):sig_start]`. Everything else removed is
docstring or comment.

Derivation is not measurement, so it was measured:

```
corpus: 88,923 markdown lines from 724 files
old flags: 190   new flags: 202
MONOTONICITY VIOLATIONS (old flags, new clears): 0
```

Zero counterexamples on the real corpus; 12 lines newly caught. **A future
change to `_negation_lead` should re-run this** — it is the property that makes
the clause-boundary work safe to extend, and it is cheap.

## The adversarial battery against the unreviewed commit

24 cases written here, aimed at the four fixes in `c9694f21` that no reviewer
saw: path-qualified interpreters, the modifier vocabulary before `given that`,
the negated-complement `as` exemption, and the paired-comma mask.

**New checker 23/24. Old checker 9/24.** Every "must stay clear" case passed on
both; the old checker's 15 failures were all holes.

### The one residual, and why the first description of it was wrong

```
Do not read the docs as gospel as agents cannot merge pull requests.   → clears
```

Both `as` tokens are exempted from being boundaries by
`NEGATED_AS_COMPLEMENT_RE` — the first legitimately (`read … as`), the second
because the negated complement verb is still within its bounded lookback. With
no boundary left, the unrelated `not` reaches the wall.

**This was first filed against #835's declared failure class, and that
attribution does not hold.** The doc's own boundary statement
(`docs/findings/2026-08-09-independent-guard-review.md:95-97`) reads: *"An
arbitrary unrelated negation inside one unsplit grammatical clause can still be
ambiguous."* But this sentence **is** split — the causal `as` is right there.
It behaves as unsplit only because an exemption fired too broadly. Same shape,
different mechanism: a declared parsing-ambiguity limit versus a bounded bug in
one regex.

Recorded, deliberately **not** patched. Another exemption-to-the-exemption is
the whack-a-mole that `docs/ideas/checker-contract-bank-2026-08-09.md` exists to
replace; this belongs in that bank as a named case for the v1.21.0 session.

`UNVERIFIED`: whether any comparable over-exemption exists for the paired-comma
mask. The battery probed it three ways and found none, which is evidence, not
proof.

## What #835 caught that fm #833/#834 got wrong

Its own record (`2026-08-09-independent-guard-review.md`) is the claim-by-claim
ledger and is not duplicated here. Two items are worth carrying forward because
they are about **how** the errors survived, not what they were:

- **A propagation gap, not a knowledge gap.** `docs/decisions.md` still carried
  the `subscribe_pr_activity` overclaim after the boot file had been corrected
  in the same session. The fact was known and the second home was missed.
- **A test suite asserting its own bug.** The 52-case trigger suite passed while
  the warning text it pinned contradicted the trigger-tools decision (stamped in
  `docs/decisions.md`) by recommending a `send_later` self-wake for PR CI. A
  green suite is evidence about its
  assertions, never about whether those assertions are the intended behaviour.

## Corrected here: the hook count was wrong, and it was mine

`docs/execution-surfaces.md` said `5 hooks` and *"none of the five hooks"*.
There are **six** scripts in `.claude/hooks/`, registered as eight hook commands
across five events. `git log -S"none of the five hooks"` puts that sentence in
`e9214c5` — written *after* `a02a4b1` added the sixth hook **in the same
session**. fm #835 found the staleness and did not fix the file; it is fixed in
fm #836.

The class of error is the one this estate keeps repeating: **a count in prose
goes stale the moment the thing it counts changes.** The durable answer is not
to write counts down. Where one is genuinely needed, derive it.
