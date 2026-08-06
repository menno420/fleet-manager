# The kit's checkers, classified — and what the gate output was actually doing

> **Status:** `reference`
>
> Written 2026-08-06 by the foundation-verification session, before any bot
> rebuild work. It answers § 3 and § 5 of
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md)
> and uses that document's certainty legend — read it first if you have not.
>
> The code half is substrate-kit PR #577.

## 0 · The orientation answers, from the repos' own docs

The handoff set an orientation test. Answering it from source rather than
from any doc's summary of source:

- **What substrate-kit is.** A single-file, stdlib-only agent substrate that
  a repo *adopts*: it plants a doc set, a control protocol, a session-card
  ritual and a CI gate, then keeps them honest. `src/engine/` is the source
  of truth; `dist/bootstrap.py` is generated from it by
  `src/build_bootstrap.py` and byte-pinned by CI; templates in
  `src/engine/templates/` render into planted docs. Adopters vendor only the
  built `bootstrap.py`.
- **Live version.** `1.20.2` (`substrate.config.json` → `kit_version`), main
  at `61278b3`. fleet-manager still vendors `1.20.1`.
- **What the gate actually enforces.** ONE required check, `kit-quality`
  (verified from the rulesets API, not owner-reported). Inside it, exit-affecting:
  the doc checks, the decisions ledger + stamp discipline, the namespace guard,
  the seam fences, the orientation budget, the false-wall leg, the engagement
  gate, the control heartbeat's *static* half, the inbox append-only gate, and
  the session-card gate. `guards.py` pins that surface four ways — 18 `ci.yml`
  steps, 6 workflow jobs, 7 `check --strict` sub-checks, 4 lifecycle hooks.
- **Mechanism vs prose.** This is the part worth the section below.

## 1 · The measurement `MEASURED`

`check --strict` run at HEAD on both trees. Both exited **0**.

| tree | total output lines | advisory ("never exit-affecting") | share |
|---|---|---|---|
| substrate-kit @ `61278b3` | 47 | 41 | **87%** |
| fleet-manager @ `c19ae90` | 89 | 80 | **90%** |

Tag breakdown, fleet-manager: `stale-wall` ×33, `capability-entry-stale` ×22,
`dateless-wall` ×12, `skill-ground-unresolved` ×9.

The composition matters more than the count:

- **13 of the 33 stale-wall rows are titled `'any'`**, and four more
  `'autonomous-project'`. The row extractor is mis-parsing, so even the
  *subject* of the warning is unreliable.
- **All nine skill-grounds rows are false.** They name `READ FIRST`,
  `verify <out.json>` and `r = np.minimum(r, np.maximum(g, b))` as commands
  that "resolve to no whitelisted executable". They are prose and a numpy
  expression.
- Many `capability-entry-stale` rows are byte-identical repeats.
- **No deterministic structural checker fired on either tree.**

So the channel an agent reads to decide whether it is done ran at roughly
**1:9 signal to noise, and the noise was wrong**.

`REASONED`: this is Goodhart's law pointed at a feedback loop, and it is not
neutral. An agent's default response to a warning is to try to fix it — the
reviewer's own objection in § 5 of the continuation doc. A large, permanent
field of false warnings therefore does not merely waste attention; it
actively recruits effort toward hallucinated repairs, in the one place an
agent looks for its verdict.

The concrete cost was visible immediately. On substrate-kit the single line
that mattered — `HOLD (by design): the born-red session gate is holding this
red … nothing to investigate` — sat buried under 41 lines of advisory. After
routing it is line 5 of 7.

## 2 · Mechanism vs prose — the honest count

The kit's rules divide three ways, not two.

| Tier | Count | What it means |
|---|---|---|
| **Exit-affecting** | 7 strict sub-checks + the doc/session/inbox/heartbeat gates | A finding reds the one required check. Real mechanism. |
| **Runs, never exit-affecting** | 29 advisory emit sites | Real code, real findings, zero consequence. |
| **Prose only** | the CONSTITUTION / PL-register rules | No checker at all. |

The middle tier is the interesting one and it was invisible as a tier: each
of the 29 sites was hand-wired with its own `posture="advisory"` seam and its
own print block, and nothing named the set. That is why nobody noticed it had
grown to 87–90% of the output.

## 3 · The classification `REASONED`, mechanised

Every one of the 29 sites is now classified in
`guards.ADVISORY_CENSUS`, with its reason, pinned by
`tests/test_advisory_census.py` asserting bidirectional set-equality against
the live call sites. **A checker can no longer ship unclassified**, and a
census entry cannot outlive the block it describes.

The axis is *deterministic vs heuristic* — not the *advisory vs blocking*
axis the code already had. They are different questions: the first is what a
checker IS, the second is how it happens to be wired.

**DETERMINISTIC (8)** — a structural disagreement between two committed
surfaces, or a reference that does not resolve. Binary, no judgement, no
prose matching. These stay in the agent's channel:
`staged_regen` · `template_sync` · `automerge_preflight` ·
`enforcement_strength` · `folded_gate` · `fastlane_symmetry` ·
`recipe_applies_when` · `baton_resolves`

**HEURISTIC (21)** — an ager, a counter, or an inference over prose;
false-positive-capable by construction. These leave the channel:
`status`(staleness half) · `adopters`(staleness half) · `owner_actions` ·
`claims` · `capability_xref` · `setup_script` · `skill_grounds` ·
`archive_ready` · `card_residue` · `seat_digest` · `orientation_headroom` ·
`model_line` · `outbox` · `stale_walls` · `dateless_walls` ·
`claim_provenance` · `wall_ledger_agreement` ·
`recipe_signature_honesty` · `recipe_discovery` · `ungroomed_ideas` ·
`baton_freshness`

The kit's own vocabulary did most of the work: the modules that classify as
heuristic are the ones whose docstrings already say *coarse*, *heuristic*,
*token-overlap*, *nudge*, or carry an `UNVERIFIED` provenance header. The
classification largely reads what the authors already knew and never wrote
down in one place.

**The validation.** All eight tags observed firing on real trees are
heuristic. So the routing removes 100% of the observed noise and loses zero
deterministic signal — and that fact is itself pinned by a test, so a future
reclassification that reopens the noise field turns red.

Result: **47 → 7 lines** on substrate-kit, **89 → 10** on fleet-manager, exit
codes unchanged. Nothing is deleted — `check --advisories` prints the full
tail, and guard fires are recorded for both classes exactly as before, so
only stdout moves and no exit code can change.

## 4 · What was deliberately NOT done, and why `REASONED`

The handoff's DONE WHEN asked for the deterministic checkers to be *wired to
the gate*. They are classified and the routing is built; **the promotion to
exit-affecting is not made here.**

The evidence for it is two repos. The kit ships to ~22 adopters on mixed
versions, and a promoted checker reds every one of them on their next
upgrade. The kit's own code already reasons about exactly this: the call site
for `check_fastlane_symmetry` says a required-check red there "would be a
fleet bomb during version skew". Flipping eight checkers to hard-red across
the fleet on two trees' worth of evidence would be the same
unverified-autonomous-change pattern this whole foundation review exists to
correct — and it would be that pattern committed *by the review*.

So the promotion becomes a measurement instead. `check --gate-preview`
reports, for any tree, exactly which deterministic sites carry findings and
would therefore red. Run it across the adopters, then promote on the answer.

`MEASURED`: it reports **0 sites carrying findings on both substrate-kit and
fleet-manager** — so on the two trees that can be tested, the promotion is
free today. That is a real result and it is also only 2 of ~22.

**The next slice is that sweep**, not more classification.

## 5 · The boot-path audit `MEASURED`

Both repos' declared read paths checked file by file against their trees.

**fleet-manager** — all 25 files its `.claude/CLAUDE.md` names resolve. But
it *omits*
[`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md),
the document that calls itself the one that "supersedes everything else about
what to do next". Nothing references it: not `CLAUDE.md`, `current-state.md`,
the consolidation program, `PROJECT-CLOSEOUT.md`, or `NEXT-TASKS.md`. It was
reachable only by being handed a prompt that named it — the same failure that
cost 2026-08-05 a day, one document later, in a boot path edited that same
day to fix the previous instance. Now added to the read path.

**substrate-kit** — had **no working boot read path at all**. Its rendered
`docs/AGENT_ORIENTATION.md` opened with "1. `.claude/CLAUDE.md` — the working
agreement"; the kit by design never installs `.claude/` into its own tree (it
stages it at `.substrate/claude/` for a host, and the source-layout guardrail
refuses writes to the kit's tree). `orientation.boot_docs` was `[]`. And
`CONSTITUTION.md` — which `render.agreement_home` correctly resolves to —
carried no boot list to point at. Fixed in substrate-kit's own
`docs/decisions.md` (its ledger, not this repo's).

The sharp part: that dead pointer was diagnosed and fixed **in the template**
on 2026-07-12. `render.agreement_home`'s docstring records it as "a dead boot
pointer verified live in 3/3 adopters (inbox ORDER 015)". The kit shipped the
fix to its adopters and never re-rendered its own copy — consumer #0 kept the
bug it had already patched for everyone else. That is the generated-artifact
drift class the kit exists to catch, landing on the kit itself, undetected
for 25 days.

## 6 · Record corrections `MEASURED`

- **superbot-next #602 was already merged** (2026-08-05T23:05:49Z), after the
  handoff naming it "your first step" was written. Its two false-wall lines
  are fixed on `main`; the repo has 0 open PRs. The estate had zero
  outstanding items on arrival.
- **"substrate-kit and fleet-manager have ZERO required status checks" is
  half stale.** From the rulesets API: true for fleet-manager (no
  `required_status_checks` rule), **false for substrate-kit**, which requires
  `kit-quality` — the P10 swap its own `WORKFLOW_JOB_CENSUS` anticipated.
  Not academic: the enabler armed auto-merge on PR #577 within a minute of it
  opening, and `kit-quality` being required is the only reason a born-red PR
  did not land unfinished.

## 7 · Honest nulls

- **The promotion is unmeasured beyond 2 repos** (§ 4). `--gate-preview`
  exists to close that; it has not been run fleet-wide.
- **Whether removing the heuristic tail is safe remains `UNVERIFIED` in one
  direction.** It was reasoned in the continuation doc and is now measured
  for *volume* and *falsity*, but "a session might legitimately have wanted
  that signal" cannot be measured from inside the session that removed it.
  The mitigation is that nothing is deleted: `--advisories` and the guard-fire
  ledger both still hold every finding.
- **The 21 heuristic checkers were classified, not repaired.** The
  `'any'`-titled stale-wall rows and the `READ FIRST` skill-grounds rows are
  real bugs in those checkers; this session moved them out of the gate channel
  rather than fixing their extractors. Off the channel they are cheap to leave
  broken, which is also how they stay broken.
- **No superbot-next code was read.** Out of scope by the handoff.
