from django.urls import include, path
from django.views.i18n import JavaScriptCatalog
from wagtail.core import hooks


@hooks.register("register_admin_urls")
def register_admin_urls():
    urls = [
        path(
            "jsi18n/",
            JavaScriptCatalog.as_view(packages=["{{ cookiecutter.__project_name_snake }}"]),
            name="javascript_catalog",
        ),
        # Add your other URLs here, and they will appear under
        # `/admin/{{ cookiecutter.__project_name_snake_without_prefix }}/`
        # Note: you do not need to check for authentication in views added here, Wagtail
        # does this for you!
    ]

    return [
        path(
            "{{ cookiecutter.__project_name_snake_without_prefix }}/",
            include(
                (urls, "{{ cookiecutter.__project_name_snake }}"),
                namespace="{{ cookiecutter.__project_name_snake }}",
            ),
        )
    ]
