# Agent Skills

A collection of reusable skills in the [Agent Skills format](https://agentskills.io/specification).

## Structure

Add each skill under `skills/<skill-name>/` with a `SKILL.md` file. Put any supporting scripts, references, or assets alongside it.

## Use with Pi

Install this repository locally:

```bash
pi install /home/adithya/projects/agent-skills
```

After adding or editing skills, use `/reload` in Pi. Invoke a skill explicitly with `/skill:<skill-name>`.
