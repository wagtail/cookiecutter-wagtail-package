# Configuration

Most configuration for My project name lives in `settings.py` via Django settings, or via [Wagtail hooks](api.md#wagtail-hooks) registered by the package.

## Django settings

Docs the settings the package reads, with their defaults and effects:

| Setting | Default | Description |
|---|---|---|
| `MY_PROJECT_NAME_SOME_OPTION` | `True` | Replace this table with the package's real settings. |

Override them in your project:

```python
# settings.py
MY_PROJECT_NAME_SOME_OPTION = False
```

## Wagtail hooks

The package registers hooks in `my_project_name/wagtail_hooks.py`. These demonstrate a homepage summary item and admin URLs:

- `construct_homepage_summary_items` – adds a `MyProjectNameSummaryItem` to the admin homepage.
- `register_admin_urls` – namespaces admin URLs under `/admin/my_project_name/` with a JavaScript catalog for [translatable strings](https://github.com/org-name-or-username/my-project-name/blob/main/CONTRIBUTING.md#translations).

## Adding configuration

Keep the list in this page in sync with the settings and hooks the package ships. This is part of the [documentation & tooling](../contributing/documentation.md) guidance.
