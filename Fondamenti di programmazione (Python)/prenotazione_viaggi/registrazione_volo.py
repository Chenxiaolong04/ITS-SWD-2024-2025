import sqlite3
from DatabaseUtilities import *
import string
import re
class Volo:
    def registrazione_volo(self,partenza,destinazione,ora,durata):
        conn,cur=aperturaConnessione()
        cur.execute('''
            insert into registrazione_volo(partenza,destinazione,ora,durata)
            values(?,?,?,?)
        ''',(partenza,destinazione,ora,durata))
        conn.commit()
        print("Registrazione volo avvenuta con successo")
        chiusura_connessione(conn,cur)
    def inputPartenza(self):
        while True:
            partenza=input("Inserisci partenza: ")
            partenza = partenza.strip()
            partenza = partenza.translate(str.maketrans("", "", string.punctuation))
            if partenza=="":
                print("Errore: hai inserito solo spazzi nell'input")
                continue
            if re.search(r'\d', partenza):
                print("Errore: la partenza non può contenere numeri, inserire nuovamente.")
                continue
            return partenza
    def inputDestinazione(self):
        while True:
            destinazione=input("Inserisci destinazione: ")
            destinazione = destinazione.strip()
            destinazione = destinazione.translate(str.maketrans("", "", string.punctuation))
            if destinazione=="":
                print("Errore: hai inserito solo spazzi nell'input")
                continue
            if re.search(r'\d', destinazione):
                print("Errore: la destinazione non può contenere numeri, inserire nuovamente.")
                continue
            return destinazione
    def inputOrario(self):
        while True:
                orario=input("Inserisci orario di partenza: ")
                orario = orario.strip()
                if orario=="":
                    print("Errore: hai inserito solo spazzi nell'input")
                    continue
                return orario
    def inputDurata(self):
        while True:
            try:
                durata=int(input("Inserisci durata di volo: "))
                if(durata<=0):
                    print("Errore: la durata non puo' essere negativa o uguale a 0 ")
                    continue
                return durata
            except Exception as e:
                print(e)
    def prenotazioneVolo(self):
        """Gestisce l'intero processo di prenotazione di un volo in un'unica funzione"""
        conn, cur = None, None
        try:
            conn, cur = aperturaConnessione()
            
            # 1. Mostra voli disponibili con formato tabellare
            print("\nVOLI DISPONIBILI:")
            print("╔════╦════════════╦═════════════╦══════════╦════════╗")
            print("║ ID ║ Partenza   ║ Destinazione║ Orario   ║ Durata ║")
            print("╠════╬════════════╬═════════════╬══════════╬════════╣")
            
            cur.execute("SELECT * FROM registrazione_volo ORDER BY partenza, orario")
            voli = cur.fetchall()
            
            if not voli:
                print("║                Nessun volo disponibile                ║")
                print("╚═══════════════════════════════════════════════════════╝")
                return
            
            for volo in voli:
                print(f"║ {volo[0]:<2} ║ {volo[1]:<10} ║ {volo[2]:<11} ║ {volo[3]:<8} ║ {volo[4]:<6} ║")
            print("╚════╩════════════╩═════════════╩══════════╩════════╝")

            # 2. Selezione volo con validazione
            while True:
                try:
                    id_volo = int(input("\n► Inserisci ID del volo da prenotare (0 per annullare): "))
                    
                    if id_volo == 0:
                        print("Prenotazione annullata.")
                        return
                    
                    cur.execute("SELECT 1 FROM registrazione_volo WHERE id_volo = ?", (id_volo,))
                    if not cur.fetchone():
                        print("❌ Errore: ID volo non valido. Riprovare.")
                        continue
                        
                    break
                except ValueError:
                    print("❌ Errore: inserire un numero valido.")

            # 3. Mostra passeggeri registrati
            print("\nPASSEGGERI REGISTRATI:")
            print("╔════╦══════════════╦══════════════╗")
            print("║ ID ║ Nome         ║ Cognome      ║")
            print("╠════╬══════════════╬══════════════╣")
            
            cur.execute("SELECT * FROM registrazione_passeggero ORDER BY cognome, nome")
            passeggeri = cur.fetchall()
            
            if not passeggeri:
                print("║     Nessun passeggero registrato      ║")
                print("╚═══════════════════════════════════════╝")
                return
            
            for p in passeggeri:
                print(f"║ {p[0]:<2} ║ {p[1]:<12} ║ {p[2]:<12} ║")
            print("╚════╩══════════════╩══════════════╝")

            # 4. Selezione passeggero con validazione
            while True:
                try:
                    id_passeggero = int(input("\n► Inserisci ID del passeggero (0 per annullare): "))
                    
                    if id_passeggero == 0:
                        print("Prenotazione annullata.")
                        return
                    
                    cur.execute("SELECT 1 FROM registrazione_passeggero WHERE id_passeggero = ?", (id_passeggero,))
                    if not cur.fetchone():
                        print("❌ Errore: ID passeggero non valido. Riprovare.")
                        continue
                        
                    break
                except ValueError:
                    print("❌ Errore: inserire un numero valido.")

            # 5. Verifica prenotazione esistente
            cur.execute('''SELECT 1 FROM prenotazioni_volo 
                        WHERE passeggero_id = ? AND volo_id = ?''', 
                    (id_passeggero, id_volo))
            
            if cur.fetchone():
                print("\n❌ Attenzione: questo passeggero ha già prenotato questo volo!")
                return

            # 6. Conferma e completamento prenotazione
            print("\nRIEPILOGO PRENOTAZIONE:")
            cur.execute("SELECT partenza, destinazione, orario FROM registrazione_volo WHERE id_volo = ?", (id_volo,))
            volo = cur.fetchone()
            
            cur.execute("SELECT nome, cognome FROM registrazione_passeggero WHERE id_passeggero = ?", (id_passeggero,))
            passeggero = cur.fetchone()
            
            print(f"• Volo: {volo[0]} → {volo[1]} alle {volo[2]}")
            print(f"• Passeggero: {passeggero[1]} {passeggero[0]}")
            
            conferma = input("\nConfermare la prenotazione? (s/n): ").lower()
            if conferma != 's':
                print("Prenotazione annullata.")
                return

            # 7. Effettua la prenotazione
            cur.execute('''INSERT INTO prenotazioni_volo(passeggero_id, volo_id) 
                        VALUES(?, ?)''', (id_passeggero, id_volo))
            conn.commit()
            
            print("\n✅ PRENOTAZIONE CONFERMATA CON SUCCESSO!")
            print("Grazie per aver scelto il nostro servizio!")

        except sqlite3.Error as e:
            print(f"\n❌ ERRORE DATABASE: {e}")
        except Exception as e:
            print(f"\n❌ ERRORE IMPREVISTO: {e}")
        finally:
            if conn and cur:
                chiusura_connessione(conn, cur)