# Wagtail {{ cookiecutter.project_name }}

{{ cookiecutter.project_short_description }}

{% if cookiecutter.open_source_license == 'MIT license' -%}
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
{% elif cookiecutter.open_source_license == 'BSD license' %}
[![License](https://img.shields.io/badge/License-BSD_3--Clause-blue.svg)](https://opensource.org/licenses/BSD-3-Clause)
{% elif cookiecutter.open_source_license == 'ISC license' -%}
 [![License: ISC](https://img.shields.io/badge/License-ISC-blue.svg)](https://opensource.org/licenses/ISC)
{% elif cookiecutter.open_source_license == 'Apache Software License 2.0' -%}
[![License](https://img.shields.io/badge/License-Apache_2.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
{% elif cookiecutter.open_source_license == 'GNU General Public License v3' -%}
{% endif %}
[![PyPI version](https://badge.fury.io/py/{{ cookiecutter.project_name_kebab }}.svg)](https://badge.fury.io/py/{{ cookiecutter.project_name_kebab }})
[![{{ cookiecutter.project_name }} CI](https://github.com/wagtail/{{ cookiecutter.project_name_kebab }}/actions/workflows/test.yml/badge.svg)](https://github.com/wagtail/{{ cookiecutter.project_name_kebab }}/actions/workflows/test.yml)

## Links

- [Documentation](https://github.com/wagtail/{{ cookiecutter.project_name_kebab }}/blob/main/README.md)
- [Changelog](https://github.com/wagtail/{{ cookiecutter.project_name_kebab }}/blob/main/CHANGELOG.md)
- [Contributing](https://github.com/wagtail/{{ cookiecutter.project_name_kebab }}/blob/main/CHANGELOG.md)
- [Discussions](https://github.com/wagtail/{{ cookiecutter.project_name_kebab }}/discussions)
- [Security](https://github.com/wagtail/{{ cookiecutter.project_name_kebab }}/security)

## Supported versions

- Python ...
- Django ...
- Wagtail ...

## Installation

- `pip install {{ cookiecutter.project_name_kebab }}`
- ...
