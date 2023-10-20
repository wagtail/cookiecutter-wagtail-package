# Wagtail {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{{ cookiecutter.__license_options_readme_badges[cookiecutter.open_source_license] }}
[![PyPI version](https://badge.fury.io/py/{{ cookiecutter.__project_name_kebab }}.svg)](https://badge.fury.io/py/{{ cookiecutter.__project_name_kebab }})
[![{{ cookiecutter.project_name }} CI](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_name_kebab }}/actions/workflows/test.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_name_kebab }}/actions/workflows/test.yml)

## Links

- [Documentation](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_name_kebab }}/blob/main/README.md)
- [Changelog](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_name_kebab }}/blob/main/CHANGELOG.md)
- [Contributing](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_name_kebab }}/blob/main/CONTRIBUTING.md)
- [Discussions](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_name_kebab }}/discussions)
- [Security](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_name_kebab }}/security)

## Supported versions

- Python ...
- Django ...
- Wagtail ...

## Installation

- `python -m pip install {{ cookiecutter.__project_name_kebab }}`
- ...

## Contributing

### Install

To make changes to this project, first clone this repository:

```sh
git clone https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_name_kebab }}.git
cd {{ cookiecutter.__project_name_kebab }}
```

With your preferred virtualenv activated, install testing dependencies:

#### Using pip

```sh
python -m pip install --upgrade pip>=21.3
python -m pip install -e .[testing] -U
```

#### Using flit

```sh
python -m pip install flit
flit install
```

### pre-commit

Note that this project uses [pre-commit](https://github.com/pre-commit/pre-commit).
It is included in the project testing requirements. To set up locally:

```shell
# go to the project directory
$ cd {{ cookiecutter.__project_name_kebab }}
# initialize pre-commit
$ pre-commit install

# Optional, run all checks once for this, then the checks will run only on the changed files
$ git ls-files --others --cached --exclude-standard | xargs pre-commit run --files
```

### How to run tests

Now you can run tests as shown below:

```sh
tox
```

or, you can run them for a specific environment `tox -e python3.11-django4.2-wagtail5.1` or specific test
`tox -e python3.11-django4.2-wagtail5.1-sqlite {{ cookiecutter.__project_name_kebab }}.tests.test_file.TestClass.test_method`

To run the test app interactively, use `tox -e interactive`, visit `http://127.0.0.1:8020/admin/` and log in with `admin`/`changeme`.
