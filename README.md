# WikiRevParser

**WikiRevParser** is a Python library that parses Wikipedia revision histories and allows you to analyse the development of pages on Wikipedia across all language versions.

The library extracts and parses Wikipedia revision histories from a language-page title pair and outputs clean, accessible data per timestamp in the revision history. 
You can use this library to access the development of references of a page, analyse the content or images over time, compare the tables of content across languages, create editor networks, and much more.

## Example

To get the revision history for the page on [Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie) on the English Wikipedia, run:

	>>> from wikirevparser import wikirevparser
	>>> parser_instance = wikirevparser.ProcessRevisions("en", "Marie Curie") 
	>>> parser_instance.wikipedia_page()
	>>> data = parser_instance.parse_revisions()

And you can access information like these:

**about links:**

	>>> edits = list(data.items())
	>>> first_links = edits[-1][1]["links"]
	>>> latest_links = edits[0][1]["links"]
	>>> print("Number of links in the first edit: %d." % len(first_links))
	Number of links in the first edit: 1. 
	>>> print("A link in the first edit: %s." % first_links[0])
	A link in the first edit: pierre and marie curie. 
	>>> print("Number of links in the latest edit: %d." % len(latest_links))
	Number of links in the latest edit: 320. 
	>>> print("A link in the latest edit: %s." % latest_links[0])
	A link in the first edit: congress poland.
	
**about editors:**

	>>> from collections import Counter
	>>> editors = Counter()
	>>> for timestamp in data:
	>>>	  editors[data[timestamp]["user"]] += 1
	>>> most_frequent = editors.most_common(1)[0]
	>>> editor, edits = most_frequent[0], most_frequent[1]
 	>>> print("%s has edited the page the most, all of %d times (%d percent)!" % (editor, edits, (edits/len(data)*100)))
	Nihil novi has edited the page the most, all of 619 times (13 percent)!

You could also investigate the use of images, the changes in tables of content, analyse differences across different language versions, and much, much more. 

## Installation

To install WikiRevParser, you can clone the repository on [GitHub](https://github.com/ajoer/WikiRevParser) or simply run:

	>>> pip3 install wikirevparser


## Requirements

The WikiRevParser requires Python 3+.

You'll also need a few common Python libraries as well as our [Wikipedia API wrapper](https://github.com/ajoer/Wikipedia) (forked from [Wikipedia](https://github.com/goldsmith/Wikipedia) by @goldsmith), which extracts and returns the entire revision history of a Wikipedia page. 

Run the following to install all requirements needed:

	>>> python3 install -r requirements.txt
	>>> git clone git@github.com:ajoer/Wikipedia.git

The first command installs all requirements specified in the [requirements.txt](https://github.com/ajoer/WikiRevParser/requirements.txt) file, and the second command clones our version of the [Wikipedia API wrapper](https://github.com/ajoer/Wikipedia) needed for revision history extraction.

## Documentation

Read the docs at [readthedocs.io](https://wikirevparser.readthedocs.io/en/latest/)

## License

This work is MIT licensed. See the [LICENSE file](https://github.com/ajoer/WikiRevParser/LICENSE) for full details.

## Credits

- @goldsmith for the Python Wikipedia API wrapper [Wikipedia](https://github.com/goldsmith/Wikipedia).
- The [Wikimedia Foundation](http://wikimediafoundation.org/wiki/Home) and all Wikipedians for creating and maintaining the data.
- This work has received funding from the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No. 812997.

