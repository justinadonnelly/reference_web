# extract references
# extract information from references (i.e. authors, titles, etc)
# output extracted info as json

import re

def extract_info(reference):
	return reference

def extract_authors(reference):
	regex = re.compile('([A-Z][a-z]*[,]\s([A-Z][.])+)')
	authors = regex.match(reference)
	return authors

def extract_titles(reference):
	return reference

def extract_citation_index(reference):
	return reference

def extract_publication(reference):
	return reference

...