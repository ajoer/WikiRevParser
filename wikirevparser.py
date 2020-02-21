#!/usr/bin/python3
""" 
	Parses elements of the edit histories of Wikipedia language versions.
"""
import nltk
import re
import string

from collections import Counter, defaultdict, OrderedDict

from urllib.request import urlopen
from Wikipedia.wikipedia import wikipedia
from Wikipedia.wikipedia import exceptions

class ProcessRevisions:

	def __init__(self, language, event):

		self.language = language
		self.event = event
		
	def wikipedia_page(self):
		''' Get wikipedia revision history for an event in a given language and yield output'''
		wikipedia.set_lang(self.language)

		try:
			print("\t* Getting data *")
			event_pagetitle = '_'.join(self.event.split())
			page = wikipedia.WikipediaPage(event_pagetitle)
			self.page = page
			self.revisions = page.revisions
			return page

		except exceptions.PageError:
			print("\tThere is no '%s' page in the '%s' language version of Wikipedia, try another one" % (self.event, self.language))
			return None

	def replace_link(self, input_string, link, text):
		# Replace link with text
		output_string = input_string.replace("[[%s]]" % link, text)
		output_string = output_string.replace("[[%s|%s]]" % (link, text), text)
		
		return output_string

	def get_links(self, input_string):

		links = []
		texts = []

		double_square_bracket, content_subbed = self.get_occurrences(r"\[\[(.*?)\]\]", input_string)
		for element in double_square_bracket:
			elements = element.split("|")

			link = elements[0]

			if len(elements) == 2:
				text = elements[1]
			else: 
				text = link
			links.append(link)
			texts.append(text)

		return links, texts

	def get_occurrences(self, regex, content):
		# Reg ex to get all references/citations in an edit history.
		# Deletes the occurences from the content

		exp = re.compile(regex, re.IGNORECASE)
		occurrences = exp.findall(content)
		content = re.sub(exp, '', content)

		return occurrences, content

	def get_reference_types(self, input_list):
		# Extract the reference type from a reference/citation block in an edit history, 
		# e.g. "book", "thesis", "news" etc.
		types = Counter()

		for element in input_list:
			try:
				reference_type = re.search("{{[c|C]ite (.*?)( |\|)", element, re.IGNORECASE).group(1)
				if len(reference_type) <= 1: continue
				types[reference_type] += 1

			except AttributeError:
				types["_nill_"] += 1

		return types

	def get_tlds(self, url_list):
		# Extract the tlds from each url in a reference/citation block in an edit history.

		tlds = Counter()

		for url in url_list:
			tld = url.split("/")[0].split(".")[-1]
			tlds[tld] += 1

		return tlds 

	def get_urls(self, input_list):

		# Todo: check whether this is the best way.

		urls = []
		http_regex = "http[s]*:\/\/([^ ]*)"

		for element in input_list:
			# they differ in endings:
			url = re.search(http_regex + r"( |}})", element, re.IGNORECASE)
			if url:
				url = url.group(1).split("|")[0]
			else:
				url = re.search(http_regex, element, re.IGNORECASE)
				if not url: continue
				url = url.group(1).split("|")[0]

			#if url is None: continue
			if "www" in url:
				url = url[4:]
			urls.append(url)
		return urls

	def parse_images(self):
		''' Extract and parse images.'''
		images = []
		captions = []
		links_from_captions = []
		extensions = [".jpg", ".svg", ".png", ".JPG", ".SVG", ".PNG"]

		for line in self.content.split("\n"):
			for extension in extensions:

				if not extension in line: continue

				# Images
				occurrence = re.search(r"(:|=)([^(:|=)].*)(.jpg|.svg|.png)", line, re.IGNORECASE)
				if not occurrence: 
					# images can be begin line, no markup
					occurrence = re.search(r"(^)([^(:|=)].*)(.jpg|.svg|.png)", line, re.IGNORECASE)
				try:
					image_title, image_extension = occurrence.group(2,3)
				except AttributeError:
					print("\tThe image in this line has not been extracted:\t", line)
					continue
				if ":" in image_title:
					image_title = image_title.split(":")[-1]

				image_title = '_'.join([x for x in image_title.split()])
				image_link = "https://commons.wikimedia.org/wiki/File:" + image_title + image_extension
				images.append(image_link)
				self.content = self.content.replace(line, "")

				# Captions
				# Some languages (e.g. EN) make use of this structure for captions: "alt=British soldiers....". They can have links in the caption.
				if "|alt=" in line:

					elements = line.split("|alt=")[-1].split("|")[1:]
					caption = '|'.join(elements)[:-2]
					self.content = self.content.replace(line, caption)
					
				# Other languages (e.g. NL) do not...
				else:
					caption = re.search(r"thumb\|(.*)\]\]", line, re.IGNORECASE)
					if not caption: continue 
					caption = caption.group(1)
					if "px" in caption or caption.startswith("{{legend"): continue

				# Get links and remove from caption
				links, texts = self.get_links(caption)

				for link, text in zip(links, texts):
					caption = self.replace_link(caption, link, text)
					self.content = self.replace_link(self.content, link, text)
					
					links_from_captions.append(link.lower())

				caption = caption.split("|")
				if len(caption) > 1: caption = caption[1]
				if len(caption) < 1: continue
				caption = self.proper_formatting(caption, punct=False)
				captions.append(caption)

		return images, captions, links_from_captions

	def parse_links_categories(self):
		# Parse links and categories from an edit history. 
		# Must be run after parse_images() because images have the same markup, and will otherwise feature as links.
		
		categories = []
		links = []
		possible_links, texts = self.get_links(self.content)

		for link, text in zip(possible_links,texts):

			if ":" in link:
				elements = link.split(":")
				if len(elements) == 2:
					l, category = elements
				elif len(elements) == 3:
					l, wiki, category = elements
				else:
					print("\tThere is an unexpected number of elements in this link:\t", link)
					continue

				# language links
				if len(l) != 2 and not l.islower():
					# categories
					categories.append(category)

				self.content = self.replace_link(self.content, link, "")

			else:
				links.append(link.lower())
				self.content = self.replace_link(self.content, link, text)

		return links, categories

	def parse_references(self):
		''' Extract and analyze references and their origin (tld) over time.'''
		reference_template_types = Counter() # some references have "type" markup, e.g. "book", "thesis", "news" etc.

		regex_letters = "\dA-Za-zğäåæáéëíıïóøöúü"
		regex_symbols = "\"'(){}[\]&=«»:.,?_~–\-/| "

		references, self.content = self.get_occurrences(r"<ref(.*?)<\/ref>", self.content) 
		citations, self.content = self.get_occurrences(r"{{[c|C]ite [" + regex_letters + regex_symbols + ">]+}}", self.content)
		
		urls = self.get_urls(references + citations + [x for x in self.content.split()])
		tlds_origin = self.get_tlds(urls)
		
		reference_types = self.get_reference_types(references + citations)
		reference_template_types += reference_types
		
		return urls, tlds_origin, reference_template_types

	def parse_sections(self):
		# Parse sections from edit history

		#Todo: consider another way to parse section titles with better depth.
		#TODO: strip '' from sections if BOLD

		sections = []
		header1s, self.content = self.get_occurrences(r"[^=]={2}([^=].*?)={2}", self.content)
		header2s, self.content = self.get_occurrences(r"[^=]={3}([^=].*?)={3}", self.content)
		header3s, self.content = self.get_occurrences(r"[^=]={4}([^=].*?)={4}", self.content)
		sections.append([self.proper_formatting(x.strip(), punct=False) for x in header1s])
		sections.append([self.proper_formatting(x.strip("=").strip(), punct=False) for x in header2s])
		sections.append([self.proper_formatting(x.strip("==").strip(), punct=False) for x in header3s])

		return sections

	def proper_formatting(self, input_string, punct=True):
		# Add end punct to lines, strip quotation marks, and tokenize
		if punct:
			if input_string[-1] not in string.punctuation: 
				input_string += "."

		input_string = "".join([x for x in input_string if x != "'"])
		output_string = ' '.join(nltk.word_tokenize(input_string))
		
		return output_string

	def parse_text(self):
		# Clean remaining content for tables, noise and image markup. Also cleans italics markup.

		clean_content = []
		italics_markup, self.content = self.get_occurrences(r"\'{2,}", self.content)

		for line in self.content.split("\n"):

			if len(line) == 0: continue
			if line[0] in string.punctuation or "px" in line: continue

			# Add end punct to lines
			clean_content.append(self.proper_formatting(line))

		self.content = ' '.join([w for w in clean_content])

	def parse_revisions(self):
		data = OrderedDict()

		if self.revisions == None:return None

		for n, revision in enumerate(self.revisions):
			parsed_data = defaultdict()
			timestamp = revision["timestamp"]

			if "user" not in revision.keys(): continue 
			user = revision["user"]
			
			if "*" not in revision["slots"]["main"].keys(): continue
			self.content = revision["slots"]["main"]["*"]
			
			urls, tlds_origin, reference_template_types = self.parse_references()
			images, captions, links_from_captions = self.parse_images()
			links, categories = self.parse_links_categories()
			sections = self.parse_sections()
			self.parse_text()

			parsed_data["captions"] = captions
			parsed_data["categories"] = categories
			parsed_data["content"] = self.content
			parsed_data["images"] = images
			parsed_data["links"] = links + links_from_captions
			parsed_data["reference_template_types"] = reference_template_types
			parsed_data["sections"] = sections
			parsed_data["tlds_origin"] = tlds_origin
			parsed_data["urls"] = urls
			parsed_data["user"] = user

			data[timestamp] = parsed_data
		return data