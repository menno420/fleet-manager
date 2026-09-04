# substrate-kit — the entry point

> **Status:** `living-ledger` · true as of **2026-09-04**
>
> **What this is:** fleet-manager's entry point for `menno420/substrate-kit` —
> where the last session left off and where the next one should look.
> **Canonical for nothing.** The kit's own `control/status.md` (freshest
> single surface) and `docs/PROJECT-CLOSEOUT.md` win on its state; the PL
> register (`docs/program/rulings.md`) is program law for every adopter; the
> live tree wins over everything. Depth files are **not yet written** —
> created by the 2026-08-21 fleet review (Tier-1, "cleared to build" since
> 2026-08-08) and carries only the entry point so far.
>
> Certainty tags per
> [`../../findings/2026-08-05-foundation-continuation.md`](../../findings/2026-08-05-foundation-continuation.md).

## The one-paragraph answer

`substrate-kit` is the estate's **method kit**: a portable agent
workflow/memory substrate shipped as a single stdlib-only `dist/bootstrap.py`,
adopted across the estate (12 registry rows), plus the **PL register** —
program law that binds every adopter — and the generated adopter registry
`docs/adopters.md`. **v1.21.0** since 2026-08-13 (cut, published, distributed;
kit #581–#586). The Self-Improvement seat closed 2026-07-21; releases are cut
by owner-directed sessions using this repo's `release` →
`upgrade-distribution` skills. `MEASURED` 2026-08-21: 0 open PRs — records
still carrying "#552 parked for owner ratification" describe July (**#552
MERGED 2026-08-04**). ~~Its own `docs/current-state.md` body still says
v1.20.2~~ — **reconciled 2026-08-28 (kit #588)**: a dated reconcile block
now heads that file; `control/status.md`'s stale #552 line fixed in the
same PR.

**Owner intent (DRAFT, awaiting his words):** [`intent.md`](intent.md) — why he
built the kit, what "done" means, and what would make him stop, from the
2026-08-28 elicitation sitting.

## Threads

### Thread: K1–K5 (the `estate` pre-seed prerequisites) — **LANDED on kit `main`, UNRELEASED**

**`MEASURED` 2026-09-04.** [D-0035]'s step 2 is built and merged:
**[kit #590](https://github.com/menno420/substrate-kit/pull/590), squash-merged
as `8a83c733eded4af06281dcbe1d01f05d3da98a94`.** `main` re-verified after the
merge, not trusted from the PR's green: 2,277 passed / 1 skipped, dist byte-pin
exit 0, and a hub adoption driven through **`main`'s own artifact** into an
empty git repo produced the tree K1–K5 specify.

**The shape, not five flags.** `engine/lib/profiles.py` names what the kit had
no name for — which shape an install was born in. `Config.adoption_profile`
persists it, so `upgrade`/`render` (which already re-run `adopt` with the
loaded config) honour it with no second orchestration path;
`adopt.adoption_plan(config)` is the one accessor every consumer reads.

| | proven against `main`'s artifact |
|---|---|
| K1 | `adopt --profile hub` plants no `control/` tree; the bus checkers are input-gated, so they quiet by construction, not by an allowlist entry |
| K2 | no `docs/` at all, no seat-digest render; the boot list follows the shape in both agreement homes |
| K3 | `sessions/README.md` present, `.sessions/` absent, `sessions_dir: "sessions"` in the planted config |
| K4 | `owner_context` renders one pointer plus the repo's own two slots; undeclared installs render byte-identically |
| K5 | ledger gitignored from birth, `tracked: false`, `max_records: 2000`; the KF-11 tracked-and-uncapped default is untouched for every existing adopter |

**Deliberately deferred, and named rather than left to be discovered:**

- **The hub has no skill pack.** A fresh hub emits **26** skill-ground
  advisories over **8** distinct paths. Those advisories are the change
  *working* — before the profile filter reached `check_skill_grounds`, every
  one passed silently as "grounded by construction", a false green in the
  checker whose job is dead pointers. The gap is a hub-compatible skill set:
  the **skills channel**, which [D-0035] defers past the first cold test. A
  test pins its exact shape rather than asserting zero.
- **Doctrine prose is reported, not forked.** `CONSTITUTION.md` and the working
  agreement still name omitted docs in prose outside the boot sections;
  `adopt` reports every surviving route, by file, on every pass instead of the
  kit forking its most important document per shape.
- **K6/K7** untouched, per the build order.
- **Found, not fixed:** `[boot-section-missing]` on `.claude/CLAUDE.md` after
  any `adopt --include-claude` — the staged agreement's heading does not match
  `check_boot_path`'s regex. Reproduced identically on the **pre-change**
  `origin/main` dist, so it is pre-existing and belongs in its own PR.

**Review cost, for the next session's calibration:** three Codex rounds (the
[D-0039] cap) returned **21** findings — 4 P1 + 6 P2, then 5 P2, then 2 P1 + 4
P2 — alongside an independent 43-agent adversarial pass whose 37 raw findings
were each handed to a separate agent instructed to refute them (**14**
survived, 8 distinct). **40 mutants applied, 40 killed.** Two findings were
latent rather than cosmetic: telemetry-path containment was *parsed* rather
than resolved (an intermediate symlink had `check` writing the ledger outside
the repository), and `upgrade` refused an unknown profile only at step 6,
*after* archiving state and replacing the vendored bootstrap — a refusal over a
partially-upgraded repo. **The merged head carries no review verdict**: round 3
reviewed the previous head and its findings were fixed after it, which the cap
makes the designed exit.


### Thread: the owner-directed review round — **session 4 DONE (the sitting ran; every letter that was ASKED is answered); session 5 named below from his own words**

> **Still open after the sitting, so no session reads "answered" as "finished":**
> the kit's **name** (he ruled it changes and will supply the word — `OQ-KIT-RENAME`) ·
> the **adopter half** of `OQ-KIT-V1-21-RELEASE` (he answered timing only) ·
> agenda **§ 2 · G** (card deletion — deliberately not asked; his answer is due
> once the report-only census exists) · the **BTD6 history loop** (not asked; its
> own sitting).

The owner ordered a kit review round in the second overnight 2026-08-27→28
hub sitting (*"review it again and improve it"* — verbatim record + the
four-step method:
[`../../findings/2026-08-28-owner-direction-agent-autonomy.md`](../../findings/2026-08-28-owner-direction-agent-autonomy.md),
**OD-24**). **Session 1** (overnight 2026-08-28, steps 1–2):
[the genesis dig](../../findings/2026-08-28-substrate-kit-genesis-dig.md) —
three-era history, twelve classified gaps (dominant
**unenforced/unrouted**), the rival-hypothesis verdict, the §10
dispositions table (recommendations only, execution owner-gated).
**Session 2** (2026-08-28, daytime) executed §11 items 1–2 and 4:

- **kit #587 (MERGED on green after three Codex rounds):** the kit-tree
  worklist pointer (gap #5 — `kit:docs/NEXT-TASKS.md` superseded into the
  route) and the false-negative family fixed (worklist rows 13/17/18, each
  reproduced against the published asset first; pre-push adversarial
  verification + Codex R1 5/5 and R2 6/6 conceded-and-fixed; R3's 4
  verified and deferred as worklist **row 35** under the two-re-review cap
  — tally 5→6→4, measured non-convergent). Fixes ride kit `main`
  unreleased; the cut stays owner-paced. **kit #590 (K1–K5) joins them there
  2026-09-04** — three merged, none released.
- **The item-4 audit:**
  [the router band re-read](../../findings/2026-08-28-router-band-reread.md)
  — all 208 body sections superbot:Q-0063–Q-0272, 59/59 quotes
  machine-verified (ledger committed in its appendix); seven genesis-dig
  claims narrowed, each routed in place at the claim site; a carrier
  census of standing owner rules (five absent from every fm document, the
  rest in seat-era/reference surfaces or carrying a different facet);
  genesis precedents mapped onto the gap table; its two new owner asks
  queued (`OQ-KIT-PROMPT-DOCTRINE` · `OQ-EAP-SPEND-WINDOW-MOOT`).
- **The morning letters (Move-1 GO · journal · §10 confirmations) were
  checked first and remain UNANSWERED** — everything owner-gated stayed
  gated. The re-read adds superbot:Q-0101 as evidence for the journal
  letter.

**Session 3** (2026-08-28, daytime — the round's next audit):
[the kit-tree truth pass](../../findings/2026-08-28-kit-tree-truth-pass.md)
— the kit's whole committed doc surface (187 files at `a9acc41`, the dig's
skipped subdirectories + `docs/succession/` included) judged per-doc with
adversarial verification (31/36 upheld; the workflow's five corrections
plus Codex fm #960's three rounds all folded in), and
**both owed checks answered**: PL-002's canonicalization **preserves**
Q-0241's rebuild-only scope (the one drop is a Q-0241-vs-Q-0271 provenance
mislabel in three derived copies of one owner-profile sentence), and
Q-0214's delete-with-tombstones retention **substantially shipped** as the
v1.0.0 economy engine — unconfigured and trace-free on the kit's own
342-card corpus at HEAD. The headline: 104 of 187 files are honest
self-bannered history; the failure class is a 23-file current-truth-voiced
set, catalogued as recommendations in the finding's §5 (a future
doc-surface truth sweep; nothing owner-gated except the flagged
economy-activation decision, carved out of the sweep's blanket).
**Executed in the kit's venue: kit #588, MERGED on green** (squash
`7f58f0e`) — `docs/current-state.md` reconciled (the supersede table's open
item 4) + `control/status.md`'s false #552 line, through the kit's full
discipline; three Codex rounds (R1 two P2s + R2 one P2, all
conceded-and-fixed — the release-path wording is now precise: tag push
owner-side canonical, workflow_dispatch the only agent-runnable trigger;
R3's one P1 was the born-red hold itself, consumed by the flip).
`OQ-KIT-P10-REQUIRED-CHECKS` retired by a live rules read (kit-quality is
the one required check — the ci.yml legacy-alias deletion is now unblocked
agent work).

**Session 4** (2026-08-28, **owner-live** — the review-and-discussion sitting he
selected: *"the next session can review everything that these 3 audits have
produced, and then helps me to discuss and answer the open questions"*):
[the sitting's answers, verbatim](../../findings/2026-08-28-od24-sitting-answers.md)
— **twelve answers recorded as each arrived**, `OWNER` quotes separated from
`DERIVED` readings, and routed the same session to the queue (7 entries updated,
1 added, **3 closed**), to `[D-0011]`, to the program as **OD-26**, and back into
[the agenda](../../planning/2026-08-28-od24-round-open-questions.md), which is
now a **record** rather than an agenda.

**The three things that change how this round is read:**

1. **One root cause, not twelve gaps** *(that the twelve are downstream of it is
   the sitting's `DERIVED` mapping — he was shown four of his own prior
   complaints, never the twelve gaps)*. Asked *which ways does the kit still not
   work* — the question no session had put to him — he collapsed four of his own
   prior complaints into one: *"they are all related to the same root cause,
   which is mostly that agents don't take enough initiative to leave the repos
   in a better shape"*. The divergence from the round's reconstruction is one of
   **altitude, not fact** — and the round **had already found it** (dig § 6.1,
   *"the central drift … and the review round's real charter"*) and then
   organised around the gap table anyway. **The round reproduced, on itself, the
   unrouted-knowledge defect it was auditing.**
2. **The cost function, unprompted:** *"a lot of work just keeps stalling, which
   is not necessarily bad, but also a reason why I think it's important that the
   workflow is working correctly, so we don't waste so much time redoing the same
   things over and over"* — **re-derivation is the waste.** *"Not necessarily
   bad"* is a **qualification**, not a blessing: some stalling is acceptable, a
   harmful stall is not thereby fine. The test for any proposed mechanism is
   *does it stop something being re-derived?* — less stalling is neither the case
   for a fix nor a mark against one — which re-ranks **routing above building**.
3. **A three-stage order, unprompted, which governs everything:** *"I am
   currently running 3 parrallel ultracode session to map most of all the repos,
   once this mapping is all done we should use this information to come up with
   a revised pan. Only after that will we move to execution of the 'GO'"* — so
   **this round's output is an input to a revised plan, not a work queue**, and
   the Move 1 hold is a **stage with an exit condition**, not a deferral to
   re-ask next session.

**Answers that bind kit work directly:** the charter is **rewritten to say
initiative** · `AGENTS.md` is **hand-written per repo** (the kit does not plant
them) · the journal **survives as the guidebook it already is** — he delegated
the call and named a function (*"easily find out what went wrong each session"*)
that the **existing session cards already capture**, so what is missing is
**retrieval** across them, not a second record (no new file, nothing enforced) · a brake may prompt **only when he is present**, never unattended
(`delete_trigger` still never) · nothing may **block** a session calling work
done · the next release is **cut when the next fix batch lands** · the kit
**is renamed**, but he supplies the name later (`OQ-KIT-RENAME`).

### Thread: **session 5 — the kit records session, cleared by him and named from his answers**

**Not a session's proposal this time.** Asked directly whether kit-side document
work also waits for the revised plan, he answered **"Records work can go now"**,
drawing the boundary himself: **mechanisms wait, record corrections do not.** So
session 5 is a **kit-venue records session**, and its two halves are both his:

1. **Rewrite the kit's charter to name initiative** — his § 2b answer, and the
   round's most direct fix for the root cause he named. *Initiative* currently
   returns **zero hits** across `kit:README.md`, `kit:docs/PROJECT-CLOSEOUT.md`
   and `kit:docs/program/rulings.md`. **Scope guard:** the purpose statements
   only — **not** the PL register's rulings, which are program law with
   append-only grammar and owner provenance.
2. **The truth pass's § 5 sweep** — the 23-file wrong-action set. Lead with the
   rows that cost sessions capability *today*, because three of his mapping
   sessions are running into them right now: `docs/CAPABILITIES.md`'s standing
   false walls (in the repo whose own `check_no_false_walls` exists to prevent
   exactly that), `docs/fleet-repos.txt`'s five missing adopters (it is the
   **live regen input**, so the gap ships into every future registry regen), and
   `control/inbox.md`'s 24 seat-era ORDERs still reading `status: new` —
   including one instructing a session to arm an hourly routine, which sits
   beside the estate's never-delete-a-trigger decision.

**Then the release**, per his timing answer: kit #587 and #588 ride `main`
unreleased and go out **with** this session's work in one cut, not before it.
The adopter half stays open — he answered timing only. **kit #590 (K1–K5) is a
third unreleased passenger as of 2026-09-04**, and does not itself unlock the
cut: his *"cut when the next fix batch lands"* sequences the charter rewrite
and the doc-surface sweep **first**, and neither has landed.

**Explicitly NOT session 5's:** Move 1 or anything Move-1-shaped (held, and it
is a stage with an exit condition — do not re-ask him before the mapping is
done); the interview and the standing leftovers surface (designs, not builds —
both inherit *never block* and *never prompt unattended*); the rename (waiting
on his name); any adopter rollout; the economy activation (flagged decision,
carved out of the sweep's blanket); fm #958; superbot.

### Thread: the v1.21.0 follow-up worklist — **open, lives in THIS repo, not the kit**

The kit's next worklist is fleet-manager's
[`../../findings/2026-08-13-substrate-kit-v1210-followups.md`](../../findings/2026-08-13-substrate-kit-v1210-followups.md)
— Codex findings on the vendored v1.21.0 (count the rows from the file;
rows 13/17/18 consumed by kit #587, row 35 added from its R3), fix order
restated at its tail (the work-destroyers 26/29/33 now lead — the false
negatives are consumed). ~~`MEASURED` 2026-08-21: the kit's own tree
references it **nowhere**~~ — **closed 2026-08-28 (kit #587):**
`kit:docs/NEXT-TASKS.md` is superseded into a routed pointer to this
worklist and the round thread, reachable from the kit's boot path via its
`current-state.md` links. Start any kit session from that finding.

### Thread: adopter currency — **3 stale rows + 5 invisible adopters** (owner-paced)

Registry at its 2026-08-14 regen: 9 of 12 rows current at v1.21.0; stale:
`superbot-games` v1.20.1 (⚠ DRIFT ×3 self-report rows — the hop is
**owner-paced** — "no adopter yet", owner 2026-08-14), `trading-strategy` v1.20.2 (skipped
pending its archive decision), `pokemon-mod-lab` v1.15.0 (owner-held).
**Adopters are invisible to the registry** where the scan roster
`docs/fleet-repos.txt` omits them: `sim-lab` (kit v1.15.0), `superbot-idle`
(v1.16.0), `product-forge` (v1.7.0 — the actual oldest, archive-bound
post-R2), and — `MEASURED` 2026-08-21, the couch-legend seed session —
**`spider-swing` (v1.20.2) and `couch-legend` (v1.21.0, seeded that day)**
too: neither is in the roster nor in the registry's 12 rows — a
registry-driven rollout can never find any of the five. The roster fix is
kit-side (this thread already carries it); until then the registry
undercounts the estate's adopters.
Rollout ask: `OQ-KIT-V1-21-RELEASE` in [`../../owner-queue.md`](../../owner-queue.md).

### Thread: the provenance mandate — **kit-side open plan** (paused)

`docs/planning/2026-08-06-provenance-review-mandate.md` (owner-specified; its
§ 8 build order is authoritative — the kit's current-state explicitly refuses
to duplicate it). The blast-radius exporter has no engine code yet. Read
fleet-manager's
[`../../findings/2026-08-06-provenance-mechanism-measured.md`](../../findings/2026-08-06-provenance-mechanism-measured.md)
before touching kit #580's territory. Also deferred by design: the `intake`
skill graduation (roadmap § 7) — its own session.

## Before you attach / modify — the traps, measured

- **`src/engine/` is source of truth; `dist/bootstrap.py` is GENERATED and
  byte-pinned** — after any engine edit run `python3 src/build_bootstrap.py`;
  CI reds on divergence.
- Gate: **`kit-quality` is the ONE required check** (live rules re-verified
  2026-08-28); local convergence is `python3 scripts/preflight.py`. Legacy
  alias jobs mirror it without running anything (`OQ-KIT-P10-REQUIRED-CHECKS`
  resolved 2026-08-28 — deleting the aliases from `ci.yml` is now unblocked
  agent work for a build session).
- **Releases: `workflow_dispatch` on `release.yml` is the only AGENT-runnable
  path** (the git proxy 403s tag pushes — path quirk, not a wall); the
  workflow's other supported trigger, a hand-pushed `v*` tag, is owner-side
  canonical (its own header; precision from Codex R1 on kit #588). Verify
  with `scripts/verify_release.py` / three-way sha256. The `release` skill
  here is the procedure.
- `docs/adopters.md` is **GENERATED — never hand-edit**; regenerate with
  `python3 dist/bootstrap.py currency` (sole writer: this repo).
- Engine code is stdlib-only, no print/assert/subprocess (CI lint leg).

## External workspaces

Pointers, never copies (the § 5.7 shape) — all **null today**: no Drive
folder, ChatGPT workspace, or Gemini notebook is mapped to `substrate-kit` in
any record this review read. Add the pointer here when one exists.
