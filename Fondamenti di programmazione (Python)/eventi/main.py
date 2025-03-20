import sqlite3
from Sala import*
from Evento import*
while True:
    scelta=input('''
        Inserisci cosa avuoi fare
        1.aggiungi sala
        2.aggiungi evento
        3.aggiungi partecipante
        4.esci
    ''')
    match scelta:
        case "1":
            nome=input("Inserisci nome della sala: ")
            nome=inputStringaConNumero(nome)
            disponibilita=input("Inserisci la disponibilita della sala: ")
            disponibilita=inputStringaSenzaNumero(disponibilita)
            Sala().registrazione_sala(nome,disponibilita)
            
            
        case "2":
            nome=input("Inserisci nome dell'evento: ")
            nome=inputStringaConNumero(nome)
            capienzaMassima=input("Inserisci la capienza massima: ")
            capienzaMassima=inputNumero(capienzaMassima)
            Evento().registrazione_evento(nome,capienzaMassima)
            
        case "3":
            break
        case "4":
            break
        