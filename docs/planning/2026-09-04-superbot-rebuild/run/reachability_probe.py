#!/usr/bin/env python3
"""Route-graph reachability over superbot-next's COMPILED MANIFEST.

Closes an explicit honest null of the 2026-08-05 live audit § 9:
  "The two-tap property was NOT measured, only the zero-button rate. Proving or
   refuting 'every feature is two taps from !help' needs the route table walked
   as a graph, which is the acceptance test proposed in § 4b, not a result
   reported here."

This is also the PROTOTYPE of the successor's reachability gate, so it is
written the way that gate must be written: it declares its population, asserts
the population is non-empty, and walks the SHIPPED ARTIFACT (the compiled
manifest) rather than a runtime registry a test fixture can empty.
"""
import json, sys, collections

SNAP = "/home/user/superbot-next/manifest.snapshot.json"

def load():
    d = json.load(open(SNAP))
    panels = {}
    for sub, s in d["subsystems"].items():
        p = s.get("panels") or {}
        it = p.items() if isinstance(p, dict) else [(x.get("panel_id", i), x) for i, x in enumerate(p)]
        for pid, spec in it:
            panels[spec.get("panel_id", pid)] = (sub, spec)
    return d, panels

def ref(x):
    """A PanelRef inside the snapshot is {'$ref': 'panel:<id>'}."""
    if isinstance(x, dict) and "$ref" in x:
        v = x["$ref"]
        if isinstance(v, str) and v.startswith("panel:"):
            return v.split("panel:", 1)[1]
    return None

def edges_of(spec, up=False):
    """Panels a viewer can reach from this one by pressing something.

    `up=False` counts only DOWNWARD/lateral edges — the ones that make a feature
    DISCOVERABLE. `up=True` additionally counts the framework's Back (parent) and
    Home links, which are real presses but cannot introduce a user to anything
    they have not already found. Both readings are reported; the discoverability
    question is answered by the first.
    """
    out = set()
    for a in spec.get("actions") or []:
        t = ref(a.get("handler"))
        if t: out.add(t)
    for s in spec.get("selectors") or []:
        for opt in (s.get("options") or []):
            t = ref(opt.get("handler") if isinstance(opt, dict) else None)
            if t: out.add(t)
        t = ref(s.get("handler"))
        if t: out.add(t)
    nav = spec.get("navigation") or {}
    for e in nav.get("extra_routes") or []:
        t = ref(e.get("route"))
        if t: out.add(t)
    if up:
        t = ref(nav.get("parent"))
        if t: out.add(t)
        h = nav.get("home_hub")
        if isinstance(h, dict):
            t = ref(h)
            if t: out.add(t)
    return out

def main():
    d, panels = load()

    # --- POPULATION CONTRACT: declared, non-empty, and the shipped artifact ---
    POPULATION = "every panel in the committed manifest.snapshot.json"
    FLOOR = 250
    if len(panels) < FLOOR:
        sys.exit(f"POPULATION FLOOR BREACH: {len(panels)} panels < {FLOOR}. "
                 f"A reachability result over a smaller population is not "
                 f"evidence about this product. ({POPULATION})")

    # Entry points a user actually has. Two readings, both reported, because
    # which one is 'the front door' is exactly what is in dispute.
    entries_help = {p for p in panels if p.startswith("help.")}
    hubish = {p for p in panels if p.endswith(".hub") or p.endswith(".main")}
    cmd_routes = set()
    for sub, s in d["subsystems"].items():
        cmds = s.get("commands") or {}
        it = cmds.values() if isinstance(cmds, dict) else cmds
        for c in it:
            t = ref(c.get("route"))
            if t: cmd_routes.add(t)

    ids = set(panels)
    adj = {pid: edges_of(spec) & ids for pid, (sub, spec) in panels.items()}
    adj_up = {pid: edges_of(spec, up=True) & ids for pid, (sub, spec) in panels.items()}

    def bfs(roots, graph=None):
        graph = graph if graph is not None else adj
        dist = {r: 0 for r in roots if r in panels}
        q = collections.deque(dist)
        while q:
            cur = q.popleft()
            for nxt in graph[cur]:
                if nxt not in dist:
                    dist[nxt] = dist[cur] + 1
                    q.append(nxt)
        return dist

    print(f"POPULATION : {POPULATION}")
    print(f"             {len(panels)} panels (floor {FLOOR}, satisfied)")
    print(f"             {sum(len(v) for v in adj.values())} DOWNWARD edges "
          f"(button/selector/extra-route to another panel)")
    print(f"             {sum(len(v) for v in adj_up.values())} edges including "
          f"framework Back/Home up-links")
    print(f"             a 314-node graph needs >= 313 edges merely to be a tree")
    print()
    for name, roots in (("help.* panels as roots", entries_help),
                        ("*.hub / *.main as roots", hubish),
                        ("every panel a COMMAND routes to", cmd_routes),
                        ("all three combined", entries_help | hubish | cmd_routes)):
        dist = bfs(roots)
        hist = collections.Counter(dist.values())
        unreach = len(panels) - len(dist)
        within2 = sum(n for d_, n in hist.items() if d_ <= 2)
        print(f"-- {name}: {len(roots & set(panels))} roots")
        print(f"   reachable {len(dist)}/{len(panels)}  unreachable {unreach}"
              f"  within 2 taps {within2}/{len(panels)} ({100*within2/len(panels):.0f}%)"
              f"  max depth {max(hist) if hist else '-'}")
        print(f"   depth histogram: {dict(sorted(hist.items()))}")
        print()

    allroots = entries_help | hubish | cmd_routes
    du = bfs(allroots, adj_up)
    print(f"-- same combined roots, counting Back/Home up-links too: "
          f"reachable {len(du)}/{len(panels)}, unreachable {len(panels)-len(du)}")
    print("   (up-links cannot introduce a user to anything they have not already"
          " found, so this is the generous bound, not the discoverability answer)")
    print()

    # Per-subsystem reachability from the combined entry set.
    dist = bfs(allroots)
    per = collections.Counter(); unre = collections.Counter()
    for pid, (sub, _) in panels.items():
        per[sub] += 1
        if pid not in dist: unre[sub] += 1
    print("-- subsystems with unreachable panels (from ALL entry points combined)")
    for sub, n in unre.most_common(15):
        print(f"   {sub:22s} {n:3d} / {per[sub]:3d} unreachable")
    print(f"   TOTAL unreachable: {sum(unre.values())} of {len(panels)}")

if __name__ == "__main__":
    main()
