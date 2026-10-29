# Pstack navigation

Use this page to resolve skill, playbook, and reference names to their files. Paths below are relative to this directory, `/home/adithya/.pi/agent/skills/pstack/`.

## Find a skill

A skill named `NAME` lives at `NAME/SKILL.md`. For example:

- `figure-it-out` is [`figure-it-out/SKILL.md`](figure-it-out/SKILL.md).
- `architect` is [`architect/SKILL.md`](architect/SKILL.md).
- `principle-model-the-domain` is [`principle-model-the-domain/SKILL.md`](principle-model-the-domain/SKILL.md).

Principle skill names keep the `principle-` prefix in both the name and directory. Do not remove the prefix or look under a `principles/` directory.

## Find a poteto-mode playbook

A playbook named `NAME` lives at `poteto-mode/playbooks/NAME.md`. For example, the investigation playbook is [`poteto-mode/playbooks/investigation.md`](poteto-mode/playbooks/investigation.md), and the opening-a-PR playbook is [`poteto-mode/playbooks/opening-a-pr.md`](poteto-mode/playbooks/opening-a-pr.md).

`figure-it-out` is a skill, not a poteto-mode playbook. A throughput checkpoint is a line of text in the relevant playbook, not a separate file.

## Find a supporting reference

References live under the skill or playbook that uses them. Follow that file's relative Markdown link instead of guessing a path. For example, the architect skill links to [`architect/references/design-red-flags.md`](architect/references/design-red-flags.md).

## Find the Pi subagents skill

The `pi-subagents` skill is not part of this directory. In this installation, it lives at `~/.pi/agent/npm/node_modules/pi-subagents/skills/pi-subagents/SKILL.md`.
