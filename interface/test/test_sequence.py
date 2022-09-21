#! /usr/bin/env python3
# coding: utf-8

import random
from domaine.sequence import *

def test_donne_une_lettre(mocker):
    mocker.patch('random.randint', return_value=1)
    assert donne_une_lettre() == 'A'
 
