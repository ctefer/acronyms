#!/usr/bin/env python

import re

acronym_flags = [
        r'\b(?:[A-Z](?:\.|[aeiou]*)){2,}(?:\.|\b)',
]

def check_acronym(text):
    _list = set()

    for reg in acronym_flags:
        c = re.compile(reg)
        m = c.findall(text)
        if m is not None:
            _list.update(m)

    return(list(_list))
