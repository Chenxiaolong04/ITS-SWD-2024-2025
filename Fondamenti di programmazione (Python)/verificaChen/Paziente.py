import sqlite3
from DatabaseUtilities import *
class Paziente:
    def registrazionePaziente(self,nome,cognome):
        conn,cur=aperturaConnessione()
        cur.execute('''
            INSERT INTO paziente (nome, cognome)
            VALUES (?, ?)
        ''', (nome, cognome))
        conn.commit()
        chiusuraConnessione(conn,cur)
        print("Registrazione paziente completata con successo")

        