# 2026-07-09 — owner-session idea capture + playbook R21 + night handoff update

> **Status:** `complete`

📊 Model: Claude Fable 5 (claude-fable-5) · docs-only session · night (~23:00Z)

## Declared at open (born-red)

1. Seed `docs/ideas/` backlog with tonight's 9 owner-session ideas
   (2026-07-09 ~22:30–23:00Z brainstorm — captured, none approved).
2. Playbook **R21** (friction → rule): REST merge-on-green is the PRIMARY
   landing path on born-red and no-CI repos; align
   `docs/gen2-blueprint.md`'s merge-mechanism wording with it.
3. Update `docs/handoff-2026-07-09.md` + `docs/dispatch-log.md` with
   tonight's arc (wind-down 7/9, PR #10 package, venture-lab seeded +
   green light, EAP window extended to 2026-07-14, Anthropic follow-up
   in-flight).

## Done (all three, this PR)

- **Ideas ×9 captured** — one file per idea in `docs/ideas/` with kit
  frontmatter (`state: captured` · `origin: owner` · `outcome: open`),
  `> **Status:** \`ideas\`` badge, and `Status: captured (not approved)`
  in the body; README backlog indexes the 2026-07-09 cohort with routing
  destinations (mobile-lab flagged as the candidate second gen-2 launch).
- **Playbook R21** — new MERGE MECHANICS section: REST merge-on-green is
  PRIMARY on born-red repos ("pull request is in unstable status") and
  PR-ruleset-no-CI repos ("Auto-merge only applies when checks are
  pending"); arm-at-creation primary only where a check can go pending.
  Provenance in the rule: fleet-manager PR #10 (3 failed arms) +
  venture-lab PR #1. R5 got a scope-narrowed cross-ref; blueprint §1
  MERGE AUTHORITY bullet + §2 deltas 1/2 rewritten to the R21 split, with
  a changelog line.
- **Handoff + dispatch log** — night updates: wind-down 7/9 DONE,
  venture-lab seeded `d065c68` + owner green light, EAP window extended
  to **2026-07-14** (Anthropic email 22:29Z; old 07-10 line superseded in
  place), new in-flight item "Anthropic follow-up draft early next week",
  standing-rules line now R1–R21; dispatch log gained the
  "2026-07-09 — night" section with the full arc.

## Landing note (R21 practiced, not just written)

No auto-merge arm was attempted on this PR — this repo is born-red by
design, the exact shape R21 names. Landed via REST merge-on-green after
the card flip.

## 💡 Session idea

**Blocked-arm detector in the worker preamble:** R21 documents WHERE
arming is impossible, but a worker only knows its repo's shape if it has
read the playbook carefully. A two-line preflight in
`templates/worker-preamble.md` — "does this repo's gate hold PRs red by
design, or does it have no CI? then plan REST merge-on-green from the
start" — would make the R21 decision mechanical at dispatch time instead
of a lesson each lane re-learns by burning arm attempts (PR #10 burned
three; venture-lab PR #1 burned one).

## ⟲ Previous-session review

The PR #10 session (merge-authority + archetypes + merge queue) shipped a
large, verifiable package and — critically — turned its own landing
friction into evidence rather than hiding it: the 3 failed arm attempts
it recorded are exactly what made R21 writable tonight with real
provenance. Two genuine improvables: (1) it wrote the blueprint's
"arm-at-creation IS the self-merge path" as unconditional in the same PR
whose own landing disproved unconditionality — a session that hits a wall
should re-read what it just wrote about that wall before merging (this
session's fix: the R21 alignment); (2) the handoff's EAP-deadline line
was left as a hard date with no "as-of" qualifier, so tonight's extension
made it silently wrong — deadline lines in living docs should carry their
source + timestamp (adopted here: the extension line cites the 22:29Z
email).
