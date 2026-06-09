---
name: package-guidelines-audit
description: Audits a Django/Wagtail package against the official Wagtail package maintenance guidelines
license: MIT
---

## Overview

Comprehensive audit of a Wagtail (or Django) package against the [Wagtail package maintenance guidelines](https://wagtail.org/package-guidelines/). Produces a structured report with findings, effort/impact ratings, and recommended actions.

## Methodology

### Goals

- Assess the current state of the package against each section of the official guidelines.
- Provide clear, actionable findings with effort and impact ratings.
- Highlight what the package already does well, alongside areas for improvement.
- Produce a structured audit report the maintainer can act on or share with collaborators.

### Guardrails

- This skill is read-only. Do not modify project files unless the user explicitly asks for changes.
- Base findings on observable project state and authoritative sources. Do not speculate about intent or history.
- When a guideline is ambiguous or context-dependent, note this rather than making assumptions.
- If the project's approach deviates from the guidelines but is clearly intentional, acknowledge the trade-off rather than flagging it as a deficiency.
- Keep findings proportional. A package that is 90% compliant should read differently from one that is 10% compliant.

### Input

To detect from the context or request from the user if unclear:

- Agent mode: full audit of all guidelines, or focused on specific sections. Default: full audit.
- Package type: Wagtail-specific or general Django/Python package. Default: infer from project metadata and imports.

### Reference data sources

Always fetch the latest guidelines from the official source:

- [Wagtail package maintenance guidelines](https://wagtail.org/package-guidelines/) -- fetch this at the start of every audit to ensure the guidelines are current.

Combine with authoritative sources for version and support information:

- [Supported versions of Python](https://devguide.python.org/versions/)
- [Supported versions of Django](https://www.djangoproject.com/download/)
- [Supported versions of Wagtail](https://github.com/wagtail/wagtail/wiki/Release-schedule)
- [Wagtail compatible Django / Python versions](https://docs.wagtail.org/en/stable/releases/upgrading.html)
- [Python Packaging User Guide](https://packaging.python.org/en/latest/)
- [PyPI classifiers](https://pypi.org/classifiers/)

Use the project's own metadata and configuration as the primary source of truth for what the package currently does.

### Reporting

The audit report should be thorough, structured, and actionable.

- Link directly to the relevant guideline section and to authoritative sources for every finding.
- Report on the methodology used and assumptions made.
- Be specific when it helps. "Add latest Python to CI matrix" is better than "Update Python support" if that is the only version missing.
- Be honest about positive findings. Confirming compliance is valuable, not filler.

### Quality assurance

- Cross-check findings against the actual project files, not just metadata.
- Verify version claims against authoritative sources (Python, Django, Wagtail release schedules).
- Confirm CI configuration matches declared support targets. Version gaps are acceptable, except for upper and lower bounds.
- Check that documentation claims match actual project state.

## Steps

### Confirm scope and goals

- [ ] Read the user's request to understand any specific focus areas or constraints.
- [ ] If the user's goals are unclear, ask what sections of the guidelines they want to focus on, or confirm that a full audit is desired.
- [ ] Identify whether the package targets Wagtail specifically or is a more general Django/Python package.

### Assess current project setup

Understand the project before evaluating it. Read key configuration and documentation files to build a picture of what the package does and how it is maintained: package metadata, README, changelog, contributing guide, license, CI workflows, test configuration, linting and formatting tools, demo project, frontend tooling, Python version pinning, dependency management automation.

Report a summary of the project setup to the user before proceeding with the audit.

### Retrieve external reference data

Fetch current information from the authoritative sources listed above so findings are based on up-to-date data, not training knowledge. Note the current date and use it to determine EOL status of any version.

### Audit against the guidelines

Work through each section of the fetched guidelines in sequence. For every recommendation in the guidelines:

- [ ] Determine whether it applies to this package (some guidelines are conditional, e.g. frontend tooling only applies if the package ships CSS or JS).
- [ ] Check the project's current state against the recommendation by reading the relevant files.
- [ ] For version support and compatibility claims, cross-reference with the external data fetched earlier.
- [ ] Record the finding: what the guideline expects, what the project does, what action to take (if any).
- [ ] For items that cannot be verified from the repository alone (like shared PyPI access), note them as recommendations to verify manually.

Report indicators of your progress to the user over time, rather than waiting for the full report.

### Produce the audit report

Compile all findings into the report format below.

- [ ] Write the executive summary.
- [ ] Organize findings by guideline section, using the section titles from the fetched guidelines.
- [ ] Rate each finding for effort and impact.
- [ ] Identify the top 10 recommended actions by impact-to-effort ratio.
- [ ] Present the report to the user.

## Report format

```markdown
# Package guidelines audit: {package name}

Audited on {date} against the [Wagtail package maintenance guidelines](https://wagtail.org/package-guidelines/).

## Executive summary

{1-3 paragraphs: what was audited, methodology, high-level findings. How many findings total, how many require action, overall compliance.}

## Audit findings

{For each section of the guidelines, create a subsection (##) with the same title.
Within each subsection, add findings as sub-subsections (###):}

### {Finding title} {checkmark or cross emoji}

Effort: {XS/S/M/L/XL} | Impact: {XS/S/M/L/XL}

{Concise description. What the guideline expects, what the project does, what action to take (if any). Link to relevant sources.}

## Recommended actions

The top 10 findings ranked by impact relative to effort:

| # | Finding | Effort | Impact | Section |
|---|---------|--------|--------|---------|
| 1 | {title} | {XS-XL} | {XS-XL} | {section} |
```

### Effort and impact scales

- **XS**: Super quick. Change a config value, add a line.
- **S**: Small task. Add a CI job, update a dependency, write a short doc section.
- **M**: Decent task. Set up a new tool, write a contributing guide.
- **L**: Major task. Redesign documentation, set up internationalization.
- **XL**: Epic. Major architectural changes, comprehensive test suite overhaul.
