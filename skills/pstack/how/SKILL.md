---
name: how
description: "Use for \"how does X work\", code walkthroughs before changing something, and placement / ownership / layering questions (\"where should this live\", \"which package owns this\", \"is this the right layer\"). Explains subsystem architecture, runtime flow, onboarding mental models. Use why for motivation."
disable-model-invocation: true
---

# How

Explore the codebase to answer "how does X work?" questions. Produce architectural explanations at the level of a senior engineer onboarding onto a subsystem, enough to build a working mental model, not so much that it reads like annotated source code.

Use Pi subagents only when the current request or applicable project instructions authorize delegation. Use the configured `scout` and `reviewer` roles from `~/.pi/agent/settings.json`. The `pi-subagents` extension resolves model and thinking settings for each role. Read its role guidance before launching; do not fall back to an unconfigured model after an error.

## Step 1. Assess Complexity

If the scope is ambiguous, state your interpretation and explore. The user can redirect.

- **Simple** (a single module, a small utility, a narrow question such as "how does function X work"): no explorers. One explainer explores and explains in a single pass. Go to Step 2b.
- **Complex** (a subsystem spanning multiple files or services, a cross-cutting feature, a full architectural overview): when delegation is authorized and will improve evidence, use a workflow script to launch distinct read-only scouts, then hand off their findings to the explainer. Go to Step 2a.

When in doubt, take the simple path.

## Step 2a. Explore (complex questions only)

Decompose the question into 2 to 4 exploration angles, each a distinct slice of the subsystem. Use `runs.all` in a Pi workflow script with `agent: "scout"`, `context: "fresh"`, and distinct exploration angles. Configure the scout's read-only tool allowlist in Pi agent settings. Each scout gets the prompt in `references/explorer-prompt.md` with its angle filled in. Then go to Step 3.

## Step 2b. Direct Explain (simple questions)

When delegation is authorized and useful, launch one Pi `scout` with `context: "fresh"` and a read-only tool allowlist. Build its prompt from `references/explainer-prompt.md` without the explorer-findings section. Go to Step 4. Otherwise inspect the code in the parent session.

## Step 3. Synthesize (complex questions only)

Once all scouts have returned, synthesize their findings in the parent session. If an independent synthesis materially improves the answer and delegation is authorized, launch a fresh `scout` with the explainer prompt and the complete findings.

## Step 4. Present

Present the explanation to the user. Check every cited path and claim yourself. Light edits for clarity or context are fine.

## Output Format

The explanation uses the sections defined in `references/explainer-prompt.md`, dropping any that do not apply: Overview, Key Concepts, How It Works, Where Things Live, Gotchas.
