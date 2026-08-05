# 2026-08-05 · hub — what a playtest Discord needs, and which bot parts serve it

> **Status:** `in-progress`

- **📊 Model:** opus-5 · high · docs-only

Time: 2026-08-05 · venue: owner-live hub chat · branch
`claude/swingy-spider-play-submission-wno3nb`

💡 Session idea: the owner owns a 61-extension Discord bot and needs a server
that does about nine things. The interesting question is not "what can the bot
do" but "what does this specific job need, and what of that is already live" —
and those two sets overlap far less than the bot's size suggests.

## Previous-session review

PR #171 recorded the trademark register search. The Play track needs 12 Android
testers opted in for 14 continuous days; a Discord server is the recruiting and
feedback vehicle for that, which is why this question arrived now.

## Planned

- `docs/findings/2026-08-05-playtest-discord-and-superbot-value.md` — Discord's
  own playtest-server guidance (fetched), the verified deployment state of both
  bots, and a ranked map of which subsystems serve this job.

## Verification

To run: `python3 tools/check_no_false_walls.py --strict` and
`python3 bootstrap.py check --strict`, both post-commit, real exit codes.
