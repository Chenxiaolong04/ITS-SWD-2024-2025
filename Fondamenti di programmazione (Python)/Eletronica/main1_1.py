from Classe import prodotti, clienti, negozio
import sqlite3
import re
conn = sqlite3.connect('eletronica.sqlite')
cur = conn.cursor()
def registrazione_prodotto():
    while True:
        nome = input("Inserisci nome del prodotto: ")
        if not re.search(r'\d', nome):
            break
        print("Il nome non può contenere numeri, inserire nuovamente.")

    while True:
        try:
            quantita = int(input("Inserisci la quantità del prodotto: "))
            break
        except:
            print("Quantita inserito non valido, inserire nuovamente.")

    while True:
        try:
            prezzo = float(input("Inserisci il prezzo del prodotto: "))
            break
        except:
            print("Prezzo inserito non valido, inserire nuovamente.")
        
    prodotti().aggiunta_prodotto(nome, quantita, prezzo)
    conn.commit()
    print("Prodotto registrato con successo!")
    conn.close()
def registrazione_cliente():
    while True:
        nome = input("Inserisci nome del cliente: ")
        if not re.search(r'\d', nome):
            break
        print("Il nome non può contenere numeri, inserire nuovamente.")
    
    while True:
        cognome = input("Inserisci cognome del cliente: ")
        if not re.search(r'\d', cognome):
            break
        print("Cognome non valido, inserire nuovamente.")
    
    while True:
        try:
            eta = int(input("Inserisci età del cliente: "))
            break
        except:
            print("Valore inserito non valido, inserire nuovamente.")
    
    clienti().aggiunta_clienti(nome, cognome, eta)
    conn.commit()
    print("Cliente registrato con successo!")
    conn.close()
def vendita_prodotto():

    while True:
        nome_prodotto = input("Inserisci nome prodotto: ")
        cur.execute("SELECT id_prodotto, quantita FROM prodotti WHERE nome = ?", (nome_prodotto,))
        risultato_query = cur.fetchone()
        
        if risultato_query is None:
            print("Errore: prodotto non trovato.")
            continue
        break
    
    id_prodotto, disponibilita = risultato_query
    
    while True:
        try:
            quantita = int(input("Inserisci quantità da acquistare: "))
            if disponibilita < quantita:
                print("Errore: quantità insufficiente in magazzino.")
                continue
            break
        except ValueError:
            print("Errore: inserire una quantità valida.")
    
    id_cliente = input("Inserisci ID cliente: ")
    negozio().vendite(id_cliente, id_prodotto, quantita)
    cur.execute("UPDATE prodotti SET quantita = quantita - ? WHERE id_prodotto = ?", (quantita, id_prodotto))
    conn.commit()
    print("Vendita registrata con successo!")
    cur.close()
    conn.close()
while True:
    print("Menu di Scelta:")
    print("1. Registrazione Prodotto")
    print("2. Registrazione Cliente")
    print("3. Vendita Prodotto")
    print("4. Esci")
    
    scelta = input('Inserisci la scelta: ').strip()
    if scelta == '1':
        registrazione_prodotto()
        break
    elif scelta == '2':
        registrazione_cliente()
        break
    elif scelta == '3':
        vendita_prodotto()
        break
    elif scelta == '4':
        print("Uscita dal programma.")
        break
    else:
        print("Scelta non valida, riprova.")