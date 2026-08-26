# 2026-08-26 — the estate activity log: what a cloud session can learn about local work

> **Status:** `complete` — born red on purpose and verified red at open and on
> every head since (`substrate-gate`'s added-card hold, naming this card).
> Flipped only after `python3 bootstrap.py check --strict` returned a real exit 0
> read from the process, never after a pipe, and after **five `@codex` rounds**
> — the last of which was acted on in full but deliberately not answered with a
> sixth request, per the convergence rule. No review request is outstanding at
> the flip (TRAP-007).

- **📊 Model:** opus-5 · high · feature build
- **📍 Venue:** cloud-container

## 💡 Session idea

The owner asked a question — *"how well does a cloud session understand what the
local sessions have been doing?"* — and proposed the fix in the same breath. The
question is answerable by measurement rather than opinion, and the measurement
belonged in the record before the fix was designed, because it is what decides
the shape. It did: the answer split one ask into three unrelated gaps.

**The new idea this session believes in, and did not build:** the four
non-archived repositories with no `.sessions/` at all are a bigger hole than
anything the log closes, and `spider-bot` is the sharp end — **live in
production, 8 commits in two days, no card protocol.** The generated
invisible-work section now names it every run, which is the right place for the
prompt. Adopting the kit there is a small, self-contained next step.

## What shipped

- **`docs/activity/`** — the section the owner asked for.
  [`README.md`](../docs/activity/README.md) (the design, the venue vocabulary,
  the honest limits), [`estate-log.md`](../docs/activity/estate-log.md)
  (GENERATED), [`off-repo-log.md`](../docs/activity/off-repo-log.md)
  (hand-written, opens empty).
- **`tools/estate_activity.py`** — `refresh` and `log`. Runs off `$GITHUB_PAT`
  over direct egress **or** the `gh` CLI, so the same command is correct in a
  container and on the owner's Windows laptop.
- **`docs/findings/2026-08-26-cross-session-visibility.md`** — the measurement.
- **Delivery, not restatement:** boot-file routing row + read-path line,
  `MAP.md`, `README.md`, `.sessions/README.md` (the `📍 Venue:` amendment),
  `session-close` step 5c, and two `doc-routes` entries — one firing when a card
  is written, one when the owner asks what other sessions did.
- **`creator-kit` registered in `ESTATE.md`**, and the baseline corrected from
  27 to **28**. It had existed for a day, unrecorded, in a file whose header
  promises *"every repository the account holds"*.
- **Roadmap § 5.7** gains the owner's laptop as a **venue** — placed below his
  `OWNER` table rather than inside it, because the row is not his.

## 🔢 What the measurement actually found

Three gaps, needing three different fixes — which is why the single ask did not
have a single answer:

1. **No aggregation.** 74 cards across six non-archived repositories in the
   seven days to 2026-08-26; a fleet-manager cloud session could reach **54**,
   all its own. The other **20** — `websites` 9, `couch-legend` 7,
   `product-forge` 2, `sim-lab` 1, `idea-engine` 1 — were unreachable from here.
   The cards were never missing. They were unreachable **from the router whose
   job is routing**.
2. **No venue on any card.** `MEASURED` at `39c9d6e`: **0 of 418** dated cards
   here record which machine ran them.
3. **Work outside every repository leaves nothing at all** — and this is what
   his question was really about. The estate's whole memory is git-shaped.

## ⚑ The @codex relay — five rounds, and the last three are the interesting ones

**46 findings · 35 `[conceded]` · 1 `[partial]` · 10 `[survived]`.** Per round:
15 (15·0·0) · 9 (8·1·0) · 8 (4·0·4) · 8 (4·0·4) · 6 (4·0·2). Every `[survived]`
is a re-emission of a fix present and verified in the tree; the `[partial]` is
round 1's venue regex, which I fixed and round 2 re-flagged from a different
angle that turned out to name a case neither of us had — a **fenced example**
of the bullet inside a card body.

**New findings per round went 15 → 9 → 4 → 4 → 4 while re-emissions went
0 → 0 → 4 → 4 → 2.** Round 5 was taken and acted on but not answered with a
sixth request, per the repo's convergence rule: it returned two genuine
completions of earlier fixes (an unborn repository answers the tree endpoint
with **409**, not 404, so the no-commit guard was half done; and in-flight card
dates entered the coverage set without the `<= today` bound their rendered
counterparts get), one real Windows-locale bug in the `gh` fallback, and one
stale tally **in this very close-out's neighbour**, `current-state.md` — which
is the un-propagated-correction class this repo keeps a checker for, caught in
the act.

**Two findings pulled in opposite directions on one predicate**, which is the
finding worth carrying forward. Round 2: an open born-red PR must not report
*itself* as unexplained movement. Round 3: an open PR must not excuse *every
other* push in the repository, because `pushed_at` is repository-wide. Neither
is satisfiable from `pushed_at` alone. The predicate now asks whether a **date
covers the push** — a card's own date, or the head-commit date of the open PR
whose branch carried it.

**And rounds 3 and 4 found the same three bugs twice**, in a second near-parallel
branch for repositories adopting the protocol: a missing `<= today` bound, a
missing coverage check, a dropped head date. Patching the symptoms drew a
reshaped finding each round. The branch is now **gone** — one path for every
repository, and a repo with no `.sessions/` on its default branch is simply one
whose `dated` list is empty. That is the lesson: a second code path that
`continue`s past shared logic will be re-found as many times as it has rules.

**The class of error I made most:** writing numbers by hand while the generated
table sat in the same commit. The reachable split was 43/31 and is 54/20; the
card baseline counted the directory README. Every figure now cites
`estate-log.md`.

## ⟲ Previous-session review

[`2026-08-25-e1-owner-revision-pass.md`](2026-08-25-e1-owner-revision-pass.md)
executed the owner's three E1 calls and left the mail waiting on his Part 1 and
his compose — untouched here, correctly: a session does not draft or send it.
Its own lesson was the same one this session repeated in a different costume —
it re-counted a figure that three committed places had wrong, and fixed it by
making the number come from `render_eap_mail.py --count` rather than from prose.
This session's fix for its own arithmetic is the same shape: the log is
generated, so the numbers cannot be remembered wrong.

Layer-2 handoff: null (fleet-manager itself; no satellite repository attached —
`creator-kit` was registered in `ESTATE.md` from live reads, and its
`docs/repos/` folder is named as follow-up rather than written blind).

## Capability delta

None new. The direct-PAT path, the Git Trees API and the `@codex` relay all
behaved as `docs/CAPABILITIES.md` already records. One method note worth having:
**`.git/shallow` exists in this container** — 52 commits here against 966 on
`main` — so any commit-count claim from a session clone is a sample, not the
repository. That cost a wrong sentence in the finding's first draft.
