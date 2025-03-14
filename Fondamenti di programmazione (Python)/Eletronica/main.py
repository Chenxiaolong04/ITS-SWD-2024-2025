from Classe import prodotti, clienti, negozio
import sqlite3
import re
import string
from datetime import datetime
conn = sqlite3.connect('eletronica.sqlite')
cur = conn.cursor()
def registrazione_prodotto():
    #while True:
    nome = input("Inserisci nome del prodotto: ")
    nome = nome.strip()
    nome = nome.translate(str.maketrans("", "", string.punctuation))
        #if not re.search(r'\d', nome):
            #break
        #print("Il nome non può contenere numeri, inserire nuovamente.")

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
def registrazione_cliente():
    while True:
        nome = input("Inserisci nome del cliente: ")
        nome = nome.strip()
        if not re.search(r'\d', nome):
            break
        print("Il nome non può contenere numeri, inserire nuovamente.")
    
    while True:
        cognome = input("Inserisci cognome del cliente: ")
        cognome = cognome.strip()
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
def vendita_prodotto():


    while True:
        nome_prodotto = input("Inserisci nome prodotto: ")
        nome_prodotto = nome_prodotto.strip()
        nome_prodotto = nome_prodotto.translate(str.maketrans("", "", string.punctuation))
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
        except:
            print("Errore: inserire una quantità valida.")
    while True:
        id_cliente = input("Inserisci ID cliente: ")
        try:
            id_cliente = int(id_cliente)
        except:
            print("Errore: inserire un ID valido.")
            continue
        cur.execute("SELECT id_cliente FROM clienti WHERE id_cliente = ?", (id_cliente,))
        risultato_query = cur.fetchone()
        if risultato_query is None:
            print("Errore: utente non registrato.")
            continue
        data_vendita= datetime.datetime.now().strftime("%Y-%m-%d")
        negozio().vendite(id_cliente, id_prodotto, quantita,nome_prodotto)
        cur.execute("UPDATE prodotti SET quantita = quantita - ? WHERE id_prodotto = ?", (quantita, id_prodotto))
        conn.commit()
        print("Vendita registrata con successo!")
        cur.execute("SELECT quantita FROM prodotti WHERE id_prodotto = ?", (id_prodotto,))
        risultato_query = cur.fetchone()[0]
        if risultato_query == 0:
            print("Prodotto esaurito")
            cur.execute("DELETE FROM prodotti WHERE id_prodotto = ?", (id_prodotto,))
            conn.commit()

        break
def restituzione_prodotto(id_prodotto,data_vendita):
    cur.execute("select data_vendita from vendite where id_vendita = ?",(id_vendita,))
    data_vendita = cur.fetchone()[0]
    data_odierna = datetime.datetime.now().strftime("%Y-%m-%d")
    if data_odierna - data_vendita<7:
        cur.execute("select quantita from vendite where id_prodotto = ?",(id_prodotto,))
        quantita = cur.fetchone()[0]
        cur.execute("update prodotti set quantita = quantita + ? where id_prodotto = ?",(quantita,id_prodotto))
        cur.execute("delete from vendite where id_prodotto = ?",(id_prodotto,))
        conn.commit()
        print("Prodotto restituito con successo")
while True:
    print("Menu di Scelta:")
    print("1. Registrazione Prodotto")
    print("2. Registrazione Cliente")
    print("3. Vendita Prodotto")
    print("4. Restituzione Prodotto")
    print("5. Esci")
    
    scelta = input('Inserisci la scelta: ').strip()
    if scelta == '1':
        registrazione_prodotto()
        continue
    elif scelta == '2':
        registrazione_cliente()
        continue
    elif scelta == '3':
        vendita_prodotto()
        continue
    elif scelta == '4':
        data_odierna = datetime.now().strftime("%Y-%m-%d")
        data_restituzione= datetime.now().strftime("%Y-%m-%d")
        if data_odierna-data_restituzione<0:
            print("minore 0")
        elif data_odierna-data_restituzione==0:
            print("uguale 0")
        else:
            print("maggiore 0")
        print(data_odierna)
        continue
    elif scelta == '5':
        print("Uscita dal programma.")
        cur.close()
        conn.close()
        break
    else:
        print("Scelta non valida, riprova.")