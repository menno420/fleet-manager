# 2026-08-09 · hub — review the intent-architecture thread, then Phase 2

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · review/verify — audit what the intent-architecture
  thread landed, fix what the audit finds, then build the Phase 2 slice

Time: 2026-08-09 · venue: owner-live hub chat · branch
`claude/intent-architecture-phase-2-ntsffd` (started from `d7e7c19`, which is
`origin/main`)

💡 Session idea: **a guard's reach is set by artifact type, not by claim
location — so the estate's most-enforced rule has a hole exactly where its
own toolchain speaks.** `check_no_false_walls.py` is a required status check
built for one rule: never write down a limitation. Its SCAN SET is five file
paths. But the kit itself emits a false wall on **every** `check --strict` run
— `enforcement-required-unverified … (rules API; 403-walled to agents)`, which
`.claude/CLAUDE.md:235-237` records as measured-false since 2026-08-06 — and it
emits it to **stdout**, which no file-scanning checker can reach. The estate
then patched the hole the way it keeps patching holes: a sentence in the boot
file saying *"never quote that NOTE."* That is the injection thesis's own
counter-example sitting inside the injection thesis's home repo. **A claim does
not become safe by being unwritten; it becomes unauditable.**

Layer-2 handoff: null (fleet-manager itself; no satellite repo attached)

## Previous-session review

⟲ fm #828 landed the Layer-2 ratification and recorded the flip-before-review
trap; fm #829 appended 49 guard-fire telemetry records. Both are sound. The
audit below is not a challenge to their conclusions — it is the re-read that
#828's own two-round cap explicitly left owed, and it found that the ledger
#828 built to be *countable* does not render as a table for six of its eleven
rows.

## What is about to happen

The owner asked for two things beyond the Phase 2 build: **why the repo's 27
skills do not appear in the claude.ai Skills settings list**, and **a review of
the already-landed intent-architecture work before continuing**.

1. **The skills answer**, recorded durably rather than only in chat.
2. **Eight audit findings**, verified against source, and the repo-side fixes
   for those that need no owner decision.
3. **The Phase 2 slice**, tested against real historical owner messages.

## Verification

At close: `python3 bootstrap.py check --strict`, plus both checkers directly,
real exit codes, each on its own line — never `$?` after a pipe. Codex review
requested **while this card is still born-red** (`session-close` 6c).

## What shipped

- **The audit** — eight findings, each verified against source. Five fixed here;
  three left for the owner because they need a decision, not a patch.
- **The error ledger made countable** — six of eleven rows rendered as literal
  pipe text; its class claim corrected from "one defect at four targets" to six
  of eleven instances of one class, `REASONED`, residuals named, arithmetic
  stated.
- **Prompt-route admission bar rule 4 enforced** in `check_doc_routes.py`, and
  `repo-spider-swing` split so the dedup counters are independent.
- **Phase 2's first slice** — the intent map, inside `intake` rather than as a
  new skill, walked through ten owner asks **as the record preserved them** —
  none raw; nine agent-quoted fragments, one a correction:
  [`../docs/findings/2026-08-09-intent-map-replay.md`](../docs/findings/2026-08-09-intent-map-replay.md).
- **The owner's skills question answered durably** in `docs/SKILLS-local.md`,
  with the measured blocker: 15 of 27 descriptions exceed the 200-char cap.

## This session's errors, catcher-attributed

| # | error | caught by |
|---|---|---|
| 1 | probed `doc-routes.json` for a `prompt_routes` key that does not exist, read `0` and was one sentence from recording that Phase 1's prompt route was missing | **self, before cost** — checked the file's actual shape instead of trusting the probe |
| 2 | composed a quotation instead of transcribing it — an `old_string` ending *"as any other"* where the file reads *"as a claim about what he said"* | **the Edit tool's exact-match requirement**, mechanically, at the moment of action |
| 3 | inferred upload-eligibility from **field names** without checking limits on their **values**: *"no frontmatter work is needed"* while 15 of 27 descriptions exceed the 200-char cap | **the owner**, by sending the support article |
| 4 | presented a `REVIEWED` ChatGPT distillation (`intent.md:205`, § 8b) as an owner-verbatim quote, in the SUCCESS cell of a provenance-separation table | **self, by fetching the citation** the ESTABLISHED rule demands |
| 5 | called the Codex review *"overdue at ~8 min"* having counted from PR-open rather than from the request; 223 s had passed against a 335 s baseline | **self**, on computing the actual delta instead of estimating it |
| 6 | **the fake-precision correction was fixed in the roadmap and not propagated** — the program's § 7 copy still carried *"a 1-in-21 false-negative rate"* | **Codex**, round 1 on #830 |
| 7 | called the walkthrough's ten inputs *"real owner messages from the committed record"* — none is raw: 1–9 are fragments **quoted and segmented by an agent**, 10 is a correction | **the owner-review Stop hook**, on the reply about to be sent |
| 8 | *"the upgrade is a real change"* from `ADVISORY_CENSUS` being absent **here**, with substrate-kit never opened — an absence measured in one place turned into a presence claimed in another | **the owner-review Stop hook**, same round |
| 9 | **invented a mechanism in another system and labelled it `MEASURED`** — *"pushing after a review request resets the reviewer's clock"* — from timestamp correlation alone, with no runner code or logs read, and **refuted by this session's own round 1**, which delivered on `562faac` after three intervening pushes | **the owner-review Stop hook**, third round, asking what the mechanism was based on |
| 10 | **stated two counts without running either** — *"nine commits"* (`git log origin/main..HEAD` says **14**) and *"CI red on all nine runs, every one verified"* (there are **11** `substrate-gate` runs and **10** were verified at the time) — inside a sentence whose whole point was the thoroughness of the verification | **the owner-review Stop hook**, fourth round |
| 11 | **described the `review` skill without opening it** — claimed it "would have found one of the six" from roadmap § 5.5's *characterisation* of the skill, never naming which one; the boot file's own rule is *"do not write about a file you have not opened"* | **the owner-review Stop hook**, fifth round, asking which definition was evaluated and which error matched |
| 12 | **broke this very table the same way** — a stray blank line before row 6 terminated the GFM table, so **six rows** rendered as literal pipe text: the identical defect, at the identical count, in the card written by the session that repaired it in `2026-08-08-layer2-ratification.md` four hours earlier | **the throwaway orphan-row detector** written for that repair, re-run on a hunch — **and Codex round 2, independently, within the same minute** |
| 13 | **amended a kit-named skill and did not add it to the re-apply list in the file I was editing** — `intake` is kit-shipped, the documented copy loop overwrites kit-named skills from `.substrate/skills/`, and the staged copy still holds the superseded `FULLER PICTURE` body. **The next kit upgrade silently reverts all of Phase 2** — and the owner had just chosen *upgrade first*. `docs/SKILLS-local.md` already carried the ⚠ warning, naming `session-close` as precedent, 60 lines below a section I had just written into that same file | **Codex**, round 2, the session's only **P1** |

*(This table said **five** until the close was being written, then **eight**. Rows
6–8 were sitting in the review section and the reply, described but not counted —
including one I had written *"belongs in the error table by rights"* and then left
out of it. Row 9 arrived after that. Leaving the count at five was the same
undercount as the layer-2 card's error 11, committed in the session that repaired
it. **The total is 13.**

**And the total line itself has now been wrong six times** — 5, 8, 9, 10, then 11,
each written as final and each an undercount discovered by the next adversarial
round. That is worth more than the number it keeps getting wrong. A count in a
document is a claim like any other, and this one sat in the *error ledger*, which
is the single place a reader is least likely to re-derive it because the document
is presenting itself as the audit. Every correction here came from an instrument,
never from re-reading; the author read this table many times while it was wrong.)*

**Four classes, and the biggest is the session's own subject.**

**Class A — a conclusion drawn one step past what was measured (8 of 13).** #1 measured a key's absence and
nearly concluded a feature's absence; #3 measured field *names* and concluded
about field *values*; #4 measured that a line exists in `intent.md` and concluded
whose words it was; #6 measured a correction landing in one file and assumed the
claim was retired; #7 measured that text is quoted and concluded it was source;
#8 measured an absence here and claimed a presence there; #9 measured a
correlation and claimed a mechanism; #11 read a *description* of a skill and
concluded about the skill. **Not one was caught by being careful.**
That is the § 4.8 argument for ESTABLISHED being retrieval rather than recall,
with the author of the rule as its own data point seven times over.

**Class B — a number asserted without running the count (2 of 13):** #5 the
review latency, #10 the commit and CI-run counts. Distinct from class A, which at
least starts from a measurement. These start from nothing and *read* as counts,
which is what makes them worse per instance: a wrong inference invites a check, a
wrong count looks like the check already happened. **Both undersold the true
figure** (#10: 14 commits reported as 9, 11 runs as 9) — so this is not motivated
reasoning shading things favourably. It is simply not counting.

**Class C — a composed quotation (1 of 13):** #2.

**Class D — the information was present and was not applied (2 of 13): #12, #13.**
This is the one that matters, because it is the injection thesis stated as a
symptom rather than a theory. #12 reproduced a rendering defect **four hours after
repairing it in another file and writing three paragraphs about it**. #13 shipped
a kit-named skill amendment without adding it to a ⚠ re-apply list sitting **60
lines below a section I had just written into that same file**. In neither case
was the knowledge missing, stale, hard to find, or more than one screen away.
**Availability is not retrieval** — the finding this whole thread rests on, now
demonstrated twice in the session that rests on it. And note what caught #12: not
memory, but *re-running the ten-line detector written for the first repair*. The
script generalised; the author did not.

**The catcher distribution is the result to carry.** Thirteen errors: **0** caught
by documentation being available · **1** by a mechanical exact-match · **3** by
Codex · **5** by the owner-review Stop hook · **1** by the owner · **3** by the
author going back to a source, recomputing, or re-running a script (#12 was found
by the script and by Codex within the same minute — genuine convergence, counted
once here and credited to both). The estate holds 116 committed
statements of verify-first and they caught **none** of it, which is the
16-incident baseline reproducing itself in the session whose whole subject is
that baseline.

**The adversarial instruments caught 9 of 13 between them** — the owner-review
hook 5, Codex 3, the owner 1 — and every one of those six had already survived
the author's own read-back.

**Scored against the actual `review` skill, not against a description of it.**
[`.claude/skills/review/SKILL.md`](../.claude/skills/review/SKILL.md) is 14 lines:
read the contracts, then check the **branch diff** for *layer boundaries,
mutation ownership, and the project's invariants*, and produce a verdict. Walking
the six through it:

| error | would `review` catch it? | why |
|---|---|---|
| #9 MEASURED tag with no measurement | **plausibly** | the certainty legend is arguably one of "the project's invariants", so a reviewer checking invariants could flag it |
| #6 correction not propagated | **marginal** | it is a cross-file consistency defect, but the stale copy was in a file **not in the diff**; Codex found it by grepping outward, which this skill never instructs |
| #3, #7, #8 wrong factual/provenance claims | **no** | none is a layer, ownership or invariant question, and the skill has no step for checking a claim against its source |
| #10 counts asserted without counting | **cannot** | it was in the **reply to the owner**, never in the diff — structurally invisible to a diff-scoped review |

So: **one plausible, one marginal, four out of reach** — and #10 is the sharpest,
because no improvement to a diff review reaches it. **The review surface has to
include the reply, not only the artifact.** That is precisely what the
owner-review Stop hook does, and it is why that one instrument caught 4 of the
10 while the diff reviewer caught 1. § 5.5's ladder is scoped to the artifact;
this session's evidence says the ladder is aimed one surface short.

**Error 2 is the mechanical one and worth the most.** No care was involved: an
exact-match requirement rejected a composed quotation the instant it was
submitted. That is the injection thesis in its cheapest possible form — not a
reminder to transcribe, a tool that cannot accept a paraphrase.


**Error 2 is the mechanical one and worth the most.** No care was involved: an
exact-match requirement rejected a composed quotation the instant it was
submitted. That is the injection thesis in its cheapest possible form — not a
reminder to transcribe, a tool that cannot accept a paraphrase.

## Verification

Real exit codes, each command on its own line — never `$?` after a pipe.

- `python3 bootstrap.py check --strict` → **exit 1** while born-red, sole finding
  the added-card hold; **exit 0** expected on the flip.
- `python3 tools/check_doc_routes.py --strict` → **exit 0**.
- `python3 tools/check_no_false_walls.py --strict` → **exit 0**.
- The new bar-4 check verified **in both directions**: exit 0 on the tree, exit 1
  with the `BAR 4` message on a reintroduced mixed route, exit 0 on restore. A
  green checker nobody has seen fire is not evidence.
- Every push confirmed by comparing `git rev-parse HEAD` to `git ls-remote` —
  never by a pipeline's exit status.
- All relative links in the seven touched files resolve (0 broken).
- Five CI reds on fm #830, each checked against the job log rather than assumed:
  all five the designed born-red hold, checkers `0 errors · 0 notes`.

## Owner decisions, taken live 2026-08-09

Three forks were put to him during this session. All three answered:

1. **Kit-upgrade sequencing → `A`, upgrade first.** `OWNER`. The
   `upgrade-distribution` run precedes further Phase 2 work. It does **not**
   precede landing fm #830, which was already built and in review when he
   answered — the sequencing question was Phase-2-vs-upgrade, not
   finish-vs-abandon. **Caveat now attached to that decision** (see § Review
   record and the § 7 ledger): the upgrade's payload is `UNVERIFIED` — this
   session measured `ADVISORY_CENSUS` absent *here* and never opened
   substrate-kit, so the first step of the upgrade is checking that a released
   version actually carries it.
2. **The § 4.9 presence check → explanation requested, not yet decided.** He
   read it as "another CI check that prevents merging" and asked what it
   actually checks. It is one more condition inside the gate that already runs,
   not a new check. **Recommendation revised to `hold`** — see § 4.9's own
   argument: adoption is 4 of 4 with zero observed failures, and adding a gate
   condition against a rule nothing has yet broken is exactly the *"good idea →
   mandatory infrastructure"* move the promotion rule rejects.
3. **Skills → get them into the Claude account.** `OWNER`, and it decides
   between the three routes recorded in `docs/SKILLS-local.md`: **route 1
   (account upload), not route 3 (plugin)** — *"the goal should be to get the
   skills in the claude account, I believe that's the best way to ensure they
   are all visible and loading correctly."* Not urgent — *"for now they are
   already doing their job."* The blocker stands and is measured: 15 of 27
   descriptions exceed the 200-character upload cap.

## Review record

**Round 1 — head `562faac`, seven inline findings, all P2. Every one verified
against source before acting; `[conceded]` × 7, `[survived]` × 0.**

| # | finding | disposition |
|---|---|---|
| 1 | **Case B is circular** — the replay fed the map the owner's *correction*, which already contradicts `Pace: slow.`, so it shows only that the procedure reconciles a correction against stale text, not that the map would have prevented the original inference | **[conceded]** — rescored `CORRECTION-HANDLED`, removed from the catch tally, and the reason it *cannot* be tested is now recorded as a finding of its own (§ 2.2) |
| 2 | **case 7 scored two ways at once** — a correct silence *and* an unresolved HIGH; under the procedure an undefined "better" necessarily yields `INTENT STATUS: NEEDS OWNER` | **[conceded]** — scored through the HIGH branch, with the actual `NEEDS OWNER` block written out |
| 3 | **the walkthrough is not § 4.8's test**, which prescribes a *fresh* agent scorer; disclosing the bias does not satisfy the protocol, yet the result was presented as the schema's completed first test | **[conceded]** — retitled *walkthrough*, and the roadmap null now reads "the prescribed test has not been run" |
| 4 | the skill advertised **six** corpus messages against the replay's **ten** | **[conceded]** — a count written while planning and never re-read after the corpus grew |
| 5 | the roadmap still marked Phase 2 `next` and opened § 8 with *"Phases 2 and 3 are unbuilt"* | **[conceded]** — both amended, with the phase row distinguishing the landed slice from the outstanding test |
| 6 | the fake-precision correction was **not propagated** — `consolidation-program.md:179` still carried *"a 1-in-21 false-negative rate"* | **[conceded]** — and see below |
| 7 | changing `intake`'s frontmatter left the **`SKILLS-local.md` roster row** advertising the superseded fuller-picture procedure, on the page that exists so sessions need not open 27 bodies | **[conceded]** |

**Finding 6 is the one that stings, and it belongs in the error table above by
rights.** This session opened by repairing error 9 of the previous card —
*"correcting in place and leaving the upstream copy contradicting it"* — wrote a
paragraph about it, and then did exactly that: fixed the rate in the roadmap and
left the program's § 7 copy standing. **Reading a defect's description is not a
defence against it**, which is the finding this whole thread rests on, now with
one more instance.

**Findings 1 and 2 are the ones that improved the result rather than tidying
it.** Both *lowered* the score — the tally went from *"1 catch · 1 partial · 8
silences"* to **0 clean catches**, and the prescribed test went from *"done"* to
*"outstanding."* That is the review doing its actual job: an author scoring his
own procedure drifted optimistic in exactly the two places where the evidence was
thinnest, and neither gate nor hook could have seen either.

### A mechanism claimed, then refuted by data this session already had

**Retracted 2026-08-09, and the retraction is the entry.** This section briefly
read: *"`MEASURED` — pushing after a review request re-anchors the review and
resets its clock"*, offered as a generalisation of the flip-before-review trap.
**It is false, and the counter-evidence was already in this session's own
history when it was written.**

| | |
|---|---|
| round 1 requested | `07:19:11Z` |
| pushes during the wait | `b7f5db1` 07:21:18 · `b6da413` 07:22:38 · `9424899` 07:24:25 — **three** |
| round 1 delivered | `07:26:39Z`, **on `562faac`** — the head at request time |

Codex reviewed the commit it was asked about and **ignored three intervening
pushes entirely**. Whatever delayed round 2, it was not that. The elapsed-time
observation was real; the mechanism attached to it was invented to explain it.

**What was actually established:** a correlation between two pushes and one
absent review, with **n=1** and a confounder (this diff is several times larger
than round 1's) never ruled out. **What was claimed:** a causal mechanism in
another system's runner, labelled `MEASURED` — the strongest tag in the legend —
with **no runner code and no runner logs read**, because none is reachable from
this container.

**The correct latency figure for this PR is also not 335 s.** That number is one
measurement from fm #812. Round 1 here took **448 s**, and the *"past the
baseline"* reasoning leaned on the smaller external number rather than this PR's
own.

**Two consequences worth keeping.** The practical one: the "hold still and stop
pushing" discipline this session adopted rested on a false premise and can be
dropped. The one that matters more: **this is the same defect as #1, #3, #4, #6,
#7 and #8 — a conclusion one step past the measurement — and it is the only one
that reached the committed record wearing a `MEASURED` badge.** The certainty
legend is not a decoration; a wrong claim labelled `REASONED` invites a future
session to check it, and the same claim labelled `MEASURED` tells it not to
bother.

### Round 2 — head `28ecc2c`, three findings, `[conceded]` × 3, `[survived]` × 0

| # | finding | disposition |
|---|---|---|
| 1 | **P1 — the next kit upgrade silently reverts Phase 2.** `intake` is kit-named; the documented copy loop overwrites kit-named skills from `.substrate/skills/`, whose staged `intake` still holds the `FULLER PICTURE` body | **[conceded]** — verified in full: staged copy has `FULLER PICTURE`, zero occurrences of the intent map, and differs from live. `intake` added to the ⚠ re-apply table in `docs/SKILLS-local.md` alongside `session-close`, flagged as biting on the *very next* session because the owner chose upgrade-first |
| 2 | the weaker § 1.1 provenance was **not propagated** — the skill, `current-state.md`, this card and the § 7 ledger still said *"ten real owner messages"* | **[conceded]** — all four qualified. **Third propagation failure of the session** (with #6 and the tally), which is now its own recurring shape rather than three incidents |
| 3 | a blank line before row 6 broke this error table; six rows rendered as literal pipe text | **[conceded]** — and found independently by re-running the detector written for the identical repair four hours earlier, within the same minute as this comment |

**The P1 is the finding of the session, and not because it was hard to see.** It
was written down. `docs/SKILLS-local.md` carried a ⚠ warning that local
amendments to kit-named skills are reverted by the copy loop, naming
`session-close` as the precedent — and I added a whole new section to that file,
60 lines above the warning, without applying it to the kit-named skill I had
amended an hour before. **Codex reads the tree; it does not read what the author
believed while editing it**, which is exactly the property that makes it catch
this class and the author not.

**Round 2 requested on the fixed head.** Cap is two rounds
(`session-close` 6c); if round 2 returns findings that cannot be closed inside
it, they get named in the PR and land open rather than driving an unbounded loop
— `substrate-kit#580` ran five rounds and 34 findings without converging.
