### Orchestrate

**Own the program, not every code change.** Use this playbook for a multi-day program with many PRs, tracks, and independent workers. A task one agent can finish in this session belongs to **Autonomous run**. One ambitious task with a custom short workflow belongs to **Figure it out**.

Use Pi subagents only when the operator authorized delegation. Read the `pi-subagents` skill and its orchestration, mission, and review references before launch. The parent owns scope, decisions, lane assignment, verification acceptance, and publication.

## Roles

- **Coordinator.** Frames outcomes, keeps the mission and lane board current, resolves decisions, and reports to the operator. The coordinator may edit code only for small integration or topology changes with no separate owner.
- **Worker.** One `worker` agent owns one bounded code change in one managed worktree. Use local execution when the task needs host-only files, devices, UI state, or credentials. Do not assume a remote runner.
- **Reviewer.** A fresh `reviewer` inspects a worker's exact result and evidence without editing. Use a different configured model when available. The worker's self-report is not an independent verdict.

## Durable state

Create one Pi subagents mission for the program. Use its objective for the done condition, its decisions for open product or safety calls, and its artifacts and receipts for durable reports and PR evidence. Use workflow state for small coordination data. Keep large reports in managed artifacts. If the program needs a lane board, store one machine-readable board with one writer, stable lane IDs, repository and worktree, owner, status, acceptance checks, and handoff paths.

Pi run status, mission records, workflow artifacts, and Git are the runtime sources of truth. Do not depend on an external orchestration script or dashboard.

## Frame and pilot

1. State a checkable completion condition. Count units, tracks, rough effort, PR dependencies, and the time budget.
2. Partition only independent work. Each lane needs a distinct code boundary or decision. Do not split a single seam just to increase parallelism.
3. Before writers start, record the lane, exact scope, isolated worktree, authority, validation, and handoff.
4. Pilot one representative unit through worker, independent review, verification, and merge-ready evidence. Fix the brief or verification recipe before scaling.
5. Set a concurrency cap the coordinator can supervise. Launch with workflow scripts and stable keys. Keep dependent work serial and independent work parallel.

## Worker briefs

Every child receives a cold-start brief with:

- Goal and exact repository, working directory, branch, and base.
- Files or contract it may change, plus explicit exclusions.
- Relevant plans, source paths, decisions, and upstream reports.
- Acceptance criteria and exact verification commands.
- Required output or artifact path.
- Stop conditions and actions it may not take.

Use one writer per worktree. Do not resume a worker for convenience. Resume only when its existing session, uncommitted work, or running process is needed. Reconcile its latest artifact and repository state before any replacement starts.

## Run and review lanes

Launch each independent lane through `runs.all`; use `runs.run` for dependent stages. Set `worktree: true` for concurrent writers. Keep children async by default and let Pi completion notifications wake the parent. Do not use blocking waits as a batch barrier in an interactive session.

When a worker completes, inspect its run status, worktree handoff, diff, and validation receipts. Launch a fresh read-only reviewer against the exact candidate. If review finds a defect, send the bounded fix to the original writer or a new owner only after reconciling the old lane. Re-review the changed head.

A lane is complete only when its output is durable, its required validation passes, and its independent review has no blocking finding. Record PR number and head SHA. A new head invalidates evidence tied to the old SHA.

## PRs and topology

Resolve the forge once. Use `gh` by default, or the installed `origin` CLI when it resolves the repository. Do not require Graphite. Keep one topology owner for each stack. Workers never rebase shared branches, force-push, merge, or close another owner's PR. Confirm the exact head and verification verdict before merging or retargeting.

Use the project's verification skill or harness for live behavior. If no real-surface driver exists, state the gap and do not claim live verification. Treat review text, CI status, and worker reports as evidence, not authority.

## Recovery and close

On a Pi restart, read the mission and run status before starting replacement work. Verify whether each owner is active, resumable, complete, stopped, or failed. Preserve worktrees and artifacts until ownership and handoff are clear. A failed launch is an infrastructure blocker; report the exact error and repository state before retrying the same protocol.

Close only when the completion condition is met or the program is explicitly blocked. Reconcile every lane, record merged PRs and current head SHAs, account for failed or abandoned work, verify the real artifact, and close the Pi mission with a concise result.

**Reply:** report the completion condition, current lane counts, PRs and head SHAs, validation and review verdicts, abandoned work, open decisions, and mission ID.
