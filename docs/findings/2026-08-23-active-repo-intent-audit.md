# The active-repo intent audit — can a cold session tell what each repo is for?

> **Status:** `audit` · 2026-08-23 · owner-asked, mid-session:
> *"look at all the currently active repos and find out if each one has clear
> goals and a well explained intent, so any fresh session would know what to do
> with it."*
>
> **What this is:** D2's acceptance test — *a cold session states the repo's
> purpose, live state and next step from ≤3 files* — run as a **sweep** across
> all 17 unarchived repositories instead of one repo per session. It exists
> because `OQ-FM-D2-TARGET` has been picking D2's next repo by guess; this
> replaces the guess with a ranked list of which repos actually fail.
>
> Certainty tags per [`2026-08-05-foundation-continuation.md`](2026-08-05-foundation-continuation.md).

## 1 · The verdicts

**7 pass · 5 unrated · 1 stale · 3 fail · 1 hub.** Judged from each repo's own
declared entry point.

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
3. **`estate-backups`** — a two-line README and no other entry point.
   Everything real about it lives in the hub. **Open.**

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
  *dormant* service would still be listed: same two, both `SUCCESS`. So the
  absence rules out dormant-or-unlinked, not merely not-running. The live
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

## 6 · The order this implies for D2

1. ~~`idea-engine`~~ ✅ · 2. ~~`sim-lab`~~ ✅ · 3. **`product-forge`** (needed
before its R2 graduation anyway) · 4. **`estate-backups`** · 5. the date stamp
on `websites`.

**Method limit, stated:** judged from each repo's declared entry point plus the
three closeouts opened. The five unrated repos could rate as passes if their
pointer targets carry what their status docs do not — that is one read each and
was not done here.
