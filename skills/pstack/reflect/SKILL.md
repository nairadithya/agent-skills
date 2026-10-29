---
name: reflect
description: Review the current Pi session for durable workflow lessons and propose targeted skill edits. Use when the user says /skill:reflect or asks to reflect.
disable-model-invocation: true
---

# Reflect

Find durable lessons in the current session and route them to skills or tooling.

## When to run

Run this when the user asks to reflect. Skip trivial or off-topic sessions, and do not turn one-off events into general rules.

## Read the transcript

Use the exact current session path in `PI_SESSION_FILE`. Do not search other sessions. For child work, use the exact run artifacts or child session paths reported by `pi-subagents`. If the current session file is unavailable, write a concise digest from the visible conversation and review that instead.

## Review the session

When delegation is authorized, launch three fresh `reviewer` subagents in one Pi workflow. Give them the transcript or digest and distinct lenses:

- **Judgment.** Find decisions, user corrections, or recurring misalignment that merit changes.
- **Tooling.** Find work the agent could have done with available Pi tools, skills, or MCP servers.
- **Divergent.** Find lessons the other reviewers may miss and challenge premature generalization.

Use the configured `openai/gpt-6.1-sol` reviewer at high thinking for judgment. Use `opencode-go/deepseek-v4.1-flash:medium` as the frequent second-family tooling or divergent reviewer via a per-run model override. For high-stakes reflection, use `opencode-go/minimax-m3:medium` or occasionally `opencode-go/kimi-k2.7-code:medium` for an additional independent family. Pass `context: "fresh"`, include the relevant reference prompt under `references/`, and grant only the tools the review requires. The explicit `:medium` suffix overrides the role's inherited thinking setting. If a model or tool is unavailable, report the gap rather than silently substituting.

Synthesize the findings in the parent session. Verify evidence and citations against the transcript and current skill files. Separate Accepted, Rejected, and Backlog items.

## Approve and apply

Show the full Accepted, Rejected, and Backlog lists to the user before applying any skill edit. Wait for approval and apply only the subset the user approves.

For each approved edit:

- Make a small correction to an existing skill directly.
- For a substantial change or a new skill, follow Pi's Agent Skills format in the Pi skills documentation. Validate frontmatter, linked paths, and skill names.
- If a lint rule, script, or runtime check can enforce the lesson, route it there instead of adding prose.

If no skill validator is available, check every changed skill's frontmatter and resolve its local links manually.

## Report

List the edits applied, new skills created, backlog items, and rejected findings with reasons. Do not file issues automatically unless the user asked.
