.. _documentation:

Documentation
=============

How does it work?
*****************

The WikiRevParser parses Wikipedia revision histories and outputs clean, accessible data for each timestamp in the revision history. 

The parser takes a language code and a page title as input and relies on our re-worked version of the Wikipedia API wrapper for extracting the revision history of the page. 
After the revision history of the page has been extracted, the parser extracts cleans and pre-processes the revision history of each timestamp. This process is essential for working with Wikipedia revision histories, as the ourput of the API call for each revision is a noisy and un-organised string. 
The parser extracts salient information from the string, such as images, section titles, references, editor IDs and content, and cleans each     
You can use this library to access the development of references of a page, analyse the content or images over time, compare the tables of content across languages, create editor networks, and much more.

How to install?
***************

Installing the WikiRevParser is easy with ``pip3``, but you'll also need to clone our forked version of the `Wikipedia API wrapper <https://github.com/ajoer/Wikipedia>`_ from Github, since the WikiRevParser relies on that for extracting revision histories. 

::

	pip3 install wikirevparser
	git clone git@github.com:ajoer/Wikipedia.git


Read more on the `PyPI <https://pypi.org/project/wikirevparser/>`_ page of the library. 
You can also find more information about the Wikipedia API wrapper on our version's `Github page <https://github.com/ajoer/Wikipedia>`_, or on the `readthedocs page <https://wikipedia.readthedocs.io/en/latest/>`_ of the original (shoutout to @goldsmith).

You can of course also clone the `Github repository <https://github.com/ajoer/WikiRevParser>`_, but then you'll also need to install the requirements(see which in the `requirements <https://github.com/ajoer/WikiRevParser/requirements.txt>`_ file):

::

	git clone git@github.com:ajoer/WikiRevParser.git
	cd WikiRevParser
	pip3 install -r requirements.txt

How to use?
***********



Content
*******

* :ref:`index`
* :ref:`quickstart`
* :ref:`search`



