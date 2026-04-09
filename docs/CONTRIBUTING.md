# Contributing guidelines

This document contains information for anyone wishing to contribute to the project.

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


-------------









## Writing tests

There is a simple test pattern library app in the `tests/` folder. The tests modules themselves and are `tests/tests`.

## Code review

Create a pull request with your changes so that it can be code reviewed by a maintainer. Ensure that you give a summary with the purpose of the change and any steps that the reviewer needs to take to test your work. Please make sure to provide unit tests for your work.

## Releasing a new version

On the `main` branch:

1. Bump the release number in `pyproject.toml`
2. Update the CHANGELOG
3. Commit and tag the release:
   ```sh
   git commit -m "Updates for version 0.1.14"
   git tag -a v0.1.14 -m "Release version v0.1.14"
   git push --tags
   ```
4. Check that your working copy is clean by running:
   ```sh
   git clean -dxn -e __pycache__
   ```
   Any files returned by this command should be removed before continuing to prevent them being included in the build.
5. Install the locked versions of the `node` dependencies and run the production build.

   You can either do this directly on your local machine:

   ```sh
   npm ci
   npm run build
   ```

   Or, via the docker container:

   ```sh
   docker-compose run frontend npm ci
   docker-compose run frontend npm run-script build
   ```

6. Package the new version using `poetry build`

7. Test the newly-built package:
   Find the file ending in `.whl` in the `dist` directory
   Copy it to a test local build.
   Run this to install it on the test build:

   ```sh
   pip install django_pattern_library-0.2.6-py3-none-any.whl
   ```

   Verify that the pattern library is working as you expect it to on your local build.

8. Upload the latest version to PyPI (requires credentials, ask someone named in the [maintainers listed on PyPI](https://pypi.org/project/django-pattern-library/)): `poetry publish`
