# Getting started

My project name is a reusable Wagtail package. The fastest way to try it is with the included demo site. For your own project, install the package and add it to your Django settings.

## Requirements

- Python 3.10 or newer.
- Django 5.2 or newer.
- Wagtail 7 or newer.

## Try the demo site

Clone the repository and run the bundled demo to see the package in action:

```sh
just install
just demo
```

This runs database migrations, loads initial data, and starts a local server. Open the site at <http://localhost:8000/> and the admin at <http://localhost:8000/admin/>.

## Install in your project

Install the package with pip:

```sh
pip install my-project-name
```

Then add the app to `INSTALLED_APPS` in your Django settings:

```python
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "wagtail",
    "wagtail.contrib.forms",
    "wagtail.contrib.redirects",
    "wagtail.contrib.settings",
    "wagtail.embeds",
    "wagtail.sites",
    "wagtail.users",
    "wagtail.snippets",
    "wagtail.documents",
    "wagtail.images",
    "wagtail.search",
    "wagtail.admin",
    "wagtail.models",
    "wagtail.api.v2",
    "wagtail.contrib.routable_page",
    "wagtail.contrib.styleguide",
    "modelcluster",
    "taggit",
    # Third-party apps.
    "my_project_name",
    # Your project's apps.
]
```

Run the migration to create any database objects the package needs:

```sh
python manage.py migrate
```

## Next steps

- [Usage](usage.md) – configuration, settings, and template integration.
- [API reference](reference/api.md) – the full public API.
- [Configuration](reference/configuration.md) – settings and Wagtail hooks.
