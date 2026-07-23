#!/usr/bin/env bash
# Land the phone-controller Slice-4 handoff into menno420/product-forge.
# Run from any venue whose product-forge pushes work (product-forge-scoped session,
# or the owner's machine). See README.md in this directory for the full ritual.
set -euo pipefail

HERE="$(cd "$(dirname "$0")" && pwd)"
BRANCH="claude/controller-app-android-apk-j7tv10"
WORK="${1:-$(mktemp -d)/product-forge}"

git clone https://github.com/menno420/product-forge.git "$WORK"
cd "$WORK"
git checkout -b "$BRANCH" origin/main
git am "$HERE"/00*.patch

# The substrate gate, locally — must be green before pushing.
python3 bootstrap.py check --strict

git push -u origin "$BRANCH"

cat <<'NEXT'
Pushed. Next steps (see README.md):
  1. Open the PR READY (base main); wait for android-ci + substrate-gate green.
  2. Merge on green (workflow-touching diff parks auto-merge; direct merge on green
     under the owner's live directive is the recorded precedent, PR #29). Or split
     commit 0003 into a companion workflows PR for the strict rail.
  3. Tag the release from the merge commit:
       git tag phone-controller-v0.4.0 <merge-sha>
       git push origin phone-controller-v0.4.0
  4. VERIFY: the GitHub Release carries phone-controller-0.4.0.apk + .sha256.
NEXT
