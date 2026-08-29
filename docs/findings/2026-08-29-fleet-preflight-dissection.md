# The fleet-preflight dissection — keep, fix, trim, lift

> **Status:** `reference` · 2026-08-29 · **plan input under OD-26 §13 — nothing
> here is built, and the skill file is not edited.** The owner's ask, verbatim:
> *"dissect it to find out if it can be improved further, and if we can take
> certain parts of it and use for other skills."*
>
> Object: [`.claude/skills/fleet-preflight/SKILL.md`](../../.claude/skills/fleet-preflight/SKILL.md)
> — 429 lines at `8fc3cc7`, in the boot-file routing table and the installed
> roster ([`docs/SKILLS-local.md`](../SKILLS-local.md)), **never yet run**.
> Evidence base: the skill read whole; its two source records
> ([the audit](2026-08-29-estate-agent-error-audit.md),
> [the retrospective](2026-08-29-fleet-orchestration-retrospective.md)) read
> whole; the parallel
> [skill-and-rule reuse map](2026-08-28-skill-and-rule-reuse-map.md) read whole;
> the fm #973 catalogue measured directly at `731c282` and re-verified after
> #973 merged (`ac5de6a`): its round-2 fixes restructured the coverage field
> (adding `already_covered_positive` / `already_covered_answers`) and every
> stat quoted here re-derives identically on the merged rows. Certainty tags per
> [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md);
> everything not marked `MEASURED` in this file is `REASONED` — a dissection is
> a judgement and says so.

## 0 · The verdict in one paragraph

The skill is the retrospective's six failures made operational — each section
carries a runnable check, a contract line, and a named blind spot, and it
gates nothing, which keeps it inside OD-26 §2 (*never block*) by construction.
Its content is right in the places that were measured hardest (§1's field
audit, §7's demand test). Its two structural weaknesses are not prose defects
and cannot be edited away: **it has only ever been validated backwards**
against the one run that produced it (seven sections mapping one-to-one onto
one run's six failures is what overfitting looks like when it is honest), and
**it lives in the container whose use the estate's own parallel audit found it
cannot count** — a skill invocation *need not* leave a record (46 recorded
invocations exist; what is missing is exhaustive telemetry, so no rate is
derivable in either direction), and this skill ships with no route, by its own
admission unfinished under the trap lifecycle (`SKILL.md:400-405`). Both are settled the same way: **run it once, for real,
and route it when the revised plan allows.** Until then, edits are guesses —
which is why this dissection names fixes and lifts rather than applying them.

## 1 · What is right and stays

- **The contract sheet as the output** (`SKILL.md:25-38`): preparation becomes
  a committed artifact quoted in the published finding, so skipping a check is
  priced (`UNCONTRACTED — <reason>`) instead of discovered by a reviewer. This
  is the estate's verbatim-evidence discipline applied to fan-out prep.
- **Nothing gates.** Written after the sitting, and compliant with OD-26 §2's
  *never block, guarantee pickup* by design rather than by accident.
- **Ordering by catch-per-second** (`SKILL.md:41-43`), with "if you read one
  section, read §1" said out loud.
- **§1 whole** — the field audit's `UNREAD`/`UNDEFINED` twins, the fixture
  rule that at least one case must die **and** at least one must survive, and
  the lens-authority check (*N−1 confirmers and a mascot*). This is the
  815-of-925 defect and the 2-vs-1 outvoting caught at the only cheap moment.
  The catalogue independently corroborates the fixture rule: *"Land a guard,
  test or checker that has never been seen red"* spans **10 repositories** in
  the #973 data.
- **§2's two instrument rules** — one positive per alternative, and print the
  compiled pattern — both derived from the actual `re.X` defect, plus the
  real-slice hits read by hand (TRAP-003's positive control).
- **§7's concurrency method** — the demand test with the barrier, the
  slot-limited vs provisioning-limited signature table, and the
  first-timestamp assumption check. The deepest measured content in the file;
  three separate `MEASURED` blocks stand behind it.
- **Every section names what it does NOT catch**, and the closing limits
  section names the skill's own missing route. That discipline is rarer than
  the checks themselves and is the main reason this file can be trusted while
  untested.

## 2 · What to fix — three defects this read found

Named, not applied: the standing decision is no edits before first real use,
and none of these is dangerous enough to overturn that.

**F1 — the §1 example predicate misreads negative coverage answers.**
`SKILL.md:70` teaches `RULE = "refuted or (already_covered_by and
lens_refuters >= 1)"`. In the real data the coverage field is
**string-valued and required**, so a lens that answers *"none"* or *"new"*
still populates it — and a truthiness test reads that negative answer as
coverage. This is exactly the class Codex round 2 caught in the #973 data
README the same evening (*field population ≠ positive coverage*), sitting in
the skill's own teaching example. Fix shape at first-use edit: the example
must test positive coverage explicitly (a structured null, or an explicit
negative-token screen), and §1a could add one line telling the reader to
fixture tri-state string fields the way §2 fixtures the instrument.
`MEASURED` on the catalogue directly, 2026-08-29: a prefix classification over
all 284 rows puts **93 at none-style answers** (leading "none"/"nothing"/"new")
against 191 positive-style. After #973's round-2 fix merged, the rows carry an
authoritative per-row label — `already_covered_positive` is **false on 51** —
and the 42-row gap between that and my cruder cut is itself instructive: those
are *"nothing fully — but adjacent-X partially covers…"* answers, which no
string test classifies reliably in either direction. **The measured effect on
this catalogue is small, and saying so is part of the claim** (Codex #978 R1):
the example's misreading branch fires only when `lens_refuters >= 1` as well,
and of the negatives only **2 of 51** (authoritative) / **3 of 93** (prefix
cut) carry a refuter — so the full predicate misclassifies 2–3 rows here, not
a third of the set. The defect is type-safety, not blast radius: the next
corpus need not be so lucky, and the merged data's boolean is exactly the fix
shape the example should teach.

**F2 — §6's state-check snippet is unexercised in its venue, not shown
unsuitable** *(narrowed on Codex #978 R1, which correctly refused the stronger
form)*. `SKILL.md:230-237` inventories open PRs with `gh pr list`. The first
cut of this finding called that a venue mismatch; the estate's own surface
record says otherwise — `docs/execution-surfaces.md:43`: the `gh` CLI is
*"installed by `setup-base.sh` Block 2b"*, and the binary is present in this
container (`MEASURED`: `/usr/bin/gh`, 2026-08-29). What stands is narrower and
still real: **no run of that snippet exists** — this session could not supply
one because its own harness policy routes all GitHub work to the MCP tools,
and that policy variance across session classes is itself the reason the
snippet should not be the only path. **And round 2 found the snippet carries
an actual defect no venue can save** (`MEASURED`, reproduced this session):
when `$REPOS` holds path-shaped entries — `projects/superbot`, any absolute
path — the redirect `> ".launch-sha.$r"` embeds the slashes in the filename
and fails with *No such file or directory*, so the later `cat` never recovers
the launch SHA and the scheduled re-read silently loses its baseline. Fix
shape: sanitize the identifier (`${r//\//-}`) or write the SHA inside each
repo; verify the `gh` half at the skill's first real use; and put the
estate-native listing (MCP or direct-PAT) beside it for the sessions whose
policy forbids `gh`. The `--limit is a maximum, not a page size` warning is
right and travels with whichever form.

**F3 — the file breaks its own no-restating promise, and that debt has already
cost one near-miss.** `SKILL.md:15-17` says it *"cites those numbers rather
than restating the record"*; §§1 and 7 then restate the verdict tallies and
three `MEASURED` narrative blocks at length. `MEASURED` by wide grep,
2026-08-29 (a first, pattern-narrow grep undercounted at three — Codex #978 R1
caught it): the 815-of-925 figure stands in **six** committed surfaces besides
this file — the retrospective, the findings index row, the skill, the
archived workflow `03-judge-panel-skill-design.js`, the panel output JSON, and
the retrospective's session card. No copy has yet diverged; the related
near-miss the #973 card records (155/122/7 against the measured 226/51/7) was
a tally **extrapolated from a subset and caught before commit**, not a stale
copy — what it evidences is numbers being retyped from memory, which is the
habit six standing copies invite. This
is the audit's proposed TRAP-008 class (*a correction that leaves its own
copies standing*) pre-registered against our own instructional surface. The
fix is §3's trim, not a hotfix.

## 3 · What to trim — later, and the trigger is named

The standing decision holds: **trim after one real use, not before** — cutting
an untested instrument is cutting on a guess. When the first real fan-out has
used the sheet, the trim targets are already identifiable:

- §7's three `MEASURED` narrative blocks (`SKILL.md:332-337, 348-351,
  355-360`) → keep the signature table and the one-line assumption result,
  cite the retrospective for the rest.
- §1's restated verdict tallies → one line citing retrospective §3.
- The per-section *"Catches failure N / does NOT catch"* footnotes → one
  closing coverage table. This is the judge panel's own usability suggestion
  (`data/workflows/skill-design-panel-output.json`: the footnotes are
  *"coverage notes addressed to a reviewer of the skill, not to the session
  using it"*, measured at ~15 % of the body) — the honesty they carry survives
  intact in table form.
- Expected landing size ~300 lines with no check removed — the cuts are
  evidence prose, never the runnable checks or the contract lines.

## 4 · What to add — candidates, each waiting on first use

- **A `DEDUP`/precision contract line.** The audit's §7 names *"no
  deduplication was performed across cards"* among its heaviest limits, and no
  contract on the sheet covers output precision — §4 contracts the input
  corpus and §1 the decision rule, but nothing asks how double-counted the
  published rows are. Candidate: `DEDUP: <method over output rows> ·
  precision spot-check <n>/<n> read by hand`.
- **Make the `PILOT` line carry the number the run will be judged by.**
  Stated precisely, because the first cut of this bullet promoted a
  counterfactual to history (Codex #978 R1): the committed evidence holds only
  the **final** aggregate — 7.0 % across all 925 verdicts — and the only
  first-batch statement anywhere is a judge's *"would have exposed the 7.0 %
  refute rate at 10 % of the spend"*. No batch-level tally exists. So the
  candidate line names the metric a pilot **should estimate**, not one that
  was ever read: `PILOT: … · metrics read: <the rates the full run will be
  judged by>`. The shipped skill's own §3 sentence (*"was knowable from the
  first batch … read only afterwards"*) rests on the same absent tally and
  should be rephrased at the same trim.
- **The hour after launch.** The skill stops at launch by design
  (`SKILL.md:425-429`); the close-time sibling — a check that a session which
  ran a fleet committed something pointing at the fleet's output — is already
  captured as the #973 card's 💡 and is **held with mechanisms under OD-26
  §14**. Cross-reference it when the plan reaches it; nothing to do now.

## 5 · The liftable parts, per target skill

The owner's second half: which parts other skills should inherit. Lifting is
itself an edit to those skills — post-plan records work — so this table is the
map, not the diff.

| part (where it lives in fleet-preflight) | lift into | what it does there |
|---|---|---|
| The census-caption rule — *composition in the same breath as the count; copy the caption, do not compose one* (§4) | `delegate-read` — **prose + tool work** | The input-side contract for every corpus handed to Gemini. Not liftable by skill text alone (Codex #978 R1): `tools/gemini_delegate.py:455-460` prints only file/char/token totals, so the bundler must first learn to emit the composition caption the rule makes authoritative. |
| The retention fields — repo + `source_path` + sha/id + verbatim span + the instrument that selected it (§5) | `delegate-read` — **prose + tool work** | Same dependency: the report `_meta` (`gemini_delegate.py:481-488`) records model/files/batches/usage/globs and none of these fields; the lift is skill prose plus the report-schema extension, or it instructs callers to retain what the tool never emits. |
| The `--limit is a maximum, not a page size` truncation lesson, and the per-repo launch-SHA capture pattern (§6) | `prompt-preflight` | Both are prompt-time material: the truncation warning generalizes to every listing API, and the launch-SHA loop is the multi-repo form of its §1. **The scheduled post-run re-read stays in fleet-preflight** — the skill marks it "belong here and only here", and it must run after the fleet, a moment `prompt-preflight` structurally never sees (Codex #978 R1 refused the original whole-row lift on exactly this). |
| The demand test with barrier, the slot-vs-provisioning discriminator, and the first-timestamp check (§7) | `capability-probe` | These ARE capability probes — *name the method, not just the number* is that skill's whole doctrine applied to concurrency. One cross-reference row each way; teach it once. |
| The `UNCONTRACTED` grammar — a skipped check travels with the deliverable, priced (`SKILL.md:38-39`) | `implementation-prompt` · `continuation-prompt` | A standard section: name the checks the prompt deliberately does not require, so the cost of skipping rides the handoff instead of surfacing in review. |
| Pilot a slice you can read whole, then commit the rest (§3) | `implementation-prompt` | For any prompt that commissions batched or repetitive work, not only fan-outs. |

And one lift in the reverse direction: once `capability-probe` carries the
probe mechanics, fleet-preflight §7 should cite it rather than teach the
method twice — the same de-duplication §3 applies to evidence.

## 6 · The container tension, stated rather than smoothed

The [reuse map](2026-08-28-skill-and-rule-reuse-map.md) §1 measured that the
estate has **no exhaustive skill-invocation telemetry** and concluded *"do not
write new skills as the primary vehicle"* — and fleet-preflight is a new
429-line skill. The tension is real and it resolves narrowly, not generally:

- fleet-manager is the one repository where a skill CAN bind — the routing
  table row exists in the boot file, and fan-outs launch from here;
- the sheet is a committed artifact, so **contract-conformance leaves a
  record** — stated at that width and no wider (Codex #978 R1 refused the
  wider form): a published fan-out finding with no quoted sheet proves the
  output contract was not followed, **not** that the skill never loaded — a
  session can invoke it and still omit the artifact, so invocation itself
  stays exactly as unmeasurable as the reuse map says. What the sheet buys is
  a checkable conformance signal most skills lack; the observability gap it
  cannot close is the reuse map's point, intact;
- the skill is owner-directed in his own words (*"not a skill that tells you
  how to start an ultracode… but to do the proper preparation in order to
  start a well organized fleet"*), which settles the should-it-exist question
  without settling the does-it-work one.

What settles the rest: the missing route (post-plan, per §14) and the first
sheet from a real run. Until both exist, the reuse map's warning stands as the
null hypothesis about this skill, and the skill's job is to refute it.

## 7 · OD-26 compliance, checked deliberately

- **§2 never block** — nothing gates, including the sheet itself. ✓
- **§7 / §14** — this dissection builds nothing, registers nothing, edits no
  file but itself; the skill it examines was owner-directed. The route it
  names as missing is a mechanism and **waits**. ✓
- **§20's test** — *does it stop something being re-derived?* Yes, directly:
  the skill exists so the next fan-out does not re-derive the six lessons at
  fleet price. It is the retrospective's knowledge routed to the moment of
  action, which is the fix family his own §20 ranks first. ✓

## 8 · Acceptance — what would make this skill trusted

It has never run, and its current validation is retrospective — *would it have
caught what already happened* — the weakest footing an instrument can have,
because the six failures it catches are the six that were caught. §3's pilot
is the only section aimed at unknowns. Two experiments are ready when wanted,
neither run in this session (both are execution, and stage one is mapping):

1. **First real use.** The next fm fan-out fills the sheet for real. That one
   run prices the §3 trim, tests F1's fix, and produces the first committed
   contract sheet — no `CONTRACTS.md` exists anywhere yet, and its first
   instance is the artifact that answers the reuse map's objection.
2. **The bad-draft probe** (from the round's open list): judge one
   deliberately broken draft with the committed panel's three lenses. All
   three real drafts scored USABLE or better, so the panel has never been
   seen to reject — the same never-seen-red defect §1b guards against, one
   layer up. Priced honestly (round 2 corrected the first cut's "three
   agents"): run surgically — the one bad draft under the three judge lenses
   — it is 3 agents; re-running the committed workflow as-is is **13** (three
   drafting lanes, three judges per draft, one synthesis). The surgical form
   answers the question.

## 9 · The round's records against each other — the reconciliation that was owed

The reuse map and the error audit ran in parallel and were never checked
against each other. Done here, read-whole on both sides:

**They agree on the diagnosis, from independent instruments.** The delivery
gap is measured three separate ways: the audit's §2/§4 (328 prose-only rules
against 172 mechanical enforcers; 1 of 20 repos with any routing layer; the
kit's four-event channel present in 18 of 20), the reuse map's §5 (71 routes
covering conventions and **zero** covering the four rule surfaces; the trap
lifecycle run to completion for 7 execution mistakes and 0 rules), and the
standing 2026-08-08 measurement stated with its denominator and limit — 116
verify-first statements across 66 files caught **0 of the 16 incidents
observed in that one session**, and its own "Honest limit" says prevented
errors are invisible, so it bounds the marginal value of a 117th statement,
not the worth of the 116 *(restored on Codex #978 R1; the first cut's "116
statements, 0 catches" dropped both)*. Same direction, no shared instrument.

**They agree on the sharpest single fact of the round: proposals duplicate
existing coverage.** The reuse map's §7: in **17 of 17** refutations the
citation held and the verdict fell — *duplicate proposed as new*. The
catalogue: all 7 killed rows died as already-covered. **The two grains must
not be conflated, and a first cut of this paragraph conflated them (Codex
#978 R1, P1):** the *duplicate-proposal* claim rests on the 17/17 and the 7
killed rows — cases where named existing coverage was the verdict. The
row-level labeling (`already_covered_positive` true on 233 of 284) supports
only the weaker claim that **coverage signal was collected and ignored**:
positive means a lens named at least one real covering mechanism, and on
**111 of the 233** at least one answer begins *"partial"* (37 where the first
answer does — the wider predicate is the one measured, stated as such after
round 2 caught this sentence attributing the 111 to the narrower one, the
field-reading error class a third time) — partial coverage is
not duplication, and treating 233 as duplicates would push the revised plan
toward rejecting genuinely additive work. (At verdict level, 815 of 925 named
something — retrospective §3 — with the same partial-inclusive caveat.) And
OD-26 §20 is the owner saying the duplicate half in his own words — *"redoing
the same things over and over"*. The convergence, stated at its supported
width: **where proposals failed, they overwhelmingly failed as re-proposals
of existing coverage, and the coverage signal that would have caught them was
collected and unread — so the revised plan should start from inventory, not
from candidate lists.**

**A third alignment, held at hypothesis grade** *(downgraded from "agreement"
on Codex #978 R1)*: the reuse map argues *prefer gates and checkers over
skills* (§1, §6 Move B) from delivery-observability evidence, and the
catalogue's fix-family distribution prescribes `checker` on 166 of 284 rows
against `skill` on 20. But those labels are synthesis-lane prescriptions
emitted under one shared schema on candidate rows the README itself says
survived almost nothing — a direction-aligned, unvalidated prescription
space, not an independent vote. It corroborates nothing; it merely fails to
disagree.

**Two tensions, neither a contradiction:**

1. **Where routing ranks as a fix.** The reuse map's Move C (route the
   rulebook) scored *"partly"* on §20's re-derivation test — routes deliver a
   rule but do not preserve a session's finding — while the audit's §9 makes
   routing-into-the-kit-channel its headline plan input. Different objects:
   fm-internal routes to rule surfaces versus estate-scale delivery of the
   whole hook layer. Both records bound themselves correctly, and both defer
   to the revised plan; the plan settles the rank, with the audit's own
   heuristic lower-bound measurement (§9) as the gate.
2. **The skill container** — §6 above. The map's warning stands as the null
   hypothesis; fleet-preflight's first real run is the experiment against it.
