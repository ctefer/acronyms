#!/usr/bin/env python
"""
Provides functions used to manipulate and find acronyms

"""
import re
import acrostore

acronym_finds = [ r'\b(?:[A-Z](?:\.|[aeiou]*)){2,}(?:\.|\b)']

def find(text):
    _dict = dict()

    for reg in acronym_finds:
        c = re.compile(reg)
        m = c.findall(text)
        if m is not None:
            _dict.update(m)

    return(_dict)

def define_first(text, acro, desc):
    return re.sub(acro, desc + '(' + acro + ')', text, 1)

def define_first_all(text):
    a_list = find(text)
    a_data = acrostore.load()

    for a in a_list:
        if a in a_data:
            define_first(text, a, a_data[a])

    return text

def get_defins(text):
    _disc = find(text)
    _ret = dict()

    for acro in _desc.items():
        if acro in _desc:
            _ret.update(acro, _desc[acro])
        else:
            _ret.update(acro, 'No Description')

    return _ret
