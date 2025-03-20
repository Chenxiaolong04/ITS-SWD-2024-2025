from DatabaseUtilities import*
import sqlite3
class Evento:
    def registrazione_evento(self,nome,capienzaMassima):
        conn,cur=aperturaConnessione()
        cur.execute('''
            insert into EVENTO(nome,capienzaMassima)
            values(?,?)
        ''',(nome,capienzaMassima))
        conn.commit()
        print("Registrazione dell'evento avvenuta con successo")
        chiusura_connessione(conn,cur)
