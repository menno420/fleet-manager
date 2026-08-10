# 2026-08-10 · hub — verify fm #835 independently, then record what the ChatGPT Work surface actually did

> **Status:** complete

- **📊 Model:** Claude Opus 5 · high · review/verify plus docs-only corrections

Time: 2026-08-10 · venue: owner-live hub chat · branch
`claude/kit-upgrade-eap-reconciliation-e9poz5` (restarted from `dd8b1a5` =
`origin/main`, its previous PR #834 having merged)

💡 Session idea: **a review that only re-reads the reviewer's evidence is not a
third rail — it is the second rail wearing a hat.** fm #835 reviewed fm
#833/#834 and Codex reviewed fm #835, but its final commit `c9694f21` landed
after the review-loop cap with four changes to a required-CI checker that nobody
examined. The cheapest way to add real information is to test the code nobody
tested, with cases nobody wrote.

Layer-2 handoff: null (fleet-manager itself)

## Previous-session review

⟲ fm #835 (ChatGPT Work, GPT-5) independently reran fm #833's kit-defect
instrument and fm #834's trigger guard, corrected the defect classification,
fixed the local false-wall negation-scope hole, and expanded the trigger suite
from 52 to 69 cases. Ten Codex findings across three exact-head reviews were all
conceded with reproductions. The owner asked for a thorough review of that
session and of the work it left in the repo.

Baseline verified before this card, on a clean detached worktree of merged
`main` (`dd8b1a5`), each command its own process and its own exit code:
`bootstrap.py check --strict` **0**, `check_doc_routes --strict` **0**,
`check_no_false_walls --strict` **0**, `test_change_guard` **0** (16/16),
`test_trigger_tools_guard` **0** (69/69). `substrate-gate` on #835: success.

## What is about to happen

1. Record the third-party verification as a dated finding: the monotonicity
   measurement over the real corpus, the reproduction of the fix against both
   checker versions, the adversarial battery against the unreviewed commit, and
   the one residual that battery found.
2. Correct `docs/execution-surfaces.md` — the hook count is wrong (mine, from
   `e9214c5`), and the surface's measured strengths and failure modes belong in
   the comparison rather than in a chat.
3. Record the connector-over-`gh` route in `docs/providers/chatgpt.md` and the
   capability ledger, as a capability rather than a wall.
4. Commit the ChatGPT project instructions so the next session's brief points at
   a file instead of carrying it.

## Close-out

### Shipped

- `docs/findings/2026-08-10-fm835-verification.md` (`a3ff1d0`) — the third-party
  record: the fix reproduced against both checker versions, the monotonicity
  property derived *and* measured, the 24-case adversarial battery, and the one
  residual with its misattribution corrected.
- `docs/execution-surfaces.md` (`a3ff1d0`) — hook count replaced with a
  derivation; the `delete_trigger` row scoped to Claude Code per the owner; the
  measured surface facts (connector over `gh`, Work ≠ Codex cloud,
  `merge-on-green` sweeps `claude/*` only) and the honest cost note.
- `docs/CAPABILITIES.md` (`a3ff1d0`) — connector-as-publishing-route appended as
  a **capability**, with the four exit codes that establish `gh`/PAT absence
  blocked nothing.
- `docs/prompts/chatgpt-project-instructions.md` (`a3ff1d0`) — the standing
  instructions as a file, rewritten against the measured run.
- `docs/current-state.md`, `docs/ideas/checker-contract-bank-2026-08-09.md`
  (`a3ff1d0`) — ledger updated; the residual banked as the bank's first case.
- `docs/ideas/derive-dont-state-counts-2026-08-10.md` — new idea, with its own
  argument against itself recorded alongside it.

### Verify — real exit codes, each its own process

```
python3 bootstrap.py check --strict          → 1  (born-red HOLD naming THIS card; sole finding)
python3 tools/check_doc_routes.py --strict   → 0  (24 routes · 19 docs · 0 errors)
python3 tools/check_no_false_walls.py --strict → 0 (CLEAN — 5 living/binding docs)
python3 tools/test_change_guard.py           → 0  (16/16)
python3 tools/test_trigger_tools_guard.py    → 0  (69/69)
```

CI agreed: `substrate-gate` on `a3ff1d0` reported exactly two findings, both the
hold — `[session-card-hold] … designed hold, not a defect` — with both repo
checkers green inside the run. Verified against the job log, not the tail.

### Review

Codex reviewed `a3ff1d0c8d` — the exact head — and returned **no findings**.
Nothing was changed after it, so no re-review round was owed and the loop
terminated on its own condition rather than on the cap. This flip commit is the
`session-close` exemption: a badge flip plus this close-out text, nothing
reviewable.

### Capability delta

One capability appended (the connector route). **No wall recorded** — the
`gh`/`$GITHUB_PAT` absences are route facts that blocked nothing, and are
written that way deliberately.

### ⚑ Owner-facing

Nothing new for `docs/owner-queue.md`. Two items remain the owner's call and are
already recorded where they belong: whether to add an `AGENTS.md`
(`docs/execution-surfaces.md` § 4b) and when to run the substrate-kit v1.21.0
session (`docs/current-state.md`).

### Ideas

Groomed forward: `checker-contract-bank-2026-08-09.md` gains its first named
case and a reusable property to bank. New: `derive-dont-state-counts-2026-08-10.md`.

### PR

#836 — merged on green after the flip; probed against the tree, not a stale read.
