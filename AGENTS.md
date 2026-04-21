# Agents

Important context for AI coding agents working on this project.

## Project structure

This repository is both a [cookiecutter](https://cookiecutter.readthedocs.io/en/stable/) template **and** a working Django/Wagtail package. The project root contains the real, runnable package. Only the files in `template/` differ between this repo and generated packages -- see [docs/README.md](docs/README.md) for how the overlay mechanism works.

When making changes:

- Most changes go to **root files** (justfile, pyproject.toml, workflows, src/, tests/, demo/), as if this project itself was a package.
- Files in `template/` must be written **as if they are part of the generated project**, not this repo.
- The `hooks/pre_prompt.py` script replaces specific placeholder strings with cookiecutter variables. If you add new files or references, use the established placeholders: `my_project_name`, `my-project-name`, `MyProjectName`, `My project name`, `org-name-or-username`, `Placeholder: Project short description`.

## Key commands

```sh
jut help        # View all commands
just install    # Install Python and Node.js dependencies
just demo       # Run the demo Wagtail site (migrate + load data + runserver)
just test       # Run tests with pytest
just lint       # Run all linters (Ruff, pre-commit, Prettier, Stylelint)
just format     # Run all formatters (Ruff, Prettier)
just coverage   # Run tests with coverage report
```
