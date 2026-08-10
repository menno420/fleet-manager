# 2026-08-10 · hub — D2 fleet-manager truth pass

> **Status:** in-progress

- **📊 Model:** GPT-5 family · high · documentation truth pass
- Time: 2026-08-10 · venue: ChatGPT Work owner-live chat · branch
  `claude/d2-fleet-manager-truth-pass`

💡 Session idea: a front door is only true when a cold reader can prove the
purpose, live state, and next action without inheriting the author's context.

Layer-2 handoff: null (fleet-manager itself)

## Previous-session review

⟲ fm #836 independently verified the late, previously unreviewed checker changes
from fm #835, recorded the remaining over-exemption without patching it, and
turned the Work surface's GitHub route into a measured capability record. Its
own exact-head Codex review returned no findings. The useful handoff into this
session was the unresolved documentation question: the surface had proved it
could review and fix code, but had not yet carried fleet-manager's documentation
method from a cold start.

## What is about to happen

Audit the repository as a genuinely cold no-boot-file session, correct
fleet-manager's documentation front door so its purpose, live state, and next
action are recoverable from no more than three files, update D2's ledger and NOW
pointer, and land the docs-only result through the full review loop.

## Close-out

### Shipped

- `README.md`, `docs/current-state.md`, and
  `docs/planning/2026-07-26-consolidation-program.md` — a surface-neutral cold
  route that directly states purpose, live state, and next action; D2's ledger
  advances from fleet-manager to shiftlife while E1 remains owner-reserved.
- `.claude/CLAUDE.md` and
  `docs/prompts/chatgpt-project-instructions.md` — the cold contract separated
  from the deeper comprehension path on both surfaces, with mutable inventory
  counts removed.
- `docs/findings/2026-08-10-fleet-manager-cold-read.md` and the findings index —
  the actual no-boot observation, every hunt and contradiction, the era rule,
  baseline exit codes, and the repaired-route proof.
- The dated closeout, fleet account, fleet-triage, old reading path, telemetry
  guide, and Projects guide — fully historical snapshots now say so at the top.
  The owner reflection, playbook, and agent-orientation guide use the mixed-era
  rule; their preserved bodies were not silently rewritten.
- `docs/owner-queue.md` and `docs/owner-profile.md` — live work no longer routes
  through the retired control bus. The `AGENTS.md` choice and separate kit
  release session are now real owner-queue items; inherited cross-repo asks are
  explicitly not re-verified by this repo-only pass.
- `docs/execution-surfaces.md`, `docs/CAPABILITIES.md`, and `docs/intent.md` —
  the local-push contradiction corrected and the deliberate Work documentation
  test recorded as a bounded capability rather than a general guarantee.
- `docs/repos/README.md` — volatile repository totals removed from the Layer-2
  coverage prose; the explicit set is the source.
- `.substrate/guard-fires.jsonl` — retained telemetry appended by the required
  strict runs. No application code, checker, hook, workflow, or generated kit
  source changed.

### Verify — real exit codes

Baseline on merged `main` (`2a0f16f8dfa20f132a1fe10bd89613275955984b`), each
command in a separate process:

```
python3 bootstrap.py check --strict             → 0
python3 tools/check_doc_routes.py --strict      → 0
python3 tools/check_no_false_walls.py --strict  → 0
python3 tools/test_change_guard.py              → 0  (16/16)
python3 tools/test_trigger_tools_guard.py        → 0  (69/69)
```

Final pre-review strict result:

```
python3 bootstrap.py check --strict             → 1
```

Its sole finding is the designed born-red hold on this in-progress card. The
gate appended its telemetry and named no documentation defect. The final `0`
is owed after exact-head review, when this badge is the last substantive state
change. Independently, `scripts/check_docs_links.py --no-anchors` exited `0`
with every scanned intra-repo link resolving, and `git diff --check` exited `0`.

### Cold proof — only the accepted route

From `README.md` → `docs/current-state.md` → the consolidation program alone:

- **Purpose:** fleet-manager is the estate router and records home; product
  truth remains in each product repository.
- **Live state:** the autonomous program is closed, seat machinery is
  historical, regular owner-directed sessions are working D2, E1 remains
  owner-reserved, and the vendored kit is v1.20.2.
- **Next:** fleet-manager's D2 pass is complete; shiftlife is the next
  actionable repository.

No fourth repository file is required.

### Review

Pending Codex review of the exact published head. Any finding will be reproduced
and dispositioned before the completion flip.

### Capability delta

One bounded capability appended: ChatGPT Work carried this documentation truth
pass from an empty directory and no auto-loaded repository file. The entry says
what that proves and explicitly does not generalise it to unattended
correctness.

### ⚑ Owner-facing

- `OQ-FM-AGENTS-BOOT` — recommendation: add a minimal root pointer now that the
  no-boot measurement is preserved; owner decides.
- `OQ-KIT-V1-21-RELEASE` — the already-decided kit release remains a separate,
  explicitly started owner-gated session; untouched here.

### Ideas

The session idea became the README's executable reading contract and the dated
finding. The existing `derive-dont-state-counts-2026-08-10.md` idea was groomed
in practice: volatile counts were removed from the boot and Layer-2 prose, but
its proposed checker remains captured and unbuilt because code is outside D2.

### PR

#837 — READY on `claude/d2-fleet-manager-truth-pass`; completion and merge
pending exact-head review and green CI.
