#! /usr/bin/env python3
# coding: utf-8

import random
import pytest
from domaine.sequence import *
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
    
def test_ajout_dans_sequence(mocker):
    random.random = Mock()
    random.random.side_effect = [0.9, 0.9, 0.001, 0.9, 0.9, 0.9]
    mocker.patch('domaine.sequence.donne_une_lettre', return_value='W')
    seq = ajout_dans_sequence('AZERTY')
    assert seq == 'AZEWRTY'
    
def test_changement_dans_sequence(mocker):
    random.random = Mock()
    random.random.side_effect = [0.9, 0.9, 0.001, 0.9, 0.9, 0.9]
    mocker.patch('domaine.sequence.donne_une_lettre', return_value='W')
    seq = changement_dans_sequence('AZERTY')
    assert seq == 'AZWRTY'
    
def test_crossing_over(mocker):
    mocker.patch('random.randint', return_value=2)
    seq1, seq2 = crossing_over('AZERTY', 'QSDFGHJ')
    assert seq1 == "AZEFGHJ" and seq2 == "QSDRTY"
