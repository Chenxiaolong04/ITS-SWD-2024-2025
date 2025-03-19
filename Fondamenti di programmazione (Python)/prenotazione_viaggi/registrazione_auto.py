import sqlite3
from DatabaseUtilities import *
import string
import re
conn,cur=aperturaConnessione()
class auto:
    def registrazione_noleggio(nome,targa,durata):
        cur.execute('''
            insert into registrazione_auto(nome,targa,durata)
            values(?,?,?)
        ''',(nome,targa,durata))
        conn.commit()
        print("Registrazione noleggio auto avvenuta con successo")
        chiusura_connessione(conn,cur)
    def inputNome():
        conn,cur=aperturaConnessione()
        nome=input("Inserisci nome della macchina: ")
        nome = nome.strip()
        nome = nome.translate(str.maketrans("", "", string.punctuation))
        chiusura_connessione(conn,cur)
        print("Registrazione nome macchina avvenuta con successo")
        return nome
    def inputTarga():
        conn,cur=aperturaConnessione()
        while True:
            targa=input("Inserisci targa: ")
            targa = targa.strip()
            targa = targa.translate(str.maketrans("", "", string.punctuation))
            chiusura_connessione(conn,cur)
            print("Registrazione targa macchina avvenuta con successo")

            return targa

            