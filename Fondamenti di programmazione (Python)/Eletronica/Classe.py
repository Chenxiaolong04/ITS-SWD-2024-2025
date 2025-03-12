'''
3 classi
    prodotti
        aggiunta di prodotti : se il prodotto esiste gia viene aggiunto altrimenti un nuovo prodotto
    clienti
        registrazione clienti
    negozio
        vendite una riga per tipo di prodotto se ne compra di piu
'''
import sqlite3
conn = sqlite3.connect('eletronica.sqlite')
cur = conn.cursor()
class prodotti:
    def aggiunta_prodotto(self,nome,quantita,prezzo):
        
        cur.execute('''
            insert into prodotti(nome,quantita,prezzo)
            values(?,?,?)
        ''',(nome,quantita,prezzo))
        print("prodotto aggiunto")
        conn.commit()
        cur.close()
class clienti:
    def aggiunta_clienti(self,nome,cognome,eta):
        cur.execute('''
            insert into clienti(nome,cognome,eta)
            values(?,?,?)
        ''',(nome,cognome,eta))
        conn.commit()
        cur.close()
class negozio:
    def vendite(self,id_cliente,id_prodotto,quantita):
        cur.execute('''
            insert into vendite(id_cliente,id_prodotto,quantita)
            values(?,?,?)
        ''',(id_cliente,id_prodotto,quantita))
        conn.commit()
        cur.close()