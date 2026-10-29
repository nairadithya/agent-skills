---
name: create-verification-skill
description: "Generate a project-local verification skill that drives the app through real user paths. Use for /skill:create-verification-skill or when a project has no scripted way to prove UI, CLI, or service behavior."
disable-model-invocation: true
---

# Create a verification skill

Generate a project-local Pi skill at `.agents/skills/verify-<app>/`. It should tell a fresh agent how to launch the app, exercise real user paths, and capture evidence.

## Interview the repository

Find these facts from the code and docs. Ask the user only about details you cannot observe.

- **Surface.** Identify the user-facing web UI, CLI, TUI, desktop app, API, mobile app, or library. Note the other surfaces if there are several.
- **Run.** Find the documented local launch command. Record ports, environment variables, seed data, and authentication.
- **Drive.** Find an existing harness first, such as Playwright, Cypress, PTY helpers, HTTP endpoints, or a debug port. Otherwise choose a suitable driver, such as CDP for web or Electron, PTY for CLI or TUI, or HTTP for a service.
- **Observe.** Name evidence the driver can capture, such as screenshots, terminal output, response bodies, logs, exit codes, or database state.
- **Isolate.** Check whether two instances can run side by side. If they cannot, state that the skill must not disrupt a shared user instance.

If the checkout cannot build or start, fix that first or report the failure. Do not write a skill that teaches a broken setup. If a missing asset irrelevant to the app blocks startup, the skill may create it as clearly marked verification scaffolding and remove it during cleanup.

## Write the skill

Create `.agents/skills/verify-<app>/SKILL.md` with Agent Skills frontmatter. Set `name: verify-<app>` and describe the app, surface, and when to use the skill. Include these sections, based on repository evidence:

- **Launch.** Give the exact command and readiness signal. Include teardown. For a short-lived CLI or TUI, build once and start each drive in an isolated PTY or tmux session.
- **Doctor.** Add a read-only check for process state, app version, port ownership, and authentication. Run it first when the target looks wrong.
- **Drive.** Show real selectors or commands from the repository. Prefer stable handles over screen coordinates or tab order.
- **Evidence.** Capture the user action and resulting state, not only the final screen. Verify side effects as well as visible state. Use mocks only at production boundaries. For dry-run paths, inspect actual file, network, or Git effects.
- **Cleanup.** Stop only processes the run started. Remove scratch state but preserve evidence at the documented path.
- **Helpers.** Give each helper script a working invocation. Do not leave scripts that readers must reverse-engineer.

## Map user-facing features

Create `.agents/skills/verify-<app>/features/README.md` and one file for each key user-facing feature, starting with three to five features found in routes, commands, menus, or docs. Follow [`references/feature-map-example/`](references/feature-map-example/). Each feature file must explain what it does, how to reach it, how to drive it, and what observable result proves it works. Use the headings `Sub-features`, `How to get to it (user POV)`, `Driving it with <harness>`, and `Gotchas`.

## Prove the skill

Run its instructions end to end for one mapped feature. Launch the app, run the doctor check, drive the feature, capture evidence, and clean up. Confirm the evidence still exists after cleanup. Clean up after failed attempts too. A skill that has not been exercised is a draft.

Point the user to `/skill:maintain-verification-skill` to keep the feature map current.
