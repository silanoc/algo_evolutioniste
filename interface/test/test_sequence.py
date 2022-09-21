#! /usr/bin/env python3
# coding: utf-8

import random
from domaine.sequence import *

def test_donne_une_lettre(mocker):
    mocker.patch('random.randint', return_value=1)
    assert donne_une_lettre() == 'B'
 
def test_calcul_score_freq_lettre():
    score = calcul_score_freq_lettre('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    assert score == 99.99
    
def test_calcul_score_freq_bigram():
    score = calcul_score_freq_bigram('SCORE')
    assert score == 3.7