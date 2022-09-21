#! /usr/bin/env python3
# coding: utf-8

import domaine.sequence as sequence

def generer_des_sequences(nb):
    for _ in range(nb):
        seq = sequence.creation_sequence(15)
        score_lettre = sequence.calcul_score_freq_lettre(seq)
        score_bigram = sequence.calcul_score_freq_bigram(seq)
        print(seq, score_lettre, score_bigram)
        
def mutation(seq1, seq2):
    new_seq1 = sequence.deletion_dans_sequence(seq1)
    new_seq2 = sequence.ajout_dans_sequence(seq2)
    ter_seq1, ter_seq2 = sequence.crossing_over(new_seq1, new_seq2)
    print(ter_seq1, ter_seq2)