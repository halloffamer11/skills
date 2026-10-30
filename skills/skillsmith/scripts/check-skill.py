#!/usr/bin/env python3
"""Check one skill folder against the Agent Skills spec and the house rules.

Usage: python3 check-skill.py <skill-dir>

Prints one line per finding: ERROR (must fix) or WARN (fix, or say why it
stays). Exits 1 when there is an ERROR, else 0. Python 3 standard library only.
"""

import re
import sys
from pathlib import Path

SPEC_KEYS = {"name", "description", "license", "compatibility", "metadata", "allowed-tools"}
KNOWN_EXTRA = {"disable-model-invocation"}
NAME_RE = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
LINK_RE = re.compile(r"\]\(([^)#\s]+)(?:#[^)]*)?\)")
PRIVATE_RE = [
    (re.compile(r"/(?:Users|home)/[A-Za-z0-9._-]+/"), "a home-directory path"),
    (re.compile(r"[\w.+-]+@(?!example\.)[A-Za-z0-9-]+(?:\.[A-Za-z0-9-]+)*\.[a-z]{2,6}\b"), "an email address"),
]
SKIP_DIRS = {".git", "__pycache__", "node_modules"}

findings = []


def report(level, where, text):
    findings.append((level, f"{level} {where}: {text}"))


def frontmatter(text):
    """Return the top-level keys and their raw values, or None if absent."""
    lines = text.splitlines()
    if not lines or lines[0].strip() != "---":
        return None
    keys, current = {}, None
    for line in lines[1:]:
        if line.strip() == "---":
            return {k: " ".join(v).strip() for k, v in keys.items()}
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m and not line.startswith((" ", "\t")):
            current = m.group(1)
            value = m.group(2).strip()
            keys[current] = [] if value in (">", "|", ">-", "|-") else [value]
        elif current is not None:
            keys[current].append(line.strip())
    return None


def unquote(value):
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def check(skill):
    skill_md = skill / "SKILL.md"
    if not skill_md.is_file():
        report("ERROR", skill.name, "no SKILL.md")
        return
    text = skill_md.read_text(encoding="utf-8")
    fm = frontmatter(text)
    if fm is None:
        report("ERROR", "SKILL.md", "no YAML frontmatter between --- lines")
        return

    name = unquote(fm.get("name", ""))
    if not name:
        report("ERROR", "SKILL.md", "name is missing or empty")
    elif not NAME_RE.match(name) or len(name) > 64:
        report("ERROR", "SKILL.md", f"name '{name}' must be 1-64 of a-z, 0-9 and single hyphens")
    elif name != skill.name:
        report("ERROR", "SKILL.md", f"name '{name}' must equal the folder name '{skill.name}'")
    if "anthropic" in name or "claude" in name:
        report("ERROR", "SKILL.md", "name must not contain 'anthropic' or 'claude'")

    desc = unquote(fm.get("description", ""))
    if not desc:
        report("ERROR", "SKILL.md", "description is missing or empty")
    elif len(desc) > 1024:
        report("ERROR", "SKILL.md", f"description is {len(desc)} characters; the limit is 1024")
    if len(unquote(fm.get("compatibility", ""))) > 500:
        report("ERROR", "SKILL.md", "compatibility is over 500 characters")

    for key in sorted(set(fm) - SPEC_KEYS):
        why = "a Claude Code field; other harnesses may ignore it" if key in KNOWN_EXTRA else "not in the Agent Skills spec"
        report("WARN", "SKILL.md", f"'{key}' is {why}")
    if fm.get("disable-model-invocation", "").lower() == "true" and "explicit" not in desc.lower():
        report("WARN", "SKILL.md", "user-invoked skill: say 'Explicit invocation only' in the description")

    n = len(text.splitlines())
    if n > 500:
        report("ERROR", "SKILL.md", f"{n} lines; the limit is 500")
    elif n > 200:
        report("WARN", "SKILL.md", f"{n} lines; move branch-only detail to references/")

    for path in sorted(skill.rglob("*")):
        rel = path.relative_to(skill)
        if any(part in SKIP_DIRS for part in rel.parts) or not path.is_file():
            continue
        if path.name == "SKILL.md" and rel != Path("SKILL.md"):
            report("ERROR", str(rel), "nested SKILL.md; a harness may load it as a skill (build it in a fixture)")
        if path.suffix not in {".md", ".json", ".yaml", ".yml", ".sh", ".py", ".txt"}:
            continue
        body = path.read_text(encoding="utf-8", errors="replace")
        for pattern, what in PRIVATE_RE:
            m = pattern.search(body)
            if m:
                report("WARN", str(rel), f"contains {what} ({m.group(0)}); the repo is public")
        if path.suffix != ".md":
            continue
        for target in LINK_RE.findall(body):
            if re.match(r"^[a-z]+:", target):
                continue
            if not (path.parent / target).exists():
                report("ERROR", str(rel), f"link target '{target}' does not exist")
            elif rel.parts[0] == "references" and target.endswith(".md"):
                report("WARN", str(rel), f"links on to '{target}'; keep references one level deep")
        if rel.parts[0] == "references" and len(body.splitlines()) > 100 and "contents" not in body.lower()[:600]:
            report("WARN", str(rel), "over 100 lines with no contents list at the top")

    if not (skill / "evals" / "evals.json").is_file():
        report("WARN", skill.name, "no evals/evals.json")


def main(argv):
    if len(argv) != 2 or argv[1] in ("-h", "--help"):
        print(__doc__.strip())
        return 0 if len(argv) == 2 else 2
    skill = Path(argv[1]).resolve()
    if not skill.is_dir():
        print(f"ERROR {skill}: not a directory", file=sys.stderr)
        return 2
    check(skill)
    for _, line in findings:
        print(line)
    errors = sum(1 for level, _ in findings if level == "ERROR")
    print(f"{errors} error(s), {len(findings) - errors} warning(s)")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
