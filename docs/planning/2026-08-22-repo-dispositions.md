# Repo dispositions — the whole estate, one verdict each

> **Status:** `plan` · 2026-08-22 · **OD-18's deliverable**
>
> **What this is:** the finalized keep / archive / delete call for **all 26
> repositories the account holds**, plus — for every keep — whether the way
> forward is **reworking** what exists or **starting fresh**. One stated reason
> per row, so a row can be disagreed with on its own.
>
> **Canonical for:** the recommendation. **Not canonical for** any repo's
> internal state — each row's reason is sourced from that repo's own
> `current-state.md` / `PROJECT-CLOSEOUT.md` and from live API reads on
> 2026-08-22, and the repo always wins over the row.
>
> **Nothing here has been executed.** No repository was archived, deleted,
> renamed or modified by this document. Execution is program step **R5** and
> waits on the owner.
>
> Certainty tags per [`../findings/2026-08-05-foundation-continuation.md`](../findings/2026-08-05-foundation-continuation.md).

## 1 · The answer

**Keep 14 · archive 12 · delete 0.** The active estate goes from 26 repositories
to 14, and the set that is unconditionally *worked in* is **7** — five of the
other keeps are kept because the owner said so or because one letter unblocks
them.

**And the start-fresh axis has almost no takers.** Of the 14 keeps, **13 are
rework**; the fourteenth is `superbot`, which is neither — it stays frozen and
maintained while its *successor* starts fresh. That is not a dodge, it is the
finding: OD-16's grounds for starting
the Discord bot fresh — live production coupling, accidental product scope, and
parity that was never porting — are properties of *the bot*, and no other repo
in the estate carries all three. Two things in the estate genuinely start over,
and both were already decided:

| kind of "fresh" | the one case | status |
|---|---|---|
| **fresh code** — throw the codebase away, rebuild from patterns | the Discord bot | already decided, OD-16 / [the GCB plan](2026-08-21-game-community-bot/README.md) |
| **fresh home** — working code, clean repository, history carried | `phone-controller` out of `product-forge` | already planned, program step **R2** |

Those are different questions and the table keeps them apart. Everything else is
reworked in place.

`MEASURED` 2026-08-22, live `GET /user/repos`: **26 repositories, zero
archived** — the archive step OD-3 has described since 2026-07-26 has still
never executed on anything. All 26 names reconcile exactly against
[`../ESTATE.md`](../ESTATE.md) (`scripts/check_estate_index.py` → 0 findings).

## 2 · The table

### Keep — active, work happens here (7)

| repo | rework or fresh | why this verdict |
|---|---|---|
| `fleet-manager` | **rework** | The hub and records home; OD-17's cut lands *here* more than anywhere, and its boot budget is already at 7000/7000 — so the rework is trimming RECORD-tier bulk off the read path, not rebuilding a repo whose identity is its history. |
| `spider-swing` | **rework** | The owner's named priority (OD-15) and the only work in the estate with a clock — a signed build sits on Play's internal testing track; starting fresh would discard a signed release lineage to gain nothing. |
| `couch-legend` | **rework** | Active, live on Pages, kit-seeded 2026-08-21 — and its mechanics base was *already* reconstructed clean on 2026-08-20, so the fresh-start question was asked and spent four days before OD-18. |
| `websites` | **rework** | Serves the bot's live public surfaces; the keep-bot-only cutover (2026-08-20/21) already performed the narrowing a fresh start would buy, by rework, and it worked. |
| `superbot` | **fresh successor, this repo unchanged** | Must stay writable: the LIVE Railway worker deploys from it, and a security patch needs a merge an archived repo would block. Its replacement is a clean repo (OD-16); this one is kept as live host and behavior oracle and is never reworked into the successor. |
| `substrate-kit` | **rework** | The method kit — 27 releases, and the source of the one local gate (`check --strict`) its adopters run, this repo included. Infrastructure, not a candidate. |
| `estate-backups` | **rework** | 5 KB private Actions venue that is the only path from a container to Railway-Postgres; kept as a *capability*, and its dormancy between owner asks is the design, not decay. |

### Keep — standing assets by directive (2)

| repo | rework or fresh | why this verdict |
|---|---|---|
| `idea-engine` | **rework** | OD-4 names it a standing asset, OD-10 makes it on-demand; the 566-file idea corpus is the value and program step R6 (make it browsable) is exactly the rework. |
| `sim-lab` | **rework** — *scope question is his* | Same OD-4 directive, but the role has narrowed: the 4-gate *method* now runs inside target repos (couch-legend did this), leaving this repo a `harness/` library. Keeping it is right; whether it still needs its own repo is a question for him, not a disposition I should take. |

### Keep — the owner's call, not mine (5)

| repo | rework or fresh | why this is his |
|---|---|---|
| `venture-lab` | **rework** | OD-11 reserves it to him personally — *"let it sit"*, he works the sellable-products angle himself. 12 finished books and 19 ready SKUs are finished goods whose value sits outside the repo, so nothing here expires. |
| `shiftlife` | **rework** | OD-15 says not active, but it is a half-built product for a real household need, not a spent experiment. If he resumes it, the 27/27-green domain engine makes rework strictly cheaper than fresh; if he does not, it is archivable — and only he knows which. |
| `gba-homebrew` | **rework** | One letter (`OQ-GBA-NEXT-PICKS`) unblocks a released engine plus four titles. Archiving before he answers would seal work he asked to continue. |
| `pokemon-mod-lab` | **rework** | One letter (`OQ-PML-EMERALD-LETTER`) unblocks it; 18 toggles, byte-identical-when-off, is finished working work waiting on a single answer. |
| `curious-research` | **rework** | His own words park it — *"gets a new mission later."* That is a keep with a stated future, not a repo awaiting a disposition. |

### Archive (12)

Reversible, blocks writes only, keeps every read path and install URL working.

| repo | why archive |
|---|---|
| `superbot-next` | OD-16 already declined it as the successor's base. It donates architecture by being **read**, and archiving blocks only writes — so its donor role survives the archive intact. Sequence it after GCB-1 so the patterns are not sealed mid-harvest. |
| `superbot-games` | The successor plan explicitly rejects its casino/economy/game-content scope; it claims plugin-shipping and has no packaging (the R1 drift), and it has no live consumer. |
| `superbot-idle` | A parked idle engine whose only consumer is a parked repo. Pinned in `superbot-next/plugins.lock.json` by `manifest_hash` — `sha256:48bf953d…`, read directly — and a hash is a verification value, not a fetch, so the pin survives. It is also the estate's clearest case of parked-but-noisy: `MEASURED` 2026-08-22 over the workflow's **complete** scheduled-run history, not a sample — `host-main-advisory` has **40 scheduled runs across 40 distinct days with no gap**, 2026-07-14 → 2026-08-22, of which **32 consecutive days fall after the repo's last commit** (2026-07-21). (An earlier draft said *1,185 runs*; that is the repo's all-workflow total, not this cron's.) |
| `superbot-mineverse` | Off Railway since 2026-08-20/21, service and project deleted. Its remaining value is being the SuperBot-World MASTER closeout, which archiving keeps readable. **One write first** — see § 4. |
| `superbot-plugin-hello` | ESTATE.md's *"never archive"* does not hold, and the reason is stronger than the lockfile: **`superbot-next` carries its own copy of the plugin in-tree** at `examples/superbot-plugin-hello/` (`pyproject.toml`, `manifest.py`, `superbot_plugin_hello/__init__.py` — `MEASURED` 2026-08-22 by code search inside that repo). The host resolves an *installed distribution* via its `sb.plugins` entry point and checks the `manifest_hash` pin against that manifest; it never reaches this standalone repo. So this is a published exemplar, not a build input, and archiving it cannot affect the host's boot. Archive it with `superbot-next`, as one pair. |
| `trading-strategy` | The research concluded: 11 rounds, 5,940 configs, **0 promoted**, holdout SPENT. The null result *is* the deliverable, and archiving preserves it readable while ending the pretence that a session might pick it up. |
| `codetool-lab-sonnet5` (cfgdiff) | R3 done — v0.1.1 released. A finished CLI whose documented `pipx install git+https://…` path is unaffected by archiving. **One write first.** |
| `codetool-lab-fable5` (envdrift) | R3 done — v0.1.0 + v0.2.0 released. Same install path; and the PyPI name `envdrift` belongs to a different project, so there is no publishing future being closed off. **One write first.** |
| `codetool-lab-opus4.8` (mdverify) | The keep-unarchived verdict traces to a 2026-07-12 **plan reconciliation**, not an owner ruling, and its stated reason (live install URLs) is not a reason — archiving keeps those resolving. Released, finished, unowned by any current task. **One write first.** |
| `Substrate-kit-app` | **The wider dependency check has now run** (§ 3): account-wide code search returns 5 references, all of them in `fleet-manager`, none in any other repository. Archive rather than delete, because its residual value is real — it is the estate's evidence of what one Gemini one-shot produced, which the multi-provider question (OD-13) cares about. |
| `proxybench` | OD-12 parks it: built mostly as a joke, answering one vendor's sales claims, and it did that. One file, zero dependents. One stray probe issue to close first. |
| `product-forge` | **After R2 only.** Its own `docs/current-state.md` is still the unfilled kit template — every content section is the generated placeholder, `MEASURED` — so the shell is empty. The living asset is `phone-controller` (19 releases through v0.22.0, signed), which R2 graduates by subtree split with history carried. The asset is reworked in a fresh home; the emptied shell is what gets archived. **Check its Pages site before sealing it** — `MEASURED` 2026-08-22, it is the only archive-bound repo serving Pages (<https://menno420.github.io/product-forge/>, HTTP 200, source `main`, `build_type: workflow`), so it is where the open Actions question below actually bites. |

### Delete (0)

**No row meets OD-3's amended bar.** That bar is *"has it served its purpose
and can it still be of value"* — a conjunction, and every archive candidate
above fails its second half: each is still of value as a readable record, an
install path, or evidence. Deletion is also the estate's only irreversible
disposition, and archiving is documented as undoable, so nothing is gained by
taking the one-way door first. **This is a recommendation to defer, not a
finding that deletion is wrong** — after these twelve archives have sat for a
while, `Substrate-kit-app` and `proxybench` are the two whose second half is
weakest and the two worth revisiting.

## 3 · The checks that changed a row

Two rows in `ESTATE.md` rested on claims that had never been tested. Both were
tested for this pass, and both moved.

- **`Substrate-kit-app`'s dependency check.** The prior note recommended
  deletion on a four-repo grep, then withdrew it as too narrow. `MEASURED`
  2026-08-22, account-wide `search/code?q=Substrate-kit-app+user:menno420`:
  **5 hits, all in `fleet-manager`** — this repo's own index and doc-routes.
  Nothing in the other 25 repositories references it. *Honest edge:* code search
  indexes default branches and text; it would not see a consumer outside GitHub.
- **`superbot-plugin-hello`'s "never archive".** Two reads, and the second is
  the deciding one. `superbot-next/plugins.lock.json` pins both plugins by
  `manifest_hash` (`sha256:…`) rather than by a fetchable ref — which shows the
  lockfile does not *point* at the repo, but says nothing yet about how the host
  actually resolves the plugin. That was checked separately, and it is the
  answer: **`superbot-next` vendors the plugin in-tree** at
  `examples/superbot-plugin-hello/`, with its own `pyproject.toml` and
  `manifest.py`. Resolution runs through an installed distribution's
  `sb.plugins` entry point against that in-tree source, so the standalone repo
  is an exemplar publication, not a build input. The prohibition rests on a
  dependency that is not there. *Not checked, and not needed:* whether the
  vendored manifest still hashes to the pinned value — archiving changes
  neither side of that comparison.

Also measured, and it settles how much of `Substrate-kit-app` is really its own:
its `README.md` and `docs/PROJECT-CLOSEOUT.md` are **byte-identical** to
`substrate-kit`'s, and its `current-state.md` differs by 8 lines. The
misidentification the index warns about is total, not partial.

## 4 · Writes must happen before the archive

GitHub's own documentation says it, sourced 2026-08-22 from
[archiving-repositories](https://docs.github.com/en/repositories/archiving-a-github-repository/archiving-repositories):
*"We recommend that you close all issues and pull requests, as well as update
the README file and description, before you archive a repository."*

**Read that quote for exactly what it covers**, because the list below is wider
than it. GitHub recommends two things: close issues/PRs, and update the
README/description — items 3 and 4. Items 1 and 2 are **this estate's
extension**, derived from the read-only property rather than recommended by
GitHub, which says nothing about stale in-repo instructions, batons or triggers.

**And this is sequencing, not a deadline.** An earlier draft of this section said
a needed write has *"exactly one window"* — which contradicts this document's own
argument two sections up, that archiving is reversible. A write discovered after
R5 costs an unarchive → write → re-archive cycle, which is cheap and undramatic.
So the list below is the order that avoids that cycle, **not a precondition that
should block the archive**: if item 2 is not written, archive anyway and fix it
later. The one item worth actually holding for is item 1, because it seals a
wrong instruction into a document other repos route to.

This is R3's lesson generalized. R3 ran first because releases must be cut
before the archive; the same shape applies to text:

1. **`superbot-mineverse`** — its `current-state.md:53-55` tells the successor
   to *"rebind-then-delete"* a named trigger, which
   [this estate's trigger decision](../decisions.md) forbids outright: a
   misbehaving trigger is **disabled** via `update_trigger`, never deleted.
   Archiving would seal that instruction, read-only, into the family's MASTER
   closeout. It is wrong twice over: `MEASURED` 2026-08-22, the trigger it names
   (`trig_01XJJ88…`, *"SuperBot World failsafe wake"*, cron `15 1-23/2 * * *`)
   **no longer exists** — the account holds three Routines and none is it, and a
   cron Routine is not one of the kinds a default listing hides. So the baton
   directs a forbidden action against a vanished target. Correct it first;
   nothing was disabled or deleted to establish this.
2. **The three code labs** — one line in each README saying the tool is
   finished and unmaintained. A release cut days before an archive over-signals
   support; `ESTATE.md` already asks for this and it has not been written.
3. **`proxybench`** — close issue #1 (`"probe issue (auto-closed)"`, still open,
   a capability-probe artifact).
4. **All twelve** — README/description line per GitHub's recommendation above.

`UNVERIFIED`, and this pass made it worth answering rather than noting:
**whether archiving stops scheduled Actions.** The archiving docs enumerate what
becomes read-only and say nothing about workflow runs, so the appealing claim
that archiving silences `superbot-idle`'s daily cron is *not* established — and
that cron is measured still firing daily, a month after the repo's last commit.
If archiving does stop it, the archive list is also the estate's cron cleanup;
if it does not, that is separate work. Cheap to settle: archive one repo with a
cron and look at the next scheduled window.

The same unknown has one place where it could cost something rather than save
it. `MEASURED` 2026-08-22: exactly one archive-bound repo publishes GitHub
Pages — `product-forge`, live and returning HTTP 200, with `build_type:
workflow`. An already-published site should keep serving, since serving is a
read; a **rebuild** is not, and the docs do not say. So `product-forge` is the
one row where the archive should be done last and the site re-checked after,
which its own R2 gate already sequences. Every other archive-bound repo has
`has_pages: false`, checked, so this is a single row's caveat rather than a
class of risk.

## 5 · What is his, and what he actually has to answer

Four keeps above are marked his (`venture-lab`, `shiftlife`, `gba-homebrew`,
`pokemon-mod-lab`), plus `curious-research` which his own words already
answered. Those are not guesses deferred — they are rows where the deciding
input is his intent, which no repo state can supply.

Reduced to what he must actually say, it is **one approval and two letters**:

- **The archive list** — the twelve in § 2. One yes covers all of them; the
  sequencing in § 4 is agent work.
- **`OQ-GBA-NEXT-PICKS`** and **`OQ-PML-EMERALD-LETTER`** — one letter each,
  each unblocking a whole repo. Until they are answered, both stay keeps.

Not required from him, and worth saying so: the seven active keeps and the two
standing assets need no decision at all.

## 6 · What this does not settle

- **`OQ-FM-D2-TARGET`** is not answered by this table. D2 is a per-repo *truth
  pass*; this is a disposition pass. What this does supply is the order — D2
  should run over the 7 active keeps and skip the 12 archive-bound, which is
  most of the reason the question felt hard.
- **`superbot`'s 8 open dependabot PRs** stay out of scope — it is a keep, so no
  archive sequencing applies. But the usual framing (*"merging them restarts the
  live bot, so batch them into a window"*) is **too broad**, and the difference
  is worth carrying. `MEASURED` 2026-08-22, the files each PR touches, against
  the W1 watch filter (`disbot/**` + root build inputs; workflow- and
  runbook-only merges deploy SKIPPED):

  Method, stated because the two halves have different provenance: the file
  lists are **mine, measured** — `GET /repos/menno420/superbot/pulls/{n}/files`
  over the direct-PAT path for each of the eight, reading `filename`. The
  **filter semantics are inherited**, not re-measured: they come from
  [`../repos/superbot/README.md`](../repos/superbot/README.md), which records
  them as live-tested on sb #2446. They are not readable from the tree — the
  repo root has a `Procfile` and no `railway.json`/`railway.toml`, so the watch
  filter is a Railway **service setting**, and confirming it first-hand would
  mean reading the live service, which the hard rail puts out of scope here.
  What the tree does settle is which files count as root build inputs:
  `pyproject.toml`, `requirements.txt`, `requirements-dev.txt` (root listing,
  measured) — which is why #2449 is treated as a restart.

  | PRs | touches | effect on the live worker |
  |---|---|---|
  | #2398 #2399 #2400 #2401 | root `requirements.txt` | **restart** |
  | #2449 | root `requirements-dev.txt` + `botsite/` + `dashboard/` | **treat as a restart** — a root build input, though a dev-only one |
  | #2448 #2447 #2402 | `botsite/` only · `dashboard/` only · `.github/workflows/codeql.yml` only | no restart (SKIPPED) |

  **None of the eight touches `disbot/**`.** So three of them can be merged at
  any time with no live effect, and only five need the deliberate window. That
  is a smaller owner ask than the one on record.
- **Nothing here is executed.** R5 executes it, after his yes.
