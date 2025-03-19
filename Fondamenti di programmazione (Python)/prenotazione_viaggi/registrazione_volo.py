import sqlite3
from DatabaseUtilities import *
import string
import re
class Volo:
    def registrazione_volo(self,partenza,destinazione,ora,durata):
        conn,cur=aperturaConnessione()
        cur.execute('''
            insert into registrazione_volo(partenza,destinazione,ora,durata)
            values(?,?,?,?)
        ''',(partenza,destinazione,ora,durata))
        conn.commit()
        print("Registrazione volo avvenuta con successo")
        chiusura_connessione(conn,cur)
    def inputPartenza(self):
        conn,cur=aperturaConnessione()
        while True:
            partenza=input("Inserisci partenza: ")
            partenza = partenza.strip()
            partenza = partenza.translate(str.maketrans("", "", string.punctuation))
            if partenza=="":
                print("Errore: hai inserito solo spazzi nell'input")
                continue
            if not re.search(r'\d', partenza):
                chiusura_connessione(conn,cur)
                return partenza
            print("Errore: la partenza non può contenere numeri, inserire nuovamente.")
            continue
    def inputDestinazione(self):
        conn,cur=aperturaConnessione()
        while True:
            destinazione=input("Inserisci destinazione: ")
            destinazione = destinazione.strip()
            destinazione = destinazione.translate(str.maketrans("", "", string.punctuation))
            if destinazione=="":
                print("Errore: hai inserito solo spazzi nell'input")
                continue
            if not re.search(r'\d', destinazione):
                chiusura_connessione(conn,cur)
                return destinazione
            print("Errore: la destinazione non può contenere numeri, inserire nuovamente.")
            continue
    def inputOrario(self):
        conn,cur=aperturaConnessione()
        while True:
            try:
                orario=input("Inserisci orario di partenza: ")
                orario = orario.strip()
                if orario=="":
                    print("Errore: hai inserito solo spazzi nell'input")
                    continue
                chiusura_connessione(conn,cur)
                return orario
            except Exception:
                print(Exception)
                continue
    def inputDurata(self):
        conn,cur=aperturaConnessione()
        while True:
            try:
                orario=int(input("Inserisci durata di volo: "))
                if(orario<=0):
                    print("Errore: la durata non puo' essere negativa o uguale a 0 ")
                    continue
                chiusura_connessione(conn,cur)
                print("Registrazione durata avvenuta con successo")
                return orario
            except Exception:
                print(Exception)
                continue
