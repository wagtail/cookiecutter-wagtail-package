from django.apps import AppConfig


class {{ cookiecutter.__project_name_camel }}TestAppConfig(AppConfig):
    label = "{{ cookiecutter.__project_name_snake }}_test"
    name = "{{ cookiecutter.__project_name_snake }}.test"
    verbose_name = "Wagtail {{ cookiecutter.project_name }} tests"
