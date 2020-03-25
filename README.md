# WikiRevParser

**WikiRevParser** is a Python library that parses Wikipedia revision histories. It allows you to analyse the development of pages on Wikipedia over time and across language versions.

The library takes a language code and Wikipedia page title as input, extracts the revision history with our [Wikipedia API wrapper](https://github.com/ajoer/Wikipedia), and parses the noisy, unstructured content into clean, accessible data for each timestamp in the revision history. 
You can use this library to access the development of references of a page, analyse the content or images over time, compare the tables of content across languages, create editor networks, and much more.

## Installation

To install WikiRevParser, run:

	$ pip3 install wikirevparser
	
## Requirements

The WikiRevParser requires Python 3+.

You'll need a version of our [Wikipedia API wrapper](https://github.com/ajoer/Wikipedia) (forked from [Wikipedia](https://github.com/goldsmith/Wikipedia) by @goldsmith), which extracts and returns the entire revision history of a Wikipedia page: 

	$ git clone git@github.com:ajoer/Wikipedia.git

## Example

To get the revision history for the page on [Marie Curie](https://en.wikipedia.org/wiki/Marie_Curie) on the English Wikipedia, run:

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
* What are the most referenced sources?
* How many Wikipedians edit the page?
* Where are the Wikipedians located?
* How frequently is the page edited? 
* Has the page developed consistently or did editing intensify at one point?
* and many other questions


## Documentation

Read the docs at [wikirevparser.readthedocs.io](https://wikirevparser.readthedocs.io/en/latest/) for more details and use case examples.

## License

This work is MIT licensed. See the [LICENSE file](https://github.com/ajoer/WikiRevParser/LICENSE) for full details.

## Credits

- @goldsmith for the Python Wikipedia API wrapper [Wikipedia](https://github.com/goldsmith/Wikipedia).
- The [Wikimedia Foundation](http://wikimediafoundation.org/wiki/Home) and all Wikipedians for creating and maintaining the data.
- This work has received funding from the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No. 812997.

