import sqlite3
from DatabaseUtilities import *

conn, cur = aperturaConnessione()

# Elimina le tabelle esistenti (se necessario)
cur.execute("DROP TABLE IF EXISTS registrazione_volo")
cur.execute("DROP TABLE IF EXISTS registrazione_hotel")
cur.execute("DROP TABLE IF EXISTS registrazione_auto")
cur.execute("DROP TABLE IF EXISTS registrazione_passeggero")
cur.execute("DROP TABLE IF EXISTS prenotazioni_volo")
cur.execute("DROP TABLE IF EXISTS prenotazioni_hotel")
cur.execute("DROP TABLE IF EXISTS prenotazioni_auto")

# Crea le tabelle
cur.execute('''
    CREATE TABLE registrazione_volo(
        id_volo INTEGER PRIMARY KEY AUTOINCREMENT,
        partenza TEXT,
        destinazione TEXT,
        ora TEXT,
        durata INTEGER
    )
''')

cur.execute('''
    CREATE TABLE registrazione_hotel(
        id_hotel INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        via TEXT
    )
''')

cur.execute('''
    CREATE TABLE registrazione_auto(
        id_noleggio INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        targa TEXT,
        durata INTEGER
    )
''')

cur.execute('''
    CREATE TABLE registrazione_passeggero(
        id_passeggero INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT,
        cognome TEXT
    )
''')

# Tabelle per le prenotazioni
cur.execute('''
    CREATE TABLE prenotazioni_volo(
        id_prenotazione INTEGER PRIMARY KEY AUTOINCREMENT,
        passeggero_id INTEGER,
        volo_id INTEGER,
    )
''')

cur.execute('''
    CREATE TABLE prenotazioni_hotel(
        id_prenotazione INTEGER PRIMARY KEY AUTOINCREMENT,
        passeggero_id INTEGER,
        hotel_id INTEGER,
    )
''')

cur.execute('''
    CREATE TABLE prenotazioni_auto(
        id_prenotazione INTEGER PRIMARY KEY AUTOINCREMENT,
        passeggero_id INTEGER,
        auto_id INTEGER,
    )
''')

conn.commit()
chiusura_connessione(conn, cur)