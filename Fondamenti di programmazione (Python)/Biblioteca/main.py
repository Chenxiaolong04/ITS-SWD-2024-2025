from classe import Libri, Iscritti, Biblioteca
import re
import sqlite3
conn = sqlite3.connect('biblioteca.sqlite')
cur = conn.cursor()
print('''
        1. Aggiungi libro
        2. Registra iscritto
        3. Prestito
        4. Restituzione
        5. Esci
        ''')
scelta=input("Inserisci la tua scelta: ")
while True:

    try:
        
        if scelta=='1':
            titolo=input("Inserisci il titolo del libro: ")
            
           
            while True:
                autore=input("Inserisci l'autore del libro: ")
                if re.search(r'\d', autore):
                    print("Errore: Il nome dell'autore non può contenere un numero.")
                    continue
                else:
                    break
            quantita=int(input("Inserisci la quantita del libro: "))
            Libri().aggiunta(titolo, autore, quantita)
            break
        
        if scelta=='2':
            nome=input("Inserisci il nome dell'iscritto: ")
            if re.search(r'\d', nome):
                print("Errore: Il nome non può contenere un numero.")
                continue
            else:
                while True:
                    cognome=input("Inserisci il cognome dell'iscritto: ")
                    if re.search(r'\d', cognome):
                        print("Errore: Il cognome non può contenere un numero.")
                        continue
                    else:
                        break
            data_nascita=input("Inserisci la data di nascita dell'iscritto: ")
            Iscritti().registrazione(nome,cognome,data_nascita)
            break

        if scelta=='3':
            id_libro=input("Inserisci id del libro che vuoi prestare: ")
            cur.execute('''
            select id_libro
            from libri
            where id_libro=?
            ''',(id_libro,))
            risultato=cur.fetchone()[0]
            if risultato==None:
                print("Il libro non e' disponibile per il prestito")
                exit()
            else:
                id_iscritto=input("Inserisci tuo id: ")
                print(type(id_iscritto))
                if re.search(r'^\d+$', id_libro,id_iscritto):  # Cerca solo numeri in tutta la stringa
                    data_prestito=input("Inserisci data prestito in formato 'aaaa-mm-gg': ")
                    Biblioteca().prestito(id_libro,id_iscritto,data_prestito)
                    break
                else:
                    print("Errore: Devi inserire solo numeri senza lettere o simboli.")
            
        if scelta=='4':
            id_prestito=input("Inserisci id del prestito: ")
            if re.search(r'^\d+$', id_prestito):
                Biblioteca().restituzione(id_prestito)
                break
            else:
                print("Errore: Devi inserire solo numeri senza lettere o simboli.")
        if scelta=='5':
            print('Uscita dal programma')
            break
    except:
        print("Inserisci un valore valido")