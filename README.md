# WikiRevParser

**WikiRevParser** is a Python library that parses Wikipedia revision histories and allows you to analyse the development of pages on Wikipedia across all language versions.

The library extracts and parses Wikipedia revision histories from a language-page title pair and outputs clean, accessible data per timestamp in the revision history. 
You can use this library to access the development of references of a page, analyse the content or images over time, compare the tables of content across languages, create editor networks, and much more.
	
## Example

To get the revision history for the page on [Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie) on the English Wikipedia, run:

	>>> from wikirevparser import wikirevparser
	>>> parser_instance = wikirevparser.ProcessRevisions("en", "Marie Curie") 
	>>> data = parser_instance.wikipedia_page().parse_revisions()

And you can access information like these:

**About links:**

	>>> edits = list(data.items())
	>>> first_links = edits[-1][1]["links"]
	>>> latest_links = edits[0][1]["links"]
	>>> print("The only link in the first version was '%s'. \nThere were %d links in the latest version, e.g. '%s'." % (first_links[0], len(latest_links), latest_links[0]))
	
	The only link in the first version was 'pierre and marie curie'.
	There were 320 links in the latest version, e.g. 'congress poland'.
	
**About editors:**

	>>> from collections import Counter
	>>> editors = Counter()
	>>> for timestamp in data:
	>>>	  editors[data[timestamp]["user"]] += 1
	>>> most_frequent = editors.most_common(1)[0]
 	>>> print("%s has edited the page the most, all of %d times (%d percent)!" % (most_frequent[0], most_frequent[1], (most_frequent[1]/len(data)*100)))
	
	Nihil novi has edited the page the most, all of 619 times (13 percent)!

You could also investigate the use of images, the changes in tables of content, analyse differences across different language versions, and much, much more. 

## Installation

To install WikiRevParser, run:

	$ pip3 install wikirevparser
	
You can also clone the [Github repository](https://github.com/ajoer/WikiRevParser):

	$ git clone git@github.com:ajoer/WikiRevParser.git

## Requirements

The WikiRevParser requires Python 3+.

You'll need a version of our [Wikipedia API wrapper](https://github.com/ajoer/Wikipedia) (forked from [Wikipedia](https://github.com/goldsmith/Wikipedia) by @goldsmith), which extracts and returns the entire revision history of a Wikipedia page: 

	$ git clone git@github.com:ajoer/Wikipedia.git

If you used ``git`` rather than ``pip3``, you'll need to run the following as well to install the necessary dependencies (see which in the [requirements](https://github.com/ajoer/WikiRevParser/requirements.txt) file):

	$ cd WikiRevParser
	$ pip3 install -r requirements.txt

## Documentation

Read the docs at [readthedocs.io](https://wikirevparser.readthedocs.io/en/latest/)

## License

This work is MIT licensed. See the [LICENSE file](https://github.com/ajoer/WikiRevParser/LICENSE) for full details.

## Credits

- @goldsmith for the Python Wikipedia API wrapper [Wikipedia](https://github.com/goldsmith/Wikipedia).
- The [Wikimedia Foundation](http://wikimediafoundation.org/wiki/Home) and all Wikipedians for creating and maintaining the data.
- This work has received funding from the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No. 812997.

