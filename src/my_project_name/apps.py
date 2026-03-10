from django.apps import AppConfig


class {{ cookiecutter.__project_name_camel }}AppConfig(AppConfig):
    label = "{{ cookiecutter.__project_name_snake }}"
    name = "{{ cookiecutter.__project_name_snake }}"
    verbose_name = "Wagtail {{ cookiecutter.project_name }}"
