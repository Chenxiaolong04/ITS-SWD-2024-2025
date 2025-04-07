import sqlite3
from DatabaseUtilities import *
class Visita:
    def registrazioneVisita(self,id_paziente,id_medico):
        conn,cur=aperturaConnessione()
        cur.execute('''
            INSERT INTO visita (id_paziente, id_medico)
            VALUES (?, ?)
        ''', (id_paziente, id_medico))
        conn.commit()
        chiusuraConnessione(conn,cur)
        print("Registrazione visita completata con successo")
        