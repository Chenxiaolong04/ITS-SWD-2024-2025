import sqlite3
from DatabaseUtilities import *
conn,cur=aperturaConnessione()
cur.execute("DROP TABLE IF EXISTS registrazione_volo")
cur.execute("DROP TABLE IF EXISTS registrazione_hotel")
cur.execute("DROP TABLE IF EXISTS registrazione_auto")
cur.execute("DROP TABLE IF EXISTS registrazione_passeggero")
cur.execute('''
    create table registrazione_volo(
    id_volo integer primary key autoincrement,
    partenza text,
    destinazione text,
    ora text,
    durata integer
)''')
cur.execute('''
    create table registrazione_hotel(
    id_hotel integer primary key autoincrement,
    nome text,
    via text
)''')
cur.execute('''
    create table registrazione_auto(
    id_noleggio integer primary key autoincrement,
    nome text,
    targa text
)''')
cur.execute('''
    create table registrazione_passeggero(
    id_passeggero integer primary key autoincrement,
    nome text,
    cognome text
)''')