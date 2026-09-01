# `spider-bot` — what I think you intend

## Current evidence

`VERIFIED`: Spider Bot is the live AI community bot for the Slingy Spider
Discord server. It supports the tester funnel, human roster, feedback path,
server management, and AI conversation. Pushes to `main` deploy to a real
Railway worker.

## My interpretation

`DERIVED`: this repository exists to give the game community a clean, safe bot
that can be improved without inheriting the old SuperBot architecture. It is
both operational infrastructure and part of the server experience.

`DERIVED`: its first finish line is a reliable tester/community loop, but it may
grow into a community product if you want the server to outlive the closed test.

`VERIFIED`: this repository already has its own dedicated intent file,
[`docs/repos/spider-bot/intent.md`](../../../docs/repos/spider-bot/intent.md),
answered in part on 2026-08-28:

> *"Superbot itself is a repo that's filled with too much history, too many
> trials and errors. What I want from spiderbot and superbot-next... is that
> they eventually are rebuild as one real well functioning bot thats build
> right from the start... The goal is to create a bot without architectural
> debt for as far as that's possible. Everything should be planned and
> connected from the start so it remains manageable and able to grow
> indefinitely."*

That file's own four open questions are the same four below (tool-vs-community,
what people should feel, the stop condition, and the deploy-gate looseness) —
answering here answers there too, no need to write it twice.

## Questions for you

1. Is Spider Bot mainly a tool for the game, or a community product in its own
   right?
2. What should people feel about the bot: quiet utility, server character, or
   something between?
3. What should happen to it if the closed test ends and the community stays small?
4. Which actions should it never take without a human?
5. Is direct deployment from `main` deliberate, or merely how the repo started?
6. What would make you consider the tester and feedback funnel complete?

## Your words

`OWNER`:

