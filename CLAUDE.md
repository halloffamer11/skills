# Skills

Personal agent skills, installed on each machine with the `skills` CLI
(`npx skills add halloffamer11/skills -g`) and refreshed with `npx skills update -g`.
Split out of `halloffamer11/dotfiles` on 2026-10-01 with its history. The repo is public.

## Rules

- One skill per directory under `skills/`. A skill here is self-contained: it must work
  after a plain `skills add`, with no Makefile step and no other repo. A skill that needs
  machine setup gets its own repo (as `halloffamer11/delegate` did).
- An installed skill is a copy. An edit here reaches a machine only after you push and
  run `npx skills update -g` there.
- Never commit secrets or personal data; anyone can install from this repo.
