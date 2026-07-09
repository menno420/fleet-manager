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

## WALLED — verified walls (quote the observed error, don't paraphrase)

- **Tag push, GitHub Release creation, remote branch deletion** — fail with **403 at the
  credential layer** → owner action required. Queue it in `docs/owner-queue.md` per R16/R17.
- **Creating/editing claude.ai environments, routines, or Projects** — no API surface for
  the agent → **owner clicks** in the claude.ai UI.
- **Direct self-merge of own PRs in established repos** — blocked by the classifier
  (**"[Self-Approval]…Merge Without Review"**). **Arming auto-merge while checks are
  pending is the sanctioned path** — the wall blocks the direct merge call, not the arm.
  (Playbook R12.)
- **GraphQL quota exhausts at fleet scale (~hourly)** — REST merge-on-green is the
  fallback; ready-flips (draft→ready) are GraphQL-only, so wait for quota reset for those.
  (Playbook R8.)
- **Force-push / amending pushed history** — never. Forward-only commits.

## DISCOVERY RULE

Before declaring anything impossible:

1. **Check this file.**
2. **Check `printenv`** (presence-grep above — the capability may be a provisioned credential).
3. **Attempt it once and capture the exact error** — verbatim, not paraphrased.

A new capability or wall discovered = **append it here (or your repo's copy) the same
session.** An unrecorded discovery is a reminder the owner will have to give again.
