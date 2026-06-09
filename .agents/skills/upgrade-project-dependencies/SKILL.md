---
name: upgrade-project-dependencies
description: Keeps a Django/Wagtail project current with dependency updates by assessing current setup, applying safe package updates, and delivering a thorough upgrade report
license: MIT
---

## Overview

Structured dependency maintenance workflow for Django/Wagtail projects and packages. Starts with understanding the project's current dependency and tooling setup, validates upgrade decisions against authoritative sources, then applies and verifies updates with clear reporting.

## Methodology

### Goals

- Build a precise baseline of the project's current dependency setup before making changes.
- Use authoritative documentation and release notes to guide every update decision.
- Upgrade dependencies in small, reviewable steps with QA checks.
- Deliver a comprehensive report with evidence, links, outcomes, and next actions.

### Guardrails

- Prefer minimal, reversible, reviewable changes over broad refactors.
- Avoid unrelated code cleanup unless required to complete or validate dependency updates.
- Do not guess compatibility. If unsure, stop and verify against official docs.
- Keep lockfiles in sync with dependency declarations.
- Report assumptions explicitly when a source does not provide a definitive answer.

### Input

To detect from context or request from the user if unclear:

- Scope: audit-only, or audit + apply updates. Default: "audit first, then ask before applying changes".
- Target set: all dependencies, only runtime dependencies, only tooling/dev dependencies, or a specific package.
- Version policy: latest available, latest non-breaking, or pinned target versions.
- Narrow or broad version range: for package dependencies, whether it might be best to keep a wide version compatibility range.
- Risk tolerance: conservative (security/patch only) or proactive (minor/major where supported).

### Assess current project setup first

Before retrieving external information or changing files, establish how this project currently works:

- [ ] Dependency management tools (`uv`, `pip`, `pip-tools`, `poetry`, `npm`, lockfiles in use).
- [ ] Python/Django/Wagtail versions and compatibility constraints in `pyproject.toml` and CI.
- [ ] Linting/formatting/test tooling and commands (`just lint`, `just test`, etc.).
- [ ] CI matrix and release workflows that define supported versions.
- [ ] Any upgrade policies documented in `README`, `CONTRIBUTING`, or maintainer docs.

Report this baseline before proposing upgrade actions.

### Reference data sources

Always prioritize official, authoritative documentation and release notes.

Core platform compatibility:

- [Python supported versions](https://devguide.python.org/versions/)
- [Django supported versions and release notes](https://www.djangoproject.com/download/)
- [Wagtail release notes index](https://docs.wagtail.org/en/stable/releases/index.html)
- [Wagtail compatible Django/Python versions](https://docs.wagtail.org/en/stable/releases/upgrading.html)

Packaging and dependency standards:

- [Python Packaging User Guide](https://packaging.python.org/en/latest/)
- [Writing your pyproject.toml](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/)

Dependency-specific references:

- [PyPI project pages](https://pypi.org/) for release history and metadata.
- Official changelog/release notes for each dependency being updated.
- Official migration guides for major versions.

### Reporting

Dependency maintenance must be transparent and evidence-based:

- Link every major decision to an explicit source.
- Differentiate observed facts, assumptions, and recommendations.
- Report both what changed and what was considered but intentionally deferred.
- Include QA outcomes and any residual risk.
- If useful, provide a follow-up test plan for manual verification.

### Quality assurance

Use project commands where available:

- Install/sync succeeds (`uv sync --dev`, `npm ci`, or project equivalent).
- Linting passes (`just lint` or equivalent).
- Tests pass (`just test` or equivalent).
- Demo/dev server smoke test where relevant (`just demo` or equivalent).
- No new deprecation warnings introduced (or documented if unavoidable).

### Definition of done

- Baseline project setup documented.
- Authoritative sources checked and cited for all important upgrade decisions.
- Dependency files and lockfiles updated consistently (if applying changes).
- QA checks completed with outcomes reported.
- Comprehensive report delivered with clear recommended next steps.

## Steps

### Clarify scope and constraints

- [ ] Confirm whether to audit only or to apply updates.
- [ ] Confirm target dependencies and version policy.
- [ ] Confirm acceptable risk level for major upgrades.

### Baseline the current setup

- [ ] Read dependency manifests and lockfiles (`pyproject.toml`, `uv.lock`, `package.json`, etc.).
- [ ] Identify current versions for Python, Django, Wagtail, and key tooling dependencies.
- [ ] Inspect QA commands and CI matrix to understand supported version boundaries.
- [ ] Share a concise baseline summary before external research.

### Research upgrade path from authoritative sources

For each dependency candidate:

- [ ] Check current vs latest available version.
- [ ] Read official release notes/changelog entries between current and target.
- [ ] Check compatibility constraints against Python/Django/Wagtail support windows.
- [ ] Identify required code/config migrations and potential breaking changes.
- [ ] Cite links for each conclusion.

### Plan updates in logical batches

- [ ] Group by risk and coupling (for example: tooling-only, framework stack, runtime libs).
- [ ] Prioritize low-risk/high-value updates first.
- [ ] For major updates, define migration tasks and rollback approach.
- [ ] Present the update plan to the user before applying changes.

### Apply updates and validate

- [ ] Update dependency declarations and lockfiles together.
- [ ] Run QA after each batch.
- [ ] Resolve issues introduced by upgrades with minimal targeted changes.
- [ ] Capture warnings/errors and how they were addressed.

### Produce a thorough maintenance report

- [ ] Summarize baseline, sources consulted, and methodology.
- [ ] Document each upgraded or deferred dependency with rationale.
- [ ] Include compatibility notes, migration actions, and QA evidence.
- [ ] Provide prioritized next steps and optional follow-up improvements.

## Report format

```markdown
# Dependency maintenance report: {project name}

Date: {YYYY-MM-DD}
Scope: {audit-only | audit-and-apply}

## 1. Baseline project setup

- Dependency management tools: {uv/pip/poetry/npm/...}
- Current core versions: Python {x}, Django {x}, Wagtail {x}
- QA commands: {commands}
- CI support matrix: {summary}

## 2. Authoritative sources consulted

- {Source name and link}
- {Source name and link}
- ...

## 3. Findings and decisions

| Dependency | Current | Target | Decision | Rationale | Sources |
|---|---|---|---|---|---|
| {name} | {x} | {y} | {Upgrade/Defer} | {short reason} | {links} |

## 4. Changes applied

- {Grouped list of actual updates}
- {Any migration/code/config updates required}

## 5. Validation results

- Install/sync: {pass/fail + notes}
- Lint: {pass/fail + notes}
- Tests: {pass/fail + notes}
- Demo/smoke checks: {pass/fail + notes}
- Warnings/deprecations: {none/list}

## 6. Deferred items and risk notes

- {Dependency}: {why deferred, trigger to revisit}
- {Any known risk that remains}

## 7. Recommended next steps

1. {highest-priority next action}
2. {next action}
3. {optional improvements}
```
