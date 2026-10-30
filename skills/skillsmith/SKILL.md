---
name: skillsmith
description: Designs, writes, tests and maintains the user's agent skills with their house practice. Checks first that a skill is the right container, writes evals from baseline failures before the draft, then keeps the skill small. Explicit invocation only, for example /skillsmith; not for ordinary coding or for editing CLAUDE.md or AGENTS.md.
disable-model-invocation: true
---

# Skillsmith

A skill is worth its context only when it changes what the agent does. The
model already knows the skill format; this skill holds the practice: evals
first, the smallest text that fixes a real failure, and reach across the
user's harnesses. Prefer the plain path. Do not design for an edge case that
no eval or real failure has shown.

Pick the mode from the request:

- **New**: a new skill, from a session, a spec or a repeated task.
- **Improve**: change an existing skill, usually after a failure or a correction.
- **Audit**: review a skill (often third party) without changing it.

Copy this checklist and keep it current. Each step ends on its done-when line.

```
Skillsmith (<mode>):
- [ ] 1 Triage
- [ ] 2 Blind-spot pass
- [ ] 3 Baseline
- [ ] 4 Evals
- [ ] 5 Draft
- [ ] 6 Check
- [ ] 7 Compare
- [ ] 8 Release
```

Audit runs steps 6 and 7 only, read-only, and adds a script review (step 7).

## 1. Triage

Ask: is a skill the right container? Take the first row that fits.

| The need is… | It goes to… |
|---|---|
| Must happen every time, with no exception | A hook |
| Needed in every session, whatever the task | One line in CLAUDE.md or AGENTS.md |
| Needed in one directory, or for one file pattern | A nested CLAUDE.md, or a scoped rule |
| A deterministic check or transform | A script, maybe called by an existing skill |
| A procedure the agent runs on demand, that works after a plain `skills add` | A skill in the skills repo |
| A procedure that needs machine setup | Its own repo (as delegate did) |

Then pick the invocation. Default to user-invoked
(`disable-model-invocation: true`) when the user starts it by name. Use
model-invoked only when the agent must start it on its own, and then write a
trigger check in step 4.

Done when the user agrees that a skill is the right unit, and its mode,
invocation and branches are named.

## 2. Blind-spot pass

Start from real material: a transcript, the user's corrections, a spec, or
the files the task touches. Never draft from general knowledge alone; that
gives vague text such as "handle errors appropriately".

List, in a few lines each:

- What the user knows but would never write down (their taste, what "good
  enough" means here). Ask for one example of a good result if none exists.
- Domain hazards: legal, financial or personal data, current facts that change.
- External actions (posting, sending, paying, deleting) that need a human gate.
- What the skill must not do.

Ask one fork question per message, with a recommended answer. Decide
conventional defaults yourself and say so.

Done when the scope, the success criteria and the open forks are written in
the effort's `.scratch/<effort>/spec.md` (or in the conversation, for a small
change).

## 3. Baseline

Run 2 or 3 realistic prompts without the skill, in a clean context: a
subagent, a fresh session, or a `delegate` lane when the user asks for one.
For Improve, the baseline is the current version: copy it to a scratch folder
first.

Done when each failure (or each thing the baseline already does well) is
written down.

## 4. Evals

Write the failures from step 3 into `evals/evals.json` before you write the
SKILL.md body. Read [references/evals.md](references/evals.md) for the schema,
the executor contract and fixtures. Never convert or rewrite an existing
eval file; add cases to it.

Done when each recorded failure has a case with checkable assertions.

## 5. Draft

Write the smallest SKILL.md that fixes the recorded failures. Read
[references/authoring.md](references/authoring.md) before the first draft and
whenever the description, a script or another harness is in question.

Done when every line answers a recorded failure or a step the agent would get
wrong without it.

## 6. Check

Run `python3 scripts/check-skill.py <skill-dir>` from this skill's folder.
Fix each ERROR. Read each WARN and fix it, or say why it stays.

Done when the checker exits 0.

## 7. Compare

Run each case with the skill and with the baseline from step 3, each in a
clean context, one run per case. Grade each assertion PASS or FAIL with quoted
evidence from the outputs or the transcript; no evidence means FAIL. Show the
user a short table (case, baseline, with skill) and the outputs that matter.
Repeat a case only when its result is unclear.

The session that wrote the skill knows what it meant, so its own run proves
little. Grade in a fresh context when the result matters.

For Audit, also read each script and flag network calls, writes outside the
project, credential reads and anything the SKILL.md does not mention.

Then improve: generalize from the failure, do not patch the one prompt; delete
any instruction whose removal changes no result. Repeat steps 5 to 7 until
the user is satisfied.

Done when every case passes, or the user accepts the named failures.

## 8. Release

- Claude Code and Codex must pass the evals. Other harnesses need a clean
  check only; say they are untested.
- Add or update the skill's row in the repo README. A new plugin (not a new
  skill) needs both marketplace files; run `claude plugin validate .`.
- Add the skill to the dotfiles Makefile `PERSONAL_SKILLS` when it is new.
- Commit with no agent attribution: no `Co-Authored-By`, no session link.

**Maintain.** When the user corrects the skill in use, add the correction as a
gotcha in SKILL.md and a regression case in `evals.json`. After a model or
harness upgrade, rerun the evals and delete instructions that no longer
change a result.

## House rules

- The repo is public. No secrets, personal data, or names of the user or of
  any organization, site or machine. Fixtures use made-up data.
- A skill is self-contained: no Makefile step, no other repo, no dependency
  outside the Python 3 standard library and POSIX shell.
- A skill carries opinions and procedures, never machine state. State lives
  in the files that own it; the skill points to them.
- An installed skill is a copy. An edit reaches a machine only after a push
  and `npx skills update -g` there.
