import sqlite3
from DatabaseUtilities import*
class Sala:
    def registrazione_sala(self,nome,disponibilità):
        conn,cur=aperturaConnessione()
        cur.execute('''
            insert into SALA(nome,disponibilita)
            values(?,?)
        ''',(nome,disponibilità))
        conn.commit()
        print("Registrazione della sala avvenuta con successo")
        chiusura_connessione(conn,cur)
