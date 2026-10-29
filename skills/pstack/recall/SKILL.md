---
name: recall
description: "Reconstruct recent work from Pi session history, live Git state, and shared project records. Use for 'recall my work on X', 'catch me up', 'where did I leave off', or before resuming work."
disable-model-invocation: true
---

# Recall

Build a concise, evidence-based summary of recent work and the next useful action. Read only in-scope sessions and project records.

The current session file is available as `PI_SESSION_FILE`. For prior Pi sessions, use `pi --resume` or inspect session files under `~/.pi/agent/sessions/`, restricted to the active project. Do not search other projects without permission. For delegated work, use exact run IDs and artifact paths from `pi-subagents`, not guessed transcript globs.

## Rebuild context

1. If the user named one specific prior run or branch to continue, use the session-pickup playbook. If the user gave a complete state capsule, use it and skip transcript mining.
2. State the project, topic, and time window before searching. Default to the active project and the last seven days. Never expand "all" into a smaller sample without saying so.
3. Search the current session and relevant recent Pi session records. Delegate transcript slices only when the user or applicable instructions authorize it and the corpus is large enough to benefit. Give each reader a distinct slice and ask for goals, decisions, open threads, corrections, and artifacts with source references.
4. When the topic names a feature or bug, check the shared records that are available through local source control, configured MCPs, issues, or docs. State which sources were not available.
5. Verify surfaced PRs, branches, and tickets against current Git and forge state. Read the full transcript when a claim depends on which tools ran or files an agent opened.
6. Write a brief grouped by thread. Sanitize private context before any public output.

## Output

Lead with the capsule, then thread status, recurring problems, and the next action.

- **Capsule.** At most five bullets describing the work and current state.
- **Threads.** One line each with a status such as `[merged #N]`, `[open PR #N]`, `[in flight <branch>]`, `[verified, uncommitted]`, `[reverted #N]`, or `[planned, not started]`.
- **Problems.** At most five recurring issues. Include fixes that shipped and were reverted.
- **Next move.** One concrete action.

Keep unrelated features out unless they block the named topic. Cite session IDs and shared-record sources. Use `/skill:unslop` for the final brief.
