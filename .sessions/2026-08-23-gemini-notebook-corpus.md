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

## Verification

- **All 75 `.md` byte-identical** to the repo — checked file by file, not spot-checked.
- `ls` == `ls -A` == 110 sources / 17 held back; 110 + 17 = 127 = 126 files + 1 index.
- Manifest reconciles: 71 verbatim + 4 held = 75 md · 25 extracted + 5 held = 30 html.
- No empty output: smallest source is 393 bytes and is a real idea file.
- Zip `testzip()` OK, 129 entries, 414 KB.

## Open

- **His answer.** The offer is put; nothing here presumes it.
- **Two Notebook facts, one now CONFIRMED.** Google's own Gemini Notebook FAQ
  states **"100 notebooks per account"** and **"Up to 50 sources per notebook"**
  on free — so the source cap is confirmed **per notebook** (the queue had it as
  *consistent, not confirmed*), and notebook count **is** capped. The PRO
  numbers are not on that page; 300/notebook remains his splash reading.
- **Does archiving stop scheduled Actions?** Still open, and today cannot settle
  it. Measured: `superbot-idle`'s `host-main-advisory` fires daily ~05:40–05:48Z,
  last run `2026-08-23T05:42:49Z`, and the repo was archived at `07:11Z` —
  **after** that day's run. The workflow `state` field reports `active` on all
  six despite the archive, so that field is not the instrument. GitHub's
  archiving doc says nothing about Actions (fetched, confirmed silent). Next
  window `2026-08-24` ~05:45Z; a run is conclusive, a miss is not.
