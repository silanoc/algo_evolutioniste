#! /usr/bin/env python3
# coding: utf-8

from cgitb import lookup
import sqlite3
import logging

from multiprocessing import connection

CHEMIN = 'interface/sqlite/db_sequence.db'

logging.basicConfig(level = logging.DEBUG,
                    filename = "interface/mes_logs/port_sql.log",
                    filemode = "w",
                    format = '%(asctime)s -%(levelname)s - %(message)s')

def connection_a_la_base(chemin = CHEMIN):
    try:
        connection = sqlite3.connect(chemin)
        logging.debug("connection à la base ok")
    except:
        logging.error("erreur de connexion")
    return connection

def creation_table_sequence(chemin = CHEMIN) -> None:
    try:
        connection = connection_a_la_base(chemin)
        curseur = connection.cursor()
        table_sequence = '''CREATE TABLE IF NOT EXISTS Tb_sequence(
            ID INTEGER primary key autoincrement,
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
    try:
        connection.close()
        logging.debug('base de donnée fermée')
    except:
        logging.error('base non fermée')   

def ecrire_dans_db(data) -> None:
    connection = connection_a_la_base()
    curseur = connection.cursor()
    try:
        sql = "INSERT INTO Tb_sequence(Naissance, Age, Etat, Sequence, Score_lettre, Score_bigram, Score_total) VALUES(?,?,?,?,?,?,?)"
        liste = [data['naissance'], data['age'], data['etat'], data['sequence'], data['score_lettre'], data['score_bigram'], data['score_total']]
        print(liste)
        curseur.execute(sql, liste)
        connection.commit()                        
        logging.debug(f"donnée écrite {data}")
    except:
        logging.error('données non écrite')
    try:
        connection.close()
        logging.debug('base de donnée fermée')
    except:
        logging.error('base non fermée')  
      

def tout_lire() -> None:
    connection = connection_a_la_base()
    curseur = connection.cursor()
    try:
        sql = "SELECT * FROM Tb_sequence"
        curseur.execute(sql)
        result = curseur.fetchall()
        print(result)
        logging.debug(result)
    except:
        logging.error('impossible de lire la base')
    try:
        connection.close()
        logging.debug('base de donnée fermée')
    except:
        logging.error('base non fermée')     
    