#! /usr/bin/env python3
# coding: utf-8

from domaine.sequence import *
from domaine.port_sql import *


def initiatisation_algo() -> None:
    creation_table_sequence()
    
def generation_sequence_et_score() -> tuple[str, float, float]:
    sequence: str = creation_sequence()
    score_lettre: float = calcul_score_freq_lettre(sequence)
    score_bigram: float = calcul_score_freq_bigram(sequence) 
    return sequence, score_lettre, score_bigram
    
def creation_generation_zero() -> tuple[int, int, str, float, float]:
    num_generation = 0
    age = 0
    sequence, score_lettre, score_bigram = generation_sequence_et_score()
    return num_generation, age, sequence, score_lettre, score_bigram
    
def mettre_generation_zero_dans_db() -> None:
    for _ in range(cst.NB_SEQ):
        num_generation, age, sequence, score_lettre, score_bigram = creation_generation_zero()   
        data = {'naissance': num_generation, 'age':age, 'etat':'actif', 'sequence':sequence, 
                'score_lettre':score_lettre, 'score_bigram':score_bigram, 'score_total': score_lettre + score_bigram }
        #print(data)
        ecrire_dans_db(data)
    
def tout_faire() -> None:
    initiatisation_algo()
    mettre_generation_zero_dans_db()
    tout_lire()