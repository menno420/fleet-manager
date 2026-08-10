# 2026-08-10 · hub — persist the audit's raw record; close Codex round 2

> **Status:** `in-progress`

- **📊 Model:** fable-5 family · high · review/verify
- Time: 2026-08-10 · venue: owner-live hub chat (same session as fm #839, model
  switched opus-5 → fable-5 by the owner) · branch
  `claude/fleet-manager-full-audit-lty31q` restarted from merged `main`

💡 Session idea: raw evidence that lives only in a container is not a record; a
review finding answered after the merge is still a finding, and the cheap moment
to persist both is before anything else happens.

Layer-2 handoff: null (fleet-manager itself)

## What is about to happen

fm #839 merged while Codex's round-2 review was still in flight; its seven
findings landed post-merge and are all real. This PR closes them and persists the
audit's raw record — the per-file gists and the full candidate→refuter
adjudication — which until now existed only in the session container. It also
records two owner statements from the live chat that the tree did not carry: the
D2 target correction (shiftlife is not active), and that no 1-PR limit was ever
his instruction (verified: no such limit exists anywhere in the repo — the
constraint came from harness notification text, not from any committed file).

## Previous-session review

⟲ fm #839 (same session, pre-model-switch) read all 833 tracked files with the
coverage proved from agent returns, and put 345 findings through independent
refutation. Its residue is exactly this PR: raw evidence unpersisted, seven
post-merge review findings, and the top defect (the NOW pointer) still awaiting
the owner statement it needed — which the owner has now given live.

## Close-out

### Shipped

- `docs/audits/2026-08-10-full-read/raw/` — `gists.tsv` (833 rows, the per-file
  reading evidence) + `adjudication.jsonl` (345 rows, every refuter verdict with
  its reason and commands). Codex round 2's two P1 absences, closed.
- `verification.md` corrected to **829/3 byte-exact** with the false "nothing
  else" clause retracted, not reworded; `findings.md` regenerated — 16 same-site
  duplicates merged (**101 defect / 205 harmless / 16 merged = 322**), evidence
  commands checkout-independent, the retired-ORDER reference back to harmless.
- **OD-15** in the program's directive table + the NOW pointer marked
  **shiftlife SUPERSEDED** (owner, live, 2026-08-10) with OD-13 as the standing
  answer pending `OQ-FM-D2-TARGET`; current-state's three echoes corrected. The
  audit's top defect, closed at its point of action.
- **The browsable-repo layer, designed and built**:
  `docs/planning/2026-08-10-repo-navigation-plan.md` (the owner's directive +
  design) · `docs/MAP.md` (every area, one line, CORE/TASK/RECORD tier) ·
  `README.md` rewritten (the story in 60 seconds — estate → EAP program →
  closed 2026-07-21 → consolidation; the six-read mandatory order, each with
  what it gives you) · eight missing area READMEs (scripts, tools, environments,
  templates, docs/conventions, docs/retro, docs/succession, docs/audits), each a
  "you are here" built from the audit's own gists · `docs/findings/README.md`
  regenerated **complete** (42 rows; the old index listed 25) · boot file
  pointed at the order + map at minimal word cost.
- Verified negative, owner-asked: **no 1-PR limit exists anywhere in this repo**
  — the constraint came from harness notification text, not a committed file.

### Verify — real exit codes

```
python3 bootstrap.py check --strict   → 1  (sole finding: this card's designed born-red hold)
added-card lane, run direct           → 1  (session-card-hold only — no masked finding)
link scan over the 11 new/rewritten files → 0 dead
```

### Capability delta

None. One method note: the per-file gists persisted by this PR were used as the
source for every "what this file is" line written today — the write-time hook
fired once on an unread description and the committed gist answered it, which is
the mechanism working end to end.

### ⚑ Owner-facing

- `OQ-FM-D2-TARGET` — unchanged; OD-15 is recorded, the concrete next repo is
  still his call.

### Ideas

💡 Groomed forward: `derive-dont-state-counts` — the area READMEs deliberately
carry no file counts, only links, so they cannot go stale the way every frozen
count has.

### ⟲ Previous-session review

fm #839 (same session, pre-switch) delivered the coverage proof but let the PR
merge with a review in flight and its raw evidence unpersisted — both now
repaired here rather than explained away.
