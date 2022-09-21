#! /usr/bin/env python3
# coding: utf-8

import random
import pytest
from domaine.sequence import donne_une_lettre, creation_sequence, calcul_score_freq_bigram, calcul_score_freq_lettre, deletion_dans_sequence
from unittest.mock import Mock, patch                                                                                                                                                                                 

def test_donne_une_lettre(mocker):
    mocker.patch('random.randint', return_value=1)
    assert donne_une_lettre() == 'B'

#@pytest.mark.parametrize('domaine.sequence.donne_une_lettre', ['A', 'B'])
def test_creation_sequence(mocker):
    mocker.patch('domaine.sequence.donne_une_lettre', return_value='A')
    #mocker.patch('domaine.sequence.donne_une_lettre', return_value='B')
    mot = creation_sequence(2)
    assert mot == ('AA')
    
def test_calcul_score_freq_lettre():
    score = calcul_score_freq_lettre('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
    assert score == 99.99
    
def test_calcul_score_freq_bigram():
    score = calcul_score_freq_bigram('SCORE')
    assert score == 3.7

def test_deletion_dans_sequence():
    random.random = Mock()
    random.random.side_effect = [0.9, 0.9, 0.001, 0.9, 0.9, 0.9]
    seq = deletion_dans_sequence('AZERTY')
    assert seq == 'AZRTY'