import os
import sys

from setuptools import setup, find_packages

from znbskeleton import get_version

setup(
    name='django-zinibu-skeleton',
    version=get_version().replace(' ', '-'),
    description='A skeleton Django application',
    author='Alexis Bellido',
    author_email='a@zinibu.com',
    url='https://github.com/alexisbellido/django-zinibu-skeleton',
    zip_safe=False,
)
