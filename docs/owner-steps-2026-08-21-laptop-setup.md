# Laptop setup — Claude Desktop + Claude Code on the Galaxy Book6 Pro

> **Status:** `owner-guidance` · written 2026-08-21 for the owner's new laptop.
>
> **What this is:** the one sitting that gets Claude Code running locally, and
> an honest account of what that changes. Every command below is paste-ready;
> nothing here asks you to go and find something.
>
> **Sources:** Anthropic's own [setup](https://code.claude.com/docs/en/setup)
> and [desktop](https://code.claude.com/docs/en/desktop) docs, both fetched and
> read in full 2026-08-21. Where this file and those docs disagree, they are
> right and this file has aged.

## The machine decides the installer — yours is x64

The **Galaxy Book6 Pro** runs an **Intel Core Ultra X7 358H** (Panther Lake).
That is an **x64** processor, so you want the **x64** installer, not the ARM64
one. Both are offered on the same download page and picking the wrong one is the
most likely way this goes wrong — the links below are already the right one.

Claude Code needs a **Pro, Max, Team, Enterprise or Console** plan. You already
have one (it is what you are using right now), so there is nothing to buy.

## ⚑ OWNER — the one sitting, about 15 minutes

Do these in order. Step 1 before step 2 saves you an app restart.

### 1 · Git for Windows — required, do it first

The Code tab **will not start a local session without Git**. It also powers
session isolation, so this is not optional on Windows.

Download: **<https://git-scm.com/downloads/win>** — take the **64-bit standalone
installer**, and click through with every default. Nothing on those screens needs
a decision from you.

*(If a repo ever says "Git LFS is required", install it from
<https://git-lfs.com/>, then run `git lfs install` once.)*

### 2 · Claude Desktop — the x64 installer

Direct download, already the right build for your chip:

**<https://claude.ai/api/desktop/win32/x64/setup/latest/redirect>**

Fallback if that link ever 404s: <https://claude.com/download> → **Windows** →
choose **x64** (not ARM64).

Run it. It does not need Administrator.

### 3 · Sign in, then open the Code tab

Launch Claude and sign in with the same account you use on the web. You get
three tabs: **Chat**, **Cowork**, and **Code**. Click **Code**.

Before your first message, the prompt area asks for four things:

- **Environment** → choose **Local**. *(This is the answer to "enable Claude
  Code locally" — Local means it runs on this laptop, against real files. The
  other options are Cloud, an SSH machine, or a WSL distribution.)*
- **Project folder** → the repo you want to work in.
- **Model** → your pick, changeable mid-session.
- **Permission mode** → how much Claude does without asking.

If you see **"Git is required"** here, Git from step 1 did not finish — install
it and **restart the app**.

### 4 · The terminal command — optional, one line

This is the same Claude Code as a terminal command. Handy for the health check
in the verify step, and for running it outside the app.

Open **PowerShell** (your prompt shows `PS C:\`) and paste:

```powershell
irm https://claude.ai/install.ps1 | iex
```

Then **open a new terminal window** — PATH only updates in new sessions.

### verify — both should succeed

```powershell
claude --version
```

Prints a version like `2.1.211 (Claude Code)`.

```powershell
claude doctor
```

Prints a read-only health report without starting a session — install health,
settings errors, and suggested fixes for anything it finds.

**And in the app:** the Code tab opens a **Local** session on a folder you
picked, and it can list that folder's files.

## What this actually changes

You already have Claude Code — on the web, in remote containers. So the honest
question is not "what can Claude do" but **what a local machine reaches that a
cloud container never can.** These are the real ones for your estate.

### It can see and play what you are building

Claude starts your dev server and opens it in a **Browser pane**: it takes
screenshots, inspects the page, clicks elements, fills forms, and fixes what it
finds — by default it auto-verifies after every edit.

For **couch-legend** that is the difference between changing a number and
watching the game respond to it. The Android/Capacitor shell is that repo's NEXT
thread, and a local machine is where a shell like that gets run rather than
merely built.

### It reaches real hardware and real toolchains

A cloud container has no USB port and no desktop. Your laptop has both. That
puts three things in reach that were previously out of it:

- **A phone on a cable** — `phone-controller` is a Bluetooth-HID Android app,
  and both games are Android-bound. Install, run, and watch on the actual device.
- **The Godot editor** — `spider-swing` is Godot 4.7.1, and its north star is
  *core-feel tuning*. That work needs someone to actually play the thing.
- **Whatever else you install**, seen by the same session that writes the code.

### It can drive apps that have no command line

**Computer use** lets Claude control your screen — open apps, click, type — for
things nothing else can reach: native apps, hardware control panels, proprietary
tools without an API. The Godot editor and the Play Console are exactly this
shape.

It is a **research preview**, **Pro or Max only**, and **off by default**. Turn
it on at **Settings → General → Computer use**; on Windows the toggle takes
effect immediately, with no extra system permissions to grant. Claude asks
before using each app the first time.

Worth knowing: it is deliberately the *last* resort. Claude prefers a connector,
then Bash, then the browser — and browsers are capped view-only, terminals and
IDEs click-only, so screen control stays reserved for things with no better path.

### Several jobs at once, without them colliding

**Ctrl+N** opens another session in the sidebar. For a Git repo, each session
gets **its own worktree** — an isolated copy — so two sessions cannot tread on
each other. Hold **Ctrl** and click a session to view two side by side.

This is what lets "one thing at a time, finished properly" coexist with having
four repos in flight: each thread is genuinely separate rather than politely
taking turns.

### It watches your PRs on your own screen

Open a PR and a **CI status bar** appears in the session. **Auto-fix** lets
Claude read failing checks and iterate until they pass; **Auto-merge** merges
once they do. You get a desktop notification when CI finishes.

This needs the GitHub CLI (`gh`) installed and signed in — the app offers to
install it the first time you create a PR, so there is nothing to do in advance.

### The repo's own setup finally loads the way it is meant to

This one is specific to how this estate is built. Claude Code loads its hooks,
skills and boot file from the **one folder you open** — and in a remote
container holding several repos at once, that folder is the shared parent, so
**every repo's setup goes quiet with no error**.

Locally, each repo is its own folder. Open `fleet-manager` and the hub's hooks
and skills load. Open `spider-swing` and that repo's do. You pick the project
folder in step 3, so you get the right apparatus every time, by construction.

### Smaller things that add up

- **Attach images and PDFs** straight into a session — not possible in the
  terminal. Directly useful for the generated-asset work.
- **Connectors** — Google Calendar, Slack, GitHub, Notion and more, via the
  **+** button in local sessions.
- **Dispatch** — message a task from your **phone**; it can spawn a Code session
  on this laptop and push-notify you when it finishes. Pro/Max only.
- **Scheduled tasks** for recurring work, without writing a cron job.
- **An integrated terminal** (Ctrl+`) sharing the session's working directory,
  and a file editor pane.

## The honest limits

- **Native Windows does not support sandboxing.** Sandboxed command execution
  needs **WSL 2**. On native Windows, a high-autonomy session runs unsandboxed
  against your real machine. If that matters for a given job, run that job in a
  WSL distribution instead — the environment dropdown offers it.
- **Computer use and Dispatch are Pro/Max only** — explicitly not available on
  Team or Enterprise plans.
- **Some CLI features are terminal-only**: scripting (`--print`, the Agent SDK),
  agent teams, and third-party model providers. Desktop talks to Anthropic's API.
- **Local and cloud sessions do not see each other.** A session in the app lists
  only other desktop sessions, not your cloud ones or terminal ones.
- **Auto-update** applies to the native install; if you ever install via WinGet
  or Homebrew instead, you update those yourself.

## If something goes wrong

- **`claude` not found after installing** → open a *new* terminal window; PATH
  only updates in new sessions.
- **"Git is required"** in the Code tab → install Git for Windows, restart the app.
- **Claude cannot find `npm`/`node`** → check they work in your own terminal
  first, then restart the app so it re-reads your environment.
- **Anything else** → `claude doctor`, then Help → Get Support in the app.
