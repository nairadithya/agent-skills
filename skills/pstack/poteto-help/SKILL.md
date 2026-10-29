---
name: poteto-help
description: Answer questions about pstack's workflows, skills, setup, and troubleshooting. Use when the user asks how to use pstack.
disable-model-invocation: true
---

# Pstack help

Answer the question, offer one prompt the user can send when useful, and link the local skill file that supports the answer. Do not start delegated work for a help question.

If the user asks for work, read [`poteto-mode`](../poteto-mode/SKILL.md) and do the task under its matching playbook. Pi loads skills when relevant or when invoked. It has no persistent skill mode. The user can invoke `/skill:poteto-mode` for each task.

## Route the question

- Setup or model routing: read [`setup-pstack`](../setup-pstack/SKILL.md). It configures Pi subagent roles in `~/.pi/agent/settings.json`.
- Start a task with the pstack workflow: read [`poteto-mode`](../poteto-mode/SKILL.md).
- Find the right skill: recommend `/skill:poteto-mode` by default, or name the specialist skill when the user wants a specific activity.
- Diagnose delegation: read the installed `pi-subagents` skill and its relevant reference. Check `/subagents-doctor` and `/subagents-models` when the user asks about their live setup.
- Prove an app change: recommend [`create-verification-skill`](../create-verification-skill/SKILL.md) when the project has no real-surface driver.

## Explain Pi behavior accurately

Pi loads a skill when it is relevant or explicitly invoked with `/skill:<name>`. A skill gives instructions; it does not itself add executable tools or switch models. Pi extensions provide tools, commands, schedules, and other runtime behavior. `pi-subagents` provides delegated agents and workflow scripts, but delegation still needs authorization from the current request or applicable project instructions.

Use `pi --list-models` to inspect installed model IDs. Use `/subagents-models` to inspect the effective child-agent mapping. Model selection belongs in Pi settings or a per-run override, not in a separate rules file.

Pi's built-in features differ by installed extension and configuration. Do not claim a command, provider, MCP server, verification driver, or remote runner exists until you can verify it in this environment.

## Reply

Lead with the answer. Include at most one example prompt, adapted to the user's task, then link the source skill by path. Keep the answer brief unless the user asks for the full map.
