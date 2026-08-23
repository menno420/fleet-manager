#!/usr/bin/env python3
"""test_build_notebook_bundle.py — one regression per @codex finding, fm #934.

================================ PROVENANCE ================================
Why added : `@codex` returned nine findings on fm #934, three P1, each with a
            reproduction. A fix asserted without re-running the reproduction is
            a claim, not a verification — and a clean run from an unexercised
            checker is TRAP-003. So every finding gets a test that FAILS
            against the original behaviour.
Date      : 2026-08-23
Reliability: Runs standalone (`python3 tools/test_build_notebook_bundle.py`),
            stdlib only, no network. Builds throwaway corpora in a temp dir.
============================================================================
"""

from __future__ import annotations

import os
import shutil
import subprocess
import sys
import tempfile

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import build_notebook_bundle as B  # noqa: E402

FAILURES: list[str] = []


def check(name: str, ok: bool, detail: str = "") -> None:
    print(f"  {'PASS' if ok else 'FAIL'}  {name}" + (f" — {detail}" if detail and not ok else ""))
    if not ok:
        FAILURES.append(f"{name}: {detail}")


def corpus(tmp: str, files: dict, name: str = "t") -> str:
    root = os.path.join(tmp, name)
    for rel, content in files.items():
        p = os.path.join(root, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        mode = "wb" if isinstance(content, bytes) else "w"
        with open(p, mode, **({} if isinstance(content, bytes) else {"encoding": "utf-8"})) as fh:
            fh.write(content)
    return root


def register(key: str, excl: dict | None = None) -> None:
    B.CORPORA[key] = {"repo": "test/test", "title": "T", "exclude_exact": excl or {}}


def run(src: str, out: str, cap: int = B.DEFAULT_CAP, key: str = "t"):
    items, nb = B.build(src, key, out, "deadbee", cap)
    B.write_index(out, key, "deadbee", "2026-01-01", items, nb)
    B.write_manifest(out, key, "deadbee", "2026-01-01", items, nb, cap)
    B.write_readme(out, key, items, nb, cap)
    return items, nb


def main() -> int:
    tmp = tempfile.mkdtemp()
    register("t")
    print("F8 (P1) — no path may leak .git/**, untracked files or secrets")

    # (a) a REAL clone: git ls-files is authoritative, .env is untracked
    src = corpus(tmp, {"README.md": "# real\n",
                       ".env": "GITHUB_PAT=ghp_secret_value\n"}, "f8a")
    for cmd in (["init", "-q"], ["add", "README.md"],
                ["-c", "user.email=t@t", "-c", "user.name=t", "commit", "-qm", "x"]):
        subprocess.run(["git", "-C", src] + cmd, check=True,
                       capture_output=True)
    out = os.path.join(tmp, "o8a")
    items, _ = run(src, out)
    paths = {i.path for i in items}
    check("real clone: .env excluded", ".env" not in paths, f"got {sorted(paths)}")
    check("real clone: no .git/", not any(p.startswith(".git/") for p in paths))
    on_disk = os.listdir(os.path.join(out, "sources"))
    check("real clone: nothing secret written",
          not [f for f in on_disk if "env" in f], f"got {on_disk}")

    # (b) a BROKEN checkout must be a hard error, never a silent walk.
    # This is the case the first version of the fix got wrong.
    src = corpus(tmp, {"README.md": "# r\n", ".env": "SECRET=1\n",
                       ".git/config": "[core]\n"}, "f8b")
    try:
        run(src, os.path.join(tmp, "o8b"))
        check("broken .git refuses to walk", False, "fell back silently")
    except SystemExit as exc:
        check("broken .git refuses to walk", "ls-files" in str(exc), str(exc)[:90])

    # (c) an extracted tarball has no .git at all — the deny-list must hold
    src = corpus(tmp, {"README.md": "# r\n", ".env": "SECRET=1\n",
                       "deploy/id_rsa": "-----BEGIN-----\n",
                       "conf/service_account.json": "{}\n"}, "f8c")
    out = os.path.join(tmp, "o8c")
    items, _ = run(src, out)
    paths = {i.path for i in items}
    check("tarball: .env deny-listed", ".env" not in paths, f"got {sorted(paths)}")
    check("tarball: private key deny-listed", "deploy/id_rsa" not in paths)
    check("tarball: service account deny-listed",
          "conf/service_account.json" not in paths)
    check("tarball: real content kept", "README.md" in paths)

    print("F4 (P1) — a native binary must survive byte-for-byte")
    png = b"\x89PNG\r\n\x1a\n\x00\xff\xfe\xfd binary payload"
    src = corpus(tmp, {"a.md": "# a\n", "img/photo.png": png}, "f4")
    out = os.path.join(tmp, "o4")
    run(src, out)
    got = open(os.path.join(out, "sources", "img__photo.png"), "rb").read()
    check("png copied unchanged", got == png, f"{len(got)}B vs {len(png)}B")
    check("png keeps its extension",
          os.path.exists(os.path.join(out, "sources", "img__photo.png")))

    print("F1 (P1) — over the cap must partition, never single-notebook")
    files = {f"g/{i:03d}.md": f"# {i}\n" for i in range(10)}
    files.update({f"h/{i:03d}.md": f"# h{i}\n" for i in range(10)})
    src = corpus(tmp, files, "f1")
    out = os.path.join(tmp, "o1")
    items, nb = run(src, out, cap=8)
    check("partitioned into >1 notebook", nb > 1, f"nb={nb}")
    check("no `sources/` dir when partitioned",
          not os.path.exists(os.path.join(out, "sources")))
    sizes = []
    for d in sorted(os.listdir(out)):
        if d.startswith("notebook-"):
            sizes.append(len(os.listdir(os.path.join(out, d))))
    check("every notebook within cap", all(s <= 8 for s in sizes), f"sizes={sizes}")
    check("no file lost across the split",
          sum(sizes) - nb == 20, f"sizes={sizes} nb={nb}")
    readme = open(os.path.join(out, "README.md"), encoding="utf-8").read()
    check("README stops claiming one notebook", "past in één notebook" not in readme)

    print("F2 (P2) — a flat-name collision must fail explicitly")
    src = corpus(tmp, {"a/b.md": "x\n", "a__b.md": "y\n"}, "f2")
    out = os.path.join(tmp, "o2")
    try:
        run(src, out)
        check("collision raises", False, "build() returned silently")
    except SystemExit as exc:
        check("collision raises", "collision" in str(exc), str(exc)[:80])
    src = corpus(tmp, {"00-INDEX.md": "x\n"}, "f2b")
    try:
        run(src, os.path.join(tmp, "o2b"))
        check("reserved index name raises", False, "returned silently")
    except SystemExit as exc:
        check("reserved index name raises", "reserved" in str(exc), str(exc)[:80])

    print("F3 (P2) — a reused --out must not keep stale sources")
    src = corpus(tmp, {"a.md": "# a\n"}, "f3")
    out = os.path.join(tmp, "o3")
    os.makedirs(os.path.join(out, "sources"), exist_ok=True)
    open(os.path.join(out, "sources", "stale.md"), "w").write("old\n")
    run(src, out)
    check("stale file removed",
          not os.path.exists(os.path.join(out, "sources", "stale.md")))

    print("F5 (P2) — CSS content: strings must not be harvested as prose")
    html_doc = ('<html><head><title>T</title>'
                '<style>.x::before{content:"This interface hint has enough words"}</style>'
                '</head><body><p>Real body text here.</p>'
                '<script>const d=[["S","This is a genuine caption with words"]]</script>'
                '</body></html>')
    src = corpus(tmp, {"p/index.html": html_doc}, "f5")
    out = os.path.join(tmp, "o5")
    run(src, out)
    got = open(os.path.join(out, "sources", "p__index.html.md"), encoding="utf-8").read()
    check("CSS content not harvested", "This interface hint" not in got)
    check("JS caption still harvested", "genuine caption with words" in got)
    check("body text kept", "Real body text here." in got)

    print("F6 (P2) — an embedded ``` must not break out of its fence")
    code = 'x = """\n```\nnot code\n```\n"""\n'
    src = corpus(tmp, {"s.py": code}, "f6")
    out = os.path.join(tmp, "o6")
    run(src, out)
    got = open(os.path.join(out, "sources", "s.py.md"), encoding="utf-8").read()
    body = got.split("---", 1)[1]
    check("fence longer than embedded run", "````" in body, "no 4-backtick fence")
    check("content intact", "not code" in got)

    print("F7 (P2) — the build date must not be hardcoded")
    src = corpus(tmp, {"a.md": "# a\n"}, "f7")
    out = os.path.join(tmp, "o7")
    items, nb = B.build(src, "t", out, "deadbee", B.DEFAULT_CAP)
    B.write_index(out, "t", "deadbee", "2099-12-31", items, nb)
    idx = open(os.path.join(out, "sources", "00-INDEX.md"), encoding="utf-8").read()
    check("index uses the passed date", "2099-12-31" in idx)
    check("no hardcoded 2026-08-23", "2026-08-23" not in idx)
    srctext = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                                "build_notebook_bundle.py"), encoding="utf-8").read()
    check("index writer takes a date param", 'built: str' in srctext)

    print("F9 (P2) — the index must count itself")
    src = corpus(tmp, {f"g/{i}.md": "x\n" for i in range(5)}, "f9")
    out = os.path.join(tmp, "o9")
    run(src, out)
    idx = open(os.path.join(out, "sources", "00-INDEX.md"), encoding="utf-8").read()
    on_disk = len(os.listdir(os.path.join(out, "sources")))
    check("index total == files on disk", f"**{on_disk} bronnen**" in idx,
          f"expected {on_disk}; index says otherwise")

    shutil.rmtree(tmp, ignore_errors=True)
    print()
    if FAILURES:
        print(f"{len(FAILURES)} FAILURE(S):")
        for f in FAILURES:
            print("  -", f)
        return 1
    print("all regressions pass")
    return 0


if __name__ == "__main__":
    sys.exit(main())
