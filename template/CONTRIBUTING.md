# Contributing guidelines

Thank you for your interest in this project! We welcome all contributions, from bug reports to new features that align with [our roadmap](ROADMAP.md). Here are instructions for anyone wishing to contribute.

## Installation

The repo includes a simple demo application that can be run to develop the package itself. Follow the instructions below for a local setup.

First, clone the repo:

```sh
git clone git+https://github.com/org-name-or-username/my-project-name
cd my-project-name
```

> Requirements: [`uv`](https://github.com/astral-sh/uv), [`just`](https://github.com/casey/just), [`prek`](https://prek.j178.dev/)

Then you can install the dependencies and run the demo app:

```sh
just install
just demo
```

## Quality assurance

Here are the available scripts for the project:

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

## Continuous integration

The project uses GitHub Actions for CI. On every push and pull request, the CI will:

- Run linters (Ruff, prek, Prettier).
- Run tests with coverage.
- Run tests against the lowest supported dependency versions.
- Run tests against the latest dependency versions.
- Run tests against a compatibility matrix of Python, Django, and Wagtail versions.

There is also a nightly job that tests against the latest development version of Wagtail, so we catch compatibility issues early.

## Code review

Create a pull request with your changes so that it can be code reviewed by a maintainer. Ensure that you give a summary with the purpose of the change and any steps that the reviewer needs to take to test your work. Please make sure to provide unit tests for your work.

## Releases

On the `main` branch:

1. Update the version number in `pyproject.toml`.
2. Update the [CHANGELOG](CHANGELOG.md) and [ROADMAP](ROADMAP.md).
3. Commit and tag the release. (`git commit -m "Release v0.1.1" & git tag -a v0.1.1 -m "Release v0.1.1" && git push --tags`)
4. Create a GitHub release from the tag. The CI will automatically build and publish the package to PyPI.
