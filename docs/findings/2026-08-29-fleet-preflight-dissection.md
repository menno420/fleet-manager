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
**it lives in the one container the estate's own parallel audit says it cannot
measure** — a skill invocation leaves no record, and this skill ships with no
route, by its own admission unfinished under the trap lifecycle
(`SKILL.md:400-405`). Both are settled the same way: **run it once, for real,
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
string test classifies reliably in either direction. Whichever number you
take, the example predicate misreads them as coverage, and the merged data's
boolean is exactly the fix shape the example should teach.

**F2 — §6's state-check snippet is `gh`-shaped, and the fan-out venue here is
not.** `SKILL.md:230-237` inventories open PRs with `gh pr list`. In this
estate's remote containers GitHub work goes through the MCP tools or the
direct-PAT path (`docs/CAPABILITIES-verified-2026-07-18.md`; the proxied REST
path 403s), and this session's harness routes GitHub work away from `gh` even
though the binary exists in the container (`MEASURED`: `/usr/bin/gh` present,
2026-08-29). So the snippet as written is untested in the venue the skill
targets. Fix shape: put the estate-native listing beside it, or defer the PR
inventory wholly to `prompt-preflight` §1 the way the rest of the state checks
already are. The `--limit is a maximum, not a page size` warning beside it is
right and worth keeping wherever the snippet ends up.

**F3 — the file breaks its own no-restating promise, and that debt has already
cost one near-miss.** `SKILL.md:15-17` says it *"cites those numbers rather
than restating the record"*; §§1 and 7 then restate the verdict tallies and
three `MEASURED` narrative blocks at length. `MEASURED` by grep, 2026-08-29:
the 815-of-925 figure stands in three committed surfaces besides this file
(the retrospective, the findings index row, the skill), and the sibling
refuter tally in three more on the #973 branch (data README, session card,
disposition comment) — and one copy was already mistyped once, the
155/122/7 near-miss the #973 card records against the measured 226/51/7. This
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
- Expected landing size ~300 lines with no check removed — the cuts are
  evidence prose, never the runnable checks or the contract lines.

## 4 · What to add — candidates, each waiting on first use

- **A `DEDUP`/precision contract line.** The audit's §7 names *"no
  deduplication was performed across cards"* among its heaviest limits, and no
  contract on the sheet covers output precision — §4 contracts the input
  corpus and §1 the decision rule, but nothing asks how double-counted the
  published rows are. Candidate: `DEDUP: <method over output rows> ·
  precision spot-check <n>/<n> read by hand`.
- **Make the `PILOT` line carry the number the run will be judged by.** The
  7.0 % refute rate was visible in the first verdict batch and read only at
  88 % of budget; §3 says so in prose, but `changed: <what>` does not force
  the metric out. Candidate: `PILOT: … · metrics read: <the rates the full
  run will be judged by>`.
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
| The census-caption rule — *composition in the same breath as the count; copy the caption, do not compose one* (§4) | `delegate-read` | The input-side contract for every corpus handed to Gemini: the fetch prints its own composition and that printout is the only quotable form. TRAP-004 at the cheap moment. |
| The retention fields — repo + `source_path` + sha/id + verbatim span + the instrument that selected it (§5) | `delegate-read` | Its citation-verification already checks the output side; this contracts the input side so follow-ups stay answerable. |
| Per-repo launch-SHA plus the scheduled re-read before writing (§6) | `prompt-preflight` | Its §1 verifies state for the repo at hand; this is the multi-repo delta form, plus the truncation warning (`--limit` is a maximum) that generalizes to every listing API. |
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
- the sheet is a committed artifact, so **use leaves a record**: a published
  fan-out finding with no quoted contract sheet is visible evidence the skill
  did not run — a partial answer to the no-telemetry objection that most
  skills cannot give;
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
2. **The bad-draft probe** (from the round's open list): re-run the committed
   judge-panel prompt (`docs/findings/data/workflows/03-judge-panel-skill-design.js`,
   fm #973) with one deliberately broken draft among the three. All three real
   drafts scored USABLE or better, so the panel has never been seen to reject
   — the same never-seen-red defect §1b guards against, one layer up. Three
   agents, minutes, decisive either way.

## 9 · The round's records against each other — the reconciliation that was owed

The reuse map and the error audit ran in parallel and were never checked
against each other. Done here, read-whole on both sides:

**They agree on the diagnosis, from independent instruments.** The delivery
gap is measured three separate ways: the audit's §2/§4 (328 prose-only rules
against 172 mechanical enforcers; 1 of 20 repos with any routing layer; the
kit's four-event channel present in 18 of 20), the reuse map's §5 (71 routes
covering conventions and **zero** covering the four rule surfaces; the trap
lifecycle run to completion for 7 execution mistakes and 0 rules), and the
standing 2026-08-08 measurement (116 statements, 0 catches). Same direction,
no shared instrument.

**They agree on the sharpest single fact of the round: proposals duplicate
existing coverage.** The reuse map's §7: in **17 of 17** refutations the
citation held and the verdict fell — *duplicate proposed as new*. The
catalogue: all 7 killed rows died as already-covered, and the survival rule
ignored the coverage field it collected — at verdict level 815 of 925 named
coverage (retrospective §3), and at row level the merged catalogue's own
labeling puts positive coverage on **233 of 284 rows** (`already_covered_positive`,
landed with #973 round 2; a cruder prefix cut this session ran reads 191, the
gap being partial "nothing fully, but…" answers — either way, most rows were
told something covers them and the rule read none of it). And OD-26 §20 is the
owner saying the same thing in his own words — *"redoing the same things over
and over"*. Three independent sources converge: **the estate's dominant
proposal-failure is re-proposing what exists, so the revised plan should start
from inventory, not from candidate lists.**

**A third quiet agreement:** the reuse map argues *prefer gates and checkers
over skills* (§1, §6 Move B), and the catalogue's own fix-family distribution
— produced by 80 harvest lanes with no such thesis — prescribes `checker` on
166 of 284 rows against `skill` on 20. The fleet independently voted the same
way.

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
