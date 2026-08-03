# 2026-08-03 · hub — the direct-PAT recipe assumed a variable that is not in every environment

> **Status:** `complete`

- **📊 Model:** opus-5 · high · docs-only — one conditional, one ledger entry

Time: 2026-08-03 · venue: owner-live hub chat · branch
`claude/gemini-video-qa-gem-jehvhh` (restarted from main after #698 merged)

💡 Session idea: **a capability entry has an implied audience, and this ledger's
entries do not say who it is.** Every line here is written as though the reader
shares the writer's environment. Most of the time that holds and the omission is
invisible; when it does not, the entry reads as a *wall* to whoever lacks the
precondition — because "the recipe does not work for me" and "the capability is
absent" are indistinguishable from the inside. That is how #698 turned a correct
finding into a latent false wall within the hour of shipping it.

The fix is a habit rather than a schema: **when a workaround depends on something
the environment supplies — a variable, a binary, a mounted path — name the check
that confirms it, in the same line.** `printenv GITHUB_PAT` costs four words and
converts "this does not work" into "this needs the other branch". Worth pairing
with the previous card's refutation recipe: together they say a ledger line
should carry both *what would disprove it* and *what it assumes*. Neither is
expensive at write time and both are unrecoverable later — the reader who needs
them is precisely the one who cannot supply them.

## previous-session review

`2026-08-03-hub-gh-is-not-a-wall.md` (PR #698, merged) closed on *a wall entry
should carry the command that would refute it*. It then shipped a recipe carrying
a precondition it never named, and the owner supplied the missing fact within the
hour — the third time today a card's own lesson was correct and pitched one step
too narrow. The pattern across all three: the lesson gets written at the
granularity of the instance that produced it, and the next instance sits one
level up. Stating it at the level that catches a *different* shape is the harder
half, and none of the three managed it unprompted.

## Scope

`environments/setup-base.sh` Block 2b and one ledger entry. #698 shipped a
`gh` recipe that assumes `$GITHUB_PAT` is present. The owner: some environments
working these repos do not have it. Make the recipe branch on the variable
instead of asserting it.

## Verify

```bash
bash -n environments/setup-base.sh
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
