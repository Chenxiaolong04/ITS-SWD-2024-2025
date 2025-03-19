import sqlite3
from DatabaseUtilities import *
import string
import re
conn,cur=aperturaConnessione()
class hotel:
    def registrazione_hotel(nome,via):
        cur.execute('''
            insert into registrazione_hotel(nome,via)
            values(?,?)
        ''',(nome,via))
        conn.commit()
        print("Registrazione hotel avvenuta con successo")
        chiusura_connessione(conn,cur)
    def inputNome():
        conn,cur=aperturaConnessione()
        while True:
            nome=input("Inserisci nome dell'hotel: ")
            nome = nome.strip()
            nome = nome.translate(str.maketrans("", "", string.punctuation))
            if not re.search(r'\d', nome):
                chiusura_connessione(conn,cur)
                print("Registrazione nome hotel avvenuta con successo")
                return nome
            print("Errore: il nome non può contenere numeri, inserire nuovamente.")
            continue
    def inputVia():
        conn,cur=aperturaConnessione()
        while True:
            via=input("Inserisci via: ")
            via = via.strip()
            via = via.translate(str.maketrans("", "", string.punctuation))
            chiusura_connessione(conn,cur)
            print("Registrazione via hotel avvenuta con successo")
            return via
