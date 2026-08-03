# 2026-08-03 · hub — the direct-PAT recipe assumed a variable that is not in every environment

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only — one conditional, one ledger entry

Time: 2026-08-03 · venue: owner-live hub chat · branch
`claude/gemini-video-qa-gem-jehvhh` (restarted from main after #698 merged)

💡 Session idea: `[[fill]]`

## previous-session review

`[[fill]]`

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
