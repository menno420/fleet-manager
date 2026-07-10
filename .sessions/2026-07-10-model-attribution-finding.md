# 2026-07-10 — Critical finding: model attribution inconsistent across surfaces (routine-fired sessions)

> **Status:** `complete`

📊 Model: fable-5 (family-level, self-reported from this session's own harness) · high · docs + control finding-landing job · start 2026-07-10T19:37Z (`date -u`)

## Declared at open (born-red)

Critical-finding job dispatched by the fleet-manager coordinator (owner report
2026-07-10 ~20:00Z, plus an owner correction mid-job). About to land, in this PR:

1. Probe record: does `create_trigger` expose a model parameter? (Answer: NO —
   verbatim schema captured; `list_triggers` objects carry no model field either.)
2. `docs/capabilities.md` — dated append: model attribution for routine-fired
   sessions is **inconsistent across surfaces** (Routines screen says fable-5;
   chat header + the session's own card say sonnet-5; no authoritative surface).
3. `docs/experiments/README.md` § Standing caveats — extend the seat-contamination
   caveat with the model-attribution disagreement.
4. `docs/prompts/init-prompt-universal.md` — dated known-limit rider on the
   verified routine recipe.
5. `docs/owner-queue.md` — Anthropic email pack parked item gains the fourth
   routines platform bug (attribution inconsistency).
6. `control/inbox.md` — ORDER 010 (per-lane model verification sweep, with a
   ground-truth self-report step).
7. `control/status.md` — heartbeat noting the finding, the probe result, the PR.

## Close-out

Landed exactly the seven items above; details live in the changed files. Key
records:

- **Probe (verbatim-grounded):** the `create_trigger` MCP schema exposes NO
  model parameter (properties: `name`, `prompt`, `cron_expression`,
  `run_once_at`, `persistent_session_id`, `create_new_session_on_fire`,
  `environment_id`, `notifications` — nothing model-shaped). `list_triggers`
  (50 triggers read): union of trigger keys has no model-related key;
  `job_config.ccr.session_context` carries only `allowed_tools` + `mcp_config`.
  The sole "model" substring across all 50 records is the phrase "collab-model"
  inside one trigger's prompt text. Full quotes: `docs/capabilities.md` append.
- **Evidence chain re-verified at HEAD:** websites `origin/main`
  `.sessions/2026-07-10-order008-first-fire-manifest-smoke.md` line 8 reads
  verbatim: `- **📊 Model:** claude-sonnet-5 · medium · maintenance +
  smoke-check build` (merged in websites PR #59, squash 2c89e96) — while the
  owner's Routines menu shows fable-5 for ALL project-created routines,
  including that one, and the fired session's chat header showed "Sonnet 5".
  Three surfaces, two answers, no ground truth → framed as **attribution
  inconsistency**, not as "fired sessions don't inherit the Project model"
  (owner correction applied before landing).

💡 **Session idea:** a tiny `tools/model_matrix.py` that greps every fleet
repo's recent `.sessions/*.md` for `📊 Model:` lines over git transport and
emits the fleet-wide Project-setting vs self-reported-family matrix ORDER 010
asks for — the sweep becomes one command instead of N manual card reads, and
it can ride the generated-roster tooling (ORDER 009) since both walk the same
per-lane files.

⟲ **Previous-session review:** the 18:31Z doctrine wake (PR #33) was thorough
and well-evidenced, but its card's model line ("wake-slice worker … model line
intentionally generic — no model identifiers") over-read the Q-0262
family-level policy: the policy bans *exact IDs*, not family names — and
today's finding shows why a generic line is costly (a card without a
family-level self-report is exactly the unrecoverable-identity gap the
experiments caveat warns about). Workflow improvement: the card template's
model line should be REQUIRED family-level, never "generic" — ORDER 010's
sweep + the init-prompt known-limit rider landed here make that the standing
rule.
