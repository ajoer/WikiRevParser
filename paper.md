---
title: 'WikiRevParser: a Python Library for Parsing Wikipedia Revision Histories'
tags:
  - Python
  - SSH
  - Wikipedia
  - Revision histories
  - Cross-lingual analysis
  - Temporal analysis
authors:
  - name: Anna Jørgensen
    orcid: 0000-0002-2568-4360
    affiliation: 1
affiliations:
 - name: Department of Media Studies, University of Amsterdam
   index: 1
date: 8 April 2020
bibliography: paper.bib

---

# Summary

Wikipedia, the largest online encyclopedia in the world, is available in 300+ languages.
Each language version is unique and offers a different presentation of concepts, people, events and places in the world than the other Wikipedias. 
When a page on one of the Wikipedia language versions is revised, the previous version of the page is stored and added to the chain of previous versions of the page. 

These previous versions of each page are retrievable using the [MediaWiki API](https://www.mediawiki.org/wiki/API:Main_page), and large amounts of scholarly work rely on the availability of these revision histories, e.g. [@Avieson2019] and [@Ford2015]. Furthermore, access to the revision histories of the articles on Wikipedia enables reproduction of experimental work based on Wikipedia while opening up for a large amount of unused data for NLP development and research.  

The output from the MediaWiki API, however, is noisy and contains markup.
Since each language version, and sometimes even each individual page, have been developed in isolation from other pages, they can each have their own markup standards and ways of representation information types. This complicates the use of the revision histories for social science and humanities research since a great deal of complicated data processing is required to get the data in a state ready for analysis.

WikiRevParser is a Python library that pre-processes and parses the noisy Wikipedia revision histories and outputs clean, structured data ready for research and data analysis.
The library is language and alphabet agnostic and can therefore be used for any page in any Wikipedia language version, ranging from the large, well-resourced languages such as English, French and German, to small, under-resourced languages such as Armenian, Bengali and Swahili. See the full list of supported languages [here](https://en.wikipedia.org/wiki/List_of_Wikipedias).

The WikiRevParser library is intended for extracting data for social science and humanities research with a temporal aspect, and it is the first tool to enable non-technical researchers to access the richness of the Wikipedia revision history, since the output is human-readable and in simple data formats. 
While not an exclusive list, we envision that the library will be beneficial for researchers investigating information organisation strategies, collaborative networks, cross-lingual comparative studies and conceptual analysis. A few studies using the WikiRevParser for social science and humanities research look at events and their development over time, as well as news practices on Wikipedia are underway.

The library can also be used for creating datasets for researching sentiment developments of a topic over time, text and image narratives in different languages, contributor networks, vandalism, or even to improve (the evaluation of) Machine Translation and dialogue systems by using re-writes of the same sentence. Again, research is currently being conducted that makes use of the WikiRevParser for dataset creation to improve entity recommendation systems and visualise the development of an event over time.

# Acknowledgements

This project has received funding from the European Union’s Horizon 2020 research and innovation programme under the Marie Skłodowska-Curie grant agreement No 812997.
