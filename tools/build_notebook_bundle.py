#!/usr/bin/env python3
"""build_notebook_bundle.py — turn a repo tree into Gemini Notebook sources.

================================ PROVENANCE ================================
Why added : `OQ-GEMINI-NOTEBOOKS`. The owner wants to build notebooks in
            Gemini Notebook (= NotebookLM, renamed; his account is PRO). The
            product's whole value is that a citation resolves to ONE specific
            source, so the standing estate rule is **partition, never
            concatenate** — merging files collapses citation granularity,
            which is the point of the upload. This tool therefore keeps
            file-to-source strictly 1:1 and merges nothing, ever.
            It exists as a tool rather than a one-off because the same job is
            owed for `idea-engine` (566 idea files, over the 300 cap, to be
            partitioned on its consumer-repo seams).
What it does:
            1. Classifies every file: a notebook source, or held back with a
               stated reason. Nothing is silently dropped.
            2. Converts what a notebook cannot ingest. Gemini Notebook takes
               Markdown/text/PDF/DOCX/CSV/audio and web URLs — NOT `.ino`,
               `.scad`, `.py`, `.yml` or `.html` files. Code is wrapped in a
               fenced block with a provenance header; HTML is reduced to its
               human-readable text (its minified CSS/JS is retrieval poison).
            3. Flattens the path INTO the filename (`a/b/c.md` ->
               `a__b__c.md`), because in this product **the filename is the
               citation label** — a flat `guide.md` cites uselessly 22 times.
Date      : 2026-08-23
Reliability: The classification rules are per-corpus and stated in CORPORA
            below, each traced to a line in the source repo that justifies it
            (e.g. curious-research's own `guides/README.md` names its five
            redirect directories as link-compatibility scaffolding). Re-read
            that table before trusting an exclusion; it is a judgment, and it
            is the only judgment in this script. Everything else is mechanical.
============================================================================
"""

from __future__ import annotations

import argparse
import html
import io
import os
import re
import sys
import tarfile
import urllib.request
from dataclasses import dataclass, field
from html.parser import HTMLParser

# --------------------------------------------------------------------------
# Per-corpus rules. Each exclusion carries the reason that goes in MANIFEST.md.
# --------------------------------------------------------------------------

MACHINERY = "repo machinery — carries no workshop knowledge"
REDIRECT = "redirect tombstone — the repo's own index lists it as a compatibility path"

CORPORA = {
    "curious-research": {
        "repo": "menno420/curious-research",
        "title": "Curious Research — de werkplaatsnotitieboek",
        "exclude_exact": {
            ".gitignore": MACHINERY,
            "site/style.css": MACHINERY,
            ".claude/settings.json": MACHINERY,
            ".github/workflows/auto-merge-enabler.yml": MACHINERY,
            ".github/workflows/pages.yml": MACHINERY,
            ".github/workflows/substrate-gate.yml": MACHINERY,
            ".github/scripts/check_links.py": MACHINERY,
            ".github/scripts/check_openscad.sh": MACHINERY,
            # The four superseded guides: BOTH halves are tombstones. Traced to
            # guides/README.md's "Compatibele oude paden" table.
            "guides/start-here/guide.md": REDIRECT + " (-> begin-hier/)",
            "guides/start-here/index.html": REDIRECT + " (-> begin-hier/)",
            "guides/infill/guide.md": REDIRECT + " (-> vulling/)",
            "guides/infill/index.html": REDIRECT + " (-> vulling/)",
            "guides/how-print-clearance-works/guide.md": REDIRECT + " (-> speling/)",
            "guides/how-print-clearance-works/index.html": REDIRECT + " (-> speling/)",
            "guides/arm-envelope-explained/guide.md": REDIRECT + " (-> arm-werkgebied/)",
            "guides/arm-envelope-explained/index.html": REDIRECT + " (-> arm-werkgebied/)",
            # Fifth redirect row, and it splits: the .md carries real content
            # (a compact 5-step PR route) and is KEPT; only the 3-second
            # meta-refresh stub is held back.
            "guides/how-a-pr-flows/index.html": REDIRECT + " (meta-refresh stub; its guide.md is kept)",
        },
    },
}

# Extensions a notebook ingests directly. Everything else gets converted.
NATIVE_MD = {".md"}
CODE_LANG = {
    ".ino": "cpp", ".scad": "openscad", ".py": "python", ".sh": "bash",
    ".json": "json", ".yml": "yaml", ".yaml": "yaml", ".css": "css",
    ".txt": "text",
}

BLOCK_TAGS = {
    "p", "div", "section", "article", "header", "footer", "main", "br",
    "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr", "td", "th", "figcaption",
    "blockquote", "pre", "ul", "ol", "table", "nav", "aside", "details",
}


class TextExtractor(HTMLParser):
    """Visible text only: <style>/<script> bodies are dropped, blocks break."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.title = ""
        self._skip = 0
        self._in_title = False
        self.scripts: list[str] = []
        self._chrome = 0

    def handle_starttag(self, tag, attrs):
        if tag in ("style", "script"):
            self._skip += 1
        elif tag == "button":
            # Control labels ("Volgende", "Alles afspelen") are interface
            # chrome, not the lesson. They ran together into one meaningless
            # line in all 26 explainers before this.
            self._chrome += 1
        elif tag == "title":
            self._in_title = True
        elif tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag in ("style", "script"):
            self._skip = max(0, self._skip - 1)
        elif tag == "button":
            self._chrome = max(0, self._chrome - 1)
        elif tag == "title":
            self._in_title = False
        elif tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        if self._skip:
            self.scripts.append(data)
            return
        if self._chrome:
            return
        if self._in_title:
            self.title += data.strip()
            return
        if data.strip():
            self.parts.append(data)

    def text(self) -> str:
        raw = "".join(self.parts)
        lines = [re.sub(r"[ \t]+", " ", ln).strip() for ln in raw.split("\n")]
        out, blank = [], False
        for ln in lines:
            if ln:
                out.append(ln)
                blank = False
            elif not blank:
                out.append("")
                blank = True
        return "\n".join(out).strip()


PROSE_RE = re.compile(r"""(['"])((?:\\.|(?!\1)[^\\]){20,})\1""")
TAG_RE = re.compile(r"<[^>]+>")


def harvest_prose(script_text: str) -> list[str]:
    """Pull caption-like string literals out of inline JS.

    These animated guides keep their per-stage captions in JS arrays, so the
    DOM text alone loses the actual lesson. Heuristic on purpose, and the
    output says so: >=4 words, no CSS braces, real letters.
    """
    found: list[str] = []
    for _q, body in PROSE_RE.findall(script_text):
        s = html.unescape(TAG_RE.sub("", body)).replace("\\n", " ").strip()
        s = re.sub(r"\s+", " ", s)
        if len(s) < 20 or s.count(" ") < 3:
            continue
        if "{" in s or "}" in s or "://" in s:
            continue
        letters = sum(ch.isalpha() for ch in s)
        if letters < len(s) * 0.6:
            continue
        if s not in found:
            found.append(s)
    return found


@dataclass
class Item:
    path: str
    kind: str
    disposition: str
    reason: str = ""
    out_name: str = ""
    nbytes: int = 0


def flat_name(path: str) -> str:
    """Path -> a single visible filename that reads as a citation.

    A leading dot is spelled out: `.github/x.yml` becomes `dot-github__x.yml.md`
    and NOT `.github__x.yml.md`, which would be a hidden file — invisible in the
    upload picker and missed by select-all. Measured while building this: two
    sources and seven held-back files vanished from `ls` for exactly that reason.
    """
    flat = path.replace("/", "__")
    if flat.startswith("."):
        flat = "dot-" + flat[1:]
    return flat if flat.endswith(".md") else flat + ".md"


def provenance(repo: str, sha: str, path: str, note: str) -> str:
    return (
        f"> **Bron:** `{path}`  \n"
        f"> **Repository:** `{repo}` @ `{sha}` (public)  \n"
        f"> **{note}**\n\n---\n\n"
    )


def convert(path: str, data: bytes, repo: str, sha: str) -> tuple[str, str]:
    """Return (markdown_text, kind)."""
    ext = os.path.splitext(path)[1].lower()
    text = data.decode("utf-8", errors="replace")

    if ext in NATIVE_MD:
        return text, "markdown (verbatim)"

    if ext in (".html", ".htm"):
        ex = TextExtractor()
        ex.feed(text)
        body = ex.text()
        captions = harvest_prose("\n".join(ex.scripts))
        head = provenance(
            repo, sha, path,
            "Interactieve visuele uitleg — tekst uit de pagina gehaald; "
            "CSS en scriptcode zijn weggelaten.",
        )
        out = [head]
        if ex.title:
            out.append(f"# {ex.title}\n")
        if body:
            out.append(body + "\n")
        if captions:
            out.append(
                "\n## Stapbijschriften uit de animatie\n\n"
                "*Machinaal uit het inline script gehaald; de volgorde volgt "
                "het script, niet noodzakelijk het scherm.*\n"
            )
            out.extend(f"- {c}" for c in captions)
        return "\n".join(out).rstrip() + "\n", "html (text-extracted)"

    lang = CODE_LANG.get(ext, "")
    head = provenance(
        repo, sha, path,
        f"Broncodebestand (`{ext or 'geen extensie'}`) — onbewerkt, in een codeblok.",
    )
    return f"{head}# `{path}`\n\n```{lang}\n{text.rstrip()}\n```\n", f"code ({ext or 'no ext'})"


def build(src_root: str, corpus: str, out_dir: str, sha: str) -> list[Item]:
    cfg = CORPORA[corpus]
    repo = cfg["repo"]
    excl = cfg["exclude_exact"]

    paths = []
    for root, _dirs, files in os.walk(src_root):
        for f in files:
            full = os.path.join(root, f)
            paths.append(os.path.relpath(full, src_root).replace(os.sep, "/"))
    paths.sort()

    src_dir = os.path.join(out_dir, "sources")
    exc_dir = os.path.join(out_dir, "excluded")
    os.makedirs(src_dir, exist_ok=True)
    os.makedirs(exc_dir, exist_ok=True)

    items: list[Item] = []
    for p in paths:
        data = open(os.path.join(src_root, p), "rb").read()
        md, kind = convert(p, data, repo, sha)
        name = flat_name(p)
        if p in excl:
            item = Item(p, kind, "excluded", excl[p], name, len(md))
            open(os.path.join(exc_dir, name), "w", encoding="utf-8").write(md)
        else:
            item = Item(p, kind, "source", "", name, len(md))
            open(os.path.join(src_dir, name), "w", encoding="utf-8").write(md)
        items.append(item)
    return items


def write_index(out_dir: str, corpus: str, sha: str, items: list[Item]) -> None:
    """A navigational source, uploaded alongside the rest.

    This is an INDEX, not a merge: it adds one source that helps the model
    orient, and collapses nobody's citation into anybody else's.
    """
    cfg = CORPORA[corpus]
    srcs = [i for i in items if i.disposition == "source"]
    groups: dict[str, list[Item]] = {}
    for i in srcs:
        top = i.path.split("/")[0] if "/" in i.path else "(root)"
        groups.setdefault(top, []).append(i)

    L = [
        f"# INHOUDSOPGAVE — {cfg['title']}\n",
        f"> Automatisch gegenereerd uit `{cfg['repo']}` @ `{sha}` op 2026-08-23.",
        f"> Dit notitieboek bevat **{len(srcs)} bronnen**. Elk bestand uit de "
        "repository is één bron; er is niets samengevoegd.\n",
        "Elke bronnaam is het oorspronkelijke pad met `/` vervangen door `__`, "
        "zodat een citaat laat zien waar het vandaan komt.\n",
    ]
    for top in sorted(groups):
        L.append(f"\n## `{top}/` — {len(groups[top])} bronnen\n")
        for i in sorted(groups[top], key=lambda x: x.path):
            L.append(f"- `{i.out_name}` — {i.path}")
    open(os.path.join(out_dir, "sources", "00-INDEX.md"), "w",
         encoding="utf-8").write("\n".join(L) + "\n")


def write_manifest(out_dir: str, corpus: str, sha: str, items: list[Item]) -> None:
    cfg = CORPORA[corpus]
    srcs = [i for i in items if i.disposition == "source"]
    excs = [i for i in items if i.disposition == "excluded"]
    kinds: dict[str, int] = {}
    for i in srcs:
        kinds[i.kind] = kinds.get(i.kind, 0) + 1

    L = [
        f"# MANIFEST — {corpus} notebook bundle\n",
        f"- **Source repo:** `{cfg['repo']}` @ `{sha}` (public)",
        f"- **Files in repo:** {len(items)}",
        f"- **Uploaded as sources:** {len(srcs)} (+ `00-INDEX.md`, generated) "
        f"= **{len(srcs) + 1}**",
        f"- **Held back:** {len(excs)} — every one listed below with its reason",
        "- **Merged:** 0. File-to-source is 1:1 by construction.\n",
        "## Conversions applied\n",
    ]
    for k in sorted(kinds):
        L.append(f"- {kinds[k]} × {k}")
    L += [
        "\n`.md` files are byte-identical to the repo. Everything else was "
        "converted because Gemini Notebook does not ingest `.html`, `.ino`, "
        "`.scad`, `.py`, `.sh`, `.json` or `.yml` uploads — code keeps its "
        "full text inside a fenced block, HTML keeps its human-readable text "
        "and loses its minified CSS/JS.\n",
        "## Held back, and why\n",
        "| file | reason |",
        "|---|---|",
    ]
    for i in sorted(excs, key=lambda x: x.path):
        L.append(f"| `{i.path}` | {i.reason} |")
    L += [
        "\nNothing here is deleted — each is in `excluded/`, already converted, "
        "so any of them can be added to the notebook by dragging it in.\n",
        "## Every source\n",
        "| source name (the citation label) | from | kind |",
        "|---|---|---|",
    ]
    for i in sorted(srcs, key=lambda x: x.path):
        L.append(f"| `{i.out_name}` | `{i.path}` | {i.kind} |")
    open(os.path.join(out_dir, "MANIFEST.md"), "w",
         encoding="utf-8").write("\n".join(L) + "\n")


def write_readme(out_dir: str, corpus: str, items: list[Item]) -> None:
    n = len([i for i in items if i.disposition == "source"]) + 1
    cfg = CORPORA[corpus]
    open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8").write(f"""\
# {cfg['title']} — klaar om te uploaden

**{n} bestanden in `sources/`.** Dat past in één notebook: de PRO-limiet is
300 bronnen per notebook.

## Wat je doet

1. Open Gemini Notebook en maak een nieuw notebook.
2. Kies **Bronnen toevoegen → Bestanden uploaden**.
3. Selecteer **alles** in `sources/` (Ctrl+A in de bestandskiezer).
4. Wachten tot alle {n} bronnen verwerkt zijn.

## Waarom het er zo uitziet

- **Eén bestand = één bron.** Er is niets samengevoegd. Dat is de hele reden
  om te uploaden: een citaat wijst naar één specifiek bestand.
- **De bestandsnaam is het citaat.** `guides__first-layer__guide.md` laat in
  het antwoord zien waar het vandaan komt; 22 bestanden die allemaal
  `guide.md` heten zouden dat niet doen.
- **`00-INDEX.md`** is een gegenereerde inhoudsopgave. Upload hem mee — hij
  helpt het notebook de rest overzien.
- **`excluded/`** hoef je niet te uploaden. Zie `MANIFEST.md` voor wat er in
  zit en waarom; je kunt er alsnog iets uit toevoegen.

## Een goede eerste vraag

> "Ik heb een print die aan de rand loslaat op de A1 mini. Welke controle doe
> ik eerst volgens mijn eigen gidsen, en welke bron zegt dat?"

Het antwoord hoort naar een specifiek bestand te verwijzen. Doet het dat niet,
dan is er iets misgegaan met de upload.
""")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--corpus", required=True, choices=sorted(CORPORA))
    ap.add_argument("--out", required=True)
    ap.add_argument("--src", help="already-extracted repo tree")
    ap.add_argument("--fetch", action="store_true",
                    help="download the tarball with $GITHUB_PAT instead")
    ap.add_argument("--ref", default="main")
    args = ap.parse_args()

    cfg = CORPORA[args.corpus]
    sha = os.environ.get("BUNDLE_SHA", args.ref)
    src = args.src

    if args.fetch:
        tok = os.environ.get("GITHUB_PAT", "")
        url = f"https://api.github.com/repos/{cfg['repo']}/tarball/{args.ref}"
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {tok}"})
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        blob = opener.open(req, timeout=90).read()
        work = os.path.join(args.out, "_src")
        os.makedirs(work, exist_ok=True)
        with tarfile.open(fileobj=io.BytesIO(blob)) as tf:
            tf.extractall(work)
        roots = [d for d in os.listdir(work) if os.path.isdir(os.path.join(work, d))]
        src = os.path.join(work, roots[0])
        sha = roots[0].rsplit("-", 1)[-1]

    if not src or not os.path.isdir(src):
        print("error: need --src <dir> or --fetch", file=sys.stderr)
        return 2

    items = build(src, args.corpus, args.out, sha)
    write_index(args.out, args.corpus, sha, items)
    write_manifest(args.out, args.corpus, sha, items)
    write_readme(args.out, args.corpus, items)

    n_src = len([i for i in items if i.disposition == "source"])
    n_exc = len(items) - n_src
    print(f"corpus     : {args.corpus} ({cfg['repo']} @ {sha})")
    print(f"files read : {len(items)}")
    print(f"sources    : {n_src} + 1 generated index = {n_src + 1}")
    print(f"held back  : {n_exc}")
    print(f"out        : {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
