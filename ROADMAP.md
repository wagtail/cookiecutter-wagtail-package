# Roadmap

This roadmap represents the current vision for this project, and is subject to change. We welcome feedback and we’re open to suggestions!

## MariaDB testing in CI

The [package maintenance guidelines](https://wagtail.org/package-guidelines/) recommend supporting all database backends supported by Wagtail. The template currently only tests with SQLite and PostgreSQL.

## Pinned GitHub Actions versions

Pin all GitHub Actions to full commit SHAs rather than version tags, to guard against supply chain attacks. The zizmor workflow already flags this. We should pin all actions across all workflows.

## Dependency management with Renovate

Set up [Renovate](https://docs.renovatebot.com/) (or Dependabot) to automatically create pull requests when dependencies are updated. This covers both Python dependencies in `pyproject.toml` and Node.js dependencies in `package.json`, as well as GitHub Actions versions.
