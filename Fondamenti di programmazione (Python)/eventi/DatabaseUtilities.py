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
'''
Funzione ricorsiva per l'input di un numero
def inputNumero(numero):
    try:
        numero=int(numero)
        return numero
    except Exception as e:
        print(e)
        nuovoNumero=input("Inserisci un numero: ")
        inputNumero(nuovoNumero)
        return inputNumero(nuovoNumero)'
'''
def inputNumero(numero):
    try:
        return int(numero)  
    except ValueError:
        print("Errore: Inserisci un numero valido!")
        nuovo_input = input("Riprova: ")  
        return inputNumero(nuovo_input)    