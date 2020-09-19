from django.apps import AppConfig


class Wagtail{{ cookiecutter.project_name_camel }}AppConfig(AppConfig):
    label = "wagtail_{{ cookiecutter.project_name_snake }}"
    name = "wagtail_{{ cookiecutter.project_name_snake }}"
    verbose_name = "{{ cookiecutter.project_name }}"
