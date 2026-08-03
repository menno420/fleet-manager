#!/usr/bin/env python3
"""Read a shared AI chat transcript (Gemini, ChatGPT) with headless Chromium.

Shared-chat pages are client-rendered single-page apps. Plain HTTP returns the
app shell with no conversation in it, and a fetcher that follows the share
redirect hits an oversized response header. A real browser is the only thing
that works, and in this container it needs three fixes that are not defaults —
see docs/conventions/reading-shared-ai-chats.md for why each one is needed.

    python3 tools/read_shared_chat.py --setup
    python3 tools/read_shared_chat.py <url> [-o out.txt] [--wait 8]

`--setup` is idempotent and needs root; run it once per container.
"""

from __future__ import annotations

import argparse
import pathlib
import subprocess
import sys
import time

CHROMIUM = "/opt/pw-browsers/chromium"
CA_BUNDLE = pathlib.Path("/root/.ccr/ca-bundle.crt")
NSSDB = pathlib.Path("/root/.pki/nssdb")

BEGIN = "-----BEGIN CERTIFICATE-----"
END = "-----END CERTIFICATE-----"


def _run(command: list[str], **kwargs) -> subprocess.CompletedProcess:
    """Run a command and return it; never pipe, so the exit code stays real."""
    return subprocess.run(command, capture_output=True, text=True, **kwargs)


def _split_bundle(text: str) -> list[str]:
    certs: list[str] = []
    current: list[str] = []
    inside = False
    for line in text.splitlines(True):
        if line.startswith(BEGIN):
            inside, current = True, [line]
        elif line.startswith(END) and inside:
            current.append(line)
            certs.append("".join(current))
            inside = False
        elif inside:
            current.append(line)
    return certs


def setup(scratch: pathlib.Path) -> int:
    """Install the browser's TLS trust. Idempotent; requires root."""
    if not CA_BUNDLE.is_file():
        print(f"no CA bundle at {CA_BUNDLE}; nothing to import", file=sys.stderr)
        return 1

    if _run(["which", "certutil"]).returncode != 0:
        print("installing libnss3-tools…")
        if _run(["apt-get", "update", "-qq"]).returncode != 0:
            print("apt-get update failed", file=sys.stderr)
            return 1
        installed = _run(["apt-get", "install", "-y", "-qq", "libnss3-tools"])
        if installed.returncode != 0:
            print(installed.stderr.strip() or "apt-get install failed", file=sys.stderr)
            return 1

    NSSDB.mkdir(parents=True, exist_ok=True)
    if not (NSSDB / "cert9.db").exists():
        created = _run(
            ["certutil", "-N", "-d", f"sql:{NSSDB}", "--empty-password"])
        if created.returncode != 0:
            print(created.stderr.strip() or "certutil -N failed", file=sys.stderr)
            return 1

    certs = _split_bundle(CA_BUNDLE.read_text(encoding="utf-8", errors="replace"))
    if not certs:
        print(f"{CA_BUNDLE} held no PEM certificates", file=sys.stderr)
        return 1

    scratch.mkdir(parents=True, exist_ok=True)
    imported = 0
    for index, pem in enumerate(certs):
        path = scratch / f"ca-{index:03d}.pem"
        path.write_text(pem)
        added = _run([
            "certutil", "-A", "-d", f"sql:{NSSDB}",
            "-t", "C,,", "-n", f"ccr-ca-{index}", "-i", str(path),
        ])
        if added.returncode == 0:
            imported += 1
        else:
            print(f"cert {index}: {added.stderr.strip()}", file=sys.stderr)

    print(f"imported {imported}/{len(certs)} certificates into {NSSDB}")
    return 0 if imported else 1


def read_share(url: str, wait_seconds: float, selector: str) -> str:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        print("playwright is not installed: pip install playwright", file=sys.stderr)
        print("(do NOT run 'playwright install' — the browser is already here)",
              file=sys.stderr)
        raise SystemExit(1)

    with sync_playwright() as driver:
        browser = driver.chromium.launch(
            # pip's playwright looks for its own build; point it at the one
            # this container ships.
            executable_path=CHROMIUM,
            headless=True,
            # The agent proxy resets these connections; the browser has to go
            # direct. TLS verification stays on — that is what --setup is for.
            args=["--no-proxy-server", "--no-sandbox"],
        )
        try:
            page = browser.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=90_000)
            # The transcript arrives after hydration; there is no load event
            # that means "the conversation is on the page".
            time.sleep(wait_seconds)
            return page.inner_text(selector)
        finally:
            browser.close()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("url", nargs="?", help="share URL to read")
    parser.add_argument("-o", "--out", help="write the transcript here")
    parser.add_argument("--wait", type=float, default=8.0,
                        help="seconds to wait after DOM ready (default 8)")
    parser.add_argument("--selector", default="body",
                        help="element to extract text from (default body)")
    parser.add_argument("--setup", action="store_true",
                        help="install browser TLS trust, then exit")
    parser.add_argument("--scratch", default="/tmp/read-shared-chat",
                        help="scratch directory for split certificates")
    args = parser.parse_args()

    if args.setup:
        return setup(pathlib.Path(args.scratch))

    if not args.url:
        parser.error("a URL is required unless --setup is given")

    text = read_share(args.url, args.wait, args.selector)
    if args.out:
        pathlib.Path(args.out).write_text(text, encoding="utf-8")
        print(f"chars={len(text)} written={args.out}")
    else:
        print(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
