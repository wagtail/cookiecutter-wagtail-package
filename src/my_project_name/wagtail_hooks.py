from django.urls import include, path
from django.views.i18n import JavaScriptCatalog
from wagtail import hooks


@hooks.register("register_admin_urls")
def register_admin_urls():
    urls = [
        path(
            "jsi18n/",
            JavaScriptCatalog.as_view(
                packages=["{{ cookiecutter.__project_name_snake }}"]
            ),
            name="javascript_catalog",
        ),
        # Add other package-scoped URLs here so they are access-restricted to the admin.
    ]

    return [
        path(
            "{{ cookiecutter.__project_name_snake }}/",
            include(
                (urls, "{{ cookiecutter.__project_name_snake }}"),
                namespace="{{ cookiecutter.__project_name_snake }}",
            ),
        )
    ]
