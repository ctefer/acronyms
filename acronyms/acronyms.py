#!/usr/bin/env python
"""
Provides functions used to manipulate and find acronyms

"""
import re

acronym_flags = [
        r'\b(?:[A-Z](?:\.|[aeiou]*)){2,}(?:\.|\b)',
]


def find(text):
    _list = set()

    for reg in acronym_flags:
        c = re.compile(reg)
        m = c.findall(text)
        if m is not None:
            _list.update(m)

    return(list(_list))

"""
Find all acronyms in a given text and standardize to a common format.

Formats should be given in the following:

"""
def standardize(text, f):
    raise NotImplementedError("standardize has not been implemented")

def define_first(acro, desc):
    raise NotImplementedError("define_first has not been implemented")
