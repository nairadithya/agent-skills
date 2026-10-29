---
name: swarm
description: "Run bounded Pi subagent workflows for parallel coverage, independent review, or comparisons, then synthesize one report. Use for `/skill:swarm`, 'swarm this', parallel coverage, races, or exploration."
disable-model-invocation: true
---

# Swarm

Use Pi subagents only when the current request or applicable project instructions authorize delegation. The parent frames the work, owns the final decisions, and returns one report.

## Frame

1. State the done condition and the artifact or report the workflow must return.
2. Choose distinct slices, a model race, or a combination. For a race, state whether selection means first pass, rank all, or best of.
3. Set the worker count from the coverage needed. The extension enforces its own concurrency limits.
4. Match the role to its capability: `worker` for implementation, `scout` for reconnaissance, `verifier` for executable checks, and read-only `reviewer` for diff inspection. Check `/subagents-models` when routing matters. Give each writer its own worktree. Reviewers receive the exact diff and evidence; verifiers receive the harness and tools their task requires.
5. Give each worker a unique output path. Verification tasks must name exact commit SHAs. Measurement tasks must name the method and sample count.

## Launch

Use one workflow script with `runs.all` for independent runs. Each prompt must stand alone and state the goal, scope, exact slice or race arm, validation, and report format. Ask for `PASS`, `ISSUES`, or `BLOCKED` with evidence. Verifiers report execution only; reviewers inspect evidence and code but do not run commands or publish results.

Pi async subagents run locally by default. Use managed worktrees to isolate concurrent writers. If a worker fails, report the failure rather than silently switching execution modes or model.

## Aggregate

Read the terminal results and inspect artifacts. Reject a result that lacks the evidence required by its brief, and retry only when the same protocol supports a clear retry. After a second miss, record a gap. Every required slice needs a result. For a race, apply the selection rule declared before launch.

Return a compact result table, evidenced issue summaries, gaps, and dropouts. Do not paste raw worker dumps.
