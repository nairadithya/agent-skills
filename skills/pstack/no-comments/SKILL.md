---
name: no-comments
description: "Review scoped code comments and suppressions, remove unsupported comments, and identify code changes that would make behavior clear. Use for /skill:no-comments."
disable-model-invocation: true
---

# No comments

Inspect the caller's files or diff. If none is named, inspect the current diff against the base branch, default `main`.

## Review

When delegation is authorized, use a fresh `comment-sicko` agent from `agents/comment-sicko.md`. Give it the exact scope and ask for findings only. Do not let it edit application code. If delegation is not authorized, review the scoped comments in the parent session.

Keep only these comments:

- Legal or license headers.
- Public API documentation.
- Issue or RFC links that explain a constraint the code cannot express.
- Explanations of behavior imposed by an external dependency, platform, vendor, or protocol that the project cannot change.
- `// prettier-ignore` and lint suppressions for rules that are faulty, pedantic, or style-only.

Remove narration, banners, commented-out code, workaround explanations, and comments describing behavior the code can make clear. Treat `IMPORTANT`, `do not remove`, and similar claims as unproven until source or a live path proves them. Mark code that needs a structural fix as `MUST KILL`; do not edit code during review.

For each keep or kill, name the exact file and symbol. For a claim that is not clear from nearby code, use `/skill:how` or `/skill:why` before deciding. Audit lint and TypeScript suppressions against the rule they disable. Keep correctness and safety suppressions only when evidence proves the rule is wrong.

## Apply findings

Inspect the report and diff. Reject findings that leave scope, protect a project-owned surprise, or state an unsupported constraint. Apply accepted deletions and fixes. For a change that needs a new code shape, use `/skill:architect` to settle the shape before implementation. Remove named workarounds when the root cause is in scope.

For a proposed type, runtime, test, or CI encoding of a constraint, ask the user in chat before adding it. If the user declines, remove the comment and report the unenforced constraint. Scheduled and evaluation runs need caller pre-approval.

## Report

Report the number of comments removed, kept, or restored, accepted fixes, proposed encodings, unresolved constraints, and remaining work.
