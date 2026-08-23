# Gemini Notebook (ex-NotebookLM) — provider reference

> **Status:** `living-ledger` · opened 2026-08-23 · owner queue
> [`OQ-GEMINI-NOTEBOOKS`](../owner-queue.md)
>
> **Not a routing table** — see [`README.md`](README.md). For the *API* Gemini
> (models, keys, billing), that is [`gemini.md`](gemini.md) plus
> [`../conventions/vertex-first-for-gemini.md`](../conventions/vertex-first-for-gemini.md).
> This file is the **consumer notebook product**, which is a different surface
> with different rules, and conflating the two is the mistake it exists to stop.

## What it is

**`Gemini Notebook` IS NotebookLM, renamed.** `OWNER` + `MEASURED` 2026-08-23 —
read off an in-app banner the owner screenshotted, verbatim: *"NotebookLM heet
nu Gemini Notebook. Nieuwe naam. Hetzelfde geweldige product."*

One product, **two entry points**: the standalone Gemini Notebook surface, and a
`Notebooks` section inside the Gemini app, whose splash reads *"Mogelijk gemaakt
door Gemini Notebook"*. The owner's account shows **PRO** on both. UI is Dutch.

**Older estate notes and any external recipe may still say "NotebookLM".** Same
product. Do not treat the two names as different things.

## Limits — and which half is confirmed

| fact | value | certainty |
|---|---|---|
| Source cap is **per notebook**, not per account | — | `MEASURED` 2026-08-23 — Google's own Gemini Notebook FAQ states **"Up to 50 sources per notebook"** |
| Notebook **count** is capped | **100 notebooks per account** (free) | `MEASURED` 2026-08-23, same FAQ |
| Sources per notebook, free | 50 | `MEASURED`, same FAQ |
| Sources per notebook, **PRO** | **300** | `OWNER` — read off the Gemini Apps splash (*"Upload maximaal 300 bronnen"*). **Not** on the FAQ page fetched here, and **not** established for the standalone surface |
| Notebook count on PRO | unknown | `UNVERIFIED` — the FAQ gives the free number only |
| Words per source / file size | 500,000 words · 200 MB | `MEASURED`, same FAQ |

**The two questions that were open before 2026-08-23 are now half-closed.** The
queue recorded *per notebook* as "consistent, not confirmed" and notebook-count
as unknown; Google's own page confirms the **shape** of both. What remains open
is only the **PRO** numbers, which is why the splash reading still stands as the
working figure and is labelled `OWNER` rather than `MEASURED`.

## The rule that governs every bundle: partition, never concatenate

**A corpus over the cap gets split into more notebooks. It never gets merged
into fewer files.** `REVIEWED` — this is the estate's standing decision, and the
reason is the product's whole point: value here is a **citation resolving to one
specific source**. Merge fifty idea files into a themed blob and every citation
resolves to the blob, so the grounding is exactly as coarse as the merge.

Selection stays legitimate — picking the best 300 of 566 is lossy but keeps
citations precise. Concatenation is the option that does not.

## What it ingests — and what it does not

`MEASURED` 2026-08-23 (vendor + third-party agreement): PDF, Word, PowerPoint,
CSV, **Markdown**, plain text, ePub, Google Docs/Slides/Sheets, images, audio,
web URLs, public YouTube, and Gemini chats.

**It does not take a source-code file as an upload.** `.ino`, `.scad`, `.py`,
`.sh`, `.yml`, `.json`, `.css` — and `.html`, which is accepted only as a *web
URL*, not as a file. A repo corpus therefore always needs conversion, and
[`../../tools/build_notebook_bundle.py`](../../tools/build_notebook_bundle.py)
does it: code keeps its full text inside a fenced block under a provenance
header, HTML is reduced to its human-readable text.

## The finding that is easy to miss: the filename is the citation label

`MEASURED` 2026-08-23, building the first corpus. A notebook cites a source by
its **name**. Upload a repo tree flat and you get 22 sources all called
`guide.md`, every citation useless. So the builder flattens the **path into the
name** — `guides/first-layer/guide.md` → `guides__first-layer__guide.md`.

**A leading dot makes a source invisible.** `.github/x.yml` flattens to
`.github__x.yml.md`, a hidden file — absent from the upload picker, missed by
select-all. Spell it `dot-github__…`. This was caught only because `ls` and
`ls -A` disagreed, and it would otherwise have shipped.

## Privacy — the split is asymmetric

`MEASURED` 2026-08-23, off the Gemini Apps splash. Source files added in Gemini
Apps are **not** used to train the models. But *"gesprekken met je notebook in
Gemini Apps worden opgeslagen volgens je instellingen voor Activiteit bewaren"*
and **are** used to improve the models. **Sources in are protected; the
conversation is not.** Sources can still be added with Activiteit bewaren off.

## API reachability

`UNVERIFIED`. This is a consumer surface behind the owner's Google login.
Whether any credential this estate holds reaches it has **not** been tested.
Do not assume it does — and do not record a wall if a probe fails; that would be
one call's result, not a property of the product. **Working assumption until
measured: an agent prepares files, he uploads them.**

## Built so far

| corpus | sources | notebook(s) | state |
|---|---|---|---|
| `curious-research` | 110 (109 files + generated index), 17 held back | 1 — fits well under the cap | **built** 2026-08-23, published as a release asset |
| `idea-engine` | 779 sources (of 1,373 files; 594 held back) | **3** — 300 / 292 / 190, split on `ideas/<consumer-repo>/` seams | **built** 2026-08-23, published as a release asset |

> **✅ The `idea-engine` seams ARE a partition — measured 2026-08-23 (fm #936).**
> An earlier note here said the recorded counts were *"overlapping consumer
> references"*. **That was an inference, it was written as a finding, and it is
> wrong.** `GET /repos/menno420/idea-engine/git/trees/main?recursive=1` (1,373
> blobs, not truncated) grouped on the second path component returns
> `ideas/superbot` **249** · `ideas/fleet` **221** · `ideas/venture-lab` **103** ·
> `ideas/superbot-games` **86** — **matching the recorded figures exactly**, and
> exclusive by construction since every path sits in exactly one directory.
> The real defect was a **denominator mismatch**: `566` counts `.md` minus 14
> README/index files, while `659` counts *all* files (157 `.py` included) in only
> the four largest of **fourteen** consumer dirs. 659 ⊂ 742 total under `ideas/`,
> leaving 83 in the other ten. Both numbers were correct; pairing them was not.
>
> **Depth matters and the default is wrong for this corpus.** Everything lives
> under one `ideas/` directory, so the builder's default depth-1 seam sees a
> single 742-file group and cuts it alphabetically. `--group-depth 2` (set in the
> corpus entry) gives the consumer-repo seams. Notebook 1 holds `superbot` whole,
> notebook 2 holds `fleet` whole; no consumer directory is split.
