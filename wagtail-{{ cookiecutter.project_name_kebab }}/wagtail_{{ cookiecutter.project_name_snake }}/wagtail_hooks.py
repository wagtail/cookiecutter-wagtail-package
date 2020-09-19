from django.urls import path, include
from django.views.i18n import JavaScriptCatalog

from wagtail.core import hooks


@hooks.register("register_admin_urls")
def register_admin_urls():
    urls = [
        path('jsi18n/', JavaScriptCatalog.as_view(packages=['wagtail_{{ cookiecutter.project_name_snake }}']), name='javascript_catalog'),
    ]

    return [
        path(
            "{{ cookiecutter.project_name_snake }}/",
            include(
                (urls, "wagtail_{{ cookiecutter.project_name_snake }}"),
                namespace="wagtail_{{ cookiecutter.project_name_snake }}",
            ),
        )
    ]
