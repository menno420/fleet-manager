# The risk register

> **Status:** `plan` — authoritative for **what could make this rebuild fail, how
> it would show itself early, and who holds each one**; not authoritative for
> any architecture, product or verification decision, which the files it cites
> own.

## 0 · How to read this register

**Five columns, and the second and third are the ones that earn the row.** A
risk that cannot name evidence *in these repositories* is speculation, and a risk
with no early warning sign is a post-mortem written in advance. Rows without both
were cut — § 11 records which, and why.

- **why it is credible HERE** — an evidence id, and where possible a `file:line`.
  A figure this session re-derived itself is **`MEASURED`**; a figure carried from
  a fan-out lane is marked **`lane-claimed`** *inline*, per the publication rule
  in [`run/independent-findings.md`](run/independent-findings.md) § I-17.
- **early warning sign** — something observable **inside the first slice or two**,
  not at the end. Where the sign can be a machine check, § 9 says so; where it
  can only be watched by a human, § 9 says that too, because pretending otherwise
  is this package's own subject.
- **owner** — the role that holds it: **owner** (a call only he can make),
  **S<n> session** (the session building that slice), **every session**, or
  **the reviewer** of the PR.

Rows are ordered within each family by consequence, worst first. **Six risks
carry an expanded treatment** — R-01, R-02, R-13, R-20, R-25, R-30 — because a
table cell cannot hold them.

**The register's own limit, stated once.** Nothing here was observed running.
Both product repositories were read-only, neither bot was booted, and no Discord
surface or production database was touched ([`13-verdict.md`](13-verdict.md)
gap 1). Every early-warning sign below is therefore a sign a *future* session
must actually go and look at.

---

## 1 · R-01 · The successor would be the third start-fresh attempt in this family, and the second one failed

| risk | why it is credible HERE | early warning sign | mitigation | owner |
|---|---|---|---|---|
| **R-01** · The successor repeats `superbot-next`: disciplined, well-instrumented, green, and parked as a donor without ever becoming the product | `superbot-next` reached **533 goldens** (**`MEASURED`** — `find parity/goldens -name '*.json' ! -name '_sweep_skips.json' \| wc -l` → 533 at pin `d5f66dc2`), **3,648 green tests** and **7 required checks on `main`** (`lane-claimed`, M9-S06 / M8-S08) — and its front door reaches nothing (I-13: help max depth **0**; `setup` **39 of 40** panels unreachable) | **At S1 exit**, any of the three artifacts in § 1.2 missing or not reproducible by a second person | § 1.1's five differences, each with the falsifier in § 1.2; and the stop rule: **if S1 exits without them, S2 does not start** | owner + S1 session |

### 1.1 · What is specifically different this time

Five differences. Each is a claim, so each is stated with what would show it to be
rhetoric.

**1 · The failure is diagnosed rather than assumed.** Attempt two was launched
against *"too much history, too many trials and errors"* — a claim about volume.
This package's diagnosis is a mechanism: **a green instrument running over a
population that is empty, a model, or smaller than reported**, with three
source-read instances in three different repositories
([`04-root-cause.md`](04-root-cause.md) § 2.5) and a fourth in the estate's own
false-done ledger. A volume diagnosis licenses "build it smaller"; a mechanism
diagnosis licenses one specific line of code in every gate
([`08-verification.md`](08-verification.md) § 1).

**2 · The acceptance oracle is not parity.** Byte-equality against a captured old
bot is structurally blind to absence — an unregistered tool emits nothing, so no
golden covers it (I-11: **36 → 8** catalogued AI tools, the one audited write
lost, invisible to 533 green goldens) — and it actively rewards transcription,
because computing a value made a golden red while pinning it made it green
(§ 2.3 of the root cause). The successor's oracle is a **journey with an asserted
effect, driven in a real guild** ([`08-verification.md`](08-verification.md)
§ 3c layers 4–8; [`09-roadmap.md`](09-roadmap.md) § 0.2).

**3 · The donor roles are corrected, and the successor is required to take both
halves.** The 2026-08-21 plan named `superbot-next` the architecture donor and
would have sent an implementation session to the wrong tree for the
import-direction guard (I-3), the provider-neutral AI gateway (I-4,
`sb/kernel/ai/gateway.py:1-6` says so itself) and the enforcement locus (I-21:
**44 of 45** `superbot` checkers driven from asserting tests, against **15**
appearing in workflows). This package's rule is that `superbot` donates guards
over the **rendered product** and `superbot-next` donates guards over the
**invariants of the system**, and that **neither repo has both**.

**4 · The extension contract carries data from slice two, not "later".**
`superbot-next` deferred the out-of-tree data lane and it never arrived: its own
fence excludes **29 of its 49 subsystems** from being plugins, and the docstring
names the reason as work not yet done (I-10). The successor's **S2 is an
out-of-tree module that owns tables** ([`09-roadmap.md`](09-roadmap.md) § 1) —
the requirement is exercised second, not deferred to a phase that never comes.

**5 · There is no replacement promise.** The promise is what converted honest
work into a failure ([`12-owner-decisions.md`](12-owner-decisions.md) OD-B, whose
default is *no replacement promise at all*). A bot that is useful is a success on
its own terms and a failure only against a promise nobody needed to make.

**And what is NOT different, said plainly, because the flattering half is easy.**
Same estate, same owner, same session cadence, same tools. Attempt two was not
careless: its authors wrote *"a vacuous check is worse than none"* into a
docstring and then built a **mutation test** to prove their guard had teeth — and
both the mutation and the check ran over a model
([`08-verification.md`](08-verification.md) § 3.2). **Intent was never the
variable, so no amount of intent is the difference.** Only mechanism is, and
mechanism is cheap in the first commits and unaddable afterwards.

### 1.2 · The falsifier — three artifacts, checked at S1 exit, by someone else

If the five differences above are real, then at the end of slice one these exist
and a **second person can reproduce them from the repository alone**:

| # | artifact | what makes it non-trivial | falsified if |
|---|---|---|---|
| 1 | **A committed `POPULATION` + `FLOOR` on every gate S1 ships**, with a fixture that fails the gate when the population empties | the negative control is the part that is skipped under time pressure (only **one** guard in either repo makes an empty population a failure — F-S02, `lane-claimed`) | any S1 gate exists whose population can go to zero and stay green |
| 2 | **One R4 record with all four fields resolved** — `build_sha` equal to the PR head, `signed_at` parsing inside the build's lifetime, every evidence link fetched, `surface_id` present in the committed manifest | a forged record with `surface_id='/NO_SUCH_COMMAND_AT_ALL'`, `signed_at='not-a-date'`, `build_sha='zzzz'` validated with **zero problems, EXIT=0** in the predecessor (`lane-claimed`, F-D04, executed in-process against the real validator) | the first R4 record is accepted with any field unresolved |
| 3 | **A reachability walk over the shipped route graph, run from the canonical entry point**, with its result committed | the predecessor's equivalent walked a registry its own `autouse` fixture cleared (I-2), and the working walk had to be written from outside the repo (`run/reachability_probe.py`) | the walk runs over a fixture, a model, or a graph the renderer does not read |

**The stop rule.** [`09-roadmap.md`](09-roadmap.md) § 0.4 already says the
population contract is in the first commits or the plan has failed. This register
makes it operational: **if any of the three above is missing at S1 exit, S2 does
not start, and the gap is reported as a finding rather than carried.**

---

## 2 · Architectural risks

| risk | why it is credible HERE | early warning sign | mitigation | owner |
|---|---|---|---|---|
| **R-02** · **The plan's own abstractions go unbuilt** — the 20-row ledger arrives as six, and the six that arrive are the ones with no second consumer | expanded in § 2.1 | the first feature PR that touches a path outside its own feature directory without a `cross_cutting` entry | `check_feature_locality` ([`07-feature-contract.md`](07-feature-contract.md) § 4.3) with its denominator assert and negative control, shipped **in S1** | S1 session |
| **R-03** · The import guard sees only module-level imports; the coupling and the cycles move into function bodies | **`MEASURED`** I-22: **268 of 296** cross-subsystem `sb.domain` imports (90.5 %) sit in function bodies, and **all 8** mutual subsystem pairs live there — **0** at module level. `superbot`'s checker has a `--report-lazy-imports` mode that raises its findings from 1 to 137 and **CI never passes the flag** (`lane-claimed`, R3/E-D1) | the guard's finding count is suspiciously stable while feature count grows; any PR that moves an import into a function body | the guard walks the **whole AST**, counts function-body imports as real edges, and **fails on cycles**; ship a fixture cycle as the negative control | S1 session |
| **R-04** · A second renderer appears — the parity twin under a new name — and the tests bind to it | **`MEASURED`**-adjacent (source-read, [`08-verification.md`](08-verification.md) § 3b): every "actual" wire byte in 533 goldens comes from `rendered_panel_payload()` at `sb/adapters/parity/transport.py:242`, while production installs `DiscordPanelPresenter` at `sb/app/panel_host.py:66` — the shipping renderer is on **neither** side of the oracle | any test asserting over a payload dict not produced by the shipping presenter; any second class implementing the presenter port outside `tests/` | a fence with a **ceiling as well as a floor**: exactly one presenter implementation outside tests, asserted; goldens are rendered *through* it or they are not goldens | S1 session |
| **R-05** · The composition root becomes the one thing no test executes | `superbot-next`'s `run_app` is **624 lines (`sb/app/main.py:213-836`) never executed by any test**; all 6 test references use `inspect.getsource` and assert on source-text substrings (`lane-claimed`, M8-D03), and 9 such assertions sit inside the required gate (`lane-claimed`, F-D07) | any assertion over `inspect.getsource`; a root that grows past ~200 lines with no headless boot test | a **headless composition boot** in the required gate that resolves every registered ref — the predecessor's `check_runtime_smoke` shape (`lane-claimed`, F-S08/M8-S05), which is genuinely good and only needs its missing assertion (every `custom_id` resolves to a handler) | S1 session |
| **R-06** · Process-global registries make "emptied population" the default shape of a test | **`MEASURED`**: `grep -rn 'def \(clear\|reset\)_[a-z_]*_for_tests' sb/` → **92** (49 `domain` · 38 `kernel` · 3 `spec` · 2 `adapters`), against **1** repo-wide in `superbot`. This is the mechanical precondition for I-2: an `autouse` fixture calling one of them is what made the navigation golden permanently vacuous | the second `clear_*_for_tests` function; any `autouse` fixture that clears a registry a gate walks | registries constructed per-boot and passed, not module-global; and a rule the framework enforces — **a gate may not run inside a fixture scope that can clear its population** | S1 session |
| **R-07** · The declaration grammar grows fields with no consumer and predicates with no population | `lane-claimed` M9-D08: **107 of 237** declared field names (45 %) are never given a non-default value anywhere in the compiled snapshot; M9-D02/D03: three compiler predicates key on fields **0 of 3,552** walked objects carry | a manifest field added "for later"; a predicate whose population is not printed in its own output | the abstraction ledger's second-consumer rule ([`06-architecture.md`](06-architecture.md) § 12) as a **gate**: a declared field with no non-default value and no reader is a build error; every predicate prints its population size | reviewer |

### 2.1 · R-02 expanded — the abstractions that do not get built are the ones with no second consumer yet

[`06-architecture.md`](06-architecture.md) § 12 lists **20** abstractions, each
with a named second consumer and the measured failure it prevents. The failure
mode is not that a session rejects them; it is that under slice pressure the ones
whose second consumer arrives in a *later* slice look optional in the current
one. On the ledger's own dependency shape those are the exposed rows: **#8** the
per-module migration ladder (second consumer: out-of-tree modules — S2), **#13**
the AI tool registry with a committed floor (S4), **#14** the risk/mode gate
(S4), **#15** the durable scheduler queue (S5), **#19** one loader for in-tree and
out-of-tree (S2), **#20** the case record (S4).

**The evidence that this is the real shape of the failure, not a worry:** every
one of the predecessor's deferred lanes is a row of this kind. The out-of-tree
data lane was deferred and never arrived (I-10). The AI tool port band was
deferred and never arrived — **36 catalogued tools became 8, all read-only**
(I-11). The `superbot` cog's audited write seam did not survive the trip. In each
case the abstraction existed and its *population* was deferred.

**So the mitigation is not "remember to build them".** It is that each of these
six rows has a slice that is the first *new kind* of caller for it
([`09-roadmap.md`](09-roadmap.md) § 0.3), and the slice does not exit until that
caller exists. **A row whose second consumer never arrives is cut, not carried** —
which is exactly what [`06-architecture.md`](06-architecture.md) § 13 already did
to six abstractions both repos built and neither used. The register's addition is
the reverse direction: **an abstraction still waiting for its second consumer two
slices after it shipped is a finding**, and the ledger is re-read at every slice
exit for exactly that.

---

## 3 · Product risks

| risk | why it is credible HERE | early warning sign | mitigation | owner |
|---|---|---|---|---|
| **R-08** · The bot says nothing when a member mistypes | `lane-claimed`, CHALLENGE D: `!helpp` and `!seting` produce **total silence** in `superbot-next`, and so does every unrecognised token — while `superbot`'s composition root (`disbot/bot1.py:540-546`) names this as a root-cause bug it already fixed with an always-answer fallback of about four lines | the first unrecognised-input path with no reply; a not-found counter that does not exist | the **not-found route is a route** with its own counter, and "zero unanswered inputs" is criterion 1 of the observation window ([`09-roadmap.md`](09-roadmap.md) § 9) | S1 session |
| **R-09** · Setup leaves the route graph again | **`MEASURED`** I-13, and **both bots failed it independently**: `superbot-next` reaches **39 of 40** setup panels from nowhere; `superbot` reaches setup only through an ephemeral out-of-graph launcher — and its `_repost_launcher` button is the tell that someone met this and shipped a way to re-post the message rather than a route back | any panel reachable only from a posted message; any "re-post the launcher" affordance; `setup` absent from the route graph's parent chain | setup is a **first-class destination with a declared parent** ([`06-architecture.md`](06-architecture.md) § 5.3), and the reachability gate walks it from the canonical entry point | S1 session |
| **R-10** · The interaction budget is declared and never walked | **`MEASURED`** I-13: 314 panels wired by **200** downward edges, when a 314-node graph needs ≥313 merely to be a tree — the graph was never capable of being connected, and adding the 78 Back/Home up-links changes reachability by **zero** panels, exactly as it must | edge count below node count minus one at any commit; a budget stated in prose with no walk behind it | the budget is a **committed number** the reachability gate asserts ([`05-product-definition.md`](05-product-definition.md) § 3.4), with per-guild visibility modelled (I-14) so a correctly-hidden subsystem is not scored as unreachable | S1 session |
| **R-11** · The feature set is chosen by what ports easily rather than by what the server needs | [`12-owner-decisions.md`](12-owner-decisions.md) **OD-D** is open: the middle set (`xp`, `karma`, `leaderboard`, `counting`, `starboard`, `community_spotlight`, `ticket`, `polls`, `reminders`) is undecided, and the portability exercise ([`07-feature-contract.md`](07-feature-contract.md) § 5.6) makes `utility_cog` the cheapest port and `starboard_cog` the one that actually tests the contract | S2's module chosen for portability rather than for the contract load it puts on § 3.5 | S2's selection criteria are written into the slice **before** the module is named ([`09-roadmap.md`](09-roadmap.md) § 3), and the default is a **stateful** module | owner (OD-D) + S2 session |
| **R-12** · Panels render with no controls, or a failed data provider renders anyway | `lane-claimed`, M9-D05: rendering all 314 panels through the real engine gives **150 of 314 with zero engine-injected nav** and **51 of 314 with zero components of any kind**; M9-D10: a failing provider is swallowed and the panel renders regardless (`RuntimeError: Database not initialised` observed live) | the first panel that renders with an empty control set; the first swallowed provider exception | actionability is asserted over the **rendered artifact** — instantiate, read `view.children`, drive the callback (`superbot`'s `test_games_hub_view.py` shape, I-6), made universal by construction; a provider failure is a visible degraded state, never a silent one | S1 session |

---

## 4 · Verification risks

| risk | why it is credible HERE | early warning sign | mitigation | owner |
|---|---|---|---|---|
| **R-13** · **The population defect returns** — a green gate over a population that is empty, a model, or smaller than reported | expanded in § 4.1 | any gate whose output does not print its own population size | the population contract as a **framework requirement**: a check registers through a helper taking `population` and `floor` as required arguments, and a check that does not register cannot run ([`08-verification.md`](08-verification.md) § 1) | every session |
| **R-14** · A skipped test inside a required gate is green | **`MEASURED`** I-16, re-run at the pin: `pytest tests/integration -q` → **`14 skipped in 0.04s`, EXIT=0**; `pytest tests/e2e -q` → **`11 skipped`, EXIT=0** — both **required** legs, in the single job that provisions Postgres *precisely so they cannot skip*, with the 12 money-race regression files among the skipped | any `s` in a required gate's pytest output; a collected count that drops between runs | **a skip in a required gate is a red gate**, and every suite asserts a **collected-count floor** — a skip is a declaration that the population was absent, which is this defect wearing a green tick | every session |
| **R-15** · A gate's real exit code is swallowed | **`MEASURED`** I-19: `restore-verify.yml:124` is `python3 -m sb.app.verify_boot \| tee verify-report.json`, with **0 occurrences of `pipefail` and 0 `shell:` keys across all 8 workflow files** — the weekly proof that the bot can be restored **cannot fail**. And I-20: **this session committed the same error in its own shell one hour after writing it up**, because the false reading agreed with the thesis | any `\| tee` on a gate step; any `$?` read after a pipe | `set -euo pipefail` in every `run:` block, no pipe on a gate step, and a checker over the workflow files — the estate already has the six-case matrix for this (`docs/traps.md:512-524`) | every session |
| **R-16** · A self-blessing button re-pins the artifact the gate compares against | `lane-claimed`, F-D05: **8** of the predecessor's tools ship a regeneration flag (`check_compat_frozen --write`, `manifest_compile --write`, `mint_golden --write`, `plugin_pin --write`, `check_lockfile_fresh --regen`, …), and F-D11: boot-gate leg A refuses on divergence from a snapshot that `manifest_compile --write` regenerates | a PR whose diff contains both a behaviour change and its regenerated baseline | ratchets are **direction-limited in source** (the predecessor got this right twice — F-S04, `lane-claimed`), and a regenerated artifact may not land in the same PR as the change it blesses | reviewer |
| **R-17** · The real-guild record is an unvalidated string | `lane-claimed`, F-D04, executed in-process against the real validator: `surface_id='/NO_SUCH_COMMAND_AT_ALL'`, `signer='me'`, `signed_at='not-a-date'`, `build_sha='zzzz'`, evidence links `'x'` and `'y'` → **zero problems, EXIT=0** | the first R4 record accepted with a field nobody resolved | the four resolution checks at rung R4 ([`08-verification.md`](08-verification.md) § 4), and **the signer is a human, never the session that wrote the feature** | reviewer |
| **R-18** · A review instrument is published to the population it measures | **`MEASURED`** I-15, this run's own defect: the survival rule was printed into the agents' prompt and then passed **108 of 110 strengths and 125 of 127 defects (98 %)**, with **45 % of rows landing on `consumers = 2`**, the threshold itself | a filter with a pass rate above ~90 % on a real population; a field distribution piling up on a threshold | never publish the predicate to the agents whose rows it scores — give them the **evidence** standard, keep the **rule** out of the prompt, and measure the pass rate on the real population as well as on fixtures | any session running a fan-out |
| **R-19** · A green board is read as readiness | `lane-claimed`, CHALLENGE F, constructive: a bot with all **863** clickable controls wired to resolvable no-op handlers, one golden per subsystem and one forged sign-off row per subsystem **passes 7/7 required checks**; and F-D10: all six required AST scans assert *absence*, which a bot doing nothing violates none of | any status-shaped report whose headline is a check count or a test count | **two verdicts, always adjacent, never summed** — PRODUCT (R-ladder, denominator visible) and DEPLOYMENT (host, real dependencies) — and a green board is explicitly **not** an input to any cutover rung ([`09-roadmap.md`](09-roadmap.md) § 9) | owner + reviewer |

### 4.1 · R-13 expanded — why this one is the register's centre of gravity

It is the estate's **dominant** failure class, not this family's: three source-read
instances in three repositories plus a fourth in the estate's own false-done
ledger ([`04-root-cause.md`](04-root-cause.md) § 2.5). What makes it a live risk
for a *fresh* repository, rather than a lesson already learned, is that every
measured instance was written by someone who understood the property they were
checking:

- `superbot-next` **built the reachability walker** and pointed it at a registry
  its own `autouse` conftest empties (I-2) — and the walk is doubly dead, because
  `register_hub()` has **1 definition and 0 production callers** (**`MEASURED`**,
  I-16), so removing the fixture would not arm it either.
- `superbot` **built the mutation test** that proves a guard has teeth, and
  applied the mutation to the model and checked it against the model
  ([`08-verification.md`](08-verification.md) § 3.2).
- `superbot-next` **built the denominator assertion** that fixes exactly this —
  `tools/run_golden_parity.py:162-170`, naming the false-green in its own comment
  — and left it in that one file.

**The four failure routes into a fresh repository**, each with the instrument that
closes it:

| route | closed by |
|---|---|
| a fixture empties the population before the gate runs | R-06's rule: a gate may not run in a fixture scope that can clear its population |
| the gate walks a model built beside the artifact | *"the shipped artifact rather than a model of it"* — the clause, not the intent ([`08-verification.md`](08-verification.md) § 1) |
| the population shrinks and nobody decides to shrink it | the committed, versioned `FLOOR`, so a shrink is a reviewable diff |
| the gate's glob matches nothing | **`MEASURED`** I-16: `ls sb/domain/*/ui/*.py` → **0 files across 49 directories**, under a required `NO EXPIRY` gate whose baseline is literally `{"per_subsystem": {}, "total": 0}`. Closed by the same `FLOOR` line, and by printing the population size in the gate's own output |

**The honest counterweight, because it is what makes the mitigation credible.**
The predecessor's **golden-parity gate refuses to be vacuous** — with no Postgres
it prints `gate: RED — 50 subsystem(s) are flipped 'ported' but no replay is
possible` and exits **1** (**`MEASURED`**, I-20). One gate in this family already
does the right thing. The successor's requirement is that it is the **default
shape of a check**, not one good day.

---

## 5 · Migration and portability risks

| risk | why it is credible HERE | early warning sign | mitigation | owner |
|---|---|---|---|---|
| **R-20** · **Cog portability fails for stateful modules** — the successor repeats the fence and OD-19 is met for the stateless minority only | expanded in § 5.1 | S2's module chosen because it owns no tables | S2 ports a module that **owns tables**, from **out of tree**, or S2 has not happened ([`09-roadmap.md`](09-roadmap.md) § 3) | S2 session |
| **R-21** · The out-of-tree path is second class — in-tree modules quietly gain privileges the plugin path lacks | I-10 is exactly this failure already run once: `ALLOWED_FACETS` vs `HOST_ONLY_FACETS` at `sb/app/plugin_host.py`, with the docstring naming the reason as *"migrations, S12 money lanes, and the G-19 setup registry have no out-of-tree lane yet"* | the first facet, helper or table an in-tree module may declare and an out-of-tree one may not | **one loader for both paths** ([`06-architecture.md`](06-architecture.md) § 12 row 19), and the first module ships **through the out-of-tree path** so the privileged path is the one under test | S2 session |
| **R-22** · The portability gate degrades to an empty population and stays green | `lane-claimed`, M8-D04 / F-D08: the plugin-boot leg of `check_runtime_smoke` — *the only automated proof of the owner's cog-portability requirement* — returns an empty problem list when its examples are absent, measured by `mv examples /tmp`, with the verbatim comment *"nothing to prove"* | the gate passing on a machine with no plugin installed | the gate declares its population and asserts a floor of **≥1 installed out-of-tree module**; a run with zero modules is RED, not clean | S2 session |
| **R-23** · A ported cog brings its cycles and its shared floor | `lane-claimed`, A-D03: the intersection of all 58 non-trivial `superbot` cog closures is **148 modules / 30,925 LOC across seven top-level packages** — lifting one cog is not a 3,389-line job; and [`07-feature-contract.md`](07-feature-contract.md) § 5.6 finds `fishing` in **2 mutual subsystem pairs visible only in function bodies** | a ported module's import closure exceeding its own directory by more than its declared dependencies | R-03's whole-AST guard applied to the ported module **at the port**, plus the closure measured and recorded before the port is accepted | S2 session |
| **R-24** · Production data import creeps in without an owner decision | [`12-owner-decisions.md`](12-owner-decisions.md) **OD-E** default is *import nothing*; `superbot` carries **104 migrations** and **45 `utils/db/` submodules**, and the live Postgres was **not read by this session** | any migration, script or fixture referencing a production table or a production connection string | OD-E's default holds until he answers; if he wants continuity he names **server-visible surfaces**, not tables, and it becomes a rehearsable exercise ([`10-migration.md`](10-migration.md)) | owner |

### 5.1 · R-20 expanded — the requirement fails silently, and it has already failed once

OD-19 is not a preference: *"I should be able to add exiting cogs to it on demand,
or be able to slightly alter an existing cog so that it works with this bot."*
The predecessor's answer was a genuinely good plugin host — entry-point discovery,
hash-pinned in `plugins.lock.json`, compiled in one joint pass — with a facet
fence that makes **29 of its own 49 subsystems ineligible** (I-10). The **20**
that are eligible are the stateless ones; everything that owns data —
`economy`, `moderation`, `roles`, `setup`, `xp`, `settings`, `ticket`,
`starboard`, `btd6`, `mining`, `fishing` — cannot be a plugin.

**Why the risk is that this recurs rather than that it was a one-off:** the data
lane is the expensive half, it has no user-visible payoff in the slice that builds
it, and deferring it is invisible — the extension mechanism *works*, for the
subset that needs nothing. That is the same shape as I-11's registry (better
abstraction, collapsed population) and it produced the same outcome.

**Two things make this tractable rather than merely hard.**

1. **Portability here is demonstrated, not hypothetical.** `superbot`↔`superbot-next`
   have **54 file pairs above 0.55 similarity, 8 at ≥0.90, and one byte-identical**
   — `disbot/utils/mining/capacity.py` and `sb/domain/mining/capacity.py` share
   md5 `64f1665a9fb83a940d95eca5b9492bf2` (I-21). A domain module has already
   crossed these two architectures unchanged. The fence is a **contract choice**,
   not a structural limit.
2. **The exercise is already scored.** [`07-feature-contract.md`](07-feature-contract.md)
   § 5.6 runs five real cogs against the contract: `starboard_cog` is
   **PORTS WITH ITS DATA — "nothing [is not mechanical], once § 3.5 exists, and
   impossible without it"**; `fishing_cog` is **CARRIED, CYCLES ARE THE WORK**.
   Those two are the acceptance test for R-20, and they exist today.

**The early warning is one sentence long:** if S2's module owns no tables, the
requirement has not been exercised, whatever the slice's board says.

---

## 6 · Operational risks

| risk | why it is credible HERE | early warning sign | mitigation | owner |
|---|---|---|---|---|
| **R-25** · **The live production bot is disturbed** | expanded in § 6.1 | any command, script, credential or workflow in the successor's tree that names `superbot`, its Railway service, its Postgres or its Discord application | the estate rail, unchanged: **nothing in this plan modifies `superbot`, its worker, its database or any Discord surface it serves** ([`09-roadmap.md`](09-roadmap.md) § 1.1) — plus § 6.1's four separations | every session |
| **R-26** · A shared credential, application, guild or database between the successor and an incumbent | `spider-bot` is live in the Slingy Spider server with real users, and OD-C's default keeps it running untouched; the venue is an **owner step** and four items ([`09-roadmap.md`](09-roadmap.md) § 1.1) | the successor booting against any token, guild or database that an incumbent also uses | S1 cannot start until an **isolated** Discord application + bot token, a test guild and a test Postgres exist, none shared ([`06-architecture.md`](06-architecture.md) § 11) | owner |
| **R-27** · "Online" means connected, not serving | **`MEASURED`** I-19: `sb/app/main.py:616` hardcodes `sync_remote(bot, committed, enabled=False)` and `sb/app/tree_sync.py:53-55` returns `SyncOutcome(False, "disabled")` before touching Discord — **this root never publishes a slash command at all**, while `/ready` answers 200. The design decision to degrade rather than refuse rests on a survivor set that does not exist | a boot that reports healthy without reading its command count back from Discord | `SURFACE` floor record ([`06-architecture.md`](06-architecture.md) § 12 row 17): **"online" is a named, counted, reachable command surface asserted at boot against a committed floor**, with `commands_published` read back from Discord | S1 session |
| **R-28** · A degraded state reaches no durable sink | `lane-claimed`, R4-D02/D11: the degrade notice appends to a module-level `deque(maxlen=256)` with **zero sinks attached**, is suppressed on later boots by a **durable** latch, and the in-Discord card meant to surface it (`!platform findings`) is a frozen literal that always renders *"(none)"* — three independent mechanisms, each of which alone would have hidden it | a degraded-state path whose sink is in-process; an observation window with **zero** recorded degradations | every degraded state goes to a sink that **survives the process**, and criterion 5 of the observation window makes a zero-degradation window a reason to check the sink ([`09-roadmap.md`](09-roadmap.md) § 9) | S5 session |
| **R-29** · There is no recovery lever below process level | `lane-claimed`, R4-D10: **0** occurrences of `reload_extension` under `sb/`, no cog model, and the only runtime lever is a process exit; R3-D6: any single plugin problem aborts the **entire** boot. `superbot`, by contrast, has two independent in-Discord levers with a deliberate protection asymmetry (`lane-claimed`, R4-S06) | a boot that fails whole because one module is wrong | **disable is the incident lever and it is the same lever as visibility** ([`06-architecture.md`](06-architecture.md) § 4.5); per-module fault isolation with the interlock that stops it hiding a missing bot (§ 4.3) | S5 session |

### 6.1 · R-25 expanded — the two live bots, and what actually reaches them

This is the only risk in the register whose consequence lands on **real people in
minutes**, so it is stated with the mechanism rather than as a caution.

**`superbot` — the live production bot.** **`MEASURED`** by this session at
`docs/operations/production-deployment.md:102`: **`Watch Paths | (none) | Every
push to main builds; no path filter.`** In a four-service monorepo that means any
push to `main` restarts the Discord gateway worker, and the estate's record says
this already cost **~293 unnecessary production restarts** with the root cause
still unfixed (`lane-claimed`, M7-D4). Its `Healthcheck Path` is also `(none)`,
so the health endpoints it genuinely ships (`disbot/healthserver.py`) are not
what the platform watches (`lane-claimed`, M7-S4).

**`spider-bot` — live in the Slingy Spider server.** **`MEASURED`** at
`.github/workflows/ci.yml:1-2`, verbatim: *"Informational quality gate … It does
NOT gate anything yet - pushes to main still auto-deploy to Railway."* Every
guard in that repo can go red on `main` while the live bot deploys anyway.

**So the disturbance vectors are pushes and shared resources, not code review.**
Four separations, all already decided elsewhere and repeated here because this is
the register that has to hold them:

1. **Repository.** The successor is a third repository (OD-C default); no commit
   in this programme lands on `superbot` or `spider-bot`.
2. **Deployment.** Its own Railway service, its own image, its own start command
   — never a second service in an incumbent's project.
3. **Identity.** Its own Discord application and bot token, its own test guild.
   A shared token is a shared rate limit, a shared audit log and a shared
   presence.
4. **Data.** Its own Postgres. OD-E's default is *import nothing*, so there is no
   reason for a connection string to production to exist anywhere in the tree.

**And the early warning that is worth more than the rule:** the first time a
successor artifact *names* an incumbent's service, token, guild or database —
even in a comment, a `.env.example` or a docstring — the separation has already
started to erode. That is greppable, and it should be grepped at every slice
exit.

---

## 7 · AI risks

| risk | why it is credible HERE | early warning sign | mitigation | owner |
|---|---|---|---|---|
| **R-30** · **AI authority creeps past [the 2026-09-04 AI-authority decision](run/in-flight-direction.md)** | expanded in § 7.1 | the first model output that reaches an action without passing a typed schema validation | [the 2026-09-04 AI-authority decision](run/in-flight-direction.md)'s pipeline as **code structure**, not convention: `event → deterministic pre-check → optional AI analysis → typed schema-validated verdict → policy engine → permission/risk gate → typed operation → Discord API → audit + case` ([`05-product-definition.md`](05-product-definition.md) § 7.1) | S4 session |
| **R-31** · Free-form prose becomes an action | `lane-claimed`, M12-D05: `spider-bot`'s *"the AI never causes side effects"* — one of only two invariants `docs/intent.md` names as most tempted to violate — **has no test, lint rule or import-boundary guard behind it**, and holds today only because nobody has wired `gateway.reply()`'s output into a role or moderation call | any code path that parses model text for an intent, an id, or a command name | invalid or incomplete model output means **no automatic action**, and that path is tested with a deliberately malformed verdict as the positive control | S4 session |
| **R-32** · The AI tool registry ships empty, or read-only, and nothing notices | **`MEASURED`** I-11: `superbot`'s **36**-tool catalogue with exactly one audited write (`open_support_ticket`, through the audited mutation seam) became `superbot-next`'s open registry with **one** `register_tool(` call site and **8 rows, all BTD6 factual reads at `AIScope.USER`, zero write-capable** — and byte parity could not see it, because an unregistered tool emits no output | a tool count that does not appear in any gate's output | a **committed floor on the tool registry** ([`06-architecture.md`](06-architecture.md) § 12 row 13), asserted in the same run as the tools' tests — the same one line that fixes the navigation golden | S4 session |
| **R-33** · Shadow mode produces no record a human can review | `lane-claimed`, M10-D3: the `AIScope` lattice is real, tested code that is **never driven by the actual per-user Discord authority** the button path uses — every production call site sits at the `USER` floor by default; without a case record there is nothing to widen authority *from* | a shadow-mode deployment with no queryable record after a week | the **case record** ([`06-architecture.md`](06-architecture.md) § 12 row 20) is S4's deliverable, and criterion 4 of the observation window joins **audit rows on actor kind — not the classifier's own log** | S4 session |
| **R-34** · The AI-off path decays until the bot needs a provider to function | `lane-claimed`, M12-S04: `spider-bot` gets this right — the gateway only constructs a client when both `ai_enabled` and a key are present, checked at 3 real trigger points; the risk is the successor losing it as AI surfaces grow | the first journey whose canonical path requires a model call | the **AI-off suite is a slice exit criterion** ([`05-product-definition.md`](05-product-definition.md) § 8; [`09-roadmap.md`](09-roadmap.md) S4 exit), green with no provider configured | S4 session |

### 7.1 · R-30 expanded — where the creep actually happens

[The 2026-09-04 AI-authority decision](run/in-flight-direction.md) is unambiguous — **AI supplies judgement, deterministic code supplies
authority** — and [`05-product-definition.md`](05-product-definition.md) § 7.2
records that this plan **confirms** it rather than proposing it, because the live
production bot already ships a compatible shape: 36 catalogued tools, exactly one
write, and that write goes through the same audited mutation seam a button uses
(I-11).

**The creep does not arrive as a decision to give the model more power.** On the
evidence it arrives in three ways, none of which reads as a policy change at the
time:

1. **A convenience parse.** The verdict schema is strict, a model returns
   something almost-valid, and a small tolerance is added. That is the moment
   free-form prose becomes an action, and it is invisible in a diff unless the
   schema is a *typed boundary object* rather than a dict the caller inspects.
2. **A second write path.** The AI reaches a mutation that is not the typed
   operation the button path uses. This is the one measurable precondition
   already present in the family: `superbot`'s authority is **166 hand-placed
   decorators** and its audit is **49 hand-written call sites across 27 files**
   (`lane-claimed`, CHALLENGE B; the 49/27 re-derived in I-18) — under that shape
   a second write path is a normal-looking commit.
3. **A threshold crossed by accumulation.** Shadow mode produces a good track
   record and the confirmation step is dropped without a decision. OD-F's
   recommended default forecloses this explicitly: *any later
   confirmation-free expansion is a new, explicit decision rather than a
   threshold the system crosses on its own.*

**What holds it, mechanically:** one `resolve()` entry point that the AI path
uses like every other surface ([`06-architecture.md`](06-architecture.md) § 12 row
11), `authority_ref` carried on the **operation** rather than attached to the
surface (row 5), one audit writer **inside the operation's transaction** (row 6),
and the risk/mode gate shared by AI actions and destructive button confirmation
(row 14) — so an AI write and a human write are the same code path with a
different actor, and there is no second lane to widen.

**Where the evidence runs out:** how much authority is appropriate on day one is
a risk appetite, and it is his. That is [`12-owner-decisions.md`](12-owner-decisions.md)
**OD-F**, whose default is auto-act on low-risk reversible operations, preview
and confirm for medium risk, deny high-risk and destructive outright. **The
pipeline order is identical under every answer he could give; only the tier
boundaries move.**

---

## 8 · Scope-growth risks

| risk | why it is credible HERE | early warning sign | mitigation | owner |
|---|---|---|---|---|
| **R-35** · The per-feature increment gets heavier than the bot it replaces | `lane-claimed`, A-D08: `superbot-next`'s marginal cost per subsystem measured at **52 modules / 10,149 LOC**, against `superbot`'s **15 modules / 3,389 LOC** on the same walker with matched thresholds — the rebuild made the per-feature increment **3×** heavier on the axis OD-19 names as a hard requirement | the second feature costing more than the first | the marginal closure is **measured at each slice exit** and recorded; § 14 of [`06-architecture.md`](06-architecture.md) already commits the successor to `spider-bot` scale for slice one (**3,172 lines / 27 files** running a live, useful bot) | reviewer |
| **R-36** · A file with no ceiling | **`MEASURED`**: `sb/domain/settings/panels.py` is **2,567 LOC** — **3.2×** `superbot`'s hard ceiling of `FAIL_LOC = 800` (`tests/unit/invariants/test_cog_size.py:42`, a `pytest.fail` in the required gate) — and it grew 89 → 504 → 1,214 → 1,910 → 2,334 in weeks (`lane-claimed`, E-D5). `superbot`'s ceiling has the opposite pathology: **7 of 59** cogs sit within 18 lines of it (`lane-claimed`, E-D4) | any file passing ~600 lines with no decomposition stage planned | a **size ceiling that hard-fails in the required gate**, plus the lesson from E-D4: the ceiling must be paired with a decomposition seam, or it becomes the design target | reviewer |
| **R-37** · The exemption ledger grows faster than the product | `lane-claimed`, E-D9: `sim/sim-gate-baseline.json` carries **904 exempt assignments** (9,202 lines) with zero sim records after two months — **5.4×** the predecessor's ledger; and **`MEASURED`** ([`08-verification.md`](08-verification.md) § 3.4): only **2 of the 10** checkers that carry exemptions expire them | the first allowlist entry with no expiry date | every allowlist, exemption, baseline and `cross_cutting` entry carries a reason and a date, the checker fails on an expired row **and** on a row matching nothing, and the rule lives in the checker **template** | every session |
| **R-38** · The generated diff nobody reads | `lane-claimed`, E-D8: **~84,400 lines** of derived/ledger state committed across 8 artifacts, `manifest.snapshot.json` alone **70,745 lines** — every feature PR carries a machine-generated diff a human must read or wave through | a PR whose generated diff is larger than its source diff | generated artifacts are **derived at build time or committed with a summary the reviewer reads instead** — and R-16's rule keeps the regeneration out of the PR that changes behaviour | reviewer |
| **R-39** · Documentation regrows, and the plan becomes the work | **`MEASURED`** I-9: the EAP added **2 runtime files** to `superbot` and **183 surviving documentation files in fourteen days** (~13/day); `lane-claimed` A-D04: `superbot`'s doc corpus is **863 files / 185,658 lines**, 76.1 % the size of the runtime, with `docs/planning` alone at **292 files / 61,398 lines** | a second planning package before slice one ships | [`09-roadmap.md`](09-roadmap.md) § 8: **a documentation programme is never a slice** — the successor's documentation is its declaration and its record; and this package's own verdict permits building slice one **now** ([`13-verdict.md`](13-verdict.md)) | owner + every session |

---

## 9 · The tripwire board — which warnings are mechanical, and which are not

The register is only worth its early-warning column, and that column is honest
only if it says which signs a machine can raise. **Twelve of the thirty-nine can
be a check; the rest need a human to look**, and pretending otherwise is the
defect this whole package is about.

**Mechanical — these become checks in S1, and each ships with a negative control**
(a fixture that must make it fire, in the same run):

| tripwire | raises | risk |
|---|---|---|
| every gate prints its population size and asserts `>= FLOOR` | R-13, R-22, R-32 | the population contract |
| a skip inside a required gate | R-14 | red, not green |
| `\| tee` or `$?`-after-pipe in any workflow `run:` block | R-15 | swallowed exit codes |
| whole-AST import scan with cycle detection | R-03, R-23 | function-body coupling |
| more than one presenter implementation outside `tests/` | R-04 | the renderer twin |
| a second `clear_*_for_tests`, or an `autouse` fixture clearing a gate's population | R-06 | emptied populations |
| `check_feature_locality` over the PR diff | R-02 | non-local features |
| a declared field with no non-default value and no reader | R-07 | grammar without consumers |
| a file over the committed LOC ceiling | R-36 | god files |
| an allowlist row with no expiry, or matching nothing | R-37 | excuse rows |
| `commands_published` below the committed surface floor at boot | R-27 | "online" ≠ serving |
| a successor artifact naming an incumbent's service, token, guild or DB | R-25, R-26 | separation erosion |

**Human-watched — no instrument, and the register says so rather than inventing
one:** R-01's three artifacts existing *and being reproducible by a second
person*; R-11's module-selection reasoning; R-19's reading of a green board;
R-30's convenience-parse (a diff can show the tolerance; only a reader knows it
is one); R-35's marginal-cost trend; R-39's plan-versus-build ratio. These are
slice-exit review questions, and they belong in the slice's exit criteria rather
than in a checklist nobody re-reads.

**And the tripwire the register cannot install on itself.** I-20 is the standing
warning: this session's own worst reading was the one that **agreed with its
thesis** — `$?` after a pipe returned `EXIT=0` and made a correct gate look
vacuous, and nothing caught it because a review about vacuous gates finding a
vacuous gate was exactly what was expected. **A finding that confirms the plan
gets the second look, not the one that contradicts it.**

---

## 10 · Risks that are owner decisions, not engineering risks

Routed rather than mitigated, because inventing product intent here is the one
failure this package refuses:

| open question | the risk it is the source of | where it lives |
|---|---|---|
| one server or many | R-11 and the whole size of S1's setup surface; whether S6 exists at all | **OD-A** |
| is replacement ever promised | R-01's fifth difference; whether the cutover ladder is ever climbed | **OD-B** |
| third repository or `spider-bot` grown | R-25 and R-26 change from *avoidable* to *first-order* — S1 becomes a refactor inside a live bot with no PR gate | **OD-C** |
| which community features are core | R-11, and how much load S2 puts on the extension contract | **OD-D** |
| does production data carry forward | R-24, and whether a rehearsal phase exists at all | **OD-E** |
| how much authority the AI holds on day one | R-30's tier boundaries — **not** the pipeline, which is identical under every answer | **OD-F** |

Every one has a recommended default in [`12-owner-decisions.md`](12-owner-decisions.md)
that the work can proceed under, and **OD-A is the only one that materially moves
the architecture** ([`13-verdict.md`](13-verdict.md) gap 3).

---

## 11 · What is deliberately NOT on this register

Recorded so each absence reads as a decision.

- **"The rebuild might not be worth doing."** That is not a risk this file
  manages; it is a live argument in the evidence, and it belongs to the owner.
  CHALLENGE A's measurement is the strongest form of it — `superbot` is **12 of
  883 modules and 1,695 of 243,961 lines (0.69 %) unreachable from its
  composition root, with exactly one `TODO` in the tree** (`lane-claimed`) —
  which is evidence that a large Discord bot survives three years without
  structural collapse. [`01-executive.md`](01-executive.md) § 1.5 states it; this
  register does not re-litigate it.
- **Schedule and effort risk.** No estimate exists anywhere in this package, in
  hours or in lines, and [`07-feature-contract.md`](07-feature-contract.md) § 5.8
  says why: nothing in this evidence base supports one. A schedule risk written
  against an invented estimate is a number wearing a warning label.
- **Provider, platform and dependency risk** (Discord API changes, Railway,
  model deprecation). Real, and generic — nothing measured in these repositories
  makes them more or less credible here than anywhere else, and a register that
  lists them dilutes the twelve tripwires that are specific.
- **Security and abuse risk beyond the AI boundary.** Out of scope for this
  package, which produced no threat model. The one adjacent measured item —
  prompt-injection containment, present and tested in both `superbot-next`
  (M10-S3) and `spider-bot` (M12-S02, `lane-claimed`) — is a `PRESERVE_CONTRACT`
  in the matrices, not a risk row.
- **Anything requiring a running bot to assess.** Every dynamic claim in this
  package is a static read ([`13-verdict.md`](13-verdict.md) gap 1). A risk that
  needs a boot to be credible would be an invented one, and this register would
  rather be short.
