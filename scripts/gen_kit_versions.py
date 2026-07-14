#!/usr/bin/env python3
"""gen_kit_versions.py — fleet kit-version table, generated from TREES.

INC-42 / central-docs-plan C4 (fm PR #185, wake 0434z): one generated table
`registry/kit-versions.md` — repo → pinned (`substrate.config.json
kit_version`) → tree (`.substrate/state.json kit_version`) → drift verdict —
plus the plugin-pin drift check (superbot-plugin-hello's pinned kit vs its
host superbot-next; the 1.13.0-vs-1.15.0 drift was previously found only by
hand). Derivation rules follow the plan's iron rule: read trees, never
heartbeat prose; absence is recorded honestly, never invented.

Provenance/reliability header (Q-0105 posture): added 2026-07-14 by the
failsafe-wake 0434z worker. Unverified: confirm its output against ground
truth a few times across sessions before trusting it. Delete this if it
proves unreliable over multiple sessions.

Usage:
    python3 scripts/gen_kit_versions.py            # write registry/kit-versions.md
    python3 scripts/gen_kit_versions.py --check    # regen + diff committed; exit 2 on drift
    python3 scripts/gen_kit_versions.py --selfcheck
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import tempfile
from datetime import datetime, timezone

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import gen_roster  # noqa: E402  (fetch machinery + LANES; same-writer reuse)

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT_REL = os.path.join("registry", "kit-versions.md")

# Passive repos with no lane row but a kit pin worth tracking, mapped to the
# host repo whose pin they claim to mirror (plugin-hello seed commit:
# "mirroring the host's pin" — the claim INC-42 caught drifting).
PLUGIN_HOSTS = {"superbot-plugin-hello": "superbot-next"}

# Deliberate pins (INC-41) — labeled, never "corrected". Kept in sync with
# gen_roster.DELIBERATE_KIT_PINS (imported, single source).
DELIBERATE = gen_roster.DELIBERATE_KIT_PINS


def repo_list() -> list[str]:
    repos = []
    for lane in gen_roster.LANES:
        r = lane.get("repo")
        if r and r not in repos:
            repos.append(r)
    for r in PLUGIN_HOSTS:
        if r not in repos:
            repos.append(r)
    return repos


def read_kit_versions(repo: str, max_attempts: int = 3) -> dict:
    """Fetch one repo and read its kit-version facts from the TREE."""
    url = gen_roster.GITHUB_BASE + repo
    out: dict = {"repo": repo, "sha": None, "pinned": None, "state": None,
                 "wall": None}
    with tempfile.TemporaryDirectory(prefix="kitver-") as tmp:
        try:
            sha, _ = gen_roster.fetch_verified(url, tmp, max_attempts)
        except gen_roster.Wall as exc:
            out["wall"] = str(exc)
            return out
        out["sha"] = sha
        for path, key in (("substrate.config.json", "pinned"),
                          (".substrate/state.json", "state")):
            try:
                data = json.loads(gen_roster._git(
                    ["show", f"FETCH_HEAD:{path}"], cwd=tmp))
                v = data.get("kit_version")
                if isinstance(v, str) and v:
                    out[key] = v
            except (gen_roster.Wall, json.JSONDecodeError):
                pass  # honest absence
    return out


def _ver_key(v: str) -> tuple:
    return tuple(int(x) for x in re.findall(r"\d+", v)[:3]) or (0,)


def verdict(row: dict, newest: str | None, rows_by_repo: dict) -> str:
    """Drift verdict for one repo row. Pure (selfcheck-pinned)."""
    if row["wall"]:
        return "NOT MEASURED (transport/auth wall)"
    pinned, state = row["pinned"], row["state"]
    if DELIBERATE.get(row["repo"]) == pinned and pinned is not None:
        return "DELIBERATE PIN (INC-41 — never auto-'fix')"
    host = PLUGIN_HOSTS.get(row["repo"])
    if host:
        hrow = rows_by_repo.get(host)
        hpin = (hrow or {}).get("pinned") or (hrow or {}).get("state")
        mine = pinned or state
        if mine and hpin and mine != hpin:
            return (f"PLUGIN-PIN DRIFT — host {host} pins v{hpin} "
                    f"(INC-42: 'mirroring the host's pin' no longer holds)")
        if mine and hpin:
            return f"OK — mirrors host {host} pin"
        return "UNKNOWN (pin unreadable on one side)"
    if pinned is None and state is None:
        return "NO KIT (no substrate.config.json / state.json in tree)"
    if pinned and state and pinned != state:
        return f"SPLIT — config pins v{pinned}, state installed v{state}"
    cur = state or pinned
    if newest and cur and _ver_key(cur) < _ver_key(newest):
        return f"LAGS newest fleet tree (v{newest})"
    return "CURRENT (= newest fleet tree)"


def render(rows: list[dict], date: str) -> str:
    rows_by_repo = {r["repo"]: r for r in rows}
    measured = [r["state"] or r["pinned"] for r in rows
                if (r["state"] or r["pinned"])
                and DELIBERATE.get(r["repo"]) != r["pinned"]
                and r["repo"] not in PLUGIN_HOSTS]
    newest = max(measured, key=_ver_key) if measured else None
    out = [
        "# Fleet kit-version table — GENERATED",
        "",
        "> **Status:** `living-ledger`",
        ">",
        "> **GENERATED — do not hand-edit** (`scripts/gen_kit_versions.py`;"
        " INC-42 / central-docs-plan C4). Regenerate with every manager wake"
        " that touches kit state; kit `docs/adopters.md` stays sole-writer"
        " kit-lab — this table is derived from TREES"
        " (`substrate.config.json` + `.substrate/state.json` at verified"
        " HEADs), never from heartbeat prose (INC-40) and never from the"
        " adopters doc.",
        ">",
        f"> generated-at **{date}** · newest fleet tree version measured:"
        f" **{'v' + newest if newest else 'n/a'}** (proxy for current"
        " release — the kit's own release ledger is kit-owned; this column"
        " is measured, not asserted). Kill-switch: if generated-at goes"
        " stale >7d, re-derive from trees before trusting a row.",
        "",
        "| Repo | Pinned (`substrate.config.json`) | Tree"
        " (`.substrate/state.json`) | Drift verdict | Evidence (HEAD) |",
        "|---|---|---|---|---|",
    ]
    for r in rows:
        pin = f"v{r['pinned']}" if r["pinned"] else "—"
        st = f"v{r['state']}" if r["state"] else "—"
        ev = f"`{r['sha'][:7]}`" if r["sha"] else "(unreadable)"
        out.append(f"| {r['repo']} | {pin} | {st} "
                   f"| {verdict(r, newest, rows_by_repo)} | {ev} |")
    out += [
        "",
        "Notes: DELIBERATE PIN rows are design, not drift (INC-41 —"
        " superbot Q-0254 pin + the kit's owner-held self-pin)."
        " PLUGIN-PIN DRIFT compares a plugin repo's pin to its host's"
        f" ({', '.join(f'{k}→{v}' for k, v in PLUGIN_HOSTS.items())});"
        " the 06023075→ff75b9eb manifest-hash class stays a follow-up"
        " (plan C10 `registry/pins.md`).",
        "",
    ]
    return "\n".join(out)


def selfcheck() -> int:
    fails = []

    def ok(cond, label):
        print(("PASS " if cond else "FAIL ") + label)
        if not cond:
            fails.append(label)

    rows = {
        "superbot-next": {"repo": "superbot-next", "pinned": "1.15.0",
                          "state": "1.15.0", "wall": None},
    }
    ok(verdict({"repo": "superbot", "pinned": "1.0.0", "state": None,
                "wall": None}, "1.15.0", rows)
       .startswith("DELIBERATE PIN"), "deliberate pin labeled")
    ok("PLUGIN-PIN DRIFT" in verdict(
        {"repo": "superbot-plugin-hello", "pinned": "1.13.0", "state": None,
         "wall": None}, "1.15.0", rows), "plugin pin drift flagged vs host")
    ok(verdict({"repo": "superbot-plugin-hello", "pinned": "1.15.0",
                "state": None, "wall": None}, "1.15.0", rows)
       .startswith("OK — mirrors"), "matching plugin pin is OK")
    ok(verdict({"repo": "x", "pinned": None, "state": "1.7.0",
                "wall": None}, "1.15.0", rows)
       .startswith("LAGS"), "older tree lags newest")
    ok(verdict({"repo": "x", "pinned": "1.14.0", "state": "1.15.0",
                "wall": None}, "1.15.0", rows)
       .startswith("SPLIT"), "config/state split flagged")
    ok(verdict({"repo": "x", "pinned": None, "state": None, "wall": None},
               "1.15.0", rows).startswith("NO KIT"), "honest absence")
    ok(verdict({"repo": "x", "pinned": None, "state": None, "wall": "boom"},
               None, rows).startswith("NOT MEASURED"), "wall never guessed")
    ok(_ver_key("1.9.0") < _ver_key("1.15.0"), "numeric version compare")
    print(f"selfcheck: {'PASS' if not fails else 'FAIL'} "
          f"({len(fails)} failure(s))")
    return 0 if not fails else 1


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--selfcheck", action="store_true")
    ap.add_argument("--max-fetch-attempts", type=int, default=3)
    args = ap.parse_args()
    if args.selfcheck:
        return selfcheck()
    rows = []
    for repo in repo_list():
        print(f"[gen_kit_versions] {repo} …", file=sys.stderr)
        rows.append(read_kit_versions(repo, args.max_fetch_attempts))
    date = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%MZ")
    text = render(rows, date)
    out_path = os.path.join(REPO_ROOT, OUT_REL)
    if args.check:
        try:
            committed = open(out_path, encoding="utf-8").read()
        except FileNotFoundError:
            print("check: no committed table", file=sys.stderr)
            return 2
        strip = re.compile(r"^> generated-at .*$", re.MULTILINE)
        if strip.sub("", committed) != strip.sub("", text):
            print("check: DRIFT vs committed table", file=sys.stderr)
            return 2
        print("check: OK", file=sys.stderr)
        return 0
    with open(out_path, "w", encoding="utf-8") as fh:
        fh.write(text)
    print(f"gen_kit_versions: wrote {OUT_REL}", file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())
