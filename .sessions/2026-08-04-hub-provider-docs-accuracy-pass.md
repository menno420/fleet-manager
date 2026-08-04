# 2026-08-04 · hub — provider docs were thin: accuracy pass against official changelogs

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · research — changelog-sourced corrections

Time: 2026-08-04 · venue: owner-live hub chat · branch
`claude/provider-docs-accuracy-pass`

💡 Session idea: `[[fill]]`

## previous-session review

`[[fill]]`

## Why this exists

The owner read the provider docs merged in #702 and found them thin and in
places wrong. He named two errors specifically, and both were real.

## Verify

```bash
python3 bootstrap.py check --strict
python3 tools/check_no_false_walls.py --strict
```
