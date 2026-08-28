# The kit-tree truth pass — 187 files at `a9acc41`, and the two owed checks

> **Status:** `audit` · 2026-08-28 · OD-24 review round, **session 3** (the
> round thread's "next audit"; the two owed checks are the router band
> re-read's §1 items 4–5, cited there as owed to the round)
>
> **Method.** Local read-only clone of `menno420/substrate-kit` at
> `a9acc413644ceb1fa48851744d7082b5fa1ce1a6` (= origin/main, re-verified this
> session; kit-quality green on the merged head `44b9847`, 0 open kit PRs).
> The whole committed **doc surface** — 187 files: all of `docs/` including
> the nine subdirectories the genesis dig's §9 names as skipped **plus
> `docs/succession/`, which that skip list never even named**, the root docs,
> `control/`, `telemetry/`, `.substrate/`, `.github/`, `bench/README.md`,
> `.sessions/README.md` — was read **in full** by 19 reader lanes, each
> primed with the session's re-verified anchors and an honest-null
> expectation; two dedicated agents answered the owed checks; every
> non-obvious verdict (32) and both owed answers (2 lenses each) then went
> through an adversarial verify pass — **57 agents, ~4.5M subagent tokens,
> 0 errors**. Coverage is whole-population by construction: assigned = 187,
> returned = 187, checked in code, nothing swept. Verdicts are `REVIEWED`
> (lane + adversarial verifier); every load-bearing claim cites `path:line`
> at the named SHA. **27 of 32 doc verdicts and 4 of 4 owed-check lenses
> were upheld unchanged; the five corrections — three line-cite offsets, one
> verdict class, one recommendation class — are applied in this text and
> named in §6.** The owed checks' source text is the frozen superbot router,
> fetched raw once this session (668,746 bytes — size-identical to the
> re-read's recorded fetch; no clone, no write; Q-0213/Q-0214/Q-0241 bodies
> extracted verbatim).
>
> **The one-paragraph result:** the kit's doc surface is **mostly honest
> history** — 104 of 187 files are dated records, and the era-banner
> discipline held on nearly all of them — but the failure class is
> **concentrated and current-truth-voiced**: the 22-file wrong-action set
> speaks in the present tense and carries month-or-seven-week-old claims
> that would misdirect a cold session today (the reconcile pair this session
> executes, a stalled ideas-conveyor cohort presenting shipped work as open,
> five apparatus docs with no era banner, and a standing-walls set that
> contradicts the estate's never-write-down-a-limitation doctrine). The two
> owed checks both came back **better than the round's working assumption**:
> PL-002's canonicalization **preserves** Q-0241's rebuild-only scope at the
> canonical block, and the kit **did ship** most of Q-0214's
> delete-with-tombstones retention posture as working mechanism — shipped,
> unconfigured on the kit's own 342-card corpus at HEAD, and trace-free
> there (no evidence it has ever run on it).

## 1 · Headline numbers

**187 files judged:** 104 historical-record · 23 stale · 20 live · 21
generated · 15 reference · 4 superseded. **Dispositions:** 143 keep · 22
banner-or-fix-in-round · 19 keep-live · 1 regen-only · 1 supersede-pointer ·
1 archive-recommend. *(Totals recomputed mechanically from the appendix
after all seven verdict corrections — the workflow verify pass's five plus
Codex fm #960's two; an earlier cut published the pre-correction totals, the
exact drift class this audit hunts.)* 0 deletions recommended
(OD-3-as-amended examined; every
candidate is either honest dated history, cited provenance, or CI-enforced
apparatus). The full 187-row table is the appendix; §4 carries the
wrong-action set in detail; §5 turns the un-executed rows into
recommendations, dig-§10-style.

## 2 · Owed check A — does the kit's PL-002 canonicalization preserve superbot:Q-0241's rebuild-only scope? **YES at the canonical block; one provenance mislabel in three derived copies**

*(Answers [the router band re-read](2026-08-28-router-band-reread.md) §1
item 5. Source: the frozen router's Q-0241 block — its scope paragraph and
the Q-0213 item-4 brake — fetched raw this session. Both adversarial lenses
upheld this answer.)*

**Preserved, both halves, essentially verbatim.** The canonical block
`kit:docs/program/rulings.md:40-71` carries a dedicated scope field
(`:66-68`): *"The rebuild program. The live production bot keeps superbot's
Q-0213 ask-first `*Delete`/`*Restore` brake and prod-data safety until the
owner generalizes this — he can extend PL-002 to all work at any time."*
That is (a) rebuild-program-only scope (also in the header `:40`, "Never-wait
autonomy for the rebuild") and (b) the standing Q-0213 production brake with
the owner-extendable clause — matching the source scope paragraph's own
summary wording, under the register's cite-the-ID-never-copy rule (`:9-10`).
The founding plan mandated exactly this shape
(`kit:docs/planning/kit-lab-founding-plan-2026-07-07.md:632-633`: *"verbatim
to its provenance: never-wait, scope = the rebuild program,
owner-extendable"*). The program's own restatements keep the scope:
`agent-decision-authority.md:37-39` ("Inside its scope (the rebuild
program)…"), `CONSTITUTION.md:71` ("PL-002 never-wait **rebuild** autonomy"),
and PL-009 explicitly refuses to smuggle the lab's autonomy into PL-002
(`rulings.md:198-199`).

**The scope's expiry clause was then exercised by the owner, not dropped.**
PL-012 (`rulings.md:285-366`, provenance superbot:Q-0271, owner directive
2026-07-12) generalizes never-wait fleet-wide for seat work and is explicit
about the relationship: *"Extends PL-002, does not supersede it… PL-002's
scope deferral ('he can extend PL-002 to all work at any time') is discharged
by this block for seat work"* (`:360-366`) — with **item 6's owner-only list
as the brake that survives generalization** (`:323-326`: external publish +
spending money · destructive prod-data ops stay ask-first), which is where
Q-0213 item 4's substance now lives fleet-wide. What the kit **plants in
adopters** is PL-012's operating form with that ask-first list inline
(`src/engine/templates/CONSTITUTION.md.tmpl:97-98, :105, :123-126`; the
embedded copy in `dist/bootstrap.py` verified byte-identical this session) —
never an unscoped PL-002.

**The one genuine drop — a derived sentence in three copies.**
`docs/owner-profile.md:11` = `.substrate/claude/CLAUDE.md:61` =
`.substrate/state.json:63` all carry: *"agents build end-to-end under program
law: decide-and-flag (Q-0240) and never-wait (Q-0241 — silence = consent,
control is reacting to what ships)."* That is an **affirmative
generalization attributed to Q-0241**, carrying neither half of the scope
clause. The behavior it describes IS owner-authorized — but by Q-0271/PL-012
— so this is a **provenance mislabel presenting the scoped ruling as
unscoped law**, not unauthorized scope creep. Disposition: §5. Two side
notes: three surfaces miscite "enforce, don't verify" as PL-002 where the
enforce doctrine is PL-007 (`auto-merge-disarm.yml:12-13`, one idea file, one
2026-07-09 card) — scope-neutral; and the scope field's Q-0213 sentence is
protected by the register's append-only grammar plus
`tests/test_rider_graduation.py:164-167`'s header/non-supersession pins, but
is **not itself verbatim-pinned by any test** (`check_program_law.py` treats
`scope` as optional grammar). Q-0213 appears exactly once in the whole kit
tree (`rulings.md:66`).

## 3 · Owed check B — did the kit ship any of superbot:Q-0214's delete-with-tombstones retention posture? **PARTIALLY — most of it, as working mechanism; unconfigured and trace-free on the kit's own corpus**

*(Answers [the re-read](2026-08-28-router-band-reread.md) §1 item 4, which
recorded "whether the kit shipped any of it is unexamined". Both adversarial
lenses upheld this answer.)*

**Decision 1 — "Delete + tombstones", harvest-gated: SHIPPED MECHANISM**, in
v1.0.0 (2026-07-09, seven days after the ruling). The context-economy
package `src/engine/economy/` ships the posture nearly verbatim: the default
sessions class is `"mode": "delete_tomb", "window_days": 14, "tombstone_dir":
"<sessions_dir>/pruned"` (`engine.py:46-48`; labelled "a STARTING POINT, not
shipped policy" — the kit deliberately ships the search, not superbot's
constants, `engine.py:62`); every deletion is gated by the **triple filter**
(harvested AND past window AND zero inbound refs, `engine.py:5-8`) with
`harvest.py` parsing committed pass-record harvest tables as the delete-side
safety input — Q-0214's "harvest-gating… the safety condition" exactly; one
~20-word grep-visible tombstone line per pruned file into per-band shards
(`engine.py:445-448, 461-495`), bodies one `git show` away; and an
unattended-safety ladder shadow → gated (first prune needs explicit
`--reviewed`) → normal (`config.py:70-87`) — deletion "the one place the
kit's fail-open posture inverts". Tested
(`tests/test_economy.py:335`), advertised (`README.md:36-41`), in the v1.0.0
changelog (`CHANGELOG.md:3107`). The retention-policy simulator itself is "a
generalized port of superbot's `tools/sim/retention_policy_sim.py`"
(`simulator.py:3`).

**Decision 3 — "Shrink duty = checker + routine": shipped at the
checker/actuator/emitter level; the routine itself is host-side.**
`economy check --strict` exits 1 on findings or debt ≥ threshold
(`cli.py:3068-3072`); the SessionStart hook renders an economy advisory
(`hooks/session_start.py:141-149`); `economy issue-body` renders exactly
"the retention-debt routine issue body" (`engine.py:592-595`) — but **no
routine/workflow that schedules or posts it ships**, and economy is
deliberately NOT in the default `check --strict` gate (consistent with "no
new per-session shrink ritual").

**Decision 2 — the `/updates` owner feed: NONE.** Zero hits for `/updates`
anywhere in the kit; `export_dashboard_data.py` appears once, in a recipe,
about a different contract. (Plausibly correct scoping — the decision bound
superbot's own plan PR 2 — but factually the kit carries neither mechanism
nor mention. The decision's 14-day floor does surface as the default
`window_days: 14`.)

**The dogfooding gap, measured:** the kit's own `substrate.config.json` keeps
`economy.classes: []` and `maturity: "shadow"` (`:22-23, :31`); its
`.sessions/` holds **342 dated cards (plus the README) with no
`.sessions/pruned/` directory** — the shipped delete-with-tombstones
machinery is **unconfigured at HEAD and has left no trace of ever running
on the kit's own corpus** (what the tree can prove: no prune artifact, no
tombstone shard, empty class config; run history beyond the tree was not
examined). The posture exists in shadow; the corpus is not bounded in
practice. Provenance note: the kit names Q-0214 by ID exactly once
(`src/engine/ledger.py:3`, the .4 depth choice), proving the decision set
reached the kit lanes.

**What this corrects upstream:** the genesis dig's §4 lost-in-extraction
table had no retention row and its §8 carried "the EAP-era answer to
maintain-cost was generation + checkers, never fewer files". The missing row
reads **"NOT lost — extracted and generalized"**: a real fewer-files layer
shipped in v1.0.0. What did not ship is decision 2's owner-feed coupling,
the scheduled retention-debt routine, and any activation on the kit's own
tree. In-place narrowing pointers added at both dig claim sites and at the
re-read's two owed lines (this PR).

## 4 · The truth pass — what the doc surface actually is

**The counter-headline first, because it is most of the tree:** 104 of 187
files are dated records — retros, reports, succession notes, gen2 snapshots,
executed plans, seat-era cards' index — and **the era-banner discipline
mostly held**: the overwhelming majority self-declare their date or era, and
17 lanes returned explicit honest-null notes of the form "all clean
self-bannered history". The 21 `generated`, 20 `live` and 15 `reference`
files verify against the tree (all four version homes read 1.21.0; the PL
register matches the anchor exactly; `docs/NEXT-TASKS.md` — the round's own
session-2 fix — verifies as exactly the supersession pointer it should be,
its terminal-state table's three cheap claims re-checked true). `CHANGELOG.md`
is live with an empty `[Unreleased]` over kit #587's merges — the kit's own
cut-time reconciliation convention, not a defect.

**The failure class is concentrated: ~20 current-truth-voiced files.**
Grouped, with the full per-doc detail in the appendix:

- **(a) The reconcile pair — executed this session, in the kit's venue.**
  `docs/current-state.md` (headline "Kit is at **v1.20.2**… the only open PR
  is #552" at `:31-34` — false on both counts at HEAD: four version homes
  read 1.21.0, #552 merged 2026-08-04, 0 open PRs; "No adopter tree has been
  upgraded… the v1.20.0 wave is the TOP next task → NEXT-TASKS.md #1" at
  `:72-75` — doubly false since the v1.21.0 wave and kit #587's supersede;
  "Next action → the provenance mandate" no longer the live worklist route)
  and `control/status.md` (the "freshest single surface", header freshly
  stamped v1.21.0 on 2026-08-13 — but its 2026-07-21 closeout body still
  says "#552 = parked for owner ratification"). This is the supersede
  table's "still open — belongs to the review round" item 4, and it is this
  session's kit PR.
- **(b) The stalled ideas conveyor — gap #1's measured instance.**
  `docs/ideas/README.md` presents already-built work as next groom targets
  and every "survive window" expired 2026-08-08..18 unflipped; four idea
  files still read `captured/open` while their deliverables are in the tree
  with PR receipts (`guard-parity…` — shipped as #459/v1.19.0, cited by the
  changelog **by this file's own path**; `make-seed-yield-keyword-bug…` —
  the fix's docstring cites the idea file; `archive-ready-close-out-surface…`
  — S1–S4 shipped in v1.18.0; `control-board-kit-readiness-cell…` — the
  remaining half targets retired seat apparatus). The intake/frontmatter
  machinery is live and CI-enforced; **the flip half stalled at program
  close** — the conveyor's demand side died, exactly the dig's gap #1.
  Route, not rebuild: the fixes are frontmatter flips in the conveyor's own
  grammar; the *mechanism* answer (Move 1's `♻ Carried forward`) stays held
  with the plan.
- **(c) Five apparatus docs with no era banner.** `control/README.md`
  (live-voiced protocol directing every session to execute `status: new`
  inbox orders), `control/inbox.md` (all 24 seat-era ORDERs still read
  `status: new`, including ORDER 010 "arm an hourly routine" — trigger
  territory — adjacent to the estate's never-delete-a-trigger decision,
  stamped in [`../decisions.md`](../decisions.md)), `docs/operations/lab-loop.md` (binding-marked
  runbook for a console Schedule that closed 2026-07-21; could revive the
  retired P4 owner ask), `docs/planning/README.md` (its "Active" tier
  presents an ORDER-025 veto menu as pending; omits the two newest planning
  docs — the provenance mandate is invisible from the index),
  `docs/planning/kit-lab-founding-plan-2026-07-07.md` (still badged "the
  executable founding plan"; its §6.1/§7.2 order actions on closed
  apparatus, and its §4.1 release mechanic — tag-push — is incomplete for
  agents: the workflow supports both triggers, tag push owner-side canonical
  and workflow_dispatch the only agent-runnable path, the git proxy 403ing
  tag pushes — precision from Codex R1 on kit #588), plus
  `docs/planning/2026-07-19-night-run-idea-groom-wave2.md` (the groom
  chain's terminus, no exhaustion banner, 10+ of its 16 "open" ladder items
  verifiably shipped) and `docs/planning/2026-07-12-grounded-skills-program.md`
  (supersede-pointer: "§7: None is implemented" while its same-day wrap
  report proves all 8 slices shipped).
- **(d) Standing walls and spent conditionals.** `docs/CAPABILITIES.md`'s
  "Walls — verified blocked" section still carries seat-era walls
  (api.github.com "blocked → MCP-tools-only"; branch deletion "403 on every
  path → owner deletes by hand") that the estate's verified direct-PAT
  matrix disproves — a cold session obeying them queues owner asks for
  normal agent work, the exact class `check_no_false_walls` exists to
  prevent, resident in the checker's own repo. `README.md`'s regen line
  (`python3 substrate-kit/src/build_bootstrap.py`) fails from the repo root
  — pre-extraction residue; CI runs `python3 src/build_bootstrap.py`.
  `.session-journal.md` asserts "👤 P10 still pending" when kit-quality IS
  the single required check (re-verified live this session) — the journal
  surface itself carrying a spent owner ask, grist for the round's journal
  letter. Same P10 conditional in `docs/operations/auto-merge-guards.md`
  (plus "guard 5 rides open PR #17" — the gate is enforcing today);
  `docs/recipes/README.md`'s deferral line invites building a checker that
  already ships; `docs/fleet-repos.txt` — the **live regen input**
  (`currency.py:83`) — omits five real adopters, so the next regen ships an
  incomplete registry (the round thread already carries this roster gap);
  `docs/house-style.md` one false table cell; `docs/ai-project-workflow.md`
  one stale slot value (hand-edit — the verifier established `render
  --live` cannot reach an already-substituted slot); `telemetry/README.md`'s
  false operational guarantee (outcome fields "are backfilled by the lab
  loop's telemetry sweep" — the loop closed 2026-07-21 and all 143 rows
  carry null outcomes); and `docs/repo-navigation-map.md`, stale by its own
  completeness invariant (a placeholder-only table that routes nothing —
  both raised on Codex review of fm #960).
- **(e) One archive-recommend.** `control/status-gba-homebrew-trackb.md` —
  a self-terminal visiting-lane heartbeat whose own header pre-authorizes
  disposal after the visit closed (2026-07-10); archiving executes the
  file's own instruction.

## 5 · Dispositions — recommendations ONLY (the dig-§10 shape; nothing executed this session beyond the named reconcile)

The reconcile pair (a) lands in this session's kit PR. Everything else below
is **recommended, not executed**. Every row **except the last** is
agent-executable in one future round session (a kit doc-surface truth
sweep), none owner-gated, no new apparatus proposed anywhere — every fix a
record edit in an existing grammar. **The last row is the carve-out**: it is
a flagged *decision* about activating deletion machinery, explicitly outside
the records sweep, and no future session may read this table's blanket as
pre-approving it:

| set | the fix | the one reason |
|---|---|---|
| (b) conveyor flips: `docs/ideas/README.md` + 4 idea files | frontmatter flips (`state`/`outcome`/`shipped_pr`) + README section moves, in the conveyor's own enforced grammar | shipped work presented as open sends a groom session rebuilding existing deliverables; the flips are the record half of gap #1 — Move 1's `♻` mechanism stays held for the owner |
| (c) era banners: `control/README.md` · `lab-loop.md` · `planning/README.md` · founding plan · wave2 groom · grounded-skills-program | one era banner / supersede line each; `control/inbox.md` via **one append-only era-closing block** (the pure-append CI gate forbids edits; ORDER 024 is the precedent) or via the README banner covering the band | live-voiced apparatus docs for a program that closed 2026-07-21; the sharpest hazard is inbox ORDER 010's standing "arm an hourly routine" imperative |
| (d) walls & conditionals: `CAPABILITIES.md` walls section · `README.md` regen line · `.session-journal.md` P10 · `auto-merge-guards.md` · `recipes/README.md` · `fleet-repos.txt` · `house-style.md` cell · `ai-project-workflow.md` slot | targeted corrections in each file's own grammar (the CAPABILITIES append-log's 2026-07-18 correction entry is the model); the roster fix adds the five missing adopters | standing walls contradicting the estate's verified capability matrix, in the false-walls checker's own repo; the roster is live machinery input, so its gap ships into every future regen |
| (e) `control/status-gba-homebrew-trackb.md` | archive per its own header | self-authorized disposal; kept-as-is it costs nothing but contradicts nothing — lowest priority |
| §2's provenance mislabel | correct the Q-0241 attribution to Q-0271/PL-012 in the owner-profile sentence's **source slot** (`.substrate/state.json:63`) and re-render the two derived copies | a boot-adjacent sentence presenting a scoped ruling as unscoped law; the fix is one attribution, not a doctrine change |
| §3's dogfooding gap | **NOT part of this sweep — a flagged decision, not a task** (see the preamble carve-out): whether the kit activates its own economy (declare classes, run shadow → gated on its 342-card corpus) | activation is behaviour change with an owner-facing surface — it belongs to the round's promote-by-measurement rule; only a report-only shadow census could ever ride a records session, and even that is a build-track call |

**Deletions recommended: none.** Same reasoning as the dig's §10 row: every
candidate is honest dated history, cited provenance, or CI-enforced
apparatus; the lever for this corpus is banners and flips, not removal.

**One owner ask retired by a live read, and one build-track unblock:** the
live effective rules on kit `main`
(`GET /repos/menno420/substrate-kit/rules/branches/main`, direct-PAT,
2026-08-28) require exactly one status check — `kit-quality`, with
strict-up-to-date `false` — which is precisely what `OQ-KIT-P10-REQUIRED-CHECKS`
asked the owner to click. The ask is marked ✅ RESOLVED (overtaken) in the
queue this session. Residue: deleting the two `legacy-alias-*` jobs from
`ci.yml` (their own comment says "delete after P10 lands") is now unblocked
**agent** work — a kit build-session item, not this records sweep.

## 6 · Coverage and verification

- **Read fully (whole-population, checked in code):** all 187 doc-surface
  files — `docs/` 144 (top-level 21 · audits 1 · gen2 7 · ideas 51 ·
  operations 6 · planning 14 · program 4 · recipes 3 · reports 15 · retro 14
  · reviews 2 · succession 6), root docs 7 (README · CHANGELOG ·
  CONSTITUTION · .session-journal.md · project.index.json ·
  substrate.config.json · pyproject.toml), `control/` 8, `telemetry/` 3,
  `.substrate/` 18, `.github/` 5, `bench/README.md`, `.sessions/README.md`.
  Data files (`guard-fires.jsonl` 766KB, `episodic_index.json`,
  `model-usage.jsonl`, the two report JSONs) were judged structurally
  (head/tail + counts), not read byte-by-byte.
- **Skipped, named (1,165 of the tree's 1,352 tracked files):** `src/` 122 ·
  `tests/` 114 · `bench/` 569 beyond its README · `scripts/` 13 · `tools/` 1
  · `dist/` 1 — code and harness, read only where a doc claim or an owed
  check pointed into them (the owed checks read the economy package, the PL
  register's mechanical pins, templates and dist embeds directly);
  `.sessions/` 342 dated cards beyond the README (records by construction;
  the dig already opened all cards programmatically); root boilerplate 3
  (LICENSE · .gitattributes · .gitignore). 187+1,165 = 1,352 ✓.
- **Verification:** 36 adversarial verifications (32 non-obvious doc
  verdicts + 2 lenses × 2 owed checks): **31 upheld**; the five corrections,
  all applied above and in the appendix — `docs/current-state.md` cite
  :34→:33 · `docs/gen2/queue-state.md` evidence cite next-boot :59→:57 ·
  `docs/ideas/README.md` cite :113→:112 ·
  `docs/planning/2026-07-19-grounded-skills-window-run.md` verdict
  superseded→historical-record (its report is its deliverable, not a
  replacement) · `docs/ai-project-workflow.md` recommendation
  regen-only→fix-in-round (`render --live` no-ops on substituted slots). No
  stale/superseded verdict was overturned to clean, and no clean verdict was
  overturned to hot — until Codex review of fm #960 overturned two the other
  way and caught three propagation errors, all folded in above: the
  headline totals had not been recomputed after the verifier corrections
  (now recomputed mechanically from the appendix);
  `docs/repo-navigation-map.md` live→STALE (its own completeness invariant);
  `telemetry/README.md`'s disposition keep→banner-or-fix (a false
  operational guarantee is wrong-action grade); the `.sessions/` corpus is
  342 dated cards plus the README, not 343 cards; and "never executed on
  the kit's own corpus" overclaimed run history from tree state — restated
  as unconfigured-and-trace-free at HEAD. Owed-check verifier residue, folded in: "shrink" also
  matches `guards.py` shrinkage-guard comments and two docs — none a
  retention mechanism, so check B's null stands as "nowhere load-bearing";
  `.substrate/claude/CLAUDE.md` is a staged render, not an installed boot
  file (the kit has no root CLAUDE.md and no `.claude/`), which narrows
  §2's "boot surface" phrasing to "boot-adjacent staged render".
- **Superbot stayed frozen:** one raw API fetch of the router file; no
  clone, no write.

## Appendix — the 187-row verdict table

Verdict vocabulary: **live** (current-truth surface, claims hold) ·
**STALE** (current-truth surface carrying false claims — itemized in the
lane notes; the load-bearing ones are in §4) · **superseded** (successor
named) · historical-record (dated record, accurate as such) · generated
(machine-written, regen-only) · reference (timeless policy/contract in
force). Dispositions: keep · keep-live · banner-or-fix-in-round ·
supersede-pointer · archive-recommend · regen-only.

**(root)** (7):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `.session-journal.md` | **STALE** | banner-or-fix-in-round | Its 'Recurring problems' section asserts as current that '👤 P10 still pending (the ruleset requires the two legacy contexts, not kit-quality directly)' when kit-quality is the ONE required check on main (re-verified… |
| `CHANGELOG.md` | **live** | keep-live | The release record's current-truth claims all verify against the tree: the newest section [1.21.0] - 2026-08-13 matches KIT_VERSION "1.21.0" (src/engine/lib/config.py:31), the header's refuse-without-section claim… |
| `CONSTITUTION.md` | **STALE** | keep | Its exhaustive-reading enumeration 'the [PL-NNN] register: PL-001 … PL-009' is six entries behind — docs/program/rulings.md holds 15 through PL-015 — but the load-bearing part is the pointer plus 'Cite PL-IDs — never… |
| `README.md` | **STALE** | banner-or-fix-in-round | The front door still describes the pre-extraction nested tree: the regen command 'python3 substrate-kit/src/build_bootstrap.py' fails from this repo root (CI runs 'python3 src/build_bootstrap.py'), tests are claimed… |
| `project.index.json` | **live** | keep | A planted contextpack-index skeleton still holding only the self-describing 'example-area' placeholder — input config for the generator, hand-fill expected, nothing false. |
| `pyproject.toml` | **live** | keep-live | version = "1.21.0" matches KIT_VERSION in src/engine/lib/config.py:31 as its own comment pledges, and the ruff engine-ban regime it declares is what CI runs; the ORDER 018/022 references in the subprocess ban message… |
| `substrate.config.json` | **live** | keep-live | kit_version 1.21.0 matches the release anchor, src/engine/lib/config.py's KIT_VERSION and pyproject.toml exactly; readpath_docs, sessions_dir and marker needles all match the tree. |

**docs (top level)** (21):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `docs/AGENT_ORIENTATION.md` | reference | keep | A timeless task-router whose claims all hold at HEAD — the boot set genuinely lives in CONSTITUTION.md ('## Boot read path' at line 28, per D-0011), every one of the 15 planted docs it lists plus CONSTITUTION.md and… |
| `docs/CAPABILITIES.md` | **STALE** | banner-or-fix-in-round | The append log is dated and self-correcting, but the standing 'Walls — verified blocked' section still carries seat-era walls (MCP-tools-only GitHub access, branch-deletion-is-owner-only, owner-click console… |
| `docs/NEXT-TASKS.md` | **superseded** | keep | Freshly rebuilt by kit #587 (2026-08-28, this round's session 2) into exactly the supersession pointer it should be — successor named in its own header: fleet-manager's… |
| `docs/PROJECT-CLOSEOUT.md` | historical-record | keep | A handover that declares its era on nearly every stateful claim — '§ 2 Current true state (verified live 2026-07-21)' and the footer both date-stamp it — so its now-superseded facts (v1.20.2, one open PR #552) read… |
| `docs/_merge_verification_2026-07-15.md` | historical-record | keep | A self-bannered (`historical`) inert probe file from 2026-07-15 that states its own purpose and its own disposal condition; it can send no reader anywhere. |
| `docs/adopters.md` | generated | regen-only | Machine-written registry (sole writer this repo, regenerated by `python3 dist/bootstrap.py currency`, last regen kit #586 stamped 2026-08-14) that faithfully reports its roster — 9/12 rows current at v1.21.0, 3… |
| `docs/ai-project-workflow.md` | **STALE** | banner-or-fix-in-round | The slot-rendered adoption-pace line says guided while .substrate/state.json holds "mode": "active" — the fix is a render rerun of the ${integration_mode} slot, never a hand edit. |
| `docs/architecture.md` | **live** | keep-live | Every checkable claim holds at HEAD (src/engine source of truth, dist generated by src/build_bootstrap.py, templates dir, tests/ present); the unfilled layer table is a declared skeleton slot, not a false claim. |
| `docs/collaboration-model.md` | **live** | keep-live | All pointers resolve (control/README.md carries both cited sections at lines 149/178; docs/program/rulings.md and program/collaboration-model.md exist) and the reconciliation cadence matches substrate.config.json's… |
| `docs/current-state.md` | **STALE** | banner-or-fix-in-round | A living-ledger current-truth surface whose headline block is a month behind the tree — it is NEXT-TASKS' still-open item 4 and the exact file this session is reconciling; a cold reader gets a false version, a false… |
| `docs/decisions.md` | **live** | keep-live | Append-only provenance ledger whose entries are dated records, not operating claims, and whose cheap checkable claims all hold at HEAD — scripts/check_program_law.py, src/engine/checks/check_status_current.py,… |
| `docs/eap-closeout-walkthrough-2026-07-14.md` | historical-record | keep | Header pins its era to the day and commit (2026-07-14, 86d8ac7, ORDER 021 final day), and the C-1/C-2 DONE stamps show it was maintained as a record; the remaining C-items (P10 swap now done — kit-quality is the one… |
| `docs/environment-setup-script.md` | reference | keep | Timeless owner-guidance whose two checkable claims hold: the repo has no requirements.txt, and CI's dev tools are exactly pytest + ruff (ci.yml line 153 'pip install pytest ruff'). |
| `docs/fleet-repos.txt` | **STALE** | banner-or-fix-in-round | It is the LIVE input to the adopters.md regen (src/engine/currency.py:83 ROSTER_RELPATH = "docs/fleet-repos.txt") yet omits five real adopters (sim-lab, superbot-idle, product-forge, spider-swing, couch-legend —… |
| `docs/helper-policy.md` | reference | keep | Four timeless placement/shadowing rules with no dated claims to go stale; the 'Where helpers go' section is a declared hand-fill slot, still empty. |
| `docs/house-style.md` | **STALE** | keep | One table cell is false — MODEL_LINE_NEEDLE is hardcoded in src/engine/grammar.py:415 and only imported by loop/telemetry.py — while every other hardcode-location claim verified (_REF_IDEA_MARK/_REF_FLAG_MARK in… |
| `docs/owner-profile.md` | **STALE** | keep | One spent conditional — 'once §3.2 item 7 makes the check required' — is now done (kit-quality IS the single required check on main, re-verified this session); the rest is the seat-era autonomy frame (never-wait,… |
| `docs/ownership.md` | **STALE** | keep | Its two future-tense claims are past: docs/program/ exists at HEAD holding rulings.md (the 'lands KL-2' already landed), and the 'lab loop' named as its owner closed 2026-07-21 — but the rest of the mutation-seam… |
| `docs/question-router.md` | **live** | keep | An empty append-only ledger whose format contract holds and whose machinery (the interview writing Q-blocks) still exists in the engine; zero blocks is an honest state, not staleness. |
| `docs/repo-navigation-map.md` | **STALE** | banner-or-fix-in-round | By its own placement rule ('if no row matches, the map is stale — extend the table') a table holding only its placeholder row is stale for every real placement task — a reachable routing surface that routes nothing; the fix is filling the rows *(corrected from live/keep on Codex review, fm #960 — the lane's 'vacuously true' reading contradicted the doc's own completeness invariant)*. |
| `docs/runtime_contracts.md` | **live** | keep-live | The one filled section (mutation seam) verifies at HEAD: atomic state backend, skip-if-exists plants, staged .claude/ (no live .claude/ dir exists in the kit tree), and the self-operation-via-dist rule; the rest are… |

**docs/audits** (1):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `docs/audits/eap-project-audit-2026-07-14.md` | historical-record | keep | Definitive dated EAP close-out audit pinned to origin/main f856ce3, self-declaring status `audit` and its write timestamp; every open item it records (P10, #317/#345 parks, ANTHROPIC asks) is framed as state at… |

**docs/gen2** (7):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `docs/gen2/README.md` | historical-record | keep | Index page of the gen-1→gen-2 kit-lab succession pack, self-dating to wind-down phase 2 (PR #74); all six linked companions plus the capstone retro and the sibling docs/succession/ pack exist at HEAD, and nothing at… |
| `docs/gen2/custom-instructions-proposal.md` | historical-record | keep | Dated (2026-07-09) proposal for a Projects-console Custom Instructions text — a surface that no longer exists since the program closed 2026-07-21; it grades gen-1 conventions with per-item evidence and an explicit… |
| `docs/gen2/environment-setup.md` | historical-record | keep | Dated (2026-07-09) environment spec for the console-era gen-2 kit-lab Project, with verbatim in-container test runs of setup.sh; its deployment target (the environment-settings Setup-script field, OWNER-ACTION 11) is… |
| `docs/gen2/feedback-for-gen2-blueprint.md` | historical-record | keep | Dated (2026-07-09) evidence-backed suggestion list for fleet-manager's gen2-blueprint — a seed standard for a generation model retired with the program close; every item is anchored to a named gen-1 incident or PR,… |
| `docs/gen2/next-boot.md` | historical-record | keep | The gen-2 boot doc, dated 2026-07-09 with a 2026-07-10 close-out handoff and one 2026-07-18 correction; imperative in form but addressed to a reader (a fresh gen-2 kit-lab Project session) that can no longer exist,… |
| `docs/gen2/queue-state.md` | historical-record | keep | Wind-down queue snapshot, reconciled twice on 2026-07-10 with per-item PR evidence, that explicitly cedes authority forward ('the living ledger and live GitHub win over it as time passes') — a model of a dated… |
| `docs/gen2/setup.sh` | historical-record | keep | Tested artifact of the succession pack — a defensive provisioning script for the console-era environment-settings field; the script itself remains internally correct as written (guarded repo detection, guarded pip,… |

**docs/ideas** (51):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `docs/ideas/README.md` | **STALE** | banner-or-fix-in-round | The conveyor's index presents already-built work as the next groom targets and every survive window has silently expired — a cold groom session following it today rebuilds existing deliverables (the exact stale-baton… |
| `docs/ideas/adopt-plants-pytest-gate-step-2026-07-10.md` | historical-record | keep | Shipped-idea record (PR #403) with valid frontmatter and a self-declaring State line; the mechanism is live at HEAD. |
| `docs/ideas/answer-time-gate-safety-advisory-2026-07-15.md` | historical-record | keep | Shipped-idea record (PR #407); the advisory function is live at HEAD. |
| `docs/ideas/archive-ready-close-out-surface-2026-07-11.md` | **STALE** | banner-or-fix-in-round | Its own flip criterion ('outcome stays open until a build slice merges') has been met since v1.18.0 — S1–S4 shipped and the archive-prep verb is live in the engine — yet frontmatter still reads routed/open, so a… |
| `docs/ideas/changelog-unreleased-structure-checker-2026-07-09.md` | historical-record | keep | Shipped-idea record (PR #351); the checker exists and runs in the kit-quality gate at HEAD. |
| `docs/ideas/control-board-kit-readiness-cell-2026-07-09.md` | **STALE** | banner-or-fix-in-round | Its only remaining half targets the seat-era websites control-plane board via ORDER 003/coordinator travel — all closed apparatus since 2026-07-21 — so `state: captured / outcome: open` no longer describes a routable… |
| `docs/ideas/currency-check-registry-delta-preflight-2026-07-15.md` | historical-record | keep | Shipped-idea record (PR #392); registry_delta is live in the engine. |
| `docs/ideas/dispatch-race-reverify-clause-2026-07-10.md` | historical-record | keep | Shipped-idea record (PR #398); the re-verify-then-stand-down clause is verbatim in the lab-loop prompt at HEAD. |
| `docs/ideas/enabler-install-preflight-2026-07-13.md` | historical-record | keep | Shipped-idea record (PR #344); the enabler preflight module exists in the engine at HEAD. |
| `docs/ideas/engage-slot-list-derived-2026-07-13.md` | historical-record | keep | Shipped-idea record (PR #387); the bank-coverage assertions are live in the test suite. |
| `docs/ideas/engagement-native-consumer-state-2026-07-12.md` | historical-record | keep | Shipped-idea record (PR #401); the native_gate evidence class is live in check_engagement. |
| `docs/ideas/engagement-wiring-strength-verification-2026-07-12.md` | historical-record | keep | Shipped-idea record (PR #402); both advisory layers are live in check_engagement. |
| `docs/ideas/feature-build-task-class-2026-07-09.md` | historical-record | keep | Shipped-idea record (PR #22, the PL-010 ruling); the 'feature build' class is live in the canonical taxonomy. |
| `docs/ideas/folded-gate-diff-aware-card-2026-07-11.md` | historical-record | keep | Dated consumer finding whose kit-side posture ('advisory only if the class recurs') still holds — and the #402 enforcement-strength advisory now covers the missing diff-aware legs kit-side anyway. |
| `docs/ideas/gate-tail1-multi-card-shadowing-2026-07-11.md` | historical-record | keep | Shipped-idea record (PR #187, v1.10.1) reconciled in-file by PR #311; every-card diff grading is live at HEAD, and its interim wave doctrine is explicitly marked OBSOLETE. |
| `docs/ideas/gate-verify-command-slot-2026-07-15.md` | historical-record | keep | Shipped-idea record (PR #405); gate_test_command reads the verify_command slot in the engine at HEAD. |
| `docs/ideas/guard-parity-kit-vs-adopter-2026-07-18.md` | **STALE** | banner-or-fix-in-round | The exact checker it asks for shipped the same day (PR #459, v1.19.0: tests/test_guard_parity.py + the src/engine/guards.py REGISTRY) yet the frontmatter still reads captured/open — a groom session pulling it forward… |
| `docs/ideas/harness-capability-roster-2026-08-04.md` | **live** | keep-live | The only post-close, owner-originated open backlog item, and genuinely still open — no capability-roster template exists anywhere in src/engine/ (grep-verified) — with owner verbatim as provenance. |
| `docs/ideas/heartbeat-delegated-tally-guidance-2026-07-13.md` | historical-record | keep | Shipped-idea record (PR #395); the delegated-tally doctrine is in both the template and the kit's own control/README.md at HEAD. |
| `docs/ideas/heartbeat-verb-2026-07-09.md` | historical-record | keep | Shipped-idea record (PR #346); cmd_heartbeat is live in the CLI at HEAD. |
| `docs/ideas/idea-index-merged-reality-2026-07-14.md` | historical-record | keep | Shipped-idea record (PR #355); the merged-reality leg with grace window and ancestry check is live in scripts/check_idea_index.py. |
| `docs/ideas/kit-preflight-dogfood-2026-07-14.md` | historical-record | keep | Shipped-idea record (PR #354); scripts/preflight.py exists and is the kit's local gate fan-out at HEAD. |
| `docs/ideas/label-added-disarm-guard-2026-07-09.md` | historical-record | keep | Shipped-idea record (PR #24); the disarm workflow is in tree exactly as designed. |
| `docs/ideas/make-seed-yield-keyword-bug-2026-07-09.md` | **STALE** | banner-or-fix-in-round | Both halves it asks for are in tree — make_seed.py's keyword/builtin screen cites this very idea file in its docstring, and run_ab.py prepare runs the seed suite — yet the frontmatter still reads captured/open,… |
| `docs/ideas/model-doctrine-emphasis-blind-phrase-2026-07-11.md` | historical-record | keep | Shipped-idea record (PR #187); the emphasis-blind presence test is live in the engine. |
| `docs/ideas/model-line-checker-false-red-2026-07-09.md` | historical-record | keep | Shipped-idea record (PR #95); both halves are live — the planted README renders label(needle) byte-forms and a miss reports the expected needle. |
| `docs/ideas/model-line-payload-lint-advisory-2026-07-11.md` | historical-record | keep | Terminal shipped capture whose frontmatter and ship banner declare its era; the shipped anchor exists at HEAD (src/engine/checks/check_model_line.py). |
| `docs/ideas/model-line-unrecorded-effort-marker-2026-07-15.md` | historical-record | keep | Terminal shipped capture (PR #394); MODEL_EFFORT_UNRECORDED verified present in src/engine/checks/check_model_line.py at HEAD. |
| `docs/ideas/multi-repo-program-kit-lab-trading-2026-07-07.md` | historical-record | keep | Deliberate content-free pointer stub, self-declared historical; superbot (canonical home) is frozen, so the pointed URL is stable. |
| `docs/ideas/order-claim-cross-branch-collision-2026-07-14.md` | historical-record | keep | Terminal shipped capture (PRs #365/#397); WORK_CLAIM_ORDER_RE verified in src/engine/grammar.py at HEAD. |
| `docs/ideas/pinned-feed-contract-doctrine-2026-07-09.md` | historical-record | keep | Terminal shipped capture (PR #482); the landed artifact docs/recipes/pinned-feed-contract.md exists at HEAD. |
| `docs/ideas/plain-adopt-lane-drift-advisory-2026-07-10.md` | historical-record | keep | Terminal shipped capture (PR #396); lane_drift_advisory verified in src/engine/adopt.py at HEAD. |
| `docs/ideas/reflection-miner-line-start-markers-2026-07-09.md` | historical-record | keep | Terminal shipped capture (PR #19); _REF_LEAD_PREFIX_RE verified in src/engine/loop/reflections.py at HEAD. |
| `docs/ideas/render-live-claude-md-gap-2026-07-09.md` | historical-record | keep | Terminal shipped capture (PR #95, fix shape (a) recorded); accurate as a dated record of the run-2 engine gap and its closure. |
| `docs/ideas/retro-docs-reachability-checker-2026-07-10.md` | historical-record | keep | Terminal shipped capture (PR #388); scripts/check_retro_index.py exists and is wired as the retro-index preflight leg at HEAD. |
| `docs/ideas/rubric-f5-none-regressing-wording-2026-07-09.md` | historical-record | keep | Self-bannered RULED + historical decision brief; the ruling record it names exists at HEAD (bench/results/cold-start/f5-ruling-order-011.md). |
| `docs/ideas/run-ab-prepare-engagement-arc-2026-07-09.md` | historical-record | keep | Terminal shipped capture (PR #95); bench/run_ab.py exists at HEAD and the record is accurate as of its date. |
| `docs/ideas/score-m1-mutation-artifacts-2026-07-09.md` | historical-record | keep | Terminal shipped capture (PR #40) of two scorer bugs and their fix, evidence-anchored in the committed run dirs; accurate as a record of its date. |
| `docs/ideas/seat-digest-adaptive-clip-2026-07-13.md` | historical-record | keep | Terminal shipped capture (PR #349); the seat-digest engine surface (src/engine/seatdigest.py) exists at HEAD, so the record matches the tree. |
| `docs/ideas/session-card-guard-recipes-2026-07-09.md` | historical-record | keep | Terminal shipped capture (PR #19) of a convention that still travels via the planted adopt README; accurate as a record of its date. |
| `docs/ideas/session-gate-diff-aware-selection-2026-07-09.md` | historical-record | keep | Terminal shipped capture (PR #19); the --session-log explicit selector verified present in src/engine/cli.py at HEAD. |
| `docs/ideas/session-gate-flip-race-fail-open-2026-07-13.md` | historical-record | keep | Terminal shipped capture (PR #342, split closure honestly recorded); check_session_log.py and _derive_diff_session_cards verified at HEAD. |
| `docs/ideas/staged-artifact-regen-lag-checker-2026-07-12.md` | historical-record | keep | Terminal shipped capture (PR #345); src/engine/checks/check_staged_regen.py exists at HEAD. |
| `docs/ideas/substrate-kit-auto-drafted-handoff-2026-07-07.md` | historical-record | keep | Deliberate content-free pointer stub, self-declared historical, canonical copy superbot-resident (frozen repo, stable URL); outcome shipped (kit PR #16) recorded in frontmatter. |
| `docs/ideas/t5-headless-guard-surface-2026-07-09.md` | historical-record | keep | The lane's only open capture (state: captured, outcome: open) — honestly unshipped, its measurements accurate as dated records, and its fix explicitly owner-gated (bench/tasks/ pin path), so it cannot send a cold… |
| `docs/ideas/taxonomy-surface-sync-checker-2026-07-09.md` | historical-record | keep | Terminal shipped capture (PR #404); scripts/check_taxonomy_sync.py exists and runs as the taxonomy-sync preflight leg at HEAD. |
| `docs/ideas/template-local-copy-sync-advisory-2026-07-15.md` | historical-record | keep | Terminal shipped capture (PR #399); src/engine/checks/check_template_sync.py exists at HEAD. |
| `docs/ideas/upgrade-apply-docs-single-shot-window-2026-07-09.md` | historical-record | keep | Terminal shipped capture (PR #106 full mechanism, #92 interim); run_apply_docs_posthoc verified in src/engine/upgrade.py at HEAD. |
| `docs/ideas/upgrade-archive-report-line-gap-2026-07-09.md` | historical-record | keep | Terminal shipped capture (PR #92); the '(already banked)' report line verified in src/engine/adopt.py at HEAD. |
| `docs/ideas/upgrade-checklist-release-json-placement-2026-07-09.md` | historical-record | keep | Terminal shipped capture (PR #92); the ADOPTER_CHECKLIST at HEAD names release.json beside bootstrap.py.new and warns about the silent skip, exactly as recorded. |
| `docs/ideas/upgrade-rollback-loses-doc-hash-records-2026-07-09.md` | historical-record | keep | Terminal shipped capture (PR #92); the record_doc_hash / byte-match self-heal machinery it describes is present in src/engine/adopt.py at HEAD. |

**docs/operations** (6):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `docs/operations/README.md` | **live** | keep-live | Reachability root whose claims hold at HEAD: all 22 linked files verified present (every docs/reports/*, the audits file, the EAP walkthrough, PROJECT-CLOSEOUT, all five operations docs) and each one-line description… |
| `docs/operations/archive-ready-close-out.md` | reference | keep-live | Binding checklist doctrine still in force — chats still archive in the regular-session era — and every mechanism claim verifies at HEAD: src/engine/templates/archive-ready.md.tmpl, src/engine/loop/archive.py… |
| `docs/operations/auto-merge-guards.md` | **STALE** | banner-or-fix-in-round | The guard-stack model itself is sound and mostly tree-verified, but two claims are now false and one could revive a retired owner ask (P10), so a two-line fix in-round is warranted. |
| `docs/operations/grounded-skills-measurement.md` | historical-record | keep | Pre-registered (2026-07-15) protocol for the 2026-07-19..26 measurement window, which ran and froze: docs/reports/2026-07-19-grounded-skills-measurement.md and its data JSON exist, and both scripts… |
| `docs/operations/lab-loop.md` | **STALE** | banner-or-fix-in-round | Marked binding but describes dead apparatus with no era banner: the console-Schedule daily routine was never armed (P4) and console Schedules, P4, and the autonomous program all closed by 2026-07-21 — a cold session… |
| `docs/operations/release-runbook.md` | **live** | keep-live | Binding runbook whose every checkable claim holds at HEAD: version homes exactly at src/engine/lib/config.py:31 (KIT_VERSION = "1.21.0") and pyproject.toml:17 (version = "1.21.0"); scripts/cut_release.py and… |

**docs/planning** (14):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `docs/planning/2026-07-12-grounded-skills-program.md` | **superseded** | supersede-pointer | Status `plan` with '§7: None is implemented in this session' and zero completion note, while the wrap report proves all 8 slices shipped same-day 2026-07-12 — one Succeeded-by line (the convention the wave-1 groom… |
| `docs/planning/2026-07-15-archive-ready-close-out-plan.md` | historical-record | keep | An executed plan: every artifact its slices specify exists at HEAD (src/engine/loop/archive.py, src/engine/checks/check_archive_ready.py, src/engine/templates/archive-ready.md.tmpl, plus check_card_residue.py for the… |
| `docs/planning/2026-07-16-overnight-veto-menu.md` | historical-record | keep | A one-night ORDER 025 breadth menu that commits to nothing by construction ("veto menu, not a plan of record") and scopes itself to a single morning review, so its dated claims (kit at v1.18.0, PRs #431/#433 live,… |
| `docs/planning/2026-07-19-grounded-skills-window-run.md` | historical-record | keep | Its window is date-gated to a past range (2026-07-19..26), its own GSW-4 bullet already deep-links the published successor report, and the baton it flips lives in a SEAT CLOSED-bannered control/status.md — no… |
| `docs/planning/2026-07-19-needs-planning-recipes.md` | historical-record | keep | An executed-and-aged recipe plan: ranks 1-2 are built at HEAD (docs/recipes/pinned-feed-contract.md exists; the CONSTITUTION.md.tmpl rider is at lines 63-69; src/engine/checks/check_folded_gate.py exists), rank 3 was… |
| `docs/planning/2026-07-19-night-run-idea-groom-wave2.md` | **superseded** | banner-or-fix-in-round | The wave-1 banner actively routes readers here as 'the next buildable-now ladder', yet wave2 carries no exhaustion banner and still presents S2–S17 as pickable (S3 'IN FLIGHT as PR #517, not yet merged'; baton… |
| `docs/planning/2026-07-19-night-run-idea-groom.md` | **superseded** | keep | Already carries the model self-banner — 'Succeeded by ...wave2.md — the R1–R13 ladder below is exhausted (all shipped)' — and tree spot-checks confirm the banner's claim, so it cannot send a cold session anywhere but… |
| `docs/planning/2026-08-06-provenance-review-mandate.md` | historical-record | keep | A dated owner-specified plan that dispositioned itself in place: every dead branch (the gate, the exporter, the UserPromptSubmit hook shape, the prevention metric) carries an inline dated SUPERSEDED/AMENDED/DEFERRED… |
| `docs/planning/README.md` | **STALE** | banner-or-fix-in-round | A nav index whose 'Active' tier tells a cold session an ORDER-025 owner-veto menu is pending work (seats/ORDERs closed 2026-07-21) and which omits the two newest planning docs — a five-line re-tier fixes it. |
| `docs/planning/kit-lab-founding-plan-2026-07-07.md` | historical-record | banner-or-fix-in-round | Still badged 'Status: plan — the executable founding plan' with no era banner seven weeks after its program closed; its execution-facing sections order actions on closed or since-changed apparatus, and one… |
| `docs/planning/kit-lab-repo-founding-brief-2026-07-07.md` | historical-record | keep | Self-bannered historical pointer stub whose only job — resolving the travelled founding plan's relative link for the check --strict link check — still works, and whose canonical target lives in the FROZEN superbot… |
| `docs/planning/phase-2.5-cold-start-report-2026-07-07.md` | historical-record | keep | Identical self-bannered pointer-stub pattern: era declared, zero content, link-resolution function intact (the founding plan links it at line 10), canonical copy in the frozen superbot repo. |
| `docs/planning/rebuild-kickoff-steps-6-8-brief-2026-07-07.md` | historical-record | keep | Same self-bannered pointer-stub pattern: era declared, zero content, link target (founding plan line 8's 'kickoff brief' link) resolves, canonical copy frozen in superbot. |
| `docs/planning/rebuild-phase-2.5-procedure-2026-07-06.md` | historical-record | keep | Same self-bannered pointer-stub pattern as its three siblings: era declared, zero content, resolves the founding plan's 'companion D' link (line 11), canonical copy frozen in superbot. |

**docs/program** (4):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `docs/program/README.md` | **live** | keep-live | Directory index for program law whose checkable claims all hold at HEAD: all three listed files exist, docs/house-style.md exists, and scripts/check_program_law.py really runs inside the kit-quality gate (ci.yml:234). |
| `docs/program/agent-decision-authority.md` | reference | keep | Canonical program copy of the PL-001/PL-002 decision-authority model, still in force; its never-wait section self-scopes ('Inside its scope (the rebuild program)') so a cold reader is not sent wrong even though the… |
| `docs/program/collaboration-model.md` | reference | keep | Timeless program-wide working-relationship statement with no dated claims to go stale; its cross-references (PL-001/PL-002/PL-006/PL-007 in rulings.md, docs/ideas/, current-state.md) all resolve in the tree. |
| `docs/program/rulings.md` | **live** | keep-live | THE live PL register, matching the anchor exactly; every cheap tree claim checks out — check_program_law.py gates in kit-quality (ci.yml:234), PL-010's 'feature build' is verbatim in TASK_CLASSES… |

**docs/recipes** (3):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `docs/recipes/README.md` | **STALE** | banner-or-fix-in-round | One false claim about the tree that invites a wrong action: it says the applies-when discovery nudge 'is deferred until >=2 recipes carry signatures' — both recipes here now carry signatures AND the check already… |
| `docs/recipes/advisory-to-born-red-gate.md` | reference | keep | Graduated pattern doc whose every checkable tree claim still holds at HEAD: the three leading-underscore helpers exist in check_session_log.py (lines 295/331/371), EXPECTED_STRICT_SUBCHECKS is still 7… |
| `docs/recipes/pinned-feed-contract.md` | reference | keep | Timeless copy-by-hand pattern explicitly marked 'NOT SOURCE OF TRUTH'; its proof lives in cross-repo PRs (superbot #1884, websites #11) cited as dated history, and it makes no claims about this tree that can go stale. |

**docs/reports** (15):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `docs/reports/2026-07-09-cfgdiff-differential-testing-method.md` | reference | keep | Timeless method doc (differential-oracle testing) whose only dated content is immutable provenance; its one live cross-claim — kinship with the bench integrity law — verifies against bench/README.md at HEAD. |
| `docs/reports/2026-07-09-cfgdiff-v0.1.1-release-decision.md` | historical-record | keep | Self-bannered dated snapshot of another repo's (codetool-lab-sonnet5) wind-down release decision; every actionable item in it targets that repo and is framed as record, so no cold kit session is sent to a wrong action. |
| `docs/reports/2026-07-09-fleet-adoption-review.md` | historical-record | keep | Era-declared audit snapshot whose banner explicitly subordinates it to source ('source code and merged PRs win over this file'); every since-falsified claim is dated-snapshot state, not a live assertion, and the… |
| `docs/reports/2026-07-09-kit-lab-run.md` | historical-record | keep | Era-declared owner day-report of the 2026-07-09 founding run; its owner-gates list (P4 Schedules, P5 Railway, P10, P11/P13) is EAP-console-era apparatus, but §4 explicitly defers to current-state as canonical rather… |
| `docs/reports/2026-07-11-adopter-outcomes-measurement.md` | historical-record | keep | Era-declared measurement snapshot in which every number carries its n and window; its §7 items are proposals not orders, and its era facts (10 registry adopters, v1.12.0-wave drift table) are accurate as of date —… |
| `docs/reports/2026-07-11-t5-rescope-analysis.md` | historical-record | keep | Era-declared supporting analysis for the T5 v1→v2 rescope that explicitly subordinates itself to the pinned task text ('the binding task text is the pinned file itself') — and the pinned file at HEAD carries the… |
| `docs/reports/2026-07-12-current-state-archive.md` | historical-record | keep | Deliberate immutable relocation archive of the living ledger's dated history (K0 orientation-budget relief); it declares its own era in the header and the live ledger still links to it as its history home, so a cold… |
| `docs/reports/2026-07-12-grounded-skills-wrap.md` | historical-record | keep | Program wrap report verified against git + the GitHub API on its own date, with an explicit source-files-win banner and honest-gaps section; every dated claim is framed as a receipt of 2026-07-12, not standing… |
| `docs/reports/2026-07-12-prompt-template-hardening-input.md` | historical-record | keep | Seat-era ORDER 014 input to the 2026-07-12 fleet prompt rebuild, self-bannered as a dated snapshot; its gap table was consumed the same day (its '❌ missing' routines/grammar rows are now live kit surfaces), so the… |
| `docs/reports/2026-07-12-trigger-forensics.md` | historical-record | keep | Owner-requested read-only forensics of one overnight window, self-bannered with an explicit source-wins line and an explicit none-executed recommendations section; its lessons were graduated into the live… |
| `docs/reports/2026-07-13-fleet-cleanup-audit.md` | historical-record | keep | Dated outside-verification audit of the EAP final night, accurate as a record of 2026-07-13; its era is declared in the title date + 'EAP final night' and the Status: audit line, and every liveness claim inside is… |
| `docs/reports/2026-07-13-night-run-adopter-outcomes.md` | historical-record | keep | ORDER 016 item 5 writeup of the 2026-07-12→13 night run, fully self-bannered as a dated snapshot with an explicit source-wins clause; every classification carries its citation and window, so it needs no reconcile. |
| `docs/reports/2026-07-19-grounded-skills-measurement.md` | historical-record | keep | Pre-registered GSW-1..4 before/after measurement report, self-bannered as a dated snapshot with source-wins clause; both frozen-data sha256 hashes it publishes verify exactly against the tree at HEAD and every… |
| `docs/reports/data/2026-07-19-grounded-skills-latency.json` | generated | keep | Machine-written frozen evidence (writer: scripts/measure_pr_latency.py, repro command in the report's §7); its sha256 is published in the companion report and re-verified matching this session, so hand-editing — or… |
| `docs/reports/data/2026-07-19-grounded-skills-results.json` | generated | keep | Machine-written frozen evidence (writer: scripts/measure_grounded_skills.py --clone per the report's §1); sha256 published in the companion report's status banner and re-verified matching this session, so the file… |

**docs/retro** (14):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `docs/retro/2026-07-11-continuous-run-retro.md` | historical-record | keep | Self-bannered `archive` durable record of the Q-0265 window with every §1 number re-verified at write time; accurate as a record of 2026-07-11 and cannot be read as a current worklist. |
| `docs/retro/QUESTIONS.md` | historical-record | keep | The gen-1 retro question set, era-declared in its own title and banner ('gen-1 retro (2026-07-09)', 'answer by ID per the inbox ORDER'); a cold reader cannot mistake it for a current instruction to answer. |
| `docs/retro/README.md` | **live** | keep | Complete, link-accurate index of the closed retro band — all 13 sibling files in docs/retro/ are indexed and every link resolves (verified against a directory listing); its status line is dated 2026-07-09, so the era… |
| `docs/retro/archive-ready-2026-07-11.md` | historical-record | keep | Self-bannered `archive` snapshot of state at coordinator-chat archive; its imperative resume path (cut v1.13.0, run-10, OA-14/15 ratification) is long executed — kit is at v1.21.0 (src/engine/lib/config.py:31) — but… |
| `docs/retro/coordinator-session-2026-07-10.md` | historical-record | keep | A dated (2026-07-10) sweep of coordinator-chat knowledge into the repo; every item is attribution-stamped 'coordinator relay 2026-07-10' and scoped to the now-closed coordinator environment, so despite its… |
| `docs/retro/project-review-2026-07-09-gen1-winddown.md` | historical-record | keep | Self-bannered `audit` wind-down capstone over the whole gen-1 life, written 'as the generation closes'; a dated, evidence-cited record whose friction ledger and prescriptions are archival by construction, with its… |
| `docs/retro/project-review-2026-07-09-kitlab-coordinator.md` | historical-record | keep | Self-bannered `audit` companion review with its verification date and SHA stated inline ('verified live on 2026-07-09 (main at de77b6c)') and every unverifiable claim marked 'per coordinator'; a model dated record… |
| `docs/retro/project-review-2026-07-09-superbot-coordinator.md` | historical-record | keep | Era-declared dated audit snapshot of the SuperBot-rebuild coordinator lane (a Project closed 2026-07-21); its banner scopes every claim to 2026-07-09 and the retro README indexes it as gen-1 record — no reconcile needed. |
| `docs/retro/project-review-2026-07-09.md` | historical-record | keep | The canonical gen-1 kit-lab audit snapshot, self-scoped to 2026-07-09 with an explicit 'source code and merged PRs win over this file' clause — accurate as a record; every owner action it asked for has since resolved… |
| `docs/retro/self-review-2026-07-09-kitlab-coordinator.md` | historical-record | keep | 'Gen-1' is in its title and its twin-execution note names the canonical successor pass (self-review-2026-07-09.md via PR #51) and its own reason for being kept — session-side facts the repo cannot reconstruct — so it… |
| `docs/retro/self-review-2026-07-09-superbot-coordinator.md` | historical-record | keep | Era-declared, lane-suffixed gen-1 retro of the closed SuperBot-rebuild coordinator; accurate as a record of 2026-07-09 and indexed as such in docs/retro/README.md, with no action line a cold reader could wrongly… |
| `docs/retro/self-review-2026-07-09.md` | historical-record | keep | Era-declared dated gen-1 retro (title + ORDER-005 status badge); every cheap checkable claim verified against the tree, and nothing in it orders an action a cold session could wrongly take today. |
| `docs/retro/wind-down-addendum-2026-07-09-kitlab-coordinator.md` | historical-record | keep | Explicitly badged 'historical' first-person gen-1 record whose only carried action (index it in docs/retro/README.md after #74) is verified done — README line 13 carries the index line, added 2026-07-10. |
| `docs/retro/wind-down-review-2026-07-09-superbot-coordinator.md` | historical-record | keep | Era-declared ('Status: audit' wind-down addendum, dated, lane-suffixed) whole-life record of the closed superbot-coordinator lane; its cross-references (the merged review pair, docs/succession/) all resolve in the… |

**docs/reviews** (2):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `docs/reviews/2026-08-06-provenance-mandate-layer1.md` | historical-record | keep | Dated answer record (date in filename, 'Answered in writing before the reviewer call', 'Sweep over 11 shallow clones, 2026-08-06') committed precisely so it could be frozen evidence; accurate as a record of… |
| `docs/reviews/2026-08-06-provenance-mandate-review-record.md` | historical-record | keep | Self-freezing dated review record — it closes with 'The record above this line is frozen history.' and its 2026-08-07 disposition section is a dated terminal state (PR #580 authorized and merged), so nothing in it… |

**docs/succession** (6):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `docs/succession/README.md` | **live** | keep | Index of the closed superbot-coordinator wind-down pack; every link resolves at HEAD (all 5 pack files + docs/retro companions + docs/gen2/README.md verified present) and every description matches the doc behind it. |
| `docs/succession/close-out-2026-07-10-superbot-coordinator.md` | historical-record | keep | Dated final record of the gen-1 coordinator lane (post-wind-down events, mandate-confusion incident, unmerged-work check at main=c2ba85f); accurate as of 2026-07-10 and self-dating in title and status line. |
| `docs/succession/custom-instructions-proposal-superbot-coordinator.md` | historical-record | keep | Dated (2026-07-09) gen-1 lessons-to-instructions rewrite for a coordinator role that closed with the program on 2026-07-21; accurate as a record, every keep/add/drop incident-anchored. |
| `docs/succession/environment-spec-superbot-coordinator.md` | historical-record | keep | Dated (2026-07-09) environment spec for a gen-2 Claude Project that was never provisioned — the program closed 2026-07-21; accurate as a record of the tested setup script and scope needs at wind-down. |
| `docs/succession/gen2-feedback-superbot-coordinator.md` | historical-record | keep | Dated (2026-07-09) incident-anchored feedback on fleet-manager's gen2-blueprint.md — a blueprint and program that closed 2026-07-21; accurate as a record and clearly framed as wind-down-time reading of a then-live doc. |
| `docs/succession/next-boot-2026-07-09-superbot-coordinator.md` | historical-record | keep | Dated (2026-07-09) first-10-minutes boot doc for a gen-2 coordinator that never booted; accurate as a record of queue state and walls at wind-down, and its own directory's close-out doc already supersedes its… |

**control** (8):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `control/README.md` | **STALE** | banner-or-fix-in-round | Live-voiced protocol whose actor half is dead: it directs every session to run the manager-era ritual and execute any `status: new` inbox order, and the inbox is frozen at 24 perpetually-new orders — a wrong-action… |
| `control/claims/README.md` | reference | keep | Self-badged binding and still fully wired: `bootstrap claim` exists (src/engine/cli.py:3780) and check_claims.py enforces exactly the advisory classes it advertises; parallel-session work-dedup remains meaningful in… |
| `control/inbox.md` | historical-record | banner-or-fix-in-round | Accurate as a record of manager dispatches 2026-07-09→15, but it declares no era and every one of its 24 ORDERs still reads `status: new` — including standing imperatives (ORDER 010 arm-an-hourly-routine, ORDER 016… |
| `control/outbox.md` | historical-record | keep | Dated append-only lane→manager ledger of the closed bus (last entry 2026-07-19, two days before program close); its final cross-seat asks (folded-gate ports to superbot-next/websites, readiness-cell render) were… |
| `control/status-gba-homebrew-trackb.md` | historical-record | archive-recommend | Self-terminal visiting-lane heartbeat — declares its own closure ('visit COMPLETE... will not write here again') and its own header pre-authorizes disposal once the visit closes, which it did 2026-07-10; archiving it… |
| `control/status-superbot-coordinator.md` | historical-record | keep | Self-bannered ARCHIVED gen-1 coordinator heartbeat: its six ⚑ owner asks are 2026-07-10 rebuild-era items long moot (superbot is now frozen; the rebuild-era wind-downs settled), but the first status line stops a cold… |
| `control/status-wave-v1.16.0.md` | historical-record | keep | Date-scoped neutral-facts relay of the v1.16.0 distribution wave (2026-07-14), accurate as a record of that day; its one open thread ('superbot-games #141 OPEN, landing owed') was overtaken by later waves — the… |
| `control/status.md` | **STALE** | banner-or-fix-in-round | The repo's heartbeat, freshly stamped 2026-08-13, still tells readers '#552 = parked for owner ratification' and that a closeout PR 'will be merged on green' — but #552 MERGED 2026-08-04 and 0 kit PRs are open today,… |

**telemetry** (3):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `telemetry/README.md` | **STALE** | banner-or-fix-in-round | Current-truth-voiced feed contract carrying a false operational guarantee — outcome fields 'are backfilled by the lab loop's telemetry sweep' (lab loop closed 2026-07-21; all 143 rows still carry null outcomes) and 'the console exporter renders declared JSON arrays' (console closed); a session relying on the contract waits for a backfill that never comes *(disposition raised from keep on Codex review, fm #960)*. |
| `telemetry/allocation-ladder.md` | reference | keep-live | PL-004 layer 2 of the live PL register (docs/program/rulings.md is live program law per this round's anchors): the program-wide model-for-task defaults remain in force, the revision log is honestly empty, and the doc… |
| `telemetry/model-usage.jsonl` | generated | keep | Machine-appended ledger — session-close's Model-line harvest writes it (src/engine/cli.py:3260; append-only per KF-11, never hand-edited): 143 structurally valid JSON rows spanning 2026-07-09→2026-07-13 only, i.e.… |

**.substrate** (18):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `.substrate/agents/architect.md` | generated | keep | Rendered agent persona whose binding-model paragraphs are the state.json architecture/ownership/mutation slot values verbatim; fixes go through the interview, not this file. |
| `.substrate/agents/researcher.md` | generated | keep | Rendered read-only persona with no dated or era-bound claims; content is generic method text that holds at HEAD. |
| `.substrate/agents/reviewer.md` | generated | keep | Rendered reviewer persona; contracts it embeds match the tree, and its one aged line (lab-loop ownership, same slot text as architect.md) traces to state.json, not this file. |
| `.substrate/ci/quality.yml.example` | generated | keep | Engine-staged example (referenced from src/engine/adopt.py); its claims about `check --strict` fan-out, the required-check in-job short-circuit, and the kit-owned substrate-gate.yml all match the engine and the live… |
| `.substrate/claude/CLAUDE.md` | generated | keep | Machine-rendered from the interview slots (staged by src/engine/adopt.py:2462 / render.py, never installed — the kit has no .claude/ dir and no root CLAUDE.md); the aged content lives in state.json's slot values, so… |
| `.substrate/episodic_index.json` | generated | keep | Engine-written session-card index (engine/loop/episodes.py); 162 entries, 2026-07-09 through 2026-07-13, structurally sound — a frozen program-era index that no live surface reads (the kit installs no hooks on… |
| `.substrate/guard-fires.jsonl` | generated | keep | Append-only guard-firing telemetry written by the engine's check/hook surfaces (src/engine/cli.py:710); still live — 1369 records spanning 2026-07-09 to 2026-08-13, the v1.21.0 release day. |
| `.substrate/hooks/README.md` | reference | keep | Timeless customization contract for hosts; every checkable claim holds (exactly 4 hooks in the template; interpreter_for_checks and all five cadence knobs exist in src/engine/lib/config.py:47-50,278). |
| `.substrate/hooks/settings.template.json` | generated | keep | Engine-staged template (src/engine/adopt.py:2475-2476); the four hook commands match the engine's hook CLI surface (bootstrap.py hook pretooluse/sessionstart/postedit/stopcheck). |
| `.substrate/reflections.json` | generated | keep | Engine-written reflection buffer (loop machinery); five provisional recurring-path entries, all dated 2026-07-13 — frozen loop state from the program era, harming nothing at HEAD. |
| `.substrate/skills/analysis/SKILL.md` | generated | keep | Engine-seeded skill (src/engine/skills/skills.py composes SKILL.md files); three-step generic method, nothing to go stale. |
| `.substrate/skills/deep-research/SKILL.md` | generated | keep | Engine-seeded skill; timeless research method with no repo-state claims. |
| `.substrate/skills/quality-gate/SKILL.md` | generated | keep | Engine-seeded skill; both named commands are real at HEAD (pytest suite in tests/, `check --strict` in the engine CLI) and match the kit's actual gate. |
| `.substrate/skills/question/SKILL.md` | generated | keep | Engine-seeded skill; generic answer-from-source method, no claims to age. |
| `.substrate/skills/repo-health/SKILL.md` | generated | keep | Engine-seeded skill; `bootstrap check` and the drift categories it names (badges, links, session-log markers) are all real engine checkers at HEAD. |
| `.substrate/skills/review/SKILL.md` | generated | keep | Engine-seeded skill; the contracts-first review method holds and pairs with the reviewer agent seam. |
| `.substrate/skills/session-close/SKILL.md` | generated | keep | Engine-seeded skill; the close ritual it prescribes (card, idea groom, verify, PR to terminal state) matches the kit's live gate machinery. |
| `.substrate/state.json` | generated | keep | Engine-state-backend-owned file (atomic writes only; hand-editing forbidden by the ownership model); the aged slot text is interview data whose revision is a round/owner decision via `bootstrap answer` + re-render,… |

**.github** (5):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `.github/CODEOWNERS` | reference | keep | Two-line timeless ownership declaration (blanket @menno420) with nothing dated to go stale; consistent with a repo whose merges gate on the required check rather than required reviews. |
| `.github/workflows/auto-merge-disarm.yml` | **live** | keep-live | Working label-is-the-switch disarm half; its honesty note correctly locates real enforcement in the required-check gate, and the guard-stack map it cites (docs/operations/auto-merge-guards.md) exists at HEAD. |
| `.github/workflows/auto-merge-enabler.yml` | **live** | keep-live | Working arming mechanism whose guards (required-context count, fresh-label re-read, claim/* head support) all match the tree and the current one-required-check reality; only its 2026-07-09 'UNVERIFIED — watch the… |
| `.github/workflows/ci.yml` | **live** | keep-live | This is the working kit-quality gate the anchors name as the ONE required check; every script it invokes exists at HEAD (all six scripts/check_*.py plus tools/check_no_false_walls.py verified) and the… |
| `.github/workflows/release.yml` | **live** | keep-live | Two supported triggers per its own header — tag push (owner-side canonical) and workflow_dispatch, the only agent-runnable path (the git proxy 403s tag pushes) — and its guard commands are real (src/build_release_json.py --verify-only at line 190; fresh-dist byte-compare)… |

**other** (2):

| doc | verdict | disposition | the one reason |
|---|---|---|---|
| `.sessions/README.md` | reference | keep-live | The operative session-card contract at HEAD: its four required markers match substrate.config.json's session_markers verbatim, the Model-line harvest it describes exists in code (src/engine/cli.py:3260), and the… |
| `bench/README.md` | reference | keep | The pinned-harness contract still holds at HEAD: every layout file it names exists (rubrics, T1-T5, seeds/make_seed.py, score_m1.py, run_ab.py, all five results families) and scripts/check_bench_integrity.py runs in… |