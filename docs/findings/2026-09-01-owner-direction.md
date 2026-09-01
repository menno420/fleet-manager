# Owner direction, 2026-09-01 — the first Fable 5.1 sitting: the mail, the successor, the hooks, and the automerger

> **Status:** `reference` · owner-live, on his new laptop (venue `local-desktop`,
> Claude Desktop's Code tab). `OWNER` throughout unless marked `DERIVED`. Same
> job as [`2026-08-28-owner-direction.md`](2026-08-28-owner-direction.md): his
> words verbatim, typos included, so that anything derived from them can be
> checked against source. Nothing here is a design; every mechanism sketched
> from these words is `DERIVED` and lives in the plans this record feeds.
>
> **Context:** he opened his first session with Fable 5.1 to test its reasoning
> on open-ended repo work, review the previous session's consolidation
> (fm #1008), and plan the successor repository's structure. Mid-session he
> redirected the priority to the final EAP review mail and answered the six
> structure questions the session had put to him. The session's own output is
> on his laptop hub: `OneDrive\Hub\records\2026-09-01 estate-successor-planning\`
> (seven files: the proposal and its evidence) and the artifact page linked
> from it.

## 1 · Why the successor exists, in one sentence — and what "done" looks like to him

> *"So the eventual goal is to make the new repo in such a way that every topic
> is explained in a short, properly named file inside a properly named folder.
> I believe that this will help tremendously."*

> *"I'm hoping to create the repos in such a way that any agent reading it, or
> working in it knows exactly what the purpose is and why the goals are what
> they are. So eventually I hope to achieve such a good and clear documentation
> that any agent can work on any repo with little to no input from my side.
> This is already true in some ways, and was especially true in /superbot before
> the EAP was announced."*

> *"I'm trying to explain everything as properly as I can so that eventually my
> true intent becomes a documented fact in the fleet-manager (or its successor)
> repo. This is especially important because there is a certain why that I like
> things to be done. So I can be confident that all the work landing in the
> repos is done according to a high standard."*

`DERIVED`: the acceptance test he names is *little to no input from my side*,
and the baseline he names for it is pre-EAP `/superbot`. That gives the
successor a measurable target and a historical control.

## 2 · The two ideas behind fixing agent mistakes — hooks at the moment, and structure

> *"My main idea for this is both to incorporate multiple hooks and skills that
> inject the right rules and questions around the time where the errors happen
> most. The other idea is to create a new repo that's better structured and
> easier to navigate, so the agents and me can find the right files faster and
> don't have to read trough immensely long files."*

> *"I was also thinking about certain other sessionstart hooks that would take
> care of some of the things that this continuation prompt provides, like that
> you should state back the goal to me and also include what you believe to be
> my intent but wasn't mentioned yet. The main reason for this is because I
> don't always use the continuation prompt and I still think it's very useful
> if the session I start tells me exactly what it thinks it's task is. This is
> because that allows me to correct it before any major work happens."*

`DERIVED`: the second quote is now a mechanism on his laptop — a first-prompt
hook that injects a four-line restatement (HE SAID · ALREADY SETTLED · I INFER
· LEAST SURE) and a post-compaction re-anchor; laptop-hub decision 39
there (OneDrive\Hub\decisions.md). The estate-side twin belongs in substrate-kit's SessionStart composer
(plan input). The `continuation-prompt` skill's restate block is aligned to the
same four lines in the PR that lands this record.

## 3 · The mail and the successor are one thread

> *"And you are sort of right that the email has priority, tho the new repo is
> also important. I believe that these are not perse two separate tasks, they
> will compliment each other. If we work on one of these tasks, it will help
> towards the other aswell. Since both of these tasks are related to the same
> root cause."*

> *"I noticed that much of the work that was claimed to be complete was in fact
> not complete at all. Which is definitely something to review closely and
> mention in the final EAP mail, which I still haven't send."*

> *"I have been a little overworked because of all the repos I had to manage
> and also I wanted to make sure that this final email provided something
> valuable other than just a normal review of the Projects, meaning that I
> wanted to really look into what the Projects did and also what the agents in
> general did and their mistakes."*

> *"Especially the email is something that feels like a big obstacle for me,
> mainly because I don't want it to seem too repetitive. I want to show
> Anthropic that my review is valuable and made with a lot of effort. I hope
> that they will choose me again for another EAP whenever they are thinking of
> adding a new feature."*

> *"Anthropic claimed that they want to make the Projects publicly available
> around October. This is why I think that we should really start to focus on
> that a but more, preferably getting it ready in the next couple of days."*

> *"A few days ago I ran an ultracode audit with nearly a thousand agents which
> mapped all the errors across the repos. This was possibly because I made sure
> (or at least I tried) to have all my agents keep a journal where they explain
> something about their session and the things that went well or went wrong."*

> *"All the audits are in fleet-manager, and the problem is that they are not
> all properly mapped in the audits folder. They are all made in the last few
> days so it shouldn't be too hard to find."*

`DERIVED`: the mail's evidence pass and the successor's failure→mechanism map
are one fan-out over one corpus (the 2026-08-28/29 audits, the raw 284-pattern
catalogue under `docs/findings/data/`, the prior mails). Its output is read
twice: as findings for Part 2, and as traps, hook moments and folder rules for
`estate`. His "nearly a thousand agents" is the 2026-08-29 estate-agent-error
audit: 986 agents, of which 80 read the corpus.

## 4 · The hooks in one repository are deliberate

> *"One thing I'd like to add is that it was deliberate that only one repo has
> these hooks etc. I always use fleet-manager as the root repo for a cloud
> session. So all the hooks and skills get loaded every time, if a session
> later adds another repo to it's scope that does not remove the functionality
> of the hooks and skills. Only if I personally attach 2 or more repos to a
> session at start then the hooks and skills do not load"*

`DERIVED`: this corrects a reading in
[`2026-08-29-estate-agent-error-audit.md`](2026-08-29-estate-agent-error-audit.md)
§ 4 that treated "hook files in 1 of 20 repositories" as a gap. It is a design
choice for cloud sessions, recorded as [D-0038]. What stays uncovered: a
session started with two or more repos attached, Codex and ChatGPT Work
sessions, and local sessions opened directly in a repo clone; and `estate`
inherits the role of root.

## 5 · The rules he set during the EAP, and the automerger he now doubts

> *"I have been "fighting" the agents so to say, to get my true intent through.
> Especially since the EAP, where a lot of agents were working in parallel on a
> lot of repo, I had to set some rules to prevent certain things like
> documenting false walls from becoming a real problem."*

> *"Now I'm still working on finding and correcting some of these rules, like
> the fact that there is now an automerger in the repo(s), which was necessary
> because these projects had told themselves that they could not merge my PRs
> themselves. Tho that was literally their task. This automerger is not really
> a problem, tho I'm wondering if it's really necessary since my agents can all
> merge PRs themselves."*

`DERIVED`, put to him as a one-letter question (G) and **not yet answered**:
the session's recommendation is no automerger in `estate` from birth — the
agent merges as the deliberate last step after the review it requested has
answered on that head — with the kit release after the revised plan removing
the enabler elsewhere. Evidence for the cost: `docs/traps.md` TRAP-006
(fm #915 merged 37 s after opening, zero reviews) and TRAP-007 (fm #937 merged
a head missing round-2 fixes).

## 6 · His own involvement is changing

> *"I just recently got a new laptop which I'm using now to run Claude locally.
> This means that you have full access over my PC and the Chrome extension,
> that doesn't change too much for you since you also have access too some of
> my account scoped tokens, for GitHub and Railway. You can freely see and edit
> everything in my accounts there, this is because I personally don't have a
> lot of knowledge how that all works. I am trying to understand it all better,
> especially now with my new laptop I want to get more involved with the repos.
> Previously I never really opened a repo and definitely didn't edit anything
> myself. That's changing now since I can use VScode to easily view and edit
> the repos when I want/need to. I want to learn more about how everything
> works and understand better how my agents work."*

`DERIVED`: owner-facing output should assume he will open it in VS Code or on
GitHub's web view, not only read it in chat. His clone-free reading route in
VS Code was set up the same evening by a Codex session; the stale personal
clone in `C:\dev` was deleted on his word (F=1).

## 7 · The six structure questions — all defaults

> *"Also for the estate blueprint you made, I believe we can go with all
> defaults."*

The six, as put to him (the full record is the hub folder named above; the
decisions landed here are [D-0033], [D-0034], [D-0035] and [D-0038] — two numbers in between are skipped because their tokens already appear in this repository's records citing other repositories' decisions): **A** archive shape
`archive/<role>/<YYYY-MM>/<original path>` plus a generated manifest · **B**
file length soft cap 120 lines advised at write time, hard cap 200 fails
preflight, `evidence/` and `archive/` exempt · **C** install the restate hook
on the laptop now (done, hub decision 39) · **D** land the restate fix in
`continuation-prompt` and `prompt-preflight` now (this PR) · **E** build order:
thin seed → blind cold test → write cutover → deeper machinery, with only kit
changes K1–K5 before the seed · **F** delete the stale personal clone (done).
