from DatabaseUtilities import*
import sqlite3
class Evento:
    def registrazione_evento(self,nome,capienzaMassima,id_sala):
        conn,cur=aperturaConnessione()
        cur.execute('''
            insert into EVENTO(nome,capienzaMassima,id_sala)
            values(?,?,?)
        ''',(nome,capienzaMassima,id_sala))
        cur.execute('''
            update SALA set disponibilita="no" where id_sala=?
        ''',(id_sala,))
        conn.commit()
        print("Registrazione dell'evento avvenuta con successo")
        chiusura_connessione(conn,cur)
    def visualizza_evento(self):
        conn,cur=aperturaConnessione()
        cur.execute('''
            select * from EVENTO where capienzaMassima>0
        ''')
        print("Eventi disponibili:")
        if(cur.fetchone() is None):
            print("Nessun evento disponibile aggiungi un evento prima")
            chiusura_connessione(conn,cur)
            return False
        for row in cur.fetchall():
            print(row[0],row[1],row[2],row[3])
        chiusura_connessione(conn,cur)
