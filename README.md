# cookiecutter-wagtail-packages

A cookiecutter template for building Wagtail add-on packages.

## What's included

This creates a simple Python/Django app with a nested "test" app.

### CI

This contains CI configs for both CircleCI and Github Actions.
We use two CI services simultaneously to allow fast response times (CircleCI)
while also allowing us to run a large test matrix at the same time (Github Actions).

### Frontend tooling

This includes a simple webpack setup with TypeScript, React, styled-components, and SVG support.

Note that React is pinned to 16.x because on production it uses the same React library as Wagtail to reduce bundle size.

I haven't yet added a question into the cookiecutter config that excludes this. So if you don't want it, delete it.

## How to use

Firstly install cookiecutter:

    pip install cookiecutter
    
Then run it like so:

    cookiecutter git@github.com:kaedroho/cookiecutter-wagtail-plugin.git
    
It'll ask for some details about you (name and email) and your project.

When it asks for your project name, exclude the "Wagtail" prefix.
For example, if your project is called "Wagtail Llamas", set your project name to "Llamas" and accept all the default project name variants it generates (unless you used a special character in the project name).
