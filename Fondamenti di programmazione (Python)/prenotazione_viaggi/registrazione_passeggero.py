import sqlite3
from DatabaseUtilities import *
import string
import re
conn,cur=aperturaConnessione()
class passeggero:
    def registrazione_passeggero(self,nome,cognome):
        cur.execute('''
            insert into registrazione_passeggero(nome,cognome)
            values(?,?)
        ''',(nome,cognome))
        conn.commit()
        print("Registrazione passeggero avvetuna con successo")
        chiusura_connessione(conn,cur)
    def inputNome(self):
        conn,cur=aperturaConnessione()
        while True:
            nome=input("Inserisci nome del passeggero: ")
            nome = nome.strip()
            nome = nome.translate(str.maketrans("", "", string.punctuation))
            if not re.search(r'\d', nome):
                chiusura_connessione(conn,cur)
                #print("Registrazione nome passeggero avvenuta con successo")
                return nome
            print("Errore: il nome non può contenere numeri, inserire nuovamente.")
            continue
    def inputCognome(self):
        conn,cur=aperturaConnessione()
        while True:
            cognome=input("Inserisci cognome: ")
            cognome = cognome.strip()
            cognome = cognome.translate(str.maketrans("", "", string.punctuation))
            if not re.search(r'\d', cognome):
                chiusura_connessione(conn,cur)
                #print("Registrazione cognome passeggero avvenuta con successo")
                return cognome
            print("Errore: la cognome non può contenere numeri, inserire nuovamente.")
            continue