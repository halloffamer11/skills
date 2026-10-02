# skills

Personal agent skills. Each one is self-contained: one directory under `skills/`, no
machine setup.

| Skill | Use |
|---|---|
| `facebook-marketplace` | Research, price, draft and post Facebook Marketplace listings |
| `fresh-context` | Wrap up a session so a fresh one can resume from files alone |
| `toolsmith` | Consulting on machine configuration, dotfiles and agent workflow |

## Install

```sh
npx skills add halloffamer11/skills -g                          # pick interactively
npx skills add halloffamer11/skills --skill toolsmith -g -y     # one skill
npx skills update -g                                            # later: pull new versions
```
