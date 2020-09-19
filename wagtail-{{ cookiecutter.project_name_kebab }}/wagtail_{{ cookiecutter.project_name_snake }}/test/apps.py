from django.apps import AppConfig


class Wagtail{{ cookiecutter.project_name_camel }}TestAppConfig(AppConfig):
    label = "wagtail_{{ cookiecutter.project_name_snake }}_test"
    name = "wagtail_{{ cookiecutter.project_name_snake }}.test"
    verbose_name = "{{ cookiecutter.project_name }} tests"
