#!/usr/bin/env python

from pybtex.database.input import bibtex
from pybtex.database import Person
import sys


paper= bibtex.Parser().parse_file(sys.argv[1])
citation= bibtex.Parser().parse_file(sys.argv[2])


def standardize1(n):
    return n.replace("-","").lower()

def standardize(p):
    return Person(standardize1(p.last_names[0]), standardize1(p.first_names[0]))

def common_authors(a1,a2):
    result=[]
    for x in a1:
        for y in a2:
            if standardize(x)==standardize(y):
            #if (x)==(y):
                result.append(x)
    return result
