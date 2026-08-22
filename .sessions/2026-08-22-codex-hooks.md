# 2026-08-22 — Codex hooks on the owner laptop

> **Status:** `in-progress` — implementation and live verification are complete
> on PR #908; the required Codex review and deliberate final flip remain.

- **📊 Model:** gpt-5.6-sol · high · implementation
- **Venue:** owner-live, Codex desktop on the owner's Galaxy Book6 Pro.

## 💡 Session idea

Keep lifecycle policy canonical and make provider adapters deliberately thin:
translate only the event fields and response fields that differ. The next hook
port should start by capturing real Codex traffic for that event, then add one
adapter test from that traffic; do not copy Claude tool names into a green
fixture and call the mechanism live.

## ⟲ Previous-session review

The immediately preceding session landed fm #907: it executed the first
pre-archive write, corrected a stale disposition item, and withdrew a
dependabot merge-safety conclusion whose deployment rule had not been read.
Its durable lesson was to verify the resolver, not merely the artifact. This
session followed that shape: direct script fixtures were not accepted as the
claim that Codex itself ran the hooks; an installed-CLI turn was required.

## Shipped

- `d9dccd9` — born-red claim, pushed before implementation; READY PR #908 opened.
- `f5414c4` — `.codex/hooks.json`; the prompt-router and owner-review adapters;
  their reference; the executable 21-contract suite; tools index; guard-fire
  telemetry from the strict check.
- Current close-out batch — the verified capability entry, worktree caveat,
  and this evidence record. The commit SHA will be added before the flip.

The document router calls the existing `.claude/hooks/route_docs.py` and
`doc-routes.json`, replacing only the POSIX temp fallback and removing Codex's
unsupported `suppressOutput` response field. The Stop adapter reads Codex's
native `last_assistant_message` and loads the existing fixed questions through
Python's AST; it does not import or execute the Claude hook's optional Gemini,
credential or transcript paths.

## Live result

Codex CLI `0.149.0-alpha.4.1`, in a disposable ordinary Windows clone of
`f5414c4`, showed **2 installed / 2 active** project hooks after the exact
definitions were reviewed in `/hooks`. One read-only turn naming
`spider-swing` then produced two assistant messages:

1. the first named `docs/repos/spider-swing/README.md` and attributed it to the
   injected estate-routing note;
2. the Stop continuation named that mapping as its load-bearing claim, stated
   that it had run no command and read no file, and marked the derivation
   `[survived]`.

The corresponding temp evidence is route-state file
`01a02add-0f5e-7741-b59b-ed25bef69174.json` plus owner-review telemetry
`reply_chars: 545, blocked: true, enriched: false` for the same session id.

A linked worktree did not activate the unmerged project layer: Codex's trust
prompt said trust would apply to primary checkout `C:\dev\fleet-manager`.
The ordinary clone was the working pre-merge test venue. That setup fact is now
in the hook reference and capability ledger; it is not an adapter failure.

## Verify

- `python tools/test_codex_hooks.py` → **21 PASS**, `Codex hooks: all contracts
  passed`, exit 0.
- `python -m py_compile .codex/hooks/route_docs.py
  .codex/hooks/owner_review.py tools/test_codex_hooks.py` → exit 0.
- `python bootstrap.py check --strict` before the flip → exit 1 on the designed
  born-red hold only: this card is in-progress and is missing its completed
  status; doc routes and false walls passed. Guard telemetry was retained.
- Installed Codex CLI read-only smoke turn → exit 0; route state + Stop
  telemetry above; two-message continuation observed in the JSON event stream.

## Review

Codex review on `abc0622` found one P2: the contract suite unconditionally
launched PowerShell, so its documented repository-wide command would crash on
Linux before reporting a result. **[conceded]** The fixture now tests
`commandWindows` when PowerShell is installed and otherwise tests the POSIX
`command` through Bash, both from the nested `docs/` directory. This correction
requires a new review on the new head before the flip.

## Close-out

Capability delta: Codex repo-local Windows hooks are proven live at prompt and
Stop. The pre-merge linked-worktree activation caveat is recorded in
`docs/CAPABILITIES.md` and `.codex/hooks/README.md`.

⚑ decide-and-flag: none. No compaction hook was added: no missing-state failure
was measured and the promotion rule does not permit speculative mandatory
infrastructure.

Layer-2 handoff: null (fleet-manager itself)

PR: #908 · READY and born-red; implementation complete, review and flip pending.
