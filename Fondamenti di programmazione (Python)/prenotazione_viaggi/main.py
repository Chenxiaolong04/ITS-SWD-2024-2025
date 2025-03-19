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
            ''')
            if scelta=="1":
                Volo().registrazione_volo(Volo().inputPartenza(),Volo().inputDestinazione(),Volo().inputOrario(),Volo().inputDurata())
    elif scelta=="2":
        while True:
            scelta=input('''
                Inserisci la scelta:
                1.Registrazione hotel
                2.Prenotazione via
            ''')
    elif scelta=="3":
        while True:
            scelta=input('''
                Inserisci la scelta:
                1.Registrazione auto
                2.Prenotazione auto
            ''')
    elif scelta=="4":
        #nome=passeggero().inputNome()
        #cognome=passeggero().inputCognome()
        passeggero().registrazione_passeggero(passeggero().inputNome(),passeggero().inputCognome())
    elif scelta=="5":
        print("Uscita dal programma")
        break