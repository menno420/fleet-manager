# 2026-07-12 — roster: honest UNREADABLE verdict + authenticated transport for pokemon-mod-lab

> **Status:** `in-progress`

📊 Model: Claude (Fable family, fable-5) · start 2026-07-12T~22:0xZ · lane
worker dispatched by coordinator (roster-measurement slice)

## Declared at open (born-red)

Scope: roster gen #21 marks pokemon-mod-lab **DEAD (not measurable)** while
the repo is demonstrably alive (kit v1.15.0 merged 759dee4
2026-07-12T16:13:27Z; heartbeat 2026-07-11T21:03:45Z ARCHIVE-READY /
honest-idle). Root cause is MEASUREMENT, not the lane: the headless
roster-regen workflow reads every heartbeat over plain unauthenticated
https git transport, which works for the public lane repos and walls on the
one private repo ("fatal: could not read Username for
'https://github.com': terminal prompts disabled"), and `verdict_for()`
collapses ANY wall into a death verdict. Fix agent-side in
`scripts/gen_roster.py` (+ the regen workflow env wiring): (1) walled repo
→ verdict **UNREADABLE (transport/auth)**, never DEAD — a measurement
artifact must not print as lane death; (2) plumb a dedicated
`ROSTER_READ_TOKEN` env (fine-grained read PAT, forwarded by the workflow
from the secret of the same name) into the git reads so the private row
comes alive once the owner adds the secret. Owner click (the secret) goes
to the report as a paste-ready owner-queue candidate — inbox/queue files
are coordinator-held in sibling PRs #142/#143 and are NOT touched here.
Files: `scripts/gen_roster.py`, `.github/workflows/roster-regen.yml`, this
card. No trigger calls; no merge; PR left READY.
