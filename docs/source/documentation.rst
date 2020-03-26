.. _documentation:

Documentation
=============

What is it?
***********

**WikiRevParser** is a Python library that parses Wikipedia revision histories. It allows you to analyse the development of pages on Wikipedia over time and across language versions.

Each Wikipedia page has a revision history with a snapshot of the page at each revision point. 
This data is a great resource for conducting temporal and/or cross-lingual analysis, but the format of the revision histories at extraction are unstructured and noisy, which complicates any analysis. 

The WikiRevParser solves this issue by extracting the important aspects of the unstructured data from each revision and neatly organizing these in an easy-to-use JSON format. 

The WikiRevParser works for all 300+ Wikipedia language versions independently of markup style, alphabet and size.

You can use this library to access the development of references of a page, analyse the content or images over time, compare the tables of content across languages, create editor networks, and much more. 
See :ref:`examples` for use cases and ideas.

How does it work?
*****************

The WikiRevParser parses Wikipedia revision histories and outputs clean, accessible data for each timestamp in the revision history. 

The parser takes a language code and a page title as input and relies on our re-worked version of the `Wikipedia API wrapper <https://github.com/ajoer/Wikipedia>`_ for extracting the revision history of the page. 

After the revision history of the page has been extracted, the parser extracts cleans and pre-processes the revision history of each timestamp. 

This process is essential for working with Wikipedia revision histories, as the output of the API call is a noisy and unstructured string for each revision. 

For each timestamp in the revision history, the parser extracts the salient information from the unstructured string, such as images, references, and editor IDs (see all elements below).
Then the text content of the page is cleaned of tables and markup.

The output is clean, easy to use structured data in a JSON format. 

What does the output look like?
*******************************

The output of the WikiRevParser is a dictionary where each key is a timepoint and each value is a dictionary.

In the following, we use the data for a timepoint in the revision history of the English page about `Marie Curie <https://en.wikipedia.org/wiki/Marie_Curie>`_:

::
	>>> print(data[0])
	{
	'captions': ["Maria Skłodowskas birthplace on ulica Freta ...", ... ],
	'categories': ['Pierre et Marie Curie', 'Experimental physicists' ...],
	'content': "Maria Skłodowska-Curie ... was a physicist and chemist ...],
	'images': ['https://commons.wikimedia.org/wiki/File:Mariecurie.jpg', ...],
	'links': ['congress poland', 'sancellemoz', 'france', 'poland', ...],
	'reference_template_types': Counter({'book': 4, 'web': 1}), 
	'sections': [['Life', 'Prizes', 'Tribute', 'See also', ...], [], []],
	'urls': ['mlahanas.de/Physics/Bios/MarieCurie.html', ...],
	'user': '67.34.139.186'
	}

**Captions** (list) are captions that accompany images on the page. 
The captions are extracted and link markup is removed before the string is tokenized and end punctuation is added if missing.

**Categories** (list) are the categories assigned to the page at the bottom of the page. These are extracted and the "Categories:" prefix removed, regardless of language. The content is tokenized and end punctuation is added if missing.

**Content** (string) is the cleaned, markup-free text content of the page. Images, tables, section titles, references, and citations have been removed as well as any markup, e.g. for links. The content is tokenized and end punctuation is added if missing.

**Images** (list) are the links to commons.wikimedia.org, where the image used on the page is kept. The name of each image is extracted and appended with the proper link to commons, so the image can be directly extracted.

**Links** (list) are the internal Wikipedia links used on the page, i.e. all the blue words on the page (and in captions). They are extracted and lower-cased. 

**Sections** (list of lists) are the headers used on the page and reflected in the table of content in the UI. These are extracted and organized based on depth, max depth is 3. The content is tokenized and end punctuation is added if missing.

**Reference urls** (list) are the urls used in references or citations on the page. These appear at the bottom of the page in the UI but are embedded in the text in the extracted unstructured string. 
We perform two 

**Reference types** (list) some Wikipedians use reference templates for adding references. These templates are reference type specific (e.g. "book", "web", "news") and are extracted when available. 

**User** (string) is the IP address or user name of the user who made the revision. 


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

::

	>>> from wikirevparser import wikirevparser
	>>> parser_instance = wikirevparser.ProcessRevisions("en", "Marie Curie") 
	>>> parser_instance.wikipedia_page()
	>>> data = parser_instance.parse_revisions()

Now you have the revisions of the `Marie Curie <https://en.wikipedia.org/wiki/Marie_Curie>`_ page in a structured dictionary format, and you can start exploring the data.

Let's look at the use of **links**.
I want to know whether the links on the page are the same now as when the page was first made?

::

	>>> edits = list(data.items())
	>>> first_links = edits[-1][1]["links"]
	>>> latest_links = edits[0][1]["links"]
	>>> present_now = first_links[0] in latest_links 
	>>> print("""The only link in the first version was '%s'. 
	...	That link is still present in the current version: 
	...	%s.""" % (first_links[0], present_now))
	The only link in the first version was 'pierre and marie curie'.
	That link is still present in the current version: False.
	
Okay, but what are then the most frequent links on the page now?

::

	>>> from collections import Counter
	>>> links = Counter()
	>>> for l in latest_links:
	...	links[l] += 1
	>>> print(links)
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


