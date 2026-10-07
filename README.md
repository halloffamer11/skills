# skills

Personal agent skills. Each one is self-contained: one directory under `skills/`, no
machine setup.

| Skill | Use |
|---|---|
| `facebook-marketplace` | Research, price, draft and post Facebook Marketplace listings |
| `fresh-context` | Wrap up a session so a fresh one can resume from files alone |
| `toolsmith` | Consulting on machine configuration, dotfiles and agent workflow |

## Install

This repo is also a plugin marketplace named `halloffamer11`. It lists two plugins:
`personal` (the skills above) and `delegate` (from
[halloffamer11/delegate](https://github.com/halloffamer11/delegate), with `delegate`
and `council`). The `delegate` plugin needs one-time machine setup: run
`delegate setup` after you install it.

| Environment | Install | Update |
|---|---|---|
| Claude Code | `claude plugin marketplace add halloffamer11/skills`, then `claude plugin install personal@halloffamer11` and `delegate@halloffamer11` (or `/plugin` in a session) | `claude plugin marketplace update halloffamer11`, then `claude plugin update <plugin>@halloffamer11`; or turn on auto-update for the marketplace in `/plugin` |
| Codex | `codex plugin marketplace add halloffamer11/skills`, then `codex plugin add personal@halloffamer11` and `delegate@halloffamer11` (or `/plugins` in a session) | `codex plugin marketplace upgrade halloffamer11` |
| Gemini CLI | `gemini extensions install https://github.com/halloffamer11/skills` (personal skills only) | `gemini extensions update personal` |
| ChatGPT | `sh scripts/zip-skills.sh`, then upload each `dist/<skill>.zip` in Skills, Create, Upload from your computer (personal skills only) | upload the new zip again |
| Any other agent | the skills CLI, below | `npx skills update -g` |

ChatGPT cannot install from a repository, and it has no shell on your machine, so
delegate does not run there.

Plugin versions follow the repo's commits: no plugin pins a `version`, so an update
picks up whatever is on `main`. Install a skill one way per machine. A plugin and a
skills CLI copy of the same skill both load.

### Skills CLI

Installs copies into the skill folders of Claude Code, Codex, Cursor, Kiro and many
other agents (`--agent` picks them).

```sh
npx skills add halloffamer11/skills -g                          # pick interactively
npx skills add halloffamer11/skills --skill toolsmith -g -y     # one skill
npx skills update -g                                            # later: pull new versions
```
