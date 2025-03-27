from DatabaseUtilities import *
import sqlite3
conn,cur=aperturaConnessione()
cur.execute('DROP TABLE IF EXISTS SALA')
cur.execute('DROP TABLE IF EXISTS EVENTO')
cur.execute('DROP TABLE IF EXISTS PARTECIPANTE')

cur.execute('''
create table SALA(
id_sala integer primary key autoincrement,
nome text,
disponibilita text
)''')
cur.execute('''
create table EVENTO(
id_evento integer primary key autoincrement,
nome text,
capienzaMassima integer,
id_sala integer
)''')
cur.execute('''
create table PARTECIPANTE(
id_partecipante integer primary key autoincrement,
nome text,
cognome text,
id_evento integer
)''')
chiusura_connessione(conn,cur)
