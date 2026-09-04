# 2026-09-04 — the SuperBot rebuild: a comparative product/architecture review of `superbot` and `superbot-next`, and the successor plan

> **Status:** `complete` — branch `claude/superbot-rebuild-review-20f9hq`.
> Born red on purpose, and all four conditions are met: the plan package is
> written (13 deliverables + index, plus `run/`), the bases were re-read against
> their launch SHAs (§ *The base re-read* below — both product pins unmoved),
> the external review round was answered (**one** Codex round, 13 findings, all
> 13 addressed at `d28d16a`, replied on the PR), and the gate is down to this
> hold alone. Flipping this line is the last act of the session.

- **📊 Model:** opus-5 · max · research + planning
  *(run as an ultracode fan-out — 24 evidence lanes + 6 adversarial challenges
  in one workflow, then 8 writing agents in a second; `ultracode` is the
  invocation, not an effort tier, which is what the card grammar caught.)*
- **📍 Venue:** cloud-container
- **🔗 Session:** [session_01AUDjqtyW5mkBPg9M2Yrgnr](https://claude.ai/code/session_01AUDjqtyW5mkBPg9M2Yrgnr) · "SuperBot rebuild design review"

**Previous-session review:** the last fleet-manager session (fm #1019,
`.sessions/2026-09-03-final-eap-mail-rewrite-after-reviews.md`) rewrote the
final EAP mail from the owner's own edits and ChatGPT Work's independent review,
and left E1 as the program's NOW pointer, drafted and staged, waiting on his
send. **Nothing in this session touches E1 or moves the NOW pointer.** This is a
parallel research track on the bots, requested directly; the program's step
ledger is not advanced by it.

**What this session is about:** a deep comparative review of `menno420/superbot`
(frozen, behind the live production bot) and `menno420/superbot-next` (the
parked ground-up rebuild), deep enough that the next rebuild is not another
translation exercise, another parity exercise, or an architecture designed from
assumptions. The deliverable is an evidence-backed plan package at
`docs/planning/2026-09-04-superbot-rebuild/`. **No implementation.** Both product
repositories, the production Railway worker, its Postgres and every Discord
surface are read-only by contract for this task.

**The direction it is built on** — the newest owner statement on the bots
(`docs/findings/2026-08-28-owner-intent-elicitation.md` § 1.15): `superbot` holds
*"too much history, too many trials and errors"*, `superbot-next` *"will have to
be remade aswell since the current build is nothing like the desired product"*,
and the end state is **one** bot, *"build right from the start"*, *"without
architectural debt"*, *"planned and connected from the start so it remains
manageable and able to grow indefinitely."* Plus OD-19's hard constraint: the
successor must be **cog-portable**, and the bots stay separated.

## What was done

*(in progress — this section is written as the work lands)*

- **Cold orientation** — the six mandatory reads in `README.md` order, then the
  three Layer-2 entry points (`superbot`, `superbot-next`, `spider-bot`), the
  2026-08-21 game-community plan and its `source-review.md`, the 2026-08-05
  live audit, and the owner-direction records through 2026-09-02. The
  2026-08-28 statement is the newest and it **supersedes** the plan's framing;
  the plan's own README already flags its unresolved internal contradiction.
- **Pins and census** — `superbot` `5e3a667b` · `superbot-next` `d5f66dc2` ·
  `spider-bot` `bf4d7527`, measured 2026-09-04T11:52:55Z. **Both product trees
  are at the exact pins the 2026-08-21 plan reviewed**; all 8 open `superbot`
  PRs are dependabot; the other two have none. Corpus census committed at
  `docs/planning/2026-09-04-superbot-rebuild/run/census.txt`.
- **`fleet-preflight` executed, not cited** — the full contract sheet at
  `run/CONTRACTS.md`. Concurrency **measured at 2** by demand test (6 probes at
  one instant, peak overlap 2, starts tracking slot-frees, provisioning 0.9 s
  within-wave) rather than quoted from the documented `min(16, CPUs−2)`. The
  survival rule is executable (`run/survival_rule.py`, exit 0): field audit 0
  unread with a **per-rule** REPORT_ONLY set, 4 fixtures die and 2 survive.
  A capture-literal instrument was built, self-tested (5/5 positives, 6/6
  negatives) and then **retired at 1/12 precision** after all 12 real-corpus
  hits were read by hand — the retirement is recorded as the finding.
- **Pilot** (2 agents, transcripts read whole) changed five things before the
  fleet committed, including cutting it 52 → 33 agents after the per-agent time
  estimate proved wrong by 2.6×. The two pilot agents **contradicted each other**
  and the contradiction was the run's best output, so every fleet prompt now
  carries an instruction to name contradictions rather than smooth them.
- **Twelve independent measurements** at `run/independent-findings.md`, kept
  separate from the fleet's rows. The sharpest:
  - `superbot-next`'s navigation-completeness golden — the suite its own
    docstring calls *"the golden proper"* — walks a panel registry that the
    suite's `autouse` conftest empties before every test. Green over the empty
    set, permanently; *"arms automatically as port bands register real panels"*
    cannot happen.
  - The `no kernel → domain` claim is **true** (0 module-level imports against
    234 the other way) and **unenforced** — none of the 27 `tools/check_*.py`
    is an import-direction guard, enumerated and read, with a positive control.
    `superbot` has that guard, in a required check.
  - `superbot` already contains the test pattern that would have caught the
    failure — `test_games_hub_view.py` instantiates the real view and asserts
    over `view.children` — applied to **2 of its 8** registered hubs.
  - **100 % of `superbot`'s runtime Python predates the EAP** (909 of 911
    files; 2 added during the fortnight) while **23 % of its docs were added
    inside those 14 days**. Its code debt is owner-era organic growth, not
    agent damage.
  - `superbot-next`'s plugin facet fence (`HOST_ONLY_FACETS = stores,
    data_invariants, wizard_sections`) makes **29 of its own 49 subsystems**
    ineligible to be out-of-tree plugins — precisely the class OD-19 wants
    portable.
  - The AI surface: a catalogue of **36** tools with one audited write became a
    registry of **8** BTD6 factual reads, zero writes, one registration site.
  - The audit's *"70 not-armed terminals across 17 subsystems"* **does not
    reproduce** against an `sb/` tree unchanged since 2026-07-19 (26
    occurrences, 22 files, 9 domain subsystems) — a failure to reproduce, not a
    refutation, and it makes `superbot-next` look better, not worse.
- **The review fleet** (33 agents: 12 map · 6 root-cause · 6 adversarial
  challenges · 6 refutation batches · 3 synthesis + 1 critic) — running.

## 💡 Session idea

**Every gate should have to declare its population, and the declaration should be
the thing CI reads.** Four times in this estate's committed record a green
instrument has run over a population smaller than, or a model of, the one it was
reported as covering — `superbot-next`'s navigation golden over a registry its own
fixture empties, its 533/533 goldens over captured bytes, `superbot`'s
help-reachability guard (and its mutation test) over a hand-built model of the hub
table, and `superbot-games`' substrate-gate over 73 of 121 collected tests. In
every case the assertion was correct and the population was wrong, and in every
case a single line — `assert len(population) >= FLOOR` beside the `assert ok`, with
FLOOR committed — would have failed on day one. The generalisable version is not a
test-writing tip: it is that **teeth are a property of the population, not of the
assertion**, so a checker framework should make the population a required, named,
committed input rather than an implicit consequence of where the check happens to
run. Candidate home: substrate-kit, as a checker-authoring rule with a
`declares_population` field the kit's own gate enforces on its own checkers first.

## Verify

```
cd docs/planning/2026-09-04-superbot-rebuild/run
python3 survival_rule.py                 # exit 0 — field audit + fixtures
python3 capture_literal_scan.py --selftest   # exit 0 — 5/5 positives, 6/6 negatives
cd /home/user/fleet-manager && python3 bootstrap.py check --strict
```

## Landed mid-session, and worth carrying

- **A merge-conflicted PR in this repo produces ZERO workflow runs, not a red
  one.** fm #1025 sat at `mergeable_state: dirty` for ~15 minutes after #1022/
  #1023/#1024 merged, and `GET /actions/runs?branch=…` returned `total_count: 0`
  throughout — no queued run, no failed run. `substrate-gate` fires on
  `pull_request`, which needs `refs/pull/N/merge`, and a conflicted PR has none.
  Positive control: `claude/fleet-manager-substrate-kit-jejk7x` had three
  successful `pull_request` runs in the same window; the actor hypothesis was
  refuted (all three open PRs opened by the same user). **So "CI never started"
  on a fleet-manager PR is a merge-conflict signal, not an Actions outage.**
  Resolving the conflict started both workflows within seconds. → `CAPABILITIES.md`
  at close.
- **`.substrate/guard-fires.jsonl` conflicts resolve as a UNION**, never by
  taking a side: it is append-only telemetry and either side's `--theirs`/`--ours`
  silently discards another session's records. Base 41,965 + main's additions +
  this session's appends, deduplicated in that order = 42,264.
- **Codex commented on fm #1025 unprompted, ~3 minutes after PR open**, with no
  `@codex review` from this session. It made no changes, correctly read the
  born-red state, and independently ran all three verify commands green. That
  **contradicts** `.claude/CLAUDE.md`'s current record that the automatic
  triggers are off and *"the comment is the only trigger"* — one observation, not
  a refutation of his 2026-09-02 statement, and it is logged here rather than
  edited into the boot file by a session that saw it once.
- **A one-shot check-in is armed** (`trig_011kkDbokoPHAuTVGg7uumoc`, fires
  2026-09-04T14:00Z) to re-check #1025, the fleet's journal, and whether #1021
  merged. **Do not delete it** ([D-0015]); a fired one-shot is inert. Disable
  with `update_trigger enabled:false` if it ever misbehaves.

## The base re-read — § BASE discharged, 2026-09-04T17:1xZ

Run immediately before publication, against live `main` on all four repos via
the direct-PAT path:

| repo | launch pin | live `main` at re-read | moved? |
|---|---|---|---|
| `superbot` | `5e3a667b` | `5e3a667b` (2026-08-20T23:17:52Z) | **no** |
| `superbot-next` | `d5f66dc2` | `d5f66dc2` (2026-08-13T15:21:11Z) | **no** |
| `spider-bot` | `bf4d7527` | `bf4d7527` (2026-08-25T22:42:55Z) | **no** |
| `fleet-manager` | — | `2561874` | **yes — merged in** |

**Both product pins are still the live head of `main`**, so every measurement in
the plan package is against current truth rather than a stale snapshot. That is
worth stating because a review of two parked repositories could easily have been
overtaken and never noticed.

`fleet-manager` moved four commits, and one of them mattered: **#1021 merged**
(`104c2e5`), so the owner statement this session caught mid-run is no longer in
flight — it is stamped in `docs/decisions.md`. Checked on the way in: **the text
that landed is the text this session recorded**, so nothing the plan package
built on it needs revising. `run/in-flight-direction.md`'s standing action is
discharged in that file.

## The external review round — one round of three, answered

Requested 17:09:08Z on head `c6b1790`; answered 17:20 with **13 inline
findings** (6 P1, 7 P2). Every one was verified against source before acting;
all 13 were addressed at `d28d16a` and answered on the PR. **No second round
requested** — the cadence reserves them, and nothing in the reply is a question
back.

**Three changed a conclusion rather than a wording, and the first is the
session's most important single correction:**

1. **The population contract was an instance of the defect it prescribes
   against.** § 1 of `08-verification.md` said `assert len(population) >= FLOOR`
   with `FLOOR = 250` — which, against the measured 314 panels, passes while 64
   panels vanish, and which a 250-entry hand-built model satisfies identically
   because `POPULATION` was only prose. A lower bound is not an identity check.
   The contract now commits an `EXPECTED` set **derived independently of the
   walker it checks** and asserts equality in both directions. **The section
   proposing the cure had the disease** — which is precisely how this defect
   survives in careful repositories, and it is now written into the package as
   its own worked example.
2. **I-19 overclaimed.** `enabled=False` proves this composition root publishes
   no new command set; it does not prove the audit's *"27 slash commands
   survive"* wrong, because an application retains what an earlier sync
   registered. Narrowed, the honest null restored, four downstream sites
   corrected including this repo's `superbot-next` entry point.
3. **I-9 did not measure what it concluded.** `--diff-filter=A` is blind to
   modification. Rather than weaken the claim I ran the churn measurement it
   needed — 10 of 883 runtime files touched, +418/−2 in the EAP window — so the
   conclusion now rests on evidence that carries it.

**What the round says about the fleet — corrected, because the first version of
this paragraph was unfair to the fleet in a way that flattered the diagnosis.**
It said 24 lanes and 6 adversarial challenges "did not find any of these three."
They could not have. **Every lane was pointed at the two product repositories,
and the challenge lanes finished between 15:36 and 16:10 — before most of the
package existed**; only 2 of the 34 agent transcripts mention `08-verification`
or `FLOOR` at all. A reviewer never shown the artifact has not missed a defect
in it.

**The accurate statement is narrower and worse.** Codex was the *only* reader of
the written package, because **this session designed a 34-agent fleet to audit
two repositories and no stage at all to audit its own output.** The comparison
is not between two reviewers; it is between "reviewed" and "never asked". The
lesson survives with its reason replaced: not *a fan-out cannot self-critique*
— untested — but **a fan-out reviews exactly what you point it at, and pointing
it at the sources while the conclusions go unreviewed is a population choice,
made by the person who wrote the contract sheet.** That is I-15's shape one
level up: the instrument was fine and its population was wrong.

**For the next fan-out:** a synthesis-critic lane over the written deliverables,
run before the external round, is the missing stage — and `run/CONTRACTS.md`'s
AGGREGATE section is where it should have been declared.
