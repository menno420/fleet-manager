I have everything. Writing the rows.

# Provenance rows — the nine archived repositories

**Live verification, all nine, `MEASURED` 2026-09-04** via `GET /repos/menno420/<repo>` and `GET /repos/menno420/<repo>/commits/<default_branch>` over the direct-PAT path (`curl --noproxy '*'`), HTTP 200 on all 18 calls. JSON at `/tmp/claude-0/-home-user-fleet-manager/ba0cfcbc-1bca-5743-a303-812375e61427/scratchpad/eb/archived/<repo>.json` and `<repo>.tip.json`.

**9 of 9 confirm `archived: true`.** The list is not stale. All nine are `private: false`, `default_branch: main`, `has_pages: false`, `open_issues_count: 0`, `forks_count: 0`. Every default-branch tip is the pre-archive notice commit from the R5 run — nothing has moved in 12 days, consistent with read-only.

| repo | archived | tip SHA (main) | tip date | `pushed_at` |
|---|---|---|---|---|
| `Substrate-kit-app` | true | `ffd452451d05dab84d6a21ecc9fe2b1baa3b48ad` | 2026-08-23T07:01:03Z | 2026-08-23T07:01:03Z |
| `codetool-lab-fable5` | true | `e615b375be9240f786e730536af6fb85dee0bc3c` | 2026-08-23T07:02:18Z | 2026-08-23T07:02:20Z |
| `codetool-lab-opus4.8` | true | `59f0b82fef8f2c225e6fa8fd3d1ca3de92dc57aa` | 2026-08-23T07:02:20Z | 2026-08-23T07:02:22Z |
| `codetool-lab-sonnet5` | true | `ef3b60097f6a2bd46dd27794d03fb120c1d6c36a` | 2026-08-23T07:02:15Z | 2026-08-23T07:02:17Z |
| `proxybench` | true | `88d5d1723561f790d0ea1cf9e0857738de5a6b89` | 2026-08-23T07:01:04Z | 2026-08-23T07:01:04Z |
| `superbot-games` | true | `c3b2e83d918958b2455dafd8c4217851763bffbd` | 2026-08-23T07:00:51Z | 2026-08-23T07:00:51Z |
| `superbot-idle` | true | `0062182c28c311c3811a6cea3bd1a6a51fd0fb51` | 2026-08-23T07:01:08Z | 2026-08-23T07:01:08Z |
| `superbot-mineverse` | true | `0bcb864dde06df7347e96c532e480f918bb646de` | 2026-08-23T07:02:59Z | 2026-08-23T07:02:59Z |
| `trading-strategy` | true | `54e1461232de4fcd689975b3c950640b08093cb6` | 2026-08-23T07:01:11Z | 2026-08-23T07:01:12Z |

---

## `Substrate-kit-app`

**What it was.** A one-shot Gemini (AI Studio) experiment, 2026-08-04, untouched since: a "Substrate Kit Dashboard" React frontend over hardcoded demo data, committed on top of a partial `substrate-kit` v1.20.2 snapshot. **It is not the kit** (`MEASURED-PRIOR` 2026-08-22, dispositions § 3: its `README.md` and `docs/PROJECT-CLOSEOUT.md` are byte-identical to `substrate-kit`'s, `current-state.md` differs by 8 lines).

**Why archived.** Frozen, no consumer, no future. Archived on **value** — it is the estate's one piece of evidence of what a single Gemini one-shot produces, which OD-13's multi-provider question cares about — explicitly *not* on a dependency sweep (see the contradiction below).

**The one thing a future session needs.** **Every in-repo surface lies about what this repo is.** The only honest self-descriptions in the tree are `metadata.json` and `package.json`; the archive froze the misidentification permanently, and the correcting notice at the top of the README (landed pre-archive, in `ffd4524`) is the sole above-the-fold text in that tree that names the repo correctly. Read the notice or the two JSON files — never the README body, CONSTITUTION or docs.

## `codetool-lab-fable5` — **envdrift**

**What it was.** A finished, zero-dependency `.env` drift/diff/lint CLI. R3 (2026-08-22) cut it two releases from scratch — it had no release workflow at all until fable5 #20 added one.

**Why archived.** Finished and unmaintained, no owner, no consumer. Archived per the OD-18 table after R3 satisfied the release-first rule.

**The one thing.** **The PyPI name `envdrift` is taken and is not ours** — `pypi.org/pypi/envdrift` is `jainal09/envdrift` v11.0.4, an unrelated tool (`MEASURED-PRIOR` 2026-08-22, HTTP 200). Any record saying PyPI publication is "one owner click away" for this repo is wrong; it would need a new name. The install path that does work is `envdrift @ git+https://github.com/menno420/codetool-lab-fable5` — **`MEASURED` 2026-09-04**, `git ls-remote` against the archived repo returned `e615b375…  HEAD`, real exit 0. Releases live: `v0.2.0` and `v0.1.0`, 2 assets each.

## `codetool-lab-opus4.8` — **mdverify**

**What it was.** A finished CLI that executes the code blocks inside your Markdown so docs cannot rot. Releases `v0.2.0` + `v0.1.0`, 2 assets each, confirmed live 2026-09-04.

**Why archived.** Released, finished, unowned. Its prior *keep-unarchived* verdict was traced and found not to rest on an owner ruling at all.

**The one thing — a trap for anyone re-litigating this.** The "never archive this one" line has **two** discredited justifications on record, and both are already refuted in `ESTATE.md:111`: (a) *"install URLs pin it"* is not a reason — archiving keeps reads and URLs working; (b) *"a standing OWNER ruling (2026-07-10)"* over-reads its source — the owner's actual words, quoted at `docs/planning/2026-07-12-repo-consolidation-plan.md:46`, are **"delete no repos (they are the fleet's memory)"**, about *deletion*, and since amended by OD-3 (2026-08-08). The keep-unarchived verdict was that plan's own reconciliation (`:92`), carried into `fleet-triage.md:61` via INC-03. Do not resurrect either argument. Install: `pipx install git+https://github.com/menno420/codetool-lab-opus4.8` — `git ls-remote` → `59f0b82f… HEAD`, exit 0, `MEASURED` 2026-09-04.

## `codetool-lab-sonnet5` — **cfgdiff**

**What it was.** A finished cross-format semantic config diff/convert CLI, `v0.1.1` released 2026-08-22 by its own `release.yml`.

**Why archived.** Same class: finished, unmaintained, released first.

**The one thing.** **Its `publish-pypi` job fails on every run** (no trusted publisher configured), so **the workflow run reads red while the Release itself is intact** — a future session auditing CI will see a red release run and must not conclude the release failed. `pypi.org/pypi/cfgdiff` is 404, so the name is free if publishing is ever wanted. This is also the repo that carries the estate's **post-archive install oracle**: `MEASURED-PRIOR` 2026-08-23, `pip install "git+https://github.com/menno420/codetool-lab-sonnet5"` into a clean venv succeeded with real exit 0 against the *already-archived* repo, resolved to default-branch HEAD `ef3b600`, and `cfgdiff --version` printed `cfgdiff 0.1.1`. Re-confirmed reachable `MEASURED` 2026-09-04 (`git ls-remote` → `ef3b6009… HEAD`, exit 0). One caveat carried from `ESTATE.md`: a bare `git+https://…` URL with no `@ref` resolves to branch HEAD, so **the tagged releases sit beside the documented install command, not on it** (`REASONED` from pip's ref handling, not tested).

## `proxybench`

**What it was.** A single-file, dependency-free, stdlib-only Python 3 proxy-provider benchmarking harness — built mostly as a joke to answer one vendor's sales claims, and it did that. 8 KB.

**Why archived.** OD-12 parked it; one file, zero dependents. Its one stray artifact — issue #1, `"probe issue (auto-closed)"`, body the single line `capability probe` — was read and closed `not_planned` before the archive; `open_issues_count` is now 0, confirmed 2026-09-04.

**The one thing.** This repo is the estate's **write-side archive oracle**: `MEASURED-PRIOR` 2026-08-23, a contents `PUT` against archived `proxybench` returned **403 — "Repository was archived so is read-only."** while a read of the same file kept working. If a successor session ever needs to demonstrate or re-verify what archiving actually blocks, this is the cheap, consequence-free target.

## `superbot-games`

**What it was.** SuperBot's game world — mining, fishing, D&D, exploration — as pure-stdlib Python. 2.6 MB, the largest of the SuperBot-World trio.

**Why archived.** The successor plan (OD-16 / the GCB plan) explicitly rejects its casino/economy/game-content scope; it has no live consumer, and its adapters into `superbot-next` were never built (the R1 drift).

**The one thing.** **Its README claims plugin-shipping and the tree has no packaging** — the known R1 drift. A future session reading the README will believe it can install a plugin from here; it cannot. Second, this is **the only one of the nine that is in GitHub's `search/code` index** (`repo:menno420/superbot-games mining` → 292 hits both before and after the archive, `MEASURED-PRIOR` 2026-08-23) — so it is the control that proves archiving does not affect code-search coverage, and simultaneously the reason a sweep that finds nothing in the other eight has found nothing at all (see the contradiction section).

## `superbot-idle`

**What it was.** An idle-game engine plus 21 data-only theme packs for SuperBot. Kit v1.16.0.

**Why archived.** A parked engine whose only consumer (`superbot-next`) is itself parked. It was also the estate's clearest parked-but-noisy case: `host-main-advisory` had fired on 40 consecutive days with no gap, 2026-07-14 → 2026-08-22, of which 32 fell *after* the repo's last commit.

**The one thing — and it settles a question the estate left open.** `superbot-idle-plugin` is pinned in `superbot-next/plugins.lock.json` by `manifest_hash: sha256:48bf953dc6a91962e4d5841f85435b20eafa7f614f6916be2320be2c8646fe1c` (`MEASURED` 2026-09-04, read live). **That pin is a hash comparison, not a fetch, and `superbot-next` vendors its own copy in-tree** at `examples/superbot-idle-plugin/` (contains `README.md`, `idle_engine/`, `pyproject.toml`, `superbot_idle_plugin/` — `MEASURED` 2026-09-04 via the contents API). So the pin survives the archive intact and the host never reaches this repo.

**Additionally, `MEASURED` 2026-09-04 — the cron question is now answered, and the answer is the opposite of what the API flag suggests.** `GET /repos/menno420/superbot-idle/actions/runs?event=schedule` returns `total_count: 41`, newest **`2026-08-23T05:42:49Z`** — the pre-archive baseline the dispositions doc recorded. **Zero scheduled runs in the 12 days since**, against a cron that had not missed a single day in the preceding 41. Meanwhile all six workflows still read `state: active`. The dispositions doc set the bar for a negative at "several consecutive missed windows (2–3 days), **or** an unarchived control"; **both halves are now met** — 12 missed windows, and the control is live (`fleet-manager` scheduled runs firing through `2026-09-04T11:42:13Z`; `superbot`'s daily Postgres backup through 2026-09-01). So: **archiving stops scheduled Actions from being dispatched while leaving `state: active` in the API.** The estate's archive list *was* also its cron cleanup, and `docs/planning/2026-08-22-repo-dispositions.md` § 4's "STILL OPEN after R5" block is now answerable and should be closed.

## `superbot-mineverse`

**What it was.** A staged browser dashboard over SuperBot's mining economy. Off Railway since 2026-08-20/21 — service and project both deleted.

**Why archived.** The web host is gone and the bot-side WRITE PR (sb #2061) closed unmerged, so its own go-live checklist is moot. Its remaining value is documentary, which archiving preserves.

**The one thing.** **Its `docs/PROJECT-CLOSEOUT.md` is the SuperBot-World fleet MASTER** — the `superbot-games` and `superbot-idle` closeouts route their fleet-wide threads *here*, so a successor investigating any of the three lands in this archived repo by design. And the trap: `current-state.md:53-55` told the successor to "rebind-then-delete" a named trigger, which `decision 15 in `docs/decisions.md`` forbids outright, against a target that no longer exists (`trig_01XJJ88…`, "SuperBot World failsafe wake", cron `15 1-23/2 * * *` — `MEASURED-PRIOR` 2026-08-22: the account held three Routines and none was it). **This was corrected before the archive** — mineverse #145, merged `fc7c349`, struck through in place with the historical text surviving beside the correction — and both siblings were searched for the same instruction with zero hits. So the trap is defused, but a future reader will still meet the struck-through original text in the MASTER and should recognise it as corrected history, not an instruction.

## `trading-strategy`

**What it was.** A closed quant research lab: 11 rounds, 5,940 configs, **0 promoted**, holdout SPENT. 8.2 MB — the largest of the nine.

**Why archived.** The research concluded. The null result *is* the deliverable; archiving preserves it readable while ending the pretence that a session might pick it up.

**The one thing.** **The holdout is spent** — that is the fact that makes this repo unrevivable rather than merely parked. Any successor tempted to "just run one more round" would be evaluating against a holdout already burned across 11 rounds, so a positive result from it would be meaningless. The paper-0001 lane is WATCH/FLAT. Treat the archive as a scientific record, not a paused project.

---

# Is anything archived still depended on by something live?

**None.** No archived repository should be anything other than archive-only in the successor.

**What I checked, `MEASURED` 2026-09-04 unless tagged otherwise:**

1. **The one real pin.** `superbot-next/plugins.lock.json`, read live: pins `superbot-idle-plugin` and `superbot-plugin-hello` by `manifest_hash` (`sha256:48bf953d…` / `sha256:ff75b9eb…`). A hash is a verification value, not a fetchable ref. Confirmed the host vendors both in-tree: `GET /repos/menno420/superbot-next/contents/examples` → `['superbot-idle-plugin', 'superbot-plugin-hello']`, and the idle one contains a full package (`pyproject.toml`, `superbot_idle_plugin/`, `idle_engine/`). Corroborated `MEASURED-PRIOR` 2026-08-22 by the host's own boot proof, `superbot-next/tests/unit/app/test_plugin_boot_real_exemplar.py`, which sets `_EXEMPLAR_ROOT = _REPO_ROOT / "examples" / "superbot-plugin-hello"` because "the exemplars live in-tree but are NOT installed dists". **And `superbot-next` is not live anyway** — parked, `archived: false`, `pushed_at: 2026-08-13T15:21:12Z`, read live.
2. **The live successor.** `spider-bot` exists and is live (HTTP 200). Grepped all four files in its `docs/` — `extraction-ledger.md`, `superbot-reuse-map.md`, `product-shape.md`, `plan-onboarding-ux-and-site.md` — for all nine archived names plus `codetool`/`mineverse`: **0 hits in 4 of 4 files.** Its documented donors are `superbot` and `superbot-next`, both unarchived.
3. **Live scheduled workloads.** `superbot-idle` was the only archived repo running a cron. It has dispatched nothing since `2026-08-23T05:42:49Z` (12 days), against live controls still firing. Nothing live is waiting on its output.
4. **Serving surfaces.** All nine read `has_pages: false` — the one Pages-serving archive-bound repo, `product-forge`, was gated on R2 and is not in this set. `superbot-mineverse`'s Railway service and project were deleted 2026-08-20/21 (`MEASURED-PRIOR`).
5. **Fork/issue exposure.** All nine: `forks_count: 0`, `open_issues_count: 0` — no third party carrying a branch, no open thread expecting a write.
6. **Local doc references.** Grepped `/home/user/fleet-manager/docs/repos/` for all nine names: 4 hits, all *descriptive records* — `substrate-kit/README.md:207-211` (kit-version rows and the note that `docs/fleet-repos.txt` omits `superbot-idle` from its scan roster, i.e. the kit registry cannot see it) and `superbot-next/README.md:74` (the lockfile pin already resolved above). No build input, no fetch.

**The near-miss worth naming explicitly:** `superbot-idle` is the only one that ever had a live-looking claim on it, and it fails on two independent grounds — the pin is a hash, and the pinning repo is itself parked. If either had gone the other way this answer would name it.

**One honest edge, and it is load-bearing.** The only method that could give an *account-wide completeness* answer — `search/code?q=…+user:menno420` — **does not cover this account.** `MEASURED-PRIOR` 2026-08-23, all 26 repos probed one query each with a term verified present in that repo's own tree: **7 of 26 indexed, 19 not** — and **8 of the 9 archived here are among the 19 unindexed** (`superbot-games`, at 292 hits, is the sole indexed one). A zero from an unindexed repo is indistinguishable from a genuine absence. So my "none" rests on the six targeted checks above — the pin read at its source, the live successor's own docs, the cron, the serving surfaces, forks/issues, and the hub's records — **not** on a code-search sweep. A consumer outside GitHub entirely would appear in none of these. To make this a completeness claim, clone-and-grep the 14 keeps; that has not been run and I am not claiming it has.

## Contradictions found

- **`UNRESOLVED` → now resolvable, one side wins.** `docs/planning/2026-08-22-repo-dispositions.md` § 4 records the archiving-stops-crons question as `UNVERIFIED` and "STILL OPEN after R5", noting the workflows still read `state: active` immediately post-archive as evidence *against*. My measurement 12 days later (0 scheduled runs vs. a 41-day unbroken daily streak, with live unarchived controls firing today) meets that document's own stated bar for a negative. **Not a live contradiction — a question whose answer arrived.** The doc should be updated; I have not edited it.
- **`Substrate-kit-app`'s dependency claim, recorded on both sides.** Dispositions § 3 first states *"5 hits, all in `fleet-manager`… nothing in the other 25 repositories references it"* (`MEASURED` 2026-08-22), then strikes it through and corrects it 2026-08-23 as *"not supported by the method used"*. `ESTATE.md` carries both halves too — the § *"search/code does NOT cover this account"* warning invalidates the claim, while a later paragraph (`ESTATE.md:255`, under *Scope of this check*) still presents the same 5-hit sweep as an `UPDATE` that *"widens the check from 4 repos to 26 and removes the stated blocker on the deletion question"*. **That paragraph is stale and contradicts the warning 40 lines above it in the same file.** Both are in the live tree today. The disposition is unaffected either way (archived on value, not on dependencies), but a future deletion call must not read `ESTATE.md:255` without `ESTATE.md`'s § `search/code` warning.
- **`codetool-lab-opus4.8`'s keep-unarchived verdict** had two successive justifications on record, both since traced and refuted in place (see its row). Recorded as resolved history, not an open conflict.
