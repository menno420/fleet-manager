# Fleet capability manifest

> **Status:** `living-ledger` — the master manifest of what sessions CAN do here that
> they routinely think they can't, and what is genuinely walled. **Read this before
> declaring anything impossible.** A new capability or wall discovered = append it here
> (or your repo's copy) the same session. Established 2026-07-09 (owner directive: the
> owner kept having to remind sessions about ffmpeg and env tokens by hand).

## CAN — capabilities sessions routinely deny having (with the recipe)

### View video / audio files (.mp4, .webm, .mov, .mp3, …)
Sessions claim they can't view an .mp4. They CAN:

```bash
ffprobe -v error -show_format -show_streams <file>          # inspect codecs/duration first
ffmpeg -i <file> -vf "fps=0.5" -q:v 2 frames_%03d.jpg       # extract frames into the scratchpad
```

Then `Read` the extracted frames as images — one frame every 2 seconds at `fps=0.5`;
raise/lower the fps for denser/sparser sampling. Audio tracks: extract with
`ffmpeg -i <file> -vn audio.wav` and process from there.

### View images and PDFs
`Read` them directly — the Read tool renders images visually and reads PDFs page-by-page
(`pages` parameter). No conversion step needed.

### Use provisioned secrets (bot token, RAILWAY_API_KEY, …)
Sessions forget tokens exist. **CHECK THE ENVIRONMENT FIRST:**

```bash
printenv | grep -iE 'token|key|railway|discord'
```

The bot token, `RAILWAY_API_KEY`, etc. are provisioned in the env. Confirm **presence
only** (names, not values) — **never echo full secret values into logs, files, or
transcripts**. Use them via the env var (`$DISCORD_TOKEN`, header injection, etc.).

### First commit to an empty repo
`git push` to a truly empty repo fails through the proxy tooling. Make the first commit
via the **Contents API** (`create_or_update_file` / `push_files`) — that creates `main`,
and normal git works from then on. (Playbook R13.)

### Arm auto-merge while checks are pending
GitHub refuses to arm auto-merge on an already-green PR — arm it **at PR creation, in
the checks-pending window** (`enable_pr_auto_merge`). This is the sanctioned merge path;
see the self-merge wall below. (Playbook R5/R12.)

### Run any repo's own checkers locally
Clone (or fetch) the repo and run its own gates — `check_quality.py`, `check_docs.py`,
`bootstrap.py check --strict`, pytest suites — before pushing. Nothing restricts a
session to the repo it was launched for.

### Read files from other public repos without extra scope
`WebFetch` on `https://raw.githubusercontent.com/<owner>/<repo>/<ref>/<path>` works
cross-repo for public content — no token scope or `add_repo` needed for read-only
single-file pulls.

### Spawn subagents for parallel work
The Agent tool runs research/implementation/verification workers concurrently — fan out
independent lanes instead of serializing them. (Worker agents themselves don't re-spawn;
the manager/coordinator tier does.)

### Watch something over time
Use **blocking foreground waits** — `until [ $(date +%s) -ge $end ]; do sleep 5; done` —
never background timers. Background timers silently drop the final report. (Playbook R4.)

### YouTube transcripts
`youtube_transcript_api` is IP-blocked from datacenter IPs — sessions conclude
transcripts are impossible. They aren't:

```bash
yt-dlp --skip-download --write-auto-sub <video-url>
```

works via its android-vr endpoint; then parse the resulting `.vtt` file.
(Discovered 2026-07-09, transcript+miner task.)

### Build + test GBA ROMs entirely in-container (toolchain scout 2026-07-09)
Sessions would assume a GBA toolchain/emulator loop is impossible headless. It isn't —
all three routes proven (`docs/findings/gba-toolchain-proof-2026-07-09.md`):

- **pokeemerald:** `apt install binutils-arm-none-eabi` (only extra dep) + agbcc per
  its INSTALL.md → byte-identical retail build, 1m20s full / 2.0s incremental.
- **devkitARM/Butano:** official devkitPro installers are WALLED (below); use the
  **leseratte10 community mirror** (`https://wii.leseratte10.de/devkitPro/`) — extract
  the devkitARM r68 linux_x86_64 `.pkg.tar.zst` packages, build make-rules/crt0 from
  devkitPro's GitHub sources (⚠ unsigned community infra — supply-chain caveat).
- **Headless emulator:** `apt install mgba-sdl` + `pip install mgba==0.10.2` (pin to
  the system libmgba 0.10.x) → boot → run N frames → PNG at ~290 fps; scripted button
  injection can verify changes in-game with no display and no human.

### Self-arm wake routines from inside a Project session (owner-verified 2026-07-10; mechanism verified ~11:01Z)
The "routine/trigger creation walled on BOTH sides" conclusion (2026-07-10 ~02:05Z)
was **WRONG for Project sessions**: agent-armed routines **WORK**, and the mechanism
is now verified — **the claude-code-remote scheduling tools (`create_trigger` /
`send_later` family)**. They are **SEAT-DEPENDENT**: the same tool family that is
absent or refused on some seats arms successfully on others — the same per-seat
inconsistency class as the merge classifier (a wall recorded from one seat is that
seat's outcome, not the platform's).

**Evidence (owner screen recordings, 2026-07-10 11:01Z + 11:04Z, on file; logged in
superbot `docs/planning/projects-eap-evaluation-log.md`):** the claude.ai Routines
screen shows two ACTIVE routines "Created by Claude" and firing — "trading-strategy
4-hourly standing ritual wake" (every 4h, completed run 10:09) and "kit-lab gen2
hourly wake" (hourly, completed runs 12:28/12:28/12:30, driving the live kit-lab
coordinator session).

**Recipe:** from the lane's own session, call `create_trigger` (5-field cron,
≥hourly) for a recurring wake, or `send_later` (delay/timestamp) for a one-shot —
the routine fires back into the same session. If the tool is missing or refused on
your seat, that is a **seat** wall — record the exact tool call + verbatim error in
`control/status.md` and fall back to the owner routine click. The walls below remain
true for non-Project surfaces (webagent coordinator + spawned workers; cross-session
trigger binding).

### ⚠ Rider on routine self-arm — model attribution is INCONSISTENT ACROSS SURFACES (recorded 2026-07-10 ~20:00Z, owner report + owner correction)
Do NOT assume a routine-fired session runs the Project's configured model — and do
NOT assert the opposite either. The verified finding is a **three-way surface
disagreement with no authoritative panel**:

- **Routines menu (owner UI):** displays **fable-5** for ALL project-created
  routines — including the websites one below.
- **Fired session's chat header (owner UI):** showed **"Sonnet 5"** for the
  websites routine-fired session of 2026-07-10.
- **Fired session's own card (committed self-report):** websites
  `.sessions/2026-07-10-order008-first-fire-manifest-smoke.md` (merged in
  websites PR #59, squash 2c89e96; re-verified at HEAD 2026-07-10 ~19:35Z)
  line 8 reads verbatim: `- **📊 Model:** claude-sonnet-5 · medium ·
  maintenance + smoke-check build` — while that Project is set to fable-5.

Ground truth (what actually executed) is currently **undeterminable from any
single panel**. Probe result (2026-07-10 ~19:34Z, this repo's finding job):
the `create_trigger` MCP tool schema exposes **NO model parameter** — its
properties are exactly `name`, `prompt`, `cron_expression`, `run_once_at`,
`persistent_session_id`, `create_new_session_on_fire`, `environment_id`,
`notifications` — so there is no agent-side way to pin a fired session's
model. `list_triggers` (50 trigger records read) shows **no model-related key**
on any trigger: union of keys = `created_at, created_via, creator,
cron_expression, enabled, ended_reason, id, job_config, last_fired_at, name,
next_run_at, persist_session, persistent_session_id, run_once_at,
session_grouping_id, updated_at`; `job_config.ccr.session_context` carries only
`allowed_tools` + `mcp_config`; the sole "model" substring in the entire output
is the phrase "collab-model" inside one trigger's prompt text.

**Working detector:** the fleet's session-card `📊 Model:` convention
(family-level names only, per Q-0262) — each fired session records the model
identity its own harness/environment reports, at the moment of work. That
self-report is itself a claim, but it is the only per-session, committed,
from-inside-the-environment signal we have; the cross-surface disagreement is
unresolved and queued for the Anthropic follow-up email (`docs/owner-queue.md`
Parked).

### Check a repo's ACTUAL visibility — one API call (added 2026-07-10, night-review Q16)
Sessions assert "this repo is PRIVATE" from READMEs and prior PR bodies without ever
checking — that bug class shipped vendored Nintendo source publicly. Visibility is one
call, no special scope needed:

```bash
# REST (works with the provisioned token, or unauthenticated for public repos):
curl -s https://api.github.com/repos/{owner}/{repo} | python3 -c \
  "import json,sys; d=json.load(sys.stdin); print('private:', d['private'], '· visibility:', d['visibility'])"
# gh CLI equivalent:
gh api /repos/{owner}/{repo} --jq '{private: .private, visibility: .visibility}'
```

The GitHub MCP works too — any get-repo-shaped call (e.g. `search_repositories` with
`repo:{owner}/{repo}`) returns the same `.private`/`.visibility` fields in its JSON.
Read `.private` (boolean) or `.visibility` (`public`/`private`/`internal`) from the
response — never from a README, a rail declaration, or another PR's assertion.
**Playbook R22:** any lane whose rails depend on visibility runs this once at every
session start.

### Codex post-merge review — ENABLED on ALL 12 active fleet repos (owner, 2026-07-11)
Codex environments exist for **every active fleet repo** — fleet-manager,
idea-engine, product-forge, sim-lab, substrate-kit, superbot, superbot-games,
superbot-idle, superbot-next, trading-strategy, venture-lab, websites — per the
owner update 2026-07-11 ~00:2xZ (fm `control/inbox.md` ORDER 014; stale envs for
dead repos deleted the same pass). **This RETIRES the recorded "fleet-manager has
no Codex env — ask on PR #26" wall** (dated retirement 2026-07-11, owner
provenance; the wall had been recorded in `control/status.md` @702ba89, the
ORDER 003 drain record, and `projects/fleet-manager/meta.md` — all corrected).
@codex is the PRIMARY review-queue drain path on all 12 repos
(`docs/review-queue.md`).

**Quota caveat:** Codex quota refusals — e.g. superbot#1920's 2026-07-10T22:03:53Z
"You have reached your Codex usage limits for code reviews" — are **RETRY-LATER,
never a wall**. Re-ask after the quota window resets; never record a quota
refusal as a Codex wall.

## WALLED — verified walls (quote the observed error, don't paraphrase)

- **Tag push, GitHub Release creation, remote branch deletion** — fail with **403 at the
  credential layer** → owner action required. Queue it in `docs/owner-queue.md` per R16/R17.
- **Creating/editing claude.ai environments or Projects** — no API surface for
  the agent → **owner clicks** in the claude.ai UI. (Routines are worse — see the
  both-sides wall below.)
- **Routine/trigger creation — walled on NON-PROJECT surfaces only** (CORRECTED
  2026-07-10 ~morning, owner-verified — the earlier "unavailable on BOTH sides" reading
  was wrong for Project sessions; SECOND correction 2026-07-10 ~11:01Z: mechanism now
  verified — see the CAN entry above: **in-Project self-arm WORKS** via the
  claude-code-remote scheduling tools (`create_trigger` / `send_later` family),
  **seat-dependent** — same per-seat inconsistency class as the merge classifier).
  Still walled:
  agent-side on the webagent coordinator + spawned workers (no send_later/self-trigger;
  self-arm attempts from those surfaces failed fleet-wide with recorded errors —
  create_trigger / trigger-binding rejections; the cross-session messaging wall below
  records the verbatim class); and cross-session trigger binding (rejected: **"binding a
  trigger to another session is not enabled for this organization"**). Owner-side,
  **this owner account's console lacked the routine/schedule option** at the 2026-07-10
  ~02:05Z paste session — but the Routines screen EXISTS on the owner's mobile browser
  (11:01Z recording, Samsung browser), so that console gap is per-device/per-surface,
  not absolute. **Wake substitute where self-arm isn't available:** timed watch
  workers (blocking foreground waits, R4) + a morning "continue"/boot message per Project;
  lanes operate **self-terminal** (every session leaves its work safe with no future wake
  needed). Rollout: wake-arm ORDERs dispatched to all active lanes 2026-07-10 (owner-queue
  item 7 — owner fallback only on a recorded lane failure).
- **claude.ai Project "Custom Instructions" field caps at 8,000 characters** (verified
  2026-07-10 ~02:05Z): two ~9k founding packages (websites 9,209 chars; trading-strategy
  8,980 chars) overflowed at paste and had to be re-trimmed live. **Recipe:** keep every
  founding text ≤7,500 chars (headroom for future edits); cut repetition and asides, never
  rules/rails/walls. The fitted texts actually deployed are recorded in
  `docs/proposals/instructions/{websites,trading-strategy}.md` § "Deployed fitted version" —
  fit new packages BEFORE handing the owner a paste.
- **Direct self-merge of own PRs in established repos** — blocked by the classifier
  (**"[Self-Approval]…Merge Without Review"**). **Arming auto-merge while checks are
  pending is the sanctioned path** — the wall blocks the direct merge call, not the arm.
  (Playbook R12.)
- **GraphQL quota exhausts at fleet scale (~hourly)** — REST merge-on-green is the
  fallback; ready-flips (draft→ready) are GraphQL-only, so wait for quota reset for those.
  (Playbook R8.)
- **Official devkitPro package installers/infra** — **Cloudflare 403** behind the fleet
  proxy (toolchain scout 2026-07-09). Don't re-probe; the working route is the
  leseratte10 mirror recipe in the CAN section above.
- **Force-push / amending pushed history** — never. Forward-only commits.
- **Cross-session agent messaging** — no `send_message`/`send_later` MCP tool exists in
  coordinator or worker sessions of this org (**"No agent named ... is reachable"**;
  trigger binding to another session rejected: **"binding a trigger to another session is
  not enabled for this organization"**). Working delivery channels = git control-files bus
  + PR comments on a PR the target session is subscribed to (delivery NOT guaranteed
  before close-out — see playbook R20).

- **Private repos on this GitHub plan cannot enable the auto-merge toggle** (appended
  2026-07-10, owner-verified: the owner flipped pokemon-mod-lab PUBLIC solely to reach
  the repo-settings *Allow auto-merge* toggle, and flipped it back PRIVATE after the
  manager's counter — the toggle simply is not offered on private repos on this plan).
  Never advise a visibility flip to get the toggle. **Resolution: REST merge-on-green
  needs no toggle (playbook R21)** — that is the standard landing path on private
  repos; `enable_pr_auto_merge` / arm-at-creation is a dead end there, don't probe it.
  Expect **rulesets / required-check features to be similarly limited on private repos**
  on this plan; where settings-enforced protection isn't available, single-writer lanes
  run **convention-enforced** (R9/R19: one writer per file, serialized inbox appends,
  born-red cards + claim files).

## DISCOVERY RULE

Before declaring anything impossible:

1. **Check this file.**
2. **Check `printenv`** (presence-grep above — the capability may be a provisioned credential).
3. **Attempt it once and capture the exact error** — verbatim, not paraphrased.

A new capability or wall discovered = **append it here (or your repo's copy) the same
session.** An unrecorded discovery is a reminder the owner will have to give again.
