# cookiecutter-wagtail-package

A cookiecutter template for building Wagtail add-on packages.

## What's included

This creates a simple Python/Django app with a nested "test" app.

### CI

This creates Github Workflows for:

- Running tests and linters on pushes and pull requests
- Running tests nightly against latest Wagtail version
- Pushing packages to PyPI when GitHub releases are created

### Frontend tooling

This includes a simple webpack setup with TypeScript, React, styled-components, and SVG support.

Note that React is pinned to 16.x because on production it uses the same React library as Wagtail to reduce bundle size.

This can be excluded by answering "no" to the `use_frontend` question.

## How to use

Firstly install cookiecutter:

    python -m pip install "cookiecutter>=2"

Then run it like so:

    cookiecutter git@github.com:wagtail/cookiecutter-wagtail-package.git

It'll ask for some details about you (name and email) and your project.

When it asks for your project name, exclude the "Wagtail" prefix.
For example, if your project is called "Wagtail Llamas", set your project name to "Llamas" and accept all the default project name variants it generates (unless you used a special character in the project name).
