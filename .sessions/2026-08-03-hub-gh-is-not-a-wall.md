# 2026-08-03 · hub — `gh` was never a wall: install it fleet-wide, and record why its absence never blocked anything

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · env + docs

Time: 2026-08-03 · venue: owner-live hub chat · branch
`claude/gemini-video-qa-gem-jehvhh` (restarted from main after #696 merged)

💡 Session idea: `[[fill]]`

## previous-session review

`[[fill]]`

## Scope

Owner: sessions keep asking him to "enable gh", he does not know what it is or
where to add it, and he is right that they do not need it. Two changes: make it
present, and record that its absence is not a blocker. Plus closing the ChatGPT
half of the share-link capability with a live link he supplied.

## Verify

```bash
bash -n environments/setup-base.sh
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
