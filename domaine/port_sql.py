#! /usr/bin/env python3
# coding: utf-8

import sqlite3

def connection_a_la_base(chemin = 'interface/sqlite/db_sequence.db'):
    try:
        connection = sqlite3.connect(chemin)
        print('connection à la base ok')
    except:
        print('erreur de connexion')
    return connection

print(connection_a_la_base())

