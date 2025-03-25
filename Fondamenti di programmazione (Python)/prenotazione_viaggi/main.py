import sqlite3
from DatabaseUtilities import *
from registrazione_auto import *
from registrazione_hotel import *
from registrazione_passeggero import *
from registrazione_volo import *
while True:
    scelta=input('''
        Inserisci il numero della sezione in cui vuoi entrare
        1.Volo
        2.Hotel
        3.Auto
        4.Passeggero
        5.Esci
    ''')
    if scelta=="1":
        while True:
            scelta=input('''
                Inserisci la scelta:
                1.Registrazione volo
                2.Prenotazione volo
                3.Torna indietro
            ''')
            if scelta=="1":
                Volo().registrazione_volo(Volo().inputPartenza(),Volo().inputDestinazione(),Volo().inputOrario(),Volo().inputDurata())
                break
            elif scelta=="2":
                cur.execute("select * from registrazione_volo")
                risultato_query=cur.fetchall()
                for i in risultato_query:
                    print(i[0],i[1],i[2],i[3],i[4])
                Volo().prenotazioneVolo()
                chiusura_connessione(conn,cur)

                break
            elif scelta=="3":
                break
            else:
                print("Valore inserito non valido")
                continue
    elif scelta=="2":
        while True:
            scelta=input('''
                Inserisci la scelta:
                1.Registrazione hotel
                2.Prenotazione hotel
                3.Torna indietro

            ''')
            if scelta=="1":
                Hotel().registrazione_hotel(Hotel().inputNome(),Hotel().inputVia())
                break
            if scelta=="2":
                cur.execute("select * from registrazione_hotel")
                risultato_query=cur.fetchall()
                for i in risultato_query:
                    print(i[0],i[1],i[2])
                Hotel().prenotazioneHotel()
    elif scelta=="3":
        while True:
            scelta=input('''
                Inserisci la scelta:
                1.Registrazione auto
                2.Prenotazione auto
                3.Torna indietro

            ''')
            if scelta=="1":
                Auto().registrazione_noleggio(Auto().inputNome(),Auto().inputTarga())
                break
    elif scelta=="4":
        #nome=passeggero().inputNome()
        #cognome=passeggero().inputCognome()
        scelta=input('''
            Inserisci la scelta:
            1.Registrazione passegero
            2.Torna indietro
        ''')
        if scelta=="1":
            Passeggero().registrazione_passeggero(Passeggero().inputNome(),Passeggero().inputCognome())
            break
    elif scelta=="5":
        print("Uscita dal programma")
        break
    else:
        print("Valore inserito non valido")
        continue
    