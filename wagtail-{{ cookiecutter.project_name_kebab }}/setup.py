#!/usr/bin/env python

from os import path

from setuptools import find_packages, setup
from wagtail_{{cookiecutter.project_name_snake}} import __version__


this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, "README.md"), encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="wagtail-{{ cookiecutter.project_name_kebab }}",
    version=__version__,
    description="{{ cookiecutter.project_short_description }}",
    long_description=long_description,
    long_description_content_type='text/markdown',
    author="{{ cookiecutter.full_name }}",
    author_email="{{ cookiecutter.email }}",
    url="",
    packages=find_packages(),
    include_package_data=True,
    license="BSD",
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Framework :: Django",
        "Framework :: Django :: 3.2",
        "Framework :: Django :: 4.0",
        "Framework :: Django :: 4.1",
        "Framework :: Wagtail",
        "Framework :: Wagtail :: 2",
        "Framework :: Wagtail :: 4",
    ],
    install_requires=["Django>=3.0,<4.2", "Wagtail>=2.15,<5.0"],
    extras_require={
        "testing": ["dj-database-url==0.5.0", "freezegun==0.3.15"],
    },
    zip_safe=False,
)
