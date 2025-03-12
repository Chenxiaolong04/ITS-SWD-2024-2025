from Classe import prodotti, clienti, negozio
import sqlite3
import re

conn = sqlite3.connect('eletronica.sqlite')
cur = conn.cursor()

print("Menu di Scelta:")
print("1. Registrazione Prodotto")
print("2. Registrazione Cliente")
print("3. Vendita Prodotto")
print("4. Esci")

#scelta = input('Inserisci la scelta: ')

while True:

    try:
        scelta = input('Inserisci la scelta: ').strip()
        if re.search(r'^\d+$', scelta):  
            if scelta == '1':  # Se la scelta è 1, registra il prodotto
                while True:
                    nome = input("Inserisci nome del prodotto: ")
                    if not re.search(r'\d', nome):  # Controllo che il nome non contenga numeri
                        while True:
                            try:
                                quantita = int(input("Inserisci la quantita del prodotto: "))
                                break  # Se il valore è corretto, esce dal ciclo
                            except :
                                print("Valore inserito non valido, inserire nuovamente.")
                        
                        while True:
                            try:
                                prezzo = float(input("Inserisci il prezzo del prodotto: "))
                                break  # Se il valore è corretto, esce dal ciclo
                            except :
                                print("Valore inserito non valido, inserire nuovamente.")
                        break  # Esce dal ciclo di registrazione prodotto
                    else:
                        print("Il nome non può contenere numeri, inserire nuovamente.")
                        continue  # Ritorna alla richiesta del nome
                prodotti().aggiunta_prodotto(nome,quantita,prezzo)
                conn.commit()
                break  # Esce dal ciclo principale dopo la registrazione del prodotto
            if(scelta=='2'):
                while True:
                    nome = input("Inserisci nome del cliente: ")
                    if not re.search(r'\d', nome):  # Controllo che il nome non contenga numeri
                        while True:
                            
                                cognome = input("Inserisci cognome del cliente: ")
                                if not re.search(r'\d', cognome):
                                    while True:
                                        try:
                                            eta = int(input("Inserisci eta del cliente: "))
                                            break  # Se il valore è corretto, esce dal ciclo
                                        except :
                                            print("Valore inserito non valido, inserire nuovamente.")
                                    break  # Esce dal ciclo di registrazione prodotto
                                else:
                                    print("Cognome non valido, inserire nuovamente.")              
                    else:
                        print("Il nome non può contenere numeri, inserire nuovamente.")
                        continue  # Ritorna alla richiesta del nome
                    break  # Esce dal ciclo principale dopo la registrazione del prodotto
                clienti().aggiunta_clienti(nome,cognome,eta)

                break
            if(scelta=='3'):
                nome_prodotto=input('Inserisci nome prodotto: ')
                cur.execute('''
                select nome
                from prodotti
                where nome=?
                ''',(nome_prodotto))
                risultato=cur.fetchone()[0]
                
                if(risultato != None):
                    quantita_prodotto=int(input("Inserisci quantita che vuoi vendere"))
                    cur.execute('''
                    select quantita
                    from prodotti
                    where nome=?
                    ''',(nome_prodotto))
                    quantita_prodotto=cur.fetchone()[0]
                    print(quantita_prodotto)
                    print(type(quantita_prodotto))
                else:
                    if(scelta=='4'):
                        pass
                        print("Uscita dal programma")
                        break
        else: 
            print("Valore inserito non valido1")  
            continue 
            
    except:
        print("Valore inserito non valido2")
        continue




            


        