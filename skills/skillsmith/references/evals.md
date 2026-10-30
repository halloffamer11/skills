# Evals

Read when you write or change a skill's eval cases, and before you grade.

## The file

Each skill keeps its cases in `evals/evals.json`. It works in any harness and needs no tooling.

```json
{
  "skill_name": "<skill-name>",
  "notes": "How fixtures are built, what the executor may and may not do, what it writes.",
  "evals": [
    {
      "id": 0,
      "name": "short-kebab-name-of-what-is-tested",
      "fixture": "fixtures/<name>.sh",
      "prompt": "The user's message, as they would type it.",
      "session": "Optional: the history the executor is told it already has.",
      "expected_output": "One or two sentences: what a good run does.",
      "assertions": [
        "One checkable fact about the result, with the file it lives in."
      ]
    }
  ]
}
```

`fixture` and `session` are optional. Add a case for each baseline failure from step 3, and one for a boundary the skill must respect (a request it must refuse or hand back). Three good cases beat ten weak ones.

Never convert, reorder or rewrite an existing `evals.json`; append. Anthropic's `skill-creator` writes per-case folders for `claude plugin eval`; keep `evals.json` here unless the user asks for CI runs.

## Fixtures

A fixture is a POSIX shell script that builds a throwaway sandbox: `sh evals/fixtures/<name>.sh <dest>`. It refuses to overwrite an existing `<dest>`, creates a git repo when the skill works on one, and uses made-up data only (`fixture@example.com`, invented names and amounts).

Build any sample skill a case needs inside the fixture script, never as a committed SKILL.md under `evals/`. Harnesses scan several folders deep and can load a committed SKILL.md as a real skill.

Fixtures never touch a real account, site or machine. Mock external actions; passing a fixture does not prove the live action works, so say so.

## The executor

The executor runs one case in a clean context (a subagent, a fresh session or a delegate lane). It cannot ask the user, so the `notes` must say:

- what it writes: the message it would send to `outputs/reply.md`, each command it ran to `outputs/commands.txt`, any question it would have asked to `outputs/questions.md`;
- what the `session` pre-approves, and that nothing else is approved.

Record which skill copy each run loaded (the path), because an installed copy can shadow the one under test. A baseline run must not load the skill at all.

## Grading

- Grade each assertion PASS or FAIL with quoted evidence from the outputs, the commands or the files. No evidence is a FAIL.
- Check mechanical facts with a command (file exists, file unchanged, exit code), not by reading.
- Write assertions about the result ("CLAUDE.md has no Current focus section"), not about where this run saved it.
- Flag an assertion that passes for both the baseline and the skill: it tests nothing, unless it guards a safety rule.
- Flag an important outcome that no assertion checks.
- Freeze assertions that guard safety or the user's rules. Never weaken an assertion to make a failing run pass; fix the skill or ask the user.

## Cost

Each run spends subscription usage. Start with one run per case. Repeat only a case whose result is unclear. Run a larger sweep only when the user asks.
