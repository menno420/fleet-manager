# The active-repo intent audit — can a cold session tell what each repo is for?

> **Status:** `audit` · 2026-08-23 · owner-asked, mid-session:
> *"look at all the currently active repos and find out if each one has clear
> goals and a well explained intent, so any fresh session would know what to do
> with it."*
>
> **What this is:** D2's acceptance test — *a cold session states the repo's
> purpose, live state and next step from ≤3 files* — run as a **sweep** across
> the unarchived repositories instead of one repo per session.
>
> **CENSUS CORRECTED 2026-08-24 (`@codex`, fm #938): this sweep covers 16 of the
> 17, not all 17.** The verdicts below name 16 repositories, and the headline said
> *7 pass* while listing **6**. The missing repository is **`spider-swing`** — it
> appears only in § 5's activity table and carries **no verdict at all**, which
> matters because it is the one asset with a live external clock. It has not been
> judged against the cold-session test; do that before anyone calls this complete
> or derives a D2 order that assumes it passed. It exists
> because `OQ-FM-D2-TARGET` has been picking D2's next repo by guess; this
> replaces the guess with a ranked list of which repos actually fail.
>
> **CENSUS DISCHARGED 2026-08-24 (fm #940): `spider-swing` is judged. It FAILS,
> and it takes rank 1** — so the caution above was worth writing: the order below
> it *was* wrong. § 6 is re-ranked and no longer provisional. The same pass
> re-read `product-forge`'s declared entry point and found that **the verdict
> recorded here names the smaller of its two defects** — see § 1. Both
> re-judgements moved the work, which is the argument for classifying before
> fixing rather than after.
>
> Certainty tags per [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).

## 1 · The verdicts

**6 pass · 5 unrated · 1 stale · 4 fail · 1 hub = 17 of 17** — complete as of
2026-08-24. *Originally published as "7 pass" against a list of six, and as a
17-repo sweep that covered 16; both corrected.* Judged from each repo's own
declared entry point.

**The four failures are not one kind of failure, and the distinction decides the
order.** Two are **empty** front doors — `estate-backups`' two lines, and
`product-forge`'s placeholder ledger. A cold session reads a blank, knows that it
knows nothing, and goes looking; that costs one wasted read and is recoverable.
The other two are **contradicting**: a front door that states, confidently and in
detail, something the repository has since stopped doing. There the session does
not go looking — it acts.

**That class has already been ranked once, and the precedent is the argument for
ranking it again.** `idea-engine`'s failure was of exactly this kind — the front
door read *"SEAT DORMANT — shut down for good"* while OD-4 and OD-10, dated twelve
days later, kept it as a standing asset — and it was **rank 1** in the original
order and the first thing fixed (#900). `spider-swing` is the same shape: 345
coherent lines leaving a cold session confidently wrong about decisions the owner
has already taken. The estate has a name for it — [TRAP-001](../traps.md), a
dated document read as current state — and this instance sits in the front door
of the one repo with a clock.

*(`product-forge` turns out to be **both**, which is why its brief in § 7 does the
README before the ledger.)*

**✅ Pass** — `pokemon-mod-lab`, `gba-homebrew`, `venture-lab` share the same
five-section closeout, and the fifth section is literally *"Working this repo
with a fresh session"* — the test written into the document. `substrate-kit` has
an explicit `## Next action`. `curious-research` states its role and is dated.
`superbot-plugin-hello` says exactly what it is.

**◻ Unrated — not "weak"** — `superbot`, `superbot-next`, `websites`,
`couch-legend`, `shiftlife`. Each **delegates** its next step to a pointer, and
every target exists and is substantial (`superbot` NEXT-TASKS 4.8 KB,
`superbot-next` 9 KB, `websites` closeout 10.6 KB, `couch-legend` DESIGN 32 KB).
**These were first rated "weak" and that was an artifact of not opening the
targets** — corrected on `@codex` review. Rating a doc weak for delegating,
without reading what it delegates to, is not a measurement.

**◐ Stale** — `sim-lab`: refreshed 2026-07-13, retired coordination vocabulary,
never stated its current role. **Fixed 2026-08-23, sim-lab #360 `72ed751e`.**

**❌ Fail**
1. **`idea-engine`** — front door read *"SEAT DORMANT — shut down for good by
   owner order 2026-07-14"*, and probing for `standing asset` / `on-demand` /
   `R6` / `resume` returned **zero hits for all four**. **OD-4 and OD-10, both
   dated 2026-07-26 — twelve days later — keep it as a standing asset.** A cold
   session read "shut down" and stopped. **Fixed 2026-08-23, idea-engine #900
   `df6b0273`**; the same probe now returns hits on all six terms.
2. **`product-forge`** — 24 lines, still the generated template:
   *"(Describe the accepted-stable baseline once established…)"*. **Open.**
   **RE-JUDGED 2026-08-24 (fm #940), and the defect above is the smaller of two.**
   The template `docs/current-state.md` is real, but it is not the declared entry
   point — `README.md` is, and `README.md` is **entirely seat-era**. It opens
   *"product-forge — the fleet's product build seat"*, carries `Status: binding`,
   and routes a cold session to **wait for an ORDER in `control/inbox.md`, written
   by the fleet manager** — a seat retired 2026-07-21, from a roster retired
   2026-08-07. Its standing fallback is *"Empty inbox → polish the newest
   product's roughest edge and flag `inbox empty` in status"*, which sends the
   session to write a heartbeat into `control/status.md` for a coordinator that
   does not exist. It never names **`phone-controller`** — the repo's only living
   asset, a shipped Android Bluetooth-HID controller app whose 22 slice cards run
   to `2026-08-20-phone-controller-slice22-foldables.md` and whose own
   `products/phone-controller/README.md` is 18,456 bytes.
   **Consequence: filling in `current-state.md` would have closed the finding
   recorded here and left the repo still failing the test.** `MEASURED`
   2026-08-24 — README fetched and read in full, tree read live from the API
   (171 blobs, `pushed_at` 2026-08-20T20:06:59Z).
3. **`estate-backups`** — a two-line README and no other entry point.
   Everything real about it lives in the hub. **Open.** Confirmed 2026-08-24: the
   repo is **3 blobs** — `README.md` (130 bytes) plus `dump.yml` and `sizing.yml`.
   The two workflows carry good header comments; the README names neither.
4. **`spider-swing`** — **the front door contradicts the repo. NEW 2026-08-24
   (fm #940); this is the verdict the header correction asked for, and it takes
   rank 1.**

   It is the only failure where the cold session ends up *worse* informed than if
   the file had been blank. `README.md` is 345 lines, well written, and its front
   matter is wrong on the one thread that has an external clock. All four
   findings below were checked against a live surface, not against another
   document.

   - **The name is settled and the README says it is open.** Lines 10–17 are a
     blockquote headed *"'Spider Swing' is a codename"* — *"**Not approved
     release branding.** … Naming, trademark, domain, and store-conflict review
     are all still open."* The name was decided **2026-08-05** as **Slingy
     Spider**; spider-swing **#171** (*"Record the trademark register search
     against the decided name"*) merged `2026-08-05T11:27:20Z`, and the repo's
     own `docs/current-state.md` records a signed bundle published under
     `com.menno420.slingyspider`. A cold session is invited to re-open a decision
     the owner closed nineteen days ago.
   - **`"No release signing exists."`** — line 268, flatly false.
     `.github/workflows/android-release.yml` is in the tree at **14,303 bytes**,
     and `current-state.md` records it as dispatch-only, signing with the
     external upload key, and *"has run successfully through version code 66."*
   - **`"…store publishing remain absent."`** — line 191. Narrowly defensible
     (nothing is *public*) and misleading in effect: signed version code **64**
     has been live on Play's **internal-testing** track since 2026-08-05 and was
     owner-confirmed working on 2026-08-23.
   - **The clock is invisible, and the two mentions of Play both deny it.**
     `grep -ci` over the README returns **0** for `closed test`, `internal
     testing`, `tester`, `Slingy`, `slingyspider` and `version code`; positive
     controls on the same file return `swing` 17, `Godot` 13, `Reel-In` 3, so the
     query works ([TRAP-003](../traps.md)) — and the file was read in full, which
     is what that trap actually requires. The only two occurrences of *"Google
     Play"* are a scope boundary (*"There is no Google Play Billing SDK"*, line
     194) and a prohibition (*"must **NEVER** be reused for Google Play"*, line
     267). Both frame Play as a thing that has not happened.

   **Why it still isn't a lack of truthful documentation.** `docs/current-state.md`
   is current to 2026-08-23 and carries all of it, including *"closed testing has
   not started."* The ≤3-file path even fits: `README.md` → `docs/AGENT_ORIENTATION.md`
   → `docs/current-state.md`. But README's Documentation table lists **ten**
   documents and includes **neither** `current-state.md` nor
   `docs/technical/play-closed-test-runbook.md`; the single pointer to
   `current-state.md` is at **line 340 of 345**, in the closing prose. The only
   forward-looking thing the front door offers is *"Phase 0 is tracked in issue
   #2"* — and issue #2 was last updated **2026-07-28** (live read, 2026-08-24),
   while `current-state.md` says it *"is expected to stay open for weeks or
   months … not a test run that closes it."*

   **So the repo fails on a front door that argues against its own ledger** — not
   on absence. That is why it outranks the empty ones, and why the fix is subtractive
   (delete four claims, add two pointers) rather than a writing job.

**Which rule decides a supersession, since this pass got it wrong once:** it is
**not** `.claude/CLAUDE.md` § Precedence — that governs *the live owner vs.
stored text*, and both sides here are stored text. It is
[`../MAP.md`](../MAP.md)'s closing rule: **"when two records disagree, the later
date wins."**

## 2 · The structural finding, narrowed after review

The first draft said *the hub is richer than the repos, estate-wide*. That
generalised from the three failures and was **partly manufactured by not
following pointers**. Narrowed: **for `product-forge` and `estate-backups`,
`ESTATE.md`'s one-line row is more informative than the repository's entire
entry point.** That is fine while every session boots at the hub, and fails the
moment one does not — the case the boot file already flags as invisible.

## 3 · `superbot` carries a diverged fork of `botsite/` and `dashboard/`

`MEASURED` 2026-08-23, and it is the sharpest misplacement in the estate.

- Both `superbot` and `websites` contain `botsite/` and `dashboard/`.
- **28 shared filenames, ZERO byte-identical** — including `app.py`, `Procfile`,
  `requirements.txt` and eight templates each. Compared by blob SHA, not by
  listing. **A fork, not a duplicate.**
- **No such services exist in `reliable-grace` today.** `MEASURED` live via
  Railway GraphQL, full workspace sweep with no assumed project id: **3 projects
  / 8 services**; `reliable-grace` = **`Postgres` + `worker` only**. Re-run a
  second time asking each service for its latest deployment status, because a
  *dormant* service would still be listed: same two, both `SUCCESS`. **That
  premise was itself unverified when first written and is now measured** — a
  positive control exists in the same workspace: `superbot-websites/dashboard`
  reports status **`SLEEPING`** and still appears in the service list. So a
  non-running service IS listed with its state, and absence from the list is
  absence of the service — not dormancy. The live
  botsite and dashboard run from `websites` in `superbot-websites`.
  **Wording corrected 2026-08-23, same day:** this bullet first read *"the
  services were deleted"* under a `MEASURED` tag. What was measured is
  **absence now**; that they were *deleted* on 2026-08-20/21 is read from
  [`2026-08-14-railway-websites-audit.md`](2026-08-14-railway-websites-audit.md)
  `:298` — a document. Both halves are true and the conclusion is unchanged, but
  blending a live read with a citation under one `MEASURED` tag is
  [TRAP-001](../traps.md), committed in the record that reports TRAP-001.
- **`superbot` still runs CI for them** — `Botsite CI` and `Dashboard CI` both
  `active`, last run 2026-08-17; `dashboard-data-refresh` `active`, last fired
  2026-08-14 and **unexplained since**.

**The danger is not the wasted CI.** It is that a session told to fix "the
dashboard template" meets two same-named files in two repos, differing, with
nothing in either saying which is live.

**Consequence for the dependabot ask:** file lists read directly from
`/pulls/{n}/files` — **#2448** touches `botsite/requirements.txt` only;
**#2447** touches `dashboard/requirements.in` + `.txt` only. **No root-level
files in either.** They update dependencies for **services that no longer
exist**, and can be closed rather than merged into the careful window. This
conclusion needs only the absence, not the deletion history: nothing serves that
code, which `reliable-grace`'s service list and superbot's root `Procfile`
(`worker: python disbot/bot1.py`) establish independently.

**How this was got wrong twice first, because the method matters more than the
finding:** a Layer-2 doc, then a workflow header comment written **2026-06-17**
— two months before the 08-20/21 cutover — were each read as current state, and
a correct finding was retracted on the second. The owner corrected it from
memory and the live read agreed with him. Registered as
[TRAP-001](../traps.md).

## 4 · Two open seams — named, not resolved

- **`postgres-botsite` is gone.** The live sweep shows `reliable-grace` =
  `Postgres` + `worker`, while
  [`2026-08-14-railway-websites-audit.md`](2026-08-14-railway-websites-audit.md)
  `:298` still records it present and `:304` calls it protected by W1's hard
  rail. `OQ-RG-ORPHAN-VOLUMES` already says "1 Postgres", so the queue agrees
  with the live read and the audit doc is the stale one. **Not corrected here:**
  it is a hard-rail record and wants a session scoped to it.
- **`4-gate` vs `five-question`.** OD-4 keeps `sim-lab` for *"the 4-gate
  verification method"*. The string `4-gate` appears **nowhere** in sim-lab's
  README, whose own gate is the *five-question validity gate*. Most likely
  vocabulary drift — `ESTATE.md` already flags sim-lab drift — but the bridge
  between OD-4's phrase and the repo's components is **unverified**, and sim-lab
  #360's banner asserts it. Trace where "4-gate" originates before anyone builds
  on the mapping.

## 5 · Work distribution, measured — and NOT with `search/issues`

`MEASURED` 2026-08-23 via `GET /repos/{owner}/{repo}/pulls?state=closed`
filtered on `merged_at`, last 14 days:

| repo | merged |
|---|---|
| `fleet-manager` | **99** |
| `superbot` | 64 |
| `websites` | 19 |
| `couch-legend` | 18 |
| **`spider-swing`** | **2** |

An earlier figure of *"fleet-manager 86 · spider-swing 2"* came from
`search/issues` and was carried second-hand. **Do not measure this account with
`search/issues` or `search/code`** — the index covers a minority of these repos
and an unindexed repo returns 0, indistinguishable from a true zero
([TRAP-003](../traps.md); the EAP evidence pack § 0 measures the same effect).

**The reading:** the estate is not doing *only* machinery — `couch-legend` 18 and
`websites` 19 are product work. The sharp fact is narrower: **`spider-swing` is
the starved one, and it is the only asset with an external clock running.**

### Re-measured live 2026-08-24 — and the starved reading needed re-checking

`MEASURED` 2026-08-24, same method (`GET /repos/{owner}/{repo}/pulls?state=closed`
filtered on `merged_at`), window **2026-08-10 → 2026-08-24**:

| repo | merged, 08-23 window | merged, 08-24 window |
|---|---|---|
| `fleet-manager` | 99 | **103** |
| `superbot` | 64 | **53** |
| `websites` | 19 | **18** |
| `couch-legend` | 18 | **18** |
| **`spider-swing`** | **2** | **5** |

**`spider-swing` more than doubled, and the three new ones are the whole point:**
**#177** *Make release verification deterministic on Windows*, **#178** *Prepare
Google Play release package*, **#179** *Publish dedicated Play contact in privacy
policy* — merged `19:29:40Z`, `19:52:39Z` and `20:17:00Z` on 2026-08-23, while
this audit landed in fm #928 at **`17:19:21Z`** the same day. So they merged
**two to three hours after the measurement above was taken** — that ordering is
read from merge timestamps, not inferred. The repo had its busiest release day of
the month immediately after being recorded as the starved one.

**The two windows are not directly comparable, and the differences are not
drift.** The window slid one day, so 2026-08-09 dropped out and 2026-08-23/24
came in. `superbot` merged **11** PRs on 2026-08-09 and **0** on 08-23/24, which
accounts for 64 → 53 exactly; `fleet-manager` lost 8 and gained 28 across two
days. Cite one window or the other, never a row from each.

**What survives and what does not.** The *ordering* is unchanged — `fleet-manager`
≫ `superbot` ≫ `websites` ≈ `couch-legend` ≫ `spider-swing`, and `spider-swing`
is still last by a wide margin. What does not survive is using "2 merges" as
evidence that the repo is *dormant*: it is a repo with **one active thread** —
the Play release — that moves in bursts when the owner is in front of it. § 6
below ranks it first on its front door, not on this table.

## 6 · The order this implies for D2 — **settled 2026-08-24**

> **The PROVISIONAL marker is discharged, and it was right to have been there.**
> fm #938 held this order open because `spider-swing` was unjudged and carried the
> only live external clock. Judged (§ 1), it **fails**, and it **displaces
> `product-forge` at the top**. The order below it is otherwise unchanged.

1. ~~`idea-engine`~~ ✅ · 2. ~~`sim-lab`~~ ✅ · 3. **`spider-swing`** ·
4. **`product-forge`** (needed before its R2 graduation anyway) ·
5. **`estate-backups`** · 6. the date stamp on `websites`.

**Why `spider-swing` outranks `product-forge`, stated so it can be argued with.**
Not because it is busier, and not because of the clock alone — because of the
**kind** of failure. `product-forge` and `estate-backups` cost a cold session one
wasted read: the front door is visibly empty and the session goes looking.
`spider-swing`'s front door is full, coherent and wrong, so the session does not
go looking — it acts. The three specific wrong beliefs it hands over are *the
name is undecided*, *no release signing exists*, and *nothing is on a store*, and
each one is about the single thread with a deadline attached. A confident
falsehood on the critical path beats a visible blank anywhere else.

**What this does NOT decide.** `OQ-FM-D2-TARGET` stays open. This is the audit's
measured order, which is what a session runs when the owner has not named a
target — it is not a repository selection made on his behalf, and OD-13 still
orders methods work ahead of the product work inside any of these repos.

**Method limit, stated:** judged from each repo's declared entry point plus the
three closeouts opened, and — for `spider-swing` and `product-forge` as of
2026-08-24 — the entry point read in full rather than probed. The five unrated
repos could rate as passes if their pointer targets carry what their status docs
do not; that is one read each and is **still not done**.

## 7 · The fix briefs — written 2026-08-24 so the next session executes

**Why these are here and the fixes are not.** Each is a write to a different
repository with its own gates, its own born-red card and its own PR —
`spider-swing`'s `main` requires **both** `substrate-gate` and `game-quality`.
Four landings in one session is not OD-6. What classification bought is that
**two of these briefs are not what the verdict above originally implied**, so a
session that had gone straight to fixing would have fixed the wrong thing twice.

### 7.1 · `spider-swing` — rank 1, and the fix is mostly deletion

`README.md`, four edits. Line numbers are against the 345-line file as of
2026-08-24; re-read before editing.

| # | where | what | replace with |
|---|---|---|---|
| 1 | lines 10–17 | the *"'Spider Swing' is a codename"* blockquote — *"Not approved release branding"*, *"review are all still open"* | the settled position: published as **Slingy Spider** / `com.menno420.slingyspider` since 2026-08-05; `com.menno420.spiderswing.dev` remains the **debug** identity and is not changing. Source: `docs/product/name-status.md`, PR #171 |
| 2 | line 268 | *"No release signing exists."* | *"Release signing exists and is owner-controlled: `android-release.yml` is dispatch-only and signs with an upload key held outside the tree."* The sentence's true intent — that the committed debug key is not a release credential — is already the preceding sentence and should stay |
| 3 | line 191 | *"…store publishing remain absent."* | narrow it to what is true: no **public** listing, no billing SDK — while stating that a signed bundle is on the internal-testing track |
| 4 | lines 317–328 (Documentation table: header, rule, **ten** data rows) | none of the ten is the ledger | add **`docs/current-state.md`** and **`docs/technical/play-closed-test-runbook.md`**. The single pointer to the ledger is currently at line 340 of 345 |
| 5 | line 327 | the table's own *Name status* row — *"Why the title is a codename and what review remains"* | the same staleness as edit 1, in the row that points at the document which settled it. Fix both or neither |

**The one addition worth making, beyond correcting falsehoods:** the front door
should say the release is on a **clock** — 12 testers × 14 continuous days, then
~7 days review, and it cannot be compressed by finishing code. That floor is
recorded in this repo at
[`2026-08-05-google-play-submission-requirements.md`](2026-08-05-google-play-submission-requirements.md)
and in spider-swing's own closed-test runbook, and it appears in **neither** of
the two files a cold session actually opens first.

**What NOT to do.** Do not rewrite the README's body — *What exists*, the
architecture table, the roadmap and the verify commands are accurate and are the
reason the file reads as trustworthy. The defect is four claims and two missing
rows, not the document.

**Acceptance:** a cold session reading `README.md` alone can state that the name
is decided, that a signed build is on Play's internal track, that closed testing
has not started, and that the clock is three weeks minimum.

### 7.2 · `product-forge` — rank 2, and `current-state.md` is the *second* edit

**Do `README.md` first.** Filling the template ledger while the front door still
routes to a retired seat closes this audit's recorded finding and leaves the repo
failing. The README needs its seat-era framing marked as history — *not deleted*,
per the estate's own convention for seat-era docs — and it needs to name
`phone-controller` as what the repo now is. Live inputs, read 2026-08-24:
`products/phone-controller/README.md` (18,456 bytes) and the slice cards through
`.sessions/2026-08-20-phone-controller-slice22-foldables.md`.

**Then `docs/current-state.md`**, whose four sections are all placeholders. The
baseline, in-flight and recently-shipped material exists — it is spread across
those 22 slice cards and the product README, which is exactly why the ledger is
worth having.

**The one thing to check before writing either:** program step **R2** graduates
`phone-controller` to its own repo. If that is close, the honest ledger says so
and says what graduation means for this repo's remaining contents. The keystore
edge is in [`../repos/product-forge/README.md`](../repos/product-forge/README.md).

**Acceptance:** a cold session states that product-forge is the seat-era shell
whose living asset is the phone-controller app, what state that app is in, and
that its next step is R2 graduation — without opening `control/`.

### 7.3 · `estate-backups` — rank 3, one file, no gates

3 blobs total. `README.md` (130 bytes) needs to carry what the two workflow
headers already say well: `dump.yml` = the restore-verified **pre-deletion**
archive of `postgres-botsite` (ran 2026-08-16), `sizing.yml` = read-only catalog
sizing (2026-08-20), both one-shot and both already run; the sealed-box
one-shot-secret pattern that *is* the venue; and the read-only posture.

**The line that prevents a real mistake:** the recurring bot backup is a
**`superbot` workflow**, not this repo. A session that reads *"durable home for
estate data backups"* and nothing else will look for the nightly job here.

### 7.4 · `websites` — rank 4, and it is more than a stamp

`docs/current-state.md` is stamped **`last updated 2026-07-21`** (live read,
2026-08-24) and its header still describes the EAP session-surface wind-down as
upcoming. It therefore predates the entire 2026-08-20/21 keep-bot-only cutover
that § 3 above measures. `UNVERIFIED here:` `docs/PROJECT-CLOSEOUT.md` lists
**review** as one of four Railway services, while
[`../repos/websites/README.md`](../repos/websites/README.md) records it as a
GitHub Pages static export with no Railway service since that cutover — check
the live service list before writing either way, exactly as § 3 did.
