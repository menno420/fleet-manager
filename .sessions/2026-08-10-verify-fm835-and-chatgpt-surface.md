# 2026-08-10 · hub — verify fm #835 independently, then record what the ChatGPT Work surface actually did

> **Status:** in-progress

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

<!-- filled before the flip -->
