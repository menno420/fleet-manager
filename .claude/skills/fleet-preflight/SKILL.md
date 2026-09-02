---
name: fleet-preflight
description: "The contracts to write before a multi-agent fan-out spawns its first agent — the survival rule and the fields it reads, the instrument tested on known positives, a readable pilot slice, the corpus census, what raw input is retained, the base SHA, and the run's size against a concurrency limit you probed rather than inherited. Sibling of prompt-preflight; run it before any ultracode workflow, mass subagent sweep, or fan-out whose results will become a finding."
---

# fleet-preflight

Not how to invoke the harness — it covers that. This is the hour before launch,
which is where a fan-out's quality is actually decided.

Derived from one measured run: fleet-manager's estate-error audit, 2026-08-28/29
— **1,063 agents, 913,042 output tokens, 17.1 h**. Its telemetry, its six
failures and its own list of what it does not establish are in
[`docs/findings/2026-08-29-fleet-orchestration-retrospective.md`](../../../docs/findings/2026-08-29-fleet-orchestration-retrospective.md);
**§ 4 numbers the failures 1–6** and this file cites those numbers rather than
restating the record. Every one of the six was a *preparation* failure. None
would have been caught by running the fleet better.

## What this produces

One **contract sheet** — a scratch file, `CONTRACTS.md` beside the run's
scripts — filled in before launch and quoted verbatim in whatever the run
publishes:

```
AGGREGATE   : dies_if <expression> · unread fields <n> (exit <code>) · fixture kill <n>/<m> · refute authority <k>/<N>
INSTRUMENT  : <file> · positives <p>/<p>, negatives <n>/<n>, exit <code> · real-slice hits <h>/<n> read by hand
PILOT       : <lane> × <n> agents first · <n> transcripts read whole · changed: <what>
CORPUS      : <n> items = <composition pasted from the census output> · from <paths> at <when>
RETAIN      : <fields> · follow-up "<the next measurement>" answerable: yes/no
BASE        : <repo>@<sha> at <t0> · open PRs <#…> · re-read <sha>..main before writing
SIZE        : limit <n> via <PROBE (capacity) | JOURNAL (throughput only)> at <when> · <a> × <d>s ÷ <n> ≈ <h> h floor
EXTERNAL    : <who reviews the output after the fleet, and how many rounds are budgeted>
MODELS      : <stage> → <model tier> … · reasons: <stage(s) on opus> · reviews last: <stage on fable>
UNCONTRACTED: <any line launched unfilled, and why>
```

**Nothing here gates.** If a contract is not worth writing, put
`UNCONTRACTED — <reason>` on its line and launch. The cost of that choice then
travels with the finding instead of being found by a reviewer.

**Steps are ordered by catch-per-second, not by chronology.** If you read one
section, read § 1; if you read two, § 1 and § 2. Sizing is last because it is
the cheapest thing to be wrong about, not the least important.

## Instructions

### 1 · Aggregation contract — name the deciding field, and one case that must die

This is where the measured run lost most of its money. Verification was **929 of
1,063 agents and 88 % of output tokens**, and returned **925 verdicts: 572
PARTIAL, 293 CONFIRMED, 60 REFUTED — 7.0 % of verdicts set `refuted=true`, and 7
of 284 patterns died.** **815 of those 925 verdicts named something in
`already_covered_by`, and the survival rule keyed only on `refuted`, ignoring
that field entirely.** The right signal was collected and thrown away in
aggregation. Separately, of three "adversarial" lenses **only one was told to
refute**, so a lone dissent was always outvoted 2-1.

Before the judging stage launches, write the rule as an expression over field
names, then run three checks.

**a · Field audit.** Every field the verdict schema collects is either read by
the expression, or listed in `REPORT_ONLY` because it exists to be published
rather than to decide, or deleted from the schema. Deterministic, so run it:

```python
import ast, json, sys
# Point this at the REAL predicate — import it, or paste the exact source line
# from the workflow script. A retyped copy can pass while the code that runs
# ignores the field, which is the failure this step exists to prevent.
RULE = "refuted or (already_covered_by and lens_refuters >= 1)"  # ← paste from source
REPORT_ONLY = {"quote", "citation", "note"}   # collected to publish, never to decide
schema = set(json.load(open(sys.argv[1])))    # one sample verdict, or a key list
read = {n.id for n in ast.walk(ast.parse(RULE)) if isinstance(n, ast.Name)}
unread, missing = schema - read - REPORT_ONLY, read - schema
print("UNREAD   :", sorted(unread) or "none")
print("UNDEFINED:", sorted(missing) or "none")
sys.exit(1 if unread or missing else 0)
```

`UNREAD` is the 815/925 defect in its egg. `UNDEFINED` is its twin — a rule
reading a field the agents never emit, which silently evaluates falsey at scale.
Paste the real exit code, not your reading of the output.

**b · Fixture kill — and fixture survival.** Hand-write one verdict per branch
and run the rule over them. **At least one must die AND at least one must
survive**, each with its expected outcome written down first. A kill-count alone
is satisfied by a predicate that rejects everything: preflight passes, the fleet
runs, nothing survives, and you learn it at the end. A rule no fixture can kill
will not kill anything at scale either — and you will have paid 88 % of the
budget to find that out.

**c · Lens authority.** If N lenses vote, either all N carry the refute
instruction, or you are running N−1 confirmers and a mascot. Record per-lens
verdicts rather than the tally, so the lens that ever disagrees stays visible.

> **Contract line:** `AGGREGATE: dies_if <expression> · unread fields <n> (exit
> <code>) · fixture kill <n>/<m> · refute authority <k>/<N>`

*Catches failure 3, both halves.* It does **not** make the survivors true —
after the run's own 929-agent verification, external review (Codex) returned
**37 findings across 4 rounds, all conceded, none survived**. Budget the external
round (§ 7); the fleet's own verification does not substitute for it.

### 2 · Instrument contract — known positives **and** negatives, before the fleet

Every fan-out has one small piece of code deciding what the agents even see. In
the measured run it was an error-phrase regex compiled with `re.X`, which
silently strips literal spaces inside alternatives — `"was wrong"` compiled as
`"waswrong"`. **6 of 7 phrases were inert; 986 agents ran on it.**

```python
from your_module import PATTERN            # import the real one, never retype it
POSITIVE = [...]   # ≥1 real corpus string per phrase/branch that MUST match
NEGATIVE = [...]   # the near-misses that must NOT match
for s in POSITIVE: assert PATTERN.search(s), f"inert: {s}"
for s in NEGATIVE: assert not PATTERN.search(s), f"overmatch: {s}"
```

Two rules that come from the actual defect:

- **One positive per alternative**, not per instrument. Seven phrases and one
  passing test is six untested branches — exactly what shipped.
- **Print the compiled pattern and read it.** Under `re.X` a literal space needs
  `\ ` or `[ ]`; the defect is invisible in the source.

Then run the instrument over a slice of the real corpus and read the hits by
hand. A matcher that passes fixtures and returns nothing on real text is still
broken — [TRAP-003](../../../docs/traps.md): absence of evidence is not evidence
of absence until the instrument has a positive control.

> **Contract line:** `INSTRUMENT: <file> · positives <p>/<p>, negatives <n>/<n>,
> exit <code> · real-slice hits <h>/<n> read by hand`

*Catches failure 1.* It does **not** catch an instrument that matches correctly
and asks the wrong question; that is a design review, not a fixture.

### 3 · Pilot contract — launch a slice you can read whole, then commit the rest

Split every large lane. Launch it first at a size whose transcripts you will read
**completely** — not summaries, not a sample of the JSON — then commit the
remaining agents.

This is the only step that catches what nobody thought to check, and it is the
only place the run's headline number was ever visible in time: **the 7.0 % refute
rate was knowable from the first batch of verdicts and was read only afterwards,
at 88 % of the budget spent.** A pilot is also where an inert instrument, a rule
that never fires, and a field the agents do not actually populate all surface at
once, priced in whole minutes rather than hours.

Write down what the pilot changed, including "nothing" — that is a result, and
the sheet is where it is countable.

> **Contract line:** `PILOT: <lane> × <n> agents first · <n> transcripts read
> whole · changed: <what>`

*Catches the residue of 1, 3 and 5 that fixtures miss.* It does **not** catch
anything in a lane too small to pilot — at that size, read all of it.

### 4 · Corpus contract — composition in the same breath as the count

The run's finding said *"7,214 sections from 4,583 cards"*. The fetch had also
taken findings, retros, audits and program docs; measured afterwards, **89 %
cards, 10 % other**. Scope of the fetch and wording of the claim were written
hours apart and never reconciled.

Make the fetch print its own composition, and let that printout be the only thing
anyone quotes. Classify by the directory the item came from — mechanical, and it
is the split that was actually mislabelled:

```bash
# Census the RECORDS you will claim, not the files that hold them. For a
# sharded or JSONL corpus the file count is 1 or 68 while the claim is "7,214
# sections" — count the extracted items by their retained source path:
python3 -c "import json,collections,sys; \
print(collections.Counter(json.loads(l)['source_kind'] for l in open(sys.argv[1])))" evidence.jsonl
# Only when one file == one item does the file-level form apply:
find "$CORPUS" -type f | sed 's|.*/\([^/]*\)/[^/]*$|\1|' | sort | uniq -c | sort -rn
```

Paste that table into the sheet. When you later write "N items from X", **copy
the caption, do not compose one**: *"N items — 89 % session cards, 10 % findings,
retros and program docs"* is the honest version and is no longer than the wrong
one. This is [TRAP-004](../../../docs/traps.md) — a claim wider than the sample
that produced it — caught at the only cheap moment.

> **Contract line:** `CORPUS: <n> items = <composition pasted from the census
> output> · from <paths> at <when>`

*Catches failure 2.* It does **not** catch a corpus wrongly *scoped* — the table
is just as tidy when the fetch missed a repo. Its cover is § 6's per-repo list.

### 5 · Retention contract — keep the input, not only the output

The extractor kept the resulting document text and discarded the authoring input,
so the audit's own recommended follow-up — *"would this route have fired on that
incident?"* — is **impossible from its own corpus** and had to be downgraded to a
heuristic.

The flat rule, which needs no foresight: **when a transform has an input and an
output, retain both.** Then, per record — each cheap now and unrecoverable later:

- **`repo`** + `source_path` + `source_sha` (or PR / comment id) — the repo is
  not optional in a multi-repo fleet: the same path and the same PR number exist
  in many of them, and a bare SHA does not say which remote to ask;
- the **raw span**, verbatim, not a summary of it;
- the **input** that produced the artefact, where the artefact is derived — the
  prompt, the diff, the authoring text. This is the one that was lost;
- the instrument version or pattern that selected it.

Then write the follow-up you expect this fleet to recommend as a one-line
pseudo-query and check the schema answers it. If it does not, add the field now
or write the impossibility into the sheet, so the finding ships with its own
limit instead of a reviewer discovering it.

> **Contract line:** `RETAIN: <fields> · follow-up "<the next measurement>"
> answerable: yes/no`

*Catches failure 5.* It does **not** make the run cheaper — retention costs
storage and extraction time, and this step deliberately spends it.

### 6 · Base contract — what HEAD was at launch, and one scheduled re-read

**Run [`prompt-preflight`](../prompt-preflight/SKILL.md) § 1** for the state
checks; a fan-out dispatch is prompt-writing at scale and that skill owns them.
Two deltas belong here and only here.

**Per repo in scope, not just the one you are standing in** — the measured run
spanned 20:

```bash
for r in $REPOS; do
  echo "== $r"; git -C "$r" fetch origin main -q && git -C "$r" rev-parse --short origin/main
  gh pr list -R "$(git -C "$r" remote get-url origin | sed 's#.*github.com[:/]##; s#\.git$##')" \
     --state open --limit 500 --json number,title -q '.[] | "#\(.number) \(.title)"'
  git -C "$r" rev-parse origin/main > ".launch-sha.$r"   # one SHA PER REPO
done
```

`--limit` is a maximum, not a page size: at the default it silently returns the
first 50 and the sheet records a partial inventory as the whole one. Raise it
past any plausible count, or detect truncation and say so.

**And one re-read, scheduled now, run immediately before you write the finding
— over EVERY repo, not just the one you happen to be standing in:**

```bash
for r in $REPOS; do
  echo "== $r"; git -C "$r" fetch origin main -q
  git -C "$r" log --oneline "$(cat ".launch-sha.$r")"..origin/main
done
```

In the measured run `main` was never re-read at launch; mid-run **one PR merged
that fixed the exact defect being measured**, and another landed an owner ruling
that **retired the framing of the recommendation**. Both surfaced at the end,
costing an extra PR. Anything in that range touching what you measured either
updates the finding or is named in it as landed-after-measurement. Say when the
snapshot was taken, in the finding, next to the numbers.

> **Contract line:** `BASE: <repo>@<sha> at <t0> · open PRs <#…> · re-read
> <sha>..main before writing`

*Catches failure 4.* It does **not** catch a change landing between the re-read
and the merge, and for a run whose § 7 floor is many hours, the re-read is late
by design — `subscribe_pr_activity` on the PRs that could invalidate the run is
the only thing that surfaces one mid-flight.

### 7 · Size contract — measure concurrency, never quote it

Do this before committing to a lane size. The documented cap is
`min(16, CPUs−2)`; **the measured run planned assuming 10–16 and got peak 4,
mean 3.8, median 4** — wrong by 3–4×, because the documented figure was reported
as observed while the journals held the real number. Do not carry those four as
your number either: the retrospective's own § 6 says concurrency 4 is *that box,
that day*. The method transfers; the number does not.

Measure it from a previous run's journals. Journals carry per-message timestamps;
concurrency is the overlap of per-agent spans, which is arithmetic, so run it:

```python
import glob, json, statistics, sys
from datetime import datetime
pat = sys.argv[1] if len(sys.argv) > 1 else \
    "/root/.claude/projects/*/subagents/workflows/wf_*/agent-*.jsonl"
spans = []
for p in glob.glob(pat):
    ts = []
    for line in open(p, errors="replace"):
        try: t = json.loads(line).get("timestamp")
        except ValueError: continue
        if t: ts.append(datetime.fromisoformat(t.replace("Z", "+00:00")).timestamp())
    if len(ts) >= 2: spans.append((min(ts), max(ts)))
if not spans:
    sys.exit(f"no journals matched {pat} — nothing to measure; probe instead")
t0, t1 = min(s for s, _ in spans), max(e for _, e in spans)
samples = [sum(s <= t < e for s, e in spans) for t in range(int(t0), int(t1) + 1, 15)]
busy = [n for n in samples if n]
print(f"agents {len(spans)}  peak {max(samples)}  mean(busy) {statistics.mean(busy):.1f}"
      f"  median {statistics.median(busy)}  idle {len(samples)-len(busy)}/{len(samples)}"
      f"  mean dur {statistics.mean(e - s for s, e in spans):.0f}s")
```

(Exits non-zero with the glob it tried when nothing matches.)

**What that script gives you is OBSERVED THROUGHPUT, not capacity — and the
difference bit three times in one session.** Overlap sampling shows what ran
together; it cannot tell you whether more *could* have. If your fan-out was
narrower than the limit, you are measuring your own fleet's width and will read
a small number as a ceiling.

**So the primary method is a DEMAND TEST, and it is the cheap one:**

> Dispatch, **at one instant**, more agents than the limit you expect, and make
> each probe **stay alive while the others are still queued** (a fixed sleep, not
> a task that can finish early). Count how many actually overlap. Fewer than
> dispatched → that is the limit. Equal → the probe was too small; go wider.

**The barrier is not optional, and review caught why (Codex, fm #971).** Without
it, staggered provisioning produces the same signature as a limit: if probe 1
finishes before probe 3 is even provisioned, you see 2 overlapping at capacity 3,
and repeating the wave repeats the artefact rather than testing it.

**Discriminate before believing the number.** Provisioning speed is directly
observable in the same data — compare the gap *within* a wave against the gap
*between* waves:

| signature | reading |
|---|---|
| new agent starts within seconds of a **slot freeing** | slot-limited — a real limit |
| new agent starts long after a slot freed, at a fixed cadence | provisioning-limited — not a limit |

`MEASURED` 2026-08-29 on the run that produced this skill: probes within a wave
started **2–3 s** apart, so provisioning is fast; the gaps *between* waves were
**107 s and 128 s**, and each new agent began within **5 s of a slot freeing**.
Fast provisioning plus starts tracking slot-frees is slot-limiting. Had
provisioning itself taken ~120 s, the same pairs would have appeared with no
limit at all — which is exactly the confusion the barrier removes.

**That reading rests on one assumption, so verify it rather than inherit it:**
that a transcript's first timestamp marks when an agent *began executing*, not
when it was *dispatched*. If it marked dispatch, the within-wave gaps would be
dispatch spacing and the whole discriminator inverts. **Check it in one pass** —
measure each agent's gap from its first timestamp to its first assistant
message. A queued agent would show that gap growing with queue depth:

> `MEASURED` 2026-08-29 across 13 agents spanning 980 s of queueing: every gap
> fell between **1.7 s and 3.8 s**, including agents starting 869 s in. Flat
> against queue depth ⇒ the clock starts at execution, not dispatch. (One 17.4 s
> outlier was the synthesis lane's ~90 KB prompt — first-token latency, not
> queueing.)

If your harness shows that gap *growing* with start time, your first timestamps
are dispatch times and this discriminator does not apply.

Three throwaway agents read a limit of 2 in one wave. `MEASURED` 2026-08-29: a
run dispatching 3 simultaneously (a `parallel()` over three lenses) never
exceeded 2 in flight, three separate times — decisive, where comparing peak
values across runs had been worthless. Run it **at launch**, never inherited: in
the same session a fan-out saw 4 and a later one saw 2, **in different
containers**, one of which had booted twenty minutes earlier.

Then:

```
wall clock ≈ agents × mean_duration ÷ measured_concurrency        (a floor)
```

At the run's observed 4 and ~190 s, **each added agent cost ~48 s of wall clock
once saturated** — below the limit an added agent costs nothing extra. 1,063
agents was ~14 h serialised against 17.1 h actual, so treat the formula as a
floor, not an estimate. Then say, in one line per lane, what a
negative result from that lane would change. If nothing, shrink it and move the
budget to § 3's pilot or to the external round — which goes on the sheet as a
lane with a number next to it, **decided before the internal lane is enlarged**,
because in the measured run the external round was the entire yield and was not
planned for.

> **Contract lines:** `SIZE: limit <n> MEASURED by <demand test | overlap
> sampling> at <when> · <a> agents × <d>s ÷ <n> ≈ <h> h floor` and
> `EXTERNAL: <who, how many rounds>`
>
> Name the *method*, not just the number — an overlap figure from an
> unsaturated run is a throughput reading wearing a capacity label, which is the
> exact defect this contract exists to stop.

*Catches failure 6* at the place it did damage — the number reported to the
owner. It does **not** catch a documented value quoted as measured anywhere else
in the run; only the habit in § 1 and § 2 of pasting real exit codes does.

### 8 · Model contract — the tier per stage is chosen, never inherited

**Owner, live, 2026-09-02:** *"the dispatch agents should be judged by the
task, for general reading and mapping Sonnet 5 would be more than enough. But
when it's also necessary to use reasoning it's better to use Opus 5 and
probably as final reviewer it should be Fable 5.1."* ([D-0040])

Both fan-out surfaces take a model per call — the Workflow tool's `agent()`
has a `model` option per stage and the Agent tool has the same — and both
**inherit the session's model when it is left unset.** That default is what
staffed fm #1010's 204 night-fleet agents and the 2026-09-02 morning
workflow's six on Fable 5.1, metered against the owner's plan, for reads that
were Sonnet work. Write the tier down per stage before the first agent
spawns:

| stage | tier | why |
|---|---|---|
| readers, mappers, classifiers, census, extraction | `sonnet` | reading and mapping; the instrument is the prompt, not the model |
| verifiers, judges, merge/dedupe that must reason from evidence | `opus` | the stage that decides what survives |
| the final reviewer, critic, or spine judge — the last look | `fable` | the one that must be right |

> **Contract line:** `MODELS: readers → sonnet · verify → opus · critic → fable`
> (one arrow per stage the script actually has). A stage with no tier named is
> a stage nobody sized — say `UNCONTRACTED — inherited` rather than leave it
> blank, so the inheritance travels with the finding.

*Catches* the silent inheritance at the only moment it can be caught: the
script is being written, and `model:` is one more field beside `label:`.

## Output

The sheet at the top of this file, filled, committed beside the run and quoted in
what the run publishes. An empty `UNCONTRACTED` line is the goal; a populated one
is fine, as long as it reaches the finding rather than the reviewer.

## What this does not catch — and why

Honest limits, in the estate's terms: an undisclosed one is the real defect.

- **All six failures are caught only if the sheet is written.** Nothing here
  gates, by design, and this skill ships with **no route** in
  `.claude/hooks/doc-routes.json` — so it binds a session only when someone
  invokes it, and a skill that never loaded cannot bind (PL-013). Under
  [`docs/traps.md`](../../../docs/traps.md)'s own lifecycle that makes it
  unfinished work: the missing half is a route on the call that spawns a fan-out.
- **Failure 1 — residual:** fixtures prove the instrument matches what you
  thought of. An instrument that matches correctly and selects the wrong evidence
  passes every check here; § 3's pilot is the only cover, and only if a human
  reads the transcripts.
- **Failure 2 — residual:** the census describes what was fetched, never what was
  missed. A repo absent from `$REPOS` produces a clean, complete-looking table.
- **Failure 3 — residual:** a rule can be faithfully implemented, kill a fixture,
  read every field, and still ask a question too weak to overturn anything. That
  the measured run's survivors would have been better under a better rule is
  `REASONED` from the 815/925 discard, not demonstrated.
- **Failure 4 — residual:** the re-read is a snapshot before writing, so anything
  landing between it and the merge is missed, and a long run still spends its
  hours measuring a defect a mid-run PR may already have fixed.
- **Failure 5 — residual:** retention only answers the follow-ups you can name at
  launch. The measured run's own follow-up emerged *from* its findings; the flat
  input-and-output rule covers that case, an unforeseen third field does not.
- **Failure 6 — residual:** § 7 measures one number. Every other documented
  figure a run quotes — model limits, rate caps, schema guarantees — is
  unaddressed here.
- **Not covered at all:** whether the question is worth N agents (sizing gives
  the price, not the value); the per-lane prompts themselves (use
  `implementation-prompt` / `prompt-preflight`); and everything after launch
  except § 3's pilot and § 6's re-read. The measured run's six failures were all
  in place before the first agent started, which is why this skill stops there.
