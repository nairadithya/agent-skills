---
name: why
description: "Investigate why code has its current design, trace regressions, explain decisions, and verify the source of thresholds. Use for 'why does this work this way', design rationale, postmortems, or data-backed numbers. Use how for runtime behavior."
disable-model-invocation: true
---

# Why

Investigate the motivation and intent behind code. `how` explains what code does. `why` traces the forces that shaped it.

Use Pi subagents only when the current request or applicable project instructions authorize delegation. Follow the `pi-subagents` skill and configured `researcher` and `oracle` roles. Do not assume a separate model or read-only mode without checking agent settings and tool access.

## Establish the code anchor

Before searching for rationale, identify the target files, line ranges, symbols, relevant commits, merged PR numbers, and linked issues. Use `git blame`, `git log --follow -p`, and `git log --oneline` to trace changes. Use `gh pr view` for relevant PR descriptions and discussion when GitHub is the project's forge.

Record this anchor before asking researchers to look elsewhere. Pass exact paths and the user's question in each delegated brief.

## Discover available evidence sources

Inspect the tools available in this Pi session, including configured MCP tools. Do not assume tools or MCP servers are available unless they appear in this Pi session. Map available sources to these categories:

1. Source control history.
2. Issue and ticket tracker.
3. Long-form design documents.
4. Real-time team chat.
5. Infrastructure observability.
6. Error tracking.
7. Product analytics.

Git and source control are always the starting point. For each other category, use it only when an available Pi tool or local source can query it. In the final report, name categories that were unavailable or irrelevant instead of implying you searched them.

## Investigate

For a narrow question answered by one or two commits, inspect the source, tests, and PR record directly. Do not delegate for ceremony.

For a broad history question, use one bounded `researcher` per relevant evidence category in a Pi workflow script. Give each researcher only the tools it needs. Use `context: "fresh"`; include the code anchor, original question, matching source playbook under `references/sources/`, and a concise expected report. Researchers inspect evidence but do not edit files.

Skip categories with a written reason. A missing source is a gap, not evidence that no rationale exists. If the target is defensive code, consult `references/sources/incident-postmortem.md` where applicable.

Synthesize the reports in the parent session. Verify important citations against the source. Do not rely on a synthesizer's unsupported claim or invent a rationale from current behavior alone.

## Report

Keep these distinctions clear:

- **Found.** Direct evidence from source, history, tests, or external records.
- **Inferred.** A conclusion supported by evidence, labeled as an inference.
- **Unknown.** A source that was unavailable or did not answer the question.

Report the question, code anchor, evidence found, reasonable inferences, competing explanations, gaps, sources consulted, and confidence. If the answer informs a code change, end with Preserve, Change, Avoid, and Risk constraints for planning.
