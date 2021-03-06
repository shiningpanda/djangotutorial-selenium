# -*- coding: utf-8 -*-
try: import setuptools
except ImportError:
    import distribute_setup
    distribute_setup.use_setuptools()

from setuptools import setup, find_packages

setup(
    name = 'DjangoTutorial',
    version = '1.3.1',
    description = 'Django tutorial project.',
    url = 'https://docs.djangoproject.com/en/1.3/intro/tutorial01/',
    packages = find_packages(),
    include_package_data = True,
    zip_safe = False,
    install_requires = [
        'Django >= 1.3.1',
    ],
)
