#!/usr/bin/env python
"""
Test the acrostore functions

"""

import os
from acronyms import acrostore

acronym_load = {
    'USA'   : 'United States of America',
    'TBD'   : 'To Be Determined',
    'DoD'   : 'Department of Defense',
    'HTML'  : 'Hypertext Markup Language',
    'FOUO'  : 'For Official Use Only',
    'ReGeX' : 'Regular Expression',
    'OS'    : 'Operating System',
}

def test_acroset_dumpload():
    test_file = 'data.json'
    assert acrostore.dump({}, test_file) == {}
    assert acrostore.dump(acronym_load, test_file) == acronym_load
    assert acrostore.load(test_file) == acronym_load

    dump_test = {
        'OS' : 'Open Source',
    }

    acronyms_update = acrostore.load(test_file)
    acronyms_update.update(dump_test)

    assert acrostore.dump(dump_test, test_file) == acronyms_update
    

    os.remove(test_file)
    print('Test file has been removed')

def test_acroset_print():

    assert acrostore.md_table(acronym_load) == \
        '|Acronym|Definition|\n' + \
        '|---|---|\n' + \
        '|ReGeX|Regular Expression|\n' + \
        '|USA|United States of America|\n' + \
        '|FOUO|For Official Use Only|\n' + \
        '|DoD|Department of Defense|\n' + \
        '|HTML|Hypertext Markup Language|\n' + \
        '|OS|Operating System|\n|TBD|To Be Determined|\n'
    assert acrostore.html_table(acronym_load, 'Test', 'Desc') == ''
