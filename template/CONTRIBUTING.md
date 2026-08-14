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

## Translating

Translations are managed using [Django's built-in internationalization framework](https://docs.djangoproject.com/en/6.1/topics/i18n/translation/). The translation files are located in the `src/my_project_name/locale/` directory of the project.

### Authoring guidance for new strings

When adding new translatable strings, use appropriate translation functions in your code. Such as `ngettext` to support pluralization or `pgettext` for context-specific translations. Use `{% raw %}{% blocktrans trimmed %}{% endraw %}` in templates for multi-line strings. The `trimmed` option removes leading and trailing whitespace from the translated string.

Principles for writing translatable strings:

- **Use decent English:** When a string is written in poor English or is ambiguous, it is hard to understand and translate. Include a `# Translators: ...` comment above the string to clarify the meaning if needed. Ask yourself: "If I were a translator, would I understand this string and how it is used in isolation? Do I need to provide additional context?"
- **Entire sentences:** Ensure that each translatable string is a complete sentence. Avoid interpolating or concatenating strings with verbs and nouns to form sentences. This makes it difficult to understand and create grammatically appropriate translations for every scenario.
- **Prefer named placeholders:** When interpolating variables into translatable messages, use named placeholders instead of positional ones (`%(placeholder_name)s` instead of `%s`). This makes it easier for translators to understand the context and allows reordering placeholders as necessary.

For detailed code examples, Wagtail's contribution guide has a section on [marking strings for translation](https://docs.wagtail.org/en/stable/contributing/translations.html#marking-strings-for-translation)

### Updating all translations

It isn't expected of contributors to update the translations after changing or adding new strings, since this often generates git conflicts with other contributors doing the same. If you do want to update all translations, run the following command:

```sh
just makemessages
```

### Adding a new language

[Find your ISO-639 language code](https://en.wikipedia.org/wiki/List_of_ISO_639_language_codes) and run the following command to create a new translation catalog for your language:

```sh
just makemessages -l=<language_code>
```

After that, you can start translating the generated `src/my_project_name/locale/<language_code>/LC_MESSAGES/django.po` file. [POEdit](https://poedit.com/) is a popular tool for editing `.po` files.

### Compiling translations

By default the source code only contains the `.po` files, which are human-readable.
If you want to make the translations available for use in the application, you need to compile them into `.mo` files. You can do this by running:

```sh
just compilemessages
```

## Releases

On the `main` branch:

1. Update the version number in `pyproject.toml`.
2. Update the [CHANGELOG](CHANGELOG.md) and [ROADMAP](ROADMAP.md).
3. Commit and tag the release. (`git commit -m "Release v0.1.1" & git tag -a v0.1.1 -m "Release v0.1.1" && git push --tags`)
4. Create a GitHub release from the tag. The CI will automatically build and publish the package to PyPI.
