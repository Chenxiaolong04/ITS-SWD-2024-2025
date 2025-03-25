import sqlite3
from DatabaseUtilities import *
import string
import re
conn,cur=aperturaConnessione()
class Hotel:
    def registrazione_hotel(self,nome,via):
        cur.execute('''
            insert into registrazione_hotel(nome,via)
            values(?,?)
        ''',(nome,via))
        conn.commit()
        print("Registrazione hotel avvenuta con successo")
        chiusura_connessione(conn,cur)
    def inputNome(self):
        conn,cur=aperturaConnessione()
        while True:
            nome=input("Inserisci nome dell'hotel: ")
            nome = nome.strip()
            nome = nome.translate(str.maketrans("", "", string.punctuation))
            if nome=="":
                print("Errore: hai inserito solo spazzi nell'input")
                continue
            if not re.search(r'\d', nome):
                chiusura_connessione(conn,cur)
                return nome
            print("Errore: il nome non può contenere numeri, inserire nuovamente.")
            continue
    def inputVia(self):
        conn,cur=aperturaConnessione()
        while True:
            via=input("Inserisci via: ")
            via = via.strip()
            via = via.translate(str.maketrans("", "", string.punctuation))
            if via=="":
                print("Errore: hai inserito solo spazzi nell'input")
                continue
            chiusura_connessione(conn,cur)
            print("Registrazione via hotel avvenuta con successo")
            return via
    def prenotazioneHotel(self):
            conn,cur=aperturaConnessione()
            while True:
                try:
                    id_hotel = int(input("Inserisci id dell'hotel: "))
                    cur.execute("SELECT id_hotel FROM registrazione_hotel WHERE id_hotel = ?", (id_hotel,))
                    risultato_query = cur.fetchone()
                    if risultato_query is None:
                        print("Errore: hotel non trovato.")
                        continue
                    while True:
                        id_passeggero=int(input("Inserisci id del passeggero: "))
                        cur.execute("SELECT id_passeggero FROM registrazione_passeggero WHERE id_passeggero = ?", (id_passeggero,))
                        risultato_query = cur.fetchone()
                        if risultato_query is None:
                            print("Errore: passeggero non trovato.")
                            continue
                        cur.execute('''
                                    INSERT INTO prenotazioni_hotel(id_passeggero,id_hotel)
                                    values(?,?)
                                    ''',(id_passeggero,id_hotel))
                        conn.commit()
                        print("Prenotazione dell' hotel avvetuno con successo.")
                        break

                    break
                except Exception as e:
                    print(e)
                chiusura_connessione(conn,cur)
