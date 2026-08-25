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

# --- E1 outbound-mail checkers (added 2026-08-25, fm #946) ---------------------
# WHY HERE AND NOT IN A WORKFLOW: same reason as the two above — this file is
# host-owned and survives kit upgrades, and it keeps the PR out of the
# workflow-touching carve-out that makes merge-on-green refuse to land it.
#
# WHY AT ALL: on 2026-08-25 two commits were pushed with check_eap_figures.py
# RED and CI passed them, because nothing ran it. That is the same shape as the
# defect recorded above — a gate staying green while a checker does not run —
# and the same shape as the outbound mail's own finding 3: a rule that does not
# arrive at the moment of action does not bind. Running it here is the arrival.
#
# SELF-SKIP: these are specific to the E1 draft. When it is archived or moved,
# the guard drops them cleanly instead of reddening the gate for every later PR.
if [ -f docs/planning/2026-08-24-final-eap-email-draft.md ]; then
  python3 tools/render_eap_mail.py --selftest
  python3 tools/render_eap_mail.py --verify
  python3 tools/check_eap_figures.py
else
  echo "repo_checks: E1 draft absent — mail checkers skipped (expected after E1 closes)"
fi
