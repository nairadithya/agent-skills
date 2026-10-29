# Prompts worth copying

Replace paths, skills, and done checks with the real ones. Invoke Pi skills with `/skill:<name>`.

## Understand

- `/skill:poteto-mode read <thread>. Restate the underlying issue in plain English.`
- `/skill:poteto-mode investigate why <symptom>. Give me the evidence and your best hypotheses. Do not change code yet.`
- `/skill:how understand <subsystem>. Then use /skill:why to trace why it broke.`
- `/skill:recall my work on <topic> from last week, then read <issue>.`
- `/skill:teach explain why you implemented it this way and what you traded off.`
- `/skill:poteto-mode take over this branch. Read the decision log, find what is done, and continue without repeating finished work.`

## Build

- Bug: `/skill:poteto-mode <symptom>. Reproduce it, fix it, and verify the result.`
- App bug: `/skill:poteto-mode reproduce this with /skill:verify-<app>. If it reproduces on main, fix it and capture proof.`
- Cheap test: `/skill:poteto-mode reproduce <bug>. If a cheap test path exists, use /skill:tdd, then fix and rerun.`
- Feature: `/skill:poteto-mode add <behavior>. Keep <current output> byte-identical and verify both.`
- Refactor: `/skill:poteto-mode move <code> into one module with no behavior change. Record the current output and prove it is unchanged.`
- Perf: `/skill:poteto-mode <operation> takes <time> on <fixture>. Trace the cause, fix it, and show before and after.`

## Design and plan

- `/skill:poteto-mode prototype options for <feature>. Capture screenshots or video for comparison.`
- `/skill:poteto-mode we need <feature>. Settle the design first. Show open questions and wait for my review before implementation.`
- `/skill:poteto-mode write a tutorial for <new package>, then explain its tradeoffs.`
- `/skill:arena compare approaches for <task>.`
- `/skill:poteto-mode turn this design into a plan with small, verifiable PRs.`
- `/skill:poteto-mode plan the migration of <library> to <target>. Preserve existing behavior, including bugs.`

## Review and ship

- `/skill:interrogate review the whole branch. Do not change anything. Report only real bugs and regressions.`
- `/skill:swarm check every package under <dir> against its check script. One worker per package. Return one report.`
- `/skill:poteto-mode open a PR with small ordered commits and evidence in the description.`
- `/skill:poteto-mode babysit this PR and get it green.` For one status pass, ask `/skill:poteto-mode check PR <number> and report outstanding items.`
- `/skill:poteto-mode land the stack.`

## Away and back

- `/skill:poteto-mode drive <goal> until <checkable condition>. Keep a decision log. Do not ask before reversible changes. Stop and report if blocked.`
- `/skill:show-me-your-work catch me up on what you did last night.`
- `/skill:poteto-mode run full autopilot on this independent queue.`
- `/skill:poteto-mode build these changes as a stack, but do not ship. I will land it.`
- `/skill:reflect capture lessons that should change future decisions.`
- `/skill:bro restate your last reply in plain words.`
