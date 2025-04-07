from DatabaseUtilities import *
import sqlite3
conn,cur=aperturaConnessione()
cur.execute('DROP TABLE IF EXISTS medici')  
cur.execute('DROP TABLE IF EXISTS paziente')
cur.execute('DROP TABLE IF EXISTS visita')

cur.execute('''
    CREATE TABLE IF NOT EXISTS medici (
        id_medico INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cognome TEXT,
        disponibilita TEXT,
        numero_pazienti INTEGER DEFAULT 0
    )
''')
cur.execute('''
create table paziente(
        id_paziente integer primary key autoincrement,
        nome text,
        cognome text,
        id_medico integer
)''')
cur.execute('''
create table visita(
        id_visita integer primary key autoincrement,
        id_paziente integer,
        id_medico integer
)''')
chiusuraConnessione(conn,cur)
