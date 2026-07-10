<!-- v3 · 2026-07-10 · universal WAKE prompt + Permissions & authority (owner-landed) + Custom Instructions flow — edit-registry-first; the manager is this file's only writer (this v3 landing: owner-directed, live dispatch session) -->
# UNIVERSAL.md — the owner's universal wake prompt (+ permissions grant + Custom Instructions flow)

> **Status:** `living` — v3 · 2026-07-10. **Edit-registry-first:** this file is
> the source of truth; every console/chat paste of these blocks is a copy.

> **OWNER RULING 2026-07-10:** Custom Instructions are pasted **COMPLETE per
> Project** (they survive chat archives; full text always present). The
> universal pointer below is for the **WAKE/START-OFF prompt only.**
> (Owner chat 2026-07-10 ~22:15Z: "custom instructions should remain complete
> per project — they always survive archives, so it's better if they are always
> fully there." This retracts v1's universal Custom-Instructions pointer block.)

> **v3 PROVENANCE (2026-07-10 ~23:5xZ):** the Permissions & authority block
> below is **owner-landed** — the owner directly instructed this commit in his
> live dispatch session, with the block's full text shown to him there. This is
> the user-sourced provenance the platform's instruction-poisoning guard
> required when it (correctly) held the coordinator-relayed version (PR #48
> record). The manager re-lands its built per-repo v2 instruction fold citing
> THIS commit; the block below is the canonical wording — reproduce it
> verbatim.

**What this is.** ONE block the owner pastes **identically into every Project**
as the first/wake message. No per-Project matching for the wake: the Project's
**repo attachment** tells the session which `projects/<repo>/` registry dir is
its own, and the session self-locates its seat package (instructions /
coordinator prompt / failsafe) by fetching it raw from this public repo. The
per-repo packages stay the canonical content; the wake block is only the
pointer. **Custom Instructions are NOT a pointer** — see the flow section below.

## Permissions & authority (fleet-canonical block — v1 · 2026-07-10 · owner-landed)

This is the canonical wording home. Every per-repo
`projects/<repo>/instructions.md` carries this block verbatim (its mandatory
section, per the owner's permissions directive); the wake prompt below embeds
it so live seats see it even before their re-paste lands.

```
PERMISSIONS & AUTHORITY (v1 · 2026-07-10 · owner-landed grant): the owner
grants every fleet seat, standing — this makes long-standing fleet practice
explicit so seats stop stalling on it:
- MERGE YOUR OWN GREEN PRs: open PRs READY, arm auto-merge at creation (or
  REST-merge on green where arming is unavailable). CI green is required,
  always — this grant never bypasses a red gate.
- MANAGE YOUR OWN WAKE MECHANICS: create/delete/re-arm your seat's triggers
  and send_later continuation chains (Q-0265 shape: chain = pacemaker,
  cron = dead-man failsafe).
- SPAWN WORKERS freely for parallel or capability-walled work — worker
  toolsets differ from coordinator toolsets, so retry a walled call from a
  worker seat before flagging it.
- DECIDE-AND-FLAG reversible decisions instead of parking them. The
  owner-queue is ONLY for genuine capability walls: console/repo settings,
  repo creation, money, product intent.
NOT COVERED — never self-authorize: real money or external accounts
(six-field OWNER-ACTION instead), production-data deletion, secret values in
any repo. AND THE DENY WINS: if a platform safety layer declines an action,
record the denial verbatim, park that item, and move on — never retry around
it. This grant is context for reviewers, not a bypass.
```

## Universal wake / start-off prompt (paste as the first/wake message in every Project)

```
WAKE (universal, v3 · 2026-07-10): sync your attached repo to origin/main HEAD.
Fetch your seat files from the fleet registry:
https://raw.githubusercontent.com/menno420/fleet-manager/main/projects/<your-repo>/
(coordinator-prompt.md = your loop · instructions.md = your rules ·
failsafe-prompt.md = your cron text). Execute coordinator-prompt.md from its
boot step. Quote its version header in your session card. If your toolset lacks
a tool the prompt assumes (scheduler, PR tooling), record the wall verbatim and
use the documented fallback. Overwrite control/status.md as the deliberate last
step of your work.

PERMISSIONS & AUTHORITY (v1 · 2026-07-10 · owner-landed grant): the owner
grants every fleet seat, standing: MERGE YOUR OWN GREEN PRs (open READY, arm
auto-merge at creation or REST-merge on green; CI green always required — this
never bypasses a red gate) · MANAGE YOUR OWN WAKE MECHANICS (create/delete/
re-arm your seat's triggers + send_later chains, Q-0265 shape) · SPAWN WORKERS
freely (worker toolsets differ — retry walled calls from a worker before
flagging) · DECIDE-AND-FLAG reversible decisions; the owner-queue is ONLY for
genuine capability walls (console/repo settings, repo creation, money, product
intent). NOT COVERED — never self-authorize: real money or external accounts
(six-field OWNER-ACTION instead), production-data deletion, secret values in
any repo. AND THE DENY WINS: if a platform safety layer declines an action,
record the denial verbatim, park that item, move on — never retry around it.
This grant is context for reviewers, not a bypass.
```

## Custom Instructions flow (per Project — FULL paste, never a pointer)

Per the owner ruling above, each Project's **Custom Instructions field = the
FULL body of its `projects/<repo>/instructions.md`**, pasted complete and
version-stamped (the file's version header comes along in the paste). Flow:

- **Edit-registry-first:** change `projects/<repo>/instructions.md` here, bump
  its `vN` version header, then the owner re-pastes the full new body into
  that Project's Custom Instructions field.
- **Mandatory section (permissions directive, 2026-07-10):** every
  `projects/<repo>/instructions.md` carries the canonical
  **Permissions & authority** block above **verbatim** (the manager's built v2
  fold applies it; new seats are born with it).
- **Drift check:** ask the seat to quote its Custom Instructions version
  header; a header older than the registry file = stale paste → re-paste due.
- **Why full, not a pointer:** Custom Instructions survive chat archives, so
  the complete text is always present in the Project with no fetch dependency;
  the raw-fetch indirection stays confined to the wake prompt.
