WikiRevParser
=========

**WikiRevParser** is a Python library that extracts and parses the revision histories of Wikipedia pages.

The library extracts and parses Wikipedia revision histories from a language-page title pair and outputs clean, accessible data per timestamp in the revision history. 
You can use this library to access the development of references of a page, analyze the content or images over time, compare the tables of content across languages, create editor networks, and much more.

The WikiRevParser relies on our forked and modified `version <https://github.com/ajoer/Wikipedia>`__ of the Python `Wikipedia <https://github.com/goldsmith/Wikipedia>`__ library, which in turn wraps the `MediaWiki API <https://www.mediawiki.org/wiki/API>`__ for quick and easy access to Wikipedia data.
Our modified `version <https://github.com/ajoer/Wikipedia>`__ of the Wikipedia library extracts and returns the entire revision history of a page.

License
-------

This work is MIT licensed. See the `LICENSE file <https://github.com/ajoer/WikiRevParser/LICENSE>`__ for full details.

Credits
-------

-  @goldsmith for the Python Wikipedia API wrapper `Wikipedia <https://github.com/goldsmith/Wikipedia>`__.
-  The `Wikimedia Foundation <http://wikimediafoundation.org/wiki/Home>`__ and all Wikipedians for creating and maintaining the data.
- This work has received funding from the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No. 812997.
