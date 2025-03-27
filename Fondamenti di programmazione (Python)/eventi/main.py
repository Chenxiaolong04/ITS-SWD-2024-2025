import sqlite3
from Sala import*
from Evento import*
from Partecipante import*
while True:
    scelta=input('''
        Inserisci cosa avuoi fare
        1.Sala
        2.Evento
        3.Partecipante
        4.esci
    ''')
    match scelta:
        case "1":
            nome=input("Inserisci nome della sala: ").lower()
            nome=inputStringaConNumero(nome)
            while True: 
                disponibilita=input("Inserisci la disponibilita della sala(si/no): ").lower()
                if disponibilita!="si" and disponibilita!="no":
                    print("Errore: hai inserito un valore diverso da si o no")
                    continue
                else:
                    disponibilita=inputStringaSenzaNumero(disponibilita)
                    Sala().registrazione_sala(nome,disponibilita)
                    break
        case "2":
            risultato=Sala().visualizza_sala()
            if risultato==False:
                continue
            while True:
                id_sala=input("Inserisci l'id della sala: ")
                id_sala=inputNumero(id_sala)
                cur.execute('''
                    select * from SALA where id_sala=? and disponibilita="si"
                ''',(id_sala,))
                if cur.fetchone() is None:
                    print("Errore: l'id inserito non è presente/disponibile")
                    continue
                else:
                    break
            nome=input("Inserisci nome dell'evento: ")
            nome=inputStringaConNumero(nome)
            capienzaMassima=input("Inserisci la capienza massima: ")
            capienzaMassima=inputNumero(capienzaMassima)
            Evento().registrazione_evento(nome,capienzaMassima,id_sala)
        case "3":
            risultato=Evento().visualizza_evento()
            if risultato==False:
                continue
            conn,cur=aperturaConnessione()
            while True:
                id_evento=input("Inserisci l'id dell'evento: ")
                id_evento=inputNumero(id_evento)
                cur.execute('''
                    select * from EVENTO where id_evento=? and capienzaMassima>0
                ''',(id_evento,))
                if cur.fetchone() is None:
                    print("Errore: l'id inserito non è presente/disponibile")
                    continue
                else:
                    break
            nome=input("Inserisci nome del partecipante: ")
            nome=inputStringaSenzaNumero(nome)
            cognome=input("Inserisci cognome del partecipante: ")
            cognome=inputStringaSenzaNumero(cognome)
            Partecipante().registrazione_partecipante(nome,cognome,id_evento)
        case "4":
            break
        case _:
            print("Errore: hai inserito un valore non valido")
            continue
        