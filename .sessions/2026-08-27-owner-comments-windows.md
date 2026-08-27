# 2026-08-27 — owner-comment verification on Windows

> **Status:** `in-progress` — reproducing and repairing the Windows-only
> verification failures without weakening the public owner-comment contract.

- **📊 Model:** GPT-5 family · high · portability repair
- **📍 Venue:** local-desktop

## Mission

Make the owner-comment implementation and its dedicated tests pass on an
ordinary Windows laptop without administrator rights or Developer Mode while
preserving canonical LF bytes, traversal protection, atomic writes, crash
recovery, append-only history, and exact staged-tree validation.

## 💡 Session idea

Keep platform-specific filesystem capability probes in the test harness so the
same contract can distinguish an unavailable symlink privilege from a product
failure without silently skipping portable recovery behavior.

## ⟲ Previous-session review

The contract session landed PR #952 with extensive crash, mode, traversal, and
reparse-point coverage, but its final verification was Linux-only. This session
preserves that contract and adds Windows evidence rather than reopening the
design.

Layer-2 handoff: null (Fleet Manager itself; no member repository is being
modified).

## Planned verification

- `python tools/test_owner_comments.py -q`
- `python tools/owner_comments.py check`
- `python bootstrap.py check --strict`
- Linux CI and an exact-head review before the completion flip
