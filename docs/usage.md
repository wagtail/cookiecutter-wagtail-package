# Usage

Describe here how users interact with the package in their projects: Python API, template tags, Wagtail editors, admin integration, and so on. Use concrete examples built from the package's actual code.

As a starting point, this template ships an example [Wagtail admin hook](reference/api.md#wagtail-hooks): a homepage summary item and a namespaced set of admin URLs with i18n support. Use them as a reference for your own integration.

## Python usage

```python
from my_project_name.something import Something

result = Something().run(...)
```

## Template usage

If the package provides template tags or a template tag library, register it with `templatetags/` and document it here. Load the tag library in templates using Django's `load` tag and call the registered tags.

## Admin integration

Wagtail hooks are registered in `my_project_name/wagtail_hooks.py` and take effect as soon as the app is in `INSTALLED_APPS`. Add your own hooks there, following the existing examples.

## Settings

See [Configuration](reference/configuration.md) for a list of settings and how to override them with `settings.py`.

## Migrations

If the package adds models, generate migrations with `just migrate` and ship them with the package so users don't need to. See the [contributing guidelines](https://github.com/org-name-or-username/my-project-name/blob/main/CONTRIBUTING.md) for the release workflow.
