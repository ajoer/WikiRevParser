# WikiRevParser

**WikiRevParser** is a Python library that parses Wikipedia revision histories and allows you to analyse the development of pages on Wikipedia across all language versions.

The library extracts and parses Wikipedia revision histories from a language-page title pair and outputs clean, accessible data per timestamp in the revision history. 
You can use this library to access the development of references of a page, analyze the content or images over time, compare the tables of content across languages, create editor networks, and much more.

The WikiRevParser relies on our forked and modified [version](https://github.com/ajoer/Wikipedia) of the Python [Wikipedia](https://github.com/goldsmith/Wikipedia) library, which in turn wraps the [MediaWiki API](https://www.mediawiki.org/wiki/API) for quick and easy access to Wikipedia data.
Our modified [version](https://github.com/ajoer/Wikipedia) of the Wikipedia library extracts and returns the entire revision history of a page.

## Installation

To install WikiRevParser, you can clone the repository on [GitHub](https://github.com/ajoer/WikiRevParser) or simply run:

	>>> pip install wikirevparser

The WikiRevParser is compatible with Python 3.4+, compatibility with earlier versions of Python has not been tested yet.


## Example

To get the revision history for the page on [knitting](https://en.wikipedia.org/wiki/Knitting) on the English Wikipedia, run:

	>>> from WikiRevParser.wikirevparser import wikirevparser
	>>> parser_instance = wikirevparser.ProcessRevisions("en", "Knitting") 
	>>> parser_instance.wikipedia_page()
	>>> data = parser_instance.parse_revisions()

And you can access information like these:

When and by whom was the first and last edit made?

	>>> edits = list(data.items())
	>>> first_timepoint = edits[-1][0]
	>>> first_editor = edits[-1][1]["user"]
	>>> last_timepoint = edits[0][0]
	>>> last_editor = edits[0][1]["user"]
	>>> print("%s first edited the page at %s, \n and it was last edited by %s at %s." % ( first_editor, first_timepoint, last_editor, last_timepoint))
	# Janet Davis first edited the page at 2001-04-07T02:39:27Z, 
	# and it was last edited by JavaHurricane at 2020-03-18T12:41:39Z.

Who has edited the page the most?

	>>> from collections import Counter
	>>> users = Counter()
	>>> for timestamp in data:
	>>>	  users[data[timestamp]["user"]] += 1
	>>> print("%s has edited the page the most, all of %s times!" % (most_editing, number_edits))
	# WillowW has edited the page the most, all of 93 times!

You could also investigate the use of images, the changes in tables of content, analyse differences between different language versions, and more. 

## Documentation

Read the docs at (https://wikirevparser.readthedocs.io/en/latest/)

## License

This work is MIT licensed. See the [LICENSE file](https://github.com/ajoer/WikiRevParser/LICENSE) for full details.

## Credits

- @goldsmith for the Python Wikipedia API wrapper [Wikipedia](https://github.com/goldsmith/Wikipedia).
- The [Wikimedia Foundation](http://wikimediafoundation.org/wiki/Home) and all Wikipedians for creating and maintaining the data.
- This work has received funding from the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No. 812997.

