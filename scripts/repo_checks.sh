#!/usr/bin/env bash
# fleet-manager's repo checkers — the HOST half of the substrate-gate
# `repo checkers` extension point (kit v1.21.0).
#
# The kit-owned .github/workflows/substrate-gate.yml runs this file when it
# exists and self-skips when it does not. Before v1.21.0 these two commands
# lived as a hand-added step INSIDE the kit-owned workflow, which every kit
# upgrade regenerated and silently dropped (fm #833 — the gate stayed green
# while running neither checker; re-applied by hand, tracked in
# docs/SKILLS-local.md's re-apply table). This file is host-owned: no kit
# command writes scripts/, so the wiring survives every upgrade.
#
# Wired 2026-08-06 (as the in-workflow step) after a merge landed conflict
# markers on main: doc-routes.json stopped parsing, route_docs.py took its
# fail-open path, and the doc-routing hook went SILENT with nothing red
# anywhere. check_doc_routes.py --strict exits 1 on unparseable JSON and
# would have caught it. Cheap, deterministic, no judgement — the tier that
# belongs on a hard gate (docs/findings/2026-08-05-foundation-continuation.md § 5).
set -euo pipefail

python3 tools/check_doc_routes.py --strict
python3 tools/check_no_false_walls.py --strict
