#!/usr/bin/env python3
"""build_notebook_bundle.py — turn a repo tree into Gemini Notebook sources.

================================ PROVENANCE ================================
Why added : `OQ-GEMINI-NOTEBOOKS`. The owner wants to build notebooks in
            Gemini Notebook (= NotebookLM, renamed; his account is PRO). The
            product's whole value is that a citation resolves to ONE specific
            source, so the standing estate rule is **partition, never
            concatenate** — merging files collapses citation granularity,
            which is the point of the upload. This tool keeps file-to-source
            strictly 1:1 and merges nothing, ever.
            It is a tool rather than a one-off because the same job is owed for
            `idea-engine` (566 idea files, over the cap, partitioned on its
            consumer-repo seams).
What it does:
            1. Enumerates **tracked files only** when the source is a git
               checkout, so `.git/**`, untracked build output and `.env` can
               never reach a bundle that gets published.
            2. Classifies every file: a source, or held back with a stated
               reason. Nothing is silently dropped.
            3. Converts what a notebook cannot ingest (`.ino`, `.scad`, `.py`,
               `.sh`, `.yml`, `.json`, and `.html`, which is accepted only as a
               web URL). Formats it DOES ingest natively — PDF, DOCX, images,
               audio — are copied through as bytes, never decoded.
            4. Partitions when the corpus exceeds the per-notebook cap, on
               top-level-directory seams, splitting no file.
            5. Flattens the path INTO the filename (`a/b/c.md` -> `a__b__c.md`),
               because in this product **the filename is the citation label**.
Date      : 2026-08-23
Reliability: The `CORPORA` exclusion table is the only judgment here; every
            other step is mechanical. Re-read it before trusting an exclusion.
            **Hardened 2026-08-23 against nine `@codex` findings on fm #934**,
            three of them P1 and each reproduced by the reviewer: a local-clone
            `--src` leaked `.git/**` and an untracked `.env` into `sources/`;
            binary sources were UTF-8 decoded into corruption; and the bundle
            claimed single-notebook regardless of size, which would have broken
            the partition rule on the very `idea-engine` reuse this exists for.
            The rest: flat-name collisions silently overwrote, a reused `--out`
            kept stale files, CSS `content:` strings were harvested as prose,
            a triple-backtick inside a code file escaped its own fence, the
            index carried a hardcoded date, and the index undercounted itself.
============================================================================
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import html
import io
import os
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import urllib.request
from dataclasses import dataclass
from html.parser import HTMLParser

MACHINERY = "repo machinery — carries no workshop knowledge"
REDIRECT = "redirect tombstone — the repo's own index lists it as a compatibility path"
UNSUPPORTED = "binary format Gemini Notebook does not ingest"
SYMLINK = "symlink — not dereferenced; it can point outside the corpus"
SECRETISH = "secret-shaped filename — never bundled, since bundles get published"
OVERSIZE = "over Gemini Notebook's documented per-source limit"

# Documented per-source ceilings (docs/providers/gemini-notebook.md). A file
# over these is rejected by the product at upload, which would silently leave
# the notebook short of the completeness count the index states.
MAX_SOURCE_BYTES = 200 * 1024 * 1024
MAX_SOURCE_WORDS = 500_000

# Sources per notebook. 300 is the owner's PRO splash reading; it is NOT
# established for the standalone surface, so it is a parameter, not a constant
# baked into the logic. See docs/providers/gemini-notebook.md.
DEFAULT_CAP = 300

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
            # (a compact 5-step PR route) and is KEPT.
            "guides/how-a-pr-flows/index.html": REDIRECT + " (meta-refresh stub; its guide.md is kept)",
        },
    },
    "idea-engine": {
        "repo": "menno420/idea-engine",
        "title": "Idea Engine — de ideeenverzameling",
        # `ideas/` holds everything, subdivided by CONSUMER REPO. Depth 1 would
        # see one 742-file group and cut it alphabetically; depth 2 gives
        # `ideas/superbot`, `ideas/fleet`, ... which are exclusive by
        # construction and are the seams the estate already records.
        "group_depth": 2,
        "exclude_exact": {".gitignore": MACHINERY},
        "exclude_prefix": {
            ".sessions/": "session cards — a different corpus (504 files) that "
                          "would swamp the ideas and burn most of the cap",
            ".substrate/": MACHINERY,
            ".github/": MACHINERY,
            ".claude/": MACHINERY,
            "control/": MACHINERY,
            "scripts/": MACHINERY,
        },
    },
}

NATIVE_MD = {".md"}
# Formats the product ingests as-is. Copied byte-for-byte; decoding one of
# these would destroy exactly the source material this tool exists to prepare.
NATIVE_BINARY = {
    ".pdf", ".docx", ".pptx", ".epub", ".csv",
    ".png", ".jpg", ".jpeg", ".gif", ".webp",
    ".mp3", ".wav", ".m4a", ".aac", ".ogg",
}
CODE_LANG = {
    ".ino": "cpp", ".scad": "openscad", ".py": "python", ".sh": "bash",
    ".json": "json", ".yml": "yaml", ".yaml": "yaml", ".css": "css",
    ".txt": "text", ".toml": "toml", ".cfg": "ini", ".ini": "ini",
}

BLOCK_TAGS = {
    "p", "div", "section", "article", "header", "footer", "main", "br",
    "h1", "h2", "h3", "h4", "h5", "h6", "li", "tr", "td", "th", "figcaption",
    "blockquote", "pre", "ul", "ol", "table", "nav", "aside", "details",
}

RESERVED_NAMES = {"00-INDEX.md"}

# POSIX filesystems cap a single name component at 255 bytes.
MAX_NAME_BYTES = 255


class TextExtractor(HTMLParser):
    """Visible text only. <style> and <script> are tracked SEPARATELY.

    Lumping them into one skip counter fed CSS bodies to the prose harvester,
    so a `content:"…"` declaration became a stage caption (@codex, fm #934).
    Presentation text is not source knowledge.
    """

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.parts: list[str] = []
        self.title = ""
        self.scripts: list[str] = []
        self._in_style = 0
        self._in_script = 0
        self._in_title = False
        self._chrome = 0

    def handle_starttag(self, tag, attrs):
        if tag == "style":
            self._in_style += 1
        elif tag == "script":
            self._in_script += 1
        elif tag == "button":
            # Control labels are interface chrome, not the lesson.
            self._chrome += 1
        elif tag == "title":
            self._in_title = True
        elif tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_endtag(self, tag):
        if tag == "style":
            self._in_style = max(0, self._in_style - 1)
        elif tag == "script":
            self._in_script = max(0, self._in_script - 1)
        elif tag == "button":
            self._chrome = max(0, self._chrome - 1)
        elif tag == "title":
            self._in_title = False
        elif tag in BLOCK_TAGS:
            self.parts.append("\n")

    def handle_data(self, data):
        if self._in_script:
            self.scripts.append(data)
            return
        if self._in_style or self._chrome:
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

    These animated guides keep their per-stage captions in JS arrays, so the DOM
    text alone loses the actual lesson. Heuristic on purpose, and the output
    says so: >=4 words, no CSS braces, mostly letters.
    """
    found: list[str] = []
    for _q, body in PROSE_RE.findall(script_text):
        s = html.unescape(TAG_RE.sub("", body)).replace("\\n", " ").strip()
        s = re.sub(r"\s+", " ", s)
        if len(s) < 20 or s.count(" ") < 3:
            continue
        if "{" in s or "}" in s or "://" in s:
            continue
        if sum(ch.isalpha() for ch in s) < len(s) * 0.6:
            continue
        if s not in found:
            found.append(s)
    return found


def fence_for(text: str) -> str:
    """A fence longer than any backtick run inside the content.

    A code file containing its own triple backtick (a prompt fixture, a README
    snippet) otherwise closes the fence early and the remainder is parsed as
    notebook prose — which can inject headings into retrieval (@codex, fm #934).
    """
    longest = max((len(m) for m in re.findall(r"`+", text)), default=0)
    return "`" * max(3, longest + 1)


@dataclass
class Item:
    path: str
    kind: str
    disposition: str
    reason: str = ""
    out_name: str = ""
    payload: object = b""
    notebook: int = 1


def flat_name(path: str, keep_ext: bool = False) -> str:
    """Path -> a single visible filename that reads as a citation.

    A leading dot is spelled out: `.github/x.yml` becomes `dot-github__x.yml.md`
    and NOT a hidden file — invisible in the upload picker and missed by
    select-all. Measured while building the first corpus: two sources and seven
    held-back files vanished from `ls` for exactly that reason.
    """
    flat = path.replace("/", "__")
    if flat.startswith("."):
        flat = "dot-" + flat[1:]
    if not (keep_ext or flat.endswith(".md")):
        flat += ".md"
    if len(flat.encode("utf-8")) > MAX_NAME_BYTES:
        # Flattening turns a legal deep path into ONE component, which can blow
        # past the 255-byte filesystem limit and fail the whole build with
        # ENAMETOOLONG (@codex round 3). Keep a readable prefix and make it
        # unique with a stable digest of the full path.
        stem, ext = os.path.splitext(flat)
        digest = hashlib.sha256(path.encode("utf-8")).hexdigest()[:12]
        budget = MAX_NAME_BYTES - len(ext.encode("utf-8")) - len(digest) - 1
        stem = stem.encode("utf-8")[:max(1, budget)].decode("utf-8", "ignore")
        flat = f"{stem}~{digest}{ext}"
    return flat


def provenance(repo: str, sha: str, path: str, note: str) -> str:
    return (
        f"> **Bron:** `{path}`  \n"
        f"> **Repository:** `{repo}` @ `{sha}` (public)  \n"
        f"> **{note}**\n\n---\n\n"
    )


def convert(path: str, data: bytes, repo: str, sha: str):
    """Return (payload, kind, keep_ext). Payload is bytes for native binaries."""
    ext = os.path.splitext(path)[1].lower()

    if ext in NATIVE_BINARY:
        return data, f"native binary ({ext}, byte-for-byte)", True

    try:
        text = data.decode("utf-8")
    except UnicodeDecodeError:
        return None, f"undecodable binary ({ext or 'no ext'})", True

    if ext in NATIVE_MD:
        return text, "markdown (verbatim)", False

    if ext in (".html", ".htm"):
        ex = TextExtractor()
        ex.feed(text)
        body = ex.text()
        captions = harvest_prose("\n".join(ex.scripts))
        out = [provenance(
            repo, sha, path,
            "Interactieve visuele uitleg — tekst uit de pagina gehaald; "
            "CSS en scriptcode zijn weggelaten.",
        )]
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
        return "\n".join(out).rstrip() + "\n", "html (text-extracted)", False

    fence = fence_for(text)
    head = provenance(
        repo, sha, path,
        f"Broncodebestand (`{ext or 'geen extensie'}`) — onbewerkt, in een codeblok.",
    )
    lang = CODE_LANG.get(ext, "")
    return (f"{head}# `{path}`\n\n{fence}{lang}\n{text.rstrip()}\n{fence}\n",
            f"code ({ext or 'no ext'})", False)


# Never bundle these, on any path. A bundle gets PUBLISHED, so this list is a
# backstop for the walk mode and is deliberately blunt: a false skip costs one
# manifest line, a false include costs a credential.
SECRET_PATTERNS = (
    re.compile(r"(^|/)\.env($|\.|/)"),
    re.compile(r"(^|/)\.netrc$"),
    re.compile(r"(^|/)\.npmrc$"),
    re.compile(r"(^|/)\.pypirc$"),
    re.compile(r"(^|/)id_(rsa|dsa|ecdsa|ed25519)($|\.)"),
    re.compile(r"\.(pem|key|p12|pfx|keystore|jks)$"),
    re.compile(r"(^|/)(credentials|secrets?)(\.(json|ya?ml|ini|txt))?$"),
    re.compile(r"(^|/)service[-_]account.*\.json$"),
)


def is_secretish(path: str) -> bool:
    low = path.lower()
    return any(p.search(low) for p in SECRET_PATTERNS)


def list_files(root: str) -> list[str]:
    """Tracked files when `root` is a git checkout; a guarded walk otherwise.

    A filesystem walk over a normal clone sweeps in `.git/**`, ignored build
    output and untracked files — `@codex` reproduced an untracked `.env`
    reaching `sources/` (fm #934). Since bundles get PUBLISHED, that is a
    credential path.

    Two rules follow, and the second was added because the first alone was not
    enough: a `.git` present but unreadable USED to fall back to a plain walk,
    which re-opened the exact leak. Measured by this repo's own regression test
    on the fix — the fallback emitted `dot-env.md`. So a broken checkout is now
    a hard error rather than a guess, and the walk carries a deny-list for the
    legitimate no-git case (an extracted tarball).
    """
    # `.git` is a FILE, not a directory, in a linked worktree or a submodule
    # checkout — testing only for a directory sent those standard checkouts down
    # the walk path, undoing the whole fix (@codex round 2).
    if os.path.exists(os.path.join(root, ".git")):
        try:
            out = subprocess.run(
                ["git", "-C", root, "ls-files", "-z"],
                capture_output=True, check=True,
            ).stdout.decode("utf-8", "replace")
            # `--untracked-files=no` is load-bearing: untracked files are
            # already excluded by ls-files, so they cannot affect a bundled
            # file's provenance. Only a MODIFIED TRACKED file makes the
            # `@ <sha>` header false. Without this the guard refused every
            # ordinary working repo — caught by this repo's own regression.
            dirty = subprocess.run(
                ["git", "-C", root, "status", "--porcelain", "--untracked-files=no"],
                capture_output=True, check=True,
            ).stdout.decode("utf-8", "replace").strip()
        except (OSError, subprocess.CalledProcessError) as exc:
            raise SystemExit(
                f"error: `{root}` carries a .git entry but git failed "
                f"({exc}). Refusing to fall back to a filesystem walk — that "
                "would sweep in untracked and ignored files, and bundles get "
                "published. Point --src at a clean checkout or an extracted "
                "tarball."
            )
        if dirty:
            # `git ls-files` constrains NAMES only; the bytes still come from
            # the working tree, so a local edit would be published under a
            # provenance header naming a commit that does not contain it.
            raise SystemExit(
                f"error: `{root}` has uncommitted changes:\n"
                + "\n".join("  " + ln for ln in dirty.splitlines()[:10])
                + "\n  Every source carries a `@ <sha>` provenance header, so "
                "publishing working-tree bytes would make that claim false — and "
                "a local edit to a tracked config file would reach the public "
                "asset. Commit, stash, or use --fetch."
            )
        paths = sorted(p for p in out.split("\0") if p)
        print(f"note: {len(paths)} tracked file(s) via git ls-files "
              "(untracked and ignored files excluded; tree verified clean)")
        # Return everything: a TRACKED secret-shaped path (`.env.example` is the
        # common one) must be classified and LISTED as held back, not silently
        # dropped from enumeration — the manifest promises every omission has a
        # stated reason (@codex round 3).
        return paths

    paths, skipped = [], []
    for dirpath, dirnames, files in os.walk(root):
        dirnames[:] = [d for d in dirnames if d != ".git"]
        for f in files:
            rel = os.path.relpath(os.path.join(dirpath, f), root).replace(os.sep, "/")
            (skipped if is_secretish(rel) else paths).append(rel)
    if skipped:
        print(f"note: {len(skipped)} secret-shaped file(s) refused: "
              + ", ".join(sorted(skipped)[:5]))
    return sorted(paths)


def group_key(path: str, depth: int) -> str:
    """The seam a partition falls on.

    Depth 1 is the top-level directory, which is right for most corpora. It is
    WRONG for a corpus whose meaning lives one level down: `idea-engine` keeps
    everything under a single `ideas/` directory subdivided by consumer repo,
    so depth 1 sees one 742-file group and splits it alphabetically — exactly
    the arbitrary cut the seam is supposed to avoid. Depth 2 gives
    `ideas/superbot`, `ideas/fleet`, ... which are exclusive by construction.
    """
    if depth < 1:
        # depth 0 collapses every path to one empty key (a single silent
        # mega-group); a negative depth slices from the end and coincidentally
        # behaves like some other depth. Both are wrong quietly, which is worse
        # than loudly. Raised by @codex on fm #936.
        raise ValueError(f"group depth must be >= 1, got {depth}")
    parts = path.split("/")
    if len(parts) > depth:
        return "/".join(parts[:depth])
    if len(parts) > 1:
        return "/".join(parts[:-1])
    return "(root)"


def partition(items: list[Item], cap: int, depth: int = 1) -> int:
    """Assign each source a notebook number, splitting on top-level seams.

    The estate rule is partition, never concatenate: a corpus over the cap
    becomes MORE notebooks, never fewer files. Groups are top-level directories
    so a partition falls on a meaning boundary rather than an alphabetical one.
    """
    srcs = [i for i in items if i.disposition == "source"]
    if len(srcs) + 1 <= cap:          # +1 for the generated index
        return 1

    groups: dict[str, list[Item]] = {}
    for i in srcs:
        groups.setdefault(group_key(i.path, depth), []).append(i)

    # First-fit-decreasing across ALL open notebooks, not just the current one.
    # Packing only forward left a 4th notebook holding 12 files while the first
    # had 50 free slots — four notebooks for him to create instead of three.
    # Largest-first keeps the big consumer seams whole and lets the long tail of
    # small groups backfill the gaps.
    load = [1]                          # each notebook also carries an index
    for top in sorted(groups, key=lambda g: (-len(groups[g]), g)):
        members = groups[top]
        if len(members) + 1 > cap:
            print(f"note: `{top}/` alone holds {len(members)} sources, over the "
                  f"cap of {cap}; it is split across notebooks. No file merged.")
            for m in members:
                slot = next((i for i, u in enumerate(load) if u + 1 <= cap), None)
                if slot is None:
                    load.append(1)
                    slot = len(load) - 1
                m.notebook = slot + 1
                load[slot] += 1
            continue
        # A group that fits stays whole, in the first notebook with room for it.
        slot = next((i for i, u in enumerate(load) if u + len(members) <= cap), None)
        if slot is None:
            load.append(1)
            slot = len(load) - 1
        for m in members:
            m.notebook = slot + 1
        load[slot] += len(members)
    return len(load)


def assert_disjoint(src_root: str, out_dir: str) -> None:
    """Refuse an --out that overlaps --src.

    `build()` rmtree's `sources/`, `excluded/` and `notebook-*` under --out to
    clear stale files. With `--src . --out .` those are directories of the
    SOURCE repository, so a build would quietly delete tracked content out of
    the caller's checkout while reporting success (@codex round 2). A
    destructive path is worth a hard stop, not a warning.
    """
    src = os.path.realpath(src_root)
    out = os.path.realpath(out_dir)
    if src == out:
        raise SystemExit("error: --out must not be the same directory as --src.")
    if out.startswith(src + os.sep):
        raise SystemExit(
            f"error: --out (`{out}`) is inside --src (`{src}`). The build clears "
            "sources/, excluded/ and notebook-* under --out, which would delete "
            "content from the source tree."
        )
    if src.startswith(out + os.sep):
        raise SystemExit(
            f"error: --src (`{src}`) is inside --out (`{out}`), so the cleanup "
            "step could remove the tree being read."
        )


def build(src_root: str, corpus: str, out_dir: str, sha: str, cap: int,
          depth: int = 1) -> tuple[list[Item], int]:
    cfg = CORPORA[corpus]
    repo, excl = cfg["repo"], cfg["exclude_exact"]
    prefixes = cfg.get("exclude_prefix", {})
    assert_disjoint(src_root, out_dir)

    items: list[Item] = []
    claimed: dict[str, str] = {}
    for p in list_files(src_root):
        full = os.path.join(src_root, p)
        if is_secretish(p):
            items.append(Item(p, "secret-shaped", "excluded", SECRETISH,
                              flat_name(p, True), None))
            continue
        bulk = next((r for pre, r in prefixes.items() if p.startswith(pre)), None)
        if bulk:
            items.append(Item(p, "structural", "excluded", bulk,
                              flat_name(p, True), None))
            continue
        if os.path.islink(full):
            # os.path.isfile() follows the link, so `notes.md -> ../private.md`
            # would copy data from OUTSIDE the corpus into a published source
            # while the manifest blamed the innocent repo path (@codex round 2).
            items.append(Item(p, "symlink", "excluded", SYMLINK,
                              flat_name(p, True), None))
            continue
        if not os.path.isfile(full):
            continue
        data = open(full, "rb").read()
        # Byte ceiling FIRST. `data.split()` on a whitespace-dense 200 MB file
        # materialises tens of millions of bytestrings and can OOM the builder
        # while trying to reject that very file (@codex round 3).
        if len(data) > MAX_SOURCE_BYTES:
            items.append(Item(p, "oversized", "excluded",
                              f"{OVERSIZE} ({len(data) // (1024 * 1024)} MB)",
                              flat_name(p, True), None))
            continue
        words = len(data.split())
        if words > MAX_SOURCE_WORDS:
            items.append(Item(p, "oversized", "excluded",
                              f"{OVERSIZE} (~{words} words)",
                              flat_name(p, True), None))
            continue
        payload, kind, keep_ext = convert(p, data, repo, sha)
        name = flat_name(p, keep_ext)

        # Compare case-INSENSITIVELY: the bundle is unzipped on whatever
        # filesystem the owner has, and on a case-insensitive one `Dir/a.md`
        # and `dir__a.md` overwrite each other while the manifest counts two
        # (@codex round 3).
        key = name.casefold()
        if key in {r.casefold() for r in RESERVED_NAMES}:
            raise SystemExit(
                f"error: `{p}` flattens to reserved name `{name}`, which the "
                "generated index uses. Rename it or add an exclusion."
            )
        if key in claimed:
            raise SystemExit(
                f"error: flat-name collision `{name}` — both `{claimed[key]}` "
                f"and `{p}` map to it (case-insensitively). 1:1 cannot be "
                "honoured; resolve first."
            )
        claimed[key] = p

        if payload is None:
            items.append(Item(p, kind, "excluded", UNSUPPORTED, name, b""))
        elif p in excl:
            items.append(Item(p, kind, "excluded", excl[p], name, payload))
        else:
            items.append(Item(p, kind, "source", "", name, payload))

    notebooks = partition(items, cap, depth)

    # A reused --out otherwise keeps files from a previous run that the fresh
    # manifest does not list, so select-all uploads content nothing describes.
    for stale in ("sources", "excluded"):
        shutil.rmtree(os.path.join(out_dir, stale), ignore_errors=True)
    for d in sorted(os.listdir(out_dir)) if os.path.isdir(out_dir) else []:
        if d.startswith("notebook-"):
            shutil.rmtree(os.path.join(out_dir, d), ignore_errors=True)

    def target(item: Item) -> str:
        if item.disposition == "excluded":
            return os.path.join(out_dir, "excluded")
        if notebooks == 1:
            return os.path.join(out_dir, "sources")
        return os.path.join(out_dir, f"notebook-{item.notebook:02d}")

    for i in items:
        d = target(i)
        os.makedirs(d, exist_ok=True)
        if i.payload is None:      # nothing to materialise (symlink, oversized)
            continue
        # NB: `not i.payload` would skip a legitimately EMPTY tracked file while
        # every generated total still counted it (@codex round 2).
        mode, enc = ("wb", None) if isinstance(i.payload, bytes) else ("w", "utf-8")
        with open(os.path.join(d, i.out_name), mode, encoding=enc) as fh:
            fh.write(i.payload)
    os.makedirs(os.path.join(out_dir, "excluded"), exist_ok=True)
    return items, notebooks


def src_dirname(notebooks: int, nb: int) -> str:
    return "sources" if notebooks == 1 else f"notebook-{nb:02d}"


def write_index(out_dir: str, corpus: str, sha: str, built: str,
                items: list[Item], notebooks: int, depth: int = 1) -> None:
    """A navigational source per notebook, uploaded alongside the rest.

    This is an INDEX, not a merge: it adds one source that helps the model
    orient and collapses nobody's citation into anybody else's.
    """
    cfg = CORPORA[corpus]
    for nb in range(1, notebooks + 1):
        srcs = [i for i in items if i.disposition == "source" and i.notebook == nb]
        # Counts ITSELF: the README tells him to upload N files, so an index
        # claiming N-1 would defeat the post-upload completeness check.
        total = len(srcs) + 1
        groups: dict[str, list[Item]] = {}
        for i in srcs:
            groups.setdefault(group_key(i.path, depth), []).append(i)

        part = f" — deel {nb} van {notebooks}" if notebooks > 1 else ""
        L = [
            f"# INHOUDSOPGAVE — {cfg['title']}{part}\n",
            f"> Automatisch gegenereerd uit `{cfg['repo']}` @ `{sha}` op {built}.",
            f"> Dit notitieboek bevat **{total} bronnen** (deze inhoudsopgave "
            "meegeteld). Elk bestand uit de repository is één bron; er is niets "
            "samengevoegd.\n",
            "Elke bronnaam is het oorspronkelijke pad met `/` vervangen door "
            "`__`, zodat een citaat laat zien waar het vandaan komt.\n",
        ]
        if notebooks > 1:
            L.append(
                f"> **Let op:** de volledige verzameling is over {notebooks} "
                "notitieboeken verdeeld omdat hij niet in één past. Geen enkel "
                "bestand is samengevoegd om te passen.\n"
            )
        for top in sorted(groups):
            L.append(f"\n## `{top}/` — {len(groups[top])} bronnen\n")
            for i in sorted(groups[top], key=lambda x: x.path):
                L.append(f"- `{i.out_name}` — {i.path}")
        d = os.path.join(out_dir, src_dirname(notebooks, nb))
        os.makedirs(d, exist_ok=True)
        open(os.path.join(d, "00-INDEX.md"), "w",
             encoding="utf-8").write("\n".join(L) + "\n")


def write_manifest(out_dir: str, corpus: str, sha: str, built: str,
                   items: list[Item], notebooks: int, cap: int) -> None:
    cfg = CORPORA[corpus]
    srcs = [i for i in items if i.disposition == "source"]
    excs = [i for i in items if i.disposition == "excluded"]
    kinds: dict[str, int] = {}
    for i in srcs:
        kinds[i.kind] = kinds.get(i.kind, 0) + 1

    L = [
        f"# MANIFEST — {corpus} notebook bundle\n",
        f"- **Source repo:** `{cfg['repo']}` @ `{sha}` (public)",
        f"- **Built:** {built}",
        f"- **Files read:** {len(items)} (tracked files only)",
        f"- **Uploaded as sources:** {len(srcs)} + {notebooks} generated "
        f"index/indexes = **{len(srcs) + notebooks}**",
        f"- **Notebooks:** {notebooks} (cap {cap} sources each)",
        f"- **Held back:** {len(excs)} — every one listed below with its reason",
        "- **Merged:** 0. File-to-source is 1:1 by construction.\n",
    ]
    if notebooks > 1:
        L.append(
            f"> The corpus exceeds {cap} sources, so it is **partitioned across "
            f"{notebooks} notebooks** on top-level-directory seams. Nothing was "
            "concatenated to make it fit — merging would collapse the citation "
            "granularity the upload exists for.\n"
        )
        for nb in range(1, notebooks + 1):
            n = len([i for i in srcs if i.notebook == nb])
            L.append(f"- `{src_dirname(notebooks, nb)}/` — {n + 1} sources")
        L.append("")

    L.append("## Conversions applied\n")
    for k in sorted(kinds):
        L.append(f"- {kinds[k]} × {k}")
    L += [
        "\n`.md` files are byte-identical to the repo, and formats the product "
        "ingests natively (PDF, DOCX, images, audio) are copied byte-for-byte. "
        "Everything else was converted because Gemini Notebook does not ingest "
        "`.html`, `.ino`, `.scad`, `.py`, `.sh`, `.json` or `.yml` uploads — "
        "code keeps its full text inside a fenced block, HTML keeps its "
        "human-readable text and loses its minified CSS/JS.\n",
        "## Held back, and why\n",
        "| file | reason |",
        "|---|---|",
    ]
    for i in sorted(excs, key=lambda x: x.path):
        L.append(f"| `{i.path}` | {i.reason} |")
    L += [
        "\nNothing here is deleted — each is in `excluded/`, already converted, "
        "so any of them can be added to a notebook by dragging it in.\n",
        "## Every source\n",
        "| source name (the citation label) | from | kind | notebook |",
        "|---|---|---|---|",
    ]
    for i in sorted(srcs, key=lambda x: x.path):
        L.append(f"| `{i.out_name}` | `{i.path}` | {i.kind} | {i.notebook} |")
    open(os.path.join(out_dir, "MANIFEST.md"), "w",
         encoding="utf-8").write("\n".join(L) + "\n")


def write_readme(out_dir: str, corpus: str, items: list[Item],
                 notebooks: int, cap: int) -> None:
    cfg = CORPORA[corpus]
    srcs = [i for i in items if i.disposition == "source"]

    if notebooks == 1:
        n = len(srcs) + 1
        where = (f"**{n} bestanden in `sources/`.** Dat past in één notebook: "
                 f"de limiet is {cap} bronnen per notebook.")
        steps = (f"1. Open Gemini Notebook en maak een nieuw notebook.\n"
                 f"2. Kies **Bronnen toevoegen → Bestanden uploaden**.\n"
                 f"3. Selecteer **alles** in `sources/` (Ctrl+A in de "
                 f"bestandskiezer).\n"
                 f"4. Wachten tot alle {n} bronnen verwerkt zijn.")
    else:
        rows = "\n".join(
            f"   - `{src_dirname(notebooks, nb)}/` → "
            f"{len([i for i in srcs if i.notebook == nb]) + 1} bronnen"
            for nb in range(1, notebooks + 1)
        )
        where = (f"**{len(srcs) + notebooks} bronnen, verdeeld over "
                 f"{notebooks} notebooks**, omdat de verzameling niet in één "
                 f"past (limiet {cap} per notebook). **Er is niets "
                 f"samengevoegd om te passen** — dat zou juist kapotmaken "
                 f"waarvoor je uploadt.")
        steps = ("1. Maak **één notebook per map** hieronder:\n" + rows +
                 "\n2. Upload per notebook **alles** uit die ene map "
                 "(Ctrl+A) — meng de mappen niet.")

    open(os.path.join(out_dir, "README.md"), "w", encoding="utf-8").write(f"""\
# {cfg['title']} — klaar om te uploaden

{where}

## Wat je doet

{steps}

## Waarom het er zo uitziet

- **Eén bestand = één bron.** Er is niets samengevoegd. Dat is de hele reden
  om te uploaden: een citaat wijst naar één specifiek bestand.
- **De bestandsnaam is het citaat.** `guides__first-layer__guide.md` laat in
  het antwoord zien waar het vandaan komt; 22 bestanden die allemaal
  `guide.md` heten zouden dat niet doen.
- **`00-INDEX.md`** is een gegenereerde inhoudsopgave, en telt zichzelf mee.
  Upload hem mee — hij helpt het notebook de rest overzien, en het getal erin
  hoort te kloppen met wat je geüpload hebt.
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
    ap.add_argument("--src", help="an already-extracted repo tree or a clone")
    ap.add_argument("--fetch", action="store_true",
                    help="download the tarball with $GITHUB_PAT instead")
    ap.add_argument("--ref", default="main")
    ap.add_argument("--cap", type=int, default=DEFAULT_CAP,
                    help=f"sources per notebook (default {DEFAULT_CAP})")
    ap.add_argument("--date", help="build date for provenance (default: today)")
    ap.add_argument("--group-depth", type=int, default=None,
                    help="path depth the partition seam falls on (default: the "
                         "corpus's own setting, else 1 = top-level directory)")
    args = ap.parse_args()

    cfg = CORPORA[args.corpus]
    sha = os.environ.get("BUNDLE_SHA", args.ref)
    built = args.date or datetime.date.today().isoformat()
    src = args.src
    fetched = None
    os.makedirs(args.out, exist_ok=True)

    if args.fetch:
        tok = os.environ.get("GITHUB_PAT", "")
        url = f"https://api.github.com/repos/{cfg['repo']}/tarball/{args.ref}"
        req = urllib.request.Request(url, headers={"Authorization": f"Bearer {tok}"})
        opener = urllib.request.build_opener(urllib.request.ProxyHandler({}))
        blob = opener.open(req, timeout=90).read()
        # Extract OUTSIDE --out. Left under --out, the raw checkout survives
        # into any archive of the bundle — a second full copy of the repo,
        # including everything deliberately held back (@codex round 2).
        work = tempfile.mkdtemp(prefix="notebook-src-")
        fetched = work
        with tarfile.open(fileobj=io.BytesIO(blob)) as tf:
            tf.extractall(work)
        roots = [d for d in os.listdir(work) if os.path.isdir(os.path.join(work, d))]
        src = os.path.join(work, roots[0])
        sha = roots[0].rsplit("-", 1)[-1]

    if not src or not os.path.isdir(src):
        print("error: need --src <dir> or --fetch", file=sys.stderr)
        return 2

    if not args.fetch and os.path.exists(os.path.join(src, ".git")):
        # A clean checkout says nothing about WHICH commit it is on. Without
        # this, a clone sitting on a feature branch or an old commit gets every
        # source stamped `@ main` — a clean tree and a false provenance header
        # at the same time (@codex round 3). Resolve it, do not label it.
        try:
            head = subprocess.run(
                ["git", "-C", src, "rev-parse", "HEAD"],
                capture_output=True, check=True,
            ).stdout.decode().strip()
        except (OSError, subprocess.CalledProcessError) as exc:
            raise SystemExit(f"error: cannot resolve HEAD in `{src}` ({exc}).")
        if sha not in (head, head[:len(sha)]) and sha != args.ref:
            print(f"note: overriding provenance `{sha}` with resolved HEAD {head[:10]}")
        elif sha == args.ref:
            print(f"note: --ref `{args.ref}` is a label; resolved HEAD is "
                  f"{head[:10]} and that is what provenance records")
        sha = head[:10]

    depth = args.group_depth or cfg.get("group_depth", 1)
    try:
        if depth < 1:
            raise SystemExit(
                f"error: --group-depth {depth} is invalid — 1 is the top-level "
                "directory; there is no shallower seam."
            )
        if args.cap < 2:
            raise SystemExit(
                f"error: --cap {args.cap} is unusable — every notebook reserves "
                "one slot for its generated index, so a cap below 2 cannot hold "
                "an index and a single source."
            )
        items, notebooks = build(src, args.corpus, args.out, sha, args.cap, depth)
        write_index(args.out, args.corpus, sha, built, items, notebooks, depth)
        write_manifest(args.out, args.corpus, sha, built, items, notebooks, args.cap)
        write_readme(args.out, args.corpus, items, notebooks, args.cap)
    finally:
        if fetched:
            shutil.rmtree(fetched, ignore_errors=True)

    n_src = len([i for i in items if i.disposition == "source"])
    print(f"corpus     : {args.corpus} ({cfg['repo']} @ {sha})")
    print(f"built      : {built}")
    print(f"files read : {len(items)}")
    print(f"sources    : {n_src} + {notebooks} index = {n_src + notebooks}")
    print(f"notebooks  : {notebooks} (cap {args.cap})")
    print(f"held back  : {len(items) - n_src}")
    print(f"out        : {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
