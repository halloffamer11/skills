# Authoring

Read before the first draft, and when a description, script or harness question comes up.

## Contents
- Frontmatter
- Description
- Body
- Degrees of freedom
- Scripts
- Harnesses
- Writing rules

## Frontmatter

The open standard ([agentskills.io/specification](https://agentskills.io/specification)) defines these fields:

| Field | Rule |
|---|---|
| `name` | Required. 1 to 64 characters: a-z, 0-9 and single hyphens, no hyphen at either end. Must equal the folder name. Do not use "anthropic" or "claude". |
| `description` | Required. 1 to 1024 characters. What the skill does and when to use it. |
| `license` | Optional. |
| `compatibility` | Optional, up to 500 characters. Use it only when the skill needs more than text: a shell, git, a browser, network. Also say it in one body line, because some harnesses strip frontmatter before the model sees it. |
| `metadata` | Optional map of string to string. |
| `allowed-tools` | Optional, experimental. |

`disable-model-invocation: true` is a Claude Code field, not in the standard. It makes the skill user-invoked there. Other harnesses may ignore it and show the description to the model, so a user-invoked description says "Explicit invocation only" and names no trigger phrases.

## Description

The description is the only text the agent sees before it loads the skill. Write it in this form:

`<Does what, third person>. Use when <one trigger per distinct case>. Not for <the nearest wrong case>.`

This fits both Anthropic's "third person" rule and the standard's "use when" advice. Name what the user is trying to do, not how the skill works. Keep each trigger a distinct case; synonyms of one case count once. Avoid "pushy" wording: the user has many skills in many harnesses, and each extra trigger costs context and false starts.

For a model-invoked skill, test the description: about 10 prompts that should start it and 10 near-misses that should not (the near-misses share words with the skill but need something else). Run them against the whole installed catalog, not the skill alone, because `skill-creator` and `writing-for-agents` also answer "make a skill".

## Body

- **Under 500 lines; aim for under 200.** Put in SKILL.md what every run needs. Move to `references/` what only some branches need, and point to it with "read X when Y".
- **One level deep.** SKILL.md points to each reference; references do not point onward to further references. Give a reference over 100 lines a contents list.
- **Steps end on a done-when line** the agent can check.
- **Gotchas inline.** A short list of the mistakes the agent makes without the skill, each from a real failure. This is often the most valuable part of the skill.
- **Defaults, not menus.** Give one default and the condition for the alternative.
- **No dated state.** A version, a price, a path on one machine goes stale. Point to where the agent finds it now (a file, `--help`, a doc URL). Put a superseded method under a short "Old way" heading only if users still meet it.
- **No extra docs** in the skill folder: no README or CHANGELOG. The repo README holds the row.
- **Consistent words.** One term per concept, used the same way throughout.

## Degrees of freedom

Match the bound to how fragile the step is:

| Step | Freedom | Write it as |
|---|---|---|
| Judgment work: research, review, drafting | High | Goals, criteria, what good looks like |
| A preferred pattern with some variation | Medium | A template or pseudocode with the parts that may change |
| Fragile or external: file formats, publishing, sending, money | Low | The exact command or sequence, and a stop for human approval before any external action |

Explain the reason behind a rule; a reason lets the agent handle the case the rule did not name. Keep a hard MUST only for a real guardrail, and state the target behaviour, not just the ban.

## Scripts

Add a script only for a step that is repeated, deterministic or fragile. Then:

- Python 3 standard library or POSIX shell, so it works after a plain `skills add`.
- No interactive prompts. Take input as arguments; give a short `--help`.
- Data on stdout, diagnostics on stderr, a non-zero exit code on failure, an error message that says how to fix it.
- Keep output short. Offer `--dry-run` for anything that changes state.
- Resolve paths from the skill folder, with forward slashes.
- In SKILL.md, say whether the agent runs the script or reads it.
- Run every script once before release.

## Harnesses

The user's skills install into Claude Code, Codex, Gemini CLI, Kiro and others, and as zips into ChatGPT (`scripts/zip-skills.sh` in the skills repo; no shell there). Keep shared text free of one harness's tool names. When a skill must reach Codex, add `agents/openai.yaml`:

```yaml
interface:
  display_name: "<Name>"
  short_description: "<one line>"
  default_prompt: "Use $<skill-name> to <task>."
```

Install one way per machine: a plugin copy and a skills-CLI copy both load. Plugins follow `main`, so a bad commit reaches every machine at the next update.

## Writing rules

Adapted from Matt Pocock's `writing-for-agents` skill (github.com/mattpocock/skills), so this skill stays self-contained:

- **Pointers decide reach.** The words of a pointer (a description, a "read X when Y" line) decide when the agent opens the target. Sharpen the wording before you inline the target.
- **Inline what every branch needs; disclose what only some branches reach.** Keep a concept's rules and caveats under one heading.
- **Sprawl is the failure.** A long file thins attention even when every line is live. Split by branch or by sequence.
- **Strong completion criteria** are checkable and exhaustive ("every changed file listed"), not vague ("understanding reached").
- **Leading words.** One well-known word ("tracer bullet", "red") can replace a sentence and anchor the behaviour. Prefer an existing word to a coined one.
- **Prompt the positive.** A ban names the banned behaviour and can make it more likely. State the target; pair any hard ban with it.
- **One source of truth.** Do not restate what the environment already says (config, `--help`, the directory layout); a copy goes stale. Write down only what the agent cannot look up: the unwritten convention, the reason, the gotcha.
- **Delete no-ops.** A sentence the model already obeys by default costs load and does nothing. Test by running, not by debate; delete the whole sentence.
