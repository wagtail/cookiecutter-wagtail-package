default_app_config = "{{ cookiecutter.__project_name_snake }}.apps.{{ cookiecutter.__project_name_camel }}AppConfig"


VERSION = (0, 1, 0)
__version__ = ".".join(map(str, VERSION))
