# -*- coding: utf-8 -*-

# Learn more: https://github.com/sneub/langsense/setup.py

from setuptools import setup, find_packages


with open('README.rst') as f:
    readme = f.read()

with open('LICENSE') as f:
    license = f.read()

setup(
    name='langsense',
    version='0.1.0',
    description='Language detection library',
    long_description=readme,
    author='Shane Neubauer',
    author_email='shanen@gmail.com',
    url='https://github.com/sneub/langsense',
    license=license,
    packages=find_packages(exclude=('tests', 'docs'))
)

