# 2026-07-14 — kit upgrade v1.15.0 → v1.16.0

> **Status:** `in-progress`

📊 Model: Claude Fable (family-level)

about to do: upgrade the substrate-kit vendored engine from v1.15.0 to v1.16.0 using the canonical two-command recipe (stage verified release asset as `bootstrap.py.new` + `release.json` → `python3 bootstrap.py.new upgrade` → `python3 bootstrap.py upgrade --apply-docs` → `check --strict`). Scope rails per Q-0261.3: bootstrap.py, `.substrate/**`, --apply-docs-applied docs, staged gate, kit pin only — no control/**, hooks, settings, or host-customized workflows. Heartbeat `kit:` bump stays lane-owed.

Provenance: substrate-kit v1.16.0 distribution wave (per-adopter worker; asset sha256 bba34e2102cbaf09394f39992f0501ea5cfd542d90301ef67e31a0854ca59170, 980026 bytes, release.json adjacent).
