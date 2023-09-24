# Wagtail {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if cookiecutter.open_source_license == 'MIT license' -%}
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
{%- elif cookiecutter.open_source_license == 'BSD 3-Clause license' -%}
[![License: BSD-3-Clause](https://img.shields.io/badge/License-BSD--3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
{%- elif cookiecutter.open_source_license == 'ISC license' -%}
[![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](https://opensource.org/licenses/ISC)
{%- elif cookiecutter.open_source_license == 'Apache Software License 2.0' -%}
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache--2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
{%- elif cookiecutter.open_source_license == 'GNU General Public License v3' -%}
[![License: GPL-3.0-only](https://img.shields.io/badge/License-GPL--3.0--only-blue.svg)](https://opensource.org/licenses/GPL-3.0)
{% endif %}
[![PyPI version](https://badge.fury.io/py/{{ cookiecutter.__project_name_kebab }}.svg)](https://badge.fury.io/py/{{ cookiecutter.__project_name_kebab }})
[![{{ cookiecutter.project_name }} CI](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_name_kebab }}/actions/workflows/test.yml/badge.svg)](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_name_kebab }}/actions/workflows/test.yml)

## Links

- [Documentation](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_name_kebab }}/blob/main/README.md)
- [Changelog](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_name_kebab }}/blob/main/CHANGELOG.md)
- [Contributing](https://github.com/{{ cookiecutter.github_username }}/{{ cookiecutter.__project_name_kebab }}/blob/main/CHANGELOG.md)
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
