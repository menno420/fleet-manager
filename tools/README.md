# `tools/` — Estate tooling

> **Status:** `reference`
>
> **Tier: TASK** — live; read when your task touches it.
> Where you are in the estate: [the map](../docs/MAP.md).

The two checkers at the top run inside the REQUIRED `substrate-gate` check with
`--strict`. The four hook-adjacent `test_*` files are executable suites for the hook
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
| `render_eap_mail.py` | Renderer + word counter over the final EAP mail's COPY block — plain text for a Gmail compose (emphasis stripped, paragraphs unwrapped), `--html` for rich paste, `--eml` for a real openable message, `--count` for the figure the one-page decision turns on. Ships `--selftest`, demonstrated to fire. |
| `check_eap_figures.py` | Reads the word/emphasis figures the E1 documents *state* and compares them against what the mail actually contains, across the draft and the session card. Reports a moved phrasing as loudly as a wrong number, and re-runs itself against a corrupted copy so its exit code means something. |
| `estate_activity.py` | The cross-session activity log's engine, two subcommands. `refresh` reads every non-archived repository's `.sessions/` directory and rolls the cards in a rolling window into `docs/activity/estate-log.md`, including an **invisible-work** section naming repositories that were pushed and left no card. `log` appends one entry to the hand-written lane for work that touches no repository at all. Runs off `$GITHUB_PAT` over direct egress **or** the `gh` CLI, so the same command is correct in a container and on the owner's laptop. Advisory — wired into no gate. |
| `owner_comments.py` | Fleet Manager's public owner-feedback contract: validates JSON records against ESTATE identities, regenerates the cheap root index and every stable per-repo README, and consumes by moving a record into preserved history while updating both indexes. `check` is required-gate input. |
| `test_owner_comments.py` | Regression suite for record/schema/path validation, exact-wording preservation, active-vs-consumed indexes, unknown repositories, stale generated output, double-consume rejection, and the Layer-2 prompt-route companion. Required-gate input. |
| `test_doc_route_patterns.py` | Regression suite for the two TRAP-004 routes, read from the live `doc-routes.json` so it fails on a real edit rather than going stale: 10 must-fire sentences (each one an agent in this estate actually wrote), 3 that must stay silent, and 4 shallow-clone command forms. Exists because the 2026-08-26 widening of `claim-beyond-the-sample` silently deleted the `every <singular> in` coverage it already had — nothing tested the table, so narrowing it looked identical to widening it. |
| *…8 more* | see the files themselves — each gist is in [the audit's raw record](../docs/audits/2026-08-10-full-read/raw/gists.tsv). |
