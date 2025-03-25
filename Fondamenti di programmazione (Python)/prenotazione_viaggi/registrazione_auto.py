import sqlite3
from DatabaseUtilities import *
import string
import re
conn,cur=aperturaConnessione()
class Auto:
    def registrazione_noleggio(self,nome,targa):
        cur.execute('''
            insert into registrazione_auto(nome,targa)
            values(?,?)
        ''',(nome,targa))
        conn.commit()
        print("Registrazione noleggio auto avvenuta con successo")
        chiusura_connessione(conn,cur)
    def inputNome(self):
        conn,cur=aperturaConnessione()
        while True:
            nome=input("Inserisci nome della macchina: ")
            nome = nome.strip()
            nome = nome.translate(str.maketrans("", "", string.punctuation))
            if nome=="":
                print("Errore: hai inserito solo spazzi nell'input")
                continue
            break
        chiusura_connessione(conn,cur)
        return nome
    def inputTarga(self):
        conn,cur=aperturaConnessione()
        while True:
            targa=input("Inserisci targa: ")
            targa = targa.strip()
            targa = targa.translate(str.maketrans("", "", string.punctuation))
            if targa=="":
                print("Errore: hai inserito solo spazzi nell'input")
                continue
            break
        chiusura_connessione(conn,cur)
        print("Registrazione targa macchina avvenuta con successo")
        return targa

            