# fleet-manager's cold front door — failure, repair, and proof

> **Status:** `reference` · 2026-08-10 · fm #837
>
> **Scope:** a ChatGPT Work session with an empty working directory and no
> automatically loaded repository file. This is the D2 truth pass for
> fleet-manager only. Certainty labels use the legend in
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md)
> § 0.

## 1 · The cold observation

`MEASURED`. Nothing in the repository loaded for this session. The working
directory began empty; the repository was cloned before any file could be read.
Both local `HEAD` and `origin/main` resolved to
`2a0f16f8dfa20f132a1fe10bd89613275955984b`, whose latest merged pull request
was fm #836. This is the surface D2 is supposed to measure, not a simulation of
one.

The old front door failed the acceptance test:

| fact a cold session needed | what the repository said at the starting commit | result | certainty |
|---|---|---|---|
| **Purpose** | `README.md` called the repo the manager Project's home and said generated fleet state was canonical here. `docs/intent.md` instead defined the present purpose as router and records home, with product truth in each product repo. | A fourth file was required to settle a first-file contradiction. **FAIL.** | `MEASURED` |
| **Live state** | `docs/current-state.md` was marked living but opened by sending the reader to the July closeout, then led with a seat that was “live” and an autonomous loop that “runs.” | The current file's first answer was historical. A reader had to recognize the era and override the document's own routing. **FAIL.** | `MEASURED` |
| **Next step** | The program's NOW heading named E1, while its own note made E1 owner-reserved and redirected available work to D2. `current-state.md` still named the already-resolved apparatus-sizing decision. | The answer could be reconstructed, but only by negating two prominent pointers. **FAIL.** | `MEASURED` |

`REASONED`. The root defect was not merely an omitted link. The repository had
several individually plausible eras with no current surface that declared
which one won. A careful reader did extra archaeology; a fast reader would have
reported the seat era as live.

## 2 · Every hunt and guess this surface exposed

These are findings because the session encountered them before repairing them:

- `MEASURED`: `.claude/CLAUDE.md` did not auto-load. It was a useful deep map
  once opened manually, but it could not be this surface's first file.
- `MEASURED`: the boot file mixed a “one command” verification claim with a
  “both gates” instruction and froze skill and corpus counts in prose. The
  exact independent baseline commands had to be recovered from a dated
  verification record rather than the front door.
- `MEASURED`: the boot file's deep path was useful for comprehension but much
  larger than D2's three-file limit. Treating that path as the acceptance route
  would make the test impossible by definition.
- `MEASURED`: `docs/execution-surfaces.md` said configured local git could push
  on the same page that recorded authenticated local push failing and the
  connector succeeding.
- `MEASURED`: `docs/owner-profile.md` still told the owner to place orders in
  the retired `control/inbox.md`; `docs/owner-queue.md` still routed current
  work through dated seat-era action lists.
- `MEASURED`: the Layer-2 coverage page embedded repository totals in prose.
  The tree had already demonstrated why those totals drift; the list is now
  named instead of counted.
- `MEASURED`: the earlier handoff said both the `AGENTS.md` decision and the
  dedicated kit release session were recorded where they belonged. Neither
  appeared in the owner queue. They do now.

## 3 · The repair: one neutral route, one deep route

`MEASURED`. The surface-neutral cold route is now exactly:

| file | job |
|---|---|
| [`../../README.md`](../../README.md) | State purpose and boundary; distinguish live surfaces from historical records. |
| [`../current-state.md`](../current-state.md) | State the current operating era, live mechanisms, and work state. |
| [`../planning/2026-07-26-consolidation-program.md`](../planning/2026-07-26-consolidation-program.md) | Hold the single NOW pointer and D2 repository order. |

Claude Code may begin with its auto-loaded boot file in place of README. The
boot file points to the same two ledgers, then carries a deliberately deeper
comprehension path. A surface with no boot file begins at README. Neither route
may hide a failed cold answer by opening a fourth file.

## 4 · Era rule chosen and applied

`REASONED`. A single `historical` label is wrong for a document that still
carries live rules, but silently rewriting its dated body destroys evidence.
The applied rule is:

1. A fully dated snapshot gets `Status: historical` plus a top banner pointing
   to its live successor. Its recorded body is not rewritten.
2. A mixed-era document keeps its existing status and gets a top banner that
   names which parts remain live and which are historical.
3. A living ledger gets a current summary first; its historical tail stays in
   place under an explicit superseded heading.

`MEASURED`. The snapshot rule was applied to the hub closeout, fleet account,
fleet triage, old reading path, telemetry guide, and Projects guide. The mixed
rule was applied to the owner reflection, playbook, and agent-orientation
guide. `docs/current-state.md` uses the living-ledger rule. Existing historical
banners on the roster, mission, next-tasks, resume, and control surfaces were
kept; the control banner's live pointer was corrected.

## 5 · Baseline and proof

`MEASURED`. Before documentation edits, each requested baseline ran as its own
process on the starting commit plus the expected telemetry delta:

| command | exit |
|---|---:|
| `python3 bootstrap.py check --strict` | 0 |
| `python3 tools/check_doc_routes.py --strict` | 0 |
| `python3 tools/check_no_false_walls.py --strict` | 0 |
| `python3 tools/test_change_guard.py` | 0 |
| `python3 tools/test_trigger_tools_guard.py` | 0 |

`MEASURED`. Reading only the repaired three-file route yields this complete
orientation:

- **Purpose:** fleet-manager is the estate router and records home. It owns
  estate-level continuity and points to product truth in each product repo.
- **Live state:** the autonomous Projects program is closed; work happens in
  regular owner-directed sessions. Seat machinery is historical. D2 is active,
  E1 is still reserved for the owner, and fleet-manager vendors kit v1.20.2.
- **Next step:** fleet-manager's D2 pass is complete; the next actionable
  repository in D2 is **shiftlife**.

No fourth repository file is needed for any of those statements. The final
strict gate and exact-head pull-request review are landing evidence and belong
in the session card; they do not change the orientation result.

## 6 · Deliberate limits and owner follow-on

- `MEASURED`: no application code, checker, hook, workflow, or generated kit
  source changed. This was a documentation truth pass.
- `MEASURED`: this session read the complete mandated path and audited the
  front-door and era-routing surfaces it exposed. It did not claim a recursive
  semantic review of every historical document in the repository.
- `UNVERIFIED`: inherited owner-queue items belonging to other repositories or
  external accounts were not re-checked. The queue now says so at the top.
- `OWNER`: a root `AGENTS.md` was deliberately not added. The cold evidence now
  makes the case for a minimal pointer compelling, but the choice remains
  `OQ-FM-AGENTS-BOOT`.
- `OWNER`: substrate-kit v1.21.0 remains a separate owner-gated release session,
  recorded as `OQ-KIT-V1-21-RELEASE` and untouched here.
