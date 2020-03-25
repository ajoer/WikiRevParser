.. _documentation:

Documentation
=============

What is it?
***********

**WikiRevParser** is a Python library that parses Wikipedia revision histories. It allows you to analyse the development of pages on Wikipedia over time and across language versions.

Each Wikipedia page has a revision history with a snapshot of the page at each revision point. 
This data is a great resource for conducting temporal and/or cross-lingual analysis, but the format of the revision histories at extraction are unstructured and noisy, which complicates any analysis. 
The WikiRevParser solves this issue by extracting the important aspects of the unstructured data from each revision and neatly organizing these in an easy-to-use JSON format. 

The output of the WikiRevParser is a dictionary where each key is a timepoint and each value is a dictionary of the following datatypes: 

* image captions: []
* categories: []
* content: str
* images: []
* links: []
* sections: [[], [], []]
* reference types: Counter()
* reference top level domains: Counter()
* reference urls: []
* user: str

The WikiRevParser works for all 300+ Wikipedia language versions independently of markup style, alphabet and size!

You can use this library to access the development of references of a page, analyse the content or images over time, compare the tables of content across languages, create editor networks, and much more. 
See :ref:`examples` for ideas!

How does it work?
*****************

The WikiRevParser parses Wikipedia revision histories and outputs clean, accessible data for each timestamp in the revision history. 

The parser takes a language code and a page title as input and relies on our re-worked version of the `Wikipedia API wrapper <https://github.com/ajoer/Wikipedia>`_ for extracting the revision history of the page. 
After the revision history of the page has been extracted, the parser extracts cleans and pre-processes the revision history of each timestamp. This process is essential for working with Wikipedia revision histories, as the output of the API call is a noisy and unstructured string for each revision. 
For each timestamp in the revision history, the parser extracts the salient information from the unstructured string, such as images, references, and editor IDs (see all elements above), and cleans the content from tables and markup.
The output is clean, easy to use structured data in a JSON format. 

How to install?
***************

Installing the WikiRevParser is easy with ``pip3``, but you'll also need to clone our forked version of the `Wikipedia API wrapper <https://github.com/ajoer/Wikipedia>`_ from Github, since the WikiRevParser relies on that for extracting revision histories. 

::

	pip3 install wikirevparser
	git clone git@github.com:ajoer/Wikipedia.git


Read more on the `PyPI <https://pypi.org/project/wikirevparser/>`_ page of the library. 
You can also find more information about the Wikipedia API wrapper on our version's `Github page <https://github.com/ajoer/Wikipedia>`_, or on the `readthedocs page <https://wikipedia.readthedocs.io/en/latest/>`_ of the original (shoutout to @goldsmith).

You can of course also clone the `Github repository <https://github.com/ajoer/WikiRevParser>`_. 
In this case, you'll also need to install the requirements (see which in the `requirements <https://github.com/ajoer/WikiRevParser/requirements.txt>`_ file):

::

	git clone git@github.com:ajoer/WikiRevParser.git
	cd WikiRevParser
	pip3 install -r requirements.txt

How to use?
***********

The WikiRevParser is easy to use for getting clean, structured Wikipedia revision histories.

To get the revision history for the page on `Marie Curie <https://en.wikipedia.org/wiki/Marie_Curie>`_ on the English Wikipedia, run:

	>>> from wikirevparser import wikirevparser
	>>> parser_instance = wikirevparser.ProcessRevisions("en", "Marie Curie") 
	>>> parser_instance.wikipedia_page()
	>>> data = parser_instance.parse_revisions()

Now you have the revisions of the `Marie Curie <https://en.wikipedia.org/wiki/Marie_Curie>`_ page in a structured dictionary format, and you can start exploring the data.

Let's look at the use of **links**.
I want to know whether the links on the page are the same now as when the page was first made?

	>>> edits = list(data.items())
	>>> first_links = edits[-1][1]["links"]
	>>> latest_links = edits[0][1]["links"]
	>>> present_now = first_links[0] in latest_links 
	>>> print("The only link in the first version was '%s'. \nThat link is still present in the current version: %s." % (first_links[0], present_now))
	
	The only link in the first version was 'pierre and marie curie'.
	That link is still present in the current version: False.
	
Okay, but what are then the most frequent links on the page now?

	>>> from collections import Counter
	>>> links = Counter()
	>>> for l in latest_links:
	...	links[l] += 1
	>> print(links)
	Counter({'polonium': 5, 'radium': 5, 'university of paris': 5, 'russian empire': 4, 'gabriel lippmann': 4, 'nobel prize in physics': 4, 'nobel prize in chemistry': 4, ... })

Using the revision history parsed by the WikiRevParser, you could also answer questions like:
* When was the 'pierre and marie curie' link deleted?
* Who made that edit?
* Did that editor also edit the `Afrikaans page <https://af.wikipedia.org/wiki/Marie_Curie>`_ on Marie Curie?
* What are the most referenced sources on the page?
* Which references are used on both the English page and the `Arabic one <https://ar.wikipedia.org/wiki/%D9%85%D8%A7%D8%B1%D9%8A_%D9%83%D9%88%D8%B1%D9%8A>`_ pages?
* How many Wikipedians have edited the English page? And the `Dutch page <https://nl.wikipedia.org/wiki/Marie_Curie>`_?
* Do all language versions use the same image of Marie Curie as the top image?
* Where are the Wikipedians located?
* How frequently is the page edited? 
* Has the English page developed consistently or did editing intensify at one point?
* How does the editing pattern of the English page match that of the `Korean page <https://ko.wikipedia.org/wiki/%EB%A7%88%EB%A6%AC_%ED%80%B4%EB%A6%AC>`_?
* ... and many other questions

See :ref:`examples` for more inspiration and functionalities, and go to `FAQ or file a bug <https://github.com/ajoer/WikiRevParser/issues>`_ if you run into issues!

Index
*****

* :ref:`home`
* :ref:`quickstart`
* :ref:`examples`
* :ref:`search`



