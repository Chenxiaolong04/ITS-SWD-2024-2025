import sqlite3
import re
import string
def aperturaConnessione():
    conn=sqlite3.connect("ospedale.sqlite")
    cur=conn.cursor()
    return conn,cur
def chiusuraConnessione(conn, cur):
    cur.close() 
    conn.close()
def inputStringaConNumero(testo):
    while True:
        testo = testo.strip()
        if testo=="":
            print("Errore: hai inserito solo spazzi nell'input")
            testo=input("Inserisci nuovamente: ")
            continue
        break
    return testo
def inputStringaSenzaNumero(testo):
    while True:
        testo = testo.strip()
        testo = testo.translate(str.maketrans("", "", string.punctuation))
        if testo=="":
            print("Errore: hai inserito solo spazzi nell'input")
            testo=input("Inserisci nuovamente: ")
            continue
        if re.search(r'\d', testo):
            print("Errore: hai inserito un numero nell'input")
            testo=input("Inserisci nuovamente: ")
            continue
        break
    return testo

def inputNumero(numero):
    try:
        return int(numero)  
    except ValueError:
        print("Errore: Inserisci un numero valido!")
        nuovo_input = input("Riprova: ")  
        return inputNumero(nuovo_input)    
    