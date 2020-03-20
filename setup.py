# -*- coding: utf-8 -*-
from setuptools import setup
from os import path

this_directory = path.abspath(path.dirname(__file__))
with open(path.join(this_directory, 'README.md'), encoding='utf-8') as f:
    long_description = f.read()

setup(
    name="wikirevparser",
    version="0.0.1",
    author="Anna Jørgensen",
    author_email="anka.jorgensen@gmail.com",
    description="Wikipedia revision history parser for Python",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/ajoer/WikiRevisionParser",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)