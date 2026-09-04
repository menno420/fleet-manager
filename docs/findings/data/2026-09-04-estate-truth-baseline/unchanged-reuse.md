All five tips re-verified; artifacts under `/tmp/claude-0/-home-user-fleet-manager/ba0cfcbc-1bca-5743-a303-812375e61427/scratchpad/eb/reuse/` (`tip-verify.tsv`, `<repo>.branch.json`, `<repo>.repo.json`).

---

## Method note (applies to all five)

`MEASURED` 2026-09-04T12:50Z, one `GET /repos/menno420/<repo>/branches/main` per repo over direct-PAT egress (`curl --noproxy '*'`), plus one `GET /repos/menno420/<repo>` for archived/private/default-branch/`pushed_at`. **5 of 5** live tips are byte-identical to the pinned SHAs. So the zero-movement fact is confirmed independently of `delta.py` for the whole population I was given.

The successor's per-repo questions are pre-registered, not invented by me — `docs/findings/data/2026-09-04-estate-truth-baseline/cold-session-rubric.md` states them as the shape Q1/Q2/Q3/Q7 test: *"What is `spider-swing` actually for? … The product in plain language, and its state word"*, *"Is `superbot-next` active, paused, archived or superseded? … The state word **and** what supersedes it"*, *"Where does current product truth live for `couch-legend`? … A path **inside that repository**, not a hub document"*, *"A fresh agent must work on `creator-kit`. What does it read first, and what must it NOT trust?"* That is the bar I judge each prior-evidence document against.

Four of the five rows are anchored to the **same** document — `docs/planning/2026-08-22-repo-dispositions.md` — so its self-declared scope governs four verdicts at once. It states its own scope verbatim in its header:

> **What this is:** the finalized keep / archive / delete call for **all 26 repositories the account holds**, plus — for every keep — whether the way forward is **reworking** what exists or **starting fresh**. One stated reason per row, so a row can be disagreed with on its own.
>
> **Canonical for:** the recommendation. **Not canonical for** any repo's internal state — each row's reason is sourced from that repo's own `current-state.md` / `PROJECT-CLOSEOUT.md` and from live API reads on 2026-08-22, and the repo always wins over the row.

`MEASURED` 2026-09-04 (`ls docs/repos/`): **4 of these 5** repositories — `curious-research`, `gba-homebrew`, `pokemon-mod-lab`, `superbot-plugin-hello` — have **no Layer-2 folder** under `docs/repos/` (present: `couch-legend`, `estate-backups`, `product-forge`, `spider-bot`, `spider-swing`, `substrate-kit`, `superbot`, `superbot-next`, `venture-lab`, `websites` — 10 of 28). `venture-lab` is the only one of my five that has one, and it is the only one of my five anchored to it.

`docs/ESTATE.md` **does** carry a purpose line, a state word and a canonical entry for all four of the folderless repos. It is **not** the pinned prior evidence for any of these rows, and the rubric excludes it from the cold-session artifact set explicitly: *"`docs/findings/2026-09-04-estate-truth-baseline.md`, `docs/planning/2026-09-04-estate-seed-manifest.csv`, and `docs/findings/data/2026-09-04-estate-truth-baseline/` … **Nothing else** — no `ESTATE.md`, no `docs/repos/`, no boot file, no consolidation program."* So ESTATE.md's coverage cannot rescue a `NOT_REUSABLE` verdict here; it can only tell the successor where the missing content would have to be re-derived from. `REASONED`, and flagged as the single most useful follow-on below.

---

## `curious-research`

**Zero movement, re-verified.** `MEASURED` 2026-09-04T12:50Z: live `main` tip `353cb4d035f48762924511a03a5d61e2f94c53d9`, committed `2026-08-07T19:02:31Z`, message `Maak de repository zichtbaar in de AI-onboarding (#78)`. Pinned SHA `353cb4d035f48762924511a03a5d61e2f94c53d9` — **identical**. Live metadata: `archived=False`, `private=False`, `default_branch=main`, `pushed_at=2026-08-07T19:02:33Z` (2 s after the commit, so no post-tip pushes on any ref).

**What the prior evidence establishes**, verbatim — this is the entire row, § 2 *Keep — the owner's call, not mine (5)*:

> | `curious-research` | **rework** | His own words park it — *"gets a new mission later."* That is a keep with a stated future, not a repo awaiting a disposition. |

and in § 5:

> Four keeps above are marked his (`venture-lab`, `shiftlife`, `gba-homebrew`, `pokemon-mod-lab`), plus `curious-research` which his own words already answered. Those are not guesses deferred — they are rows where the deciding input is his intent, which no repo state can supply.

So it establishes: **disposition = keep**, **axis = rework not fresh**, **grounds = owner intent, quoted** (`OWNER`, *"gets a new mission later"*), and that no further owner decision is owed on it (*"Not required from him"* covers only the seven active keeps and two standing assets, so this row is instead covered by *"his own words already answered"*).

**What it explicitly does NOT establish.** It does not say what `curious-research` **is** — no product, no domain, no one-line purpose anywhere in the document. It gives no **state word** in the rubric's vocabulary (active/paused/archived/superseded); *"parked"* appears only inside the owner quote as a verb of the author's, and *"a keep with a stated future"* is a disposition, not a state. It names **no path inside the repository** — the words `README`, `current-state` and `PROJECT-CLOSEOUT` never occur in this row, and the document's own header disclaims exactly this: *"**Not canonical for** any repo's internal state."* It names nothing a fresh agent must **not** trust. The document did not read this repository's tree for this row at all: its stated basis is *"his own words."*

**Verdict: NOT_REUSABLE** for the successor's routing questions. It cannot answer *what is this repo for*, *what is its state word*, *where does its truth live*, or *what must a fresh agent not trust* — and zero movement of the tree does not change that, because the evidence never asked those questions. **REUSABLE, narrowly**, for exactly one question: *what is this repository's disposition and on whose authority* — keep/rework, on the owner's quoted words. Second-order caveat, `REASONED`: the row's basis is **owner intent**, which is not a property of the tree; zero commits is therefore not even the right instrument for its freshness. *"Gets a new mission later"* is by construction a claim that expires the day he gives it one, with no commit required.

---

## `gba-homebrew`

**Zero movement, re-verified.** `MEASURED` 2026-09-04T12:50Z: live `main` tip `7a4977bb06fcb87ca72950f97f26c43a991c001b`, committed `2026-08-14T05:58:15Z`, message `substrate-kit v1.20.1 → v1.21.0 (distribution wave, phase 3) (#215)`. Pinned SHA identical. `archived=False`, `private=False`, `pushed_at=2026-08-14T05:58:17Z`.

**What the prior evidence establishes**, verbatim (§ 2, *Keep — the owner's call, not mine*):

> | `gba-homebrew` | **rework** | One letter (`OQ-GBA-NEXT-PICKS`) unblocks a released engine plus four titles. Archiving before he answers would seal work he asked to continue. |

and § 5:

> - **`OQ-GBA-NEXT-PICKS`** and **`OQ-PML-EMERALD-LETTER`** — one letter each, each unblocking a whole repo. Until they are answered, both stay keeps.

Establishes: **keep · rework**; the block is **one owner letter** with a stable slug; and a scale fact — *"a released engine plus four titles."* That last clause is the closest thing in the document to a purpose statement for any of my five, and it is still a size, not a subject: it does not say the titles are GBA/NDS homebrew, does not name them, does not say anything is on Pages.

I re-checked the gate rather than assuming it: `MEASURED` 2026-09-04, `docs/owner-queue.md:327` still carries `OQ-GBA-NEXT-PICKS` as an open ask (*"the letter pick + playtest verdicts that would resume the game lab (added 2026-08-21, fleet review fm #878)"*) with no ANSWERED marker, contrasting with `OQ-ESTATE-ARCHIVE-LIST` at line 270 which is marked *"✅ ANSWERED 2026-08-22 · ✅ EXECUTED 2026-08-23."* So the row's gating condition is still live.

**What it explicitly does NOT establish.** No purpose in plain language (no game names, no platform, no site). No state word — *"unblocks"* implies blocked but the document never says *parked*, *frozen* or *complete*. No path inside the repository; the row cites `OQ-GBA-NEXT-PICKS`, which is a **hub** document, and the rubric's Q3 form demands *"a path **inside that repository**, not a hub document."* Nothing about what not to trust — notably the required-check trap (`NDS ROM build` reds on cold-cache PRs) that ESTATE.md line 88 carries is absent here, so a fresh agent working from this evidence alone would meet it unwarned.

**Verdict: NOT_REUSABLE** for purpose, state word, in-repo truth location and trust warnings. **REUSABLE** for: the disposition (keep · rework), the identity of the single blocking owner ask, and the instruction *"Until they are answered, both stay keeps."*

---

## `pokemon-mod-lab`

**Zero movement, re-verified.** `MEASURED` 2026-09-04T12:50Z: live `main` tip `086dde68d5e2ad6f1dfe9cc90d093487505d459f`, committed `2026-07-21T18:07:39Z`, message `Final closeout: PROJECT-CLOSEOUT.md + current-state true-up + claims prune + seat close (#112)`. Pinned SHA identical. `archived=False`, **`private=True`**, `pushed_at=2026-07-21T18:07:40Z`. Its tip is the oldest of the five — **45 days** of stillness at the pinned instant.

**What the prior evidence establishes**, verbatim (§ 2):

> | `pokemon-mod-lab` | **rework** | One letter (`OQ-PML-EMERALD-LETTER`) unblocks it; 18 toggles, byte-identical-when-off, is finished working work waiting on a single answer. |

plus the same § 5 sentence quoted above. Gate re-checked: `docs/owner-queue.md:342` still carries `OQ-PML-EMERALD-LETTER` open, with the choice enumerated (*"**B** = keep deepening the QoL+ preset · **A** = start the Emerald Hard slices · **Q** = playtest first"*) and *"Nothing multi-session moves until the owner picks."*

Establishes: **keep · rework**; the block is one owner letter; and a genuine **content** fact — *"18 toggles, byte-identical-when-off"* — which is the only claim across the four disposition-sourced rows that describes what the repository actually contains. It is a `MEASURED-PRIOR` claim at best from my seat: the document sources its row reasons to *"that repo's own `current-state.md` / `PROJECT-CLOSEOUT.md`"*, and I did not open the private repo's tree, so I am relying on a document describing a surface rather than the surface.

**What it explicitly does NOT establish.** Not the purpose — *"18 toggles"* of what, in which game, is nowhere in the row; the words *Pokémon*, *Emerald*, *rom-hack* and *private* do not appear in it. No state word. No in-repo path. Nothing about what not to trust — and this repo has a real trap the row omits: it is **private**, which the document never mentions and which changes what a fresh agent can even fetch. `MEASURED` by me, 2026-09-04: `private=True`.

**Verdict: NOT_REUSABLE** for purpose, state word, in-repo truth location and trust warnings. **REUSABLE** for the disposition, the blocking letter, and the single content fact (*18 toggles, byte-identical-when-off*) — the last tagged `MEASURED-PRIOR` 2026-08-22, not `MEASURED`.

---

## `superbot-plugin-hello`

**Zero movement, re-verified — with one thing worth stating.** `MEASURED` 2026-09-04T12:50Z: live `main` tip `abd91334dc554c26098eb4af4fac0ec3478437d9`, committed `2026-07-15T15:29:41Z`, message `ci: install merge-on-green automation (#3)`. Pinned SHA identical. `archived=False`, `private=False`.

**`pushed_at=2026-07-18T09:35:59Z` is three days LATER than the tip commit.** I did not leave that as an anomaly: `GET /branches?per_page=100` returns **1 of 1** branch — `main` at `abd9133…` — so no other branch carries the later push today. `REASONED`: the later `pushed_at` is consistent with a since-deleted branch or a tag push. It does not disturb the zero-movement finding on `main`, which is what the classification measures, but it is a live demonstration that `pushed_at` and default-branch movement are different instruments.

**Second live fact the classification's shape invites getting wrong:** this repo is listed in the disposition document's **Archive (12)** section, yet it is **`archived=False` today**. That is not a contradiction — the document's own header says so: *"The three gated rows (`superbot-next` + `superbot-plugin-hello` on GCB-1, `product-forge` on R2) were not touched."* But a successor reading only the § 2 table, without the header, would record this repo as archived and be wrong. Flagged as a reading hazard of the evidence, not as a defect in it.

**What the prior evidence establishes.** Unusually for these rows, it is substantial. § 2, Archive table:

> | `superbot-plugin-hello` | ESTATE.md's *"never archive"* does not hold, and the reason is stronger than the lockfile: **`superbot-next` carries its own copy of the plugin in-tree** at `examples/superbot-plugin-hello/` (`pyproject.toml`, `manifest.py`, `superbot_plugin_hello/__init__.py` — `MEASURED` 2026-08-22 by code search inside that repo). The host resolves an *installed distribution* via its `sb.plugins` entry point and checks the `manifest_hash` pin against that manifest; it never reaches this standalone repo. So this is a published exemplar, not a build input, and archiving it cannot affect the host's boot. Archive it with `superbot-next`, as one pair. |

and § 3, second bullet, which is the deciding read:

> **Strengthened 2026-08-22 by reading the host's own boot proof** rather than inferring from the files' presence — a vendored copy proves nothing unless the host actually loads it. `superbot-next/tests/unit/app/test_plugin_boot_real_exemplar.py` sets `_EXEMPLAR_ROOT = _REPO_ROOT / "examples" / "superbot-plugin-hello"` and puts that package root on `sys.path` because *"the exemplars live in-tree but are NOT installed dists"*, then verifies the committed pin against **that** manifest by hash. So the load path is the in-tree copy and the pin is a hash comparison; neither is a fetch, and the standalone repo is an exemplar publication rather than a build input. The prohibition rests on a dependency that is not there.

with its own honest boundary, verbatim:

> *Not checked, and not needed:* whether the vendored manifest still hashes to the pinned value — archiving changes neither side of that comparison.

This row **does** answer a purpose question: *"a published exemplar, not a build input"*, *"an exemplar publication rather than a build input."* It answers a **relational** question decisively — nothing consumes this repo at build time; `superbot-next` vendors its own copy. It is `MEASURED-PRIOR` 2026-08-22 from a named test file, which is far better provenance than the other three rows carry.

**What it does NOT establish.** Not a state word: the row gives a **disposition** (*archive it, as one pair*) and — measured above — that disposition has **not been executed**, so a successor that reads the row as a state statement records the wrong thing. Not an in-repo path: no `README`, no `current-state.md`, no closeout is named for **this** repository; every path cited (`examples/superbot-plugin-hello/`, `plugins.lock.json`, `tests/unit/app/test_plugin_boot_real_exemplar.py`) lives in `superbot-next`. Not what the exemplar demonstrates in its own terms — the plugin contract's shape is nowhere here. And the one thing the row explicitly disclaims, quoted above, is the hash currency.

**Verdict: split, and I will not round it.** **REUSABLE** for: *is this repository a build input for anything* (**no** — measured from the host's own boot test) and *what is its intended disposition* (archive, paired with `superbot-next`, **gated and not yet executed**). **NOT_REUSABLE** for: *what state is it in* (the row's disposition is not the live state — measured `archived=False` — and a successor cannot get the state word from here), and *where does its truth live inside itself* (no path in this repository is named anywhere in the evidence).

---

## `venture-lab`

**Zero movement, re-verified.** `MEASURED` 2026-09-04T12:50Z: live `main` tip `a7220b1d348a7045acda828c52e47f51ee2844c8`, committed `2026-08-13T18:58:29Z`, message `substrate-kit v1.20.1 → v1.21.0 (distribution wave, phase 3) (#289)`. Pinned SHA identical. `archived=False`, `private=False`, `pushed_at=2026-08-13T18:58:30Z`.

**This is the one row anchored to a different, and different-in-kind, document** — `docs/repos/venture-lab/README.md`, dated **2026-08-21**, i.e. **8 days after** the tree stopped moving. Its own header states its scope:

> **What this is:** fleet-manager's entry point for `menno420/venture-lab` — where the last session left off and where the next one should look. **Canonical for nothing.** The repo's own `docs/PROJECT-CLOSEOUT.md` wins on the handover, `docs/current-state.md` on its state (with the two staleness caveats below), `docs/conventions.md` on how work ships, and the live tree wins over all of them. Depth files are **not yet written** — created by the 2026-08-21 fleet review (Tier-1, "cleared to build" since 2026-08-08) and carries only the entry point so far.

**What it establishes**, and it answers the successor's questions directly rather than by implication:

*Purpose*, verbatim:

> `venture-lab` is the estate's commerce lane ("Venture"): find and validate the cheapest credible path to first revenue — **agents build, the owner clicks**. What it holds now: **1 LIVE $29 Gumroad SKU** (Stripe Webhook Test Kit, launched 2026-07-12, 0 organic sales measured), 19 publish-READY SKUs, 3 hard-gated bundles + photo packs, and **12 finished books** (The Night Kiln ×6, Lull/DREAMLINE ×3, Ultramarine ×3) with 7 KDP-ready packages. Last merge: #289, kit v1.20.1 → **v1.21.0** (2026-08-13, distribution wave). Last product work: 2026-07-20/21 (closeout).

*State word*, verbatim, twice:

> ### Thread: product/publishing — **paused by OD-11** (owner-paced, indefinitely)

> What would resume it: the owner's word, nothing else.

*Where truth lives, inside the repository* — the header names `docs/PROJECT-CLOSEOUT.md`, `docs/current-state.md`, `docs/conventions.md`, and the traps section corrects the front door:

> - The repo README is frozen in seat-era lane framing ("ORDER 001 in control/inbox.md") — the real front door is `docs/PROJECT-CLOSEOUT.md` § 5.

*What must NOT be trusted* — four separate warnings, verbatim:

> **The governing fact a session must carry in: OD-11 supersedes the repo's own top threads.** The owner ruled 2026-07-26: *"let it sit"* — no kill-clock action, no delist, no publish wave; he works the sellable-products angle himself, at his own pace. The repo has **zero awareness of OD-11** (`MEASURED` 2026-08-21: no hits in its docs): its `PROJECT-CLOSEOUT.md` § 3 and `launch/kill-clock-decision-packet.md` still present the (expired 2026-07-26) T+14 delist call and the publish wave as live top threads. **Do not action delist/publish/kill-clock work from the repo's docs alone.**

> - **The auto-merge enabler is ACTIVE** — a green READY `claude/*` PR squash-merges itself; opt out with a `do-not-automerge` label set at open.
> - **`docs/publishing/OWNER-QUEUE.md` is GENERATED — never hand-edit**; regenerate via `scripts/derive_owner_queue.py`.
> - **Hard rails:** NO spend, account creation, publishing, or payment flows without explicit owner action (`README.md` § rails). NL proofread is owner-only.

*Verify command*, verbatim:

> - Verify: `python3 bootstrap.py check --strict` + `python3 -m pytest scripts/test_*.py`; required on `main`: PR + exactly one check, `substrate-gate` (already the OD-9 one-check model). No deploy — merging is not publishing here.

**Why zero movement genuinely does work here, and only here.** This document's tree-derived claims were measured 2026-08-21 against a tree whose last commit was 2026-08-13. Zero commits since means every one of them still describes the current tree. The clearest instance is its own known drift, which it records:

> The repo's own `docs/current-state.md:64` still claims kit **v1.20.1**; the tree is **v1.21.0** (`substrate.config.json`, #289 touched only kit files — no restamp). A session doing any work here should restamp that line in passing.

Zero movement means that drift is **still** present and still exactly as described — the warning has not gone stale, it has been preserved. Same for the auto-merge enabler, the generated OWNER-QUEUE and the frozen README.

**What it does NOT establish, and this half is real.** Its **product/state layer is owner intent, not tree state**: *"paused by OD-11"* rests on a ruling of **2026-07-26**, and OD-11 lives in the hub, not in this repository — the document says so itself (*"The repo has **zero awareness of OD-11**"*). **Zero commits is not evidence about OD-11's currency**, because the owner can lift a hold without any commit landing anywhere; the tree is simply the wrong instrument for that claim. `MEASURED` 2026-09-04 by me: `docs/owner-queue.md` still lists the venture asks under the hold (`OQ-VENTURE-PUBLISH-CLICKS`, `OQ-VENTURE-STRIPE-KEYS`, `OQ-VENTURE-GOTCHA-ARTICLE` are named in the README as waiting *"under OD-11's blanket hold"*), so nothing contradicts it — but a hub record agreeing with a hub record is not independent confirmation, and I record it as `MEASURED-PRIOR` + `OWNER`, not `MEASURED`. Two further gaps: it says of itself *"Depth files are **not yet written**"*, so anything below the entry-point layer is absent by the author's own statement; and its *"0 organic sales measured"* is a **Gumroad dashboard** fact — the document states *"its metrics are owner-dashboard-only"* — which no amount of git stillness can refresh.

**Verdict: REUSABLE**, and it is the only unqualified one of the five. Reusable for: what the repo is for, what it holds, its state word (*paused*), where truth lives **inside the repository** (`docs/PROJECT-CLOSEOUT.md` § 5 as the real front door, `docs/current-state.md` for state), what a fresh agent must not trust (the frozen README, the OD-11-unaware closeout threads, the generated OWNER-QUEUE, the live auto-merge), the verify command and the required check. **Two carve-outs that must travel with it, or the reuse over-claims:** (1) the OD-11 pause is `OWNER` 2026-07-26 and expires on his word without a commit — do not treat zero movement as evidence for it; (2) the sales/SKU numbers are external-surface facts (Gumroad), not tree facts, and are `MEASURED-PRIOR` 2026-08-21 with no in-repo way to refresh them.

---

## The pattern, stated once

**4 of 5** rows — every row anchored to `planning/2026-08-22-repo-dispositions.md` — are `NOT_REUSABLE` for the successor's routing questions **despite** a fully confirmed zero-movement fact. The reason is uniform and is not a defect in that document: it measured *"should this be archived, and if kept, rework or fresh"*, and it says in its own header that it is *"**Not canonical for** any repo's internal state."* A truthful answer to a different question does not become an answer to this one because the tree held still. The one row anchored to a **Layer-2 entry point** (`repos/venture-lab/README.md`) is reusable, because that genre asks the successor's questions by design.

**The correlation is exact and worth acting on:** the four `NOT_REUSABLE` repos are precisely the four of my five with **no `docs/repos/<name>/` folder**, and the one `REUSABLE` repo is the one that has one. `REASONED`. The cheapest fix is not a re-audit of four trees that have not moved — it is writing four Layer-2 entry points, and `docs/ESTATE.md` already holds a purpose line, a state word and a canonical entry for all four (lines 88, 89, 95, 110), so the raw material exists in the hub even though the baseline's artifact set excludes it.

**One contradiction, recorded rather than resolved in my favour:** `superbot-plugin-hello` sits in the disposition document's *Archive (12)* table and is `archived=False` live (`MEASURED` 2026-09-04). Both are correct — the document's header names it one of three gated rows *"not touched"* — but the table and the live state disagree on their face, and a successor reading the table alone will get the state wrong. Not `UNRESOLVED`; resolved by the header, and the hazard is in the reading, not the record.

**Walls:** none. Every call returned; no error text to report.
