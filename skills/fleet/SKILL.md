---
name: fleet
description: Guide the owner through Belt maintenance on a macOS or Omarchy Machine managed by chezmoi. Use for Pack selection, tool and MCP changes, Site kits, cutover, drift reports, and stopped fleet-sync runs.
---

Version 1 may run only `fleet-check` (optionally `--brief`), from the project directory when its Git state matters. Explain the relevant finding and give the owner commands to run. This applies even to requests to update, install, repair, or enable a timer. If the check is unavailable, guide the owner using the procedures below.

## What needs updating?

| What changes | Who does it and when |
| --- | --- |
| Tool binaries | The owner attends upgrades. On Omarchy run `omarchy update`, which includes mise. On macOS run `mise up` for CLI tools and `brew upgrade` for Homebrew packages. |
| Shared configuration | Every four hours the Machine's `fleet-sync` checks for local edits, runs `git pull --ff-only` in the dotfiles source, then `chezmoi apply --no-tty --error-on-conflict`. |
| Skill contents | The last step of the same sync runs `skills update -g -y` for every installed global skill, including ad-hoc skills. The skills CLI records their sources and versions in its global lock file. |
| An owner's Belt change | Edit the source checkout, inspect `chezmoi diff` and try `chezmoi apply` interactively, even on a working branch. Review `git diff`, stage the intended paths with `git add -- PATH`, then `git commit` and `git push` on the intended branch. A site deployment keeps its changes in the Site kit. |
| A project repo | The owner and agents push the project branch when work ends, or report what is still local. A Machine can see another Machine's work only after it reaches their remote. |

Keep topgrade out of this sequence. Its chezmoi step can autostash and rebase past the sync checks, and its skill, mise and Harness steps can repeat updates owned elsewhere.

## Set up a Machine

On a new Machine, prepare any Site kit first. Install Git, mise and Python 3.11+ and put mise's shims and `~/.local/bin` on the login PATH. With chezmoi installed, run `chezmoi init --apply halloffamer11/dotfiles`. To supply chezmoi through mise, run `mise exec chezmoi@latest -- chezmoi init --apply halloffamer11/dotfiles`. Select the Packs and enter the T3 Antigravity provider instance IDs at the prompts. The Machine stores its answers locally.

On an occupied Machine, **back up before applying**. The skills CLI replaces same-name directories. Follow [the occupied Machine procedure](references/occupied-machine.md) for the local backup, restore check, ownership handoff and rollback.

After apply, open Codex, enter `/hooks`, inspect the SessionStart command pointing to `"$HOME/.local/bin/fleet-check" --brief` and trust it. Review and trust it again if the hooks file changes. In fresh direct and T3 sessions of each Harness, verify a distinctive global rule, discover a selected skill and call the declared Playwright server once. T3 needs version 0.1.11 or later for the Antigravity rules link.

After rehearsal and cutover, enable the four-hour timer. On Omarchy run `systemctl --user daemon-reload`, then `systemctl --user enable --now fleet-sync.timer`. On macOS load the deployed agent with `launchctl bootstrap "gui/$(id -u)" "$HOME/Library/LaunchAgents/org.dotfiles.fleet-sync.plist"`.

## Change Belt membership

These paths are relative to the dotfiles **repository root**. Use `git -C "$(chezmoi source-path)" rev-parse --show-toplevel` to find it. Apply changed declarations with `chezmoi apply`, then run `fleet-check`. Apply installs mise tools, selected skills and MCP entries in that order when their rendered inputs change. Removing a declaration leaves the installed copy for the owner to reconcile on each Machine.

- **Tool.** Add a key under `[tools]` in `home/.chezmoidata/tools.toml`, e.g. `jq = "latest"`. Use a version string to pin. The result is `~/.config/mise/conf.d/50-belt.toml`. The Omarchy template omits names already provided by pacman or the Platform's mise config. Desktop apps and system libraries belong to the Platform. On macOS apply Brewfile changes with `brew bundle`. To retire a CLI, remove its Belt declaration, apply, inspect `mise ls TOOL` and `which -a COMMAND`, then use `mise uninstall TOOL@VERSION` only for an installed version no remaining config or project needs. Keep Platform-owned copies.
- **Skill.** Publish authored procedures at `skills/NAME/SKILL.md` in their Pack. In `home/.chezmoidata/packs.toml`, set the Pack's `repo` and enable the name in its `skills` table. External skills take their original upstream repo. Select a new Pack with `chezmoi init --prompt`. To narrow one, set e.g. `core = ["toolsmith", "fleet"]` under `[data.skillSelection]` in the Machine's chezmoi config. Apply uses `skills add REPO -g -y -s NAME -a claude-code codex antigravity-cli`. Use that same command for a missing declared installation if the inputs have already been applied. To retire, remove its declaration or selection first, apply, then run `skills remove -g NAME` with no `-a`. Without `-a` it removes the shared copy in `~/.agents/skills`, every Harness link and the lock entry; with `-a` it removes only the links, and Codex still reads the shared copy. Keep Platform and Harness skills, and install a skill through one channel.
- **MCP server.** Add `[mcp.NAME]` in `home/.chezmoidata/mcp.toml` with either `command` and optional `args`, or `url`. Optional `platforms` takes `["macos"]` or `["omarchy"]`, and `requires` names a binary on PATH. `secrets` contains environment variable names only. The verified secret transport is Codex HTTP with a single bearer-token environment variable. Other secret-bearing transports are skipped. Inspect the entries locally with `claude mcp list`, `codex mcp list` and `agy mcp list`. The MCP script runs only when its rendered input changes, so an entry skipped for a missing `requires` binary, or removed by hand, is not added again by itself. Add it by hand with the command apply uses. For a `command` entry: `claude mcp add -s user NAME -- COMMAND ARGS`, `codex mcp add NAME -- COMMAND ARGS`, `agy mcp add NAME -- COMMAND ARGS`. For a `url` entry: `claude mcp add -s user --transport http NAME URL`, `codex mcp add NAME --url URL` (add `--bearer-token-env-var VAR` when the entry declares one secret), `agy mcp add --type http NAME URL`. Do not add a secret-bearing entry to a Harness that apply skipped. To retire, remove the declaration and apply. **Manually** remove the remaining user entry wherever installed with `claude mcp remove -s user NAME`, `codex mcp remove NAME` and `agy mcp remove NAME`. An undeclared entry may be an intentional ad-hoc install. Confirm its owner before removal.

## Use a Site kit

Run `mkdir -p ~/.config/fleet/site` or place a private checkout there. Use read-only upstream access on a site deployment. Each file is optional.

| File | Effect on this Machine |
| --- | --- |
| `rules.md` | Appends text to each Harness's global rules. Keep each rendered file under 24,000 bytes. |
| `mcp.toml` | Merges named MCP entries in the same schema as the core Manifest. |
| `skills.toml` | Merges named Packs. Select a new Pack with `chezmoi init --prompt`. Use `false` to disable an inherited skill. |
| `mise.toml` | Links into mise as `~/.config/mise/conf.d/90-site.toml`. Retiring the file also requires removing its old link. |
| `ignore` | Lists chezmoi target paths or patterns, one per line. The Machine owns any replacement for an ignored target. |

Site values win on overlapping keys. Inspect `chezmoi diff`, apply, and review reported overlaps with `fleet-check`. Keep the local entry until upstream supplies what the Machine needs. Keep private values and account aliases machine-local.

## Read the check and recover a stopped sync

Run `fleet-check` for the full report. The session hook uses `--brief`; silence means there were no findings. The full report also gives the last sync timestamp and result, or “never run”. Read the report text even when the process exits successfully.

| Finding | Owner's next step |
| --- | --- |
| Uncommitted, unpushed, upstream commits, no upstream | Inspect `git status -sb` in the named repo. A failed fetch uses the last fetched counts. Check connectivity and branch tracking before acting. |
| Edited deployed target | Inspect `chezmoi diff`, save the local copy, and incorporate wanted edits into the source or Site kit. Apply the reviewed result interactively. Column one of `chezmoi status --exclude=scripts` stops sync for locally edited targets except shared `modify_` files. Column two alone is pending work for apply. |
| Missing, undeclared, skipped | Check the selected Pack, Platform, binary on PATH or secret-reference support as applicable. Restore the intended selection or reconcile a retired item manually. A missing Pack declaration can leave a stale Machine selection. |
| Site kit overlap or ad-hoc mise tool | Check the Site kit or `~/.config/mise/config.toml`. Decide whether the local choice should travel. |
| Duplicate command or replaced T3 link | Inspect `which -a COMMAND` and its owners before retiring a copy. For a replaced T3 link, preserve any plain file, check the selected provider IDs and apply to restore the link to `~/.gemini/config/mcp_config.json`. |
| Check incomplete | Inspect the reported failure type and local declarations. Retry from the intended project with chezmoi and its prerequisites on PATH. |

For a stop, read `cat "${XDG_STATE_HOME:-$HOME/.local/state}/fleet/last-sync"`. The first failing step ends that run. For a dirty source, save the intended work in Git. For a failed fast-forward inspect `git status -sb` and `git log --oneline --left-right HEAD...@{upstream}` in the source checkout. Preserve both histories and let the owner reconcile them or restore the intended tracking branch. For an apply or skills failure, check the named command's prerequisites, PATH and upstream access. A pull or earlier installer may already have succeeded. Once resolved, run `fleet-sync` again and confirm a timestamped `ok` with `fleet-check`.
