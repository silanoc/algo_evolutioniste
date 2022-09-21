#! /usr/bin/env python3
# coding: utf-8

import random
import domaine.constante as cst

def donne_une_lettre()-> str:
    """defini un caractere au hasard issus de la constante ALPHABET
    
    :rtype: str
    """
    return cst.ALPHABET[random.randint(0, len(cst.ALPHABET) -1)]


def creation_sequence(taille: int) -> str:
    """créeation d'une chaine de caractère de taille défini en parametre.
    
    :param int taille: nombre de caractère attendu dans la chaine
    :return: sequence
    :rtype: str
    """
    sequence: str = ""
    for _ in range(taille):
        sequence += donne_une_lettre()
    return sequence


def calcul_score_freq_lettre(sequence: str) -> float:
    """definition du score d'une chaine en fonction de la fréquence d'une lettre.
    Il est défini par la somme des fréquence de chacune des lettre, fréquence défini dans le dictionnaire FREQ_LETTRE
    
    :param str sequence: la sequence dont on veut calculer le score
    :return: score, chiffre à 2 décimale
    :rtype: float
    """
    score: float = 0.0
    for lettre in sequence:
        score += cst.FREQ_LETTRE[lettre]
    return round(score, 2)

def calcul_score_freq_bigram(sequence: str) -> float:
    """definition du score d'une chaine en fonction de la fréquence d'un bigram.
    Il est défini par la somme des fréquence de chacune des bigram, fréquence défini dans le dictionnaire FREQ_BIGRAM
    
    :param str sequence: la sequence dont on veut calculer le score
    :return: score, chiffre à 2 décimale
    :rtype: float
    """
    score: float = 0.0
    for caract in range(len(sequence) - 1):
        bigram = sequence[caract] + sequence[caract + 1]
        if bigram in cst.FREQ_BIGRAM:
            score += cst.FREQ_BIGRAM[bigram]
    return round(score, 2)


def deletion_dans_sequence(sequence: str) -> str:
    """Pour chaque caractère de la sequence, si la fréquence est inf à FREQ_DELETION, supprime le caratère de la sequence
    
    :param str sequence: la sequence à muter par deletion
    :return: new_seq, sequence avec le meme nombre de caratère ou moins
    :rtype: str
    """
    new_seq: str = ""
    for caractere in sequence:
        hasard: float = random.random()
        if hasard > cst.FREQ_DELETION:
            new_seq += caractere
    return new_seq
      
def ajout_dans_sequence(sequence: str) -> str:
    new_seq: str = ""
    for caractere in sequence:
        hasard: float = random.random()
        if hasard < cst.FREQ_AJOUT:
            new_seq += caractere + donne_une_lettre()
        else:
            new_seq += caractere    
    return new_seq

def changement_dans_sequence(sequence: str) -> str:
    new_seq: str = ""
    for caractere in sequence:
        hasard: float = random.random()
        if hasard < cst.FREQ_PERMUTATION:
            new_seq += donne_une_lettre()
        else:
            new_seq += caractere    
    return new_seq

def crossing_over(sequence1: str, sequence2:str)-> tuple[str]:
    new_sequence1 = ""
    new_sequence2 = ""
    if len(sequence1) > len(sequence2):
        petit = sequence2
    else:
        petit = sequence1
    point_de_crossing = random.randint(0, len(petit) - 1)
    new_sequence1 = sequence1[:point_de_crossing + 1] + sequence2[point_de_crossing + 1:]
    new_sequence2 = sequence2[:point_de_crossing + 1] + sequence1[point_de_crossing + 1:]
    return(new_sequence1, new_sequence2)