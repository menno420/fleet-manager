# What is wrong with fleet-manager — findings from the full read

> **Status:** `audit`

Produced by reading every tracked file in the repository (coverage proof:
[`verification.md`](verification.md), ledger: [`coverage-ledger.tsv`](coverage-ledger.tsv)).
Every finding below was then handed to an independent agent instructed to **refute**
it against the tree and to default to refuted when uncertain.

| | count |
|---|---|
| findings raised | 345 |
| **survived refutation** | **322** |
| refuted and dropped | 23 |
| — of survivors: defect | 101 |
| — of survivors: stale but harmless | 205 |
| — merged as duplicates of a row above | 16 |

The three survivor rows sum to 322. Duplicates arise where two agents
raised the same defect at the same `path:line` from different batches; where one judged
it a defect and another harmless, **the defect classification wins** and the harmless
twin is merged, so no site carries contradictory guidance.

Decision ids are neutralised so that quoting them as evidence does not register a
second *home* under the gate's stamp discipline. In prose they use a non-breaking
hyphen (the estate's own fix, `scripts/gen_roster.py:1029`); in the **Check it**
commands they use a regex character class (`D[-]0015`), which runs verbatim in any
quoting style — a command a reader cannot paste is not evidence.

**The split is the point.** *Defect* means a live surface a session could act on
today and be misled. *Stale but harmless* means accurate-but-inert: a dated session
card, an explicitly historical doc, a record that was true when written. An
undifferentiated list is unusable to whoever has to act on this, and roughly half of
what the readers raised is inert.

---

## Start here — the seven that cost the most

A hundred defects is nearly as unusable as no split at all, so these are ranked by
what they cost a session that acts on them. Each was verified by hand against the
tree, not only by the agent that raised it. The rest of the list is ordered
live-surface-first below.

**1 · The NOW pointer routes the next session to a repository the owner has
deprioritised.** `docs/planning/2026-07-26-consolidation-program.md:62` reads
`### ➡ NOW: **D2 — shiftlife truth pass**`, echoed at `docs/current-state.md:40`,
`:176` and `:517`. `OWNER` (2026-08-10, live, to this session): shiftlife is not
active; spider-swing and the superbot repos are. **That statement is nowhere in this
repository** — which is why every document agrees with every other one and all of
them are wrong; a session cross-checking finds agreement, not contradiction.
`MEASURED` and independent of the owner's statement: spider-swing appears in **none**
of §2's eight target-picture rows and nowhere in D2's order, while `:86` of the same
file records that every evening since 07-26 has gone to it, *"the only asset in the
estate with a live external signal."* The ordering encodes 2026-07-26 activity;
spider-swing was created 2026-07-28, so advancing the pointer can never arrive there.

**2 · The capability ledger opens with three walls it later retracts.**
`docs/CAPABILITIES.md` is `living-ledger`, *"verified findings, never assumptions —
Read at session start."* Its `:123` section **"Walls — verified blocked (use the
workaround; don't rediscover)"** lists tag push, branch deletion (*"403 on every
path"*) and `api.github.com` (*"blocked → GitHub access is MCP-tools-only"*). All
three are refuted in the same file at `:775` and `:888`. The corrections were
appended; the rows were never touched. The gate does fire — as `[stale-wall]`
advisories, *"29 days old > 14-day window"*, explicitly never exit-affecting. **The
instrument says the claim is old where the file already says it is false.**

**3 · Live deployment text tells a session to make the one call the estate denies.**
`docs/prompts/init-prompt-universal.md` is `living-ledger` and says *"Use the current
text for every new deployment."* `:22` reads *"⚠ NEVER `delete_trigger` … This prompt
founds sessions in repos that do NOT load fleet-manager's guard hook, so this line is
the only protection they get."* `:24` reads *"then `delete_trigger` the old one (F-1
rule)."* Commit `0ab4d07` — the commit that built `trigger_tools_guard.py` — added
`:22` and left `:24`. Nineteen further files carry the same order
(`git grep -ln 'Delete every routine THIS seat created'`), but those are the
seat-era prompt corpus and are filed harmless: bannered historical, seats closed,
guard chain in front. **This one is not.**

**4 · The owner's own reserved step points at nothing, and is absent from his queue.**
The program's E1 row (`:95`) says *"Method + sources: the plan doc above."* The
program contains **zero** markdown links before that line. The real plan,
`docs/planning/2026-07-26-final-eap-email-plan.md`, has exactly one live inbound
link (`docs/planning/README.md`, itself four hops out) and its own header still calls
E1 *"the program's NOW"*, which stopped being true on 2026-08-01. `docs/owner-queue.md`
— the file the boot file calls the consolidated queue of genuinely owner-only asks —
carries **no entry for E1 at all**, while listing the email-pack the program schedules
for supersession under *"Parked (valid, no rush)"*, with *"send on the existing Gmail
thread"* where E1 requires a fresh compose.

**5 · The kit re-apply table names two of seven skills at risk.** `docs/SKILLS-local.md:109`
warns that *"Two kit-named skills now carry fleet-manager amendments."* Seven diverge
from their staged copies, extra text always on the live side: `intake`,
`prep-owner-steps`, `quality-gate`, `release`, `scope-backlog-item`, `session-close`,
`upgrade-distribution`. A session following that table after an upgrade re-applies
two, silently reverts five, and reports a clean install. Reverting `quality-gate`
deletes the skill's only pointer to `check_no_false_walls.py`.

**6 · The false-wall checker calls itself advisory; it is a required check.**
`tools/check_no_false_walls.py:26,28,80` — *"advisory only, never wired into a
blocking gate"*, *"can never jam the substrate-gate"*, *"PROMOTE to a required check
once it stays clean"* — against `.github/workflows/substrate-gate.yml:170`, which runs
it `--strict` inside the required gate. Its escape clause (*"not wired into
`bootstrap.py check`"*) is **literally true**, which is exactly why the sentence
survived its own promotion on 2026-08-06.

**7 · The link checker cannot see the surfaces that bind a session.**
`scripts/check_docs_links.py:99` scans `docs`, `projects`, `environments`, `registry`,
`templates`, root `*.md` and `control/README.md`. It never scans `.claude/` — so
neither the boot file nor any of the 27 installed skills is link-checked. That is why
a broken link in `session-close` survived with the checker exiting 0. Fixed in this
PR as a one-line correction; the scan-set gap is not.

### The mechanism underneath all seven

Every one of these was produced the same way: **a correction was derived and the
document around it was inherited.** The append went in — the retraction at
`CAPABILITIES.md:775`, the warning at `init-prompt-universal.md:22`, the promotion of
the false-wall checker, the supersession note in the Layer-2 design — and the text it
contradicted was left in place, still reading as current. Every one of these documents
is internally coherent, which is why review passes over them.

The estate already knows this shape. `docs/ideas/derive-dont-state-counts-2026-08-10.md`
names it for counts and lists three prior instances; this audit found a fourth on the
day that idea was written (`docs/CAPABILITIES.md` says *"19 routes"* twice; the tree
holds 24, and it was already wrong at 20 when written). What the idea does not cover is
the larger class: **an appended correction does not retract what it corrects.** A
checker that ages claims cannot notice a retracted one, and the retraction is usually
sitting in the same file.

### Where the seven stand now — re-measured against the tree, 2026-08-11

The audit read the tree at `4b59e9b`. The session that produced it then landed
fm #839/#840/#842, which moved three of these seven. **Each row below was re-run
against the working tree rather than inferred from what a PR claimed**, so the next
session neither re-fixes what is closed nor assumes the rest decayed with it.
~~**1 closed · 6 open.**~~

**Re-verified and then worked, 2026-08-11 (fm #846) — 7 closed.** All seven
re-check commands were executed *before* any edit and every verdict reproduced
(1 closed / 6 open; no third bad command — the two earlier bad versions stay
recorded in row 1). The edit pass then closed the six at their sites. Each
row's command below was run **after** its fix and proves the closed state.

**The sweep, 2026-08-11 (fm #849) — 99 of 101 entries now closed; 2 open,
both kit-side.** The 67 the edit pass left were taken by the sweep session:
59 fixed at their sites, six recorded as already discharged (D4 and D84 by
fm #840, D61/D62 by the 2026-08-10 index regeneration, D94/D95 by fm #846),
and **D44/D45 left honestly OPEN** — `bootstrap.py` is GENERATED, so their
fix is substrate-kit's (v1.21.0 track). Derive the counts rather than
quoting them: `grep -c '^\*\*Closed 2026-08-11' docs/audits/2026-08-10-full-read/findings.md`
→ **99** closure paragraphs against
`grep -cE '^### D[0-9]+\.' docs/audits/2026-08-10-full-read/findings.md`
→ **101** entries. Every closure carries its exact executed proving command;
the 86-assertion battery re-ran green after the session's last edit.

**A `PARTIAL` here would be a lie of the useful kind**, so there are none. Rows 5
and 7 were first published `PARTIAL` on the strength of edits that touched the
same *file* — and Codex refused both on review: fm #840 added an amendment to the
`session-close` row that was already listed, documenting none of the five omitted
skills, and it fixed one link that had escaped the checker without touching the
checker's scan set. **Repairing an instance is not progress on the defect that
produced it**, and crediting it as progress is how an edit pass concludes that
half the work is already discharged. Where a same-file edit happened, the row
says so and still reads `OPEN`.

| # | the finding, short | status | re-check it |
|---|---|---|---|
| 1 | NOW pointer routes to a deprioritised repo | **CLOSED** (fm #840) | `git grep -n 'shiftlife truth pass' -- docs/planning/2026-07-26-consolidation-program.md docs/current-state.md` → **exit 1, no hits**. **Name the two routing files; do not sweep a directory.** An unscoped sweep exits 0 on this audit's own record, on `raw/adjudication.jsonl` and on `owner-queue.md:46` — all hits on the *description* of the defect, not the *pointer*. Two earlier versions of this cell shipped a command that did not reproduce: the first swept `docs/`, the second used a `git`-only pathspec against GNU `grep` (which reads it as a filename and exits 2) and still matched the owner queue. The pointer now reads *"D2 — next repository awaits the owner's target (shiftlife SUPERSEDED)"* with the owner's live statement quoted beneath it, and OD-15 is in the directive table. **The defect is closed; the decision it exposed is not** — which repository D2 targets is open at `OQ-FM-D2-TARGET`. |
| 2 | The capability ledger opens with three walls it later retracts | **CLOSED** (fm #846) | `sed -n '123,146p' docs/CAPABILITIES.md \| grep -c RETRACTED` → **3**. All three rows struck in place, each pointing at its append-log refutation and re-dated to its real last verification (2026-08-05 / 2026-07-31); `docs/seat-digest.md`'s derived render carries the same strike. The rows sit **inside the kit's `capability-seed` fence**, so the correction is registered in `docs/SKILLS-local.md` § Generated-file corrections — an upgrade may restore the false rows, and the durable fix is the kit seed (v1.21.0 track). |
| 3 | Live deployment text orders the one call the estate denies | **CLOSED** (fm #846), per the fm #845 re-judgement | `sed -n '3p' docs/prompts/init-prompt-universal.md` → `` `historical` ``, and the header's deploy sentence is gone (`grep -c 'Use the current text for every new deployment' docs/prompts/init-prompt-universal.md` → **0**). The re-judged defect was the badge + deploy sentence — *"live deployment text"* had been inferred from a `living-ledger` badge on a file whose own header says `superseded 2026-07-10` and which `docs/MAP.md:67` / the boot file classify as retired record. An **Era banner (2026-08-11)** now names `[D‑0015]` and rules the `:24` `delete_trigger` step must not be followed; the block itself stays verbatim per the file's own convention, as record. |
| 4 | E1's reserved step points at nothing and is absent from the queue | **CLOSED** (fm #846) | `grep -c 'final-eap-email-plan' docs/planning/2026-07-26-consolidation-program.md` → **2** (the E1 row and the §7 fm #833 row both link the real plan) and `grep -c 'OQ-E1-FINAL-EAP-EMAIL' docs/owner-queue.md` → **1** (the queue entry, owner-reserved, fresh-compose noted, cross-linked to the email-pack it supersedes). The plan's own header no longer claims *"the program's NOW"* — it states OWNER-RESERVED, as does its `planning/README.md` row (which also gained the four missing index rows, D81). |
| 5 | The kit re-apply table names two of seven skills at risk | **CLOSED** (fm #846) | `grep -n 'SEVEN kit-named skills' docs/SKILLS-local.md` → hit; the ⚠ table now carries **all seven** rows with per-skill amendment descriptions derived from `diff` (not recalled), the derivation one-liner is committed beside the prose so the set is re-derivable, and the six understated roster rows read `kit, fm-amended` (D15). Note the divergence *set* grew inside this same PR — `quality-gate` and `scope-backlog-item` gained further amendments (D21/D22) and their table rows say so. |
| 6 | The false-wall checker calls itself advisory; it is a required check | **CLOSED** (fm #846) | `grep -c 'PROMOTED 2026-08-06' tools/check_no_false_walls.py` → **1** and `grep -c 'BLOCKS the merge' tools/check_no_false_walls.py` → **1** — the Reliability header states the promotion and names all three enforcement paths (required `substrate-gate` · `scripts/preflight.py` · the engine port — D24's refuter set); the "DELETE this if unreliable" licence is replaced with the opposite instruction. The old wording survives only inside quoted retraction parentheticals, which is the correct shape. Docstring-only; `--selftest` still passes. |
| 7 | The link checker cannot see the surfaces that bind a session | **CLOSED** (fm #846) | `python3 scripts/check_docs_links.py --list \| grep -c '^\.claude/'` → **29** files now scanned, and the full run prints `CLEAN — every intra-repo link in 369 file(s) resolves`, exit **0**. The first `.claude` scan immediately surfaced two checker defects — a link inside an *inline code span* flagged as dead (code spans do not render as links), and `slugify` collapsing the `--` GitHub really produces for em-dash headings, which made a *correct* anchor read dead — both fixed with selftest cases pinning them. |

**Anchor drift — read this before quoting a `path:line` below.** The entries are
anchored against `4b59e9b`. **Do not trust a list of the files that moved — derive
it**, because the set grows with every PR that lands and a written list is stale on
arrival. The first version of this paragraph named six files from what the session
remembered editing; the derivation below returned **24**, and Codex caught the gap
on review:

```bash
git diff --name-only 4b59e9b..HEAD          # everything that moved since the audit
```

Intersect that with the paths an entry cites. As of fm #845 it covers the whole
front door — `README.md`, `.claude/CLAUDE.md`, `docs/current-state.md`,
`docs/owner-queue.md`, `docs/decisions.md`, `docs/SKILLS-local.md`, the program,
the ChatGPT instructions, `session-close/SKILL.md` and every area `README.md` the
navigation work touched.

**Every entry carries the quoted text as well as the line** — resolve by the quote
and treat the number as a hint. A quote that no longer appears anywhere in its file
is the interesting case: the site was rewritten, so the finding needs re-judging
rather than re-applying.

---

## Defects — a session could act on these today and be misled

### D1. `.claude/CLAUDE.md:122` — contradiction

> **Live vs historical:** `docs/roster.md`, `control/`, `telemetry/`, `docs/prompts/` are **seat-era apparatus — historical record**, not current truth

**Claims:** The boot file's enumeration of seat-era historical apparatus is docs/roster.md, control/, telemetry/, docs/prompts/ — four items, and projects/ is not among them.

**Actually:** README.md:55-57 gives a DIFFERENT four-item set for the same concept — docs/roster.md, control/, telemetry/, projects/ — omitting docs/prompts/ where CLAUDE.md omits projects/. Both are live surfaces, each internally coherent, and neither set is complete. The asymmetry matters because .claude/CLAUDE.md is the auto-loaded boot file (README.md is only the fallback for a session where it did not load), so the normal session is never told that projects/ is historical. projects/ is 30 directories holding 27 generated seat packages whose bodies are imperative standing orders (arm a failsafe cron, keep a send_later pacemaker, delete every routine at session end) — the largest body of seat-era instruction text in the repo, and the only historical tree whose contents read as commands rather than as records. The fence exists only inside projects/README.md, one hop below where a booting session looks.

**Check it:** `cd . && grep -n -A4 'Live vs historical' .claude/CLAUDE.md && sed -n '55,57p' README.md && ls projects/ | wc -l`

**Refuter's correction:** The "both sets are incomplete, symmetrically" framing is wrong. README.md:47-49 names "Its generated roster, `control/` bus, committed trigger telemetry, project packages, and prompt registry" as records of that era — so README covers all five (docs/prompts/ in prose even though the bullet at :55-57 links only four). The asymmetry is one-way: only .claude/CLAUDE.md omits projects/. Two mitigations the finding understates: projects/README.md opens with "> **Status:** `historical`" and "must not be used to boot a session", and the single most dangerous imperative is neutralized independently — .claude/hooks/trigger_tools_guard.py hard-DENIES `delete_trigger` via permissionDecision: deny. The unguarded residue is the rest (arming failsafe crons, send_later pacemakers, account-wide list_triggers sweeps).

**Closed 2026-08-11 (fm #846):** `projects/` added to the boot file's Live-vs-historical set, aligning it with `README.md`'s historical map. Prove: ``grep -cF 'projects/`, `docs/prompts/`' .claude/CLAUDE.md`` → **1**. *(The first recorded form escaped the backticks for the bash that ran it — GNU grep reads `\`` as a buffer anchor and returns 0; Codex caught the recorded-vs-executed gap on review. The command now IS the executed string.)*

### D2. `.claude/CLAUDE.md:241` — stale-count

> Measured 2026-08-05 — seven corrections from him in one session, **all seven right, zero false positives.**

**Claims:** The boot file's owner-authority bullet still cites the superseded 'seven corrections in one session' figure as the measured evidence base for DISCOVERY RULE step 0.

**Actually:** .sessions/2026-08-05-calibration-and-602.md (this batch, lines 21-22 and 26) records that this exact number 'was wrong by roughly a factor of six' and that it was replaced in docs/CAPABILITIES.md § step 0 and docs/owner-profile.md with three independently-counted sessions. Both of those landed: CAPABILITIES.md:53-54 now reads 'The evidence base is three independent sessions... landing near 90-100 % on unhedged claims' and owner-profile.md:27-29 matches. .claude/CLAUDE.md is the ONLY file outside .sessions/ still carrying the old figure, and it is the one file every session reads unconditionally at boot. A session boots on the weaker n=1 number, and the boot file contradicts the ledger it points at. It also drops the hedge-reading rule (read the hedge; an unhedged provisioning statement is not worth checking) that the correction added and that is the operative part.

**Check it:** `cd . && grep -rlzP --include=*.md 'seven\s+corrections' . | tr '\0' '\n'; sed -n '241,242p' .claude/CLAUDE.md; sed -n '52,58p' docs/CAPABILITIES.md; sed -n '27,31p' docs/owner-profile.md`

**Refuter's correction:** The sentence is not false on its own terms — that one session genuinely had seven catches, seven correct. The accurate defect is narrower: the boot file cites the superseded n=1 figure as the evidence base for the owner-authority rule while the two ledgers it routes to carry the three-session base, and it omits the operative half the correction added (read the hedge; a hedged number is worth checking, an unhedged provisioning statement is not). Impact is on the strength of the evidence and the missing hedge rule, not on the rule's direction.

**Closed 2026-08-11 (fm #846):** the boot file now carries the three-session evidence base and the hedge-reading rule the correction added. Prove: `grep -c 'seven corrections' .claude/CLAUDE.md` → **0** · `grep -c 'hedged number is worth checking' .claude/CLAUDE.md` → **1**. *(A first version of this command grepped a phrase the fix wraps across two lines — caught by running it, which is the whole point of the column.)*

### D3. `.claude/CLAUDE.md:115` — contradiction

> `docs/playbook.md` (mixed era — R1/R2/R16/R17/R22/R24/R29/R30 still bind, the
dispatch and relay rules do not)

**Claims:** The boot file's frozen enumeration of binding playbook rules tells sessions the relay rules do not bind, which writes off R28 — the rule that carries a live, estate-general, 2026-08-05 addition.

**Actually:** R28 is titled 'ORDER/relay composition + ack-sweep hygiene' (docs/playbook.md:170), so it falls squarely inside 'the dispatch and relay rules do not [bind]'. But docs/playbook.md:177-185 carries a bullet added 2026-08-05 by the session in this batch (.sessions/2026-08-05-calibration-and-602.md:23, 48-58): repo-qualify every PR and issue number as owner/repo#N, because GitHub silently re-resolves a bare #N to the rendering repo — measured that day when the owner clicked a bare #602 and concluded merged work was done. That rule is not seat-era and applies to fleet-manager above all ('the hub, which talks about every repo'). The enumeration is also internally inconsistent: R24 is itself a relay rule ('@codex review relay', playbook.md:336) and is listed as binding, so 'the relay rules do not bind' is a one-day snapshot of which rules someone had triaged, not a property of the class. Net effect: a fix placed in the playbook to stop a recurring owner-facing failure sits in a section the boot file tells every session to skip.

**Check it:** `cd . && sed -n '115,116p' .claude/CLAUDE.md; sed -n '170,171p;177,179p;336p' docs/playbook.md`

**Refuter's correction:** The same omission exists in docs/playbook.md's own mixed-era banner (lines 6-12), which enumerates R1/R2, R16/R17, R22/R24, R29/R30 as remaining useful and likewise omits R28 — so the fix is two-file, not one, and the boot file is echoing the playbook rather than diverging from it. Strength is medium: the rule is genuinely live but the mis-classification is by omission from an enumeration plus a loose category word, not an explicit 'R28 is historical'.

**Closed 2026-08-11 (fm #846):** R28 added to both enumerations (the refuter's two-file fix — boot file and the playbook's own banner), with the category phrase narrowed to the seat-era *mechanics*. Prove: `grep -c 'R28' .claude/CLAUDE.md` → **2** (the rule list and its inline gloss) · `grep -c 'R28' docs/playbook.md` ≥ **2**.

### D4. `docs/planning/2026-07-26-consolidation-program.md:62` — contradiction

> ### ➡ NOW: **D2 — shiftlife truth pass**

**Claims:** The consolidation program's NOW pointer — the single authority the boot file and current-state.md both send every session to for 'the next actionable step' — names shiftlife as the next repository, and docs/current-state.md repeats it three times (line 40 "**shiftlife is next** in the repository order", line 176 "D2 advances to **shiftlife**", line 517 "with **shiftlife next** in its repository order").

**Actually:** Ground truth for this audit records the owner stating live on 2026-08-10 that shiftlife is NOT active, and that spider-swing and the superbot repos are the important ones. Per .claude/CLAUDE.md § Precedence the live owner outranks any stored text, so the NOW pointer and its three echoes in current-state.md are a stored ordering that one day's state froze — exactly the ranking-encodes-a-snapshot class already found once in this repo (D2's 2026-07-26 repo ordering). A session booting the read path today would open shiftlife and work a repository the owner has said is not active. I verified the repo half only (the four in-tree claims); I could not independently verify the owner's live statement from the tree — I am taking it from the audit's ground truth.

**Check it:** `cd . && grep -rn 'shiftlife' docs/current-state.md docs/planning/2026-07-26-consolidation-program.md | head -6`

**Refuter's correction:** The finding's stated uncertainty can be discharged: the owner statement is not hearsay for this audit — it is the last-but-one line of the GROUND_TRUTH block the audit harness itself pins (fm-read-r3.js:31). Scope should also include the program's line 102 D2 row, which both fixes the order and asserts D2 covers 'each active repo' — that row, not just the NOW header, is what makes shiftlife read as active.

**Closed 2026-08-11 (fm #849, recording only — the fix landed 2026-08-10, fm #840):** the headline table's row 1 is this entry's closure; the edit pass never added the entry-level paragraph, and its card's open-set enumeration listed 66 ids for "67 open" — the 101-headers-minus-34-paragraphs derivation surfaces D4 as the missing one. Prove: `git grep -n 'shiftlife truth pass' -- docs/planning/2026-07-26-consolidation-program.md docs/current-state.md` → exit **1**, no hits (name the two routing files — an unscoped sweep still matches this audit's own description of the defect and the owner queue). The decision the defect exposed stays open at `OQ-FM-D2-TARGET`.

### D5. `docs/planning/2026-07-26-consolidation-program.md:95` — broken-ref

> Method + sources: the plan doc above.

**Claims:** E1's method and source material are described in a plan document appearing earlier on this page.

**Actually:** There is no plan doc above, and no plan doc anywhere on the page. `grep -c 'final-eap-email-plan'` on the program returns 0, the phrase 'plan doc' occurs exactly once (this line), and the program contains ZERO markdown links of any kind before line 95 - the only link in the preceding block points at findings/2026-08-05-foundation-continuation.md, which is a finding, not a plan. The real plan is docs/planning/2026-07-26-final-eap-email-plan.md, which the program never names.

**Check it:** `grep -c 'final-eap-email-plan' docs/planning/2026-07-26-consolidation-program.md; head -95 docs/planning/2026-07-26-consolidation-program.md | grep -c ']('`

**Refuter's correction:** The claim "the program contains ZERO markdown links of any kind before line 95" is wrong - there are six link-carrying lines (6, 7, 38, 39, 68, 71), including one to `2026-07-26-consolidation-plan-v2.md`. The accurate statement: none of them is the EAP email plan, and no plan doc is named anywhere above the E1 row, so "the plan doc above" resolves to nothing. Same dangling reference recurs at §7 line 186 ("linked from the plan's § 2").

**Closed 2026-08-11 (fm #846):** the E1 row and the §7 fm #833 row both link the real plan. Prove: `grep -c 'final-eap-email-plan' docs/planning/2026-07-26-consolidation-program.md` → **2**.

### D6. `docs/owner-queue.md:621` — stale-count

> wake was the autonomous fleet, which closed 2026-07-21. The last generation read **21 DARK /

**Claims:** The roster's last generation read 21 DARK / 3 UNREADABLE / 0 LIVE.

**Actually:** That distribution was computed by pattern-matching and is wrong; docs/roster.md:17-19 now carries the corrected figures read off the file's own generated verdict summary — 31 rows: 18 DARK · 7 n/a · 3 STALE-BY-DESIGN · 1 STALE · 1 PRIVATE · 1 UNREADABLE · 0 LIVE — and roster.md:21-22 names "21 `DARK` / 3 `UNREADABLE`" explicitly as one of two earlier banners that got it wrong. The correcting session card (.sessions/2026-08-07-codex-caught-four.md:57) states outright that "leaving the wrong numbers in durable session history would reproduce the exact error this card documents" — yet the wrong pair survives here on a live surface. Only the 0 LIVE half is right.

**Check it:** `cd . && grep -rn '21 DARK\|21 `DARK`\|18 `DARK`' docs/owner-queue.md docs/roster.md .sessions/2026-08-07-retire-the-roster.md .sessions/2026-08-07-codex-caught-four.md`

**Refuter's correction:** Accurate as filed. Worth adding for whoever fixes it: the wrong pair sits inside a ✅ RESOLVED queue entry (OQ-FM-APPARATUS-SIZING, lines 588-608), so the fix is a one-line replacement with roster.md's generated summary — 18 DARK · 7 n/a · 3 STALE-BY-DESIGN · 1 STALE · 1 PRIVATE · 1 UNREADABLE · 0 LIVE — not a re-litigation of the entry. Note the neighbouring '18 consecutive failed runs' in the same entry is CORRECT (API-verified) and must not be 'fixed' alongside it.

**Closed 2026-08-11 (fm #846):** the site now carries the generated verdict summary's distribution, with the wrong pair quoted as retracted rather than silently replaced; the correct '18 consecutive failed runs' beside it untouched, per the refuter. Prove: `grep -c '18 DARK · 7 n/a' docs/owner-queue.md` → **1**.

### D7. `docs/owner-queue.md:357` — contradiction

> HOW: paste-ready — (1) `list_triggers` and verify BOTH ids exist enabled; (2)
  `delete_trigger trig_01XJJ88pQaQFRSpVAviCfAZe`; (3) `list_triggers` again

**Claims:** The active queue item OQ-SBW-DUP-FAILSAFE instructs a session to run `delete_trigger` as a paste-ready step, and its program-close note (lines 434-439) generalises it: "after 2026-07-22, `list_triggers` to exhaustion; if either id survives, delete it".

**Actually:** [D‑0015] (decided 2026-08-09) states a session must NEVER call delete_trigger — it is the one call that raises an owner approval prompt in automode and stalls the session. `.claude/hooks/trigger_tools_guard.py` DENIES the tool outright (DELETE_TOOL_RE + permissionDecision: deny) — the estate's only denying hook. The owner queue is read-path entry 4 and a live `living-ledger`, so a session sweeping its active items today meets a paste-ready instruction the hook will refuse and the boot file forbids. The correct remedy under current doctrine is `update_trigger enabled:false`, which this item never mentions.

**Check it:** `grep -n "delete_trigger" docs/owner-queue.md; grep -n "DELETE_TOOL_RE\|permissionDecision" .claude/hooks/trigger_tools_guard.py; grep -n "D[-]0015" -A 15 docs/decisions.md`

**Refuter's correction:** Two corrections, one narrowing and one widening. NARROWER: the item is NOT in a 'current owner decisions' section — it sits under `## Inherited cross-repo owner asks — status as recorded` (line 65), whose banner at 67-69 says 'These entries preserve their last recorded status and instructions… Re-check the owning surface before acting', and the item's own note already calls itself 'likely MOOT after 2026-07-22'. Because the hook DENIES rather than prompts, the realistic failure mode is a denied tool call and a wasted turn, not the owner-prompt stall D‑0015 guards against. WIDER: the same instruction is not confined to owner-queue.md — docs/PROJECT-CLOSEOUT.md, read-path entry 5, repeats it twice with no banner at all: §3 item 3 (line 217, 'if either id survives, delete it') and §4 Owner checklist item 1 (line 342, 'Delete any survivor'). That is the higher-value fix target.

**Closed 2026-08-11 (fm #846):** the HOW is rewritten under [D‑0015] — a session disables with `update_trigger enabled:false`; deleting is the owner's, from the console — and the refuter's higher-value targets, the two `PROJECT-CLOSEOUT.md` repetitions (§3 item 3, §4 checklist item 1), carry dated D‑0015 annotations with the records preserved. Prove: `grep -c 'delete_trigger trig' docs/owner-queue.md` → **0** · `grep -c 'D‑0015' docs/PROJECT-CLOSEOUT.md` → **2** — the pattern carries the non-breaking hyphen (U+2011) the annotations actually use, since the stamp-discipline pass converted them after this proof was first written (Codex caught the stale ASCII form on review).

### D8. `docs/owner-queue.md:560` — contradiction

> **Conditional** — only needed **if roster autogen is retained** (currently under the sizing
  review; see NEXT-TASKS.md).

**Claims:** Section (B) still lists OQ-FM-ROSTER-READ-PAT as an open owner-only secret ask whose fate is "currently under the sizing review", and points the reader at NEXT-TASKS.md for that review.

**Actually:** Two contradictions inside this same live file. (1) Line 607, in the resolved OQ-FM-APPARATUS-SIZING entry, says the 2026-08-07 owner ruling "**Moots `OQ-FM-ROSTER-READ-PAT`** — that secret was conditional on retaining roster autogen"; the roster was retired and both roster-regen cron lines removed, so the ask is dead, not conditional. (2) The pointer to NEXT-TASKS.md contradicts this file's own §Context line 14-15: "`owner-actions-2026-07-17.md` and `NEXT-TASKS.md` are seat-era records and must not be used as live action lists." A session sweeping section (B) for owner asks would surface a mooted PAT request and route the owner to a document the same file forbids.

**Check it:** `grep -n "OQ-FM-ROSTER-READ-PAT\|NEXT-TASKS.md" docs/owner-queue.md; grep -n "on:" -A 3 .github/workflows/roster-regen.yml`

**Refuter's correction:** Partial mitigation the finding omits: section (B) falls under the `## Inherited cross-repo owner asks — status as recorded` heading (line 65) whose banner says these preserve last-recorded status and must be re-checked before acting. That does not clear it — OQ-FM-ROSTER-READ-PAT is a fleet-manager secret, not a cross-repo one, so it is mis-filed under a banner that does not honestly describe it, and the moot ruling lives 66 lines below in the same file with no back-pointer.

**Closed 2026-08-11 (fm #846):** the entry is marked ☠ MOOT with the 2026-08-07 ruling cited at the site, and the forbidden NEXT-TASKS.md pointer is gone. Prove: `grep -c 'MOOT 2026-08-07 — do not create' docs/owner-queue.md` → **1**.

### D9. `docs/decisions.md:25` — contradiction

> verdict: Any session may spend `GEMINI_API_KEY_PAID` without asking — Pro-model

**Claims:** D‑0011 (status: decided, no amendment, no superseded-by) says any session may spend the paid AI Studio key without asking, with no per-call budget, and that the worst case is 'the balance reaching zero, which costs nothing beyond the €10 already spent'.

**Actually:** docs/conventions/vertex-first-for-gemini.md (Status `binding`, same date, corrected 2026-08-06) rules the opposite: 'Use Vertex. Reach for `GEMINI_API_KEY_PAID` only when Vertex has actually failed for the task in hand', and its identity table gives that route's binding constraint as 'none — and that is the problem' with measured card spend rising €0.49 → €7.88 month-to-date. The boot file follows the convention, not the ledger. Both are live surfaces, both internally coherent; D‑0011 carries no amendment row pointing at the directive, and the boot file still advertises it as 'D‑0011 the paid Gemini key is free to spend', so a session that reads the decision record acts on the un-capped, un-gated version.

**Check it:** `sed -n '21,39p' docs/decisions.md; sed -n '26,31p;119,122p' docs/conventions/vertex-first-for-gemini.md; grep -n GEMINI_API_KEY_PAID .claude/CLAUDE.md`

**Refuter's correction:** The finding understates the reach. It says 'the boot file follows the convention, not the ledger' — the boot file does BOTH: line 228 carries the Vertex-first rule and line 136 separately advertises 'D‑0011 the paid Gemini key is free to spend' with no caveat. And docs/providers/gemini.md:304 (a live provider doc, the one the doc-routing hook fires on for Gemini calls) restates 'Sessions may spend it without asking ([D‑0011])'. So the un-amended record propagates to three live surfaces, not one.

**Closed 2026-08-11 (fm #846):** D‑0011 gained an amendment field naming the Vertex-first convention as the *route* authority (budget vs route split), and both propagated surfaces — the boot file's decision-records line and `providers/gemini.md:304` — carry the caveat. Prove: `grep -cF 'amendment: **(2026-08-11)' docs/decisions.md` → **1** · `grep -c 'Vertex-first' docs/providers/gemini.md` ≥ **1**. *(The field was re-spelled to the ledger grammar after this proof was first written — the gate rejected `- amendment (date):` — and the proof lagged one edit behind; Codex caught it on review.)*

### D10. `docs/CAPABILITIES.md:125` — contradiction

> - `any` · **Tag push / release create via git**: HTTP 403 from the
  environment's git proxy → use the workflow_dispatch release path.
  — LAST-VERIFIED: 2026-07-12
- `any` · **Branch deletion**: 403 on every path (git push `:branch` and
  API) → owner deletes by hand / enables "Automatically delete

**Claims:** Under the header '## Walls — verified blocked (use the workaround; don't rediscover)', three rows assert that tag push / release creation, branch deletion, and direct api.github.com access are blocked for agents.

**Actually:** The same file's own append log declares all three false: the 2026-08-05 entry (line 775) reads 'Tag creation, GitHub Release creation and branch deletion ALL SUCCEED on the direct-PAT path — the three "Walls — verified blocked" rows above are false as written' with measured 201/201/201/204 codes, and the 2026-07-31 entry (line 888, written by .sessions/2026-07-31-false-github-api-wall.md in this batch) does the same for api.github.com. .claude/CLAUDE.md:205 independently states agents 'Merge PRs, delete branches, change settings/rulesets, create releases/secrets/tags' as normal work. The false rows carry no marker at the point of reading — the correction sits 650+ lines below under a section header that explicitly tells the reader not to re-derive. This is the exact defect class: a session that reads the Walls section inherits three refuted conclusions and stops.

**Check it:** `sed -n '123,133p' docs/CAPABILITIES.md; sed -n '775,784p' docs/CAPABILITIES.md; grep -n 'delete branches' .claude/CLAUDE.md docs/CAPABILITIES-verified-2026-07-18.md`

**Closed 2026-08-11 (fm #846):** see the headline table, row 2. Prove: `sed -n '123,146p' docs/CAPABILITIES.md | grep -c RETRACTED` → **3**. The seed-fence hazard is registered in `docs/SKILLS-local.md` § Generated-file corrections.

### D11. `docs/CAPABILITIES.md:128` — contradiction

> - `any` · **Branch deletion**: 403 on every path (git push `:branch` and

**Claims:** The ACTIVE 'Walls — verified blocked' section at the top of docs/CAPABILITIES.md (lines 122-153, inside the `substrate-kit:capability-seed` block) still lists three standing walls: tag push / release create via git (403), branch deletion (403 on every path), and '`api.github.com` direct HTTP: blocked → GitHub access is MCP-tools-only'.

**Actually:** The same file's append log, line 775, says verbatim: 'Tag creation, GitHub Release creation and branch deletion ALL SUCCEED on the direct-PAT path — the three "Walls — verified blocked" rows above are FALSE AS WRITTEN' (2026-08-05, owner-live, 201/201/204 measured). The correction was appended but never applied to the rows it names, and the rows sit ABOVE the append log — i.e. in the region a session reads first, and the only region tools/check_no_false_walls.py scans. It survives the checker because its DATED exemption ('LAST-VERIFIED: 2026-07-10') clears exactly the rows that are false. The `api.github.com` row is independently refuted by tools/check_no_false_walls.py's own NB ('Plain api.github.com is NOT blocked — direct egress answers 200 authenticated, rulesets and /actions/* included') and by .claude/CLAUDE.md's direct-PAT path. Note the rows live inside a kit-managed seed block, so a naive edit may be regenerated away — the fix has to survive `upgrade`. Out of batch b24's file list; surfaced by this batch's `check --strict` run (33 stale-wall advisories, all against this file) and verified directly.

**Check it:** `cd . && sed -n '122,133p' docs/CAPABILITIES.md; echo '--- its own refutation ---'; sed -n '775,781p' docs/CAPABILITIES.md; grep -n 'capability-seed END\|^## Append log' docs/CAPABILITIES.md`

**Refuter's correction:** One quotation detail: the finding renders line 777 as 'FALSE AS WRITTEN' in caps and calls it verbatim; the file has 'false as written' lowercase. Content unaffected. Also the cited checker NB is paraphrased — the file reads 'Plain `api.github.com` is NOT blocked — direct egress (`curl --noproxy '*'`) answers 200 authenticated, rulesets and `/actions/*` included' (lines 43-46).

**Closed 2026-08-11 (fm #846):** same fix as D10 — and this finding's upgrade warning is honoured by the re-apply registration rather than ignored. Prove: `sed -n '123,146p' docs/CAPABILITIES.md | grep -c RETRACTED` → **3**.

### D12. `docs/SKILLS-local.md:66` — contradiction

> It is generated, so **it is not corrected by hand**; it will clear at the next adopt/upgrade, and this roster is the true list until then.

**Claims:** The stale 'Fleet seed skills' section in docs/SKILLS.md is generated and will be cleared automatically by the next kit adopt/upgrade, so no hand fix is needed.

**Actually:** The next upgrade already ran (v1.20.1 -> v1.20.2, 2026-08-09, fm #833) and did not clear it — the section is still at docs/SKILLS.md:87-104 today. The upgrade's own report says why: '.substrate/upgrade-report.md' classifies `docs/SKILLS.md | consumer-edited | template unchanged — consumer-owned, nothing to apply'. This same file establishes that mechanism 73 lines later (lines 139-149: 'docs/SKILLS.md is NOT on this list ... apply_doc_improvements() writes only consumer-untouched ones'), so the file now contains both the correct mechanism and the prediction that mechanism falsifies. The practical cost is that the defect is parked forever waiting on an event that can never fire.

**Check it:** `grep -n 'docs/SKILLS.md' .substrate/upgrade-report.md ; sed -n '55,70p;139,150p' docs/SKILLS-local.md ; sed -n '87,92p' docs/SKILLS.md`

**Closed 2026-08-11 (fm #846):** the sentence now records that the promised regen can never fire (consumer-edited; `apply_doc_improvements()` writes only consumer-untouched docs) and that the section was fixed by hand. Prove: `grep -c 'Corrected by hand 2026-08-11' docs/SKILLS-local.md` → **1**.

### D13. `docs/SKILLS-local.md:68` — stale-fact

> **Neither file stated its own scope**, so a session reading one had no signal that the other half existed. Both headers now say so.

**Claims:** Both docs/SKILLS.md and docs/SKILLS-local.md now carry header text declaring which half of the skill set they cover.

**Actually:** Only one of the two does. docs/SKILLS.md's header (lines 3-8) reads 'Generated by substrate-kit. The table below renders FROM the kit's SKILLS list ... NOT SOURCE OF TRUTH for skill bodies' — it never says it covers only the kit half, never names SKILLS-local.md, and never hints that 13 local skills and 4 further kit skills exist outside its 10-row table. So the failure this paragraph declares fixed ('an index that does not state what it covers reads as complete') is still live on the file it was primarily about; the only cross-reference is a parenthetical 45 lines down in a bullet about the install loop.

**Check it:** `sed -n '1,10p' docs/SKILLS.md ; grep -c 'SKILLS-local' docs/SKILLS.md ; grep -n '^| ' docs/SKILLS.md | wc -l`

**Refuter's correction:** Directionally right; the detail to soften is that SKILLS.md is not scope-silent by accident — its '## What this is' line does say 'kit-shipped procedure' — but that is inherited template text, not an added scope declaration, and the header names no counterpart file. Low blast radius: the boot file separately points at docs/SKILLS-local.md as 'the installed roster with one line per skill', so a booted session still reaches the full list. The defect is the false self-report that the fix landed on both files.

**Closed 2026-08-11 (fm #846):** `SKILLS.md`'s header now states its scope (the kit half, 10 rows) and names `SKILLS-local.md` as the complete roster — and the false 'cannot hand-drift' claim is corrected in the same block. Prove: `grep -c 'Scope: this file covers only the' docs/SKILLS.md` → **1**.

### D14. `docs/SKILLS-local.md:105` — stale-count

> **Two kit-named skills now carry fleet-manager amendments, and both are reverted by that loop** — so **re-apply them after every upgrade**

**Claims:** Exactly two kit-named skills (`session-close`, `intake`) carry fleet-manager-local amendments that the documented `cp` loop from `.substrate/skills/` would revert, so re-applying those two after an upgrade is sufficient.

**Actually:** Seven of the 14 staged kit skills now diverge from their live `.claude/skills/` copies, and in every case the extra text is on the LIVE side — i.e. it is a local amendment at risk. Five are undocumented: `prep-owner-steps`, `release` and `scope-backlog-item` each carry the 2026-08-04 owner-ratified 'Venue note' block (10 lines apiece) that the staged copies lack, and `quality-gate` and `upgrade-distribution` each carry a local correction naming `tools/check_no_false_walls.py` where the staged copy names `bootstrap.py check --strict` twice. A session that follows this table verbatim after an upgrade re-applies two skills, silently reverts five, and reports a clean install. This is a live surface: the boot file routes kit-version work to `upgrade-distribution`, whose step 5-7 sequence lands on this loop, and `.claude/hooks/change_guard.py` check A explicitly points the author at this table as the place the amendment must be registered.

**Check it:** `cd . && for d in .substrate/skills/*/; do n=$(basename "$d"); [ -f ".claude/skills/$n/SKILL.md" ] && ! diff -q ".claude/skills/$n/SKILL.md" ".substrate/skills/$n/SKILL.md" >/dev/null && echo "DIVERGES: $n"; done; grep -n 'Two kit-named skills now carry' docs/SKILLS-local.md`

**Refuter's correction:** One supporting detail is overstated: the `cp` loop is NOT a step inside upgrade-distribution. I read that skill's live body — its eight steps are download / sha256 three-way / born-red PR / `bootstrap.py.new upgrade` / carve-out scan / verify+flip / verify merged main, and none of them mentions `.claude/skills/` or the copy loop. The exposure is one hop further out: the loop lives in docs/SKILLS-local.md:92-99 under the standing instruction at line 101, 'Re-run it after a kit upgrade' — so it is this document, not the skill, that tells a post-upgrade session to run the reverting command and then tells it only two skills need re-applying. Everything else in the finding reproduces exactly.

**Closed 2026-08-11 (fm #846):** see the headline table, row 5. Prove: `grep -c 'SEVEN kit-named skills' docs/SKILLS-local.md` → **1**.

### D15. `docs/SKILLS-local.md:44` — stale-fact

> | `quality-gate` | kit | Run the project's full verification before pushing and report what must be fixed. |

**Claims:** The roster's provenance column marks `quality-gate` (and likewise `prep-owner-steps` l.42, `release` l.47, `scope-backlog-item` l.50, `upgrade-distribution` l.53) as plain `kit` — unmodified kit-shipped skills — with `intake` (l.39) the only row flagged `kit, **fm-extended 2026-08-09**`.

**Actually:** All five of those rows describe skills whose live `.claude/` body has been locally edited away from the kit's staged body, so the column understates provenance for five of the six diverging kit skills. `quality-gate` is the sharpest case: the live copy's step 2 is `python3 tools/check_no_false_walls.py --strict` with the note '(nothing in CI runs it for you)', while the staged copy it would be overwritten from lists `python3 bootstrap.py check --strict` twice — step 1 mislabelled as 'the project's full verification (tests + lint/types)'. Reverting it deletes the skill's only pointer to the false-wall checker, which the boot file names as the guard for the estate's central rule.

**Check it:** `cd . && diff .claude/skills/quality-gate/SKILL.md .substrate/skills/quality-gate/SKILL.md; grep -n '^| `\(prep-owner-steps\|quality-gate\|release\|scope-backlog-item\|upgrade-distribution\|intake\)`' docs/SKILLS-local.md | cut -c1-90`

**Refuter's correction:** Two precision fixes. (1) The column is headed 'body', not 'provenance' — the finding's substance survives because row 39 uses that same column to record 'fm-extended', but the label should be quoted correctly. (2) The understated rows number six, not five: `session-close` at line 51 is also a bare `kit` in that column despite being the file's flagship documented amendment. It is covered by the ⚠ re-apply table at line 111, so a session reading the whole file is not misled about it — but if the claim is about the column specifically, session-close belongs in the list.

**Closed 2026-08-11 (fm #846):** all six understated rows in the body column now read `kit, fm-amended` (the refuter's set, session-close included). Prove: `grep -c 'kit, \*\*fm-amended\*\*' docs/SKILLS-local.md` → **6**.

### D16. `.claude/hooks/README.md:150` — broken-ref

> jq -e '.hooks.PreToolUse[] | select(.matcher == "Bash|WebFetch|Read|Glob|Grep")

**Claims:** This jq command schema-validates the route_docs.py hook registration in .claude/settings.json.

**Actually:** No PreToolUse block in .claude/settings.json carries the matcher "Bash|WebFetch|Read|Glob|Grep" — all three read-tool blocks now use "Bash|WebFetch|Read|Glob|Grep|Edit|Write" (the Edit|Write suffix was added when content routes landed). The command produces no output and `jq -e` exits 4, so a session running the documented verification of its own hook wiring gets a failure that looks like the hook is unregistered when it is correctly registered. This is a live how-to-verify recipe, not narrative.

**Check it:** `jq -e '.hooks.PreToolUse[] | select(.matcher == "Bash|WebFetch|Read|Glob|Grep") | .hooks[] | select(.type == "command") | .command' .claude/settings.json; echo "exit=$?"; jq -r '.hooks.PreToolUse[].matcher' .claude/settings.json`

**Closed 2026-08-11 (fm #846):** the recipe's matcher updated to the registered `Bash|WebFetch|Read|Glob|Grep|Edit|Write`, with the failure mode noted inline; the corrected command was run and exits 0 returning three registrations. Prove: run the README's step-2 jq → exit **0**.

### D17. `.claude/hooks/README.md:1` — unreachable-authority

> # Hooks — the doc-routing net

**Claims:** This file is the place that documents what each hook in .claude/hooks/ does (per .claude/CLAUDE.md:163, "What each hook does: `.claude/hooks/README.md`").

**Actually:** The README has sections for route_docs.py, owner_review.py, read_before_write.py, change_guard.py and trigger_tools_guard.py — but git_state_guard.py is not mentioned anywhere in it, not even by filename. It is a registered, live PreToolUse hook (.claude/settings.json line 44) that warns on squash-merged-branch continuation, force-pushes and `git reset --hard` with a dirty tree. A session sent here by the boot file to learn what the hooks do meets five of six and has no way to know the sixth exists, so an unexplained advisory arriving before a `git push` has no authority to resolve it against.

**Check it:** `grep -c git_state_guard .claude/hooks/README.md; ls .claude/hooks/*.py; grep -n 'git_state_guard' .claude/settings.json`

**Refuter's correction:** Accurate that the routed reference omits git_state_guard.py, but 'has no way to know the sixth exists' is overstated: docs/current-state.md:347-349 names it, links it, and gives a one-line description of all three of its checks (squash-stacked branches, force-push tree comparison, reset --hard dirty-tree listing), and docs/findings/2026-08-08-why-rules-dont-bind.md covers the incidents it was built from. The gap is specifically in .claude/hooks/README.md, the file CLAUDE.md:163 names as the hook reference.

**Closed 2026-08-11 (fm #846):** `git_state_guard.py` has its own section, written from the hook's docstring (its three checks, the advisory contract, the heredoc exclusion). Prove: `grep -c '^## .git_state_guard' .claude/hooks/README.md` → **1** — the section heading exists (the whole file had **0** mentions before).

### D18. `.claude/hooks/owner_review.py:5` — contradiction

> transcript, sends it to the owner-stand-in reviewer on Vertex, and — only when

**Claims:** The Stop hook blocks only when the reviewer returns questions; on the null path the reviewer says NO QUESTIONS and "the turn ends untouched" (lines 17-18).

**Actually:** The code always blocks. main() lines 454-461: `specifics` is set to "" when the model returns NO QUESTIONS, then `q = FIXED + (...)` and `print(json.dumps({"decision": "block", ...}))` runs unconditionally for any turn with a transcript and a reply of >=400 chars. The model is strictly additive enrichment — the file's own inline comment at lines 104-113 and .claude/hooks/README.md:275-285 both record this inversion ("the fixed question IS the hook", selective firing rated the worst of three options), but the module docstring at the top of the same file was never updated. A session debugging why the Stop hook fires every turn reads the docstring first and concludes the reviewer must be finding questions every time, when in fact the block is unconditional.

**Check it:** `sed -n '3,8p;16,19p;454,462p' .claude/hooks/owner_review.py; grep -n 'the fixed question IS the hook' .claude/hooks/README.md`

**Refuter's correction:** Also stale in the same clause: 'sends it to the owner-stand-in reviewer on Vertex' — routing was inverted 2026-08-08 to free AI Studio key first with Vertex only as the 429 fallback, which the same docstring says 27 lines further down (line 27: 'Routing, revised 2026-08-08: **free AI Studio key first, Vertex as fallback.**'). Two independent un-propagated corrections in one sentence.

**Closed 2026-08-11 (fm #846):** the module docstring now states the inversion — blocks once unconditionally, the model strictly additive, NO QUESTIONS appends nothing — matching main() and the README. Prove: `grep -c 'blocks ONCE, unconditionally' .claude/hooks/owner_review.py` → **1**.

### D19. `.claude/hooks/owner_review.py:34` — contradiction

> model for a job the small one does, and it was the only part that ever broke.

**Claims:** The Vertex/Railway/service-account auth chain was the only part of the owner-review mechanism that ever broke.

**Actually:** This exact sentence is on the record as an owner-caught error: docs/findings/2026-08-08-why-rules-dont-bind.md line 41 logs it as incident 16 ("a working capability written up as fragile"), and .claude/hooks/README.md:251 opens a paragraph titled 'Correction — "the only part that ever broke" was an overstatement'. The same file contradicts itself: _free_review's docstring at lines 355-368 says "Do not read that as 'Vertex is fragile' — it is not, and the first version of this docstring implied it", and gives the cold re-measurement (7.5 s end to end). The correction propagated to the README and to the function docstring and not to the module docstring 320 lines above it — the un-propagated-correction class that this repo built change_guard check C for.

**Check it:** `git grep -n 'only part that ever broke'; grep -n 'was an overstatement' .claude/hooks/README.md; sed -n '355,368p' .claude/hooks/owner_review.py`

**Closed 2026-08-11 (fm #846):** the overstatement is replaced by the correction with pointers to `_free_review`'s docstring and the README's Correction section (the second stale clause in the same sentence — 'reviewer on Vertex' — fell to the D18 rewrite). Prove: `grep -c 'an overstatement the estate logged' .claude/hooks/owner_review.py` → **1**.

### D20. `.claude/skills/capability-probe/SKILL.md:80` — stale-fact

> phrasing in living docs — run it yourself; nothing in CI runs it for you. A

**Claims:** tools/check_no_false_walls.py is not run by any CI workflow, so a session must run it manually or nothing checks it.

**Actually:** substrate-gate.yml line 170 runs `python3 tools/check_no_false_walls.py --strict`, and substrate-gate is a required status check on main. The boot file (.claude/CLAUDE.md:262-267) states the opposite explicitly and dates the change to 2026-08-06 — the skill inherited the pre-2026-08-06 conclusion and was never updated. A session reading this skill (which fires exactly when it is about to write a limitation) is told the gate will not catch it, so it may push wall-shaped prose expecting only a local advisory and get a red required check instead.

**Check it:** `grep -n 'check_no_false_walls' .github/workflows/substrate-gate.yml .claude/skills/capability-probe/SKILL.md .claude/CLAUDE.md`

**Closed 2026-08-11 (fm #846):** the skill now states the 2026-08-06 enforcement (required gate + local fan-out) and keeps the true residue — chat passes every guard. Prove: `grep -c 'nothing in CI runs it for you' .claude/skills/capability-probe/SKILL.md` → **0**.

### D21. `.claude/skills/quality-gate/SKILL.md:11` — stale-fact

> 2. Run `python3 tools/check_no_false_walls.py --strict` — the false-wall guard (nothing in CI runs it for you).

**Claims:** The false-wall checker is not run by CI, so a session must run it as a separate second command.

**Actually:** Wrong on both halves. CI runs it: .github/workflows/substrate-gate.yml:170 executes `python3 tools/check_no_false_walls.py --strict` in its 'repo checkers' step, and substrate-gate is the required status check on main (wired 2026-08-06; the workflow's own comment at lines 143-167 explains the carve-out). And the local step 1 above it already covers it: `bootstrap.py check --strict` fans out through scripts/preflight.py, whose line 96 runs the same checker (preflight's docstring lines 19-20 say so explicitly). This is exactly the class CLAUDE.md warns about — a written enumeration of the check list that went stale — and a session reading it concludes CI has no false-wall enforcement.

**Check it:** `grep -n "check_no_false_walls" .claude/skills/quality-gate/SKILL.md .github/workflows/substrate-gate.yml scripts/preflight.py`

**Refuter's correction:** The whole of step 2 is now redundant, not just its parenthetical — bootstrap.py check --strict fans out through scripts/preflight.py, which runs check_doc_routes.py --strict and check_no_false_walls.py --strict on the full lane. This is precisely the failure class CLAUDE.md flags: 'The check list lives in that script, not in prose here — every written enumeration of it has gone stale.'

**Closed 2026-08-11 (fm #846):** step 2 keeps the direct run as a findings-reader and corrects the coverage claim (runs in step 1's preflight fan-out AND CI's required gate). Kit-named — registered in the ⚠ re-apply table. Prove: `grep -c 'nothing in CI runs it for you' .claude/skills/quality-gate/SKILL.md` → **0**.

### D22. `.claude/skills/scope-backlog-item/SKILL.md:77` — snapshot-as-instruction

> 5. RETARGET THE BATON. Update the coordinator's Next-2 baton in `control/status.md` so the next

**Claims:** The installed scope-backlog-item skill instructs a session to write the coordinator baton into control/status.md and calls that 'the whole output'.

**Actually:** control/ is retired seat-era apparatus. control/README.md line 1: "RETIRED 2026-07-17 — autonomous apparatus wound down; historical only … do not resume the ORDER-relay or treat these files as live state." control/status.md line 1: "SEAT CLOSED — 2026-07-21T20:35Z". README.md's historical map lists control/ as explicitly historical. The skill is routed by the standing 'when no executable work is left, plan' order, so a session invoking it today is directed to write live planning state into a closed historical record — and the skill declares that step the whole point of the run, so the real output (the scoped recipe) lands nowhere current. Same text is present in the staged copy in this batch at .substrate/skills/scope-backlog-item/SKILL.md:68.

**Check it:** `sed -n '77,79p' .claude/skills/scope-backlog-item/SKILL.md; head -2 control/README.md; head -1 control/status.md`

**Closed 2026-08-11 (fm #846):** step 5 retargets the baton to the live venues (card close-out + PR description, per the skill's own 2026-08-04 venue note) and names `control/status.md` retired at the step itself. Kit-named — registered in the ⚠ re-apply table. Prove: `grep -c 'retired seat-era' .claude/skills/scope-backlog-item/SKILL.md` → **1**.

### D23. `tools/check_no_false_walls.py:80` — stale-fact

> wired into `bootstrap.py check`, so it can never jam the substrate-gate).

**Claims:** The false-walls checker is advisory-only and structurally incapable of blocking a merge; --strict is described as 'opt-in, for promotion to required later' and the header says it 'fails SAFE — advisory only, never wired into a blocking gate, so a miss or a false flag never blocks a merge. PROMOTE to a required check once it stays clean'.

**Actually:** It is already promoted. .github/workflows/substrate-gate.yml line 170 runs `python3 tools/check_no_false_walls.py --strict` inside the substrate-gate job, and the workflow's own comment eight lines above says 'substrate-gate is the REQUIRED status check on main'. --strict exits 1 on any finding, so a false positive from these best-effort text heuristics turns the required check red and blocks the merge. A session that hits a red gate and reads this docstring to triage it will conclude this checker cannot be the cause; a session weighing whether to fix a flagged line will believe it is advisory. The docstring also still describes its own reliability as 'unverified — PROMOTE once it stays clean', i.e. the promotion decision it documents as pending was taken on 2026-08-06 without updating the file.

**Check it:** `grep -n 'never jam the substrate-gate\|advisory only, never' tools/check_no_false_walls.py && grep -n 'check_no_false_walls\|REQUIRED' .github/workflows/substrate-gate.yml`

**Closed 2026-08-11 (fm #846):** see the headline table, row 6. Prove: `grep -c 'PROMOTED 2026-08-06' tools/check_no_false_walls.py` → **1** · `grep -c 'BLOCKS the merge' tools/check_no_false_walls.py` → **1**. The old wording survives only *inside quoted retractions* (`grep -n 'advisory only\|never jam' tools/check_no_false_walls.py` → 2 hits, both in "(This header said …)" / "(The prior text …)" parentheticals) — which is the correct shape: the retraction at the site, the claim gone.

### D24. `tools/check_no_false_walls.py:80` — contradiction

> wired into `bootstrap.py check`, so it can never jam the substrate-gate).

**Claims:** The checker's own SEVERITY CONTRACT and PROVENANCE state it is 'advisory only, never wired into a blocking gate, so a miss or a false flag never blocks a merge', that it is 'NOT wired into `bootstrap.py check`, so it can never jam the substrate-gate', and that `--strict` is 'opt-in, for promotion to required later' / 'PROMOTE to a required check once it stays clean'.

**Actually:** It was promoted on 2026-08-06 and the file never learned. .github/workflows/substrate-gate.yml:170 runs `python3 tools/check_no_false_walls.py --strict` in the 'repo checkers' step, and substrate-gate is THE required status check on main — the workflow's own comment at line 160 says so ('`substrate-gate` is the REQUIRED status check on main'), and .claude/CLAUDE.md confirms the promotion. So a false flag from this heuristic DOES block a merge today. Both readings are internally coherent, which is why it survived: a session hitting a red from this checker and reading its header would conclude the red is advisory and land anyway (it cannot), or would skip fixing a heuristic false positive believing it is harmless (it is not). Found while establishing why the bootstrap.py wall above is unguarded. Out of batch b24's file list, but verified directly.

**Check it:** `cd . && sed -n '26,29p;78,81p' tools/check_no_false_walls.py; grep -n 'check_no_false_walls' .github/workflows/substrate-gate.yml; sed -n '159,161p' .github/workflows/substrate-gate.yml`

**Refuter's correction:** Understated, not overstated. The finding names only substrate-gate.yml:170; the header is falsified on three independent paths — substrate-gate.yml:170 (required check), scripts/preflight.py:96 (the local `check --strict` fan-out), and bootstrap.py:24677 (engine port run inside `bootstrap.py check`). So the clause 'NOT wired into `bootstrap.py check`' is false too, not merely its consequent.

**Closed 2026-08-11 (fm #846):** the rewritten SEVERITY CONTRACT names all three enforcement paths this finding's refuter enumerated (gate · preflight · engine port). Prove: `grep -c 'scripts/preflight.py' tools/check_no_false_walls.py` ≥ **1**.

### D25. `tools/check_no_false_walls.py:27` — stale-fact

> wired into a blocking gate, so a miss or a false flag never blocks a

**Claims:** The checker 'fails SAFE — advisory only, never wired into a blocking gate, so a miss or a false flag never blocks a merge', and should be PROMOTEd to a required check later / DELETEd if it proves unreliable.

**Actually:** .github/workflows/substrate-gate.yml:170 runs `python3 tools/check_no_false_walls.py --strict`, and the surrounding comment in that same workflow states '`substrate-gate` is the REQUIRED status check on main'. .claude/CLAUDE.md says the same ('as of 2026-08-06 it is enforced for you'). The promotion the header defers to the future already happened, so a false flag DOES block a merge today. A session or reviewer trusting this header would (a) believe a red from this checker is advisory noise and (b) read 'DELETE this if it proves unreliable' (line 29) as licence to remove a script that main's required gate now invokes.

**Check it:** `sed -n '26,29p' tools/check_no_false_walls.py; grep -n 'check_no_false_walls' .github/workflows/substrate-gate.yml; grep -n 'REQUIRED status check on main' .github/workflows/substrate-gate.yml`

**Closed 2026-08-11 (fm #846):** the 'DELETE this if unreliable' licence is replaced with 'Do NOT delete this script — main's required check invokes it'. Prove: `grep -c 'Do NOT delete this script' tools/check_no_false_walls.py` → **1**.

### D26. `tools/gemini_delegate.py:63` — contradiction

> # not the AI Studio key, which spends the owner's card. Vertex is therefore the

**Claims:** Vertex spends pre-paid credit while 'the AI Studio key' spends the owner's card — stated in the singular, in the header of the tool a session is about to run.

**Actually:** docs/conventions/vertex-first-for-gemini.md was explicitly corrected on 2026-08-06 for exactly this singular collapse: 'Note "the AI Studio key" is two keys — GEMINI_API_KEY is free tier and costs nothing', and its § 'Two identities, three billing outcomes' records the cost of the old wording — 'a session reading either this doc or the boot file learned only "AI Studio spends the owner's card" and avoided the whole surface — including the free one.' .claude/CLAUDE.md agrees (GEMINI_API_KEY is free tier; only GEMINI_API_KEY_PAID bills the card). This tool reads GEMINI_API_KEY — the free key — so its own header tells a session that its own default path bills the owner. The correction landed in the convention doc and never propagated here; the same wording is repeated in the --studio help text at line 424-426.

**Check it:** `sed -n '60,67p' tools/gemini_delegate.py; grep -n 'GEMINI_API_KEY' tools/gemini_delegate.py; sed -n '6,12p;26,31p' docs/conventions/vertex-first-for-gemini.md`

**Refuter's correction:** The repeated wording is in the --vertex-sa help at line 419, not the --studio help at 424-426. Mitigating context the finding omits: line 4 of the same docstring already calls GEMINI_API_KEY "free-tier", so the file contradicts itself rather than being uniformly wrong.

**Closed 2026-08-11 (fm #846):** header and `--vertex-sa` help now carry the two-key truth — `GEMINI_API_KEY` is the free tier; only `GEMINI_API_KEY_PAID` bills the card, and this tool never reads it. Prove: `grep -c 'AI Studio key, which spends' tools/gemini_delegate.py` → **0**.

### D27. `tools/gemini_delegate.py:64` — contradiction

> # DEFAULT here; `--studio` is the opt-out and must be justified in the session

**Claims:** Vertex is the DEFAULT route in this tool and `--studio` is the explicit opt-out that must be justified in the session card.

**Actually:** The code makes Studio the default and --studio a no-op. main() gates Vertex on `if args.vertex_sa and not args.studio:` (line 429), so with no flags — the shape of every usage example in this same docstring, lines 26-30 — _VERTEX stays empty and _url() returns https://generativelanguage.googleapis.com/v1beta/models/<m>:<verb>?key=$GEMINI_API_KEY. Passing --studio alone changes nothing. A session that runs the documented command believes it is on the pre-paid Vertex credit and is silently on the AI Studio path, with no warning and nothing to justify in the card. Combined with the line-63 billing error, the tool both mislabels which key costs money and mislabels which path it takes by default.

**Check it:** `grep -n 'if args.vertex_sa' tools/gemini_delegate.py; GEMINI_API_KEY=DUMMY python3 -c "import importlib.util;spec=importlib.util.spec_from_file_location('gd','tools/gemini_delegate.py');m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);print(m._url('gemini-3.6-flash','generateContent'));print('_VERTEX empty?',m._VERTEX=={})"`

**Refuter's correction:** The billing consequence is smaller than the finding implies: silently landing on generativelanguage with GEMINI_API_KEY costs nobody anything (the free key). The real harm is a session believing it is on Vertex when it is on the free tier — wrong session-card record, and it hits the ~20/day RPD cliff with no explanation.

**Closed 2026-08-11 (fm #846) — doc matched to code, deliberately not code to doc:** the header and both help strings now state the real no-flag default (free Studio path; Vertex only with `--vertex-sa`; `--studio` alone a no-op). Silently flipping the default instead would change callers' billing route unasked — the wrong-direction fix for a description defect. Prove: `grep -c 'no-flag default is the free Studio path' tools/gemini_delegate.py` → **1**.

### D28. `tools/install_root_hooks.py:60` — stale-count

> # it, which left the rescue path rescuing three hooks out of four.

**Claims:** The rescue script's HOOKS table is the complete set of hooks this repo installs — four of them — and line 24 asserts the repo-local .claude/settings.json 'already carries the same registration'.

**Actually:** There are SIX hook scripts in .claude/hooks/ and .claude/settings.json registers all six across 5 event/matcher slots. The HOOKS table names only route_docs.py, read_before_write.py, git_state_guard.py and trigger_tools_guard.py. change_guard.py (PreToolUse Write|Edit|MultiEdit AND PostToolUse Edit|MultiEdit) and owner_review.py (Stop) are absent, so the rescue path restores 4 of 6 — and the two it misses are the change guard and the Stop gate that .claude/CLAUDE.md describes as 'The Stop hook reviews the reply you are about to send, and blocks once'. .claude/CLAUDE.md sends a multi-root session here with 'run python3 tools/install_root_hooks.py --apply before trusting any gate', and it prints a clean 'installed' with no signal that two hooks were skipped — the exact silent half-install the merge() docstring says it was table-driven to prevent. This is the same 'four vs six' class as the already-fixed '5 hooks' doc count, still live in the tool.

**Check it:** `diff <(ls .claude/hooks/*.py | xargs -n1 basename | sort) <(grep -oP '^\s{4}"\K[a-z_]+\.py' tools/install_root_hooks.py | sort)`

**Refuter's correction:** 'registers all six across 5 event/matcher slots' is imprecise — .claude/settings.json holds 8 hook registrations across 4 event types (PreToolUse ×5 for route_docs/read_before_write/git_state_guard/change_guard/trigger_tools_guard, Stop ×1 owner_review, UserPromptSubmit ×1 route_docs, PostToolUse ×1 change_guard). The substance is unchanged: the rescue table restores 4 of 6 scripts and 6 of 8 registrations, silently.

**Closed 2026-08-11 (fm #846):** `change_guard.py` (PreToolUse Write|Edit|MultiEdit + PostToolUse Edit|MultiEdit) and `owner_review.py` (Stop) added to the HOOKS table, with per-hook timeouts so the rescued Stop hook keeps its 120s instead of dying at the 10s default; dry-run verified in a scratch root — 6 hooks, 8 registrations. Prove: this finding's own Check-it diff → empty, exit **0**.

### D29. `scripts/check_docs_links.py:99` — other

> SCAN_DIRS = ("docs", "projects", "environments", "registry", "templates")

**Claims:** The S5 link-drift checker sweeps the repo's living markdown surfaces for dead intra-repo links.

**Actually:** Its scan set is docs/ + projects/ + environments/ + registry/ + templates/ + root *.md + control/README.md. It never scans .claude/ - so neither the boot file .claude/CLAUDE.md nor any of the 27 installed skills is link-checked, and those are the surfaces that actually bind a session at the moment of action. This is why the session-close broken link above survived; the checker exits 0 with it present. The mechanism gap, not the single link, is the finding.

**Check it:** `grep -n 'SCAN_DIRS\|CONTROL_FILES' scripts/check_docs_links.py; python3 scripts/check_docs_links.py --list`

**Refuter's correction:** The causal sentence is overstated. `check_docs_links.py` is advisory and standalone - its own docstring says "not wired into `bootstrap.py check`", and grep confirms it appears in no workflow (`substrate-gate.yml`'s repo-checkers step runs only `tools/check_doc_routes.py --strict` and `tools/check_no_false_walls.py --strict`; the only YAML hit is a test fixture). So adding `.claude` to SCAN_DIRS would not by itself have red-flagged the session-close link in CI - the gap is two-part: no `.claude` coverage AND no CI wiring. Also, `.claude/` currently holds no real dead links.

**Closed 2026-08-11 (fm #846):** see the headline table, row 7 — `.claude` scanned (29 files), two checker defects the new surface exposed fixed with selftest cases, full run CLEAN exit 0. The refuter's CI-wiring half is recorded as still open: the checker remains advisory + standalone by its spec; wiring it into a gate is a policy change nobody has asked for.

### D30. `scripts/check_owner_queue.py:156` — stale-fact

> active = line.lower().startswith("## active")

**Claims:** The checker's active-region parser assumes docs/owner-queue.md has a `## Active …` heading whose bullets carry inline `OQ-…` slugs (module comment lines 108-110: "Active items are now bullets carrying an inline `OQ-…` slug (2026-07-17 wind-down slim), grouped under ### (A)–(G)").

**Actually:** docs/owner-queue.md has had no `## Active` heading since the 2026-07-21 program-closed restructure — its headings are `## Context`, `## Program closed…`, `## Current owner decisions…`, `## Inherited cross-repo owner asks…`, then dated `## Resolved …` sections. The parser therefore never enters an active region, parses ZERO items, and the checker fires its own `FLAG [no-items] … format drift or wrong file` and exits 1. Every one of its four checks (merged-citation drift, slug discipline, dirty-parked PR, satisfied required-check ask) is dead against the real queue while the script still presents itself as the queue's guard. The ~100 OQ- slugs in the live file are unchecked.

**Check it:** `cd . && grep -n '^## ' docs/owner-queue.md | head -5; python3 scripts/check_owner_queue.py --skip-positional-lint; echo "REAL_EXIT=$?"`

**Refuter's correction:** '~100 OQ- slugs' is 94 unique slugs by enumeration. One blast-radius nuance the finding omits: the only automated caller is .github/workflows/roster-regen.yml:171 (`python3 scripts/check_owner_queue.py --advisory`), and that workflow lost both cron lines on 2026-08-07, so the dead parser is not currently failing any scheduled run — it misleads a human or session who invokes it directly, or who reads projects/fleet-manager/coordinator-prompt.md:38 naming it as the queue's verify step.

**Closed 2026-08-11 (fm #849):** the module comment now states the parser is dead against the current queue — the `## Active…` heading died in the 2026-07-21 restructure, zero items parse, and the `[no-items]` FLAG is the format mismatch announcing itself — and names the parser rebuild as open work, deliberately not claimed. Prove: `grep -c 'STALE PARSER (recorded 2026-08-11' scripts/check_owner_queue.py` → **1**.

### D31. `scripts/check_owner_queue.py:67` — stale-fact

> In agent sessions api.github.com is proxy-walled (403) and there is no HTML fallback for rules — the probe degrades honestly to NOT MEASURED; the Actions regen run is the reliable venue for this check.

**Claims:** Check 4 (satisfied required-check asks) cannot be measured from an agent session, and the scheduled roster-regen Actions run is the venue that does measure it.

**Actually:** Two halves, both stale. (a) The exact endpoint this paragraph declares unreachable — GET /repos/menno420/<repo>/rules/branches/main — returns HTTP 200 from this session over direct egress with $GITHUB_PAT (`curl --noproxy '*'`), the path .claude/CLAUDE.md documents as MEASURED. The 403 is a proxy-path quirk, not a wall, and the script writes the wall down instead of routing around it (urllib honours the proxy env by default). (b) The named "reliable venue" no longer runs unattended: roster-regen.yml was retired 2026-08-07 with BOTH cron lines removed, leaving only workflow_dispatch — so nothing fires this check on a schedule any more. A session reading this defers a probe it can run in one command to a workflow that never wakes.

**Check it:** `cd . && curl -s --noproxy '*' -o /dev/null -w 'direct_egress_rules_api=%{http_code}\n' -H "Authorization: Bearer $GITHUB_PAT" -H 'Accept: application/vnd.github+json' https://api.github.com/repos/menno420/fleet-manager/rules/branches/main; grep -c 'cron:' .github/workflows/roster-regen.yml; grep -n 'RETIRED 2026-08-07' .github/workflows/roster-regen.yml`

**Refuter's correction:** The line anchor is off by one: the quoted paragraph begins at line 67 ('In agent sessions api.github.com is proxy-walled (403) and there is no'), not line 66 — line 66 is 'menno420/<repo> reference in the item, else note-skip (never guessed).' Everything else in the finding holds verbatim across lines 67-69.

**Closed 2026-08-11 (fm #849):** the 403 wall is replaced with the measured truth — proxied path 403s, direct egress with the PAT answers 200 — plus the honest urllib caveat, and the "reliable venue" clause now records that the Actions regen lost both crons 2026-08-07. Prove: `grep -c 'direct egress with $GITHUB_PAT answers 200' scripts/check_owner_queue.py` → **1**.

### D32. `scripts/check_roster_freshness.py:38` — contradiction

> - roster-freshness workflow (PRs): BLOCKING on manager-authored (claude/*) branches, ADVISORY elsewhere — a lane/owner PR must never be jammed by the manager's own stale roster. The workflow passes --advisory for the non-blocking lane

**Claims:** The script's SEVERITY CONTRACT states its two consumers: roster-regen runs it as a blocking self-check after each regeneration, and roster-freshness gates pull requests, blocking on claude/* and passing --advisory elsewhere.

**Actually:** Both consumers were retired 2026-08-07 and the workflow files say so, so the two documents are each internally coherent and disagree. .github/workflows/roster-freshness.yml now carries a `RETIRED 2026-08-07 (owner directive)` banner, its `on:` block is `workflow_dispatch:` only (the `pull_request` trigger is gone), and its single run step invokes `python3 scripts/check_roster_freshness.py` with NO `--advisory` and no branch conditional — deliberately unconditionally blocking, the inverse of the contract quoted here. roster-regen.yml is likewise workflow_dispatch-only. A session reading this script believes a PR gate exists that does not, and believes an advisory lane exists that was removed.

**Check it:** `cd . && grep -n 'RETIRED\|^on:\|workflow_dispatch\|pull_request\|advisory\|check_roster_freshness' .github/workflows/roster-freshness.yml`

**Refuter's correction:** Impact is narrower than "a session believes a PR gate exists" implies: the workflow files themselves carry loud retirement banners, so anyone who opens the workflow learns the truth within one hop. The defect is the asymmetry — the two workflows were bannered on 2026-08-07 and the script's SEVERITY CONTRACT prose describing them was not.

**Closed 2026-08-11 (fm #849):** the SEVERITY CONTRACT now opens with the retired-consumers reality (both workflows retired 2026-08-07; no --advisory lane exists; RED is the designed state) and keeps the seat-era contract as quoted record. Prove: `grep -c 'RETIRED CONSUMERS (2026-08-11' scripts/check_roster_freshness.py` → **1**.

### D33. `scripts/check_roster_freshness.py:360` — stale-fact

> "Fix: check .github/workflows/roster-regen.yml runs (cron " "40 */2 * * *) — a dead cron here is the single-point-of-" "freshness failing; regenerate via scripts/gen_roster.py

**Claims:** The RED remedy text tells the reader the roster went stale because the `40 */2 * * *` cron in roster-regen.yml died, and that the fix is to regenerate the roster.

**Actually:** The cron was removed on purpose by owner directive on 2026-08-07 ("Yes retire the roster, I don't need it"), and docs/roster.md itself now opens with `⛔ RETIRED 2026-08-07 … Do not read the rows below as the state of anything.` The checker is therefore permanently RED (real exit 1, roster 100.6h old at audit time) and sends the reader hunting a scheduler fault that is actually a deliberate retirement. The same single run contradicts itself: three lines above the remedy it prints `REGEN WINDOWS: not measured — no \`- cron:\` schedule line found in .github/workflows/roster-regen.yml`, i.e. the script observes the cron is gone and then blames it for dying.

**Check it:** `cd . && python3 scripts/check_roster_freshness.py; echo "REAL_EXIT=$?"; head -3 docs/roster.md`

**Refuter's correction:** Two details to tighten. (a) The age is 100.8h at my run, not 100.6h — it grows, and the generated-at stamp is 2026-08-06T14:57Z (the day before retirement), not the retirement date. (b) The blast radius is smaller than "permanently RED" suggests operationally: the script is NOT in the local gate — `scripts/preflight.py` contains no reference to 'roster' at all, so `bootstrap.py check --strict` is unaffected. It reds only on a hand run or a `workflow_dispatch`. The instruction that sends you to run it (telemetry/README.md:52, "must exit 0") lives in telemetry/, which the boot file already classifies as seat-era historical.

**Closed 2026-08-11 (fm #849):** the RED remedy now states the retirement was deliberate, that the RED is permanent by design, and that a regen would overwrite docs/roster.md's RETIRED banner — the seat-era fix text preserved as a quoted parenthetical. Prove: `grep -c 'designed permanent' scripts/check_roster_freshness.py` → **1**.

### D34. `scripts/check_trigger_health.py:476` — contradiction

> f"(keep `{p['ticks'][-1]['id']}`, delete the rest); "

**Claims:** The I7 TICK-PILE-UP remedy string this live script prints instructs the reading session to delete triggers ('REMEDY: prune to the NEWEST tick (keep `X`, delete the rest)'); the I8 DUPLICATE-CRON remedy at line 517 likewise says 'the owning seat (or hub) deletes them'.

**Actually:** D‑0015 (docs/decisions.md:131, dated 2026-08-09, status decided) is the live rule that 'A session must never call `delete_trigger`', and .claude/hooks/trigger_tools_guard.py DENIES the tool outright — the estate's only denying hook. The emergency stop is `update_trigger` with `enabled: false`. The script is in scripts/ (a live 20-entry directory), carries no historical banner, contains no reference to D‑0015 or to disabling, and its remedy text is the exact instruction the hook exists to block. A session that runs it and follows the printed remedy either trips the deny or routes to the direct-API path (which only warns) and stalls the owner on an approval prompt. This is the seat-era prune-list doctrine (visible verbatim in .sessions/2026-07-13-night-watchdog-1/2/3.md) still baked into a live executable.

**Check it:** `grep -n 'delete the rest\|deletes them' scripts/check_trigger_health.py; grep -n 'D[-]0015\|update_trigger\|enabled: false' scripts/check_trigger_health.py; sed -n '131,136p' docs/decisions.md; grep -n 'delete_trigger.*DENY\|permissionDecision' .claude/hooks/trigger_tools_guard.py`

**Refuter's correction:** Two details need tightening. The consequence is milder than stated: the MCP tool call is denied outright by the hook (trigger_tools_guard.py:84 DELETE_TOOL_RE, :315 return deny), so a session following the remedy is blocked, not stalled — only the direct-API route warns rather than blocks, and that is the sole stall path. Second, no live surface routes to this script: its referrers are docs/playbook.md:83/112 (R26, which the playbook's own 2026-08-10 banner consigns to the historical column), telemetry/README.md:46, control/inbox.md, and projects/fleet-manager/coordinator-prompt.md — all bannered or boot-file-classified historical. That lowers the exposure but does not remove it, since the script itself carries no banner and sits in scripts/ beside checkers preflight.py does use.

**Closed 2026-08-11 (fm #849):** both remedy strings now disable per [D‑0015] (`update_trigger enabled:false`; deleting is owner-console work) and record to the session card instead of the retired heartbeat; the selfcheck assertion that pinned the old "prune…delete" wording is updated to pin the new remedy. Prove: `python3 scripts/check_trigger_health.py --selfcheck` → exit **0** (`selfcheck: PASS`) · `grep -c 'delete the rest' scripts/check_trigger_health.py` → **0**.

### D35. `scripts/check_trigger_health.py:150` — snapshot-as-instruction

> WAKE PROCEDURE (playbook R26): export list_triggers (ALL pages) → telemetry/triggers-snapshot.json with top-level `captured_at` → run this script → act on FAILs same wake

**Claims:** A standing, imperative per-wake procedure: every manager wake must export the trigger registry, run this checker, and act on FAILs in the same wake — cited as binding playbook rule R26.

**Actually:** There are no manager wakes: the autonomous-Projects program closed 2026-07-21 and the fleet-manager coordinator seat closed with it (control/status.md line 1: `SEAT CLOSED — 2026-07-21T20:35Z`). The rule it cites is also not live — .claude/CLAUDE.md enumerates the playbook rules that still bind as R1/R2/R16/R17/R22/R24/R29/R30, and R26 is not among them. Concretely the instruction is now unfollowable and self-defeating: run today the checker evaluates a snapshot frozen at 2026-07-21T16:00Z, reports I5 ROSTER-FRESH FAIL and I6 SNAPSHOT-FRESH FAIL (483.6h stale), exits 1, and prints `VERDICT: FAIL — 2/9 invariant(s) red. Act SAME WAKE…` plus an I8 WARN about a July seat duplicate. Unlike docs/roster.md and control/, this script carries no historical banner, so it reads as live tooling.

**Check it:** `cd . && timeout 120 python3 scripts/check_trigger_health.py > /tmp/th.txt 2>&1; echo "REAL_EXIT=$?"; grep -n 'I5 ROSTER-FRESH\|I6 SNAPSHOT-FRESH\|VERDICT' /tmp/th.txt; grep -n 'R1/R2/R16' .claude/CLAUDE.md; head -1 control/status.md`

**Closed 2026-08-11 (fm #849):** the docstring gains an ERA NOTE (no manager wakes; snapshot frozen 2026-07-21; I5/I6 FAIL by design) and the WAKE PROCEDURE header names R26 HISTORICAL at the site. Prove: `grep -c 'HISTORICAL, see the era note at top' scripts/check_trigger_health.py` → **1**.

### D36. `scripts/gen_idea_backlog.py:66` — other

> BULLET_RE = re.compile(r"^- (?:\*\*)?" + MARKER)

**Claims:** The harvester that produces docs/planning/idea-backlog.md finds every session-card 💡 idea, so the backlog is the machine-built candidate list every groom can start from (per the script's own PROVENANCE header).

**Actually:** BULLET_RE only matches a 💡 at the start of a top-level list item ('- 💡' / '- **💡'). Across .sessions/, 116 cards use the '## …💡' HEADING form and only 57 use the bullet form the regex accepts. The docstring discloses that 'Inline 💡 mentions mid-prose are NOT harvested' but never says the heading form — the majority convention — is also invisible, so the generated '4 ungroomed' figure reads as a measurement of the corpus when it is a measurement of one minority formatting style.

**Check it:** `cd . && sed -n '66p' scripts/gen_idea_backlog.py && echo -n 'heading-form cards: ' && grep -l '^#\{1,4\} .*💡' .sessions/*.md | wc -l && echo -n 'bullet-form cards: ' && grep -lE '^\s*-\s+(\*\*)?💡' .sessions/*.md | wc -l`

**Refuter's correction:** The docstring is less silent than the finding allows — lines 39-41 do say 'top-level bullets' and give the two accepted forms, which by exclusion covers the heading case. The defect is better stated as a mismatch between the script's honest narrow contract and the two surfaces that advertise it as complete: docs/planning/README.md:18 ('every `.sessions/*.md` card 💡 idea', 'grooming passes start here') and the generated file's own '57 idea block(s) across 345 card(s)' summary line. Also add the paragraph-start form to the tally: 115 cards are heading-only and 170 more are paragraph-start-only, for 285 structured idea markers missed versus 57 harvested.

**Closed 2026-08-11 (fm #849):** the generator's emitted header and its docstring now disclose the bullet-form-only harvest scope — the heading and paragraph forms most cards use are not harvested, so the counts are a floor over one formatting style, never a corpus measurement. The description was fixed rather than the regex widened: extending the harvest is a behavior change nobody asked for, and the honest scope line is what the two advertising surfaces lacked (`docs/planning/README.md`'s row is corrected the same way). Prove: `grep -c 'Harvest scope is the BULLET form only' scripts/gen_idea_backlog.py` → **1** · `python3 scripts/gen_idea_backlog.py --selfcheck` → exit **0**.

### D37. `scripts/gen_kit_versions.py:131` — snapshot-as-instruction

> " INC-42 / central-docs-plan C4). Regenerate with every manager wake"

**Claims:** The generator stamps its output `> **Status:** `living-ledger`` and states its only regeneration trigger: "Regenerate with every manager wake that touches kit state", with a kill-switch that the table must be re-derived if generated-at goes stale >7d.

**Actually:** Manager wakes ended with the program on 2026-07-21, so the sole stated regeneration trigger can never fire again and nothing else invokes this script (it is not in scripts/preflight.py, bootstrap check, or any of the four workflows). The consequence is live on disk: registry/kit-versions.md still carries the `living-ledger` badge while stamped `generated-at **2026-07-14T04:49Z**`, declares "newest fleet tree version measured: **v1.15.0**", and rates fleet-manager `v1.15.0 … CURRENT (= newest fleet tree)` — but substrate.config.json and .substrate/state.json both read kit_version 1.20.2. Its own >7d kill-switch has been blown by 27 days without anyone tripping it, so a session consulting the ledger for fleet kit state is told v1.15.0 is current.

**Check it:** `cd . && sed -n '3,7p' registry/kit-versions.md; grep -n 'fleet-manager |' registry/kit-versions.md; python3 -c "import json;print('config',json.load(open('substrate.config.json'))['kit_version'],'state',json.load(open('.substrate/state.json'))['kit_version'])"; grep -rn 'gen_kit_versions' scripts/preflight.py .github/workflows/ | wc -l`

**Closed 2026-08-11 (fm #849):** the emitted regen-trigger line no longer names manager wakes — "Regenerate on demand", with the seat-era wording quoted as record, and the emitted Status downgraded from `living-ledger` to a dated `reference` snapshot. Prove: `grep -c 'Regenerate on demand' scripts/gen_kit_versions.py` → **1**.

### D38. `scripts/gen_roster.py:155` — snapshot-as-instruction

> scripts/check_roster_freshness.py is a REQUIRED wake step, not a commit-only-on-change option.

**Claims:** Regenerating the roster and getting check_roster_freshness.py green is a standing REQUIRED step of every session/wake.

**Actually:** The roster was retired 2026-08-07 by owner directive. docs/roster.md carries a '⛔ RETIRED 2026-08-07' banner, roster-freshness.yml carries a 'RETIRED 2026-08-07 (owner directive)' banner and its pull_request trigger is removed, and the 'manager wake' this imperative binds to ended when the autonomous-Projects program closed 2026-07-21. Every other file in the roster chain got an era banner on 2026-08-07; scripts/gen_roster.py alone did not (grep -ci for retired/historical returns 2 hits, both about the retired 'hub' disposition, not the file's era). A session reading this script — the only unbannered surface in that chain — is told a retired regen is a required step it must perform.

**Check it:** `grep -n 'REQUIRED wake step' scripts/gen_roster.py; grep -n 'RETIRED 2026-08-07' docs/roster.md .github/workflows/roster-freshness.yml; grep -ni 'retired\|historical' scripts/gen_roster.py`

**Refuter's correction:** Two details to tighten: the quote spans lines 155-156, not line 155 alone. And the finding understates the consequence — because ROSTER_REL is docs/roster.md and gen_roster regenerates the file, obeying the imperative would overwrite the ⛔ RETIRED banner, not merely waste a step. The script is also still named as live in project.index.json's `verification` list (`python3 scripts/gen_roster.py --selfcheck`) and in registry/README.md as the source of truth for registry/lanes.json, so it is genuinely reachable.

**Closed 2026-08-11 (fm #849):** docstring ERA NOTE added — roster retired 2026-08-07, nothing schedules this script, and (the refuter's point) **a regen overwrites the hand-applied RETIRED banners** on all three outputs; the "REQUIRED wake step" imperative is re-tensed to seat-era record at its site. Prove: `grep -c 'ERA NOTE (2026-08-11, audit D38)' scripts/gen_roster.py` → **1**.

### D39. `.github/workflows/merge-on-green.yml:40` — contradiction

> # required-check enforcement state is unverified (the rules API

**Claims:** This repo's required-check enforcement state is unverified because the rules API reported ZERO required contexts live (PR #146, run 29214147939, dated 2026-07-12).

**Actually:** Contradicted three ways, including by the same file. Line 82 of merge-on-green.yml itself says 'substrate-gate is the sole required check and the real signal'; roster-freshness.yml:31 says 'substrate-gate is the sole required check on main, verified from the rulesets API'; and .claude/CLAUDE.md:266 records substrate-gate as a required status check under the active main-branch-protection ruleset, plus an explicit MEASURED 2026-08-06 note that the rulesets API reads fine agent-side and that the 'enforcement-required-unverified' claim must never be quoted. A 2026-07-12 probe result written in the present tense is now a false wall sitting in a live workflow header. (I did not re-probe the live rulesets API this session; the contradiction is established entirely from the tree.)

**Check it:** `grep -n "required-check enforcement state is unverified\|sole required check\|required status check" .github/workflows/merge-on-green.yml .github/workflows/roster-freshness.yml .claude/CLAUDE.md`

**Refuter's correction:** Only the stated rationale is stale, not the design: generic head-SHA check verification ('trusts what actually ran, never a rules count') remains correct and should not be changed — the fix is to re-date or replace the 'enforcement state is unverified' clause, not to make the workflow read the rules count. Note also that the same header carries a second present-tense limitation at lines 7-8, 'This repo CANNOT use GitHub-native auto-merge (toggle unavailable on the private repo/plan)', which is the same class and was not flagged.

**Closed 2026-08-11 (fm #849):** the header rationale is re-dated — substrate-gate has been a required check under the active ruleset since 2026-08-06, MEASURED agent-side — while the generic trusts-what-ran design is kept exactly as the refuter directed. The lines-7-8 native-auto-merge clause stands: the program's C2 row treats it as true for this private-repo plan, and nothing measured contradicts it. Prove: `grep -c 'substrate-gate IS a required' .github/workflows/merge-on-green.yml` → **1**.

### D40. `.sessions/2026-07-10-universal-permissions-block.md:3` — contradiction

> > **Status:** `in-progress`

**Claims:** This session card declares itself in-progress — i.e. an unfinished, in-flight session.

**Actually:** The card's own line 22 closure note ('superseded by PR #76 … this card merged stuck at in-progress via #47 and is grandfathered') says the session is closed, so the badge contradicts the body. It is the only one of 344 cards carrying a non-terminal Status. 'Grandfathered' was a 2026-07-11 judgement that every session since has inherited rather than re-derived, and by 2026-08-09 it had cost a hand carve-out in the repo's required status check — a standing re-apply obligation on a kit-owned generated file, where flipping one token on an inert historical card would remove the cause.

**Check it:** `cd . && grep -rl '^> \*\*Status:\*\* `in-progress`' .sessions/ && sed -n '3p;22p' .sessions/2026-07-10-universal-permissions-block.md && grep -n 'universal-permissions-block\|__no-card-in-diff__' .github/workflows/substrate-gate.yml`

**Closed 2026-08-11 (fm #849):** the badge is flipped `in-progress` → `complete` with a dated note quoting the card's own closure line — the last non-terminal Status among 344 cards. Lane-safe: preflight's added-card lane selects only cards ADDED vs origin/main, and this is a modification. The gate's `--session-log` sentinel carve-out stays as defense-in-depth (mtime selection is still arbitrary); its comment's "this repo still carries…" rationale clause is now historical, which the re-apply table's kit-side durable fix will absorb. Prove: `sed -n '3p' .sessions/2026-07-10-universal-permissions-block.md` → contains `` `complete` ``.

### D41. `.substrate/agents/architect.md:12` — snapshot-as-instruction

> docs/ (playbook, owner-queue, dispatch-log — manager working memory) + templates/ (worker preamble blocks) + control/ (protocol heartbeat: owner-written inbox.md, manager-written status.md)

**Claims:** fleet-manager's binding architecture is the seat-era control bus: control/inbox.md is the owner's live write path, control/status.md is 'overwritten by the manager each working session' (line 14), and ownership violations are to be flagged against that model.

**Actually:** control/ has been RETIRED since 2026-07-17 — control/README.md line 1 reads '**RETIRED 2026-07-17 — autonomous apparatus wound down; historical only.**' and explicitly says 'do **not** … treat these files as live state'. Neither control/inbox.md nor control/status.md has been touched by a human writer since 2026-08-06, and then only by the automated roster-regen that was itself retired 2026-08-07. This persona is a standing instruction ('Flag every layer-boundary or ownership violation with file:line and the rule it breaks') written against apparatus that no longer exists, and unlike docs/roster.md, control/, telemetry/ and docs/prompts/ it carries no era banner and appears on no historical list in .claude/CLAUDE.md. Mitigation that a reader should weigh: .claude/agents/ does not exist, so Claude Code does not auto-load this file today — the harm requires a session to read or install the staged persona.

**Check it:** `head -6 control/README.md; git log -1 --format='%ad %s' -- control/status.md; ls -d .claude/agents 2>&1; grep -rn -i 'historical|retired|seat' .substrate/agents/`

**Refuter's correction:** The persona file is a symptom, not the source, and the finding understates reach. The text is rendered verbatim from .substrate/state.json slot_values Q-004 `architecture_layers` and Q-009 `mutation_seam` (bootstrap.py cmd_agents renders persona bodies from those slots), so `bootstrap.py agents --build` regenerates the same stale text — fixing only the .md leaves the defect armed. More importantly the identical seat-era sentences are already planted in LIVE docs that carry '> **Status:** `binding`' and no era banner: docs/architecture.md (Layers section) and docs/ownership.md:15. Those are far more reachable than the staged persona, and are where the defect should be fixed. The 'touched only by roster-regen since 2026-08-06' claim is weakened by the clone being shallow (57 commits, .git/shallow present, floor commit dfccceb 2026-08-06) — the correct statement is 'no commit touches control/ after the shallow floor'.

**Closed 2026-08-11 (fm #849):** fixed at the root the refuter named — the `architecture_layers` slot corrected via `bootstrap.py answer` and the personas regenerated with `bootstrap.py agents --build` (derived renders are never hand-edited), so a rebuild now reproduces the current text, not the seat era. Prove: `grep -c 'Flat docs repo' .substrate/agents/architect.md` → **0** · `grep -c 'post-program era' .substrate/agents/architect.md` → **1**.

### D42. `.substrate/agents/architect.md:12` — contradiction

> Program record lives in menno420/superbot docs/eap/, never here.

**Claims:** EAP program records must not live in fleet-manager; an architect subagent should flag any EAP material committed here as a layer violation.

**Actually:** The tree contradicts it outright: fleet-manager holds nine top-level docs/eap-*.md files (eap-story.md, eap-retrospective.md, eap-audit-collection.md, eap-owner-checklist-2026-07-14.md, and five more), docs/findings/2026-08-09-eap-correspondence-record.md (committed deliberately by fm #833 after Gmail verification), and docs/planning/2026-07-26-final-eap-email-plan.md. The boot file's own deep read path routes sessions to docs/fleet-account-2026-07-26.md as the distillation of 'eap-story, eap-retrospective, dispatch-log and the rest' — i.e. the estate treats this repo as the EAP records home. The word 'never' makes this actionable rather than merely stale. Same not-auto-loaded caveat.

**Check it:** `ls docs/ | grep -i eap; ls docs/findings/ docs/planning/ | grep -i eap; grep -n 'never here' .substrate/agents/architect.md .substrate/agents/reviewer.md`

**Refuter's correction:** The count is wrong: there are SEVEN top-level docs/eap-*.md files, not nine (`ls docs/eap-*.md | wc -l` -> 7). Nine is the right total only if the two nested ones (docs/findings/2026-08-09-eap-correspondence-record.md and docs/planning/2026-07-26-final-eap-email-plan.md) are counted with them, which the finding lists separately. Also note this is a *stale* absolute, not a wrong one: the seat-era sentence was written when the program record lived in superbot; the records were consolidated here afterwards. Same root as 94/95 — the sentence comes from state.json slot Q-004 and is also planted, unbannered, in docs/architecture.md under '> **Status:** `binding`'.

**Closed 2026-08-11 (fm #849):** same slot fix as D41 — the regenerated persona no longer carries the "never here" absolute; the slot states program records live HERE and superbot docs/eap/ holds the EAP-era record. Prove: `grep -c 'never here' .substrate/agents/architect.md` → **0**.

### D43. `.substrate/agents/reviewer.md:11` — stale-fact

> Shared-repo protocol surfaces follow docs/playbook.md R9-R10.

**Claims:** playbook R9 (one writer per file / inbox appends) and R10 (first-declared + claim-filed arbitration) are the binding protocol a reviewer judges diffs against.

**Actually:** Two live surfaces say otherwise and this file was never updated to match. .claude/CLAUDE.md:115 enumerates the playbook rules that still bind — 'R1/R2/R16/R17/R22/R24/R29/R30 still bind, the dispatch and relay rules do not' — and R9/R10 are not in that set. docs/playbook.md's own mixed-era banner (added 2026-08-10) names 'R1/R2, R16/R17, R22/R24, and R29/R30' as the ones that remain useful and says the control-bus rules 'describe the closed autonomous program and are historical'; R9/R10 sit under the '## PROTOCOL' heading whose mechanism (claims/, inboxes, lanes) is retired. A reviewer persona pointed at R9-R10 would request changes against a rule the estate has retired. Same caveat as architect.md: staged, not auto-loaded.

**Check it:** `grep -n 'R1/R2/R16' .claude/CLAUDE.md; sed -n '1,14p;52,58p' docs/playbook.md; grep -n 'R9-R10' .substrate/agents/reviewer.md .substrate/agents/architect.md`

**Refuter's correction:** Same root as index 94: the sentence is rendered from .substrate/state.json slot Q-006 `ownership_model`, so a persona rebuild reproduces it. The reachable instance is docs/ownership.md:15, which carries the identical 'Shared-repo protocol surfaces follow docs/playbook.md R9-R10' under '> **Status:** `binding`' with no era banner, and docs/AGENT_ORIENTATION.md:31 (which at least has a mixed-era banner). Fixing the staged persona alone leaves the binding doc wrong.

**Closed 2026-08-11 (fm #849):** the `ownership_model` slot corrected and personas regenerated — the reviewer now carries R9-R10 as historical (playbook's 2026-08-10 banner) instead of as the binding protocol. The reachable planted copy, docs/ownership.md, is corrected under D75. Prove: `grep -c 'R9-R10 arbitration' .substrate/agents/reviewer.md` → **1**.

### D44. `bootstrap.py:21020` — stale-fact

> whether {named} is a REQUIRED status check on the base branch is owner-UI state this gate cannot read (rules API; 403-walled to agents)

**Claims:** The GitHub rulesets/rules API is unreadable by agents (403-walled) and required-status-check state is owner-UI-only, so `bootstrap.py check --strict` cannot verify it.

**Actually:** Refuted MEASURED 2026-08-06 and recorded in docs/CAPABILITIES.md (~line 353): GET /repos/menno420/fleet-manager/rules/branches/main and GET+PUT /repos/menno420/fleet-manager/rulesets/18725475 all returned 200 over direct egress, and substrate-gate was MADE a required check that way. This is a false wall printed at runtime by the one command CLAUDE.md names as the local gate, so a session that ran the gate without having loaded .claude/CLAUDE.md (boot case two/three: satellite root, or bare-clone parent /home/user) meets the wall and never meets the correction. Two aggravators: the file is GENERATED/DO-NOT-EDIT so the fix must land upstream in substrate-kit (CAPABILITIES.md already logs this as 'Kit-side follow-up' and it has not landed as of v1.20.2), and tools/check_no_false_walls.py line 73 explicitly excludes bootstrap.py, so the estate's own false-wall checker structurally cannot catch it. Mitigated but not fixed: .claude/CLAUDE.md:274 and docs/CAPABILITIES.md both counter-instruct ('read the endpoint, never quote that NOTE').

**Check it:** `cd . && python3 bootstrap.py check --strict 2>&1 | grep -n 'enforcement-required-unverified'   # prints: check: NOTE — enforcement-required-unverified — whether `substrate-gate` is a REQUIRED status check on the base branch is owner-UI state this gate cannot read (rules API; 403-walled to agents) …`

### D45. `bootstrap.py:19783` — stale-fact

> "# historically 403-walled in fleet sessions (capability ledger\n"

**Claims:** The generated branch-sweep workflow template writes into adopting repos: 'WHY A WORKFLOW, NOT THE AGENT: agent-side branch deletion is historically 403-walled in fleet sessions (capability ledger OA-10 — classifier + proxy deny every delete path). This workflow … is the sanctioned path around that wall.'

**Actually:** This is the canonical false wall the estate has already refuted twice. docs/CAPABILITIES.md's own 2026-08-05 owner-live entry: 'branch deletion ALL SUCCEED on the direct-PAT path'; tools/check_no_false_walls.py's provenance names this exact claim as the wall it was built to catch ('branch deletion is a normal capability, 204 via the direct-token path; only the proxied path 403s'); .claude/CLAUDE.md lists 'delete branches' as normal agent work. 'classifier + proxy deny EVERY delete path' is a present-tense absolute that is false. Secondary defect in the same block: the citation 'capability ledger OA-10' does not resolve — OA-10 appears 0 times in docs/CAPABILITIES.md (only in seat-era prompts and 2026-07 research docs). Lower blast radius than the NOTE above because no branch-sweep workflow is currently rendered here (.github/workflows has only merge-on-green, roster-freshness, roster-regen, substrate-gate), but this is live generator text, not a dated record, and bootstrap.py is excluded from the false-walls checker so nothing catches it.

**Check it:** `cd . && sed -n '19782,19786p' bootstrap.py; echo "OA-10 in ledger: $(grep -c 'OA-10' docs/CAPABILITIES.md)"; ls .github/workflows/`

**Refuter's correction:** Directionally right, but rank it below findings 130/132/133. Two softeners the finding understates: the sentence is hedged with 'historically', and nothing in this repo renders the branch-sweep workflow today, so no adopter file currently carries the text. The present-tense parenthetical 'classifier + proxy deny every delete path' is the actually-false part and is the minimal fix target — upstream in substrate-kit src/engine, since bootstrap.py is GENERATED, DO NOT EDIT.

### D46. `control/claims/README.md:3` — contradiction

> > **Status:** `binding`

**Claims:** The control/claims/ work-claim protocol is binding on sessions today.

**Actually:** Its own parent, control/README.md:2-4, names `claims/` in the retired set — 'The control/ message-bus (inbox.md, outbox.md, status.md, claims/) and the roster/telemetry autogen are retired with the EAP wind-down ... do not ... treat these files as live state'. control/inbox.md is closed by ORDER 049 and control/outbox.md carries the same RETIRED banner; this is the only file in control/ that carries no banner and instead asserts the opposite. The two documents are each internally coherent and disagree, so a session that lands here (e.g. told to claim before building) follows a protocol whose surrounding apparatus — the control fast lane it tells you to land the claim on, and the sibling heartbeat it defers ORDER claims to — no longer exists. control/claims/ holds only this README at HEAD.

**Check it:** `cd . && sed -n '1,10p' control/claims/README.md && sed -n '1,6p' control/README.md && ls -a control/claims/`

**Refuter's correction:** The finding assumes `binding` is the wrong side of the contradiction. That is not established: bootstrap.py:197 still pins DEFAULT_CLAIMS_DIR to control/claims and bootstrap.py:25183 still calls check_claims, so the claim ledger is live kit apparatus while the ORDER-relay it sits next to is not. The accurate statement is 'control/README.md's retirement banner sweeps `claims/` in with the message bus, and the claims README says the opposite; one of the two is over-broad and neither says which' — and the claim checker is advisory-only regardless.

**Closed 2026-08-11 (fm #849):** resolved the way the refuter framed it — by saying which side is over-broad, and in which narrow sense. The parent banner (and its copy in `control/outbox.md`) now carries a claims carve-out: `claims/` is NOT retired **as kit apparatus** (`claims_dir` + the advisory claims check), while the claims README's contested-status note states the operative rule the first version of this closure got wrong — **in fleet-manager the claim is the born-red card + open PR, never a file here** (the installed `session-close` skill, step 1; Codex round 1 on fm #849 caught the overclaim, which had been written from the skill's description line without reading its body) — and names the README's own retired parts (the fast-lane and heartbeat references). Prove: `grep -c 'is NOT retired' control/README.md` → **1** · `grep -c 'Contested-status note, 2026-08-11' control/claims/README.md` → **1** · `grep -c 'is NOT retired' control/outbox.md` → **1** · `grep -c 'NOT a file here' control/claims/README.md` → **1**.

### D47. `control/status.md:11` — contradiction

> updated: 2026-08-03T21:29:58Z

**Claims:** This CLOSED seat's heartbeat carries a freshness stamp 13 days after its own 'SEAT CLOSED — 2026-07-21T20:35Z' banner, and the repo's one local gate still demands it be restamped every session.

**Actually:** control/README.md:2-6 declares the control/ bus retired and says 'do NOT ... treat these files as live state', yet substrate.config.json still lists control/status.md in heartbeat_files, so `python3 bootstrap.py check` (the gate CLAUDE.md names as THE local gate) emits: '[status-stale] control/status.md: heartbeat is ~165h old (> 72h) — the manager treats a stale status as a DARK Project; overwrite control/status.md this session (mechanical restamp: `python3 bootstrap.py heartbeat`)'. A session that obeys the checker writes a fresh liveness date onto a record of a seat that closed 2026-07-21 — which is exactly what already happened: the 2026-08-03 stamp was written by automated roster-regen commit dfccceb (2026-08-06). Six live scripts (gen_roster.py, check_lane_liveness.py, check_trigger_health.py, verify_routine_state.py, check_owner_queue.py, check_label_hygiene.py) read this file's `updated:` value.

**Check it:** `cd . && sed -n '1,14p' control/status.md && python3 bootstrap.py check 2>&1 | grep status-stale && grep -n heartbeat substrate.config.json && git log -p --format='COMMIT %h %ad' --date=short -1 -- control/status.md | grep -E '^COMMIT|^\+updated:'`

**Refuter's correction:** Two overstatements to fix. (1) status-stale is NOT exit-affecting — the strict run groups it under 'check: 1 control-status advisory warning(s) (never exit-affecting)'; the exit-1 came from [preflight-script] on the born-red session card. It still instructs a restamp, but it does not red the gate. (2) 'Six live scripts read this file's `updated:` value' is too strong: only scripts/gen_roster.py, scripts/check_lane_liveness.py, scripts/check_trigger_health.py and scripts/verify_routine_state.py actually parse an `updated:` stamp; scripts/check_owner_queue.py and scripts/check_label_hygiene.py only mention control/status.md in docstring prose. Also the age is now ~166h, not ~165h.

**Closed 2026-08-11 (fm #849) — at the reachable site; the off-switch is the kit's:** a first version of this closure emptied `heartbeat_files` and claimed the advisory gone — **it was not**: the kit's `heartbeat_relpaths` deliberately falls back to `control/status.md` on an empty list ("misconfiguration never silently disables the gate", the template's own words), and the check-exceptions allowlist is applied to `doc_findings` only, never to the advisory stream — both verified in the vendored source, and the advisory re-fired in CI against the "fixed" config. So the config is restored to the kit default, and the fix lands where a misled session actually arrives: `control/status.md` now opens with a **do-not-restamp note** under its SEAT CLOSED line, naming the advisory, the forged-liveness failure (the 2026-08-03 automated restamp this entry records), and the kit-side switch filed for v1.21.0. Prove: `sed -n '3p' control/status.md` → contains `Do not restamp this heartbeat (2026-08-11, audit D47)` · `python3 -c "import json;print(json.load(open('substrate.config.json'))['heartbeat_files'])"` → **['control/status.md']** (the default, deliberately).

### D48. `docs/AGENT_ORIENTATION.md:30` — stale-fact

> Flat docs repo, no code layers: docs/ (playbook, owner-queue, dispatch-log — manager working memory) + templates/ (worker preamble blocks) + control/ (protocol heartbeat...). Program record lives in menno420/superbot docs/eap/, never here.

**Claims:** fleet-manager is a flat docs repo with no code layers and three content dirs, and the program record is never stored here.

**Actually:** There are 27 tracked .py files under scripts/ (20 entries) and tools/ (11 entries), plus bootstrap.py and six .claude/hooks/ scripts — the checkers and hooks that gate every PR live in exactly the 'code layers' this bullet says do not exist, and the enumerated dir list omits scripts/, tools/, .claude/, projects/, .sessions/. The program record also now lives here: docs/fleet-account-2026-07-26.md (the owner-reviewed 2025-08→now account, read-path entry 3) and docs/PROJECT-CLOSEOUT.md. This is the half the file's own banner blesses — line 25-26 says 'That half is still accurate and is what this router is for.'

**Check it:** `cd . && sed -n '24,30p' docs/AGENT_ORIENTATION.md && ls scripts/*.py tools/*.py | wc -l && ls .claude/hooks/*.py && ls docs/fleet-account-2026-07-26.md docs/PROJECT-CLOSEOUT.md`

**Refuter's correction:** Two details to fix. (1) The directory-entry counts are slightly off: `ls scripts` = 20 entries and `ls tools` = 12 (not 11); the .py count of 27 is right by `ls`, 28 by `git ls-files`. (2) More important: AGENT_ORIENTATION.md:30 is not the source. The identical string is the substrate-kit 'architecture' state value stored at .substrate/state.json:58 and mirrored verbatim into docs/architecture.md:10, .substrate/agents/architect.md:12, .substrate/agents/reviewer.md:11 and .substrate/claude/CLAUDE.md:49. Editing AGENT_ORIENTATION alone leaves five other copies and the generated text will come back at the next kit regen — the fix is the state value.

**Closed 2026-08-11 (fm #849):** the banner's blanket certification ("that half is still accurate") is replaced with a scoped one that disowns the inline contract summaries, and the three Binding-contracts bullets now point at the corrected planted docs with the seat-era render named as what they carried. The shared root (the state slots the refuter identified) is fixed under D41–D43/D53/D75/D93. Prove: `grep -c 'Do not read the inline contract summaries below as' docs/AGENT_ORIENTATION.md` → **1** · `sed -n '/## Binding contracts/,/## Manager working memory/p' docs/AGENT_ORIENTATION.md | grep -c 'Flat docs repo'` → **0**.

### D49. `docs/CAPABILITIES-verified-2026-07-18.md:37` — stale-fact

> **Do not poll `GET /commits/<sha>/check-runs`** with the fleet PAT — it answers `403 Resource not accessible by personal access token`

**Claims:** Polling GET /repos/{o}/{r}/commits/{sha}/check-runs with $GITHUB_PAT is refused 403 and must not be used; use pull_request_read get_check_runs or /actions/runs instead.

**Actually:** Measured today at HEAD: that exact endpoint returns HTTP 200 with total_count 9 over direct egress with $GITHUB_PAT. Worse, the live boot file gives the opposite standing instruction — .claude/CLAUDE.md:190-193 tells every session to 'Poll to a terminal state inside the turn (loop on commits/{sha}/check-runs until every run is completed; measured on fm #833, green on the 2nd of 12 x 15 s iterations)'. The boot file's Capabilities section names THIS file as the 'Full verified matrix', so a session that follows the pointer meets a recorded wall telling it to abandon the loop the boot file mandates. It is also a written-down limitation, the one thing this repo's own rule (same file, § 'Never document limitations') forbids.

**Check it:** `curl -s -o /tmp/cr.json -w 'HTTP %{http_code}\n' --noproxy '*' -H "Authorization: Bearer $GITHUB_PAT" https://api.github.com/repos/menno420/fleet-manager/commits/4b59e9ba9fd079ccffc246446174cc29d63e8cd1/check-runs && python3 -c "import json;d=json.load(open('/tmp/cr.json'));print(d['total_count'])" ; grep -n 'check-runs' .claude/CLAUDE.md docs/CAPABILITIES-verified-2026-07-18.md`

**Refuter's correction:** The finding reports total_count 9; I measured 16 at that SHA and 2 at HEAD — the count varies with time, the HTTP 200 is the load-bearing part and reproduces on both.

**Closed 2026-08-11 (fm #849):** the check-runs wall struck in place — re-measured today at HEAD: HTTP **200** with the PAT over direct egress — with the boot file's poll-to-terminal instruction cited and the struck sentence named as a written-down limitation in the one file whose header forbids them. Prove: `grep -c 'RETRACTED 2026-08-11 (audit D49)' docs/CAPABILITIES-verified-2026-07-18.md` → **1**.

### D50. `docs/PROJECT-CLOSEOUT.md:7` — contradiction

> is preserved as evidence, not a current queue. Live state and next action are

**Claims:** The banner tells a reader that §3's continuation list is historical evidence and not something to work from; live next actions are elsewhere.

**Actually:** The boot file says the opposite about the same section: .claude/CLAUDE.md:97-99 lists it as ordered read-path entry 5 — 'docs/PROJECT-CLOSEOUT.md §3 — the priority-ordered continuation threads, each self-contained. Two were still open 15 days after the close because no one re-read them.' The tree backs the boot file: §3 item 1 (trading-strategy #160) is still OPEN today, last updated 2026-07-21. So a session that follows the read path to §3 and then obeys the banner it lands on stops reading precisely the list the boot file sent it to work — which is the exact failure mode the boot file's own note complains about. Two internally coherent live surfaces, opposite instructions.

**Check it:** `sed -n '3,10p' docs/PROJECT-CLOSEOUT.md ; grep -n -A3 'The handover' .claude/CLAUDE.md ; curl -s --noproxy '*' -H "Authorization: Bearer $GITHUB_PAT" https://api.github.com/repos/menno420/trading-strategy/pulls/160 | python3 -c "import json,sys;d=json.load(sys.stdin);print(d['number'],d['state'],d['merged'])"`

**Refuter's correction:** The banner (added in PR #837, 'D2: make fleet-manager's front door tell the truth') overshot its target. The consolidation program §7 records the era-bannering pass as flagging `PROJECT-CLOSEOUT` §5, and §5 indeed carries its own precise, scoped banner at line 361. The top-of-file banner's separate sentence 'Its continuation list is preserved as evidence, not a current queue' disclaims §3, which is NOT stale: item 1 (trading-strategy #160) is verified OPEN today and its only resume recipe in the repo is that section, pointed to by both .claude/CLAUDE.md:97-99 and docs/owner-queue.md:487. The fix is to scope the top banner the way §5's is scoped — the historical claim applies to the §2 state snapshot and §5 boot route, not to §3.

**Closed 2026-08-11 (fm #846):** the banner is scoped per the refuter — §2/§5 historical, §3 named as the live handover record the boot file routes to, with the overshoot dated. Prove: `grep -c 'still the live handover record' docs/PROJECT-CLOSEOUT.md` → **1**.

### D51. `docs/ROUTINES.md:33` — snapshot-as-instruction

> Record every trigger create/delete call **verbatim** — id, cron, binding,

**Claims:** Status: `binding` doctrine for this repo on arming, verifying and auditing triggers — trigger deletion is normal recorded work, and (lines 90-94) every turn must end with 'exactly one future tick armed + the failsafe verified' and control/status.md re-stamped.

**Actually:** This is seat-era doctrine carrying a live `binding` badge and no era banner, while every sibling seat-era doc got one (RESUME.md and NEXT-TASKS.md on 2026-08-08, reading-path.md and AGENT_ORIENTATION.md on 2026-08-08/08-10). It is actively routed to: docs/AGENT_ORIENTATION.md:87 names it as the doc to 'read it before touching the trigger registry'. Yet it contains zero mentions of D‑0015 (docs/decisions.md:131, decided 2026-08-09: 'A session must never call delete_trigger'), zero mention of .claude/hooks/trigger_tools_guard.py — the estate's only denying hook — and zero mention of the `update_trigger enabled:false` emergency stop that replaced deletion. Its end-of-turn invariant also directs a session to re-stamp control/status.md, which is retired seat-era apparatus. A session routed here before touching triggers gets doctrine that normalises the one call the estate bans.

**Check it:** `grep -c 'D[-]0015' docs/ROUTINES.md ; grep -n -i 'delete\|update_trigger\|enabled: false' docs/ROUTINES.md ; grep -n 'ROUTINES.md' docs/AGENT_ORIENTATION.md ; grep -n -A6 'D[-]0015' docs/decisions.md`

**Refuter's correction:** Two details to narrow. (1) ROUTINES.md never *instructs* deletion — line 33 instructs recording, and line 46 is an observation; it presupposes deletion as ordinary rather than directing it, and the actual delete call is hard-denied by trigger_tools_guard.py, so that half of the harm is contained. The uncontained half is the seat-era end-of-turn invariant at lines 90-94, which under a live `binding` badge tells a session to re-stamp `control/status.md` (retired apparatus) and to keep exactly one tick armed every turn or suffer a 'seat-killing bug' — nothing gates that. (2) Reachability is narrower than the finding implies: .claude/CLAUDE.md, docs/current-state.md, docs/reading-path.md and README.md contain zero references to ROUTINES.md; the only live router is AGENT_ORIENTATION.md — but that router explicitly certifies the routines route as still-accurate at its lines 25-26, which makes the defect worse, not better.

**Closed 2026-08-11 (fm #849):** ROUTINES.md gains an era note under its badge — the method halves that stay sound, [D‑0015] with the disable-not-delete rule and the denying hook, and the dead end-of-turn invariant (no `control/status.md` re-stamp) — and AGENT_ORIENTATION's certifying route ("Arming, deleting…") is re-worded to carry the same rule at the routing moment. Prove: `grep -c 'Era note, 2026-08-11 (audit D51)' docs/ROUTINES.md` → **1** · `grep -c 'D‑0015' docs/ROUTINES.md` → **1** (the non-breaking-hyphen form, U+2011).

### D52. `docs/SKILLS.md:89` — stale-fact

> Two owner-directed seed methods (superbot Q-0273, 2026-07-12) are **installed as reference implementations in superbot**, canonical there until the kit generalizes them into the shipped skill set

**Claims:** Under the heading '## Fleet seed skills — pointer (not kit-shipped yet)', chase-references and prep-owner-steps are not kit-shipped and their bodies live in superbot at superbot `.claude/skills/<name>/SKILL.md`.

**Actually:** Both skills are installed here and invocable — .claude/skills/chase-references/SKILL.md (3263 bytes) and .claude/skills/prep-owner-steps/SKILL.md (3957 bytes) — and docs/SKILLS-local.md classifies both as body='kit', i.e. the kit does ship them. A session that reaches for chase-references (a boot-file routing-table skill, via `intake`) and reads this section is sent to another repo for a body sitting in its own tree. SKILLS.md is a live index the boot file's routing table depends on.

**Check it:** `ls -la .claude/skills/chase-references/ .claude/skills/prep-owner-steps/ ; sed -n '87,104p' docs/SKILLS.md ; grep -n 'chase-references\|prep-owner-steps' docs/SKILLS-local.md`

**Closed 2026-08-11 (fm #846):** the section now states both skills are kit-shipped and installed in this tree, bodies at their real paths, with the stale superbot pointer quoted as record. Prove: `grep -c 'installed in this repo' docs/SKILLS.md` ≥ **1**.

### D53. `docs/architecture.md:10` — stale-fact

> control/ (protocol heartbeat: owner-written inbox.md, manager-written status.md). Program record lives in menno420/superbot docs/eap/, never here.

**Claims:** The repo's `binding` architecture doc describes the estate as a seat-era manager repo: docs/ as 'manager working memory' (playbook, owner-queue, dispatch-log), templates/ as 'worker preamble blocks', control/ as a live protocol heartbeat, and the program record as living in menno420/superbot, never here.

**Actually:** Every clause describes the closed autonomous-Projects era. control/ is retired (its own README says so), the ORDER relay is dead, and the program record now lives in this repo (docs/planning/2026-07-26-consolidation-program.md, docs/fleet-account-2026-07-26.md). Unlike MISSION.md / NEXT-TASKS.md / fleet-triage.md / roster.md, this file carries no era banner and is still stamped `binding` — and it is reachable from a live surface: docs/intent.md line 12 sends a session here for architecture.

**Check it:** `sed -n '1,12p' docs/architecture.md; head -8 control/README.md; sed -n '11,13p' docs/intent.md`

**Refuter's correction:** 'Every clause describes the closed autonomous-Projects era' is overstated — two of the four survive. `ls templates/` shows worker-preamble.md still exists, and `ls docs/dispatch-log*` shows docs/dispatch-log.md still exists, so the docs/ and templates/ clauses are stale in tone, not in fact. 'Program record lives in menno420/superbot docs/eap/, never here' is scope-correct: it refers to the EAP autonomous-Projects program, whose record does live there; the *consolidation* program is a different program and lives here. The genuinely stale, misleading clause is the single one about `control/` being a live protocol heartbeat with an owner-written inbox.md and manager-written status.md, in a `binding`, un-bannered doc.

**Closed 2026-08-11 (fm #849):** the Layers section body is replaced with the current truth (checkers, hooks, vendored kit, records home) with the seat-era render quoted as a dated retraction, and the source slot corrected so regens agree. Prove: `grep -c 'Records-and-checkers repo, post-program era' docs/architecture.md` → **1** · `sed -n '/## Layers & import rules/,/| Layer |/p' docs/architecture.md | grep -c '^Flat docs repo'` → **0**.

### D54. `docs/collaboration-model.md:43` — unreachable-authority

> standard (canonical: `control/README.md` § "Owner-assist output standard"):

**Claims:** A `binding` doc names control/README.md as the canonical home of both the OWNER-ACTION six-field format (line 38) and an 'Owner-assist output standard' section.

**Actually:** control/README.md contains neither string — a case-insensitive grep for 'owner.action', 'owner-assist', 'WHY-IT-MATTERS' and 'UNBLOCKS' returns nothing, and its heading list has no such section. Worse, that file opens '> **RETIRED 2026-07-17 — autonomous apparatus wound down; historical only.** … do **not** … treat these files as live state.' The format actually lives in CONSTITUTION.md and .claude/skills/session-close/SKILL.md. A session sent to the cited authority finds a retired file that does not contain the rule.

**Check it:** `grep -ni "owner.action\|owner-assist\|WHY-IT-MATTERS\|UNBLOCKS" control/README.md; head -8 control/README.md; grep -rln "WHY-IT-MATTERS" --include=*.md .`

**Closed 2026-08-11 (fm #849):** both canonical pointers repointed at the verified real homes — `CONSTITUTION.md` (the OWNER-ACTION fields) and the skills that carry the output standard — with the dead `control/README.md` citations named at each site; grep-verified before repointing that the retired file contains neither string. Prove: `grep -c 'repointed 2026-08-11, audit D54' docs/collaboration-model.md` → **2**.

### D55. `docs/collaboration-model.md:85` — stale-fact

> Staleness review cadence: control/status.md is refreshed every working session (its updated: line is the heartbeat)

**Claims:** A `binding` doc states as current operating cadence that control/status.md is refreshed every working session.

**Actually:** control/status.md's first line is 'SEAT CLOSED — 2026-07-21T20:35Z' and control/README.md declares the whole bus retired 2026-07-17; current-state.md says 'the retired control/inbox.md is not an order channel' and the boot file lists control/ as historical apparatus. No session refreshes it. The same line also calls docs/playbook.md 'living', while the boot file says only R1/R2/R16/R17/R22/R24/R29/R30 still bind and the dispatch/relay rules do not.

**Check it:** `head -12 control/status.md; head -8 control/README.md; sed -n '85p' docs/collaboration-model.md`

**Refuter's correction:** The secondary half of the finding is weak and should be dropped. It says the same line 'calls docs/playbook.md living' in conflict with the boot file — but `head -8 docs/playbook.md` shows playbook.md declares itself 'Status: `living-ledger`' and already carries a '**Mixed-era banner, 2026-08-10:**' naming exactly which rules still apply and which (dispatch, control-bus, roster, wake-chain, seat-liveness) do not. Calling it living is correct. The defect is only the control/status.md clause.

**Closed 2026-08-11 (fm #849):** the cadence line now names the live surfaces only, with the control/status.md clause quoted as the correction; the finding's playbook half was dropped per the refuter (calling the playbook living is correct). Round-1 addendum (Codex, fm #849): the backing `staleness_review` slot in `.substrate/state.json` is corrected too, so a future `render` re-emits the fixed doctrine instead of the seat-era cadence. Prove: `grep -c 'Corrected 2026-08-11, audit D55' docs/collaboration-model.md` → **1**.

### D56. `docs/evidence-index.md:5` — stale-fact

> **GENERATED — NOT SOURCE OF TRUTH.** Do not hand-edit; regenerated with `docs/roster.md` on every regen (`scripts/gen_roster.py`, P3 — centralization plan §3c).

**Claims:** The file presents itself as a `living-ledger` (line 3) that is automatically regenerated alongside docs/roster.md, and line 7 names the live schedule: "dispatched by cron 40 */2 * * * (.github/workflows/roster-regen.yml…)".

**Actually:** The roster was retired 2026-08-07 by PR #812, which removed BOTH cron lines from roster-regen.yml (`on:` is now `workflow_dispatch:` only) and stamped docs/roster.md with a "⛔ RETIRED 2026-08-07 — this file is a record, not current truth" banner and `Status: historical`. That same PR never touched docs/evidence-index.md: its last commit is still the automated `Roster regen (automated, Generation #430)`. So the two halves of one generator now disagree — roster.md says the mechanism is dead, evidence-index.md still says it runs every two hours — and evidence-index.md keeps the `living-ledger` marker with no banner. This matters because docs/current-state.md:102 (boot read-path entry 1) still lists it as live apparatus: "**Evidence index**: `docs/evidence-index.md` (generated with the roster)". A session following the read path meets a frozen 2026-08-06 snapshot labelled current and auto-maintained, with pinned HEADs (e.g. fleet-manager @ `837bfe8`) that are now hundreds of commits stale.

**Check it:** `cd . && sed -n '1,8p' docs/evidence-index.md && sed -n '/^on:/,/^jobs:/p' .github/workflows/roster-regen.yml && sed -n '1,6p' docs/roster.md && git log --oneline -2 -- docs/evidence-index.md && grep -n 'Evidence index' docs/current-state.md`

**Refuter's correction:** Two details are overstated. (1) Reachability: the finding says "docs/current-state.md:102 (boot read-path entry 1) still lists it as live apparatus." It does not — line 102 sits under "## Historical seat-era baseline — preserved, not current" (line 61) → "### Seat-era stability baseline" (line 78), an explicitly bannered historical section. A repo-wide grep for live references finds none outside that section and the dated July planning/closeout records, so the doc is reachable mainly by direct opening or hygiene work, not by walking the read path. (2) Staleness magnitude: git rev-list --count 837bfe8..HEAD = 39, not "hundreds of commits stale" for the fleet-manager pin. Worth adding: roster-regen.yml:159 still hard-codes --dispatched-by "cron 40 */2 * * * ...", so any manual workflow_dispatch would re-stamp the now-false cron claim into the regenerated header.

**Closed 2026-08-11 (fm #849):** roster-style ⛔ banner applied — retired with the roster 2026-08-07, frozen at Generation #430, HEAD pins are that moment's — with the hand-edit exception stated (docs/roster.md's own precedent) and the on-demand `workflow_dispatch` residue kept honest per the refuter. Prove: `grep -c 'RETIRED with the roster, 2026-08-07' docs/evidence-index.md` → **1**.

### D57. `docs/evidence-index.md:3` — snapshot-as-instruction

> > **Status:** `living-ledger`

**Claims:** docs/evidence-index.md presents itself as a live, continuously-regenerating ledger — `Status: living-ledger`, line 5 "regenerated with `docs/roster.md` on every regen (`scripts/gen_roster.py`)", line 7 "dispatched by cron 40 */2 * * * (.github/workflows/roster-regen.yml)" — and its rows pin every lane's current-state / latest session card / retro at a "verified HEAD".

**Actually:** The roster was retired 2026-08-07 (PR #812) and BOTH roster-regen cron lines were removed; roster-regen.yml now carries only `workflow_dispatch` (line 107: "Both cron lines removed"). The file's own last write is Generation #430, generated-at 2026-08-06T14:57Z — it has not regenerated since and cannot. Its sibling from the SAME generator, docs/roster.md, got a `⛔ RETIRED 2026-08-07 … Status: historical` banner in that commit; evidence-index.md was left behind still badged live. A session opening it today reads four-day-frozen HEAD pins as current fleet truth and is told a cron is keeping them fresh.

**Check it:** `cd . && sed -n '1,7p' docs/evidence-index.md && head -6 docs/roster.md && grep -n 'cron lines removed' .github/workflows/roster-regen.yml && git log --oneline -2 -- docs/evidence-index.md`

**Refuter's correction:** 'it has not regenerated since and cannot' is overstated on the second half: PR #812 removed only the two cron lines and deliberately KEPT `workflow_dispatch:` (roster-regen.yml line 107 comment: 'workflow_dispatch KEPT, so the roster can still be generated on demand'). The file cannot refresh on a schedule; an on-demand dispatch is still available. Also worth noting for whoever fixes it: docs/current-state.md's mention of the evidence index (line 102) already sits inside the '## Historical seat-era baseline — preserved, not current' section (line 61), so only the file's own header needs the banner.

**Closed 2026-08-11 (fm #849):** the same banner flips the badge. Prove: `grep -c 'Status:\*\* `historical`' docs/evidence-index.md` → **1**.

### D58. `docs/findings/2026-08-05-foundation-continuation.md:34` — snapshot-as-instruction

> Revised, in order:

**Claims:** The five-row table that follows (port the reachability checker to superbot-next → build the Golden Transcript + state assertion → bifurcate the kit's checkers → featured_actions facet → CAPTURE-WORLD LITERAL sweep) is the standing order of work.

**Actually:** It is a 2026-08-05 snapshot written in the imperative, and two live surfaces now route sessions to it as the superseding next-action authority: .claude/CLAUDE.md:79 ('the revised order of work — foundation before rebuild') and consolidation-program:70-75 ('Before acting on this pointer, read ... it revises the order of work'). Five days and roughly fifteen PRs later none of items 1, 2, 4 or 5 has landed, the work went to OD-13 / intent layer / Layer 2 / the kit upgrade instead, and the strings 'reachability checker', 'Golden Transcript' and 'CAPTURE-WORLD LITERAL sweep' appear nowhere in current-state.md, the program, or intent.md — so the ordering has no live status row anywhere while still being cited as what to do next. What I could not establish: whether the owner regards the ordering as void, only that no live ledger tracks it and the program's NOW points elsewhere (D2).

**Check it:** `cd . && sed -n '70,76p' docs/planning/2026-07-26-consolidation-program.md && grep -n 'the revised order of' .claude/CLAUDE.md && grep -rn 'reachability checker\|Golden Transcript\|CAPTURE-WORLD LITERAL sweep' docs/current-state.md docs/planning/2026-07-26-consolidation-program.md docs/intent.md; echo "exit=$?  (1 = zero hits)"`

**Refuter's correction:** Line is 34, not 35 — "Revised, in order:" is at line 34 and the table runs 36-42 (line 35 is blank). Item 3 (bifurcate the kit's checkers) was at least partly discharged by the 2026-08-06 checker-classification doc + substrate-kit #577; items 1, 2, 4, 5 are all superbot-next-scoped and have no row in the program's step ledger, so the accurate statement is that the ordering has no live tracking surface, not that the owner voided it.

**Closed 2026-08-11 (fm #849):** a dated status note now sits between the two live routing surfaces and the table they route to: item 3 partially discharged (the 2026-08-06 checker classification, wiring deliberately deferred), items 1/2/4/5 superbot-next-scoped and unstarted, no live ledger tracks the ordering, the owner has not voided it, and the current next action is the program's NOW pointer (OD-13). The certainty legend's authority is restated untouched. Prove: `grep -c 'Status note, 2026-08-11 — audit D58' docs/findings/2026-08-05-foundation-continuation.md` → **1**.

### D59. `docs/findings/2026-08-05-google-play-submission-requirements.md:146` — stale-fact

> Limits apply identically to full-width and half-width characters. "Swingy
Spider" is 14 — comfortable.

**Claims:** The app's store-listing name is "Swingy Spider", and it is 14 characters against the 30-character App name limit.

**Actually:** Two errors in one sentence. (a) "Swingy Spider" was ruled out on 2026-08-05 — docs/owner-queue.md:210 records `OQ-SWINGY-NAME` as RESOLVED with the name **Slingy Spider**, because Swingy Spider is taken by two same-genre products. The title line 1 carries the same dead name ('verified for Swingy Spider'). (b) 'Swingy Spider' is 13 characters, not 14. This is the document a session preparing the Play listing will work from, and its §6 store-listing budget is computed against a rejected identifier.

**Check it:** `cd . && grep -n 'Swingy' docs/findings/2026-08-05-google-play-submission-requirements.md && sed -n '210,214p' docs/owner-queue.md && python3 -c "print(len('Swingy Spider'))"`

**Refuter's correction:** The character arithmetic is wrong but immaterial in effect — "Slingy Spider" is also 13, and either is far under the 30-char App name limit, so the §6 limits table itself is sound. The substantive error is the rejected product name in the title (line 1) and in the §6 example, with no superseded note, in a doc that the live Layer-2 README (docs/repos/spider-swing/README.md:97) hands a session for exactly this work.

**Closed 2026-08-11 (fm #849):** title and §6 now carry **Slingy Spider** (the `OQ-SWINGY-NAME` resolution) with the rejected name quoted as record and the 14→13 miscount corrected — refuter honoured: the limits table itself was sound and is untouched. Prove: `head -1 docs/findings/2026-08-05-google-play-submission-requirements.md | grep -c 'Slingy Spider'` → **1** · `grep -c 'OQ-SWINGY-NAME' docs/findings/2026-08-05-google-play-submission-requirements.md` → **2**.

### D60. `docs/findings/2026-08-09-substrate-kit-defects.md:199` — broken-ref

> because that file is the capability ledger and `tools/check_no_false_walls.py:296` special-cases it

**Claims:** tools/check_no_false_walls.py line 296 is where docs/CAPABILITIES.md is special-cased by the local false-wall checker.

**Actually:** At HEAD line 296 is `after = prefix[boundary.end():]`, inside the negation-boundary helper. The CAPABILITIES.md special-case is at lines 385-389 (`if os.path.basename(rel) == "CAPABILITIES.md":`) with its stop-heading regex at :193. The citation went stale inside the same PR (fm #835) that rewrote this checker's negation handling and also edited this doc — so the doc's own landing session invalidated its pointer. This file is the v1.21.0 session's worklist and is cited from docs/owner-queue.md and docs/current-state.md, so the next release session follows this pointer.

**Check it:** `sed -n '296p' tools/check_no_false_walls.py; grep -n 'CAPABILITIES.md' tools/check_no_false_walls.py`

**Closed 2026-08-11 (fm #849):** the pointer is re-anchored content-first — the `basename == "CAPABILITIES.md"` branch scanning the ACTIVE region above `## Append log` — with today's line number given as a hint only, because the audit's own corrected anchor (:385-389) had already drifted to :397 before this fix landed: the third drift of one pointer, which is the argument for resolving by code, not number. Prove: `grep -c ':397. as of 2026-08-11' docs/findings/2026-08-09-substrate-kit-defects.md` → **1**.

### D61. `docs/findings/README.md:10` — unreachable-authority

> ## Index (2026-07-09, evening — succession set)

**Claims:** docs/findings/README.md presents itself as the index of the findings corpus, but 16 of the 42 findings docs in docs/findings/ have no row in it.

**Actually:** The estate treats an index row as the anti-orphan mechanism — two cards in this batch state it explicitly ('docs/findings/README.md — index row, so the finding is not an orphan', .sessions/2026-08-05-discord-test-server-and-bot-value.md:27 and .sessions/2026-08-05-superbot-next-live-audit.md:27). 16 findings break it, including docs/findings/2026-08-05-owner-calibration-three-sessions.md (the doc that supersedes the 'seven corrections' figure), 2026-08-05-gemini-delegation.md, 2026-08-05-hud-telemetry-verification.md, 2026-08-06-provenance-mechanism-measured.md, 2026-08-08-why-rules-dont-bind.md and the whole 2026-08-09 set. A session that opens the index to find what has been established meets 26 of 42 documents and cannot tell the other 16 exist. The heading's own scope stamp ('2026-07-09, evening — succession set') is a snapshot that the file has long since outgrown, which is how the drift went unnoticed.

**Check it:** `cd . && for f in $(ls docs/findings/*.md | grep -v README); do b=$(basename $f); grep -q "$b" docs/findings/README.md || echo "ORPHAN $b"; done | wc -l; ls docs/findings/*.md | grep -vc README`

**Refuter's correction:** The count is 17 orphans of 42, not 16 of 42. 2026-08-06-checker-classification.md is also among them — notable because .claude/CLAUDE.md read-path entry 2b names that file directly, so it is reachable from the boot file even though the findings index does not list it. Reachability is therefore partial for a handful of docs; the index-completeness breach itself is confirmed.

**Closed 2026-08-11 (fm #849, recording only — discharged 2026-08-10):** the index was regenerated **complete** from the audit's per-file gists before the edit pass began; its header records the regeneration and the derivation now returns zero orphans. Prove: `for f in $(ls docs/findings/*.md | grep -v README); do b=$(basename $f); grep -q "$b" docs/findings/README.md || echo "ORPHAN $b"; done | wc -l` → **0**.

### D62. `docs/findings/README.md:10` — stale-count

> ## Index (2026-07-09, evening — succession set)

**Claims:** This file is the `living-ledger` index of the findings tree — one row per committed finding.

**Actually:** The index heading is frozen at 2026-07-09 and the table lists only 25 of the 42 finding documents in docs/findings/. Seventeen are absent, including 2026-08-06-checker-classification.md (which the boot file's read-path entry 2b names as the follow-on that carries the checker classification and boot-path audit), all six 2026-08-09 findings, 2026-08-08-why-rules-dont-bind.md, and 2026-08-10-fm835-verification.md. A session that opens the findings index to see what research exists gets a picture that stops in July, and 2026-08-09-substrate-kit-defects.md — which argues in its own header that a worklist nobody can find is a false-done waiting to happen — is one of the omissions.

**Check it:** `python3 -c "import pathlib,re; idx=pathlib.Path('docs/findings/README.md').read_text(); listed={l.split('/')[-1] for l in re.findall(r'\(([^)]+\.md)\)',idx)}; allf={p.name for p in pathlib.Path('docs/findings').glob('*.md') if p.name!='README.md'}; print(len(allf),'total',len(listed&allf),'listed'); print(sorted(allf-listed))"`

**Refuter's correction:** Two details are wrong. (1) The index does NOT 'stop in July': it carries eight August rows, including six 2026-08-05 docs and the 2026-08-10 cold-read row at line 38. Only the *heading* is frozen at 2026-07-09; the table has been appended to selectively. (2) There are five 2026-08-09 findings, not six (`ls docs/findings/ | grep -c 2026-08-09` = 5). The accurate statement: a `living-ledger` index claiming one row per committed finding lists 25 of 42, silently omitting 17 — the whole 2026-08-06 → 2026-08-09 research block, 2026-08-04-generated-art-pipeline.md, three further 2026-08-05 docs, 2026-08-10-fm835-verification.md, and two July docs.

**Closed 2026-08-11 (fm #849, recording only — discharged 2026-08-10):** same regeneration; the header carries the provenance ("regenerated complete … after the old index was measured listing 25 of 42"), which is this entry's claim stated as fixed. Prove: `grep -c 'regenerated \*\*complete\*\* on 2026-08-10' docs/findings/README.md` → **1**.

### D63. `docs/findings/ultracode-verification-2026-07-10.md:193` — stale-fact

> - ⚑ **fleet-manager's own `docs/findings/ping-test-2026-07-09.md` is wrong

**Claims:** An owner-morning flag stating fleet-manager's ping-test finding wrongly records websites as 'NO ACK', 'Not corrected in this PR … cheap follow-up for the next fleet-manager session'.

**Actually:** The correction landed the same day: docs/findings/ping-test-2026-07-09.md:96 now reads '✅ ACK (late) — corrected 2026-07-10; the ❌ NO ACK previously recorded here was FALSE' and the file carries a dedicated '### Correction (2026-07-10) — the websites row was FALSE' section with the re-derived 1h38m54s latency. The flag is an already-satisfied ask (the INC-06 class). Inert: it sits in a dated `reference` verification record whose flags are explicitly scoped to 'owner's morning' 2026-07-10, and no live surface routes to it.

**Check it:** `cd . && sed -n '193,197p' docs/findings/ultracode-verification-2026-07-10.md && sed -n '96p;104,110p' docs/findings/ping-test-2026-07-09.md`

**Closed 2026-08-11 (fm #849):** the flag is struck SATISFIED at its site with the same-day correction cited (ping-test's websites row and its § Correction section), the original disposition preserved in quotes. Prove: `grep -c 'SATISFIED same day' docs/findings/ultracode-verification-2026-07-10.md` → **1**.

### D64. `docs/fleet-inconsistencies-2026-07-13.md:3` — snapshot-as-instruction

> > **Status:** `living-ledger`

**Claims:** The 82-item inconsistency ledger presents itself as a live, maintained instrument — 'This is a living doc: retire items by striking the row and citing the fixing PR/ORDER, never by deleting it' (line 12) — with 44 rows dispositioned `ORDER-to-lane(<repo>)` = 'route via the control bus' (line 53) and a severity key reading 'HIGH = misleads owner/fleet operations right now' (line 49).

**Actually:** 65 of the 82 items are still unretired, and the machinery they are routed through no longer exists: the control bus was retired as live machinery at program close 2026-07-21 (docs/fleet-account-2026-07-26.md line 130: 'Retired as live machinery at close; historical record now'; .claude/CLAUDE.md 'Live vs historical' lists control/ as seat-era apparatus). Every peer register produced by the same 2026-07-13/14 fleet review has since been re-banner'd `historical` — docs/fleet-triage.md ('this register closed with the autonomous seat on 2026-07-21'), docs/roster.md ('RETIRED 2026-08-07'), docs/reading-path.md, docs/NEXT-TASKS.md, docs/RESUME.md ('era-banner added 2026-08-08') — but this file was missed by that sweep and is the only seat-era ledger still self-declaring `living-ledger`. It is reachable from a live surface (docs/current-state.md:483 links it) and from scripts/gen_roster.py:388. A session opening it today reads ~65 open items whose stated next action is to dispatch ORDERs down a bus that was dismantled. Its §12 self-defence ('verify a row's citation against HEAD') covers per-row staleness only — not the status header or the disposition column.

**Check it:** `cd . && grep -n '^> \*\*Status:\*\*' docs/fleet-inconsistencies-2026-07-13.md docs/fleet-triage.md docs/roster.md docs/reading-path.md && grep -c 'ORDER-to-lane' docs/fleet-inconsistencies-2026-07-13.md && grep -o 'INC-[0-9]\+' docs/fleet-inconsistencies-2026-07-13.md | sort -u | wc -l && grep -o '~~INC-[0-9]\+~~' docs/fleet-inconsistencies-2026-07-13.md | sort -u | wc -l && grep -n 'Retired as live machinery' docs/fleet-account-2026-07-26.md && grep -n 'fleet-inconsistencies' docs/current-state.md`

**Refuter's correction:** Two details to tighten. (a) The '44 rows dispositioned ORDER-to-lane' is 44 *matching lines*, one of which is the legend at line 53 ('`ORDER-to-lane(<repo>)` = route via the control bus') — so ~43 rows; the file's own §1 summary says '~40'. (b) Reachability is thinner than 'reachable from a live surface' suggests: current-state.md:483 sits under '## Recently shipped (newest first)' as a dated 2026-07-13/14 deliverable, and the file is named nowhere in .claude/CLAUDE.md, README.md, docs/README.md or the consolidation program. The fix is the same either way — add the `historical` era banner the 2026-08-08 sweep gave every peer register.

**Closed 2026-08-11 (fm #849):** `historical` era banner applied — the last seat-era ledger still self-declaring `living-ledger` — naming the dead ORDER-to-lane disposition and routing anything still worth fixing to today's channels. Prove: `grep -c 'Era banner, 2026-08-11 (audit D64)' docs/fleet-inconsistencies-2026-07-13.md` → **1**.

### D65. `docs/gen2-blueprint.md:3` — snapshot-as-instruction

> > **Status:** `binding`

**Claims:** The gen-2 seed standard — seat births, Project creation, Custom-Instruction pastes, cadence wake routines, per-lane CI tiers — is standing, binding law.

**Actually:** It is the seat-era launch standard for the autonomous-Projects program that CLOSED 2026-07-21. Every sibling doc of the same era got an explicit era banner in the 2026-08-08/2026-08-10 front-door sweeps — MISSION.md keeps `binding` but adds a 15-line 'Era note, 2026-08-08' explaining the done-when is unmeasurable today; docs/NEXT-TASKS.md was flipped to `historical` with 'era-banner added 2026-08-08'; docs/fleet-triage.md was flipped to `historical`. gen2-blueprint.md was missed: `grep -ci 'era note|historical|seat-era'` returns 0 for the whole 513-line file. It is also unreachable from every Layer-1 live surface (0 hits for 'gen2-blueprint' in .claude/CLAUDE.md, README.md, docs/current-state.md, the consolidation program, docs/intent.md, docs/decisions.md), so nothing a session walking the read path ever warns it that this `binding` badge describes dead apparatus — a session that finds it by grep or via docs/prompts/README.md takes §1's checklist and §3's owner click list as current procedure. Note the file WAS swept for false walls (classifier-denial sentences carry inline date stamps like 'classifier denied (2026-07-10)'), so the omission is specifically the era sweep, not neglect.

**Check it:** `cd . && grep -n '^> \*\*Status:\*\*' docs/gen2-blueprint.md MISSION.md docs/NEXT-TASKS.md docs/fleet-triage.md; grep -ci 'era note\|historical\|seat-era' docs/gen2-blueprint.md; grep -c gen2-blueprint .claude/CLAUDE.md README.md docs/current-state.md docs/planning/2026-07-26-consolidation-program.md docs/intent.md docs/decisions.md`

**Closed 2026-08-11 (fm #849):** era note added (badge kept, MISSION.md treatment): the seed standard is record, not procedure. Prove: `grep -c 'Era note, 2026-08-11 (audit D65/D66)' docs/gen2-blueprint.md` → **1**.

### D66. `docs/gen2-blueprint.md:373` — contradiction

> - Landing path: REST merge-on-green (R21 primary on this shape).

**Claims:** Playbook R21 is the governing landing-path rule; a lane picks arm-at-creation vs REST merge-on-green 'per playbook R21'.

**Actually:** R21 is dead twice over, and this `binding` doc cites it as law in EIGHT places (lines 22, 117, 212, 224, 371, 373, 401, 425). docs/playbook.md:285 reads '**R21 (2026-07-09) — SUPERSEDED 2026-07-11 by the corrected UNIVERSAL v4 §2.4 merge clause** … agents never REST-merge or arm their OWN PRs' — so the blueprint's own citation was already stale one day after it was written. And that superseding clause was itself reversed on 2026-07-18/19 (fm #308/#309, playbook R30), leaving today's live rule in .claude/CLAUDE.md: 'You hold admin + push on every repo … Merge PRs, delete branches … all normal agent work.' A session that trusts the `binding` badge and follows R21 adopts a landing doctrine two revisions behind live capability. playbook.md carries a 2026-08-10 mixed-era banner naming R1/R2, R16/R17, R22/R24, R29/R30 as still useful — R21 is pointedly not on that list.

**Check it:** `cd . && grep -n 'R21' docs/gen2-blueprint.md && sed -n '283,292p' docs/playbook.md && sed -n '1,12p' docs/playbook.md`

**Closed 2026-08-11 (fm #849):** the same era note carries the double supersession of R21 (superseded 2026-07-11 by UNIVERSAL v4 §2.4; that clause reversed 2026-07-18/19, fm #308/#309/R30) so all eight citations are disarmed at the front door — and names the max-one-status-PR rule as one of `[D‑0016]`'s two live narrow caps. Prove: `grep -c 'R21 was SUPERSEDED 2026-07-11' docs/gen2-blueprint.md` → **1**.

### D67. `docs/handoff-2026-07-10.md:13` — contradiction

> 1. `playbook.md` — **R1–R23, all binding** (R22 visibility guard

**Claims:** All playbook rules R1 through R23 are binding, and this handoff is the successor session's first-read (repeated at line 114: '**R1–R23 are binding**').

**Actually:** docs/playbook.md now carries a 'Mixed-era banner, 2026-08-10' saying the dispatch, control-bus, roster, wake-chain and seat-liveness rules 'describe the closed autonomous program and are historical', and that only R1/R2, R16/R17, R22/R24, R29/R30 remain useful. The playbook also now runs to R30, not R23. Every peer seat-era doc got an era banner (MISSION.md 'Era note, 2026-08-08'; docs/NEXT-TASKS.md 'SUPERSEDED'; docs/fleet-triage.md 'Historical snapshot'; docs/roster.md 'RETIRED 2026-08-07'; playbook.md itself) — this handoff did not, and still presents a live read order, a live ORDER/inbox delivery SOP, and a false wall at line 98 ('No cross-session send tools exist in this org').

**Check it:** `grep -n 'R1–R23' docs/handoff-2026-07-10.md; sed -n '1,12p' docs/playbook.md; grep -oE 'R[0-9]+' docs/playbook.md | sed 's/R//' | sort -n | uniq | tail -3; grep -niE 'historical|superseded|retired|era.note' docs/handoff-2026-07-10.md || echo 'NO BANNER'`

**Refuter's correction:** Scope is understated in one direction and overstated in another. Understated: docs/handoff-2026-07-09.md has the identical problem — same `owner-guidance` status, same 'The successor session's first-read' framing, no era banner — so the fix is a two-file class, not one. Overstated: reachability is thin. Nothing in .claude/CLAUDE.md, README.md, docs/current-state.md or the consolidation program links to handoff-2026-07-10.md; the only inbound references are docs/launch-readiness-2026-07-10.md:124 and docs/dispatch-log.md:307, both themselves seat-era. A session reaches it by grep or file-tree browsing, not by walking the read path.

**Closed 2026-08-11 (fm #849):** era banners on **both** files (the refuter's two-file class — `handoff-2026-07-09.md` had the identical shape): no successor seat exists, the read orders and ORDER SOPs are record, and 07-10's "no cross-session send tools" dead wall is named as such. Prove: `grep -c 'Era banner, 2026-08-11 (audit D67)' docs/handoff-2026-07-10.md` → **1** · `grep -c 'Era banner, 2026-08-11 (audit D67)' docs/handoff-2026-07-09.md` → **1**.

### D68. `docs/ideas/archive-ready-retro-gap-advisory-2026-07-11.md:38` — stale-fact

> Quick-win, fleet-manager-side (`scripts/gen_roster.py`), no lane

**Claims:** This is a routable quick-win: add an advisory section to scripts/gen_roster.py (~15 lines + a --selfcheck pin), 'a good first slice for the successor coordinator between orders'. docs/ideas/README.md:65 carries the same route in the live backlog as `captured`.

**Actually:** The roster was retired 2026-08-07 — docs/roster.md opens '⛔ RETIRED 2026-08-07 — this file is a record, not current truth' and .github/workflows/roster-regen.yml now has only `workflow_dispatch:` with both cron lines removed, so gen_roster.py no longer runs on any schedule and the advisory would never be emitted. The idea also depends on docs/evidence-index.md being 'generated with the roster', and on 'the successor coordinator', a seat that ceased to exist when the program closed 2026-07-21. docs/ideas/README.md's own lifecycle says GROOM = 'pull one routable idea forward each session', so a grooming session today would take this and build into dead machinery.

**Check it:** `sed -n '1,10p' docs/roster.md; grep -n -A6 '^on:' .github/workflows/roster-regen.yml; grep -n 'gen_roster' docs/ideas/README.md docs/ideas/archive-ready-retro-gap-advisory-2026-07-11.md`

**Refuter's correction:** 'gen_roster.py no longer runs on any schedule and the advisory would never be emitted' is half overstated. scripts/gen_roster.py still exists (110 KB) and roster-regen.yml still carries `workflow_dispatch:`, which docs/roster.md itself preserves deliberately ('Neither workflow is deleted — workflow_dispatch still works on both, per OD-3'). So the advisory could be emitted on a manual dispatch. The accurate statement is narrower and still damning: it never fires unattended (both cron lines removed 2026-08-07), and it would write into a file whose own header says 'Do not read the rows below as the state of anything.'

**Closed 2026-08-11 (fm #849):** the idea is flipped `historical` / outcome `rejected` with a route-death note at its Route section (the roster it would write into is retired; the coordinator seat is gone; a manual dispatch would emit into a file whose banner disclaims it), and the `docs/ideas/README.md` backlog row says the same so no groom pulls it forward. Prove: `grep -c 'Route died 2026-08-07' docs/ideas/archive-ready-retro-gap-advisory-2026-07-11.md` → **1** · `grep -c 'state: historical' docs/ideas/archive-ready-retro-gap-advisory-2026-07-11.md` → **1**.

### D69. `docs/launch-readiness-2026-07-10.md:86` — stale-fact

> **owner-eyes-only** — agents can neither read nor write those surfaces

**Claims:** The repo-settings REST API (auto-merge toggles, required-check lists, rulesets, branch auto-delete) is 'walled from agent seats' (line 30); rulesets are 'unreadable first-hand' (line 36); § 'The settings-API wall' restates it as 'a standing finding'.

**Actually:** .claude/CLAUDE.md:271 records the opposite as MEASURED 2026-08-06: 'The rulesets API is readable AND writable agent-side — GET/PUT /repos/{o}/{r}/rulesets/{id} over direct egress, both 200, re-verified from the effective-rules endpoint after the write.' This is exactly the 'never write down a limitation' class the estate guards, but tools/check_no_false_walls.py scans only 5 files (CONSTITUTION.md, docs/current-state.md, docs/owner-queue.md, .claude/CLAUDE.md, docs/CAPABILITIES.md), so this doc is invisible to the required gate — and unlike its seat-era peers it carries no era banner, so nothing tells a reader the wall is dead.

**Check it:** `grep -n 'walled from agent seats\|unreadable first-hand\|neither read nor write' docs/launch-readiness-2026-07-10.md; grep -n 'rulesets API is readable' .claude/CLAUDE.md; python3 tools/check_no_false_walls.py --list`

**Refuter's correction:** One mitigation the finding omits: the only live inbound link is docs/owner-queue.md:23, and it introduces the doc as 'Historical lineage of the gen-2 launch that seeded the earliest queue items', so a reader arriving by the read path is already told it is history. The other references are projects/venture-lab/meta.md (a projects/ file the boot file classifies as historical). That lowers the odds of the wall being believed but does not remove it — the doc's own words are 'a standing finding', present tense, with no date qualifier.

**Closed 2026-08-11 (fm #849):** era banner naming the settings-API wall REFUTED (rulesets API readable AND writable agent-side, MEASURED 2026-08-06) plus an inline REFUTED marker at § "The settings-API wall" for the grep-arriving reader; body preserved verbatim. Prove: `grep -c 'Era note, 2026-08-11 (audit D69)' docs/launch-readiness-2026-07-10.md` → **1** · `grep -c 'REFUTED — see the 2026-08-11 era note' docs/launch-readiness-2026-07-10.md` → **1**.

### D70. `docs/owner-actions-2026-07-17.md:9` — snapshot-as-instruction

> > `claude/owner-actions-0717` (PR #279). Hand this to an owner-live hub session

**Claims:** This is the single verified paste-ready list of everything the owner must do fleet-wide, to be handed to an owner-live hub session and executed in one sitting; §4 (6 veto menus, ~266 proposals) and §6 (9 console items) are flagged 'Still OPEN for the owner (NOT executed)'.

**Actually:** docs/owner-queue.md:14 states plainly: '`owner-actions-2026-07-17.md` and `NEXT-TASKS.md` are seat-era records and must not be used as live action lists.' The file itself carries no such banner — nothing in it signals that its ~266 open proposals and 9 console items are dead, and its closing line invites re-verification rather than retirement. Worse, docs/owner-queue.md contradicts itself at line 528-529: 'Any remaining fleet-wide merges/ready-flips live in owner-actions-2026-07-17.md, not here.' Two claims in one live file, one pointing at the doc as authoritative and one forbidding its use.

**Check it:** `sed -n '10,16p' docs/owner-queue.md; sed -n '526,530p' docs/owner-queue.md; grep -niE 'seat-era|historical|superseded record|retired' docs/owner-actions-2026-07-17.md || echo 'NO BANNER'`

**Refuter's correction:** The 'owner-queue.md contradicts itself' half does not hold up and should be dropped. Line 528-529 is not a second live assertion: a heading scan shows it sits under '## Inherited cross-repo owner asks — status as recorded' (line 65), whose own banner reads 'These entries preserve their last recorded status and instructions. They are not a 2026-08-10 verification of another repository or external account. Re-check the owning surface before acting.' The sentence is further wrapped in a dated '*Standing note (R30, 2026-07-19):*' — a preserved record quoting the then-routing, not the queue claiming the doc is authoritative today. The surviving defect is the simple one: docs/owner-actions-2026-07-17.md is an unbannered file that presents ~266 open proposals and 9 console items as a live paste-ready owner list, and only owner-queue.md:14 — a different file — says otherwise.

**Closed 2026-08-11 (fm #849):** the file itself now carries the banner owner-queue.md has pointed at since the close — seat-era record, never a live action list — so the demotion no longer lives only in a different file. The refuter's narrowing (the queue's line 528 sits under the inherited-asks banner and is not a live contradiction) is adopted; owner-queue.md is untouched. Prove: `grep -c 'Era banner, 2026-08-11 (audit D70)' docs/owner-actions-2026-07-17.md` → **1**.

### D71. `docs/owner-queue-candidates.md:7` — stale-fact

> > **Generation #430** · generated-at **2026-08-06T14:57Z** · by roster-regen workflow (GitHub Actions, headless), dispatched by cron 40 */2 * * * (.github/workflows/roster-regen.yml, fleet-manager PR #81)

**Claims:** The file is a `living-ledger` that is "regenerated with the roster on every regen" and dispatched by the 2-hourly cron `40 */2 * * *`, so its 12 candidate owner asks are a current feed awaiting curation.

**Actually:** The roster was retired 2026-08-07 and BOTH roster-regen cron lines were removed — .github/workflows/roster-regen.yml now has only `workflow_dispatch` (its own header at line 107 says "Both cron lines removed; workflow_dispatch KEPT"). Nothing regenerates this file on a schedule, so it is frozen at Generation #430 forever, and every block in it is a verbatim extraction from a seat heartbeat dated 2026-07-09 to 2026-07-24 — seats terminated 2026-07-21. docs/roster.md received an explicit "⛔ RETIRED 2026-08-07 — this file is a record, not current truth" banner in that same pass; this companion generated feed (and docs/evidence-index.md, which carries the identical false cron line) did not, so the retirement is only partly landed and this file still presents itself as live.

**Check it:** `head -9 docs/owner-queue-candidates.md; sed -n '105,120p' .github/workflows/roster-regen.yml; head -12 docs/roster.md; head -8 docs/evidence-index.md`

**Refuter's correction:** Accurate as written, including the 12-block count and the identical defect in docs/evidence-index.md:7. Worth noting the fix is one banner applied to both files, matching docs/roster.md's, since they are generated by the same `scripts/gen_roster.py` run.

**Closed 2026-08-11 (fm #849):** the same roster-style ⛔ banner as evidence-index (one retirement, two generator outputs — the refuter's one-banner-for-both fix, applied per file): frozen at Generation #430, extractions from heartbeats of seats closed 2026-07-21, do not curate the queue from it. Prove: `grep -c 'RETIRED with the roster, 2026-08-07' docs/owner-queue-candidates.md` → **1**.

### D72. `docs/owner-queue-candidates.md:3` — snapshot-as-instruction

> > **Status:** `living-ledger`

**Claims:** docs/owner-queue-candidates.md declares itself a live feed — `Status: living-ledger`, "regenerated with the roster on every regen (`scripts/gen_roster.py`, P2)", "Generation #430 · generated-at 2026-08-06T14:57Z · dispatched by cron 40 */2 * * *" — and docs/current-state.md describes docs/owner-queue.md as "fed by the generated docs/owner-queue-candidates.md".

**Actually:** Same defect as evidence-index.md and the same root commit: the roster retirement (2026-08-07, PR #812) removed both roster-regen cron lines, so this feed is frozen at 2026-08-06T14:57Z with no path to refresh. docs/roster.md received the historical banner; this second same-generator output did not. A session grooming the owner queue would treat a stale extraction of seat-era heartbeats (from repos whose seats no longer exist) as a live candidate feed.

**Check it:** `cd . && sed -n '1,7p' docs/owner-queue-candidates.md && grep -n 'workflow_dispatch:\|cron lines removed' .github/workflows/roster-regen.yml && git log --oneline -1 -- docs/owner-queue-candidates.md`

**Refuter's correction:** Two details need softening. (1) 'no path to refresh' — `workflow_dispatch:` is retained in roster-regen.yml (line 117); only the schedule was removed. (2) The supporting citation to docs/current-state.md is weaker than stated: the phrase 'fed by the generated docs/owner-queue-candidates.md' is at line 99, which falls inside the section opened at line 61, '## Historical seat-era baseline — preserved, not current' — already bannered. The live defect is entirely in this file's own unbannered `living-ledger` header.

**Closed 2026-08-11 (fm #849):** the banner flips the badge. Prove: `grep -c 'Status:\*\* `historical`' docs/owner-queue-candidates.md` → **1**.

### D73. `docs/owner-steps-2026-07-18.md:3` — contradiction

> > **Status:** `audit`

**Claims:** This 2026-07-18 fleet-wide owner-step list carries no era banner and no supersession pointer, and docs/current-state.md:438 describes it as "the current consolidated, payoff-ordered, one-sitting-batched list of every open owner-only step across the fleet".

**Actually:** docs/owner-queue.md:3 declares itself "the ONE deduplicated list of things waiting on the owner", and its §Context explicitly demotes the sibling seat-era lists (owner-actions-2026-07-17.md, NEXT-TASKS.md) — but never mentions owner-steps-2026-07-18.md, which current-state.md (read-path entry 1) still advertises as current. Two live surfaces therefore each name a different document as the owner's action list. Comparable seat-era docs (docs/roster.md, control/README.md, docs/playbook.md) all received explicit RETIRED/mixed-era banners; this one was missed, so nothing tells a session its contents are three weeks stale.

**Check it:** `grep -rn "owner-steps-2026-07-18" --include=*.md . | grep -v '/.sessions/'; head -20 docs/owner-steps-2026-07-18.md; head -10 control/README.md`

**Refuter's correction:** 'Two live surfaces each name a different document as the owner's action list' is overstated. current-state.md:438 sits inside `## Recently shipped (newest first)` (heading at line 166) — a dated changelog whose neighbours are 2026-07-16..07-18 entries, not a live index; the present-tense 'the current…' is that entry's wording as of its ship date. The real defect is narrower and still real: the doc itself carries no era banner while every comparable seat-era doc got one in the 2026-08-10 pass, and owner-queue.md's §Context demotes its siblings owner-actions-2026-07-17.md and NEXT-TASKS.md by name but never this file. Fix = add the banner to the file (and/or name it in owner-queue.md:14-15), not rewrite current-state.md's changelog.

**Closed 2026-08-11 (fm #849):** era banner naming the live queue and the settled asks. Prove: `grep -c 'Era banner, 2026-08-11 (audit D73/D74)' docs/owner-steps-2026-07-18.md` → **1**.

### D74. `docs/owner-steps-2026-07-18.md:167` — stale-fact

> - **Approve the apparatus-sizing recommendation** (OQ-FM-APPARATUS-SIZING). Keep
  merge-on-green / substrate-gate / roster-freshness + the S3/S5/S9 checkers; slow
  `roster-regen.yml` from every-2h to daily.

**Claims:** The owner-only section still asks the owner to approve keeping roster-freshness and slowing roster-regen to a daily cron, and (line 186) to answer the curious-research slicer question, and (line 164) to answer delete-vs-archive.

**Actually:** All three are answered and the first was answered differently from what this list asks for. docs/owner-queue.md:588 records OQ-FM-APPARATUS-SIZING RESOLVED 2026-08-07 — the owner said "Yes retire the roster, I don't need it", both roster-regen cron lines were removed (not slowed to daily) and roster-freshness.yml's pull_request trigger was removed. docs/owner-queue.md:674 records OQ-CR-SLICER-ANSWER RESOLVED 2026-08-07 (Bambu Studio). Delete-vs-archive was ruled 2026-07-26 as OD-3. Because the file carries no era banner and current-state.md calls it current, a session preparing owner steps would re-put three settled questions to the owner, and the apparatus one in a form the owner already overruled.

**Check it:** `sed -n '162,170p' docs/owner-steps-2026-07-18.md; grep -n "OQ-FM-APPARATUS-SIZING\` .RESOLVED\|OQ-CR-SLICER-ANSWER" docs/owner-queue.md; grep -n "on:" -A 3 .github/workflows/roster-regen.yml`

**Refuter's correction:** Line numbers slightly off for two of the three: the slicer ask spans 186-187 and delete-vs-archive is at 164-166 (the finding cites 186 and 164 as the anchors, which is fine). A fourth stale item sits in the same unbannered file at 157-160 — the `ROSTER_READ_TOKEN` conditional PAT, the same ask finding 135 shows was mooted on 2026-08-07 — so the count of settled questions this file would re-put to the owner is four, not three.

**Closed 2026-08-11 (fm #849):** the banner enumerates all **four** settled asks with their real resolutions — the refuter's fourth (`ROSTER_READ_TOKEN`, mooted) included, and the apparatus-sizing one flagged as answered *differently* (retire outright, not slow to daily), which is the dangerous half of re-putting it. Prove: `grep -c 'four asks below' docs/owner-steps-2026-07-18.md` → **1**.

### D75. `docs/ownership.md:15` — stale-fact

> One writer per file: the owner writes control/inbox.md; the manager writes everything else (docs/, templates/, control/status.md). Shared-repo protocol surfaces follow docs/playbook.md R9-R10.

**Claims:** A document whose status is `binding` states the repo's live write-ownership model in terms of the seat-era control bus and defers shared-surface conflicts to playbook rules R9-R10.

**Actually:** Both halves describe machinery that no longer exists and that other live surfaces mark historical. control/README.md opens "**RETIRED 2026-07-17 — autonomous apparatus wound down; historical only** … do not resume the ORDER-relay or treat these files as live state"; the boot file lists control/ as seat-era historical. There is no "manager" seat: the autonomous-Projects program closed 2026-07-21 and work now runs in regular sessions. docs/playbook.md's own 2026-08-10 mixed-era banner names R1/R2, R16/R17, R22/R24, R29/R30 as still useful and classes the control-bus rules as historical — R9 ("One writer per file; appends only on inboxes") and R10 (arbitration precedent) are in the historical class. ownership.md is in the kit's planted doc set and is reached from docs/AGENT_ORIENTATION.md as a binding contract, so a session routed there is handed a retired ownership model as binding law. Its ownership table is also still the unfilled template placeholder "(one row per owned area)".

**Check it:** `cat docs/ownership.md; head -10 control/README.md; sed -n '1,15p;54,58p' docs/playbook.md; grep -n "ownership" docs/AGENT_ORIENTATION.md`

**Refuter's correction:** Understated on one point: AGENT_ORIENTATION.md does not merely reach ownership.md, it affirmatively vouches for it. Its 2026-08-10 mixed-era banner (lines 5-10) sends the manager-seat routes to history but lines 24-26 explicitly keep the planted doc set — naming 'ownership' — and assert 'That half is still accurate.' So the 2026-08-10 banner pass actively certified this file while its body still describes the retired control bus and a nonexistent manager seat.

**Closed 2026-08-11 (fm #849):** the Ownership model section is rewritten to the current truth with the seat-era model quoted as a dated retraction; the § New areas manager clause is corrected in the same pass — including its OWN backing slot, `new_area_ownership`, which the first version of this closure missed (Codex round 1, fm #849: a render would have re-emitted the manager-as-sole-writer doctrine); the ownership-model slot is fixed under D43 so regens agree; and the certifying router line that vouched for this file is scoped under D48. Prove: `grep -c 'no manager seat' docs/ownership.md` → **2** · `sed -n '/## Ownership model/,/## Ownership table/p' docs/ownership.md | grep -c '^One writer per file'` → **0**.

### D76. `docs/planning/2026-07-14-central-docs-plan.md:3` — snapshot-as-instruction

> > **Status:** `plan`

**Claims:** A 389-line actionable plan badged `plan` (i.e. live), prescribing 47 concrete moves, a Slice 0 that 'outranks everything', and execution mechanics built entirely on the seat era — routing changes 'via inbox ORDER', per-lane 'ORDER 028 / ORDER 007', the dispatch-log, `docs/roster.md`, `control/` outboxes, the 19-repo lane fleet and `scripts/gen_roster.py`.

**Actually:** Every mechanism it instructs a session to use is retired: the autonomous-Projects program closed 2026-07-21, seat-era apparatus (docs/roster.md, control/, telemetry/, docs/prompts/) is historical per .claude/CLAUDE.md, and the roster stopped regenerating 2026-08-07. D2's own method is 'seat-era docs get an historical era-banner (never rewritten)' — that banner was applied to the sibling seat-era plan (2026-07-12-repo-consolidation-plan.md is badged `historical`) but not to this one, and docs/planning/README.md line 20 lists it with no superseded marker while explicitly marking v1/v2 '(SUPERSEDED)'. A session that greps into it for owner-queue, CAPABILITIES or fence conventions reads live-badged instructions to dispatch ORDERs to seats that do not exist.

**Check it:** `for f in docs/planning/*.md; do printf '%s ' "$(grep -m1 -o '`\(plan\|historical\|living-ledger\)`' $f)"; echo $f; done; grep -c 'inbox ORDER\|control/outbox\|dispatch-log' docs/planning/2026-07-14-central-docs-plan.md`

**Refuter's correction:** "Every mechanism it instructs a session to use is retired" is overstated. The doc's goal (fm as the docs SSOT) is still the live direction, and its class-C conventions remain cited as authority by live generated files — registry/README.md line 5 ("central-docs-plan §4 class C") and registry/kit-versions.md line 5 ("INC-42 / central-docs-plan C4"). The accurate finding is the missing `historical` era-banner over the seat-era EXECUTION mechanics (inbox ORDERs, lanes, roster regen), not that the whole document is dead.

**Closed 2026-08-11 (fm #849):** mixed-era banner per the refuter's split — the SSOT goal and class-C conventions stay live (registry files still cite them); the execution mechanics (inbox ORDERs, lanes, roster regen) are named the closed program's; work routes to the consolidation program. Prove: `grep -c 'mixed era, banner added 2026-08-11 (audit D76)' docs/planning/2026-07-14-central-docs-plan.md` → **1**.

### D77. `docs/planning/2026-07-24-app-plan-life-admin.md:3` — stale-fact

> > **Status:** `plan` — awaiting owner go/no-go (see Decisions below; queued as `OQ-APP-PLAN-GO`).

**Claims:** The plan presents itself as still awaiting an owner go/no-go decision, with §12 offering a five-row decision table and 'A single "go, defaults" starts phase 0.'

**Actually:** The decision was taken the same day the plan was written. docs/owner-queue.md line 764: '`OQ-APP-PLAN-GO` — RESOLVED: owner GO (hub chat 2026-07-24…); defaults D1–D5 taken, no overrides voiced. Executed same-session: private repo menno420/shiftlife created… + phase-0 scaffold pushed'. The repo has existed for 17 days and the program's §2 lists it as a section. A session reading this header would re-ask the owner a settled question — the precise waste v2 §1 criticises v1 for. docs/planning/README.md line 17 repeats the stale 'owner go/no-go queued as OQ-APP-PLAN-GO' phrasing, so the index does not correct it either.

**Check it:** `sed -n '3p' docs/planning/2026-07-24-app-plan-life-admin.md; grep -n 'OQ-APP-PLAN-GO' docs/owner-queue.md docs/planning/README.md`

**Closed 2026-08-11 (fm #849):** the header now records GO taken same-day (defaults D1–D5, shiftlife created, phase-0 pushed) with an explicit do-not-re-ask, and `planning/README.md`'s row — the index that repeated the stale phrasing — is corrected in the same pass. Prove: `grep -c 'GO taken 2026-07-24' docs/planning/2026-07-24-app-plan-life-admin.md` → **1** · `grep -c 'RESOLVED same day — owner GO' docs/planning/README.md` → **1**.

### D78. `docs/planning/2026-07-26-ci-consolidation.md:118` — contradiction

> `merge-on-green`, `auto-merge-disarm`, `automerge-card-guard`,

**Claims:** §3 'What gets deleted outright' lists the entire agent merge-plumbing class including `merge-on-green`, justified by 'With PRs now reviewed rather than self-landed, GitHub's native auto-merge toggle covers the remaining need.'

**Actually:** Both halves are false for fleet-manager itself. (1) `.github/workflows/merge-on-green.yml` is live at HEAD and is the workflow that actually lands this repo's PRs — the program's own §7 ledger records 'merge-on-green merged fm #827 22 seconds after a Codex review was requested'. (2) Its provenance header states the stated replacement does not exist here: 'This repo CANNOT use GitHub-native auto-merge (toggle unavailable on the private repo/plan)'. The program's C2 row (line 131) records the corrected rule — 'keep merge-on-green/enabler only where it still lands PRs' — but this doc is still badged `plan` with no supersession note, so a session doing the OD-9 CI work from it would delete the estate's landing path.

**Check it:** `sed -n '116,122p' docs/planning/2026-07-26-ci-consolidation.md; sed -n '1,12p' .github/workflows/merge-on-green.yml; sed -n '131p' docs/planning/2026-07-26-consolidation-program.md`

**Refuter's correction:** Slightly overstated on blast radius: the program's C2 (line 131) already carries the corrected rule, so the risk materialises only for a session that works the CI cleanup from this companion doc without reading the program's C-track row. The heading the quote sits under is line 115, not 118 (118 is the list line itself, which is where the quote was taken from and is correct).

**Closed 2026-08-11 (fm #849):** § "What gets deleted outright" opens with a dated supersession note for this repo — merge-on-green is what lands fm's PRs and native auto-merge is unavailable here — routing the C-track work to the program's corrected C2 row, exactly the two facts the entry established. Prove: `grep -c 'Superseded for fleet-manager itself — 2026-08-11, audit D78' docs/planning/2026-07-26-ci-consolidation.md` → **1**.

### D79. `docs/planning/2026-07-26-final-eap-email-plan.md:1` — unreachable-authority

> > **Status:** `plan` - owner-directed 2026-07-26 ... Program step **E1** (the program's NOW).

**Claims:** This is the live plan for program step E1, the owner's own reserved step.

**Actually:** It is referenced from exactly one file in the entire repository - docs/planning/README.md - which is itself 4 hops from the front door, putting the plan at depth 5. Neither the boot file, the README, current-state.md, nor the consolidation program names it. A session picking up E1, or the owner asking where his material is, never meets it. Its own header also still declares E1 'the program's NOW', which stopped being true on 2026-08-01 when E1 became owner-reserved and D2 became the actionable step.

**Check it:** `grep -rln 'final-eap-email-plan' --include=*.md . | grep -v '^./.sessions/'`

**Refuter's correction:** Measured depth is 4 hops from README.md, not 5 (README -> docs/intent.md -> planning/2026-08-08-fleet-manager-as-index.md -> planning/README.md -> plan). The staleness also propagates: docs/planning/README.md's own table row calls it "Program step **E1** (the NOW)". Mitigation worth noting: the program's own E1 block loudly says OWNER-RESERVED and points at D2, so a session that read the mandatory files first is unlikely to be misled by the plan's header alone.

**Closed 2026-08-11 (fm #846):** the plan is now linked from the program (×2), the owner queue's new E1 entry and `planning/README.md` — no longer a depth-4 orphan — and its header states OWNER-RESERVED. Prove: `grep -rln 'final-eap-email-plan' docs/planning/2026-07-26-consolidation-program.md docs/owner-queue.md docs/planning/README.md` → **3 files**.

### D80. `docs/planning/2026-07-26-final-eap-email-plan.md:6` — contradiction

> Program step **E1** (the program's NOW).

**Claims:** This plan doc, badged `plan` (live) and maintained as recently as 2026-08-09, tells its reader that E1 is the consolidation program's current NOW step and that execution was 'targeted for the owner's next free sitting (~2026-07-27)'.

**Actually:** The program says the opposite in bold: 'E1 remains OWNER-RESERVED and deliberately deferred… It is not stalled and it is not available to pick up… A session must NOT draft, send, or restart this step. If you are looking for work, take the repository named by D2's NOW pointer instead' (2026-07-26-consolidation-program.md lines 77-84), and the NOW header at line 62 names D2, not E1. Both documents are internally coherent; a session that arrives at the EAP plan first (it is the top row of docs/planning/README.md, which repeats 'Program step E1 (the NOW)' at line 12) is told to start the one piece of work the program explicitly forbids touching. The doc's §2 was updated on 2026-08-09 with the correspondence record, so the stale NOW claim survived a live edit pass.

**Check it:** `grep -n "program's NOW" docs/planning/2026-07-26-final-eap-email-plan.md; sed -n '62,84p' docs/planning/2026-07-26-consolidation-program.md; sed -n '12p' docs/planning/README.md`

**Closed 2026-08-11 (fm #846):** the header and the `planning/README.md` row both state OWNER-RESERVED / not the NOW. Prove: `grep -c 'OWNER-RESERVED and' docs/planning/2026-07-26-final-eap-email-plan.md` → **1**.

### D81. `docs/planning/README.md:5` — stale-count

> > Index of `docs/planning/` — dated plans and launch/follow-up records. Each

**Claims:** This table is the index of docs/planning/; its newest row is 2026-07-26.

**Actually:** docs/planning/ holds 15 documents plus this README; the table lists 12. Missing are overnight-menu-2026-07-17.md and — far more consequentially — BOTH live 2026-08-08 architecture records: 2026-08-08-agent-operating-environment-roadmap.md (the owner's three-phase roadmap) and 2026-08-08-fleet-manager-as-index.md (the Layer 1/Layer 2 design that .claude/CLAUDE.md cites as canonical for Layer 2 decisions). A session opening the directory's own index to answer 'what plans exist' concludes the newest plan is the 2026-07-26 consolidation program and never meets either 2026-08-08 document.

**Check it:** `ls -1 docs/planning/; grep -c '^| 20' docs/planning/README.md; grep -n '2026-08-08' docs/planning/README.md`

**Closed 2026-08-11 (fm #846):** four rows added — the two 2026-08-08 architecture records, the 2026-08-10 navigation plan (which had joined the missing set since the audit; the set grows, as predicted) and the overnight menu. Prove: the derivation loop over `docs/planning/*.md` → **0 MISSING** (README itself excepted).

### D82. `docs/planning/idea-backlog.md:12` — stale-count

> > 46 idea block(s) across 244 card(s) · 4 ungroomed · 4 ungroomed older than 2d.

**Claims:** The generated session-card idea backlog states it harvested 46 idea blocks across 244 cards, of which only 4 are ungroomed.

**Actually:** The tree now holds 344 session cards (345 .md files minus README.md), and 342 of them carry a 💡 idea block — so the file's own scope line is ~100 cards stale and its harvest total is off by roughly 7x. Derived from this batch: 25 of my 26 cards (all dated 2026-07-10/11, well inside the 244 the file claims to have scanned) carry a 💡 Session idea block, yet exactly ONE (2026-07-10-registry-gap-closure.md) appears in the backlog table. A planning session that reads '4 ungroomed' concludes grooming is essentially finished; the true ungroomed population is in the hundreds. The file's 'NOT SOURCE OF TRUTH' and 'generated-at 2026-07-19' banners disclose staleness but not the undercount, which is a harvest defect inside the window it did scan.

**Check it:** `cd . && sed -n '10,12p' docs/planning/idea-backlog.md && ls .sessions/*.md | wc -l && grep -l '💡' .sessions/*.md | wc -l && for f in $(tail -n +3 docs/audits/2026-08-10-full-read/enumeration.tsv | cut -f2 | sed -n '69,94p'); do grep -qF "$(basename $f)" docs/planning/idea-backlog.md && echo "listed: $(basename $f)"; done`

**Refuter's correction:** Two details wrong, one of them load-bearing. (1) '~100 cards stale' mischaracterizes the scope line: 244 was accurate for the 2026-07-19 generation date (245 cards existed dated on/before it), and the drift to 344 is ordinary snapshot aging that the 'generated-at' stamp discloses. Drop that half. (2) 'off by roughly 7x' uses the wrong denominator; within the window the harvester found 46 of 243 idea-carrying cards, ~5.3x. The surviving, sharper statement: the harvester misses ~81% of in-window idea-carrying cards, and regenerating the file today still reports '4 ungroomed', so the misleading figure is structural and cannot be fixed by re-running the generator.

**Closed 2026-08-11 (fm #849):** regenerated with `python3 scripts/gen_idea_backlog.py` (derived render — never hand-edited) from the D36-corrected generator: fresh generated-at, current card count, and the header now disclosing that the counts are a floor over the bullet form only. The structural undercount is disclosed rather than "fixed" by widening the harvest — per the refuter, re-running alone could never repair the misleading figure; the scope line is what does. Prove: `grep -c 'Harvest scope is the BULLET form only' docs/planning/idea-backlog.md` → **1** · `grep -c 'generated-at 2026-08-11' docs/planning/idea-backlog.md` → **1**.

### D83. `docs/project-recreation-runbook.md:78` — contradiction

> 3. **Delete only ids attributed to stopped seats** — the failsafe id (and its I8 dup) for each Project the owner stopped.

**Claims:** A live-reading session is instructed to enumerate triggers and delete the ones attributed to stopped seats (also §2 step 2, §5 step 5 'both stale ids in each pair are deletable', and §5's Safety note 'deleting a trigger is reversible only by recreating it').

**Actually:** This directly contradicts [D‑0015] (docs/decisions.md:131, decided 2026-08-09): 'A session must never call delete_trigger' — enforced by .claude/hooks/trigger_tools_guard.py, the estate's only DENYING hook, and restated in .claude/CLAUDE.md. The runbook carries no era banner (Status: `audit`, 'Created: 2026-07-16'), is written entirely in the imperative for a program that closed 2026-07-21, and is linked plainly from the live docs/current-state.md:442. A session that greps for trigger procedure finds a step-by-step deletion sweep with no marker that the whole procedure is now forbidden.

**Check it:** `sed -n '73,84p' docs/project-recreation-runbook.md; sed -n '131,146p' docs/decisions.md; grep -n 'delete_trigger' .claude/hooks/trigger_tools_guard.py | head -5; grep -n 'project-recreation-runbook' docs/current-state.md`

**Refuter's correction:** Two overstatements worth fixing. (1) 'linked plainly from the live docs/current-state.md:442' — the link is real but sits inside the '## Recently shipped (newest first)' log whose heading is at docs/current-state.md:166, i.e. a chronological record of what landed, not an active pointer. (2) The §2 reference is step 2 (line 31: 'so a post-stop sweeper session (§5) can find and delete them'), not an instruction to delete. Mitigation the finding omits: the MCP route is now hard-denied by trigger_tools_guard.py, so following the runbook costs a blocked call rather than an actual deletion — the exposure is the warn-only direct-API route and the wasted cycle.

**Closed 2026-08-11 (fm #849):** era note at the top ruling the whole runbook non-executable and naming [D‑0015] over its deletion steps, plus an inline read-delete-as-disable annotation at §5 where the sweep procedure lives; body preserved verbatim as record. Prove: `grep -c 'Era note, 2026-08-11 (audit D83)' docs/project-recreation-runbook.md` → **1** · `grep -c 'read "delete" as "disable' docs/project-recreation-runbook.md` → **1**.

### D84. `docs/prompts/chatgpt-project-instructions.md:3` — contradiction

> > **Status:** `owner-guidance` · rewritten 2026-08-10 after the first measured run

**Claims:** This file is the live, current Instructions text for the owner's ChatGPT 'Fleet Manager' project — rewritten today (2026-08-10) against a measured run (fm #835), and cited as current by docs/execution-surfaces.md:281.

**Actually:** .claude/CLAUDE.md:123 tells every booting session that 'docs/roster.md, control/, telemetry/, docs/prompts/ are **seat-era apparatus — historical record**, not current truth'. That blanket label is now false for docs/prompts/: this file is a live standing instruction set for an entire execution surface, and docs/prompts/2026-08-07-curious-research-external-review.md is a live owner deliverable too. A session obeying the boot file would discount both — and would not think to update the ChatGPT instructions when the estate's facts change, which is exactly the drift this file was created to prevent.

**Check it:** `sed -n '120,126p' .claude/CLAUDE.md; sed -n '1,11p' docs/prompts/chatgpt-project-instructions.md; grep -n 'chatgpt-project-instructions' docs/execution-surfaces.md; ls -1 docs/prompts/`

**Refuter's correction:** Scope is slightly wider than stated: docs/prompts/README.md is also non-historical ('Status: `living-ledger`'), so three files in the directory contradict the blanket label, not two. Note also that the label is defensible for the bulk of the directory (baseline-2026-07-11/, v3/, gen1-winddown-universal.md, universal-wakeup.md etc. are genuinely seat-era) — the fix is a carve-out sentence, not deleting the classification.

**Closed 2026-08-11 (fm #849, recording only — the fix landed 2026-08-10, fm #840 `d73d063`):** the boot file's Live-vs-historical line now carries exactly the carve-out this finding demanded — `docs/prompts/chatgpt-project-instructions.md` and the curious-research review prompt named live, `control/claims/` named contested — so the blanket label no longer discounts the live surfaces. The refuter's third file (`docs/prompts/README.md`, `living-ledger`) is judged no-defect: it is the *index* of a historical directory, and an index being maintained does not contradict its contents being record. Prove: `sed -n '154,157p' .claude/CLAUDE.md | grep -c 'chatgpt-project-instructions'` → **1**.

### D85. `docs/prompts/init-prompt-universal.md:24` — contradiction

> At seat cutover: the NEW seat re-arms its own trigger FIRST, then `delete_trigger` the old one (F-1 rule).

**Claims:** The same paste-ready block instructs a founded session to call delete_trigger at seat cutover.

**Actually:** Two lines earlier, in the SAME verbatim block, a 2026-08-09 amendment says '⚠ NEVER `delete_trigger`' and justifies itself with 'This prompt founds sessions in repos that do NOT load fleet-manager's guard hook, so this line is the only protection they get.' The amendment (commit 0ab4d07, PR #834) added the warning but never swept the block it was warning about, so the one artifact designated as the sole protection for hook-less repos still hands them the forbidden call. This is a live surface by its own header: Status `living-ledger` + 'Use the current text for every new deployment.' The live rule is [D‑0015] (docs/decisions.md:131) and .claude/hooks/trigger_tools_guard.py DENYs the call.

**Check it:** `grep -n "delete_trigger" docs/prompts/init-prompt-universal.md`

**Closed 2026-08-11 (fm #846):** see the headline table, row 3 — the badge and deploy sentence were the re-judged defect; the block stays verbatim as record under an era banner naming the live rule. Prove: `sed -n '3p' docs/prompts/init-prompt-universal.md` → `historical`.

### D86. `docs/providers/grok.md:146` — contradiction

> - Nothing here is measured in this estate yet.

**Claims:** No claim in the Grok provider doc has been measured in this estate.

**Actually:** The same file carries a whole section headed '## Measured here — the chat tab and Imagine are different capabilities' at line 92, with owner-run sprite tests dated 2026-08-04 scored against spider-swing's reference art, plus an app-settings measurement at line 119 that the doc itself says 'closes' one of its own nulls. The boilerplate honest-null line is correct in cohere.md, deepseek.md, meta-llama.md and mistral.md and was copied into grok.md without re-deriving it. A session reading the nulls section concludes nothing has been tried here and re-runs measurements that exist — and docs/repos/spider-swing/records.md points at this very file for 'per-provider rows measured on this repo's art work'.

**Check it:** `cd . && grep -n 'Measured here\|Nothing here is measured\|measured 2026-08-04' docs/providers/grok.md && grep -rn 'Nothing here is measured in this estate yet' docs/providers/`

**Closed 2026-08-11 (fm #849):** the false boilerplate null is replaced with the scoped truth — the API surface is what remains unmeasured; the 2026-08-04 measurements cover the chat tab and Imagine — with the copied-from-the-unmeasured-docs provenance stated. The four sibling provider docs keep the line because for them it is true. Prove: `grep -c '^- Nothing here is measured' docs/providers/grok.md` → **0** (the old wording survives only inside the retraction quote, not as a live bullet) · `grep -c 'chat tab and the Imagine image surface only' docs/providers/grok.md` → **1**.

### D87. `docs/q-index.md:1` — unreachable-authority

> # Q-index — repo-qualified owner-decision register (INDEX)

**Claims:** This is the estate's register for cross-repo-cited Q-numbers, existing 'to kill the ID-mislabel class'.

**Actually:** Nothing a session reads today reaches it. Outside .sessions/, .substrate/ and this audit's own files, docs/q-index.md is referenced only by four seat-era documents all dated 2026-07-11..2026-07-14 (dispatch-log.md, findings/manifest-parallel-run-2026-07-11.md, fleet-inconsistencies-2026-07-13.md, planning/2026-07-14-central-docs-plan.md). It is absent from .claude/CLAUDE.md, README.md, docs/AGENT_ORIENTATION.md, docs/decisions.md, docs/intent.md and docs/playbook.md. Critically, CLAUDE.md's § 'Where a decision lives, so you cite the right record' enumerates docs/decisions.md, the program OD table, the Layer-2 planning doc and substrate-kit's PL register — and omits the one register for cross-repo Q-IDs. So a session about to cite a Q-number has no route to the index built to stop it mislabelling one, while the file still wears a `living-ledger` badge implying someone maintains it.

**Check it:** `cd . && git grep -lI 'q-index' -- . | grep -v '^\.sessions/' | grep -v '^\.substrate/' | grep -v '^docs/q-index.md' && grep -c 'q-index' .claude/CLAUDE.md docs/decisions.md README.md`

**Refuter's correction:** Two referrers are not bannered historical — docs/dispatch-log.md and docs/fleet-inconsistencies-2026-07-13.md both carry `Status: living-ledger`, and docs/planning/2026-07-14-central-docs-plan.md carries `Status: plan`. They are nonetheless all seat-era 2026-07-11..07-14 documents outside every current read path, so the reachability conclusion is unaffected.

**Closed 2026-08-11 (fm #849):** re-badged `reference` with the maintenance truth dated, and routed from the citing moment — `docs/decisions.md`'s header now points Q-NNNN citations here — rather than growing the boot file. Prove: `sed -n '3p' docs/q-index.md | grep -c 'reference'` → **1** · `grep -c 'q-index.md' docs/decisions.md` → **1**.

### D88. `docs/reading-path.md:24` — stale-fact

> all fleet siblings are public and readable read-only EXCEPT pokemon-mod-lab (PRIVATE — raw/clone hits an auth wall; roster marks it NOT MEASURED; never raw-fetch or guess about it)

**Claims:** Every repo in the estate is public except pokemon-mod-lab, which is the sole dark repo a session must never raw-fetch or guess about.

**Actually:** There are two private repos, not one: GET /user/repos?affiliation=owner returns pokemon-mod-lab AND shiftlife as private (24 owned repos total). shiftlife was created 2026-07-24 — before the 2026-08-08 correction block in this same file, which re-blesses this section verbatim: 'The read authorization and the mechanics in §0 and §§2–4 below are unchanged and still correct.' The corrector inherited §0 rather than re-deriving it. The historical banner at the top does not cover §0, because §1 explicitly exempts §0 from it. A session following this treats shiftlife as public and guessable — and the owner stated live on 2026-08-10 that shiftlife is not active, so guessing about it is exactly the wrong move.

**Check it:** `curl -sS --noproxy '*' -H "Authorization: Bearer $GITHUB_PAT" 'https://api.github.com/user/repos?per_page=100&affiliation=owner' | python3 -c "import sys,json;d=json.load(sys.stdin);print('owned',len(d));print('private',[r['name'] for r in d if r['private']])" && sed -n '24p;49,50p' docs/reading-path.md`

**Closed 2026-08-11 (fm #849):** §0 now names **two** private repos, re-measured today via `/user/repos?affiliation=owner` (exactly pokemon-mod-lab and shiftlife of 24 owned), notes the 2026-08-08 correction block's inheritance, and corrects the dead roster pointer in the same bullet. Round-1 addendum (Codex, fm #849): the backing `fleet_dark_repos` slot is corrected too — and the same sweep that verified it derived three MORE stale slots Codex had not named (`fleet_siblings`, `fleet_status_command`, `review_ritual`), all six now corrected via `bootstrap.py answer`, so no future render reintroduces the seat-era claims. Prove: `grep -c 'two PRIVATE repos' docs/reading-path.md` → **1**.

### D89. `docs/research/2026-07-12-platform-capabilities.md:24` — stale-fact

> 9. GitHub is **MCP-only** (no `gh` CLI, REST 403 via proxy incl. stub-200 bodies); tags/releases via `workflow_dispatch`; Actions runners face GH013 + a PR-create permission toggle (§5).

**Claims:** GitHub is reachable only through the MCP tools; the gh CLI is absent, direct REST 403s, and tags/releases can only be cut via workflow_dispatch.

**Actually:** All three sub-claims are refuted at HEAD. `command -v gh` returns /usr/bin/gh. The estate's live capability record says the opposite: .claude/CLAUDE.md holds 'admin + push on every repo via the direct-PAT path ... Merge PRs, delete branches, change settings/rulesets, create releases/secrets/tags' and docs/CAPABILITIES.md:776 records tag/release/branch-delete 'ALL SUCCEED on the direct-PAT path'. Only the *proxied* REST path 403s. This matters because the doc is not inert: docs/AGENT_ORIENTATION.md:47 links it in present tense as 'the verified platform capability/limitation ledger (what claude.ai Projects/sessions CAN and CANNOT do)', and that file's 2026-08-10 era banner explicitly keeps the document-set routes as live 'reference material' while retiring only the manager-seat routes. The same wall is restated at line 344. tools/check_no_false_walls.py cannot catch it: its scan set is a narrow allowlist (CONSTITUTION, current-state, owner-queue, .claude/CLAUDE.md, active CAPABILITIES) that excludes docs/research/.

**Check it:** `cd . && command -v gh; grep -n 'MCP-only' docs/research/2026-07-12-platform-capabilities.md; grep -n 'research/2026-07-12-platform-capabilities' docs/AGENT_ORIENTATION.md; sed -n '5,8p' docs/AGENT_ORIENTATION.md; grep -n 'releases/secrets/tags' .claude/CLAUDE.md; sed -n '776,779p' docs/CAPABILITIES.md`

**Closed 2026-08-11 (fm #849):** era banner (dated snapshot, not the live ledger; CAPABILITIES.md and the boot file win) + a REFUTED marker on headline row 9 at the site; `gh` presence re-measured in this container; AGENT_ORIENTATION's vouching route re-worded under D48's fix so the "verified ledger" framing is gone from the router too. Prove: `grep -c 'Era note, 2026-08-11 (audit D89)' docs/research/2026-07-12-platform-capabilities.md` → **1** · `grep -c 'REFUTED 2026-08-11 — see the era note at top' docs/research/2026-07-12-platform-capabilities.md` → **1**.

### D90. `docs/research/README.md:8` — unreachable-authority

> Each entry gets a link line below when it merges; reports on unmerged branches are not listed (no dangling links).

**Claims:** The research index promises a link line for every merged report, so the table is the complete set of committed research reports.

**Actually:** Three merged, tracked reports are absent from the table: docs/research/2026-07-12-platform-capabilities.md, docs/research/2026-07-12-problem-census-satellites.md, and docs/research/2026-07-12-prompt-architecture.md. Two of the three are in this batch. The platform-capabilities ledger is the most-cited artifact of that night (docs/CAPABILITIES.md:963 and docs/AGENT_ORIENTATION.md:47 both point at it), and the satellites census is the one that carries the correct historical banner — yet neither is discoverable from its own index, so a session browsing docs/research/ concludes they do not exist. The index also carries the only staleness rider these docs get ('a snapshot of its census moment: verify claims against the repos'), which the unlisted files therefore never receive.

**Check it:** `cd . && for f in $(git ls-files 'docs/research/*.md' | grep -v README); do b=$(basename "$f"); grep -q "($b)" docs/research/README.md || echo "MISSING FROM INDEX: $f"; done`

**Closed 2026-08-11 (fm #849):** the three merged, tracked reports have rows; the derivation the entry's own Check-it prescribes returns zero missing. Prove: `for f in $(git ls-files 'docs/research/*.md' | grep -v README); do b=$(basename "$f"); grep -q "$b" docs/research/README.md || echo "MISSING $f"; done | wc -l` → **0**.

### D91. `docs/research/README.md:8` — stale-count

> > the repos before acting on them (playbook R2). Each entry gets a link line

**Claims:** The index states its own completeness contract — 'Each entry gets a link line below when it merges; reports on unmerged branches are not listed (no dangling links)' — but three merged, tracked reports sitting in the same directory have no row: 2026-07-12-platform-capabilities.md, 2026-07-12-problem-census-satellites.md, 2026-07-12-prompt-architecture.md. The table lists 12 of the directory's 15 reports.

**Actually:** All three files are tracked at HEAD (git ls-files confirms), so under the README's own stated rule their absence reads as 'not merged / on a branch' — which is false. A session consulting this living-ledger index to find whether platform-capability research exists is told it does not. The three are reachable by other routes (docs/AGENT_ORIENTATION.md:47, docs/prompts/v3/per-project/README.md:70, docs/current-state.md:478), so the docs are not orphaned — but the index that declares itself authoritative for this directory is silently incomplete, which is the failure mode the stated contract was written to prevent.

**Check it:** `ls docs/research/*.md | wc -l; grep -c '^| 2026' docs/research/README.md; for f in 2026-07-12-platform-capabilities.md 2026-07-12-problem-census-satellites.md 2026-07-12-prompt-architecture.md; do git ls-files --error-unmatch "docs/research/$f" >/dev/null && printf '%s tracked, in README: ' "$f" && grep -c "$f" docs/research/README.md; done`

**Closed 2026-08-11 (fm #849):** each added row carries the dated note naming this entry, and the platform-capabilities row states the era-note/refutation so the index no longer implies the walls are current. Prove: `grep -c 'Row added 2026-08-11, audit D90/D91' docs/research/README.md` → **3**.

### D92. `docs/review-queue.md:11` — snapshot-as-instruction

> > **BINDING — auto-append rule (ORDER 003, 2026-07-10, program-review §5.2):**

**Claims:** A `living-ledger` doc with no era note declares it BINDING that every PR over 50 changed lines of runtime code, or carrying any self-flagged risk, MUST get a row here appended by its own session before close — and states as standing policy that 'no PR ever waits for review before landing' (line 7), with drain routed to '@codex on all 12 active repos' and 'the manager's failsafe-wake batches'.

**Actually:** Both halves describe apparatus that no longer exists and one half contradicts the live boot file. There is no manager, no failsafe-wake batch and no 12-repo active fleet (program closed 2026-07-21; roster.md shows 0 LIVE rows). The 'no PR ever waits for review before landing' policy is contradicted by .claude/CLAUDE.md:218 — '**Never merge a PR you have asked Codex to review before it answers**' — and by docs/workflow-pr-merge-policy.md, which makes a Codex-clean review of the exact head SHA a precondition for merging any .github/workflows PR. The append rule is also unenforced: `python3 bootstrap.py check --strict` fans out through scripts/preflight.py and never touches this file, and the session-close skill does not mention it. A session that finds this file reads a live-badged MUST it should not obey and a merge policy that the boot file forbids.

**Check it:** `sed -n '3,20p' docs/review-queue.md; grep -n 'Codex to review before it answers' .claude/CLAUDE.md; grep -rn 'review-queue' .claude/skills/session-close/SKILL.md scripts/preflight.py docs/current-state.md .claude/CLAUDE.md; grep -c 'LIVE' docs/roster.md`

**Refuter's correction:** One scope detail is overstated: docs/workflow-pr-merge-policy.md governs `.github/workflows` PRs specifically, not every PR, so its conflict with 'no PR ever waits for review before landing' is narrower than the finding implies. The .claude/CLAUDE.md conflict (line 218, never merge a PR you asked Codex to review before it answers) is exact and unqualified. Everything else in the finding checks out.

**Closed 2026-08-11 (fm #849):** re-badged `historical` with the banner naming both dead halves — the routed-to apparatus (manager, drain batches, 12-repo fleet) and the no-wait-for-review policy the boot file contradicts — and the unenforced BINDING append rule called what it is. Prove: `grep -c 'Era banner, 2026-08-11 (audit D92)' docs/review-queue.md` → **1**.

### D93. `docs/runtime_contracts.md:25` — stale-fact

> All changes land as forward-only git commits through READY PRs to main (ruleset: PR required); control/inbox.md is append-only and owner-written; control/status.md is overwritten by the manager each working session.

**Claims:** A doc badged `Status: binding` states as the repo's current mutation seam that control/inbox.md is the owner-written order channel and control/status.md is rewritten by the manager every working session.

**Actually:** `control/` is seat-era apparatus and .claude/CLAUDE.md lists it under 'Live vs historical' as historical record; there is no manager and no working-session heartbeat, so the second and third clauses describe a bus that stopped on 2026-07-21 (control/README.md was itself re-bannered in the 2026-08-10 D2 pass). Only the first clause (READY PRs to main) is still true. Every other section of this binding-badged file is an unfilled kit placeholder, which is what makes the one filled line read as authoritative.

**Check it:** `sed -n '3p;25p' docs/runtime_contracts.md; grep -n 'control/' .claude/CLAUDE.md | grep -i historical; git show --stat 4b59e9b | grep control/README`

**Refuter's correction:** One sub-claim is wrong on its date: control/README.md was NOT first bannered in the 2026-08-10 D2 pass — it already carried 'RETIRED 2026-07-17' before commit 4b59e9b (which only touched it, per `git log`). The staleness of docs/runtime_contracts.md:25 relative to that banner is therefore ~3 weeks older than the finding suggests, which strengthens rather than weakens it.

**Closed 2026-08-11 (fm #849):** the Mutation seam keeps only the true clause (READY PRs; substrate-gate sole required check) with the two control/-bus clauses quoted as a dated retraction, and the source slot corrected so regens agree. The refuter's date fix is adopted (control/README.md was bannered 2026-07-17, not first in the D2 pass). Prove: `grep -c 'Corrected 2026-08-11, audit D93' docs/runtime_contracts.md` → **1** · `grep -c 'substrate-gate is the sole required check' docs/runtime_contracts.md` → **1**.

### D94. `docs/seat-digest.md:44` — stale-fact

> - `any` · **`api.github.com` direct HTTP**: blocked → GitHub access is MCP-tools-only.

**Claims:** Direct HTTP to api.github.com is blocked, so GitHub access is only available through MCP tools.

**Actually:** Measured false on 2026-07-31 and recorded in docs/CAPABILITIES.md's append log (proxied 403 / direct 200 / direct+PAT 200); .claude/CLAUDE.md states the same. The card in this batch (.sessions/2026-07-31-false-github-api-wall.md, 'Honest null' section) flagged this exact line as the residual gap because the digest renders the kit seed fence only — it is still unfixed 10 days later. The file carries `Status: reference`, not `historical`, and is not in the boot file's seat-era historical list, so nothing tells a reader it is stale. Low traffic (only projects/*/seat-digest.md and bootstrap.py reference it), which is why I rank it below the CAPABILITIES.md finding.

**Check it:** `grep -n 'MCP-tools-only' docs/seat-digest.md; sed -n '1,8p' docs/seat-digest.md; grep -rn 'seat-digest' --include=*.md . | grep -v '^./.sessions/'`

**Refuter's correction:** Accurate, but it is a registered gap rather than a discovery: docs/CAPABILITIES.md:910-917 and the 2026-07-31 session card both name this exact line as the known unfixed residual, with the reason (the digest is a derived render of the kit-owned seed fence, so `bootstrap.py seat-digest` regenerates it byte-identical). Note also that lines 42 and 43 carry the same two false walls as line 44 — the defect is three rows in the digest, not one.

**Closed 2026-08-11 (fm #849, recording only — discharged by fm #846):** the edit pass's seat-digest regen (its Codex round-2 fix 4) propagated the CAPABILITIES retractions through the derived pipeline, and all **three** rows this entry's refuter widened it to (lines 42–44: tag/release, branch deletion, api.github.com) read RETRACTED — verified at `9df0a55` this session **before any edit**, then recorded here, which the edit pass never did. Prove: `sed -n '42,44p' docs/seat-digest.md | grep -c RETRACTED` → **3**.

### D95. `docs/seat-digest.md:36` — contradiction

> Full index (grounds + capabilities): `docs/SKILLS.md` — the source this block derives from.

**Claims:** seat-digest.md's skills block lists 14 kit skills and names docs/SKILLS.md as the source it derives from.

**Actually:** docs/SKILLS.md's table renders only 10 rows — `scope-backlog-item`, `chase-references`, `prep-owner-steps` and `rationalize` are absent from it, though all four are in the vendored kit's SKILLS list (bootstrap.py:14516ff), all four are installed under .claude/skills/, and both seat-digest.md and docs/SKILLS-local.md list them. So the two kit-generated renders of the same list disagree, and the one that self-describes as the full index ('Check this index before improvising a workflow', 'regenerates ... so it cannot hand-drift') is the incomplete one — a session consulting SKILLS.md would conclude four installed skills do not exist.

**Check it:** `for s in chase-references prep-owner-steps rationalize scope-backlog-item; do printf '%s SKILLS.md=%s seat-digest=%s installed=%s\n' "$s" "$(grep -c "\`$s\`" docs/SKILLS.md)" "$(grep -c "\`$s\`" docs/seat-digest.md)" "$([ -d .claude/skills/$s ] && echo yes || echo no)"; done; sed -n '14516,14670p' bootstrap.py | grep -oP '^\s+"name":\s+"\K[a-z-]+' | wc -l`

**Refuter's correction:** Overstated: only TWO of the four (`rationalize`, `scope-backlog-item`) are absent from SKILLS.md entirely. `chase-references` and `prep-owner-steps` DO appear, at lines 87-100 under "## Fleet seed skills — pointer (not kit-shipped yet)", which wrongly says their bodies live in superbot — stale rather than missing. The finding's backticked grep returned 0 for all four because that section writes them bold, not backticked. Also already-known: docs/SKILLS-local.md § "What this roster fixed" (MEASURED 2026-08-08) documents both defects and declares itself the true list until a regen clears them, and .claude/CLAUDE.md routes sessions to SKILLS-local.md for the installed roster — so a boot-path-following session is not misled.

**Closed 2026-08-11 (fm #849, recording only — discharged by fm #846):** SKILLS.md's header now names itself a PARTIAL legacy render, lists the four absent skills, cites this very entry by id, and routes to SKILLS-local.md as the complete roster (the edit pass's D13/D52 fixes plus its Codex round-2 re-scope) — so the render that self-described as the full index no longer does, which was the harm. The seat-digest's kit-templated "Full index" pointer now lands the reader on a header that immediately corrects them; that residual wording is the kit's own template, v1.21.0 track. Prove: `grep -c 'PARTIAL legacy render' docs/SKILLS.md` → **1** · `grep -c "audit's D95" docs/SKILLS.md` → **1**.

### D96. `docs/trigger-health-spec.md:3` — snapshot-as-instruction

> > **Status:** `binding`

**Claims:** The trigger-health per-wake spec is badged `binding` with no era banner, and prescribes a standing ritual over apparatus that no longer exists: 'Group by the seat session it belongs to' (line 43), 'if a seat's pacemaker session has a dropped one-shot AND no future tick armed, treat that seat's chain as DEAD' (44-45), 'for each DEAD-chain / dark seat, `send_message` that seat's session' (46).

**Actually:** The autonomous-Projects program closed 2026-07-21 and the seats no longer exist; the roster was retired 2026-08-07. docs/playbook.md's own mixed-era banner (lines 6-13, dated 2026-08-10) explicitly consigns 'the dispatch, control-bus, roster, wake-chain, and seat-liveness rules' — which is exactly R26, the rule this spec encodes — to the historical column, and names only R1/R2, R16/R17, R22/R24, R29/R30 as still binding. Two live documents therefore disagree: the playbook says this ritual is historical, the spec says it is `binding`. Every other explicitly seat-era surface in the estate (docs/roster.md, control/, telemetry/, docs/prompts/, docs/playbook.md, MISSION.md, docs/NEXT-TASKS.md, docs/fleet-triage.md) now carries a banner at the top saying so; this one does not, and its `binding` badge actively asserts the opposite.

**Check it:** `sed -n '1,5p;40,48p' docs/trigger-health-spec.md; sed -n '6,13p' docs/playbook.md; grep -n -i 'historic\|closed\|superseded\|retired\|no longer' docs/trigger-health-spec.md`

**Refuter's correction:** One detail is overstated: docs/prompts/README.md is badged 'living-ledger', not historical, so 'every other explicitly seat-era surface carries a banner' is not quite exact. The sharper precedent is MISSION.md, which keeps 'Status: `binding`' but adds '**Era note, 2026-08-08 — the mission below is seat-era and its done-when is not measurable today**' — exactly the treatment this spec is missing.

**Closed 2026-08-11 (fm #849):** the MISSION.md treatment the refuter prescribed — badge kept, era note added: no manager wakes, R26 in the playbook's historical class, the roster record-of-record retired and frozen by design, the detection signatures preserved as sound method, and [D‑0015] named for any trigger work. Prove: `grep -c 'Era note, 2026-08-11 (audit D96/D97)' docs/trigger-health-spec.md` → **1**.

### D97. `docs/trigger-health-spec.md:35` — snapshot-as-instruction

> Each manager wake:

**Claims:** A doc badged `Status: binding`, with no era note, states a mandatory six-step per-wake ritual for 'the manager', names docs/roster.md as its 'Record of record', and instructs the reader to 'flag it loudly' whenever docs/roster.md is older than its regen threshold.

**Actually:** There is no manager seat and no wake ritual — the autonomous Projects program closed 2026-07-21 and docs/roster.md was RETIRED 2026-08-07 with both roster-regen cron lines removed (`on: workflow_dispatch:` only in both workflows), so the roster is permanently frozen at Generation #430 by design. A session obeying §6 today would flag the roster as wedged forever. Its own 'Operating rule' anchor, playbook R26, falls squarely in the class docs/playbook.md's 2026-08-10 mixed-era banner calls historical ('the dispatch, control-bus, roster, wake-chain, and seat-liveness rules ... are historical'), and .claude/CLAUDE.md's still-binding list (R1/R2, R16/R17, R22/R24, R29/R30) excludes R26 — yet this spec still carries the unqualified `binding` badge. Nothing in the ordered read path, README, current-state, the program or intent.md links to it, so it is only ever met by a session that greps for it and takes the badge at face value.

**Check it:** `sed -n '3p;35p;53,55p;87,88p' docs/trigger-health-spec.md; sed -n '3,4p' docs/roster.md; grep -n -A2 '^on:' .github/workflows/roster-regen.yml; sed -n '6,13p' docs/playbook.md; grep -rn 'trigger-health-spec' docs/current-state.md README.md .claude/CLAUDE.md docs/reading-path.md`

**Refuter's correction:** docs/reading-path.md (named in the finding's evidence_cmd) does not exist in the tree; the reachability result is unchanged — the grep across CLAUDE.md, README.md, current-state.md and the consolidation program returns nothing.

**Closed 2026-08-11 (fm #849):** the same era note covers this entry — the per-wake ritual and the §6 forever-firing staleness flag are declared seat-era at the top of the file. Prove: `grep -c 'Era note, 2026-08-11 (audit D96/D97)' docs/trigger-health-spec.md` → **1** (one note, both entries).

### D98. `project.index.json:9` — stale-fact

> "MISSION.md",

**Claims:** The records-custody area declares MISSION.md, docs/playbook.md and docs/architecture.md as `binding_docs` ('authoritative contracts to read first'), lists docs/roster.md, telemetry/triggers-snapshot.json and docs/fleet-triage.md among its source_roots, asserts in do_not_create that 'docs/roster.md is canonical', and gives `python3 scripts/gen_roster.py --selfcheck` and `check_roster_freshness.py --advisory` as verification commands.

**Actually:** Every one of those anchors is now explicitly historical. MISSION.md carries an 'Era note, 2026-08-08 — the mission below is seat-era and its done-when is not measurable today'; docs/fleet-triage.md is badged `Status: historical`; docs/roster.md is badged RETIRED 2026-08-07 ('this file is a record, not current truth') so calling it 'canonical' and gating on its freshness is backwards; docs/playbook.md carries a mixed-era banner. This is not an inert doc: project.index.json is a live kit surface (bootstrap.py plants it, EXTRA_SCAN_RELPATHS scans it, and `bootstrap.py contextpack` generates agent context packs from it), so a generated pack instructs an agent to read a seat-era mission as an authoritative contract and to keep a retired roster canonical.

**Check it:** `grep -n 'MISSION.md\|roster.md is canonical\|fleet-triage\|gen_roster' project.index.json; sed -n '3,6p' MISSION.md; sed -n '3,4p' docs/roster.md; sed -n '3,4p' docs/fleet-triage.md; grep -n 'EXTRA_SCAN_RELPATHS\|_adopt_plant(root / "project.index.json"' bootstrap.py`

**Refuter's correction:** The 'generated pack instructs an agent' impact is latent, not realised: `ls .substrate/contextpacks/` returns 'No such file or directory' — no context pack has ever been generated in this repo, so the misdirection only fires if someone runs `bootstrap.py contextpack`. The file-level staleness is nonetheless real and unbannered, and the second area (`control-bus`, folio control/README.md, source_roots control/inbox.md + control/status.md + control/claims) is equally stale — the finding understates the scope by naming only records-custody.

**Closed 2026-08-11 (fm #849):** the stale values are corrected in place — binding_docs leads with `docs/intent.md` instead of the era-noted seat MISSION, do_not_create now says the roster is RETIRED rather than canonical (and the control-bus area says the bus is retired), verification swaps the three retired roster commands for `scripts/preflight.py` + the strict gate — with the top _comment carrying the dated era-correction note and the JSON re-validated. The contextpack consumer remains never-run (the refuter's latency point), so this closes the misdirection before it ever fires. Prove: `python3 -c "import json;d=json.load(open('project.index.json'));a=d['areas'][0];print(a['binding_docs'][0], 'RETIRED 2026-08-07' in a['do_not_create'][0], a['verification'][0])"` → `docs/intent.md True python3 scripts/preflight.py`.

### D99. `projects/UNIVERSAL.md:4` — contradiction

> > **Status:** `living` — v5 · 2026-07-15. **Edit-registry-first:** this file is

**Claims:** projects/UNIVERSAL.md is a `living` document and the source of truth for the owner's standing permissions grant.

**Actually:** It sits inside `projects/`, which projects/README.md (lines 3-9) badges `historical` and says "must not be used to boot a session", and which README.md line 56 calls "explicitly historical". A `living` badge plus "this grant is standing owner authority; it survives session restarts" reads as current truth, and it is the route target of two files in this batch (projects/self-improvement/instructions.md line 61 `UNIV=fm:projects/UNIVERSAL.md`; projects/product-forge/instructions.md line 73). Its content is not inert: line 61 and line 120 both grant "MANAGE YOUR OWN WAKE MECHANICS: create/delete/re-arm your seat's triggers", which contradicts the live `[D‑0015]` rule in .claude/CLAUDE.md ("Never delete a trigger") that .claude/hooks/trigger_tools_guard.py enforces with the estate's only `permissionDecision: deny`.

**Check it:** `cd . && sed -n '1,6p' projects/UNIVERSAL.md && sed -n '3,9p' projects/README.md && grep -n "delete/re-arm" projects/UNIVERSAL.md && grep -n 'permissionDecision' .claude/hooks/trigger_tools_guard.py`

**Refuter's correction:** Ten instructions.md files route to it, not two (ideas-lab, game-lab, self-improvement, fleet-manager, superbot-world, websites, venture-lab, curious-research, superbot-2.0 all carry `UNIV=fm:projects/UNIVERSAL.md (grant v2 + MANDATE)` on line 60/61). Practical harm from the delete-trigger clause specifically is capped by trigger_tools_guard.py's deny; the live-badge-inside-a-dead-tree problem is what makes it a defect.

**Closed 2026-08-11 (fm #849):** re-badged `historical` with the parent-tree contradiction named, edit-registry-first re-tensed to its live-era role, and a [D‑0015] note over the two wake-mechanics grant lines — which stay verbatim as record; the guard hook already caps their practical harm, per the refuter. Prove: `sed -n '4p' projects/UNIVERSAL.md | grep -c 'historical'` → **1**.

### D100. `registry/README.md:11` — stale-fact

> `scripts/gen_roster.py` (regenerated with every roster generation)

**Claims:** registry/lanes.json is a maintained generated artifact with a live named writer, in a directory badged `Status: reference` that instructs 'Do not hand-edit files here.'

**Actually:** Roster generation was retired by owner directive on 2026-08-07: .github/workflows/roster-regen.yml had BOTH cron lines removed (workflow_dispatch only) and roster-freshness.yml carries a matching RETIRED banner; .claude/CLAUDE.md says the roster 'was retired 2026-08-07 and no longer regenerates'. lanes.json is therefore frozen at generation #430 / 2026-08-06T14:57:19Z with no automatic writer, and nothing in registry/ records this. Worse, registry/ is the only surviving output of the retired gen_roster.py that is NOT named as historical: README.md:55-57 lists docs/roster.md, control/, telemetry/, projects/ as 'explicitly historical' and .claude/CLAUDE.md:122-123 lists docs/roster.md, control/, telemetry/, docs/prompts/ — registry/ appears in neither, while being badged `reference`. A session reading it takes lanes.json as current fleet truth, including its seat-era `registry-only` lanes for seats terminated 2026-07-21 (SuperBot World, Ideas Lab, Self Improvement, SuperBot 2.0, Curious Research, retro-games, game-lab) and its `"lane": "shiftlife" … "disposition": "live"` row, which the owner contradicted live on 2026-08-10.

**Check it:** `grep -n 'regenerated with every roster generation' registry/README.md; grep -n 'RETIRED 2026-08-07' .github/workflows/roster-regen.yml; sed -n '116,118p' .github/workflows/roster-regen.yml; grep -n '"generation"\|"generated_at"' registry/lanes.json; sed -n '55,57p' README.md; sed -n '122,123p' .claude/CLAUDE.md`

**Refuter's correction:** Accurate as written. One nuance worth carrying: the sentence is not literally false (a manual `workflow_dispatch` run would still regenerate lanes.json) — the defect is the omission, i.e. registry/README.md records a writer that no longer fires on any schedule and carries no retirement note, while `registry/` is the only surviving gen_roster.py output not classified historical anywhere.

**Closed 2026-08-11 (fm #849):** the README now records both writers retired and both outputs frozen (lanes.json at generation #430 with seat-era rows; kit-versions.md a bannered snapshot) — registry/ is no longer the one surviving gen_roster output unclassified anywhere. Prove: `grep -c 'Writers retired, outputs frozen (2026-08-11, audit D100)' registry/README.md` → **1**.

### D101. `registry/kit-versions.md:7` — stale-fact

> generated-at **2026-07-14T04:49Z** · newest fleet tree version measured: **v1.15.0**

**Claims:** The table is badged `living-ledger`, asserts v1.15.0 is the newest substrate-kit version measured across the fleet, and marks 12 repos CURRENT (= newest fleet tree) on that basis.

**Actually:** 27 days stale at HEAD and factually wrong: this repo itself vendors kit v1.20.2 (.substrate/state.json). Every `CURRENT (= newest fleet tree)` verdict in the table is therefore false, and product-forge's `LAGS newest fleet tree (v1.15.0)` understates its lag by five minor versions. The file's own kill-switch (>7d stale → re-derive) fired 20 days ago, and its regeneration instruction — 'Regenerate with every manager wake that touches kit state' — points at manager wakes that ended with the autonomous program on 2026-07-21, so nothing will ever refresh it. A `living-ledger` badge on a dead generated file is exactly the inherited-conclusion class: a session quoting 'newest fleet version is v1.15.0' would be wrong today.

**Check it:** `grep -n 'generated-at\|newest fleet tree version measured\|Regenerate with every manager wake' registry/kit-versions.md; grep -n '"kit_version"' .substrate/state.json`

**Refuter's correction:** Two notes that sharpen rather than weaken it. The strongest single piece of evidence is not product-forge but the fleet-manager row itself: the file asserts this repo is at v1.15.0 and CURRENT while .substrate/state.json in the same checkout says 1.20.2 — a self-contradiction any session can check in one command. Mitigation the finding omits: the file states its own >7d kill-switch inline, so a reader who reads line 7 is warned before trusting a row; the exposure is the `living-ledger` badge on line 3 plus 12 confident CURRENT verdicts, not a total absence of warning. Fix is cheap — scripts/gen_kit_versions.py still exists and is runnable (`--check` exits 2 on drift); if it is not going to be re-run, the honest move is re-badging the file historical rather than leaving it living.

**Closed 2026-08-11 (fm #849):** ⛔ banner + `historical` re-badge stating the refuter's one-command self-contradiction at the site (the table calls this repo v1.15.0-CURRENT; this checkout's state.json reads 1.20.2), with the refresh path named (the D37-corrected generator) and every CURRENT verdict disowned until someone runs it. Prove: `grep -c 'Status:\*\* `historical`' registry/kit-versions.md` → **1** · `grep -c '1.20.2' registry/kit-versions.md` → **1**.

---

## Stale but harmless — accurate, inert, no action required

Listed so the next session does not rediscover them and mistake them for live
defects. Nothing here needs fixing; several are historical records that are
*supposed* to preserve what was true on their date.

| path:line | kind | what |
|---|---|---|
| `docs/current-state.md:390` | known-example | Layer-2 Tier 1 has been filled with four repo folders, and the remaining repos are present as stubs. |
| `docs/owner-queue.md:1082` | contradiction | Under '## Parked (valid, no rush)': the owner's next Anthropic email is the capability self-knowledge pack, to be sent on the existing Gmail thread. |
| `docs/CAPABILITIES.md:1495` | contradiction | In the folded 2026-07-12 fleet manifest: the GitHub /actions/* admin and /rulesets API paths are walled even in the owner-live credentialed venue, so  |
| `docs/CAPABILITIES.md:238` | stale-count | The doc-routing hook carries 19 routes. Stated twice - also at line 433. |
| `docs/repos/spider-swing/records.md:10` | stale-count | Exactly 28 files in fleet-manager mention spider-swing, and this index covers them. |
| `docs/repos/spider-swing/records.md:63` | stale-count | docs/CAPABILITIES.md is 1,638 lines. |
| `docs/repos/spider-swing/records.md:23` | other | The Layer-2 spider-swing folder's "Research — the Gemini/visual-QA line" table lists three of the four 2026-08-03 Gemini research documents and omits  |
| `docs/repos/spider-swing/working-here.md:9` | broken-ref | The intent doc that ratified this file's shape lives at ../intent.md. |
| `.claude/hooks/README.md:381` | stale-count | The estate's hook inventory is three PreToolUse hooks, one Stop and one UserPromptSubmit (five registrations, five scripts). |
| `.claude/hooks/change_guard.py:15` | stale-count | The estate had three PreToolUse hooks, one Stop and one UserPromptSubmit when this file was written. |
| `.claude/hooks/doc-routes.json:335` | stale-count | docs/repos/spider-swing/records.md indexes 28 dated files about spider-swing. |
| `.claude/hooks/route_docs.py:36` | stale-count | There are 21 probe routes that would have been switched onto prompt matching. |
| `.claude/skills/delegate-read/SKILL.md:9` | stale-count | 'The estate' has 329 session cards (and 391 bench results) — the size that makes a corpus read expensive enough to delegate. |
| `.claude/skills/release/SKILL.md:19` | broken-ref | The canonical prose version of this runbook is at docs/operations/release-runbook.md. |
| `tools/install_root_hooks.py:11` | stale-count | /home/user currently holds four repo clones. |
| `tools/sim/ci_tier_sim.py:24` | broken-ref | The simulation's calibration provenance is calibration-prod.json / calibration-labs.json (and doctrine-constraints.md, cited in the emitted meta at li |
| `scripts/assemble_triggers_snapshot.py:48` | snapshot-as-instruction | The script documents a standing per-wake procedure whose output is the committed telemetry/triggers-snapshot.json consumed by gen_roster.validate_expo |
| `scripts/check_fleet_triage_staleness.py:7` | contradiction | The checker's provenance header treats docs/fleet-triage.md as a living register whose 'verdicts can rot', notes 'the living register is swept ~daily' |
| `scripts/check_lane_liveness.py:30` | stale-fact | The checker's universe of live repos is gen_roster.LANES, presented as the current lane→repo map of the estate. |
| `scripts/emit_routine_claims.py:287` | stale-fact | The fence emitter's default write target is control/status.md, described throughout the module as "the heartbeat file" that "heartbeat writers call th |
| `scripts/gen_roster.py:150` | stale-fact | gen_roster.py's SNAPSHOT CONVENTION docstring repeats that the canonical committed export has records stable-sorted by trigger id. |
| `scripts/gen_roster.py:152` | stale-fact | A headless roster-regen cron runs every two hours at minute 40 and keeps docs/roster.md fresh between manager wakes. |
| `scripts/gen_roster.py:312` | stale-fact | shiftlife is a live lane; 16 of the 25 LANES entries carry disposition "live". |
| `.github/workflows/roster-regen.yml:67` | broken-ref | The owner click that unblocks Actions PR creation is tracked in docs/owner-queue.md under the id OQ-FM-ACTIONS-PR-PERMISSION. |
| `.gitignore:8` | stale-fact | HANDOFF.md is regenerated by substrate-kit at every session boot in this repo, which is the stated reason the ignore entry exists. |
| `.session-journal.md:19` | other | This file is fleet-manager's cross-session process memory, holding the boot runbook, recurring traps and past mistakes so successors don't re-discover |
| `.sessions/2026-07-11-kit-v1121-upgrade.md:80` | contradiction | That on 2026-07-11 the control/status.md heartbeat kit: line still read v1.7.0. |
| `.sessions/2026-07-11-p2-queue-generation.md:95` | stale-fact | That api.github.com returns 403 for agent sessions and that this is an egress-policy wall to be routed around with a github.com HTML-scraping fallback |
| `.sessions/2026-07-11-roster-gen-4.md:52` | broken-ref | The roster generator, described parenthetically as 'already the owed mechanization', is at tools/gen_roster.py. |
| `.sessions/2026-07-12-prompts-v3-1-qa-fixes.md:63` | broken-ref | The B-file regeneration script is at tools/regen_b_files.py. |
| `.sessions/2026-07-12-prompts-v3-2-stateless.md:26` | broken-ref | The regen script that rewrote every seat's FIRST WORK ORDERS into a WORK SOURCES ladder lives at tools/regen_b_files.py. |
| `.sessions/2026-07-13-night-watchdog-2.md:90` | snapshot-as-instruction | Three cards in this batch (night-watchdog-1 line 70, night-watchdog-2 lines 90-111, night-watchdog-3 lines 62-67) carry imperative prune lists naming  |
| `.sessions/2026-07-13-wake-1633z.md:16` | contradiction | Two identical fleet-manager failsafe crons were live simultaneously and double-firing every wake window — the observation that motivated the I8 DUPLIC |
| `.sessions/2026-07-15-registry-v3-5-synthesis.md:42` | broken-ref | The seat-digest drift remedy lives at docs/prompts/tools/seat_digest_sync.py. |
| `.sessions/2026-07-17-fm-recreation-ruling.md:14` | snapshot-as-instruction | The card states, in the present tense and with no supersession marker, that agent self-scheduling of the wake chain is walled in both venues — the exa |
| `.sessions/2026-07-18-fm-owner-steps-revise.md:38` | stale-fact | The card states in the present tense that tools/check_no_false_walls.py is 'still not planted in this repo and no workflow invokes it', so the session |
| `.sessions/2026-07-18-fm-websites-custody-snapshot.md:17` | stale-fact | The card records that GitHub MCP create_pull_request was 'unavailable' and the direct-egress REST POST was classifier-denied from that worker venue. |
| `.sessions/2026-07-21-fm-0042z-cycle.md:58` | snapshot-as-instruction | Worker prompts forbid the EnterWorktree/ExitWorktree tools because three records workers died hanging on an unanswerable EnterWorktree permission prom |
| `.sessions/2026-07-23-hub-forge-slice4-handoff.md:80` | broken-ref | The owner-queue shape checker lives at tools/check_owner_queue.py. |
| `.sessions/2026-08-05-presence-model.md:24` | contradiction | Two cards written the same day on the same branch report different totals for the same session's owner catches — eight here, seven in .sessions/2026-0 |
| `.sessions/2026-08-07-retire-the-roster.md:56` | known-example | The roster's last generation read 21 DARK · 3 UNREADABLE · 0 LIVE. |
| `.sessions/2026-08-08-owner-intent-capture.md:73` | broken-ref | docs/fleet-account-2026-07-26.md line 148 labels fleet-manager "hub + records custodian". |
| `.sessions/2026-08-09-intent-architecture-phase-2.md:178` | other | n/a — the paragraph at lines 178-181 is a verbatim duplicate of the paragraph at lines 172-175. |
| `.sessions/2026-08-09-trigger-tools-guard.md:72` | stale-count | fm #835 grew the trigger-guard suite to 58 cases. |
| `.substrate/backup/bootstrap-1.10.0.py:14655` | stale-count | The kit's planted CLAUDE.md template tells every adopting repo that bootstrap.py is '~12k generated lines'. |
| `.substrate/backup/bootstrap-1.11.0.py:14938` | snapshot-as-instruction | The kit's CAPABILITIES.md.tmpl ships a pre-filled 'Walls — verified blocked' list as seed content: direct api.github.com HTTP blocked, 'Branch deletio |
| `.substrate/backup/bootstrap-1.12.0.py:15264` | stale-fact | Direct HTTP to api.github.com is blocked and GitHub access is MCP-tools-only; branch deletion 403s on every path. |
| `.substrate/backup/bootstrap-1.12.0.py:15265` | stale-fact | `.substrate/` holds kit state plus a byte backup of THE PREVIOUS dist (singular). |
| `.substrate/backup/bootstrap-1.12.1.py:1` | other | Retained as kit rollback state under the upgrade-distribution skill's "banked rollback" step (SKILL.md line 35: "It banks the OLD dist to `.substrate/ |
| `.substrate/backup/bootstrap-1.15.0.py:17829` | stale-fact | The kit's planted CAPABILITIES seed records standing walls — branch deletion 403 on every path, and `api.github.com` direct HTTP blocked so "GitHub ac |
| `.substrate/backup/bootstrap-1.7.0.py:1` | other | These archived dists are the kit's rollback bank — the copies `bootstrap upgrade --rollback` restores. |
| `.substrate/backup/state.json:83` | stale-fact | The fleet_status_command slot answers 'what is the fleet doing?' with 'open docs/roster.md', a roster regenerated roughly every two hours. |
| `.substrate/check-exceptions.yml:72` | snapshot-as-instruction | These (path, kind) carve-outs on the live `check --strict` gate are still needed to suppress false positives. |
| `.substrate/check-exceptions.yml:45` | contradiction | The link suppression at owner-queue-candidates.md is triaged as covering the quoted pokemon-mod-lab link ../docs/play/README.md. |
| `.substrate/check-exceptions.yml:72` | stale-fact | The false-wall suppression on docs/owner-queue-candidates.md is temporary - the offending quoted block will age out of the generated feed at the next  |
| `.substrate/ci/auto-merge-enabler.yml:97` | broken-ref | docs/operations/auto-merge-guards.md documents the fallback landing path. |
| `.substrate/ci/branch-sweep.yml:22` | stale-fact | Agent-side branch deletion is 403-walled; the workflow is 'the sanctioned path around that wall'. |
| `.substrate/claude/CLAUDE.md:41` | stale-count | The vendored dist is about 12,000 generated lines, and .substrate/ holds kit state plus a byte backup of the previous dist (singular). |
| `.substrate/claude/CLAUDE.md:28` | contradiction | A `binding`-badged working agreement declaring the whole boot set to be three items (this file, HANDOFF.md, docs/current-state.md), with the architect |
| `.substrate/episodic_index.json:16` | stale-fact | The episodic index holds one episode - the 2026-07-09 seed-home-repo session, summarised as in-progress. |
| `.substrate/guard-fires.jsonl:9811` | other | This file has a stable content fingerprint that can be recomputed and compared like the other 837 tracked files. |
| `.substrate/guard-fires.jsonl:9806` | other | Raw guard-fire volume in this ledger reflects where the estate's defects actually are (top guards: stale-wall 2,431, stamp 2,351, dateless-wall 1,884) |
| `.substrate/guard-fires.jsonl:1` | other | This ledger is the estate's guard telemetry, fed by both of the kit's guard-fire choke points — `check` and the hook dispatch. |
| `.substrate/skills/upgrade-distribution/SKILL.md:42` | contradiction | Step 7 of the staged `upgrade-distribution` procedure instructs the session to run two commands, both of which are the identical string `python3 boots |
| `.substrate/state.json:83` | stale-fact | The kit's confirmed `fleet_status_command` slot answers 'what is the fleet doing?' with the roster, described as regenerating every two hours. |
| `.substrate/state.json:53` | stale-count | The kit's state records zero sessions, last_compaction_session 0, reflection_buffer last mined 2026-07-09, graduation_proposed false against a 50-sess |
| `CONSTITUTION.md:151` | contradiction | The binding constitution's repo-specific rails section is still the unfilled kit placeholder, so it asserts fleet-manager has no hard rules of its own |
| `CONSTITUTION.md:154` | stale-count | The constitution instructs that the file be kept under 150 lines. |
| `bootstrap.py:19782` | stale-fact | Agent sessions are 403-walled from deleting remote branches on every path (capability-ledger row OA-10), so a scheduled workflow is the only sanctione |
| `bootstrap.py:17725` | stale-count | WORKFLOW_JOB_CENSUS is the complete, ground-truth-read census of every job in every .github/workflows/*.yml, and EXPECTED_CENSUS_GATES = 1 pins 'exact |
| `control/claims/README.md:8` | broken-ref | control/README.md contains a section titled 'Claiming an order' that defines the ORDER-claim carve-out. |
| `control/outbox.md:6` | contradiction | The retirement banner routes a reader's 'next steps' to docs/NEXT-TASKS.md. |
| `docs/AGENT_ORIENTATION.md:39` | stale-count | The playbook is advertised as containing rules R1 through R19. |
| `docs/AGENT_ORIENTATION.md:72` | unreachable-authority | This router reaches every live doc in the repo. |
| `docs/CAPABILITIES-verified-2026-07-18.md:22` | stale-count | The PAT's coverage is admin+push on all 20 repos in the estate (repeated verbatim at line 51: 'Coverage: **admin+push on all 20 repos.**'). |
| `docs/PROJECT-CLOSEOUT.md:228` | stale-fact | §3 item 5, the continuation thread 'Post-close apparatus decision': roster-regen.yml keeps firing ~hourly on dual crons forever and should be reduced  |
| `docs/ROUTINES.md:3` | stale-fact | The wake-chain / routines doctrine binds current sessions. |
| `docs/SKILLS.md:26` | contradiction | The generated skill index lists quality-gate's two commands as the same command twice. |
| `docs/architecture.md:14` | other | A `binding` doc ships the kit template's unfilled placeholders: the layer/import table has one instruction-text row and no layers, and the Invariants  |
| `docs/audits/eap-project-audit-2026-07-14.md:54` | stale-fact | The §3 'Tooling walled or missing' table records, among others, that repo settings/branch-protection/rulesets are unreadable to agents and that direct |
| `docs/conventions/adversarial-review.md:5` | contradiction | The doc declares itself unratified input ('Treat it as input to that work, not as a decided rule'; Honest nulls: 'Unratified. The owner has not adopte |
| `docs/conventions/outbox-rollover.md:52` | snapshot-as-instruction | A `binding` convention (no era banner) assigns first-execution rollover targets to sim-lab and idea-engine and specifies the delivery mechanism as 'OR |
| `docs/dispatch-log.md:3` | stale-fact | The dispatch log is a living ledger of current dispatch activity, appended one line per dispatch. |
| `docs/eap-audit-collection.md:99` | snapshot-as-instruction | A standing update protocol: later sweeps must re-probe docs/audits/eap-project-audit-2026-07-14.md at every one of 13 target repos' HEADs, refill rows |
| `docs/eap-final-email-draft-2026-07-14.md:5` | contradiction | An unsent, still-updatable owner draft with a COPY FROM HERE block awaiting the owner's paste. |
| `docs/eap-owner-checklist-2026-07-14.md:7` | stale-count | docs/owner-queue.md currently holds 63 active items. |
| `docs/eap-owner-checklist-2026-07-14.md:13` | broken-ref | Rows 1/3/6/15 (and the B#5 / B#43 / B#51 / B#59 citations in rows 4, 13, 14) point at live entries E#28, E#58, E#65, E#66, E#67 and those B# ids insid |
| `docs/eap-owner-checklist-2026-07-14.md:5` | snapshot-as-instruction | This is a live, still-updatable owner action list: 47 open rows including '⏰ EXPIRES TODAY' (row 1) and 'window closes TODAY (2026-07-14)' (row 52), p |
| `docs/eap-retrospective.md:27` | stale-count | The fleet-manager playbook runs R1–R27. |
| `docs/execution-surfaces.md:54` | stale-count | The § "What actually changes a prompt" announces four rows and then enumerates them. |
| `docs/execution-surfaces.md:6` | stale-fact | The header dates the whole document's facts to 2026-08-03. |
| `docs/experiments/README.md:13` | snapshot-as-instruction | The index carries `Status: living-ledger` (line 3) and its only row reports the experiment as launching tonight with judging due 2026-07-10 — read tod |
| `docs/experiments/prompts/pair-opus.md:120` | stale-count | Describes the pre-registered judge's WCAG contrast script as 15 lines. |
| `docs/findings/2026-08-05-playtest-discord-and-superbot-value.md:120` | contradiction | superbot loads 61 extensions (also used at line 178: 'Roughly **25 of 61 loaded extensions**'). |
| `docs/findings/2026-08-05-three-repo-state-audit.md:59` | stale-fact | The program's §7 progress ledger has no rows after 2026-07-26 and its NOW pointer still reads E1. |
| `docs/findings/2026-08-05-three-repo-state-audit.md:69` | stale-fact | docs/findings/2026-08-05-playtest-discord-and-superbot-value.md §6 carries no superseded note despite the owner overriding it. Repeated at line 376 in |
| `docs/findings/2026-08-06-checker-classification.md:25` | stale-fact | fleet-manager vendors substrate-kit 1.20.1 and is one version behind. |
| `docs/findings/2026-08-06-checker-classification.md:196` | contradiction | fleet-manager's main has no required_status_checks rule — nothing blocks a merge on a red gate here. |
| `docs/findings/2026-08-06-checker-classification.md:163` | stale-count | The boot file names 25 files, and all 25 resolve. |
| `docs/findings/2026-08-07-what-the-substrate-caught.md:45` | stale-count | Of 11 instrument catches, 13 were Codex findings. |
| `docs/findings/2026-08-08-why-rules-dont-bind.md:88` | stale-count | The repo carries 116 statements of the verify-first rule across 66 files, and the snippet above reproduces those numbers. |
| `docs/findings/2026-08-09-error-to-mechanism.md:137` | broken-ref | § 4b's whole anchor argument is pinned to specific vendored bootstrap.py line numbers, explicitly labelled 'verified rather than inferred'. |
| `docs/findings/2026-08-10-fleet-manager-cold-read.md:115` | contradiction | The repaired three-file cold route yields, as its verified orientation answer, that the next actionable repository is shiftlife. |
| `docs/findings/README.md:37` | stale-count | The findings index tells a session the rollout audit's result is 13 PROVEN / 5 installer PRs still open, and that it feeds a live owner-queue ask for  |
| `docs/findings/README.md:18` | contradiction | The findings index describes ping-test-2026-07-09.md as having its ack sweep still pending at handoff. |
| `docs/findings/README.md:38` | contradiction | The findings index states, as the standing consequence of the 2026-08-10 cold read, that D2 advances to shiftlife. |
| `docs/findings/enabler-install-verification-2026-07-11.md:71` | stale-fact | Direct GitHub REST via curl + token returns 403 ('GitHub access is not enabled for this session'), there is no repo-get / branch-protection / rulesets |
| `docs/findings/fable5-review-2026-07-09.md:180` | broken-ref | Drift-fixes D1/D2 are QUEUED against 'owner-queue item 14', and §7's blueprint amendments are 'owned by the CI-tier sim session'. |
| `docs/findings/gba-toolchain-proof-2026-07-09.md:68` | snapshot-as-instruction | The official devkitPro package infrastructure is unreachable in-container and sessions should not re-probe it; the recipe lives in docs/capabilities.m |
| `docs/findings/instruction-and-env-audit-2026-07-11.md:18` | stale-fact | The audit's fleet-critical headline asserts, in the present tense, that projects/UNIVERSAL.md tells every seat to 'MERGE YOUR OWN GREEN PRs: open PRs  |
| `docs/findings/manifest-parallel-run-2026-07-11.md:45` | snapshot-as-instruction | A decide-and-flag recommendation, written in the imperative and marked 'decided, owner may veto', that docs/roster.md becomes the canonical fleet regi |
| `docs/findings/merge-on-green-rollout-verification-2026-07-15.md:117` | contradiction | The audit doc's final (17:0xZ addendum) headline is 18/19 — 15 PROVEN · 2 INSTALLED-UNPROVEN, naming codetool-lab-opus4.8 and product-forge as never e |
| `docs/findings/merge-on-green-rollout-verification-2026-07-15.md:16` | contradiction | The doc's superseded-headline banner splits 18/19 as 15 proven + 3 installed-unproven. |
| `docs/findings/model-matrix-2026-07.md:76` | broken-ref | The matrix's standing-rule citation points at a section '§ routine self-arm rider' inside docs/capabilities.md. |
| `docs/findings/night-review-2026-07-10.md:1278` | broken-ref | The review's dated Q25 commitment (repeated in ranked recommendation #4 at line 1444) is that the fleet economics ledger lands at docs/findings/fleet- |
| `docs/fleet-account-2026-07-26.md:132` | stale-fact | The records-custody section states the generated docs/roster.md regenerates every ~2h by Actions and is 'still firing'; §5 (line 141) and §4 (line 233 |
| `docs/fleet-account-2026-07-26.md:151` | stale-fact | §3 opens 'Live/active (4)' and lists shiftlife first, verified 'Committing today 18:39Z; API /healthz 200'. |
| `docs/fleet-account-2026-07-26.md:180` | other | The websites row reports the nightly bake still committing, with the PR number prefixed by the CJK token 今日 ('today' in Chinese). |
| `docs/fleet-inconsistencies-2026-07-13.md:7` | broken-ref | The ledger names `fleet-review/notes/<repo>.md` as its declared truth source and as the home of the ~120 raw findings it deduplicates — cited three ti |
| `docs/fleet-inconsistencies-2026-07-13.md:143` | stale-count | INC-49 (unretired, LOW-MED) asserts fleet-manager's decisions register contains a single entry, D‑0001. |
| `docs/fleet-triage.md:910` | contradiction | Sessions should keep re-verdicting register rows against live source, edit rows in place with dated evidence, cross-check the owner-queue for OQ- slug |
| `docs/gen2-blueprint.md:73` | snapshot-as-instruction | The standing operating posture is to spend capacity excessively, because everything produced feeds the owner's post-window consolidation pass. |
| `docs/handoff-2026-07-09.md:18` | stale-fact | All of playbook rules R1 through R21 bind the reading session. |
| `docs/helper-policy.md:26` | other | Status `binding`, 'read this **before** adding a utility function anywhere' — and the section that would tell you where helpers go in fleet-manager is |
| `docs/idea-routing-2026-07-18.md:8` | unreachable-authority | Status `living-ledger`; the routing table's custody model is that 'the recreated per-lane seats (or the owner via a fan-out) pick up the slice for the |
| `docs/merge-queue-2026-07-09.md:7` | snapshot-as-instruction | Status `owner-guidance`; 'Paste this into your merge session and work top to bottom' over a 7-row table of open PRs verified at 2026-07-09T22:41Z, wit |
| `docs/planning/2026-07-19-next-slices.md:226` | snapshot-as-instruction | The doc is badged `plan` and ends with a 'Standing queue' whose item 2 is marked '**NEXT SLICE**' — 'Wake-without-work detector in `check_lane_livenes |
| `docs/planning/2026-07-26-ci-consolidation.md:55` | contradiction | The doc dates the end of the autonomous program to 2026-07-22, twice (line 55 and the pull-quote at line 72: 'roughly 175 serve a program that ended o |
| `docs/planning/2026-08-08-fleet-manager-as-index.md:193` | stale-fact | SKILLS-local.md covers only 13 of the 27 installed skills, omitting session-close, release, review, intake, quality-gate, deep-research, rationalize,  |
| `docs/planning/2026-08-08-fleet-manager-as-index.md:200` | stale-fact | The boot file carries no mention of the @codex review path, so a session's own orientation never surfaces it; stated as a standing owner requirement. |
| `docs/planning/2026-08-08-fleet-manager-as-index.md:89` | other | Recording the supersession in place protects a session from acting on the superseded Tier-2 directive. |
| `docs/planning/README.md:18` | stale-fact | The generated idea backlog indexes every session card's 💡 idea, and grooming passes should start from it. |
| `docs/planning/overnight-menu-2026-07-17.md:3` | snapshot-as-instruction | A standing 'veto-ready menu' of 25 fleet-manager proposals for the owner's filter pass, carrying no era marker, linked from the live docs/current-stat |
| `docs/prompts/README.md:5` | stale-count | This index is the verbatim record of every prompt deployed to the fleet, and its index table plus the v3/external sections enumerate the directory. |
| `docs/prompts/README.md:21` | contradiction | The index of deployed prompts records the universal gen-1 wind-down prompt as never deployed. |
| `docs/prompts/game-lab-founding.md:166` | stale-fact | The game-lab founding instruction has never been pasted; the launch clicks are still outstanding in the owner queue. |
| `docs/prompts/v3/README.md:18` | snapshot-as-instruction | Reads as a standing operational recipe — six numbered steps and a nine-row live-seat index — for founding or re-founding a seat today. |
| `docs/prompts/v3/final-closer.md:22` | contradiction | A seat closing down must delete every trigger it created, and relay the deletion through a worker if it is walled. |
| `docs/prompts/v3/per-project/README.md:103` | stale-count | The 'v3.8 size table (real counts, checker-verified 2026-07-18)' states the current per-seat Custom-Instructions and startup character counts. |
| `docs/prompts/v3/per-project/curious-research-startup.md:12` | snapshot-as-instruction | Reads as a live, standing identity brief with imperative boot steps ('BOOT NOW, in order', 'ARM YOUR ROUTINES') for a seat that still exists. |
| `docs/prompts/v3/per-project/curious-research-startup.md:4` | stale-count | The paste body is 37,263 chars. |
| `docs/prompts/v3/per-project/fleet-manager-custom-instructions.md:12` | contradiction | The seat's Orientation route sends a booting session to read docs/roster.md as one of three orientation documents. |
| `docs/prompts/v3/per-project/fleet-manager-custom-instructions.md:4` | stale-count | The paste body is 7,963 chars / 7,996 bytes, leaving 4 bytes of headroom under the hard 8,000 console cap. |
| `docs/prompts/v3/per-project/fleet-manager-startup.md:160` | contradiction | SESSION ENDER step 3 orders a session to delete its triggers, including the failsafe cron, and step 'Confirm before ending' (line 164) asks it to 'rec |
| `docs/prompts/v3/per-project/fleet-manager-startup.md:69` | stale-fact | docs/roster.md is a live rung of the WORK SOURCES ladder whose rows should be re-verified against live GitHub. |
| `docs/prompts/v3/per-project/self-improvement-startup.md:4` | stale-count | The paste body below the header block is 36,493 characters. |
| `docs/prompts/v3/per-project/superbot-startup.md:4` | stale-count | The paste body below the header block is 36,853 characters. |
| `docs/prompts/v3/per-project/superbot-startup.md:141` | contradiction | A session ending its turn must delete its triggers, and if the delete is refused it must route around the refusal via a spawned worker until the delet |
| `docs/prompts/v3/per-project/superbot-world-custom-instructions.md:15` | snapshot-as-instruction | superbot-games has no landing workflow, so installing merge-on-green is the seat's standing first slice and green PRs there wait until it lands. |
| `docs/prompts/v3/per-project/superbot-world-startup.md:4` | stale-count | The paste body below the header block is 36,535 characters. |
| `docs/prompts/v3/per-project/venture-lab-startup.md:4` | stale-count | The paste body below the header block is 35,905 characters. |
| `docs/prompts/v3/per-project/venture-lab-startup.md:140` | contradiction | At session end the Venture Lab seat must delete every routine it created including every business cron, normal or fresh-session-per-fire — no exceptio |
| `docs/prompts/v3/per-project/websites-startup.md:8` | snapshot-as-instruction | A standing owner grant, in the owner's first person, authorising the reader to decide, build and self-land on green CI, and to outrank any restriction |
| `docs/prompts/v3/tools/regen_b_files.py:33` | stale-count | There are eight seat startups to re-splice when the canonical session ender changes. |
| `docs/prompts/venture-lab-draft.md:124` | stale-fact | The venture-lab gen-2 founding instruction has not been deployed; the lane is still waiting on the owner's launch clicks. |
| `docs/proposals/README.md:9` | stale-count | This table is the index of docs/proposals/, and it enumerates four documents. |
| `docs/proposals/generated-roster-from-heartbeats.md:52` | stale-fact | docs/roster.md is (or is to be) a generated artifact regenerated on every manager wake, with check_manifest_freshness.py retiring into it. |
| `docs/proposals/instructions/README.md:15` | contradiction | None of the ten founding-instruction packages in this folder has been deployed. |
| `docs/proposals/instructions/game-lab.md:148` | stale-fact | No archetype covers a GBA cross-compiler, so game-lab is assigned python-lab plus a per-repo env-setup.sh hook rather than a new archetype — "decide-a |
| `docs/proposals/instructions/mobile-lab.md:241` | stale-count | The owner directive caps the fleet at 4 archetypes, so this package "deliberately does NOT propose a fifth archetype". |
| `docs/proposals/instructions/trading-strategy.md:3` | contradiction | The file's own status badge says this package was never deployed. |
| `docs/proposals/instructions/trading-strategy.md:14` | broken-ref | The lane's entire relaunch is gated on a numbered owner-queue item ("item 1"), and "owner-queue item 5" is the archive-the-dead-session click (L319, L |
| `docs/proposals/instructions/venture-lab.md:18` | broken-ref | Header L5 cites "owner-queue item 14" as a source, L15 asserts "Owner-queue item 14's \"github.com/new\" step is stale", and L356 routes the owner to  |
| `docs/q-index.md:61` | contradiction | Program law is kit-owned per decision D‑0002. |
| `docs/repo-navigation-map.md:12` | other | This table records where things live and where new code goes. |
| `docs/research/2026-07-12-problem-census-core.md:759` | snapshot-as-instruction | Standing boilerplate — explicitly headed '(goes in ALL fleet Project instructions)' — that docs/roster.md is the one live fleet roster. |
| `docs/research/2026-07-12-problem-census-core.md:3` | missing-certainty-marker | The core census is current reference material, with no in-file staleness rider. |
| `docs/research/2026-07-12-prompt-architecture.md:1` | unreachable-authority | This merged research deliverable is discoverable through the research folder's ledger. |
| `docs/research/2026-07-12-qa-boot-simulation.md:431` | contradiction | Reading a repo's branch-protection ruleset / required-check set is capability-walled for an agent, so sessions should route around it via a probe PR's |
| `docs/research/2026-07-12-qa-incident-replay.md:253` | stale-fact | Three named sibling reports are not in this tree (they live on unmerged research branches), and one of them is called 'problem-census-labs'. |
| `docs/research/2026-07-12-qa-incident-replay.md:245` | snapshot-as-instruction | Five owner-queue entries are owed: the websites Actions-PR toggle, env-teardown trigger auto-disable, venture-lab PR #51 photo takedown (HOT, 'erodes  |
| `docs/research/2026-07-12-qa-incident-replay.md:3` | contradiction | The research ledger states 'Each doc is `reference`' for the whole folder. |
| `docs/research/2026-07-12-repo-consolidation-census.md:521` | snapshot-as-instruction | The census closes with a three-phase work programme written in the imperative present — "can start now (all agent-doable)", "All migration PRs in phas |
| `docs/research/README.md:6` | stale-fact | The index header asserts that every document in docs/research/ carries the `reference` status badge. |
| `docs/retro/archive-ready-2026-07-11.md:51` | snapshot-as-instruction | Under the heading "What a fresh session needs to resume", the doc states the routing chain for a fresh session: projects/fleet-manager/reboot-prompt.m |
| `environments/archetypes.md:122` | stale-count | A `living-ledger` doc claims to map EVERY current and planned project to an environment archetype, and enumerates 20 repos (substrate-kit, codetool x3 |
| `environments/env-grant-policy.md:10` | broken-ref | The hard-rule line links a document called RAILWAY-SAFETY.md, and the See-also section (line 130) points at `../docs/RAILWAY-SAFETY.md`. |
| `projects/UNIVERSAL.md:61` | contradiction | The owner-landed permissions grant in projects/UNIVERSAL.md (Status: `living`, v5 2026-07-15), repeated verbatim at line 120, grants every seat standi |
| `projects/_inventory/trigger-registry-2026-07-10.md:10` | snapshot-as-instruction | Standing procedure: whoever re-arms a trigger must re-extract the full list_triggers registry and update the affected seat's failsafe-prompt.md, and o |
| `projects/curious-research/meta.md:37` | stale-fact | All three generated parts in projects/curious-research/ are at prompts generation v3.7 and are registry-current, with an owner re-paste to v3.7 outsta |
| `projects/fleet-manager/coordinator-prompt.md:152` | contradiction | A session ending its turn must delete every trigger it created — the pending send_later pacemaker, every session-bound wake trigger, and the seat fail |
| `projects/fleet-manager/seat-digest.md:17` | stale-fact | This registry render is a VERBATIM byte-match extraction of docs/seat-digest.md, whose content hashes to 10565e4c8d8f. |
| `projects/fleet-manager/seat-digest.md:44` | known-example | Direct HTTP to api.github.com is blocked, so agents can only reach GitHub through MCP tools; and (line 43) branch deletion 403s on every path. |
| `projects/game-lab/coordinator-prompt.md:150` | snapshot-as-instruction | A pasted seat session must delete every trigger it created at session end (and, in BOOT step 4, delete predecessor trigger ids). |
| `projects/game-lab/meta.md:13` | contradiction | gba-homebrew is Track B and pokemon-mod-lab is Track A. |
| `projects/game-lab/meta.md:24` | stale-count | As of 2026-07-18 each of the three registry parts is at v3.7 and is registry-current. |
| `projects/product-forge/handoff/2026-07-23-phone-controller-slice4/land.sh:1` | broken-ref | The handoff's documented one-command ritual is `./land.sh` (README.md line 41; the script's own NEXT block references the same invocation). |
| `projects/product-forge/instructions.md:73` | stale-fact | The permissions block quoted below this line is the current fleet-canonical grant, verbatim from projects/UNIVERSAL.md. |
| `projects/product-forge/meta.md:27` | stale-fact | fleet-manager's environments/ registry has no entry for product-forge, so a spec is still owed. |
| `projects/self-improvement/coordinator-prompt.md:150` | snapshot-as-instruction | A session ending its work must call delete_trigger on every routine it created, and confirm zero routines remain. |
| `projects/self-improvement/meta.md:6` | contradiction | Nothing of this seat package is deployed and its instructions.md is still the never-pasted v1 authored during the 2026-07-11 restructure. |
| `projects/superbot-2.0/coordinator-prompt.md:151` | contradiction | A session ending its work must call delete_trigger on every routine it created — the failsafe cron, the pending send_later pacemaker, every business c |
| `projects/superbot-2.0/instructions.md:21` | snapshot-as-instruction | These seat packages are standing, owner-signed instructions that survive restarts and outrank any rule lacking owner provenance. |
| `projects/superbot-retro/meta.md:7` | stale-fact | The retired Retro-Games seat's failsafe trig_01Y99uDKNtKTz2EtRYPWZkGY and hourly child wakes trig_0137SkvhXEJvwepX8aVNkcSn / trig_01BTJjkMVMKtWPjuYe76 |
| `projects/superbot-world/meta.md:16` | stale-fact | Three named old-seat failsafe triggers (games trig_019ZgWyL78Rx1sr6LhvL8NE3, idle trig_01TWKGFW8RUsMvxUMt2ndzqA, mineverse trig_01K8xmAKYS5S2HLy1HPANM |
| `projects/venture-lab/meta.md:24` | contradiction | The package's setup-script.sh is the probe variant of the python-lab archetype for the console env field, probing STRIPE_SECRET_KEY, STRIPE_WEBHOOK_SE |
| `projects/venture-lab/meta.md:6` | snapshot-as-instruction | venture-lab is live but clockless, its heartbeat stale, three ORDERs unexecuted at control/inbox.md, and it is the sharpest state-risk in the fleet re |
| `projects/websites/coordinator-prompt.md:151` | snapshot-as-instruction | The session ender orders wholesale trigger deletion (pacemaker, wake triggers, the failsafe cron, business crons) and BOOT step 4 describes a delete-b |
| `projects/websites/meta.md:54` | contradiction | meta.md's header stamp and its whole 2026-07-18 Deployed-state table record all three parts (instructions / coordinator-prompt / failsafe-prompt) as v |
| `substrate.config.json:71` | contradiction | docs/AGENT_ORIENTATION.md is one of exactly two declared boot read-path roots, used by bootstrap.py's check_reachable to certify that 'Every live doc  |
| `telemetry/README.md:15` | stale-fact | The committed telemetry/triggers-snapshot.json has its records stable-sorted by trigger id. |
| `telemetry/README.md:43` | stale-fact | Dump-recipe step 4 instructs writing the snapshot with 2-space indent, sorted keys and a trailing newline. |
| `telemetry/README.md:59` | stale-count | An enumeration of everything a trigger record in the snapshot holds: ids, crons, timestamps, session ids, and stored wake prompts. |
| `telemetry/README.md:23` | stale-fact | The roster-regen cron runs every 2h at minute 40 off the committed snapshot, and the six-step 'Dump recipe (manager wake, REQUIRED + verified)' plus t |
| `templates/worker-preamble.md:3` | unreachable-authority | These preamble blocks are a living ledger to be pasted verbatim into every worker prompt. |

