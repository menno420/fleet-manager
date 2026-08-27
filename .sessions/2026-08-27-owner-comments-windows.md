# 2026-08-27 — owner-comment verification on Windows

> **Status:** `complete` — Windows and Linux-compatible verification now
> preserves the public owner-comment contract without requiring administrator
> rights or Developer Mode.

- **📊 Model:** GPT-5 family · high · runtime bugfix
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

## What shipped

- `tools/owner_comments.py` now flushes existing transaction artifacts through
  a platform-aware helper. POSIX keeps a read-only descriptor; Windows uses the
  write-capable descriptor its CRT requires, fixing the real rollback-backup
  `EBADF` without relaxing transaction prevalidation.
- `tools/test_owner_comments.py` writes canonical UTF-8/LF fixtures as bytes,
  uses path-level durability probes instead of Linux `/proc`, exercises the
  observable Windows writable/read-only mode distinction, and skips only real
  symlink creation when Windows reports privilege error 1314. Mocked reparse
  and fail-closed coverage remains active.
- `.claude/hooks/route_docs.py` normalizes Windows tool paths after removing
  checkout plumbing and treats an absolute checkout named in prompt text as an
  intentional Fleet Manager selection.

## Verification

- `python tools/test_owner_comments.py -q` — **PASS**, 91 tests in 234.807 s;
  five symlink-creation tests skipped because this ordinary Windows account has
  neither Developer Mode nor administrator link privilege.
- `python tools/owner_comments.py check` — **PASS**, 28 repositories, zero
  unconsumed and zero consumed records.
- `python bootstrap.py check --strict` — the only pre-flip finding is the
  designed born-red hold on this still-`in-progress` card; all other strict
  checks passed.
- Exact-head Codex review of `104946dd76` raised two portable-routing findings.
  Both were **[conceded]**: prompt checkout matching now observes path
  boundaries instead of accepting sibling prefixes, and comment-index
  self-reads require an exact normalized path instead of accepting backup
  filename substrings. Focused regressions cover both cases, and the complete
  dedicated suite above passed after the fixes.
- Exact-head Codex rereview of product commit `be589cb406` found no major
  issues. This status/closeout update is the deliberate records-only change
  after that clean review.
- The first Linux closeout run then exposed two gate-only issues: the card's
  task-class label was outside the taught taxonomy, and a CI checkout path of
  `.../fleet-manager/fleet-manager` let the canonical parent directory route a
  sibling `-old` prompt. Both were **[conceded]**. The label now uses
  `runtime bugfix`, and prompt routing removes checkout plumbing before slug
  matching while retaining the exact-checkout decision.
- `python bootstrap.py check --strict` — **PASS** after the completion flip;
  the Linux `substrate-gate` is also green on the same product head.
