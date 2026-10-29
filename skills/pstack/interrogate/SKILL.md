---
name: interrogate
description: "Run independent Pi subagent reviews against a code change, then synthesize evidence-backed findings. Use for `/skill:interrogate`, 'adversarial review', 'multi-model review', 'challenge this', or 'find blind spots'."
disable-model-invocation: true
---

# Interrogate

Use Pi subagents only when the current request or applicable project instructions authorize delegation. Reviewers independently inspect the same change. The parent decides what to do and never auto-applies findings.

## Set the scope and intent

1. Identify the target from the user's request, current diff, or relevant files.
2. State the intended behavior in one paragraph. If intent is unclear, ask the user before reviewing.
3. Give each reviewer the same diff, surrounding contracts, rubric, and review prompt. Require concrete findings with file and line references.

## Launch reviewers

Use `runs.all` in one Pi workflow script. The primary `reviewer` uses `openai/gpt-6.1-sol` at high thinking. For a second family, set that run's `model` override to `opencode-go/deepseek-v4.1-flash:medium` (frequent second review); use `opencode-go/minimax-m3:medium` for an alternative design/review candidate, and add `opencode-go/kimi-k2.7-code:medium` as an occasional third-family judge. Keep each task identical apart from its model and role-specific lens. Check IDs with `pi --list-models`; use `/subagents-models` for persistent role mappings. The explicit `:medium` suffix replaces the selected agent role's thinking level for each alternate run.

Set `context: "fresh"` and give reviewers read-only tool access. Use the `pi-subagents` workflow schema. Do not assume a multi-model panel exists. Each task must say not to edit project files.

Read `references/reviewer-prompt.md`, `references/rubric.md`, `references/code-quality-review.md`, and `references/lead-judgment.md` when applicable. Pass the same completed review brief to every reviewer.

## Synthesize findings

1. Merge reports that describe the same issue.
2. Note which findings multiple reviewers independently raised.
3. Check every finding against the current code and stated intent.
4. Classify each finding as **Act on**, **Consider**, **Noted**, or **Dismissed**, with one line explaining the decision.
5. Do not apply fixes. Report the review verdict and evidence to the user.

## Output

Include the intent, reviewer models and finding counts, categorized findings, and an agreement map. Link each actionable finding to its source location.
