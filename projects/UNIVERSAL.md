<!-- v1 · 2026-07-10 · universal pointer prompts — edit-registry-first; the manager is this file's only writer -->
# UNIVERSAL.md — the owner's universal pointer prompts

> **Status:** `living` — v1 · 2026-07-10. **Edit-registry-first:** this file is
> the source of truth; every console/chat paste of these blocks is a copy.

**What this is.** Two blocks the owner pastes **identically into every
Project** — Block 1 into the Custom Instructions field, Block 2 as the
first/wake message. No per-Project matching: the Project's **repo attachment**
tells the session which `projects/<repo>/` registry dir is its own, and the
session self-locates its real package (instructions / coordinator prompt /
failsafe) by fetching it raw from this public repo. The per-repo packages stay
the canonical content; these blocks are only the pointer.

## Block 1 — Universal Custom Instructions (paste into every Project's Custom Instructions field)

```
UNIVERSAL FLEET BOOT (v1 · 2026-07-10). This Project's real instructions live in
the fleet registry, not in this paste. First action every session: identify your
repo (the one attached to this Project), then fetch these two files raw:
https://raw.githubusercontent.com/menno420/fleet-manager/main/projects/<your-repo>/instructions.md
https://raw.githubusercontent.com/menno420/fleet-manager/main/projects/<your-repo>/coordinator-prompt.md
instructions.md = your binding working rules. coordinator-prompt.md = your
operating loop. Quote each file's version header (first line) in your session
card so drift is detectable. If the fetch fails or your repo has no registry
entry, say so in your heartbeat and fall back to your repo's own
.claude/CLAUDE.md + control/README.md. The registry is canonical
(edit-registry-first; the manager is its only writer) — never edit projects/
yourself; propose changes via a ⚑ INTAKE line in your heartbeat.
```

## Block 2 — Universal wake / start-off prompt (paste as the first/wake message in every Project)

```
WAKE (universal, v1 · 2026-07-10): sync your attached repo to origin/main HEAD.
Fetch your seat files from the fleet registry:
https://raw.githubusercontent.com/menno420/fleet-manager/main/projects/<your-repo>/
(coordinator-prompt.md = your loop · instructions.md = your rules ·
failsafe-prompt.md = your cron text). Execute coordinator-prompt.md from its
boot step. Quote its version header in your session card. If your toolset lacks
a tool the prompt assumes (scheduler, PR tooling), record the wall verbatim and
use the documented fallback. Overwrite control/status.md as the deliberate last
step of your work.
```
