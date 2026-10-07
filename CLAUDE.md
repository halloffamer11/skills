# Skills

Personal agent skills, installed on each machine with the `skills` CLI
(`npx skills add halloffamer11/skills -g`) and refreshed with `npx skills update -g`.
The repo is also a plugin marketplace for Claude Code and Codex, and it lists delegate
from its own repo. `README.md` has the install line for each environment.
Split out of `halloffamer11/dotfiles` on 2026-10-01 with its history. The repo is public.

## Rules

- One skill per directory under `skills/`. A skill here is self-contained: it must work
  after a plain `skills add`, with no Makefile step and no other repo. A skill that needs
  machine setup gets its own repo (as `halloffamer11/delegate` did).
- An installed skill is a copy. An edit here reaches a machine only after you push and
  run `npx skills update -g` there.
- The manifests are `.claude-plugin/marketplace.json` and `.claude-plugin/plugin.json`
  (Claude Code; Codex and the skills CLI read them too), `.agents/plugins/marketplace.json`
  (Codex, which cannot read a `github` source) and `gemini-extension.json`. A new skill
  needs no manifest change; a new plugin goes in both marketplace files. Check with
  `claude plugin validate .`. No plugin pins a `version`, so installs follow `main`.
- Never commit secrets or personal data; anyone can install from this repo.
