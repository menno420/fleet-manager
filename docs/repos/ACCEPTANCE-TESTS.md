# Layer 2 — the two acceptance tests, and what they returned

> **Status:** `audit` · run **2026-08-08**
>
> Both tests are **owner-stated** and they are the definition of done for
> `docs/repos/`, not a nice-to-have
> ([`../planning/2026-08-08-fleet-manager-as-index.md`](../planning/2026-08-08-fleet-manager-as-index.md)
> § "Acceptance tests"). Written down first, then run — a test described but
> never executed is the same defect as a design that lives only in a chat.
>
> Re-run these whenever a folder is added or the shape changes.

## Test 1 — the single-repo boot

**Setup:** boot fleet-manager, say *"this session is for spider-swing"*.
**Passes when:** the session finds that repo's objectives, capabilities and
where to look — **before attaching it**.

### Result: **PASS**, 14/14 questions answerable from the folder alone

Run 2026-08-08 with the repo not attached. Each row is a question a session
must answer before it can decide anything, checked against the folder:

| question | answered in |
|---|---|
| what is it — engine, platform, genre | `README.md` |
| what is it called when published | `README.md` |
| the current objective / north star | `README.md` |
| what is **deferred by directive** (so it is not picked up by accident) | `README.md` |
| what is blocking it | `README.md` |
| the hard schedule constraint (12 testers × 14 continuous days) | `README.md` |
| do I even need to attach it | `README.md` |
| where to look once attached | `README.md` |
| which paths reach it | `capabilities.md` |
| how PR review works here | `capabilities.md` |
| which gates must be green | `working-here.md` |
| what command verifies before push | `working-here.md` |
| traps that have actually bitten | `working-here.md` |
| what this estate has already written about it | `records.md` |

```bash
# the mechanical half, re-runnable
cd docs/repos/spider-swing && grep -ciE 'Godot 4\.7\.1|Slingy Spider|north star' README.md
```

**Honest limit on this result.** The check above establishes the answers are
**present**. It does not establish they are **good** — that is a judgement, and
mine is `REASONED`, not `MEASURED`: a cold session reading `README.md` alone
lands on the right first move (the difficulty thread, with the run-evidence
system as its instrument) and correctly does *not* try to route around the
owner-gated Play items. The strongest available falsification is an unprimed
reader who has never seen this repo. That has not been run.

## Test 2 — the survey

**Setup:** boot fleet-manager, ask *"what are the current open projects"*.
**Passes when:** the session reviews the repo folders and, for each, states the
current main point of importance plus a short suggestion for how to start or
continue — so the owner can **choose** what to work on.

This is the stronger test: it exercises every folder at once and fails loudly on
any that is empty, stale or unreadable.

### Result: **PARTIAL PASS — and the partiality is the honest outcome, not a defect hidden**

What passed, measured 2026-08-08:

- The thread blocks are **machine-legible**. A survey walking `docs/repos/*/README.md`
  extracts, for spider-swing, four threads with their states parsed cleanly —
  `core feel & difficulty` **active** · `Google Play release` **active,
  owner-gated** · `run evidence` **closed 2026-08-06** · `generated art
  pipeline` **paused** — plus each active thread's next step.
- **Paused and closed threads survive** alongside active ones, which is the
  whole reason threads are the unit of replacement rather than the file.
- **Absence is visible, not silent.** `README.md`'s coverage table marks every
  unbuilt repo `⬜ not built` and states in words that a blank row means *"not
  written yet"*, never *"nothing is happening there"*. Silence and "nothing
  active" are different answers, and the owner is choosing what to work on from
  this.

What cannot pass yet: **1 folder of a 24-repo estate exists.** The test as
stated exercises *every* folder, so it is not fully satisfiable until the other
Tier-1 folders are built — which is deliberately out of this session's scope
(build one, show the shape, replicate only after sign-off). Re-run this test
after each folder lands; it is the one that will catch a stub that was never
filled.

```bash
# the survey, re-runnable — prints each repo's threads and next steps
for d in docs/repos/*/; do echo "== $(basename "$d")"; \
  grep -E '^### Thread:|^Next step:' "$d/README.md"; done
```

## Test 3 — retrieval (not owner-stated; added because it is what makes Layer 1 light)

**Passes when:** naming a repo in a message pulls its Layer 2 `README.md` in
without the session having to search for it.

### Result: **PASS**, 6/6

`route_docs.py` now runs on `UserPromptSubmit` as well as `PreToolUse`.
`MEASURED` 2026-08-08 by piping payloads into the hook directly:

| case | expected | got |
|---|---|---|
| `UserPromptSubmit` prompt naming `spider-swing` | fires, `hookEventName: UserPromptSubmit` | ✔ |
| `UserPromptSubmit` prompt naming `Slingy Spider` | fires (publishing name routes too) | ✔ |
| `UserPromptSubmit` unrelated prompt | **silent** | ✔ |
| `cwd` / `transcript_path` containing the repo name, empty prompt | **silent** — plumbing never trips a route | ✔ |
| `PreToolUse` Bash mentioning the repo | fires, `hookEventName: PreToolUse` (no regression) | ✔ |
| malformed stdin | exit 0, no output (fail-open) | ✔ |

The payload field was **verified, not assumed**: `UserPromptSubmit` carries the
message as a top-level `prompt` key, sibling to `hook_event_name` — read out of
the shipped binary, which builds it as
`{...,hook_event_name:"UserPromptSubmit",prompt:e,...}`. The public hooks
reference does not publish that field. A defensive fallback means a future
rename degrades to noisier matching rather than silence.

**Note for anyone reading the provenance findings:** that document refutes
`UserPromptSubmit` for the *review* hook, on the grounds that at prompt-submit
no claim exists yet to ask about. That argument is specific to review and does
not touch retrieval — retrieval is precisely the thing that belongs *before*
work starts. The two hooks share an event surface and disagree about it for good
reasons.
