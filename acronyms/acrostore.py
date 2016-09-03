#!/usr/bin/env python

import cPickle as pickle
import os.path

_acronym_pickle = '../data/acronyms.p'
_dir_setup = os.path.dirname(os.path.realpath(__file__))

def dump(acroset, save=_acronym_pickle):
    raise NotImplementedError("dump has not been implemented")
