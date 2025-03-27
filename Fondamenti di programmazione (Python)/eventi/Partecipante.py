import sqlite3
from DatabaseUtilities import*
class Partecipante :
    def registrazione_partecipante(self,nome,cognome,id_evento):
        conn,cur=aperturaConnessione()
        cur.execute('''
            insert into PARTECIPANTE(nome,cognome,id_evento)
            values(?,?,?)
        ''',(nome,cognome,id_evento))
        cur.execute('''
            update EVENTO set capienzaMassima=capienzaMassima-1 where id_evento=?
        ''',(id_evento,))
        conn.commit()
        print("Registrazione del partecipante avvenuta con successo")
        chiusura_connessione(conn,cur)
 