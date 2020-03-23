# -*- coding: utf-8 -*-
import setuptools

with open("README.md", "r") as readme_file:
    long_description = readme_file.read()

with open("requirements.txt", "r") as req_file:
    requirements = req_file.readlines()

install_reqs = [l.strip() for l in requirements if l.strip() != ""]
print(install_reqs)

setuptools.setup(
    name="wikirevparser",
    version="0.0.3",
    author="Anna Jørgensen",
    author_email="anka.jorgensen@gmail.com",
    description="Wikipedia revision history parser for Python",
    url="https://github.com/ajoer/WikiRevisionParser",
    license = "MIT",
    keywords = "python wikipedia API",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires = install_reqs,
    packages=['wikirevparser'], # setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.6',
)
