# -*- coding: utf-8 -*-
import setuptools

import codecs
import os
import re


def local_file(file):
  return codecs.open(
    os.path.join(os.path.dirname(__file__), file), 'r', 'utf-8'
  )

install_reqs = [
  line.strip()
  for line in local_file('requirements.txt').readlines()
  if line.strip() != ''
]


with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="WikiRevParser",
    version="0.0.1",
    author="Anna Jørgensen",
    author_email="anka.jorgensen@gmail.com",
    description="Wikipedia revision history parser for Python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ajoer/WikiRevisionParser",
    install_requires = install_reqs,
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
