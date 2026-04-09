# Task runner: https://github.com/casey/just
# Requires: `uv`, `npm`, and `just`.
# Editable package path under `src/` (passed to `coverage run --source`).

src_package := "src/my_project_name"

# List all the justfile recipes.
help:
    just --list --list-prefix 'just '

# Remove all the Python and Node.js cache files.
clean-pyc:
    find . -name '*.pyc' -exec rm -f {} +
    find . -name '*.pyo' -exec rm -f {} +
    find . -name '*~' -exec rm -f {} +

# Install the dependencies.
install: clean-pyc
    uv sync --dev
    npm ci

# Lint the server code with uv.
lint-server:
    uv run ruff format --check .
    uv run ruff check .
    SKIP=ruff,ruff-format uv run prek run --all-files

# Lint the client code with Prettier.
lint-client:
    npm run lint --loglevel silent

# Run all linters.
lint: lint-server lint-client

# Format the server code with uv.
format-server:
    uv run ruff check . --fix
    uv run ruff format .
    SKIP=ruff,ruff-format uv run prek run --all-files

# Format the client code with Prettier.
format-client:
    npm run format

# Run all formatters.
format: format-server format-client

# Run tests with pytest.
test:
    uv run pytest

test-lowest-deps:
    #!/usr/bin/env bash
    set -euo pipefail
    lowest_python=$(uv run python -c 'import tomllib; print(tomllib.load(open("pyproject.toml","rb"))["project"]["requires-python"].removeprefix(">=").strip())')
    uv run --isolated --python "$lowest_python" --resolution lowest-direct pytest

test-highest-deps:
    uv run --isolated --with 'Django, Wagtail' pytest

# Run tests with coverage.
coverage:
    uv run pytest --cov {{ src_package }}
    uv run coverage report -m
    uv run coverage html
    @if command -v open >/dev/null 2>&1; then \
    	open htmlcov/index.html; \
    elif command -v xdg-open >/dev/null 2>&1; then \
    	xdg-open htmlcov/index.html; \
    else \
    	echo 'Open htmlcov/index.html in your browser.'; \
    fi

# Make migrations and migrate the database.
migrate:
    uv run ./demo/manage.py makemigrations
    uv run ./demo/manage.py migrate

# Run the development server at the given host and port.
runserver:
    uv run ./demo/manage.py runserver

# Load the initial data into the database.
load_initial_data:
    uv run ./demo/manage.py load_initial_data

# Open a shell to the demo application.
shell:
    uv run ./demo/manage.py shell

# Run the demo application.
demo: migrate load_initial_data runserver
