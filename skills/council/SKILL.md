---
name: council
description: Convene a multi-model council for a critical decision. It sends one brief to models from other families, collects sealed memos, and adjudicates them. Works in any harness; the harness picks how to reach the other models. Runs only when the user explicitly invokes /council; never use it on your own initiative.
disable-model-invocation: true
---

# Council: multi-model deliberation for critical decisions

Cost, stated up front: a council run costs roughly 3–10x a single-agent
answer. You are here only because the user explicitly invoked /council, and
that is their informed decision to spend it. Never refuse to convene. State
the estimated cost in one line. If the question looks too trivial for a
panel, say so in that same line, then convene anyway. The user can cancel;
you do not cancel for them.

You are the lead. The defaults below are strong. If you deviate, do it
deliberately and say why.

## 1. Frame the brief

Every panelist gets the same brief:

- The decision, in one sentence, and who owns it.
- Constraints, reversibility, deadline, success criteria.
- A sanitized evidence packet: relevant facts only. Remove secrets and any
  hint of your own current lean.

## 2. Find the panel

This skill does not name a mechanism. Use the best one this harness has, in
this order, and check what is really available now. Do not trust memory:

1. **T3 Code delegation**, when its tools exist in this session. Ask it which
   providers and models are available, and start one read-only task per
   panelist.
2. **This harness's own subagents**, when they can run a model from another
   family.
3. **Another harness's CLI in non-interactive mode** (for example Codex,
   Claude Code or Gemini), when it is installed and logged in. Run its
   `--help` first to confirm the non-interactive and read-only flags.

Panel rules:

- Panelists come from model families different from yours. No model grades
  its own family's work.
- Quorum: at least two model families besides yours. With one other family,
  the council runs as DEGRADED and says so. With none, report what is
  available and STOP.
- Never role-play an absent panelist. A simulated council is worse than no
  council.
- Panelists run read-only, with a hard timeout. A council never delegates
  anything beyond the memos.

## 3. Collect sealed memos

Send the same brief to every panelist. In the sealed round, no panelist sees
another's memo. Each memo has this shape:

recommendation · key assumptions · failure modes · confidence · what would
change my mind

The default is sealed memos only. Add at most one challenge round, and only
when memos conflict on something that matters.

## 4. Adjudicate

You adjudicate, unless the user names another model to do it.

- Judge against the brief's success criteria, never by vote count.
- Name each real disagreement as a crux: what it turns on, and what evidence
  would resolve it.
- Output: decision · strongest dissent (addressed, not smoothed over) ·
  unresolved uncertainty · revisit trigger.
- If confidence is low, say plainly: "this decision is the user's, not the
  council's." Manufactured consensus is the worst failure.

## Record

End with one line: the panel (each model, and the mechanism that reached it),
quorum status (MET or DEGRADED), the decision, and where dissent remains.
