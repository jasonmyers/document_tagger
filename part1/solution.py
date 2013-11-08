import re
import sys
from pg_sample_texts import DIV_COMM, MAG_CART

documents = [DIV_COMM, MAG_CART]

# Assign a dictionary of each keyword and corresponding regex pattern

searches = {}
for kw in sys.argv[1:]:
    searches[kw] = re.compile(r'(?:\*{3} START OF.*$)|' + r'\b' + kw + r'\b', re.IGNORECASE)

# Assign regex patterns to find the titles, even if they extend across
# multiple lines.

title_search = re.compile(r'(?:title:\s*)(?P<title>(.*)(\n +.*)+)',
                            re.IGNORECASE|re.MULTILINE)

author_search = re.compile(r'(author:)(?P<author>.*)', re.IGNORECASE)
translator_search = re.compile(r'(translator:)(?P<translator>.*)', re.IGNORECASE)
illustrator_search = re.compile(r'(illustrator:)(?P<illustrator>.*)', re.IGNORECASE)
 
# Loop through each document and search for title, author, translator
# and illustrator.

for i, doc in enumerate(documents):
    title = re.search(title_search, doc).group('title')
    author = re.search(author_search, doc)
    translator = re.search(translator_search, doc)
    illustrator = re.search(illustrator_search, doc)
    if author: 
        author = author.group('author')
    if translator:
        translator = translator.group('translator')
    if illustrator:
        illustrator = illustrator.group('illustrator')
    print "***" * 25
    print "The title of the text is {}".format(title)
    if author:
        print "The author is {}".format(author)
    if translator:
        print "The translator is {}".format(translator)
    if illustrator:
        print "The illustrator is {}".format(illustrator)

# Loop through this document and search for the keywords supplyed by argv

    print "Here's the counts for the keywords you searched for:"
    for search in searches:
        print "\"{0}\": {1}".format(search, len(re.findall(searches[search], doc)))
    print "\n"