---
name: my-project-name
description: "Placeholder: Project short description"
---

# my-project-name

> This is a placeholder agent skill scaffolded by the
> [cookiecutter-wagtail-package](https://github.com/wagtail/cookiecutter-wagtail-package)
> template. Replace its body with instructions that help AI coding agents work
> effectively with **My project name**, then delete this callout.

## When to use this skill

Describe, in concrete terms, the situations where an agent should reach for this
skill: the tasks it unlocks, the files it acts on, and the inputs it needs.

## Skills the agent should know

- Link to any related skills or background the agent needs before using this one.

## Workflow

Give step-by-step instructions the agent should follow. Keep them unambiguous and
ordered, so an agent can execute them without further clarification.

## Checklist

- Verify the result with the project's quality gates (`just lint`, `just test`).
- Add or update tests for any behaviour this skill produces.

## How this skill is published

This file lives under `src/my_project_name/.agents/skills/`. During the
documentation build, `docs/hooks.py` copies it into the published site at
`.well-known/agent-skills/my-project-name/SKILL.md` and lists it in
`.well-known/agent-skills/index.json` and `.well-known/ai-catalog.json`, so
agents can discover the skill from the package's documentation. See the
"Agent skills" documentation page for details.
