# 2026-07-12 — roster: honest UNREADABLE verdict + authenticated transport for pokemon-mod-lab

> **Status:** `complete`

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

## Shipped (close-out)

- **Verdict split** (`scripts/gen_roster.py` `verdict_for`): a walled repo
  now reports **`UNREADABLE (transport/auth)`**, never `DEAD (not
  measurable)`; DEAD is reserved for a READABLE repo with no measurable
  heartbeat signal. New verdict added to the staleness-verdicts ordering,
  the roster header's transport note, and the docstring ladder.
- **Wall annotation** (`describe_wall` + `AUTH_WALL_RE`): auth-shaped wall
  reasons (`could not read Username/Password`, `Authentication failed`,
  `Repository not found`) get the fix pointer appended — every UNREADABLE
  row now says HOW to make it readable. Live-verified: the local proxy
  variant says "Password" where Actions says "Username"; regex covers both.
- **Authenticated transport** (`_auth_args`, `AUTH_TOKEN_ENV`): dedicated
  `ROSTER_READ_TOKEN` env → basic-auth extraheader (`x-access-token:` pair,
  base64 — same mechanism as actions/checkout) on all github.com
  `ls-remote`/`fetch` reads. Blank/unset → unchanged unauthenticated path.
  `GH_TOKEN`/`GITHUB_TOKEN` deliberately NOT picked up: this container
  exports literal `proxy-injected` placeholders in both — a silent pickup
  would 401 reads that succeed today.
- **Workflow wiring** (`.github/workflows/roster-regen.yml`): regen step
  forwards `secrets.ROSTER_READ_TOKEN`; provenance comment updated (the
  "owner can wire a PAT in" note is now "the wire exists; only the secret
  is the owner click"). YAML parse-verified.
- **Verification**: `--selfcheck` PASS (new assertions: verdict split,
  wall annotation incl. masked-404, auth-arg builder never cleartext,
  blank-token = unset, non-github URL never gets the header);
  `check_roster_freshness.py` exit 0; `bootstrap.py check --strict` green
  except the DESIGNED born-red hold on this card; full `--stdout` dry-run
  (nothing committed — the workflow owns generation): pokemon-mod-lab
  measured honestly over authenticated transport — heartbeat
  2026-07-11T21:03:45Z, evidence `759dee4` 2026-07-12T16:13:27, verdict
  DARK (~25h24m — honest staleness, not fabricated death).
- **Owner click still owed** (paste-ready candidate in the worker report;
  inbox/queue coordinator-held in sibling PRs #142/#143, untouched):
  fine-grained PAT, Contents:read on `menno420/pokemon-mod-lab`, saved as
  fleet-manager repo secret `ROSTER_READ_TOKEN`.

💡 Session idea: **UNREADABLE-regression canary in the regen workflow** —
gen_roster (or a tiny post-step) compares this generation's set of
UNREADABLE/walled lanes against the previous committed roster's; a lane
that was readable last generation and walled this one raises a loud
`::warning::` (and a roster-header flag). Catches a revoked/expired
`ROSTER_READ_TOKEN` — or a repo flipped private — the moment it happens,
instead of the row silently degrading and waiting for a human to notice
the verdict changed. Deduped against `docs/ideas/` (no transport/canary
idea exists).

⟲ Previous-session review (staleness-sweep worker): its method was right —
it read verdicts against ground truth per-lane instead of trusting the
roster wholesale, and that cross-check is exactly what exposed both the
3h-stale triggers-snapshot riding under fresh heartbeat columns AND (this
session's slice) the pokemon-mod-lab DEAD-vs-alive contradiction. What it
could improve: it reported the snapshot-lag finding as prose only.
Concrete improvement: stamp the snapshot's age (e.g. "trigger columns from
snapshot captured 3h04m before generated-at") directly in the roster
header next to the trigger-evidence line, so every reader of every
generation sees the trigger-column lag without re-deriving it — the regen
workflow already computes exactly this age in its advisory step and then
throws it away.
