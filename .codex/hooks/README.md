# Codex hook adapters

> **Status:** `reference` · added 2026-08-22

These are Fleet Manager's first repo-local [Codex hooks](https://learn.chatgpt.com/docs/hooks).
They make two measured Claude mechanisms available to Codex sessions without
pretending the two hosts have the same event schema.

| Codex event | Adapter | Canonical behavior reused |
|---|---|---|
| `UserPromptSubmit` | `route_docs.py` | `.claude/hooks/route_docs.py` + `doc-routes.json` |
| `Stop` | `owner_review.py` | the fixed questions and response contract in `.claude/hooks/owner_review.py` |

## Why adapters, not copied hooks

The prompt event is close enough to reuse the Claude matcher, but Codex does
not currently support its top-level `suppressOutput` field. The adapter runs
the canonical matcher, removes only that unsupported field, and forwards the
remaining `additionalContext`. It also gives the Claude matcher a real Windows
temporary directory; its `/tmp` fallback is not a Windows directory.

The Stop event is different. Codex supplies `last_assistant_message` directly,
while the Claude hook reconstructs the reply from Claude's transcript format.
The adapter uses the native Codex field and loads the two fixed questions from
the Claude source. It deliberately does not run the optional Gemini enrichment:
the fixed question is the measured mechanism, and making a Windows Codex turn
depend on credentials or network would weaken it.

Both adapters fail open. A malformed event, missing source, subprocess error or
timeout produces no hook output and never blocks the session. The owner-review
loop guard, `stop_hook_active`, still limits it to one round per turn.

## Why only these two

Fleet Manager's other Claude hooks sit on tool payloads and tool names. Codex
covers Bash, `apply_patch`, MCP and local function tools, but their inputs do
not share Claude's `Read` / `Edit` / `Write` shapes. Porting those guards before
recording real Codex traffic would create a guard that looked live while
missing the calls it was meant to inspect.

No compaction hook is registered either. The repository already reloads its
instructions after compaction, and no lost-state failure has been measured
here. Add one only when a concrete payload can restore concrete missing state.

## Registration and trust

`.codex/hooks.json` is project-scoped. Codex discovers it automatically when
the repository is the project, but a new or changed non-managed hook definition
must be reviewed once in `/hooks`; trust is tied to the exact definition hash.
The registration includes both `command` and `commandWindows`. Each resolves
the active Git worktree root first, so it works from a nested directory and
does not hard-code `C:\dev\fleet-manager`.

**Pre-merge worktree caveat, measured on Codex CLI 0.149.0-alpha.4.1 for
Windows:** Codex's project-trust prompt canonicalized a linked worktree to its
primary checkout. An unmerged `.codex/hooks.json` present only in the linked
worktree therefore did not become active there. A disposable ordinary clone of
the PR branch loaded, reviewed and ran both hooks. Use that shape for a live
pre-merge smoke test; once the definition is on the primary checkout's branch,
the caveat no longer applies.

## Verification

Run the executable contract suite from the repository root:

```bash
python3 tools/test_codex_hooks.py
```

It covers prompt routing, once-per-session deduplication, removal of the
unsupported field, Stop blocking, the one-round guard, fail-open inputs, and
the exact active-platform registration command from a nested directory
(`commandWindows` through PowerShell, or `command` through Bash).

Then verify discovery in a real Codex session:

1. Open `/hooks` and approve the two project hook definitions.
2. Submit a prompt naming `spider-swing`; the Layer 2 entry point should appear
   as additional context before work begins.
3. Let a claim-bearing reply longer than 400 characters finish; owner review
   should return once, and its second pass should complete normally.

Transient state stays outside the repository:

- document-route dedupe: the operating system temp directory under
  `claude-doc-routes/` (the canonical matcher's existing format);
- Codex owner-review telemetry: the operating system temp directory under
  `codex-owner-review/log.jsonl`.
