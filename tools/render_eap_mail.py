#!/usr/bin/env python3
"""Render the final EAP mail's COPY block into something sendable — and count it.

WHY THIS EXISTS. Two send-day defects, both measured on 2026-08-25 (fm #946).

1. THE BLOCK IS MARKDOWN AND THE MAIL IS NOT. Part 2 carries 29 `**bold**` and
   13 `*italic*` spans, backticked URLs and hard line wraps at ~76 columns.
   (`--count` reports these, because the figure was asserted wrong twice before
   it was computed: first as "~90 bold", then as 83 total — that second one
   reused the asterisks inside `**bold**` as italic delimiters.) Pasted
   into a Gmail compose that is exactly what the recipient sees: literal
   asterisks through a carefully-argued vendor mail, and ragged wrapping that
   re-breaks at whatever width their client uses. Nothing in the draft said so.

2. THE WORD COUNT DRIFTED EVERY TIME IT WAS TOLD. On 2026-08-25 three committed
   places carried three different values for one block — the draft said 2,082,
   `docs/owner-queue.md` said 2,127, the file was 2,151 — and the *method* was
   never stated, so none of them could be checked. The whole one-page decision
   turned on that number.

The fix for a number that goes stale is not another statement of it. It is one
command that recomputes it, which is `--count`. The fix for a format mismatch is
not a second copy of the mail in the repo — that is the append-without-retract
defect this very mail reports — it is a renderer over the single source.

    A check whose failure mode is SILENCE must be shown to fire before its
    silence means anything.

This renderer can fail silently: swallow a paragraph, leave emphasis marks in,
or extract the wrong span. So it ships `--selftest`, which asserts each of those
on a fixture built to contain them.

USAGE
    python3 tools/render_eap_mail.py            # plain text, paragraphs unwrapped
    python3 tools/render_eap_mail.py --html > /tmp/mail.html   # then OPEN IN A
        BROWSER, select all, copy, paste. Pasting the HTML source itself gives
        literal <p> tags. NOTE: no session has tested either output in a real
        mail client — none is reachable from here.
    python3 tools/render_eap_mail.py --count    # the number, with its method
    python3 tools/render_eap_mail.py --eml > mail.eml   # open in a real client to
        SEE the rendering before sending — headers blank, this previews, never sends
    python3 tools/render_eap_mail.py --selftest # prove the renderer fires
"""
from __future__ import annotations
import argparse, html as _html, re, sys
from pathlib import Path

DRAFT = Path(__file__).resolve().parent.parent / "docs/planning/2026-08-24-final-eap-email-draft.md"
START, END = "## COPY FROM HERE", "## COPY TO HERE"


def extract(md: str) -> list[str]:
    """The lines strictly between the COPY markers. Raises if either is missing."""
    lines = md.split("\n")
    try:
        s = next(i for i, l in enumerate(lines) if l.strip() == START)
        e = next(i for i, l in enumerate(lines) if l.strip() == END)
    except StopIteration:
        raise SystemExit(f"render_eap_mail: missing {START!r} or {END!r} marker")
    if e <= s:
        raise SystemExit("render_eap_mail: COPY markers are inverted")
    return lines[s + 1:e]


def blocks(lines: list[str]):
    """Group into (kind, text) blocks: 'ol' (numbered), 'ul' (bulleted), 'para'.

    ORDERED AND UNORDERED ARE DISTINCT KINDS ON PURPOSE. The mail holds both — the
    numbered asks and the bulleted links block — and an earlier version told them
    apart by guessing at the text (`endswith('.md')`), which also advanced the
    ordinal counter for bullets. A fifth link would have renumbered the asks.
    """
    out, buf, kind = [], [], "para"
    def flush():
        if buf:
            out.append((kind, " ".join(x.strip() for x in buf).strip()))
            buf.clear()
    for l in lines:
        if not l.strip():
            flush(); continue
        m = re.match(r"^\s{0,3}(\d+\.|[-+])\s+", l)
        if m:
            flush(); kind = "ol" if m.group(1)[0].isdigit() else "ul"
            buf.append(l[m.end():])
        elif buf and kind in ("ol", "ul"):
            buf.append(l)
        else:
            if not buf: kind = "para"
            buf.append(l)
    flush()
    return out


def strip_marks(t: str) -> str:
    # A LINK KEEPS ITS DESTINATION. Flattening `[label](url)` to `label` makes a
    # descriptive link unusable in a plain-text mail, and `--verify` cannot see
    # the loss because it applies this same transform to both sides of its
    # comparison (`@codex`, fm #946). The COPY block currently holds 0 markdown
    # links, so this changes no present figure — it stops a future one silently
    # losing its URL.
    t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1 (\2)", t)
    t = re.sub(r"\*\*(.+?)\*\*", r"\1", t, flags=re.S)  # bold
    t = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"\1", t, flags=re.S)  # italic
    t = t.replace("`", "")
    return re.sub(r"[ \t]+", " ", t).strip()


def to_text(lines: list[str]) -> str:
    """Plain text: emphasis marks gone, paragraphs unwrapped so the client reflows."""
    parts, n = [], 0
    for kind, t in blocks(lines):
        t = strip_marks(t)
        if kind == "ol":
            n += 1
            parts.append(f"{n}. {t}")
        elif kind == "ul":
            # a visible glyph, not bare indentation — otherwise the links block
            # reads as four unrelated paragraphs. Punctuation-only tokens are
            # excluded from count(), so this moves no figure.
            parts.append(f"- {t}")
        else:
            n = 0
            parts.append(t)
    return "\n\n".join(parts) + "\n"


def to_html(lines: list[str]) -> str:
    def inline(t: str) -> str:
        t = _html.escape(t)
        t = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', t)
        t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t, flags=re.S)
        t = re.sub(r"(?<!\w)\*(.+?)\*(?!\w)", r"<em>\1</em>", t, flags=re.S)
        return t.replace("`", "")
    out, open_tag = [], None
    for kind, t in blocks(lines):
        if kind in ("ol", "ul"):
            if open_tag != kind:
                if open_tag: out.append(f"</{open_tag}>")
                out.append(f"<{kind}>"); open_tag = kind
            out.append(f"  <li>{inline(t)}</li>")
        else:
            if open_tag: out.append(f"</{open_tag}>"); open_tag = None
            out.append(f"<p>{inline(t)}</p>")
    if open_tag: out.append(f"</{open_tag}>")
    body = "\n".join(out)
    # A COMPLETE DOCUMENT, not fragments. You cannot paste HTML SOURCE into a
    # Gmail compose and get formatting — you get literal <p> tags, which is worse
    # than the asterisks this mode exists to avoid. The only route that works is
    # to render it first: write this to a .html file, open it in a browser,
    # select all, copy, and paste THAT into the compose window.
    return (
        "<!doctype html>\n<html><head><meta charset=\"utf-8\">\n"
        "<title>EAP final review — Part 2</title>\n"
        "<style>body{font:16px/1.55 -apple-system,Segoe UI,Roboto,sans-serif;"
        "max-width:44em;margin:2em auto;padding:0 1em}li{margin:.6em 0}</style>\n"
        "</head><body>\n" + body + "\n</body></html>\n"
    )


def to_eml(lines: list[str], subject: str) -> str:
    """A real multipart/alternative message: plain text AND html, one file.

    WHY. "How will a mail client treat this?" was called untestable here on
    2026-08-25 without anything being tried. It is not: an `.eml` opens in Gmail
    (drag into the compose window or import), Thunderbird, Apple Mail and Outlook,
    so the owner can SEE the rendering the recipient gets before he sends —
    which no amount of reasoning about the markup establishes. Headers are
    deliberately left blank: this is a preview artifact, not a sending path.
    """
    from email.message import EmailMessage
    m = EmailMessage()
    m["Subject"] = subject
    m.set_content(to_text(lines))
    m.add_alternative(to_html(lines), subtype="html")
    return m.as_string()


def count(lines: list[str]) -> dict:
    """Count the artifact that is actually pasted, not the markdown that stores it.

    THE DEFINITION, because two defensible-looking ones disagreed by 12 words on
    2026-08-25 and neither was right:
      * substituting a SPACE for each emphasis mark splits `**fortnight**,` into
        `fortnight` + `,` and counts the bare comma as a word (+8 here);
      * deleting the marks instead leaves the links block's `-` bullet markers
        standing as words (+4 here).
    Neither punctuation nor a bullet glyph is a word. So: render to the plain
    text that goes in the mail, then count tokens carrying at least one
    alphanumeric character. `markdown_tokens` is kept only so the gap between
    the stored form and the sent form stays visible.
    """
    body = to_text(lines)
    raw = "\n".join(lines)
    bold = re.findall(r"\*\*.+?\*\*", raw, flags=re.S)
    # count italics only AFTER bold is removed, and forbid a match spanning another
    # asterisk — otherwise the `*` inside `**bold**` gets reused as an italic
    # delimiter and the total roughly doubles. That error was made twice here.
    ital = re.findall(r"(?<!\w)\*(?!\*)[^*]+?\*(?!\w)", re.sub(r"\*\*.+?\*\*", " ", raw, flags=re.S))
    return {"mail": sum(1 for w in body.split() if re.search(r"[A-Za-z0-9]", w)),
            "markdown_tokens": len(raw.split()),
            "bold": len(bold), "italic": len(ital),
            "residual_marks": sum(body.count(c) for c in "*`_")}


FIXTURE = f"""preamble that must not appear
{START}
To the team,

**Finding 1 — a bold lead.** Text that is hard-wrapped
across two source lines.

1. **An ask.** *Because* of `a reason`.
2. **A second ask.** See [the pack](../x.md).

Everything above is public:
- A link line: example.com/a
- A second link line: example.com/b
{END}
trailing text that must not appear
"""


def selftest() -> int:
    lines = extract(FIXTURE)
    txt, htm = to_text(lines), to_html(lines)
    fails = []
    # 1. extraction is bounded by the markers
    if "preamble" in txt or "trailing" in txt:
        fails.append("extract() leaked text from outside the COPY markers")
    # 2. nothing is swallowed
    for probe in ("To the team,", "a bold lead", "An ask", "A second ask"):
        if probe not in txt:
            fails.append(f"to_text() dropped {probe!r}")
    # 3. emphasis marks really are gone from the plain rendering
    for mark in ("**", "`"):
        if mark in txt:
            fails.append(f"to_text() left {mark!r} in the output")
    # 3b. SINGLE-asterisk emphasis too — the loop above passes while `*Because*`
    # renders literally, which is the exact thing this mode exists to prevent.
    if "*" in txt:
        fails.append("to_text() left a single-asterisk emphasis mark in the output")
    if "Because" not in txt:
        fails.append("to_text() destroyed italic content instead of unwrapping it")
    # 3c. a link must arrive with its destination, not just its label
    if "the pack (../x.md)" not in txt:
        fails.append("to_text() dropped a link destination")
    # 4. hard wraps are unwrapped so the mail client can reflow
    if "hard-wrapped across two source lines" not in txt:
        fails.append("to_text() kept the source's hard line wrap")
    # 5. list numbering survives
    if "1. An ask." not in txt or "2. A second ask." not in txt:
        fails.append("to_text() lost list numbering")
    # 5b. bullets must NOT consume ordinals, and must not be numbered themselves
    if "3. A link line" in txt or "1. A link line" in txt:
        fails.append("to_text() numbered a bulleted item")
    if "- A link line: example.com/a" not in txt:
        fails.append("to_text() lost the bulleted links block")
    if "<ul>" not in htm or htm.count("<ol>") != 1:
        fails.append("to_html() did not separate the ordered and unordered lists")
    # 6. the html path keeps what the text path removes
    if "<strong>" not in htm or "<ol>" not in htm or '<a href="../x.md">' not in htm:
        fails.append("to_html() lost bold, list or link structure")
    # 7. the count excludes what is not a word — the defect that produced the drift
    c = count(lines)
    if c["mail"] <= 0:
        fails.append(f"count() returned no words: {c}")
    if c["mail"] >= c["markdown_tokens"]:
        fails.append("count() is not excluding markdown-only tokens: "
                     f"mail={c['mail']} markdown={c['markdown_tokens']}")
    if any(re.fullmatch(r"[^A-Za-z0-9]+", w) for w in to_text(lines).split()
           if w not in ("—",)) and c["mail"] == len(to_text(lines).split()):
        fails.append("count() counted a bare-punctuation token as a word")
    for f in fails:
        print(f"selftest FAIL: {f}", file=sys.stderr)
    print(f"selftest: {13 - len(fails)}/13 assertions passed"
          + ("" if fails else " — renderer demonstrated to fire"))
    return 1 if fails else 0


def verify(lines: list[str]) -> int:
    """Assert the rendering drops nothing and invents nothing.

    The selftest proves the renderer works on a FIXTURE. This proves it on the
    actual mail, which is the thing that gets pasted: a silently swallowed
    paragraph would send the vendor a truncated argument and nothing would say so.

    ITS LANE, stated because the two checks are complementary and neither is
    complete alone (measured 2026-08-25 by mutating this file in place):
      * `--verify` is a CONTENT check. Dropping a paragraph and inventing a word
        are both caught. A formatting-only regression is NOT caught and should
        not be — the words are all still there.
      * `--selftest` is a MECHANISM check and covers formatting: routing the
        links block through the paragraph branch leaves the word count identical,
        so `--verify` passes it at exit 0 while `--selftest` fails it 9/10.
    Run both. (The mutation harness needs the mutant to live in `tools/` — a copy
    under /tmp dies on FileNotFoundError resolving DRAFT, which exits 1 and reads
    as a catch when nothing was caught. That false pass happened here first.)
    """
    words = lambda s: [w for w in re.sub(r"\s+", " ", s).split() if re.search(r"[A-Za-z0-9]", w)]
    a, b = words(strip_marks("\n".join(lines))), words(to_text(lines))
    import difflib
    ops = difflib.SequenceMatcher(None, a, b).get_opcodes()
    dropped = [w for op, i1, i2, _, _ in ops if op in ("delete", "replace") for w in a[i1:i2]]
    added = [w for op, _, _, j1, j2 in ops if op in ("insert", "replace") for w in b[j1:j2]]
    print(f"source words {len(a)} -> rendered words {len(b)}")
    if dropped: print(f"DROPPED in rendering: {dropped}", file=sys.stderr)
    if added:   print(f"INTRODUCED by rendering: {added}", file=sys.stderr)
    if dropped or added:
        return 1
    print("verify: rendering is loss-free — nothing dropped, nothing introduced")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    # MUTUALLY EXCLUSIVE. `--html --count > mail.html` used to exit 0 and write
    # the count report into the file the owner then opens and pastes from
    # (`@codex`, fm #946). Silent precedence between output modes is how you send
    # the wrong artifact.
    mode = ap.add_mutually_exclusive_group()
    mode.add_argument("--html", action="store_true",
                      help="complete HTML document; open in a browser and copy from there, "
                           "do not paste the source")
    mode.add_argument("--count", action="store_true", help="word count, with its method")
    mode.add_argument("--verify", action="store_true",
                      help="assert the real mail renders loss-free (nothing dropped or invented)")
    mode.add_argument("--eml", action="store_true",
                      help="a .eml preview (plain + html); open it in a real mail client "
                           "to see what the recipient sees")
    mode.add_argument("--selftest", action="store_true", help="prove the renderer fires")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    lines = extract(DRAFT.read_text(encoding="utf-8"))
    if a.verify:
        return verify(lines)
    if a.count:
        c = count(lines)
        print(f"Part 2, measured on {DRAFT.name} between the COPY markers:")
        print(f"  {c['mail']:>5}  WORDS IN THE MAIL  <- quote this one; every figure in the draft uses it")
        print(f"  {c['markdown_tokens']:>5}  tokens in the markdown that stores it (not the mail)")
        print(f"  emphasis in source: {c['bold']} bold + {c['italic']} italic = "
              f"{c['bold']+c['italic']} spans, ALL removed by the plain-text route")
        print(f"  residual markdown marks in the plain-text output: {c['residual_marks']} "
              f"({'clean' if not c['residual_marks'] else 'LEAK — investigate'})")
        return 0
    if a.eml:
        sys.stdout.write(to_eml(lines, "Claude Code Projects EAP — the final review, one month on"))
        return 0
    sys.stdout.write(to_html(lines) if a.html else to_text(lines))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
