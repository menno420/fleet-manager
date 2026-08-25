# `tools/` — Estate tooling

> **Status:** `reference`
>
> **Tier: TASK** — live; read when your task touches it.
> Where you are in the estate: [the map](../docs/MAP.md).

The two checkers at the top run inside the REQUIRED `substrate-gate` check with
`--strict`. The three `test_*` files are executable suites for the hook
implementations under `.claude/hooks/` and `.codex/hooks/`.

| file | what it is |
|---|---|
| `check_doc_routes.py` | Validator for .claude/hooks/doc-routes.json — duplicate ids, empty `says`, prompt-route bar 4, uncompilable regex, missing docs, and patt…. |
| `check_no_false_walls.py` | Heuristic scanner banning present-tense standing capability-denial claims across 5 living/binding docs, with a large negation-scope/exemp…. |
| `gemini_delegate.py` | CLI (bundle/run/verify) that ships a globbed corpus to Gemini under a file+line+quote citation contract and mechanically verifies every r…. |
| `install_root_hooks.py` | Rescue script that merges this repo's hook registrations into whichever directory is the live session root, for the multi-root case where…. |
| `test_change_guard.py` | Regression suite for the change_guard hook covering malformed table delimiters, fence identity, dash-prefixed grep fragments, .substrate …. |
| `test_trigger_tools_guard.py` | Both-directions suite for the trigger_tools_guard hook: deny/warn/silent expectations across MCP tool spellings, Bash route-arounds, here…. |
| `test_codex_hooks.py` | Contract suite for the repo-local Codex prompt-router and Stop adapters, including the exact active-platform registration command from a nested directory. |
| `render_eap_mail.py` | Renderer + word counter over the final EAP mail's COPY block — plain text for a Gmail compose (emphasis stripped, paragraphs unwrapped), `--html` for rich paste, `--count` for the figure the one-page decision turns on. Ships `--selftest`, demonstrated to fire. |
| *…8 more* | see the files themselves — each gist is in [the audit's raw record](../docs/audits/2026-08-10-full-read/raw/gists.tsv). |
