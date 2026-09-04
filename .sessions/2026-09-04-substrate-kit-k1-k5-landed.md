# 2026-09-04 · substrate-kit K1–K5 built and merged; the estate route reconciled

> **Status:** `complete`

- **📊 Model:** opus-5 · xhigh · feature build
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01Y3DjrdYmx4ahPkvdZnWNNm](https://claude.ai/code/session_01Y3DjrdYmx4ahPkvdZnWNNm) · "Fleet Manager substrate-kit implementation"

💡 Session idea: **a requirement list written as N rows is not evidence that N
things need building.** K1–K5 read as five kit changes; they were one missing
abstraction. `ADOPT_PLAN` was already a data table, `Config` already carried
`sessions_dir`/`docs_root`/`claims_dir`, and `upgrade`/`render` already re-ran
`adopt` with the loaded config. What the kit had no name for was *which shape
an install was born in* — so every consumer that walked the plant table
assumed the one historical shape. Naming the shape made four of the five rows
fall out of one accessor, and it made the fifth (telemetry) a config section
rather than a special case. **The read to make before implementing a numbered
list is: what would make these one thing?**

## previous-session review

`2026-09-03-final-eap-mail-rewrite-after-reviews.md` closed the EAP-mail track
by putting the draft in his mailbox and leaving the sending to him. This
session is the other half of the estate program — [D-0035]'s step 2, the kit
prerequisites — and inherits the same discipline in a place with more surface
area: the change touches adoption itself, so every existing adopter is a
regression target, and the proof had to be *the merged artifact producing the
tree*, not the source suite agreeing with itself.

## What shipped

**In substrate-kit** — [kit #590](https://github.com/menno420/substrate-kit/pull/590),
squash-merged **`8a83c733eded4af06281dcbe1d01f05d3da98a94`**, unreleased.
K1–K5 as one **adoption profile** (`bootstrap.py adopt --profile hub`), with
`Config.adoption_profile` persisting the shape so `upgrade` and `render`
honour it without a second orchestration path. Detail, proofs and deferrals:
[`../docs/repos/substrate-kit/README.md`](../docs/repos/substrate-kit/README.md)
§ *Thread: K1–K5*.

**In this repo** — records only, no implementation: the Layer-2 entry point
gains the K1–K5 thread; the proposal README and the kit-prerequisites file are
no longer "nothing here is built"; `current-state.md` carries the live entry;
`owner-queue.md` records the third unreleased passenger and the exact command
that would release it.

## Verify

```bash
# in substrate-kit, on main AFTER the merge — not the PR's green
python3 -m pytest tests/ -q                                  # 2277 passed, 1 skipped
python3 src/build_bootstrap.py && git diff --exit-code dist/bootstrap.py   # 0
# hub adoption driven through main's OWN artifact, empty git repo: exit 0,
# no control/, no docs/, sessions/ visible, ledger gitignored + capped

# in this repo
python3 scripts/preflight.py                                 # exit 0, 9 legs
```

**40 mutants applied across the kit change, 40 killed.** Four of my own tests
failed that check before they passed — the useful half of the exercise.

## Honest null

- **Not released, and not mine to release.** His *"cut when the next fix batch
  lands"* sequences the charter rewrite and the doc-surface sweep first;
  neither has landed. `OQ-KIT-V1-21-RELEASE`'s adopter half is still open.
  Three merged-unreleased kit PRs now wait: #587, #588, #590.
- **`estate` is NOT seeded.** The accepted build order makes seed creation the step *after*
  the folder contracts and migration manifest. The next executable step is
  step 3, not the seed.
- **The hub has no skill pack** (26 advisories over 8 paths) and the kit's
  doctrine prose is *reported* rather than forked per shape. Both deliberate,
  both pinned by tests rather than left as prose.
- **The merged head carries no review verdict.** Round 3 was the per-PR cap
  and its six findings were fixed after it. Verified by the suite, every CI
  leg, the cold-adoption smoke and the mutation pass — not by a fourth round,
  because there is not one.
- **Found, not fixed:** `[boot-section-missing]` on `.claude/CLAUDE.md` after
  any `adopt --include-claude`, reproduced identically on the pre-change
  `origin/main` dist. Pre-existing; its own PR.
