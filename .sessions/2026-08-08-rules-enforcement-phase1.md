# 2026-08-08 · hub — Phase 1: make the corpus trustworthy enough to retrieve from

> **Status:** `complete`

- **📊 Model:** fable-5 · high · feature build — retrieval & orientation repair, plus the roadmap that frames it

Time: 2026-08-08 · venue: owner-live hub chat · branch
`claude/fleet-manager-rules-enforcement-18o8t1` · PR fm #826

💡 Session idea: **an orientation surface that is wrong costs more than one that
is missing.** A missing doc produces a search; a stale router produces confident
action in the wrong direction, and nothing downstream can tell the difference.
That is why most of this session is subtraction and correction rather than
addition — and why the boot file ended **31 words shorter** while gaining four
things it did not have.

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached — the
step this session added to `session-close`, run on its own first session)

## Previous-session review

⟲ The 2026-08-08 index/instruments sessions (#817–#825) built the five injection
mechanisms and the finding that organises them, and stopped at exactly the right
place: they mechanised the *action* moment and left the *orientation* moment
alone. This session is the other half, and it inherits their central result —
rules bind only when they arrive — which is why almost nothing here is new prose.

## What shipped

**The roadmap that reframes the work** —
[`docs/planning/2026-08-08-agent-operating-environment-roadmap.md`](../docs/planning/2026-08-08-agent-operating-environment-roadmap.md),
recording the owner's architecture review: the goal is a **model-independent agent
operating environment** *[phrase superseded later the same day — the precise one is
**provider-aware, model-portable**; kept as written because dated cards are not
silently rewritten]*, and the bottleneck is **upstream of code** — understanding
intent, retrieving intent that already exists, selecting the procedure, carrying it
through to review. Phase 2 specifies the intent map (EXPLICIT / ESTABLISHED /
DERIVED / OPEN, never collapsed), LOW/MEDIUM/**HIGH** ambiguity with *no silent
resolution of HIGH*, the `RESOLVED` / `NEEDS OWNER` seam before planning, **ephemeral
maps kept distinct from durable intent**, and the invariant that every active repo has
*one discoverable canonical intent source* — not necessarily a file called
`intent.md`. Phase 3: `/documentation`, INTENT/ACTION/CLAIM as the hook moments, kit
inheritance instead of copying, structured traps, review tracing back to intent, the
procedure registry, and the workspace topology (Drive = persistent **non-code
supporting material**; mappings optional and many-to-many, never 1:1 per repo).

**Phase 1 itself:**

- **Boot file, net-zero words (2807 → 2776).** Stale route count and roster clause
  corrected; the verify truth stated as **one command** with the note that the check
  list lives in `scripts/preflight.py`, not in prose; the **Stop-hook answer protocol**
  added (`[survived]`/`[conceded]`/`[partial]`) — the one piece with no delivery
  channel of its own; a canonical-for line for the decision records; era flags on the
  floor list. Paid for by cutting the Gemini bullet down to its decision rule, because
  the doc-routing hook already delivers the rest at the moment of a Gemini call.
- **`session-close`** gained the **Layer 2 handoff step** that `docs/repos/README.md`
  and the index plan both promised and the skill never carried, with a pinned null
  format; the verify step now names one command instead of an enumeration that had
  gone stale at two of three; the §7/NOW ledger step; steps rewritten at their live
  venue instead of leaving a translation for the reader.
- **One prompt route** (`error-review`) under an **admission bar written into the route
  table**: name the wrong action, distinctive multi-word patterns only,
  inject the method never an interpretation, `UserPromptSubmit`-only.
- **Six seat-era routers now say which era they describe** — `NEXT-TASKS`, `RESUME`,
  `reading-path`, `PROJECT-CLOSEOUT` §5, `AGENT_ORIENTATION`, `MISSION`. Additive
  banners, closed-set badges, nothing deleted (OD-3).
- **Three defects found by using the instruments, all in the instruments:**
  1. a check-exceptions entry suppressing one decision-stamp finding under a
     *different* decision's rationale (Codex P2, verified against `apply_allowlist`
     before acting);
  2. `preflight.py` reporting a red against the leg that had **passed**, because
     bootstrap surfaces only its last line and a failing run ends on telemetry —
     the fix verified live in CI on the next run;
  3. `read_before_write`'s badge check applied the **docs** taxonomy to **session
     cards**, whose vocabulary is different (`in-progress`, `complete`) — so it
     fired on every born-red card and again on every flip, twice per session
     forever. Scoped to docs; the task-class half, which is what caught the
     CI-only red on 2026-08-08, still runs on cards. 5/5 on a case table.

## Measured

**The boot file is a sufficient index — scored on first actions, not recall.** A fresh
subagent given *only* `.claude/CLAUDE.md` answered 6/6 and named its first three
actions as the boot-triad diagnostic → the owner reflection (entry 0) → `current-state`
(entry 1). All four new additions were retrieved correctly. It also reported the honest
limit unprompted: *what* the next step is "is not answerable from the boot file alone."

**The Layer 2 folder drives a correct first move without the repo.** The falsification
`ACCEPTANCE-TESTS.md` admitted it had never run: an unprimed agent, folder only, repo
unattached — **2/2 on the pre-declared criteria**, and it added three things the rubric
did not ask for, including the calibration trap (the sim bot cannot tune the bird in the
owner's band, so calibrate before tuning) and the folder's own basis limit (*"my actual
first read at HEAD is `docs/current-state.md`, and if it contradicts the above, the repo
wins"*). Full record: `docs/repos/ACCEPTANCE-TESTS.md` § Test 4.

**The route was tested on real owner utterances, not invented payloads.** 12 quotes
harvested from committed records, hand-labelled: **fires on the one it was written for,
0 false fires, 9 correct silences**, and 2 deliberate misses recorded as recall traded
for precision. Acceptance tests 1–3 re-run unchanged (test 3 still 6/6).

**A probe route cannot fire on a prompt, and the harness proved it mid-run.** One replay
case failed because *my label* was wrong: `adversarial-review` has no `tools` key, so it
inherits the probe set and is silent on `UserPromptSubmit` by construction — while the
same text in a `Grep` input fired it that same minute. The split is real and now
demonstrated rather than assumed.

## Error count — two axes, kept separate

**Axis 1 — incidents this session, catcher-attributed like the 16-incident baseline.**
This scores the *landed* mechanisms, not this session's changes.

| catcher | n | what |
|---|---|---|
| **owner** | 1 | dated the roadmap `2026-08-09` without checking; `date -u` says 08-08 — composed, not transcribed, in the provenance line of a document about provenance |
| **Codex (review)** | 1 | the allowlist entry suppressing one stamp finding under another's rationale |
| **local gate** | 2 | invented the `retriaged:` allowlist key (closed vocabulary); then writing two decision ids in prose **moved a finding's path** and unmatched the entry I had just fixed |
| **self, before cost** | 3 | a placeholder accidentally written into a live route's `says` (reverted next call); the mislabelled replay expectation; and the plan's claim that the program's NOW pointer misdirects — **refuted by reading the page before editing it** |
| **documentation recalled at the right moment** | 0 | unchanged from the baseline |

Seven incidents, none reaching `main`. The shape differs from the baseline in the way
the design predicts: the two costliest classes there (momentum-over-evidence, unread
descriptions) did not recur, and the gate caught what it is good at — closed
vocabularies and structural drift — within one command of the mistake.

**Axis 2 — orientation quality (what this session's changes can actually move).**
Boot-file probe 6/6 with correct first actions · Layer 2 unprimed probe 2/2 · route
replay 12 prompts, 0 false fires · acceptance tests 1–3 unchanged, test 4 new and
passing · boot file −31 words.

**Instrument telemetry, snapshotted because `/tmp` dies with the container** — recorded
as an **experiment**, not a permanent `session-close` step, per the promotion rule
(adopt only if ~3 sessions show the data is used): route fires this session —
`adversarial-review`, `github-api`, `openai`, `recording-a-wall`, `repo-spider-swing`
(+ `error-review` in replay); `read_before_write` read-set 83 paths, 2 reports, both
`[survived]`; owner-review log 1 line (`skip: reply-too-short`); `git_state_guard` no
fires; guard-fires delta +165 lines.

## Verification

Real exit codes, each command on its own — never `$?` after a pipe:

- `python3 bootstrap.py check --strict` → **exit 0** after the card flip (before it:
  exit 1, the born-red HOLD naming this card, verified against the CI job log rather
  than the advisory tail).
- `python3 tools/check_doc_routes.py --strict` → **exit 0**, 23 routes · 19 docs · 0 errors.
- `python3 tools/check_no_false_walls.py --strict` → **exit 0**, CLEAN across 5 docs.
- `python3 scripts/preflight.py` → exercised both ways; its FAILED line now names the
  failing leg, verified **live in CI** on the second run.
- Allowlist correction re-checked: still exactly 4 findings suppressed, nothing
  un-suppressed.

## Honest nulls

- **Phase 1 cannot move the baseline's failure classes** and is not claimed to. The
  landed injection mechanisms cover those; this session covers the orientation class.
  Axis 1 is n=1 against n=1 on a different task shape — directional, not proof.
- **Both probes were graded by the party that wrote the rubric**, on one run each. They
  show the surfaces can drive correct first moves; they do not establish a rate.
- **Route recall is deliberately poor.** Two real error-review-shaped phrasings in the
  corpus do not match, including the owner's own calibration sentence. Precision was
  bought with recall on purpose, and the misses are recorded rather than smoothed.
- **The session-id rotation across a usage-limit pause splits `/tmp` hook state**, so
  `read_before_write` fired once on a file this session had genuinely read. Counted as a
  false positive of the instrument, not a catch — and it means per-session hook counts
  undercount long sessions.
- **`MISSION.md` carries an era note, not a rewrite** — it is `binding`, so it changes by
  proposal; the note *is* the proposal and the owner has the last word.
- **The kit upgrade that would de-noise the check channel is scheduled, not done.** Every
  strict run still prints ~90 advisory lines, including known-false rows, into the exact
  channel this session argues must stay quiet.
