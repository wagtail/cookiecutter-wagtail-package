# cookiecutter-wagtail-package

A [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template for building Wagtail and Django packages according to the the Wagtail [package maintenance guidelines](https://wagtail.org/package-guidelines/).

## Usage

```bash
# Shortest one-liner, you will be prompted for important package information.
uvx cookiecutter gh:wagtail/cookiecutter-wagtail-package
```

## What's included

The generated package contains:

- A Django app under `src/` with an `AppConfig`, empty `models.py`, and example `wagtail_hooks.py` (Wagtail admin summary item and admin URL registration with i18n support).
- A `demo/` Wagtail site with home, blog, and search apps, ready to run with `just demo`.
- A `tests/` directory with pytest and pytest-django configured, and a placeholder test.
- A `justfile` with recipes for linting, formatting, testing, coverage, and running the demo.
- Project configuration with `pyproject.toml` (uv build backend), `ruff.toml`, pre-commit hooks, Prettier, and Stylelint.

### CI

The generated package includes GitHub Actions workflows for:

- Running tests and linters on pushes and pull requests.
- Testing against the lowest and highest supported dependency versions, and a compatibility matrix of Python, Django, and Wagtail versions.
- Running tests nightly against the latest Wagtail development version (with optional Slack notifications on failure).
- CodeQL security scanning and GitHub Actions security analysis with zizmor.
- Publishing to PyPI when GitHub releases are created. This requires two additional setup steps:
  - Create a pending publisher in PyPI: https://docs.pypi.org/trusted-publishers/creating-a-project-through-oidc/
  - Create an environment called "publish" in GitHub: https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment#creating-an-environment

### What's not included

The following are intentionally left out of the template:

- **Frontend build tools** (Vite, webpack, esbuild). Many packages don't need a build step, and those that do have varied requirements. Set up a build pipeline based on your package's needs.
- **Example models, views, or forms**. The generated `models.py` is empty -- the `wagtail_hooks.py` demonstrates Wagtail integration, but the package's domain logic is yours to define.
- **Internationalization scaffolding**. While the `wagtail_hooks.py` registers a JavaScript i18n catalog URL, there is no `locale/` directory or example translations. Add these when your package needs them.

## How to use

### With cookiecutter

Install cookiecutter:

    python -m pip install "cookiecutter>=2"

Then run it like so:

    cookiecutter git@github.com:wagtail/cookiecutter-wagtail-package.git

It'll ask for some details about you (name and email) and your project.

When it asks for your project name, exclude the "Wagtail" prefix.
For example, if your project is called "Wagtail Llamas", set your project name to "Llamas" and accept all the default project name variants it generates (unless you used a special character in the project name).

### Agent skills

This project includes reusable [agent skills](https://agentskills.io/) for AI coding agents. Install the project skills with [Vercel Lab’s Agent Skills CLI](https://github.com/vercel-labs/agent-skills):

```sh
npx skills add wagtail/cookiecutter-wagtail-package
```

#### Create a package from scratch

[create-django-package](.agents/skills/create-django-package.md) creates a new Wagtail/Django package from the cookiecutter-wagtail-package template. Example prompts:

- "Create a new Wagtail package called 'Wagtail Color Picker' for adding a color field to Wagtail pages"
- "Set up a new Django package called 'django-webhook-relay' for forwarding webhook events to multiple endpoints"

#### Create a package from existing code

[create-django-package](.agents/skills/create-django-package.md) also supports extracting Django apps from an existing project to make them reusable as a package. Example prompts:

- "Extract the `myproject/analytics` app into a standalone Wagtail package called 'Wagtail Analytics'"
- "Turn the `utils/markdown_fields.py` module into a reusable Django package"

#### Package guidelines audit

[package-guidelines-audit](.agents/skills/package-guidelines-audit.md) audits a Django/Wagtail package against the official [Wagtail package maintenance guidelines](https://wagtail.org/package-guidelines/). Example prompts:

- "Audit this package against the Wagtail package guidelines"
- "Check whether this package's CI and version support are up to date with Wagtail's guidelines"

#### Update package from template

[update-package-from-template](.agents/skills/update-package-from-template.md) updates an existing Wagtail/Django package to align with the latest cookiecutter-wagtail-package template. Example prompts:

- "Compare this package with the latest cookiecutter-wagtail-package template and report any differences"
- "Update this package's tooling and CI to match the latest cookiecutter-wagtail-package template"
