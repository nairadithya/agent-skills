# Agent Skills

A collection of reusable skills in the [Agent Skills format](https://agentskills.io/specification).

## Structure

Add each skill under `skills/<skill-name>/` with a `SKILL.md` file. Put any supporting scripts, references, or assets alongside it.

## Included skills

The `skills/` directory contains the personal `lean-mode` and `scientific-figure-making` skills and the `pstack` collection copied from the original Pi configuration. Some pstack workflows depend on other Pi configuration, tools, or locally installed packages; consult the individual skill instructions before use.

## Use with Pi

Install this repository locally:

```bash
pi install /absolute/path/to/agent-skills
```

After adding or editing skills, use `/reload` in Pi. Invoke a skill explicitly with `/skill:<skill-name>`. If the same skills also exist in a default Pi skills directory, Pi will warn about duplicate names and keep the first discovered copy.
