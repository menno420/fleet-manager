# 2026-08-23 — the first Gemini Notebook corpus: curious-research, built and offered

> **Status:** `in-progress` — branch `claude/gemini-notebook-corpus-f7sa69`, cut
> from `origin/main` at `42a2e28` (fm #933). Born red on purpose: the card is
> the merge hold (TRAP-006). Flips only after
> `python3 bootstrap.py check --strict` returns a real exit 0 on this tree,
> read directly and never after a pipe.

- **📊 Model:** opus-5 · high · tool + docs

## 💡 Session idea

`OQ-GEMINI-NOTEBOOKS` had exactly one thing left in it: the **build offer**. The
product was settled the day before (Gemini Notebook **is** NotebookLM, renamed —
off the rename banner he screenshotted), the constraint was settled
(**partition, never concatenate** — merging files collapses the citation
granularity that is the entire point of the upload), and the target was settled
(`curious-research`, 126 files, one notebook, no partition needed). What was
missing was his *go*.

The trap here is treating "waiting on him" as "nothing to do". The queue entry
itself says the agent half needs nothing from him — *"prepare export bundles …
so his first notebook is a paste, not a project."* So this session **put the
offer to him and built it in the same turn.** If the answer is no, it is a
branch he never merges; if it is yes, the work is already done and his step is
an upload.

The second idea: build it as a **tool, not a one-off**, because the same job is
owed for `idea-engine` — 566 idea files, genuinely over the 300 cap, to be
partitioned on its consumer-repo seams (superbot 249 · fleet 221 · venture-lab
103 · superbot-games 86).

## previous-session review

fm #933 re-derived the corpus sizes and corrected an earlier plan: it had
proposed splitting `curious-research` into themed notebooks, and the measurement
showed 126 files — comfortably under the cap — so the split was invented work.
That correction held: the live tree read here returns **126 blobs, 75 `.md`**,
matching exactly. The prompt's other stated facts were re-verified rather than
trusted: `origin/main` = `42a2e28`, and `GET /user/repos?affiliation=owner` =
**26 repos / 9 archived**, sound because `GET /user/orgs` returns **0**.

## What landed

**[`tools/build_notebook_bundle.py`](../tools/build_notebook_bundle.py)** — turns
a repo tree into notebook sources, 1:1, merging nothing. Corpus-agnostic so
`idea-engine` reuses it.

**The built bundle** — 126 files in, **110 sources** out (109 + a generated
index), 17 held back with a stated reason each, published as a release asset so
his step is one download.

## What this session measured, and what it changes

Three findings changed the build. All were things the prompt could not have
known, and two of them would have quietly degraded his first notebook.

1. **`index.html` is not a render of `guide.md`.** The assumption going in was
   that 26 of the 30 HTML files duplicated their markdown sibling and should be
   dropped. Opening a pair falsified it: `index.html` is a self-contained
   **animated visual explainer** whose six step-captions live in a JS array, and
   whose condensed "Beslisregel" the markdown does not state that way. The
   repo's own `.claude/skills/visual-explainers/SKILL.md` confirms the design —
   `guide.md` is called *"de companion"*. So they are kept, but **text-extracted**:
   uploading them raw would have fed the notebook ~4KB of minified CSS/JS each.
2. **Five directories are redirect tombstones, and the repo says so itself.**
   `guides/README.md` has a **"Compatibele oude paden"** table naming
   `start-here/` · `infill/` · `how-print-clearance-works/` ·
   `arm-envelope-explained/` · `how-a-pr-flows/` as paths kept *"zodat bestaande
   links niet breken"*. Four are tombstones in **both** halves (*"Deze gids is
   samengevoegd"*). Uploading them would let the notebook answer *"use vulling
   instead"* — and reintroduce the exact divergence that merge removed
   (*"zodat wand- en infilladvies niet dubbel uiteenloopt"*). Held back. The
   fifth splits: `how-a-pr-flows/guide.md` carries real content and is **kept**;
   only its meta-refresh stub is held.
3. **A leading dot makes a source invisible.** `.github/x.yml` flattened to
   `.github__x.yml.md` — a **hidden file**, absent from the upload picker and
   missed by select-all. Caught because `ls` and `ls -A` disagreed: two sources
   and seven held-back files had silently vanished from the listing. Now spelled
   `dot-github__…`. This is the defect that would have shipped.

## Adversarial review — `@codex`, fm #934, round 1

**Nine findings, three P1, and the tally is `[conceded] 9 / [survived] 0.`** Each
came with a reproduction the reviewer had actually run, and each was real. The
three P1s are the ones worth naming, because two of them would have shipped:

- **A local-clone `--src` leaked `.git/**` and untracked files.** `@codex`
  reproduced an untracked `.env` landing in `sources/` with its contents. This
  session's own build used a tarball, so it never fired — but the flag invites a
  clone, and **bundles get published as a release asset**, so this was a
  credential path into a public artefact. Now `git ls-files` decides.
- **Binary sources were UTF-8 decoded into corruption.** A PDF or image — formats
  the provider doc I wrote in this same PR says the product ingests *natively* —
  would have been `errors="replace"`d into garbage and emitted as Markdown. The
  tool would have destroyed exactly the material it exists to prepare. Now they
  are copied byte-for-byte.
- **The bundle claimed single-notebook regardless of size.** The README said
  "this fits in one notebook" unconditionally, which is false the moment a corpus
  exceeds the cap — **guaranteed** for the `idea-engine` reuse this tool was
  built for. It would have broken the partition-never-concatenate rule on the
  very case that rule exists for. Now it partitions on top-level seams.

The six P2s: flat-name collisions silently overwrote while the manifest still
claimed 1:1; a reused `--out` kept stale files the manifest did not list; CSS
`content:` strings were harvested as stage captions (I had lumped `<style>` and
`<script>` into one skip counter); a triple-backtick inside a code file escaped
its own fence; the index carried a hardcoded date; and the index undercounted
itself by one, so it said 109 while the README said upload 110.

**The fix for the worst one was itself wrong, and the test caught it.**
[`tools/test_build_notebook_bundle.py`](../tools/test_build_notebook_bundle.py)
writes one regression per finding. On its first run, F8 **failed**: when
`git ls-files` errors, my code fell back to a filesystem walk — and the walk
re-emitted `dot-env.md`. A broken checkout is now a hard error rather than a
guess, and the no-git path (an extracted tarball) carries a secret deny-list.
Three paths are now tested: a real clone, a broken `.git`, and a tarball.
**24 assertions, all passing, exit 0.**

### Round 2 — nine more, four P1: `[conceded] 8 / [survived] 1`

Round 1's fixes introduced surface of their own, and round 2 went at it. Eight
were real; the four P1s again include two that would have caused damage:

- **`--out . --src .` would have deleted tracked directories out of the caller's
  checkout.** The stale-file cleanup from round 1 rmtree's `sources/`,
  `excluded/` and `notebook-*` under `--out`; point `--out` at the source and
  those are the *source repo's* directories. A build would report success while
  destroying content. Overlapping paths are now a hard stop.
- **`.git` is a FILE, not a directory, in a linked worktree or submodule** — so
  the round-1 `os.path.isdir` test sent exactly those standard checkouts back
  down the walk path, undoing the credential fix for them.
- **A dirty checkout published working-tree bytes under a `@ sha` header** that
  did not contain them — so a local edit to a tracked config file could reach
  the public asset, and every provenance claim was potentially false. Now
  refused.
- **A tracked symlink was dereferenced**, so `notes.md -> ../private.md` would
  copy content from outside the corpus into a published source while the
  manifest blamed the innocent repo path. Now held back.

Four P2s fixed: a group that would fit was sliced across notebooks anyway
(defeating the consumer-repo seam the partition promises); an empty-but-valid
file was skipped while still counted in every total; the `--fetch` checkout was
left inside `--out`, so archiving the bundle shipped a second full copy of the
repo including everything held back; and sources over the documented 200 MB /
500,000-word ceilings were emitted rather than held back.

**`[survived] 1` — the born-red card.** Codex flagged the card still reading
`in-progress` as a defect to fix before merge. It is the opposite: the card **is**
the merge hold (TRAP-006), and the gate's own message calls it a *"designed hold,
not a defect"*. Flipping it early is precisely the trap. It flips as the last
commit, which is what the badge already promised.

**My own guard was wrong again, and again the test caught it.** The dirty-tree
check first used `git status --porcelain`, which counts **untracked** files — and
untracked files are exactly what `git ls-files` already excludes, so they cannot
affect provenance. That version refused every ordinary working repo. Narrowed to
`--untracked-files=no`, so only a modified *tracked* file blocks.

**38 assertions across both rounds, exit 0.** And the published asset is
**byte-identical** after all of it: every round-2 finding concerned input shapes
`curious-research` does not contain, so the artefact he downloads was already
correct.

### Round 3 — seven, two P1: `[conceded] 7 / [survived] 0`. Converging.

The severity curve is the useful signal: rounds 1–2 found credential paths and a
destructive delete; round 3 found an OOM edge case, a false provenance label, and
filesystem-portability gaps. **9 → 9 → 7, narrowing.** So this is the last round
requested, per `docs/conventions/adversarial-review.md`'s convergence rule.

- **`--ref` was recorded as provenance without being resolved (P1).** A clean
  clone sitting on a feature branch or an old commit stamped every source
  `@ main`. The round-2 clean-tree guard proves the tree matches *its own* HEAD
  and says nothing about which commit that is — clean and false at once. HEAD is
  now resolved with git and that is what provenance records.
- **The 200 MB ceiling tokenised before it rejected (P1).** `data.split()` on a
  whitespace-dense 200 MB file materialises tens of millions of bytestrings and
  can OOM the builder *while trying to reject that very file*. Byte check first.
- Four P2s fixed: flattening a deep path could exceed the 255-byte filename
  limit and fail the build with `ENAMETOOLONG` (now a bounded prefix plus a
  stable digest); collisions were compared case-sensitively, so `Dir/a.md` and
  `dir__a.md` overwrite each other on a case-insensitive filesystem while the
  manifest counts two; `--cap 1` produced an empty first notebook; and a
  **tracked** secret-shaped file such as `.env.example` was dropped from
  enumeration entirely rather than listed as held back — which broke the
  manifest's promise that every omission carries a reason.

**The finding worth the whole review: `idea-engine`'s seam counts do not
partition.** Codex checked the arithmetic in the provider doc I wrote:
`superbot` 249 + `fleet` 221 + `venture-lab` 103 + `superbot-games` 86 = **659**,
against a **566**-file corpus — **93 more than exists**. So they cannot be
disjoint sets; they are almost certainly *overlapping consumer references*,
which is a fine measurement and a **useless partition key** — assign a file to
two notebooks and its citations split, the exact failure the
partition-never-concatenate rule exists to prevent. **This was not my error to
invent but it was mine to propagate**: I copied it out of `owner-queue.md`, where
it reads as a clean plan (*"two notebooks split cleanly on those seams"*). Both
the queue entry and the provider doc are now corrected and marked `UNVERIFIED`,
with the instruction to re-derive an exclusive assignment summing to 566 before
`idea-engine` is built. The builder's default — partition on top-level
directories — is exclusive by construction and is the stated fallback.

**48 assertions across three rounds, exit 0**, and the published asset is
byte-identical after every round.

## Verification

- **All 75 `.md` byte-identical** to the repo — checked file by file, not spot-checked.
- `ls` == `ls -A` == 110 sources / 17 held back; 110 + 17 = 127 = 126 files + 1 index.
- Manifest reconciles: 71 verbatim + 4 held = 75 md · 25 extracted + 5 held = 30 html.
- No empty output: smallest source is 393 bytes and is a real idea file.
- Zip `testzip()` OK, 129 entries; published asset re-downloaded and sha256-matched.
- **24 regression assertions** across all nine `@codex` findings — exit 0.
- Index self-count now reads **110**, matching what the README tells him to upload.

## Open

- **His answer.** The offer is put; nothing here presumes it.
- **Two Notebook facts, one now CONFIRMED.** Google's own Gemini Notebook FAQ
  states **"100 notebooks per account"** and **"Up to 50 sources per notebook"**
  on free — so the source cap is confirmed **per notebook** (the queue had it as
  *consistent, not confirmed*), and notebook count **is** capped. The PRO
  numbers are not on that page; 300/notebook remains his splash reading.
- **Does archiving stop scheduled Actions?** Still open — and the useful result
  is **which instruments cannot answer it**, so the next session does not repeat
  these.
  - **The docs gap is closed, and the answer is "the docs are silent."** GitHub's
    archiving page was fetched: it enumerates what becomes read-only (issues,
    PRs, code, labels, milestones, projects, wiki, releases, commits, tags,
    branches, reactions, alerts, comments, permissions) and **never mentions
    Actions, workflows or schedules**. Swept from the Actions direction too; the
    only concrete artefact is a GitHub-rendered UI string on archived repos —
    *"GitHub Actions workflows can't be executed on this repository"* — sourced
    from community threads, **not** from GitHub's documentation.
  - **Two API surfaces were probed and BOTH are the wrong instrument.**
    `GET /actions/workflows` reports `state: active` for all six of
    `superbot-idle`'s workflows despite the archive, and
    `GET /actions/permissions` returns `{"enabled": true, "allowed_actions":
    "all"}` — **byte-identical to live `fleet-manager`**, which was run as the
    control. The API does not model the archive/Actions relationship at all, so
    neither reading is evidence that Actions still run. Recording the null as a
    property of the probes, not of the world (TRAP-003).
  - **Observation is the only instrument left, and today cannot supply it.**
    `host-main-advisory` fires daily ~05:40–05:48Z (41 scheduled runs, an
    unbroken daily series). Last run `2026-08-23T05:42:49Z`; the repo was
    archived at `07:11Z` — **after** that day's run. Next window `2026-08-24`
    ~05:45Z. **A run is conclusive; a miss is not** — GitHub drops schedule
    windows on inactivity, and an archived repo takes no commits by definition,
    so the 60-day inactivity suspension is a confound that will eventually
    produce a miss for a reason unrelated to archiving.
