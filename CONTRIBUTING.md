# Contributing guidelines

Thank you for your interest in this project! We welcome all contributions, from bug reports to new features that align with [our roadmap](ROADMAP.md).

## How the template works

For ease of maintenance and usage, this repository is both a cookiecutter template _and_ a working Django/Wagtail package. The project root is the template itself -- when a new package is generated, those files are copied as-is. Only a handful of files in the `template/` directory differ between this repo and the generated project: `README.md`, `CONTRIBUTING.md`, `CHANGELOG.md`, `LICENSE`, and `ROADMAP.md`. With the [hooks/pre_prompt.py script](./hooks/pre_prompt.py), we will also adjust specific placeholders.

In practice, this means that most contributions are made directly to the root files and will be reflected in newly-generated packages. The `template/` files should be written as if they are part of the generated project, not this repo.

## Installation

The repo includes a simple demo application that can be run to develop the package itself. Give it a try by following the instructions below for a local setup.

First, clone the repo:

```sh
git clone git+https://github.com/wagtail/cookiecutter-wagtail-package
cd cookiecutter-wagtail-package
```

We use [just](https://github.com/casey/just) as a task runner, [prek](https://github.com/j178/prek) for pre-commit hooks, and [uv](https://docs.astral.sh/uv/) to manage Python dependencies. Make sure you have all three installed.

Then you can install the dependencies and run the demo app:

```sh
just install
just demo
```

## Quality assurance

Here are the available tooling scripts for the project:

```sh
just clean-pyc         # Remove all the Python and Node.js cache files.
just coverage          # Run tests with coverage.
just demo              # Run the demo application.
just format            # Run all formatters.
just format-client     # Format the client code with Prettier.
just format-server     # Format the server code with uv.
just help              # List all the justfile recipes.
just install           # Install the dependencies.
just lint              # Run all linters.
just lint-client       # Lint the client code with Prettier.
just lint-server       # Lint the server code with uv.
just load_initial_data # Load the initial data into the database.
just migrate           # Make migrations and migrate the database.
just runserver         # Run the development server at the given host and port.
just shell             # Open a shell to the demo application.
just test              # Run tests with pytest.
```

## Writing tests

There is a simple test app in `tests/`. Write your test modules there alongside the existing files.

## Code review

Create a pull request with your changes so that it can be reviewed by a maintainer. Ensure that you give a summary with the purpose of the change and any steps that the reviewer needs to take to test your work. Please make sure to provide unit tests for your work.

## Releases

On the `main` branch:

1. Update the version number in `pyproject.toml`.
2. Update the [CHANGELOG](CHANGELOG.md) and [ROADMAP](ROADMAP.md).
3. Commit and tag the release. (`git commit -m "Release v0.1.1" & git tag -a v0.1.1 -m "Release v0.1.1" && git push --tags`)
4. Create a GitHub release from the tag. The CI will automatically build and publish the package to PyPI.
