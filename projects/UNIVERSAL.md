<!-- v2 · 2026-07-10 · universal WAKE prompt + Custom Instructions flow — edit-registry-first; the manager is this file's only writer -->
# UNIVERSAL.md — the owner's universal wake prompt (+ Custom Instructions flow)

> **Status:** `living` — v2 · 2026-07-10. **Edit-registry-first:** this file is
> the source of truth; every console/chat paste of these blocks is a copy.

> **OWNER RULING 2026-07-10:** Custom Instructions are pasted **COMPLETE per
> Project** (they survive chat archives; full text always present). The
> universal pointer below is for the **WAKE/START-OFF prompt only.**
> (Owner chat 2026-07-10 ~22:15Z: "custom instructions should remain complete
> per project — they always survive archives, so it's better if they are always
> fully there." This retracts v1's universal Custom-Instructions pointer block.)

**What this is.** ONE block the owner pastes **identically into every Project**
as the first/wake message. No per-Project matching for the wake: the Project's
**repo attachment** tells the session which `projects/<repo>/` registry dir is
its own, and the session self-locates its seat package (instructions /
coordinator prompt / failsafe) by fetching it raw from this public repo. The
per-repo packages stay the canonical content; the wake block is only the
pointer. **Custom Instructions are NOT a pointer** — see the flow section below.

## Universal wake / start-off prompt (paste as the first/wake message in every Project)

```
WAKE (universal, v2 · 2026-07-10): sync your attached repo to origin/main HEAD.
Fetch your seat files from the fleet registry:
https://raw.githubusercontent.com/menno420/fleet-manager/main/projects/<your-repo>/
(coordinator-prompt.md = your loop · instructions.md = your rules ·
failsafe-prompt.md = your cron text). Execute coordinator-prompt.md from its
boot step. Quote its version header in your session card. If your toolset lacks
a tool the prompt assumes (scheduler, PR tooling), record the wall verbatim and
use the documented fallback. Overwrite control/status.md as the deliberate last
step of your work.
```

## Custom Instructions flow (per Project — FULL paste, never a pointer)

Per the owner ruling above, each Project's **Custom Instructions field = the
FULL body of its `projects/<repo>/instructions.md`**, pasted complete and
version-stamped (the file's version header comes along in the paste). Flow:

- **Edit-registry-first:** change `projects/<repo>/instructions.md` here, bump
  its `vN` version header, then the owner re-pastes the full new body into
  that Project's Custom Instructions field.
- **Drift check:** ask the seat to quote its Custom Instructions version
  header; a header older than the registry file = stale paste → re-paste due.
- **Why full, not a pointer:** Custom Instructions survive chat archives, so
  the complete text is always present in the Project with no fetch dependency;
  the raw-fetch indirection stays confined to the wake prompt.
