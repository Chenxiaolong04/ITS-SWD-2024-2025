import sqlite3
from DatabaseUtilities import *
from registrazione_auto import *
from registrazione_hotel import *
from registrazione_passeggero import *
from registrazione_volo import *

while True:
    scelta = input('''
        Inserisci il numero della sezione in cui vuoi entrare:
        1. Volo
        2. Hotel
        3. Auto
        4. Passeggero
        5. Esci
    ''')
    
    if scelta == "1":  # Sezione Volo
        while True:
            scelta_volo = input('''
                Inserisci la scelta:
                1. Registrazione volo
                2. Prenotazione volo
                3. Torna al menu principale
            ''')
            if scelta_volo == "1":
                Volo().registrazione_volo(Volo().inputPartenza(), Volo().inputDestinazione(), Volo().inputOrario(), Volo().inputDurata())
            elif scelta_volo == "2":
                conn, cur = aperturaConnessione()
                try:
                    # Mostra i voli disponibili
                    cur.execute("SELECT id_volo, partenza, destinazione, ora FROM registrazione_volo")
                    voli = cur.fetchall()
                    if not voli:
                        print("Nessun volo disponibile.")
                        continue
                    
                    print("Voli disponibili:")
                    for volo in voli:
                        print("ID: %d, Partenza: %s, Destinazione: %s, Orario: %s" % (volo[0], volo[1], volo[2], volo[3]))
                    
                    volo_id = input("Inserisci l'ID del volo che desideri prenotare: ")
                    if not volo_id.isdigit():
                        print("Errore: l'ID del volo deve essere un numero.")
                        continue
                    
                    # Verifica se il volo esiste
                    cur.execute("SELECT id_volo FROM registrazione_volo WHERE id_volo = ?", (volo_id,))
                    if not cur.fetchone():
                        print("Errore: volo non trovato.")
                        continue
                    
                    # Inserisci la prenotazione del volo
                    passeggero_id = input("Inserisci l'ID del passeggero: ")
                    if not passeggero_id.isdigit():
                        print("Errore: l'ID del passeggero deve essere un numero.")
                        continue
                    
                    cur.execute("INSERT INTO prenotazioni_volo (passeggero_id, volo_id) VALUES (?, ?)", (passeggero_id, volo_id))
                    conn.commit()
                    print("Prenotazione volo avvenuta con successo!")
                
                except sqlite3.Error as e:
                    print("Errore durante la prenotazione del volo: %s" % e)
                finally:
                    chiusura_connessione(conn, cur)
            
            elif scelta_volo == "3":
                break
            else:
                print("Scelta non valida. Riprova.")
    
    elif scelta == "2":  # Sezione Hotel
        while True:
            scelta_hotel = input('''
                Inserisci la scelta:
                1. Registrazione hotel
                2. Prenotazione hotel
                3. Torna al menu principale
            ''')
            if scelta_hotel == "1":
                hotel().registrazione_hotel(hotel().inputNome(), hotel().inputVia())
            elif scelta_hotel == "2":
                conn, cur = aperturaConnessione()
                try:
                    # Mostra gli hotel disponibili
                    cur.execute("SELECT id_hotel, nome, via FROM registrazione_hotel")
                    hotel = cur.fetchall()
                    if not hotel:
                        print("Nessun hotel disponibile.")
                        continue
                    
                    print("Hotel disponibili:")
                    for h in hotel:
                        print("ID: %d, Nome: %s, Via: %s" % (h[0], h[1], h[2]))
                    
                    hotel_id = input("Inserisci l'ID dell'hotel che desideri prenotare: ")
                    if not hotel_id.isdigit():
                        print("Errore: l'ID dell'hotel deve essere un numero.")
                        continue
                    
                    # Verifica se l'hotel esiste
                    cur.execute("SELECT id_hotel FROM registrazione_hotel WHERE id_hotel = ?", (hotel_id,))
                    if not cur.fetchone():
                        print("Errore: hotel non trovato.")
                        continue
                    
                    # Inserisci la prenotazione dell'hotel
                    passeggero_id = input("Inserisci l'ID del passeggero: ")
                    if not passeggero_id.isdigit():
                        print("Errore: l'ID del passeggero deve essere un numero.")
                        continue
                    
                    cur.execute("INSERT INTO prenotazioni_hotel (passeggero_id, hotel_id) VALUES (?, ?)", (passeggero_id, hotel_id))
                    conn.commit()
                    print("Prenotazione hotel avvenuta con successo!")
                
                except sqlite3.Error as e:
                    print("Errore durante la prenotazione dell'hotel: %s" % e)
                finally:
                    chiusura_connessione(conn, cur)
            
            elif scelta_hotel == "3":
                break
            else:
                print("Scelta non valida. Riprova.")
    
    elif scelta == "3":  # Sezione Auto
        while True:
            scelta_auto = input('''
                Inserisci la scelta:
                1. Registrazione auto
                2. Prenotazione auto
                3. Torna al menu principale
            ''')
            if scelta_auto == "1":
                auto().registrazione_noleggio(auto().inputNome(), auto().inputTarga(), auto().inputDurata())
            elif scelta_auto == "2":
                conn, cur = aperturaConnessione()
                try:
                    # Mostra le auto disponibili
                    cur.execute("SELECT id_noleggio, nome, targa FROM registrazione_auto")
                    auto = cur.fetchall()
                    if not auto:
                        print("Nessuna auto disponibile.")
                        continue
                    
                    print("Auto disponibili:")
                    for a in auto:
                        print("ID: %d, Nome: %s, Targa: %s" % (a[0], a[1], a[2]))
                    
                    auto_id = input("Inserisci l'ID dell'auto che desideri prenotare: ")
                    if not auto_id.isdigit():
                        print("Errore: l'ID dell'auto deve essere un numero.")
                        continue
                    
                    # Verifica se l'auto esiste
                    cur.execute("SELECT id_noleggio FROM registrazione_auto WHERE id_noleggio = ?", (auto_id,))
                    if not cur.fetchone():
                        print("Errore: auto non trovata.")
                        continue
                    
                    # Inserisci la prenotazione dell'auto
                    passeggero_id = input("Inserisci l'ID del passeggero: ")
                    if not passeggero_id.isdigit():
                        print("Errore: l'ID del passeggero deve essere un numero.")
                        continue
                    
                    cur.execute("INSERT INTO prenotazioni_auto (passeggero_id, auto_id) VALUES (?, ?)", (passeggero_id, auto_id))
                    conn.commit()
                    print("Prenotazione auto avvenuta con successo!")
                
                except sqlite3.Error as e:
                    print("Errore durante la prenotazione dell'auto: %s" % e)
                finally:
                    chiusura_connessione(conn, cur)
            
            elif scelta_auto == "3":
                break
            else:
                print("Scelta non valida. Riprova.")
    
    elif scelta == "4":  # Sezione Passeggero
        passeggero().registrazione_passeggero(passeggero().inputNome(), passeggero().inputCognome())
    
    elif scelta == "5":  # Uscita
        print("Uscita dal programma.")
        break
    
    else:
        print("Scelta non valida. Riprova.")