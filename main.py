#! /usr/bin/env python3
# coding: utf-8

import interface.prototype.simple_testeur as simple_testeur
import domaine.algo_evolutioniste as algo

def test_1():
    simple_testeur.generer_des_sequences(2)
    for _ in range(2):
        simple_testeur.mutation('lechatestsurlemur','yvesestlamidebeatrice')

if __name__ == "__main__":
    test_1()
    algo.tout_faire()
    
    
