---
name: arena
description: "Run independent attempts at the same task, select the strongest base, combine useful ideas, and verify the result. Use for `/skill:arena`, 'arena this', or when one attempt risks locking in the wrong design."
disable-model-invocation: true
---

# Arena

Use Pi subagents only when the current request or applicable project instructions authorize delegation. Run N independent candidates, choose a base, incorporate useful ideas from the others, and verify the final result.

## Frame the run

1. State the artifact each candidate will produce.
2. Define three to six criteria that make success observable.
3. Select candidate models from the active `pi-subagents` settings and use per-run `model` overrides for each candidate. Use distinct model families for judgment-sensitive tasks. Keep the usual generator on `openai/gpt-6-luna`; use `opencode-go/minimax-m3:medium` for an alternative design candidate and `opencode-go/deepseek-v4.1-flash:medium` for frequent exploration. Use `opencode-go/kimi-k2.7-code:medium` only when a third-family candidate adds value. The explicit suffix prevents role-level thinking from leaking into alternate runs. Read `/skill:setup-pstack` for defaults and estimated request allowances.
4. Give every candidate its own output path and managed worktree when it edits the repository.

## Run candidates

Use one Pi workflow script with `runs.all`. Give each child the same complete brief, its own stable key and output path, and the model selected for its run. Each brief must state the task, constraints, acceptance criteria, validation, and required report. Candidates return an artifact and a short rationale naming alternatives they rejected.

If a candidate fails, continue with the results that arrived and report the dropout. Do not silently replace its model after a launch failure.

## Choose a base

Read every candidate artifact. Score each one against the criteria. Use an independent `reviewer` to compare candidates when that adds useful evidence and delegation is authorized. The reviewer must inspect the rubric and candidate artifacts, not rely on candidate summaries alone.

Choose the base a maintainer can extend with the least risk. Record the choice and reason beside the final artifact.

## Combine and verify

Review each losing candidate for one or two useful ideas. Add only ideas that fit the chosen design. Record accepted and rejected ideas with their sources.

Verify the combined result against the same criteria. If verification reveals a gap, correct the rubric or the result and rerun the relevant check. Report the final artifact, chosen base, useful additions, dropouts, and verification evidence.
