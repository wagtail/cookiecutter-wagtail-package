# cookiecutter-wagtail-plugin

An opinionated cookiecutter template for building Wagtail plugins.

## What's included

### Python

This creates a simple Python/Django app with a nested "test" app.

### CI

This contains CI configs for both CircleCI and Travis.
We use two CI services simultaneously to allow fast response times (CircleCI)
while also allowing us to run a large test matrix at the same time (Travis).

### Docs

This bit isn't done yet. I plan to use Sphinx (because autodoc is very useful for plugins)

### Frontend tooling

This includes a simple webpack setup with TypeScript, React, styled-components, and SVG support.

Note that React is pinned to 16.x because on production it uses the same React library as Wagtail to reduce bundle size.
