# First apply on an occupied Machine

These are owner-run commands. Rehearse in a throwaway home first. Keep the dated backup on the same Machine, outside every Git checkout.

1. Record one row per deployed path with its current owner, the Layer that takes it, a hand check and a reverse step. Include Makefile special cases, selected Stow packages and local overrides. Keep Layers outside the agentic cutover with their existing owner.
2. Prepare any Site kit. For a first clone run `chezmoi init halloffamer11/dotfiles` without apply. Review the Pack selection and provider instance IDs.
3. Start a POSIX shell with `sh` and use it throughout this procedure. Create a private backup. The skills CLI keeps its live lock file under `$XDG_STATE_HOME/skills/` when that variable is set; the backup takes it and the older `~/.agents/.skill-lock.json`. Preserve skill and rule symlinks as links **and** copy their resolved contents, so a later installer cannot destroy the saved data. Pause if a copy fails, including on a broken link. Identify its intended target before proceeding.

```sh
backup_root="${XDG_STATE_HOME:-$HOME/.local/state}/fleet/backups"
backup=$(mkdir -p "$backup_root" && mktemp -d "$backup_root/$(date +%Y%m%d)-XXXXXX") &&
  [ -d "$backup" ] && export backup || { backup=; echo "No backup folder. Stop here." >&2; }
[ -n "$backup" ] && (
  # Inside the subshell only: a failure does not close the terminal, and the
  # strict umask does not reach the later chezmoi apply.
  set -eu
  umask 077
  cd "$HOME"
  for path in .agents/skills/* .claude/skills/* .codex/skills/* .gemini/config/skills/* \
              .agents/.skill-lock.json .claude/CLAUDE.md .codex/AGENTS.md .gemini/AGENTS.md; do
    [ -e "$path" ] || [ -L "$path" ] || continue
    case "$path" in */synced|*/.system) continue ;; esac
    if [ -d /usr/share/omarchy ] || [ -d "$HOME/.local/share/omarchy" ]; then
      case "$path" in */omarchy|*/omarchy-app|*/diagnose-crash) continue ;; esac
    fi
    mkdir -p "$backup/links/$(dirname "$path")" "$backup/contents/$(dirname "$path")"
    cp -pRP "$path" "$backup/links/$path"
    cp -pRL "$path" "$backup/contents/$path"
  done
  lock="${XDG_STATE_HOME:-$HOME/.local/state}/skills/.skill-lock.json"
  if [ -e "$lock" ]; then
    mkdir -p "$backup/state"
    cp -p "$lock" "$backup/state/skill-lock.json"
  fi
)
```

Compare an edited skill before continuing. For a restore trial set `skill` to an actual path relative to HOME (for example `.agents/skills/toolsmith`), then run these commands. A clean comparison prints nothing. For a linked skill, the link tree preserves the original target spelling and the contents tree holds a standalone copy.

```sh
: "${backup:?run step 3 first}"
trial=$(mktemp -d)
cp -pR "$backup/contents/$skill" "$trial/restored"
diff -r "$HOME/$skill" "$trial/restored"
```

4. Back up only the user MCP entries the owner recognizes. Run this Python 3.11+ command in the same terminal. It shows names, then asks about each. Include user-installed ad-hoc servers. Skip Claude connectors, plugin entries and bundled servers, including Codex's bundled servers. Each JSON backup holds the original configuration fields and can contain credentials. The backup folder is private (mode 700, from `mktemp -d`), and the command runs with `umask 077`. Keep it private; use it locally to reconstruct a chosen entry with its Harness CLI.

```sh
(umask 077; python3 - <<'PY'
import json, os, tomllib
from pathlib import Path

home, dest = Path.home(), Path(os.environ.get("backup", ""))
if not dest.is_absolute() or not dest.is_dir():
    raise SystemExit("No backup folder. Run step 3 first.")
files = [
    ("claude", ".claude.json", "mcpServers"),
    ("codex", ".codex/config.toml", "mcp_servers"),
    ("agy", ".gemini/config/mcp_config.json", "mcpServers"),
]
with open("/dev/tty") as tty:
    for harness, filename, key in files:
        path = home / filename
        if not path.exists():
            continue
        with path.open("rb") as src:
            data = tomllib.load(src) if path.suffix == ".toml" else json.load(src)
        saved = {}
        for name, entry in data.get(key, {}).items():
            if name.startswith(("claude.ai", "plugin:")):
                continue
            print(f"Back up user-installed {harness} entry {name!r}? [y/N] ", end="", flush=True)
            answer = tty.readline()
            if not answer:
                raise SystemExit("Backup interrupted")
            if answer.strip().lower() in ("y", "yes"):
                saved[name] = entry
        (dest / f"{harness}-mcp.json").write_text(json.dumps(saved, indent=2) + "\n")
        print(f"{harness}: saved {len(saved)} entries")
PY
)
```

5. For each **selected** T3 Antigravity profile with a plain `config/mcp_config.json`, preserve that file before chezmoi creates the symlink. List the configured paths, then set `path` to each printed path in turn. Existing symlinks do not need moving.

```sh
chezmoi execute-template '{{ (includeTemplate "declarations" . | fromJson).profileLinks | join "\n" }}'
# path is the selected path relative to HOME
: "${backup:?run step 3 first}"
if [ -f "$HOME/$path" ] && [ ! -L "$HOME/$path" ]; then
  mkdir -p "$backup/profiles/$(dirname "$path")" &&
    mv "$HOME/$path" "$backup/profiles/$path"
fi
```

6. Release the paths in one ownership row at a time. Set `checkout` to the existing Stow checkout, `package` to the row’s package name and `target` to its absolute deployed path. For a whole Stow package use `stow -n -D -d "$checkout/stow" -t "$HOME" "$package"` to preview and drop `-n` only when every affected path is ready. For a mixed package or a Makefile-owned link, release the individual path and retire its old provisioning step before the next Stow run. Move any conflicting real file into the backup. Inspect `chezmoi diff "$target"`, then `chezmoi apply -P "$target"` for that target (`-P` also creates missing parent folders, such as `~/.config/mise/conf.d`). Record the hand check. Run full `chezmoi apply` only after all first-scope paths are ready for their installers. Finish the hook trust, fresh-session checks and timer steps in the main skill.
7. To reverse a Layer, stop its timer first (`systemctl --user disable --now fleet-sync.timer` on Omarchy, or `launchctl bootout "gui/$(id -u)/org.dotfiles.fleet-sync"` on macOS). Release the Layer from chezmoi management before another apply, move the deployed copies aside, restore any wanted local contents, links and user MCP entries, and restow its old package from the current fallback checkout with `stow -R -d "$checkout/stow" -t "$HOME" "$package"`. Verify the recorded hand check before re-enabling sync.
