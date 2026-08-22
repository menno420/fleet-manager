# 2026-08-22 — the Windows case collision that shadows CAPABILITIES.md

> **Status:** `in-progress`

- **📊 Model:** fable-5 · medium · docs-only
- **Venue:** owner-live, local Claude Code on the owner's new Galaxy Book6 Pro
  (Windows 11, NTFS case-insensitive) — the estate's first local Windows session.

## Session idea

`docs/CAPABILITIES.md` (1,865 lines — the capability ledger and THE DISCOVERY
RULE) and `docs/capabilities.md` (a 9-line "MOVED" pointer stub) are **both
tracked**. NTFS is case-insensitive, so a Windows clone cannot hold both. Git
warns once at clone time and is silent forever after.

## Previous-session review

The stub was created 2026-07-12 (v3.4 delta 14, I-44 "case-duplicate
resolution") to keep old links resolving after the fold into the uppercase file.
On Linux that is harmless. Nothing recorded that it becomes actively destructive
on a case-insensitive filesystem — because until 2026-08-21 the estate had no
Windows checkout.

## What was measured (MEASURED 2026-08-22, this machine)

1. **A fresh `git clone` silently checks out the 9-line stub under the name
   `docs/CAPABILITIES.md`.** Every later read of the capability ledger — by a
   session, a hook, or a checker — returns the stub.
2. **`python3 scripts/preflight.py` fails**: `doc routes -> exit 1`, **6 errors**,
   all of the form *"COVERAGE — none of its N patterns appears in
   docs/CAPABILITIES.md"* (`recording-a-wall`, `discovery-probe`, `github-api`,
   `provisioned-secrets`, `youtube`, `empty-repo-first-commit`). The routes are
   fine; the file they point at is the stub.
3. **The serious one — a data-loss landmine.** `git status` reports
   `M docs/CAPABILITIES.md`, because the working tree holds the stub while the
   index holds the real blob. `git diff --stat` on a clean clone:
   `1 file changed, 7 insertions(+), 1863 deletions(-)`. **Any session running
   `git add .` or `git commit -a` on Windows commits the stub over the ledger.**

## The fix

Delete the lowercase `docs/capabilities.md` stub. Its stated purpose ("so old
links resolve") does not work on Windows anyway — there, it *is* the uppercase
file — and it now shadows the document it points to. Under `OD-3` as amended
(cleanup allowed with a stated reason) this is the "served its purpose, no
longer of value" case.

`docs/MAP.md` and the boot file already route to the uppercase path only; a
tree-wide grep for the lowercase spelling finds no inbound reference.

## Verification

- `python3 tools/check_doc_routes.py` → **54 routes · 28 docs routed · 0 errors ·
  4 notes**, exit 0 (was 6 errors).
- `python3 scripts/preflight.py` → `doc routes -> exit 0`; `false walls -> exit 0`.
- `docs/CAPABILITIES.md` restored to its real 1,865 lines; `git status` no longer
  reports it modified.

## Residue

`.substrate/guard-fires.jsonl` carries the telemetry delta from this session's
gate runs, retained per `current-state.md` § Live operating mechanisms.

The four `unrouted:` NOTEs in the doc-route checker are pre-existing and
untouched by this change.
