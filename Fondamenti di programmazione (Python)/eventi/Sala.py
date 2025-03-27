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
    def visualizza_sala(self):
        conn, cur = aperturaConnessione()
        cur.execute('''select * from SALA where disponibilita="si"''')
        rows = cur.fetchall()  
        if not rows:  
            print("Nessuna sala disponibile, aggiungi una sala prima")
            chiusura_connessione(conn, cur)
            return False
        print("Sale disponibili:")
        for row in rows:
            print(row[0], row[1], row[2])  
        chiusura_connessione(conn, cur)
        return True