# skills

The core Pack holds shared procedures for agents. Each skill lives under `skills/`.
Facebook Marketplace moved to the [personal Pack](https://github.com/halloffamer11/skills-personal).

| Skill | Use |
|---|---|
| `council` | Multi-model council for a critical decision, in any harness (run it by name) |
| `fleet` | Read Belt drift and guide an owner through updates, Machine setup and recovery |
| `fresh-context` | Wrap up a session so a fresh one can resume from files alone |
| `skillsmith` | Design, test and maintain agent skills, evals first (run it by name) |
| `toolsmith` | Consulting on machine configuration, dotfiles and agent workflow |

## Install

Fleet Machines use the skills CLI for Claude Code, Codex and Antigravity CLI:

```sh
skills add halloffamer11/skills -g -y -s council fleet fresh-context skillsmith toolsmith -a claude-code codex antigravity-cli
```

Existing plugin installations use the marketplace name `halloffamer11` and plugin
ID `personal`. That ID continues to deliver this repository's core skills.

| Environment | Install | Update |
|---|---|---|
| Claude Code | `claude plugin marketplace add halloffamer11/skills`, then `claude plugin install personal@halloffamer11` (or `/plugin` in a session) | `claude plugin marketplace update halloffamer11`, then `claude plugin update personal@halloffamer11`; or turn on auto-update for the marketplace in `/plugin` |
| Codex | `codex plugin marketplace add halloffamer11/skills`, then `codex plugin add personal@halloffamer11` (or `/plugins` in a session) | `codex plugin marketplace upgrade halloffamer11` |
| Gemini CLI | `gemini extensions install https://github.com/halloffamer11/skills` | `gemini extensions update personal` |
| ChatGPT | `sh scripts/zip-skills.sh`, then upload each `dist/<skill>.zip` in Skills, Create, Upload from your computer | upload the new zip again |
| Any other agent | the skills CLI, below | `npx skills update -g` |

ChatGPT cannot install from a repository, and it has no shell on your machine.

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
