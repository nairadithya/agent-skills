---
name: automate-me
description: "Turn the user's recurring workflow preferences into a reusable Pi skill. Use when they ask to automate their habits or create a personal workflow skill."
disable-model-invocation: true
---

# Automate a workflow

Create a reusable Pi skill from the user's demonstrated working habits. A Pi skill supplies instructions. It does not add tools or remain active unless invoked or selected as relevant.

## Gather evidence

1. Read the active transcript at `PI_SESSION_FILE`. Search prior Pi sessions only within the active project and only when the user asked to use history.
2. Identify recurring decisions, preferred checks, formatting, and tool use. Separate repeated behavior from one-off requests.
3. When the user asked to mine several transcripts and delegation is authorized, split the exact in-scope session files across read-only reviewers. Otherwise inspect the records in the parent session.
4. Ask the user in chat about preferences that the conversation does not reveal. Offer concrete choices rather than inventing answers.

## Draft the skill

Create the skill under `.agents/skills/<name>/SKILL.md` for a project workflow, or `~/.pi/agent/skills/<name>/SKILL.md` for a personal workflow. Use the Agent Skills frontmatter format. Give it a lowercase hyphenated name, a specific description that says when to use it, and instructions that change decisions.

Read Pi's `docs/skills.md` before relying on skill discovery, frontmatter, or invocation behavior. Link supporting files relative to the skill directory. Prefer the smallest instruction set that preserves the observed habits. Do not claim the skill persists in every turn like a mode; the user can invoke it with `/skill:<name>`.

## Review and report

Show the proposed skill and ask for approval before writing it unless the user already requested the skill itself. Validate its frontmatter, referenced files, and local links. Report the path and how to invoke it.
