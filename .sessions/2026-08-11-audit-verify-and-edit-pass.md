# 2026-08-11 · hub — verify the full-read audit's verdicts, then work its defect list

> **Status:** `in-progress`

- **📊 Model:** fable-5 · high · review/verify — re-run the headline-seven status
  table, then fix the verified live-surface defects at their sites and record
  each closure in findings.md with the command that proves it

Time: 2026-08-11 · venue: scheduled continuation session · branch
`claude/fleet-manager-verify-defects-cb6gxk` (restarted from `ba34aef` =
`origin/main` after fm #845 merged)

## Previous-session review

⟲ fm #839/#840/#842/#845 produced and corrected the full-read audit: 833/833
files read with coverage proved, 345 findings adversarially refuted to
101 defect / 205 harmless, the headline seven re-measured to 1 closed / 6 open.
Nothing was fixed — that session read, reported and recorded, and said so. This
session is the edit pass it left behind.

## What is about to happen

1. **Verify, not trust:** run all seven re-check commands from findings.md's
   status table; any command that fails to reproduce its verdict is a new
   finding for the same file.
2. **Fix the six open headline defects at their sites** (CAPABILITIES walls
   rows · init-prompt badge+deploy sentence · E1 link + queue entry ·
   SKILLS-local re-apply table · false-wall checker docstring · link-checker
   scan set), plus the live-surface defect band around them (boot file D1–D3,
   owner-queue D6–D8, decisions D9, SKILLS files D12–D15, hooks/skills
   D16–D22, tools D23–D29 where doc-safe).
3. **Record each closure in findings.md with the proving command**; leave
   everything not taken honestly OPEN.
4. Land on green: ready PR, `@codex review` and wait, flip last.

## Close-out

**Verification first, and it held:** all seven status-table re-check commands
were executed before any edit; all seven verdicts reproduced (1 closed / 6
open), so the table's command column is finally right on its third version.

**Shipped (PR #846, branch `claude/fleet-manager-verify-defects-cb6gxk`):**

- **34 defects closed at their sites**, each recorded in
  `docs/audits/2026-08-10-full-read/findings.md` with a proving command that
  was *run after the fix*: the six open headline rows (2–7) plus D1–D3, D5–D29,
  D50, D52, D79–D81, D85. Commit `fa3fd4e` (23 files) + the findings/card
  bookkeeping commits.
- Highlights: the three refuted CAPABILITIES walls retracted **in place**
  (registered against kit-upgrade clobber in `docs/SKILLS-local.md`
  § Generated-file corrections); `init-prompt-universal.md` re-badged
  `historical` per the fm #845 re-judgement; E1 linked from the program and
  added to the owner queue as `OQ-E1-FINAL-EAP-EMAIL`; the kit re-apply table
  now names **all seven** diverging skills with a committed derivation
  one-liner; the false-wall checker's docstring matches its 2026-08-06
  promotion; `check_docs_links.py` scans `.claude/` — and the new surface
  immediately exposed two checker defects (inline-code-span links flagged as
  dead; `slugify` collapsing GitHub's real `--`), both fixed with selftest
  cases, full run CLEAN over 369 files, exit 0.
- `install_root_hooks.py` now rescues **all six** hooks (change_guard,
  owner_review added; per-hook timeouts so the Stop hook keeps 120 s) —
  dry-run verified in a scratch root.

**Verify (run this session, tails verbatim):**

- `python3 scripts/check_docs_links.py --selftest` → `selftest: PASS (0 failure(s))`
- `python3 scripts/check_docs_links.py` → `check_docs_links: CLEAN — every intra-repo link in 369 file(s) resolves`, exit 0
- `python3 tools/check_no_false_walls.py --selftest` → fixture flag expected, PASS
- 40-assertion closure-proof battery → all PASS after four proving-command
  corrections (see 💡 below)
- `python3 bootstrap.py check --strict` → run at close; the only red is the
  designed born-red hold on this card until the flip

**Honestly not done — 67 defects remain OPEN** (D30–D49, D51, D53–D78,
D82–D84, D86–D101): overwhelmingly RECORD-tier era banners and
retired-apparatus scripts (the roster/trigger checker family, seat-era
`binding` badges, generated-file frozen snapshots) plus the kit-side pair
D44/D45 (bootstrap.py is GENERATED — v1.21.0 track). A mechanical
banner-sweep session closes most of them; nothing in the open set misroutes
the boot path.

⚑ The CAPABILITIES walls fix sits **inside the kit's capability-seed fence** —
an upgrade may silently restore the false rows. Registered in the re-apply
table; the durable fix is the kit's seed, which belongs to the v1.21.0
session's worklist.
⚑ `docs/current-state.md` deliberately untouched — it is 6,036 words against a
7,000-word orientation-headroom ceiling, so this session's record lives in
findings.md and this card instead of another Recently-shipped entry. Trimming
that file is standing welcome work for a future session.

💡 Session idea: **a closure's proving command must discriminate the claim
from its quoted retraction — and the only way to know it does is to run it.**
Five of my forty proving commands initially failed against my own fixes: a
phrase the fix wrapped across two lines, and greps re-matching the old wording
*inside the retraction parenthetical that replaced it*. The audit's command
column was wrong twice for the same reason before this session. A convention
(or a checker) for closure records: the command is run, its output pasted, and
it must return the corrected state, not merely fail to find the old one.

⟲ Previous-session review: fm #845 committed the chat-only residue of the
audit session — [D-0016], the measured headline-seven status block, the
open-PR-signal idea. Its status table was accurate to the tree, its two prior
bad re-check commands were honestly recorded, and the anchor-drift paragraph's
"derive, don't list" rule held up exactly as written (the planning-README
missing set had already grown from 3 to 4 by today).

**Codex round 1 (head `bbfc513`): 7 inline P2 findings — 7 `[conceded]`, all
verified against source before acting, all fixed:**

1. Code-span stripping leaked ``…``-delimited spans → run-aware
   `CODE_SPAN_RE` with a backreference + selftest case.
2. D1's recorded proof carried bash-escaped backticks GNU grep reads as a
   buffer anchor — the recorded command was not the executed command →
   re-recorded as the `-F` form, run verbatim.
3. D7's proof still grepped ASCII `D-0015` after the stamp pass converted the
   annotations to U+2011 → proof re-recorded with the real spelling.
4. D9's proof lagged the gate-driven amendment-grammar respelling → `-F` form
   matching the finalized field.
5. `owner_review.py`'s § 8 provenance line still said "turn ends untouched" —
   the exact residue class D18 fixed one paragraph up → amended.
6. **Real code defect:** the rescued `change_guard.py` mis-rooted `REPO` from
   `CLAUDE_PROJECT_DIR` in the multi-root case the rescue exists for →
   `__file__`-derived (git_state_guard's pattern); probed under a foreign
   `CLAUDE_PROJECT_DIR` → resolves to this repo; suite 16/16.
7. The `session-close` re-apply row's "no checker covers `.claude/`" went
   stale the moment this PR extended the scan set → row updated (advisory
   hand-run coverage, still nothing in CI).

Findings 2–4 sharpen the 💡 above into its final form: **the recorded command
must BE the executed string, and the whole battery must re-run after the last
edit of the session** — two proofs were invalidated by later same-session
fixes to the very files they proved. Full battery re-run after round 1:
**39/39 PASS**.

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached)

PR: menno420/fleet-manager#846 — ready, born-red hold until this badge flips.
