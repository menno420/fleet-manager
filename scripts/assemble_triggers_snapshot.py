#!/usr/bin/env python3
"""assemble_triggers_snapshot.py — one-command R26 trigger-snapshot assembler.

================================ PROVENANCE ================================
Why added : PR #253's recorded session idea (session card
            .sessions/2026-07-16-fm-wake-jul16.md, ender 💡): the R26 wake
            export was ~20 hand-driven list_triggers MCP paginations plus an
            ad-hoc assembly script re-written from scratch each wake
            (dedupe, prior-diff, capture_notes grammar). This script makes
            the assembly step deterministic: feed it the raw page-dump JSON
            files verbatim as captured, get the committed snapshot shape
            that gen_roster.validate_export / check_trigger_health.py
            consume, with the capture_notes grammar uniform across wakes.
            It FAILS LOUDLY on partial pagination (a supplied final page
            still advertising has_more / next_cursor, or zero records) —
            a silently-partial snapshot is exactly the flying-blind class
            R26 exists to prevent.
Date      : 2026-07-16 (R26 maintenance wake, model: fable-5;
            fleet-manager PR #255)
Reliability: unverified — confirm its output against ground truth a few
            times across sessions before trusting it.
            Proof run 1 (2026-07-16, PR #255): assembled the 20-page
            01:44-01:49Z live export (1964 records after 0 in-page
            duplicates, 17 enabled) and the result passed
            gen_roster.validate_export + fed check_trigger_health.py
            directly; verdict in the PR #255 session card.
Kill-switch: delete this if it proves unreliable over multiple sessions.
=============================================================================

WHAT IT DOES
  1. Reads one or more RAW paginated `list_triggers` page dumps — the tool
     result JSON saved verbatim, shape {"data": [...], "has_more": bool,
     "next_cursor": "..."} (the terminal page carries only "data") — from
     argv paths in pagination order, or from stdin (a single page object,
     or a JSON array of page objects).
  2. Fails loudly (exit 1, clear message) when the export is PARTIAL:
     the last supplied page still advertises has_more / a next_cursor
     (a subsequent page exists but was not supplied), or zero trigger
     records parsed.
  3. Dedupes records by id (first occurrence wins — cursor-overlap
     duplicates across page boundaries are dropped and counted).
  4. Diffs ids against the prior committed snapshot (+new / -gone).
  5. Writes the snapshot the health tooling consumes:
     {"capture_notes": [...], "captured_at": "...Z", "data": [...]},
     validated through gen_roster.validate_export before writing so a
     malformed assembly can never land as the committed snapshot.

WAKE PROCEDURE (playbook R26): save every list_triggers page verbatim →
  python3 scripts/assemble_triggers_snapshot.py pages/page-*.json →
  python3 scripts/check_trigger_health.py → act on FAILs same wake.

USAGE
  python3 scripts/assemble_triggers_snapshot.py page-01.json page-02.json ...
  cat pages.json | python3 scripts/assemble_triggers_snapshot.py -
  python3 scripts/assemble_triggers_snapshot.py pages/*.json \
      --captured-at 2026-07-16T01:49:00Z --note "extra capture caveat..."
  python3 scripts/assemble_triggers_snapshot.py --selfcheck

No third-party deps: stdlib + this repo's gen_roster (schema validator).
"""

from __future__ import annotations

import argparse
import io
import json
import os
import sys
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import gen_roster  # noqa: E402  (sibling module, validate_export / repo_root)


class AssemblyError(Exception):
    """A page set that must not become the committed snapshot."""


def parse_captured_at(value: str | None) -> str:
    """Normalize the capture instant to `%Y-%m-%dT%H:%M:%SZ` (UTC).

    Accepts any ISO-8601 UTC form gen_roster.parse_when understands;
    defaults to UTC now. Raises AssemblyError on an unparseable value —
    a snapshot with a bad captured_at poisons every I6 freshness verdict.
    """
    if value is None:
        return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    dt = gen_roster.parse_when(value)
    if dt is None:
        raise AssemblyError(f"cannot parse --captured-at {value!r} "
                            "(expected ISO UTC, e.g. 2026-07-16T01:49:00Z)")
    return dt.strftime("%Y-%m-%dT%H:%M:%SZ")


def coerce_pages(obj, source: str) -> list[dict]:
    """Coerce one parsed JSON document into a list of page dicts.

    A document is either a single page ({"data": [...], ...}) or an array
    of pages. Anything else is a loud failure — never guess at a shape.
    """
    if isinstance(obj, dict):
        pages = [obj]
    elif isinstance(obj, list):
        pages = obj
    else:
        raise AssemblyError(f"{source}: top level must be a page object or "
                            f"an array of pages; got {type(obj).__name__}")
    for i, page in enumerate(pages):
        if not isinstance(page, dict) or not isinstance(page.get("data"), list):
            raise AssemblyError(
                f"{source} page[{i}]: not a list_triggers page dump — "
                f"expected a dict with a 'data' list (found "
                f"{sorted(page.keys()) if isinstance(page, dict) else type(page).__name__}); "
                "save the tool result verbatim, don't hand-edit it")
    return pages


def load_pages(paths: list[str], stdin: io.TextIOBase) -> list[tuple[str, dict]]:
    """Load pages from argv paths (pagination order) or stdin ('-'/empty)."""
    labeled: list[tuple[str, dict]] = []
    if not paths or paths == ["-"]:
        source = "stdin"
        try:
            obj = json.load(stdin)
        except json.JSONDecodeError as exc:
            raise AssemblyError(f"{source}: invalid JSON: {exc}")
        labeled.extend((source, p) for p in coerce_pages(obj, source))
    else:
        for path in paths:
            try:
                with open(path, encoding="utf-8") as fh:
                    obj = json.load(fh)
            except (OSError, json.JSONDecodeError) as exc:
                raise AssemblyError(f"{path}: cannot read page dump: {exc}")
            labeled.extend((path, p) for p in coerce_pages(obj, path))
    if not labeled:
        raise AssemblyError("no pages supplied — nothing to assemble")
    return labeled


def check_exhaustion(pages: list[tuple[str, dict]]) -> None:
    """PARTIAL-PAGINATION guard — the loud-failure heart of this script.

    The pages are supplied in pagination order; the LAST one must be
    terminal (no truthy has_more, no non-empty next_cursor — the live API
    omits both keys entirely on the final page). A non-terminal last page
    means at least one subsequent page exists that was never captured:
    the snapshot would silently under-count the registry.
    """
    source, last = pages[-1]
    if last.get("has_more") or last.get("next_cursor"):
        raise AssemblyError(
            f"PARTIAL PAGINATION: the last supplied page ({source}) still "
            f"advertises has_more={last.get('has_more')!r} / next_cursor="
            f"{str(last.get('next_cursor'))[:24]!r}… — at least one further "
            "page was never captured. Re-run list_triggers from that cursor "
            "to exhaustion and supply ALL pages; a partial snapshot must "
            "never be committed (R26 flying-blind class).")


def assemble(pages: list[tuple[str, dict]]) -> tuple[list[dict], int]:
    """Dedupe by id across pages (first wins). Returns (records, dropped)."""
    seen: set[str] = set()
    records: list[dict] = []
    dropped = 0
    for source, page in pages:
        for i, rec in enumerate(page["data"]):
            if not isinstance(rec, dict) or not isinstance(rec.get("id"), str):
                raise AssemblyError(f"{source} data[{i}]: record without a "
                                    "string 'id' — not a list_triggers dump")
            if rec["id"] in seen:
                dropped += 1
                continue
            seen.add(rec["id"])
            records.append(rec)
    if not records:
        raise AssemblyError("ZERO trigger records parsed — refusing to write "
                            "an empty snapshot (a real registry sweep has "
                            "hundreds; this smells like a bad export)")
    return records, dropped


def prior_ids(prior_path: str) -> tuple[set[str], str] | None:
    """(ids, captured_at) of the prior snapshot, or None when unreadable."""
    try:
        with open(prior_path, encoding="utf-8") as fh:
            prior = json.load(fh)
        data = prior["data"]
        return ({r["id"] for r in data if isinstance(r, dict) and "id" in r},
                str(prior.get("captured_at", "unknown")))
    except (OSError, json.JSONDecodeError, KeyError, TypeError):
        return None


def build_payload(pages: list[tuple[str, dict]], captured_at: str,
                  prior: tuple[set[str], str] | None,
                  extra_notes: list[str]) -> dict:
    """Assemble + validate the snapshot payload (raises AssemblyError)."""
    check_exhaustion(pages)
    records, dropped = assemble(pages)
    enabled = sum(1 for r in records if r.get("enabled"))
    diff = ""
    if prior is not None:
        ids = {r["id"] for r in records}
        p_ids, p_stamp = prior
        diff = (f"; +{len(ids - p_ids)} new / -{len(p_ids - ids)} gone "
                f"vs the prior {p_stamp} capture")
    note = (f"Capture {captured_at} is a FULL list_triggers export "
            f"({len(pages)} pages, cursor-to-exhaustion; {len(records)} "
            f"records after {dropped} cursor-overlap duplicate(s) dropped"
            f"{diff}; {enabled} with enabled=true). Assembled by "
            f"scripts/assemble_triggers_snapshot.py; read-only export — no "
            f"trigger was created, modified, fired, or deleted.")
    payload = {"capture_notes": [note] + extra_notes,
               "captured_at": captured_at, "data": records}
    try:
        gen_roster.validate_export(payload)  # never land a malformed snapshot
    except gen_roster.SchemaError as exc:
        raise AssemblyError(f"assembled snapshot fails the roster schema — "
                            f"refusing to write it: {exc}")
    return payload


def selfcheck() -> int:
    """Offline assertions over the assembly wiring. Exit 0 on pass."""
    fails: list[str] = []

    def ok(cond, msg):
        if not cond:
            fails.append(msg)

    def err_of(fn):
        try:
            fn()
        except AssemblyError as exc:
            return str(exc)
        return None

    rec = {"id": "trig_a", "name": "n", "created_at": "2026-07-16T00:00:00Z",
           "enabled": True, "cron_expression": "30 */2 * * *"}
    rec_b = dict(rec, id="trig_b", enabled=False)
    page1 = {"data": [rec], "has_more": True, "next_cursor": "abc"}
    page2 = {"data": [rec_b]}  # terminal page: no has_more/next_cursor

    payload = build_payload([("p1", page1), ("p2", page2)],
                            "2026-07-16T01:49:00Z", None, [])
    ok(payload["captured_at"] == "2026-07-16T01:49:00Z",
       "captured_at stamps the payload")
    ok([r["id"] for r in payload["data"]] == ["trig_a", "trig_b"],
       "records concatenate in page order")
    ok("2 pages" in payload["capture_notes"][0]
       and "2 records" in payload["capture_notes"][0]
       and "1 with enabled=true" in payload["capture_notes"][0],
       "capture note carries page/record/enabled counts")

    e = err_of(lambda: build_payload([("p1", page1)], "2026-07-16T01:49:00Z",
                                     None, []))
    ok(e and "PARTIAL PAGINATION" in e,
       "non-terminal last page fails loudly (has_more with no next page)")
    e = err_of(lambda: build_payload(
        [("p1", {"data": [], "has_more": False})],
        "2026-07-16T01:49:00Z", None, []))
    ok(e and "ZERO trigger records" in e, "zero records fails loudly")

    dup = build_payload([("p1", page1), ("p2", {"data": [rec, rec_b]})],
                        "2026-07-16T01:49:00Z", None, [])
    ok(len(dup["data"]) == 2 and "1 cursor-overlap duplicate(s) dropped"
       in dup["capture_notes"][0],
       "cursor-overlap duplicate is dropped and counted")

    prior = ({"trig_a", "trig_gone"}, "2026-07-15T21:48Z")
    diffed = build_payload([("p2", {"data": [rec, rec_b]})],
                           "2026-07-16T01:49:00Z", prior, ["extra note"])
    ok("+1 new / -1 gone vs the prior 2026-07-15T21:48Z capture"
       in diffed["capture_notes"][0], "prior diff counts +new/-gone by id")
    ok(diffed["capture_notes"][1] == "extra note",
       "--note text rides as an additional capture note")

    e = err_of(lambda: build_payload(
        [("p1", {"data": [{"name": "no id"}]})],
        "2026-07-16T01:49:00Z", None, []))
    ok(e and "'id'" in e, "record without an id fails loudly")
    e = err_of(lambda: coerce_pages("not a page", "s") and None)
    ok(e and "page object" in e, "non-dict/list document fails loudly")
    e = err_of(lambda: coerce_pages([{"rows": []}], "s") and None)
    ok(e and "'data' list" in e, "page without a data list fails loudly")
    e = err_of(lambda: parse_captured_at("yesterday-ish"))
    ok(e and "cannot parse" in e, "bad --captured-at fails loudly")
    ok(parse_captured_at("2026-07-16T01:49:00Z") == "2026-07-16T01:49:00Z",
       "ISO captured_at normalizes round-trip")
    e = err_of(lambda: build_payload(
        [("p1", {"data": [{"id": "not-a-trigger", "name": "n",
                           "created_at": "t"}]})],
        "2026-07-16T01:49:00Z", None, []))
    ok(e and "roster schema" in e,
       "schema-invalid assembly is refused (validate_export gate)")

    stdin_pages = load_pages([], io.StringIO(json.dumps([page1, page2])))
    ok(len(stdin_pages) == 2 and stdin_pages[0][0] == "stdin",
       "stdin accepts a JSON array of pages")

    for msg in fails:
        print(f"SELFCHECK FAIL: {msg}", file=sys.stderr)
    print(f"selfcheck: {'FAIL' if fails else 'PASS'} ({len(fails)} failure(s))")
    return 1 if fails else 0


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    default_out = os.path.join(gen_roster.repo_root(), "telemetry",
                               "triggers-snapshot.json")
    ap.add_argument("pages", nargs="*",
                    help="raw list_triggers page-dump JSON files in "
                    "pagination order ('-' or none = read stdin)")
    ap.add_argument("--out", default=default_out,
                    help="snapshot path to write (default: the committed "
                    "telemetry/triggers-snapshot.json)")
    ap.add_argument("--prior", default=None,
                    help="prior snapshot for the +new/-gone diff (default: "
                    "the --out path's current content, when readable)")
    ap.add_argument("--captured-at", default=None,
                    help="ISO UTC capture instant (default: UTC now — pass "
                    "the export time when assembling later)")
    ap.add_argument("--note", action="append", default=[],
                    help="extra capture note (repeatable; e.g. a capture "
                    "caveat about an in-flight cutover)")
    ap.add_argument("--selfcheck", action="store_true",
                    help="run offline assertions and exit")
    args = ap.parse_args(argv)

    if args.selfcheck:
        return selfcheck()

    try:
        captured_at = parse_captured_at(args.captured_at)
        pages = load_pages(args.pages, sys.stdin)
        prior = prior_ids(args.prior or args.out)
        payload = build_payload(pages, captured_at, prior, list(args.note))
    except AssemblyError as exc:
        print(f"ASSEMBLY: RED — {exc}", file=sys.stderr)
        return 1

    with open(args.out, "w", encoding="utf-8") as fh:
        json.dump(payload, fh, ensure_ascii=False)
        fh.write("\n")
    enabled = sum(1 for r in payload["data"] if r.get("enabled"))
    print(f"ASSEMBLY: OK — wrote {args.out}: {len(payload['data'])} records "
          f"({enabled} enabled, {len(payload['data']) - enabled} disabled/"
          f"other) from {len(pages)} page(s), captured_at {captured_at}")
    print(f"  note: {payload['capture_notes'][0]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
