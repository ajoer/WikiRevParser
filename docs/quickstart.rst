.. _quickstart:

Quickstart
==========

Installing and using the WikiRevParser is easy! Just follow the simple steps below.
If you want more information about the library, see :ref:`documentation`.

Install WikiRevParser

::

	$ pip3 install wikirevparser

Let's try it out and get the changes in page size for the article on Marie Curie over time. 

Our task plan:
1. extract the data
2. parse the data
3. get the page sizes from the parsed data

**Extracting the data**

For extracting the data, we rely on our forked version of the `Wikipedia API wrapper <https://github.com/ajoer/Wikipedia>`_. 
This takes a language code and a Wikipedia page title as input:

::

	>>> from wikirevparser import wikirevparser
	>>> parser_instance = wikirevparser.ProcessRevisions("en", "Marie Curie") 
	>>> data = parser_instance.wikipedia_page().parse_revisions()

See see :ref:`documentation` for more information on the functionalities of the library! 
And see FAQ or file a bug if you run into issues `here <https://github.com/ajoer/WikiRevParser/issues>`_!

Indices and tables
==================

* :ref:`quickstart`
* :ref:`documentation`
* :ref:`search`

