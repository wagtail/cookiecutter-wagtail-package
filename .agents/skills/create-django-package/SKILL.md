---
name: create-django-package
description: Creates a new Wagtail/Django package from the cookiecutter-wagtail-package template
license: MIT
---

## Overview

Guided creation of a new Wagtail or Django package using the [cookiecutter-wagtail-package](https://github.com/wagtail/cookiecutter-wagtail-package) template. Covers goal-setting, template rendering, customization for the user's needs, initial QA, and a structured handoff report.

## Methodology

### Goals

- Understand what the user wants to build and how the package fits into their project.
- Create a new package from the template with correct metadata and configuration.
- Customize the generated package where the template defaults don't match the user's goals.
- Verify the package installs, lints, and tests successfully. And the demo works.
- Produce a clear report so the user knows what was set up, what to review, and what to do next.

### Guardrails

- Prefer minimal changes to tooling unless explicitly asked by the user. Avoid diverging from the template without a clear reason.
- If the user is extracting code from an existing project, confirm with the user which aspects of the source project to adapt or leave exactly as-is.
- Do not invent package functionality unless asked. The skill and template sets up scaffolding; the user decides what the package should contain.
- When a decision is ambiguous (like support targets), present options with trade-offs rather than assuming.

### Input

To detect from the context or request from the user if unclear:

- Package name and short description.
- Repository URL (GitHub org and repo name, or another forge).
- Target audience: Wagtail-specific package, or general Django package that also works with Wagtail. Default: infer based on name / description.
- Whether this is a new package from scratch, or an extraction from an existing project. Default: new package from scratch.
- (Other specific requirements, depending on the stated goals)

### Reference data sources

Always fetch latest information from authoritative sources when relevant to the package setup.

Template and ecosystem:

- [cookiecutter-wagtail-package README](https://github.com/wagtail/cookiecutter-wagtail-package/blob/main/README.md) and template files in the repository.
- [Wagtail package maintenance guidelines](https://wagtail.org/package-guidelines/)

Versions and compatibility:

- [Supported versions of Python](https://devguide.python.org/versions/)
- [Supported versions of Django](https://www.djangoproject.com/download/)
- [Supported versions of Wagtail](https://github.com/wagtail/wagtail/wiki/Release-schedule)
- [Wagtail compatible Django / Python versions](https://docs.wagtail.org/en/stable/releases/upgrading.html)

Packaging:

- [Python Packaging User Guide](https://packaging.python.org/en/latest/)
- [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)
- [PyPI classifiers](https://pypi.org/classifiers/)
- [PyPI Trusted Publishers](https://docs.pypi.org/trusted-publishers/)

### Reporting

Package creation involves many decisions. Report clearly at each stage so the user stays oriented.

- Use text formatting (tables, lists, Markdown links).
- Link to relevant documentation pages when mentioning tools or standards.
- Report on the methodology and the outcome at each step, not just the final result.
- When sharing docs references, link to the HTML pages rather than raw sources.

### Quality assurance

Options to verify the generated package is in good shape, to use as needed through the creation steps:

- Package installs without errors (`uv sync --dev`)
- Linting passes (`just lint` or equivalent)
- Test suite passes (`just test` or equivalent)
- Demo project runs (`just demo` or equivalent)

Look for any warnings from the package manager or from QA tools.

### Definition of done

- Package directory created with all template files rendered.
- Package metadata (`pyproject.toml`) reflects the user's choices.
- Dependencies install cleanly.
- Linting, tests, demo all pass / work.
- Any customizations beyond the template are documented in the report.
- Handoff report delivered to the user.

## Steps

### Understand the user's goals

- [ ] Ask the user about their package if not already clear from context:
  - What does the package do? (brief description of functionality)
  - What name do they want? (add a "Wagtail" or "Django" prefix if it seems sensible)
  - Is this a new package or an extraction from an existing project?
  - Where will the repository live? (repo org/username and repo name)
  - Any specific requirements? (license, Python/Django/Wagtail version constraints, database backends)
- [ ] If extracting from an existing project, understand what code will move into the package and what integration points exist.
- [ ] Report back a summary of the plan before proceeding.

### Assess current tooling setup

- [ ] Confirm the user has the required tools available: `uv`, `uvx` (for `cookiecutter`), `npm`, `just`.
- [ ] Check Node and Python versions (`node --version`, `uv run python --version`).
- [ ] Note any constraints from the user's environment that might affect the setup.

### Retrieve relevant external documentation

- [ ] Fetch the current [Wagtail compatible Django / Python versions](https://docs.wagtail.org/en/stable/releases/upgrading.html) to confirm the template's default support targets are still current.
- [ ] If the user has specific version requirements, cross-reference against the [supported versions of Python](https://devguide.python.org/versions/) and [supported versions of Django](https://www.djangoproject.com/download/).
- [ ] Note any findings that should influence the package configuration.

### Create the package from the template

- [ ] Review the template's `cookiecutter.json` to understand the available parameters.
- [ ] Run the cookiecutter template with the user's inputs:
  ```bash
  uvx cookiecutter https://github.com/wagtail/cookiecutter-wagtail-package --no-input \
    project_name="<name>" \
    project_short_description="<description>" \
    repository_url="<url>"
  ```
  Or interactively if the user prefers to answer prompts.
- [ ] Verify the generated directory structure looks correct.
- [ ] Report what was generated: key files, directory layout, and any template parameters used.

### Customize for the user's goals

- [ ] Review the generated `pyproject.toml` and adjust if needed:
  - Python version requirement (`requires-python`)
  - Django/Wagtail dependency versions
  - Classifiers matching actual support targets
  - License (default is BSD-3-Clause)
- [ ] Review the generated README and update the description, supported versions, or links if they don't match the user's intent.
- [ ] If extracting from an existing project, move the relevant source code into the package's `src/` directory, adjusting imports and module paths as needed.
- [ ] Review CI workflows (`.github/workflows/`) and confirm the test matrix matches the intended support targets (does not need full matrix, just representative).
- [ ] Report any customizations made and the reasoning behind them.

### Initial QA

- [ ] Install the package dependencies: `uv sync --dev` and `npm ci`.
- [ ] Run linting: `just lint` (or the package's equivalent).
- [ ] Run the test suite: `just test` (or the package's equivalent).
- [ ] If the demo project is set up, verify it runs: `just demo`.
- [ ] Fix any issues surfaced by QA. Report fixes to the user.
- [ ] Note any warnings or issues that need the user's attention but don't block initial setup.

### Produce the handoff report

- [ ] Check specific instructions from the user or the coding harness on how to report information.
- [ ] Deliver the report covering the sections below.

## Report format

```markdown
# Package creation report: {package name}

## Executive summary

{1-2 paragraphs: what was created, from which template, with which key parameters. Brief note on QA results.}

## Package overview

| Aspect | Value |
|--------|-------|
| Package name | {name} |
| Python package | {snake_case name} |
| PyPI name | {kebab-case name} |
| Repository | {URL} |
| License | {license} |
| Python | {requires-python} |
| Django | {dependency range} |
| Wagtail | {dependency range} |

### Key files

{Brief tour of the generated structure -- what's where and why. Focus on files the user will want to edit first.}

### CI and publishing

{What's configured in GitHub Actions. Mention the two manual setup steps for PyPI publishing (trusted publisher + GitHub environment).}

## Next steps

Recommended actions, roughly in order:

1. {First thing to do -- e.g. initialize a git repo, or start adding package code}
2. {Second thing -- e.g. set up the GitHub repository}
3. ...

### Optional improvements

- {Suggestions for things the user might want to add or change, with links to relevant docs}
```
