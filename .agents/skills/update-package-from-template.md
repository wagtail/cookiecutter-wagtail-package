---
name: update-package-from-template
description: Updates an existing Wagtail/Django package to align with the latest cookiecutter-wagtail-package template
license: MIT
---

## Overview

Structured review and update of an existing Wagtail or Django package against the latest [cookiecutter-wagtail-package](https://github.com/wagtail/cookiecutter-wagtail-package) template. Compares the current package setup with the template, reports differences and recommended actions, and optionally applies updates.

## Methodology

### Goals

- Understand what the user wants to achieve with the update and any constraints on scope.
- Compare the package's current setup with the template to identify meaningful differences.
- Produce an actionable report: what changed, what matters, what to do about it.
- If the user wants direct updates, apply changes incrementally with QA checks at each step.

### Guardrails

- Prefer minimal, reviewable changes. Do not bundle unrelated improvements into the update.
- Distinguish between differences that are template drift (the package fell behind) and intentional customizations (the package diverged for a reason). Ask when unsure.
- Do not overwrite intentional customizations unless the user explicitly asks.
- When a change is ambiguous, present the trade-off rather than assuming. Choose the option with the least technical debt if forced to decide.
- Base findings on observable project state and authoritative sources. Do not speculate about intent.

### Input

To detect from the context or request from the user if unclear:

- Agent mode: whether to produce an audit report, or directly apply updates. Default: assume "audit first, then ask before applying changes".
- Package location: path to the package to update. Default: current working directory.
- Template version: which version of the template to compare against. Default: latest from `main` branch of the [cookiecutter-wagtail-package](https://github.com/wagtail/cookiecutter-wagtail-package) repository.
- Scope: full comparison or focused on specific areas (e.g. CI only, dependencies only). Default: full comparison.
- Any files or patterns the user considers intentional deviations from the template.

### Reference data sources

Always fetch latest information from authoritative sources so findings are current.

Template and ecosystem:

- [cookiecutter-wagtail-package repository](https://github.com/wagtail/cookiecutter-wagtail-package) -- the template source of truth. Read the `CHANGELOG.md`, `pyproject.toml`, `src/`, `template/`, and other root configuration files.
- [Wagtail package maintenance guidelines](https://wagtail.org/package-guidelines/)

Versions and compatibility:

- [Supported versions of Python](https://devguide.python.org/versions/)
- [Supported versions of Django](https://www.djangoproject.com/download/)
- [Supported versions of Wagtail](https://github.com/wagtail/wagtail/wiki/Release-schedule)
- [Wagtail compatible Django / Python versions](https://docs.wagtail.org/en/stable/releases/upgrading.html)

Packaging:

- [Python Packaging User Guide](https://packaging.python.org/en/latest/)
- [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

### Reporting

Updates are sensitive tasks. Report clearly at each stage so the user stays oriented.

- Use text formatting (tables, lists, Markdown links).
- Link to relevant documentation pages when mentioning tools or standards.
- When sharing docs references, link to the HTML pages rather than raw sources.
- Report on both the methodology and the outcome.
- Be specific. "Template now uses `uv` instead of `pip`" is better than "build tooling changed".

### Commit and pull request strategy

If the current task mode is to apply updates directly, commit regularly on a new branch unless otherwise noted by project instructions.

Commit for:

- Configuration and tooling changes (pyproject.toml, justfile, tox.ini, etc.)
- CI workflow updates
- Dependency changes
- Documentation updates

Push if allowed from current permissions or after user confirmation, when:

- We want to see results from Continuous Integration tools.
- We want human review.
- We think the work is done.

### Quality assurance

Options to check that the update works correctly, to use as needed - make sure to use the project’s commands if different:

- Package installs without errors (`uv sync --dev`)
- Linting passes (`just lint` or equivalent)
- Test suite passes (`just test` or equivalent)
- Demo project runs (`just demo` or equivalent)

Look for any deprecation warnings or new errors introduced by the changes.

### Definition of done

- All meaningful template differences identified and reported.
- If applying changes: updated files are consistent, QA passes, no new warnings introduced.
- Upgrade report delivered to the user with clear next steps.

## Steps

### Confirm the user's goals

- [ ] Read the user's request to understand what they want from the update.
- [ ] If the scope is unclear, ask:
  - Do they want a full comparison or focus on specific areas?
  - Are there files or patterns they consider intentional deviations?
  - Do they want changes applied directly, or just a report?
- [ ] Report a summary of the plan before proceeding.

### Assess current package setup

Understand the package before comparing it. Read key configuration and documentation files:

- [ ] Package metadata (`pyproject.toml` or `setup.cfg`/`setup.py`)
- [ ] Task runner configuration (`justfile`, `Makefile`, or equivalent)
- [ ] Test configuration (`tox.ini`, `nox`, or equivalent)
- [ ] CI workflows (`.github/workflows/`)
- [ ] Linting and formatting tools (ruff, prettier, editorconfig, pre-commit)
- [ ] Documentation files (README, CONTRIBUTING, CHANGELOG, LICENSE, SECURITY)
- [ ] Demo project setup
- [ ] Python version pinning and dependency management (lockfiles, `.python-version`)
- [ ] Source code structure (`src/` layout, apps, migrations, static, templates)

Report a summary of the current setup to the user before proceeding.

### Retrieve the template for comparison

- [ ] Fetch or read the latest template files from [cookiecutter-wagtail-package](https://github.com/wagtail/cookiecutter-wagtail-package):
  - Root configuration files (`pyproject.toml`, `justfile`, `tox.ini`, `ruff.toml`, `.editorconfig`, `.pre-commit-config.yaml`, `package.json`, `prettier.config.js`)
  - Template overlay files (`template/` directory)
  - Source scaffold (`src/` directory structure and key files like `apps.py`, `test/settings.py`)
  - CI workflows if present
- [ ] Fetch current version and compatibility data from the authoritative sources listed above.
- [ ] Note the current date and use it to determine what is EOL or upcoming.

### Compare the package with the template

Work through each area systematically. For every difference:

- [ ] Determine whether it is template drift, an intentional customization, or a new template feature.
- [ ] Assess the impact of aligning with the template (does it fix a problem, improve maintenance, or is it cosmetic?).
- [ ] Note where the package is already ahead of the template (newer tools, stricter config, extra features).

Key comparison areas:

- [ ] **Build and packaging**: `pyproject.toml` structure, build backend, metadata fields, dependency ranges, classifiers, `requires-python`.
- [ ] **Task runner**: commands available, naming conventions, tool versions.
- [ ] **Testing**: test runner, configuration, test app structure, settings.
- [ ] **CI/CD**: workflow structure, matrix (Python/Django/Wagtail versions), publishing setup, additional checks.
- [ ] **Linting and formatting**: tools used, configuration, scope.
- [ ] **Documentation**: README structure, CONTRIBUTING guide, CHANGELOG format, LICENSE, SECURITY policy.
- [ ] **Source structure**: directory layout, app configuration, module organization.

### Report differences and recommended actions

- [ ] Compile all findings into the report format below.
- [ ] Write the executive summary.
- [ ] Organize findings into the differences overview.
- [ ] Rate each finding for effort and impact.
- [ ] Identify the top 10 recommended actions by impact-to-effort ratio.
- [ ] Present the report to the user.

### Apply updates (if requested)

Only proceed with this step if the user confirms they want direct changes.

- [ ] Create a branch for the update (check any conventions for branch names, or `update-from-template`).
- [ ] Apply changes in logical groups, committing after each group.
- [ ] Run QA checks after each group of changes.
- [ ] Report any issues encountered and how they were resolved.
- [ ] Produce a final summary of all changes applied.

## Report format

```markdown
# Template update report: {package name}

Compared on {date} against [cookiecutter-wagtail-package](https://github.com/wagtail/cookiecutter-wagtail-package) (`main` branch).

## Executive summary

{1-3 paragraphs: what was compared, methodology, high-level findings. How many differences found, how many need action, overall alignment with the template.}

## Differences overview

{For each comparison area, a subsection with findings.}

### {Area name}

| Aspect | Package | Template | Status |
|--------|---------|----------|--------|
| {aspect} | {current value} | {template value} | {Aligned / Drifted / Intentional / New in template} |

{Brief notes on context or trade-offs where relevant.}

## Recommended actions

The top 10 differences ranked by impact relative to effort:

| # | Action | Effort | Impact | Area |
|---|--------|--------|--------|------|
| 1 | {description} | {XS-XL} | {XS-XL} | {area} |

### Effort and impact scales

- **XS**: Super quick. Change a config value, add a line.
- **S**: Small task. Add a CI job, update a dependency, write a short doc section.
- **M**: Decent task. Set up a new tool, write a contributing guide.
- **L**: Major task. Redesign documentation, set up a new CI pipeline.
- **XL**: Epic. Major structural changes, comprehensive test suite overhaul.
```
