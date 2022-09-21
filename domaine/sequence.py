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