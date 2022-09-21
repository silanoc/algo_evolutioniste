#! /usr/bin/env python3
# coding: utf-8

import random
import constante as cst

def donne_une_lettre()-> str:
    return cst.ALPHABET[random.randint(0, len(cst.ALPHABET))]