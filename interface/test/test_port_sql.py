#! /usr/bin/env python3
# coding: utf-8

from domaine.port_sql import *

def test_connection_a_la_base():
    conn = connection_a_la_base()
    assert type(conn) == sqlite3.Connection
    
def test_creation_base():
    pass