# Agent skills

My project name ships [agent skills](https://agentskills.io/) that help agents get better results with agentic coding. They are published with the documentation site so they can be discovered and reused with a wide range of tools.

## Editing the skills

Skills live under `src/my_project_name/.agents/skills/`. The template ships one placeholder skill you can replace or extend. Edit the `SKILL.md` files there; the post-build hook in `docs/hooks.py` publishes them automatically.

## Direct link to the skill

The published skill is served from the documentation site at `.well-known/agent-skills/my-project-name/SKILL.md`. Open the URL to read the skill, point an agent at it, or download it and place it in `.agents/skills/my-project-name/SKILL.md` in your project so tooling that reads local skills picks it up.

## Well Known Discovery

Machine-readable index of all skills: `/.well-known/agent-skills/index.json`. This is per the [Well Known Discovery RFC](https://github.com/cloudflare/agent-skills-discovery-rfc). Agents that support the format can fetch it to discover the skills.

## AI catalog

Machine-readable index that also covers options other than skills: `/.well-known/ai-catalog.json`. This is per the [AI Catalog](https://ai-catalog.io/) specification.

## How it works

During the documentation build, `mkdocs-simple-hooks` runs `docs/hooks.py:on_post_build`, which copies each skill and generates both discovery catalogs. Set `include-hidden-files: true` on the Pages upload in `.github/workflows/test.yml` so the `.well-known/` directory is included in the deployed artifact.
