# The off-repo log — hand-written lane

> **Status:** `living-ledger`
>
> **What this file is:** the record of work that touches **no repository** and
> therefore cannot be derived from anything. Laptop setup. A ChatGPT or Gemini
> sitting. A Drive reorganisation. An install, a subscription, a device paired.
> A decision taken in a chat and acted on outside git. It is the other half of
> [`estate-log.md`](estate-log.md), which is generated and covers repository
> work automatically.
>
> **What it is NOT:** a diary, a task list, or a place for repository work. If
> the work produced a commit, it belongs in that repository's `.sessions/` card
> and the generated lane will pick it up — writing it here as well creates two
> records that will disagree.
>
> **Who writes here:** any session, local or cloud, and the owner. One command:
>
> ```bash
> python3 tools/estate_activity.py log \
>   --venue local-desktop \
>   --title "what happened, in six words" \
>   --agent "opus-5" \
>   --touched "FreeCAD library, godot/workbench.tscn" \
>   --why "..." --state "..." --next "..."
> ```
>
> Then commit. Any field you leave out reads `unstated`, which is a legitimate
> answer and better than an invented one.
>
> **Venue vocabulary** (the closed set, shared with the session-card
> `📍 Venue:` line): `local-desktop` · `local-cli` · `cloud-container` ·
> `codex-cloud` · `chatgpt-work` · `other`.

## Entries, newest first

<!-- newest entry goes directly below this line -->

### 2026-08-25 — creator-kit seeded on the laptop: FreeCAD + Godot tooling

- **venue:** `local-desktop`
- **agent:** unstated — `REASONED`, see the provenance note below
- **touched:** `menno420/creator-kit` (created 2026-08-25T21:14:50Z), one commit
  *"Seed creator-kit: existing FreeCAD/Godot tooling + substrate-kit 1.21.0"*
- **why:** unstated by the owner. The tree is a reusable starting point for
  physical ideas in FreeCAD and spatial experiments in Godot, deliberately
  usable without coding.
- **state left:** 111 files. Windows `.cmd` launchers (`Open FreeCAD
  Library.cmd`, `Rebuild FreeCAD Library.cmd`, `Open Creator Workbench.cmd`),
  eight named FreeCAD parts driven by `freecad/dimensions.txt`, a Godot
  workbench scene, substrate-kit v1.21.0 vendored. `docs/current-state.md` is
  still the **unrendered kit template** — every `${...}` slot unfilled.
- **next:** run the kit interview (`python3 bootstrap.py ask`) so the repo has
  its own truth; give it a `docs/repos/creator-kit/` folder here.

> **Provenance of this entry — `REASONED`, not `OWNER`.** It is the seed entry,
> reconstructed on 2026-08-26 from the repository itself because it is the
> exact class of work this lane exists to catch: it happened, fleet-manager did
> not know, and nothing would have told a later session. The `local-desktop`
> venue is inferred from the tree — Windows `.cmd` launchers and a FreeCAD
> library are not things a Linux container produces — and from the owner's
> stated laptop work in the same days. **Inferred, not measured**; correct it
> here if it is wrong.

*(This is the first entry. Everything before 2026-08-25 predates the lane and
was never recorded — that gap is real and is not backfilled, because a
reconstructed diary would read exactly like a remembered one.)*
