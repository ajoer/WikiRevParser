WikiRevParser
=========

Shield: [![CC BY-SA 4.0][cc-by-sa-shield]][cc-by-sa]


**WikiRevParser** is a Python library that parses Wikipedia revision histories and allows you to analyse the development of pages on Wikipedia across all langage versions.

The library extracts and parses Wikipedia revision histories from a language-page title pair and outputs clean, accessable data per timestamp in the revision history. 
You can use this library to access the development of references of a page, analyze the content or images over time, compare the tables of content across languages, create editor networks, and much more.

The WikiRevParser relies on our forked and modified `version <https://github.com/ajoer/Wikipedia>`__ of the Python `Wikipedia <https://github.com/goldsmith/Wikipedia>`__ library, which in turn wraps the `MediaWiki API <https://www.mediawiki.org/wiki/API>`__ for quick and easy access to Wikipedia data.
Our modified `version <https://github.com/ajoer/Wikipedia>`__ of the Wikipedia library extracts and returns the entire revision history of a page, which allows you further access in the revision history than the standard `Wikipedia <https://github.com/goldsmith/Wikipedia>`__ library.

Installation
------------

%To install Wikipedia, simply run:

%::

%  $ pip install wikipedia

%Wikipedia is compatible with Python 2.6+ (2.7+ to run unittest discover) and Python 3.3+.

Documentation
-------------

%Read the docs at https://wikipedia.readthedocs.org/en/latest/.

%-  `Quickstart <https://wikipedia.readthedocs.org/en/latest/quickstart.html>`__
%-  `Full API <https://wikipedia.readthedocs.org/en/latest/code.html>`__

%To run tests, clone the `repository on GitHub <https://github.com/goldsmith/Wikipedia>`__, then run:

%::

 % $ pip install -r requirements.txt
 % $ bash runtests  # will run tests for python and python3
 % $ python -m unittest discover tests/ '*test.py'  # manual style

%in the root project directory.

%To build the documentation yourself, after installing requirements.txt, run:

%::

%  $ pip install sphinx
 % $ cd docs/
 % $ make html

License
-------

This work is licensed under a [Creative Commons Attribution-ShareAlike 4.0
International License][cc-by-sa].

[![CC BY-SA 4.0][cc-by-sa-image]][cc-by-sa]

[cc-by-sa]: http://creativecommons.org/licenses/by-sa/4.0/
[cc-by-sa-image]: https://licensebuttons.net/l/by-sa/4.0/88x31.png
[cc-by-sa-shield]: https://img.shields.io/badge/License-CC%20BY--SA%204.0-lightgrey.svg

See the `LICENSE file <https://github.com/ajoer/WikiRevParser/LICENSE>`__ for
full details.

Credits
-------

-  @goldsmith for the Python Wikipidia API wrapper `Wikipedia <https://github.com/goldsmith/Wikipedia>`__.
-  The `Wikimedia Foundation <http://wikimediafoundation.org/wiki/Home>`__ and all Wikipedians for creating and maintaining the data.


