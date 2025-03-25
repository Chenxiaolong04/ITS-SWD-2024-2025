import sqlite3
from DatabaseUtilities import *
import string
import re
class Passeggero:
    def registrazione_passeggero(self,nome,cognome):
        conn,cur=aperturaConnessione()
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
            if nome=="":
                print("Errore: hai inserito solo spazzi nell'input")
                continue
            if re.search(r'\d', nome):
                print("Errore: il nome non può contenere numeri, inserire nuovamente.")
                continue
            return nome
    def inputCognome(self):
        conn,cur=aperturaConnessione()
        while True:
            cognome=input("Inserisci cognome: ")
            cognome = cognome.strip()
            cognome = cognome.translate(str.maketrans("", "", string.punctuation))
            if cognome=="":
                print("Errore: hai inserito solo spazzi nell'input")
                continue
            if re.search(r'\d', cognome):
                print("Errore: la cognome non può contenere numeri, inserire nuovamente.")
                continue
            return cognome
