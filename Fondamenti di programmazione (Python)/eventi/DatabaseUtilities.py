import sqlite3
import re
import string
def aperturaConnessione():
    conn=sqlite3.connect("eventi.sqlite")
    cur=conn.cursor()
    return conn,cur
def chiusura_connessione(conn, cur):
    cur.close() 
    conn.close()
def inputStringaConNumero(testo):
    while True:
        testo = testo.strip()
        if testo=="":
            print("Errore: hai inserito solo spazzi nell'input")
            continue
        return testo
def inputStringaSenzaNumero(testo):
    while True:
        testo = testo.strip()
        testo = testo.translate(str.maketrans("", "", string.punctuation))
        if testo=="":
            print("Errore: hai inserito solo spazzi nell'input")
            continue
        return testo
def inputNumero(numero):
    try:
        numero=int(numero)
        return numero
    except Exception as e:
        print(e)
        numero=input("Inserisci un numero: ")
        inputNumero(numero)