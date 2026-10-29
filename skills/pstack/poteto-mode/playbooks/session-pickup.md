### Session pickup

**You own the resume point. Read the prior trail, don't redo it.**

1. Locate the prior trail from the user's session ID, Pi resume history, `PI_SESSION_FILE`, a `pi-subagents` run or mission ID, or a pushed branch. Read the session metadata and last messages first, then scan the decision points. Do not search unrelated projects' session files. For a long transcript, delegate a bounded summary only when authorized.
2. Reconstruct operational state. The branch and worktree, what already landed (`git log`, `git diff` against the base), the open todos, the decisions made. The prior trail is authoritative input. Resist the bias to re-derive it.
3. Diff done vs pending. Compare what shipped against what was planned, name the resume point, do not re-run the prior repro or redo completed work. A "let me verify from scratch" pass means you're treating the trail as untrustworthy when it's authoritative.
4. Route remaining work to the matching playbook and decide whether to continue, deliver a finished recommendation, ratify or override a conclusion, or postmortem a failed run. The pickup playbook ends here. The routed playbook owns the rest.
5. Verify the inherited claims against the original goal on the real artifact (the **principle-prove-it-works** skill). A passing prior self-report is not the proof.

**Reply:** where the prior agent stopped, what you inherited vs redid (ideally nothing redone), the resume point, and the outcome.
