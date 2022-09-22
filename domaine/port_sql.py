#! /usr/bin/env python3
# coding: utf-8

from cgitb import lookup
import sqlite3
import logging

from multiprocessing import connection


CHEMIN = 'interface/sqlite/db_sequence.db'

logging.basicConfig(level = logging.DEBUG,
                    filename = "interface/mes_logs/port_sql.log",
                    filemode = "a",
                    format = '%(asctime)s -%(levelname)s - %(message)s')

def connection_a_la_base(chemin = CHEMIN):
    try:
        connection = sqlite3.connect(chemin)
        logging.debug("connection à la base ok")
    except:
        logging.error("erreur de connexion")
    return connection

def creation_table_sequence(chemin = CHEMIN):
    try:
        connection = connection_a_la_base(chemin)
        curseur = connection.cursor()
        table_sequence = '''CREATE TABLE IF NOT EXISTS Tb_sequence(
            ID INTEGER,
            Naissance INTEGER,
            Age INTEGER,
            Etat INTEGER,
            Sequence TEXT,
            Score_lettre REAL,
            Score_bigram REAL,
            Score_total REAL     
        )'''
        curseur.execute(table_sequence)
        logging.debug('création base ok')
    except:
        logging.error('base non créée')    


creation_table_sequence()