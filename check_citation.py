#!/usr/bin/env python

from pybtex.database.input import bibtex
import sys
from cite_utils import common_authors

paper= bibtex.Parser().parse_file(sys.argv[1])
citation= bibtex.Parser().parse_file(sys.argv[2])


this_paper=paper.entries.items().__iter__().__next__()[1]
this_id=paper.entries.items().__iter__().__next__()[0]
authors=this_paper.persons['author']



cnt_cite_3rd=0

print("Items with common authors:----------vvv\n")
for k,v in citation.entries.items():
    cit_authors=v.persons['author']
    ca=common_authors(authors, cit_authors)
    if ca:
        print(f"{k} : {ca}")
    else:
        cnt_cite_3rd+=1
print("\nEnd of items with common authors----^^^\n")
print("Summary\n")
print(f"id: {this_id}")
print(f"Title: {this_paper.fields['title']}")
print(f"Number of all cit: {len(citation.entries)}")
print(f"Number of 3rd cit: {cnt_cite_3rd}")
