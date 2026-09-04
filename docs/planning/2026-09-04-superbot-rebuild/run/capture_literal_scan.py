#!/usr/bin/env python3
"""Instrument: find module-level literals in superbot-next's sb/domain that
stand in for LIVE SYSTEM STATE (the capture-world-literal defect class).

Signature hunted (from the 2026-08-05 audit's own definition):
    "static data presented as live system state"
i.e. a module-level collection/scalar literal naming the PROGRAM's own
inventory, roster, count or status — as opposed to game/world data, which is
legitimately constant.

Two independent detectors, deliberately kept separate so a hit says which
fired:
  D1  name-shaped : module-level literal whose NAME matches a self-describing
                    inventory/roster/status/count concept
  D2  label-shaped: the file carries the repo's own CAPTURE-WORLD LITERAL /
                    "capture world" / "honest successor" marker
D2 is the audit's method (grep a label) and is known-incomplete; D1 is the
sweep the audit named in its § 6 and never ran.
"""
import ast, re, sys, os, json, collections

# D1: names that describe the PROGRAM's own state, not the game world.
SELF_STATE_NAME = re.compile(
    r"(?ix)^_?("
    r"cogs?|modules?|extensions?|subsystems?|plugins?|"
    r"commands?|cmds?|command_(names?|list|catalog(ue)?)|"
    r"flags?|feature_flags?|flag_catalog(ue)?|"
    r"registry|registries|roster|inventory_of|manifest_(names?|list)|"
    r"loaded|installed|available|enabled_(subsystems?|modules?|features?)|"
    r"status(es)?|health_(rows?|lines?)|"
    r"(total|count|num|n)_[a-z_]*|[a-z_]*_(count|total|totals)|"
    r"services?|tables?|stores?|"
    r"panel_(ids?|names?)|route_(table|map)"
    r")$"
)
LITERAL_NODES = (ast.Tuple, ast.List, ast.Set, ast.Dict, ast.Constant)
LABEL = re.compile(r"CAPTURE-WORLD LITERAL|capture world|capture-world|honest successor|successor read", re.I)

def is_literal(node):
    """True when the RHS is a pure literal (no calls, no names, no comprehensions)."""
    for n in ast.walk(node):
        if isinstance(n, (ast.Call, ast.Name, ast.Attribute, ast.comprehension,
                          ast.ListComp, ast.DictComp, ast.SetComp, ast.GeneratorExp,
                          ast.Lambda, ast.Await)):
            return False
    return isinstance(node, LITERAL_NODES) or isinstance(node, ast.BinOp)

def scan_file(path):
    try:
        src = open(path, encoding="utf-8", errors="replace").read()
    except OSError:
        return []
    hits = []
    labelled = bool(LABEL.search(src))
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []
    for node in tree.body:                       # MODULE LEVEL ONLY
        targets = []
        if isinstance(node, ast.Assign):
            targets = [t.id for t in node.targets if isinstance(t, ast.Name)]
            value = node.value
        elif isinstance(node, ast.AnnAssign) and isinstance(node.target, ast.Name):
            targets = [node.target.id]; value = node.value
        else:
            continue
        if value is None or not is_literal(value):
            continue
        size = len(getattr(value, "elts", getattr(value, "keys", [])) or [])
        for name in targets:
            if SELF_STATE_NAME.match(name):
                hits.append({"path": path, "line": node.lineno, "name": name,
                             "detector": "D1_name", "size": size, "labelled": labelled})
    if labelled:
        for m in LABEL.finditer(src):
            hits.append({"path": path, "line": src[:m.start()].count("\n") + 1,
                         "name": m.group(0), "detector": "D2_label", "size": 0,
                         "labelled": True})
    return hits

# ---- positive / negative controls, run before any corpus sweep -------------
POSITIVE_SRC = [
 ('_COGS: tuple[str, ...] = ("admin_cog", "ai_cog", "xp_cog")',      "D1_name"),
 ('COMMAND_NAMES = ["help", "ping", "setup"]',                        "D1_name"),
 ('SUBSYSTEMS = {"admin": 1, "ai": 2}',                               "D1_name"),
 ('TOTAL_LOADED = 58',                                                "D1_name"),
 ('# CAPTURE-WORLD LITERAL (trap 10a): the shipped description\nX = 1',"D2_label"),
]
NEGATIVE_SRC = [
 'WEATHER_TABLE = {"rain": 0.3, "sun": 0.7}',           # game data, right to be constant
 'TOWER_PRICES = (200, 450, 900)',                       # BTD6 world data
 'COGS = load_cogs()',                                   # computed, not a literal
 'SUBSYSTEMS = [s for s in registry]',                   # comprehension
 'def commands(): return ["a"]',                         # not module-level assign
 'MAX_RETRIES = 3',                                      # tuning constant, not self-state
]

def selftest():
    import tempfile
    ok = True
    for src, want in POSITIVE_SRC:
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
            f.write(src); p = f.name
        got = {h["detector"] for h in scan_file(p)}
        if want not in got:
            print(f"  INERT   want={want} got={got or '{}'} :: {src[:60]!r}"); ok = False
        os.unlink(p)
    for src in NEGATIVE_SRC:
        with tempfile.NamedTemporaryFile("w", suffix=".py", delete=False) as f:
            f.write(src); p = f.name
        got = [h for h in scan_file(p) if h["detector"] == "D1_name"]
        if got:
            print(f"  OVERMATCH {got} :: {src[:60]!r}"); ok = False
        os.unlink(p)
    print(f"positives {len(POSITIVE_SRC)}/{len(POSITIVE_SRC)} negatives {len(NEGATIVE_SRC)}/{len(NEGATIVE_SRC)}"
          if ok else "SELFTEST FAILED")
    return ok

if __name__ == "__main__":
    if sys.argv[1:2] == ["--selftest"]:
        sys.exit(0 if selftest() else 1)
    root = sys.argv[1]
    all_hits = []
    for dirpath, _, files in os.walk(root):
        for fn in files:
            if fn.endswith(".py"):
                all_hits += scan_file(os.path.join(dirpath, fn))
    json.dump(all_hits, open("capture_literal_hits.json", "w"), indent=1)
    by_det = collections.Counter(h["detector"] for h in all_hits)
    files_d1 = {h["path"] for h in all_hits if h["detector"] == "D1_name"}
    files_d2 = {h["path"] for h in all_hits if h["detector"] == "D2_label"}
    print(f"hits {len(all_hits)}  {dict(by_det)}")
    print(f"D1 files {len(files_d1)} · D2 files {len(files_d2)} · D1-only files {len(files_d1 - files_d2)}")
