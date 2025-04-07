from Medico import*
from Paziente import*
from Visita import*
import sqlite3

while True:
    print('''
    1. Registrazione del medico
    2. Registrazione paziente
    3. Registrazione visita
    4. Esci
    ''')
    scelta=input("Inserisci la tua scelta: ")
    match scelta:
        case "1":
            conn,cur=aperturaConnessione()
            cur.execute('''
                select * from paziente
                where id_medico is null
            ''')

            risultato_query=cur.fetchall()
            chiusuraConnessione(conn,cur)
            if not risultato_query:
                print("Non ci sono pazienti registrati, impossibile registrare un medico")
                continue
            nome=input("Inserisci nome del medico: ")
            nome=inputStringaSenzaNumero(nome)
            cognome=input("Inserisci cognome del medico: ")
            cognome=inputStringaSenzaNumero(cognome)
            while True:
                disponibilita=input("Inserisci disponibilità del medico (input si/no): ").lower()
                disponibilita=inputStringaConNumero(disponibilita)
                if disponibilita=="si" or disponibilita=="no":
                    Medico().registrazioneMedico(nome,cognome,disponibilita)
                    break
                else:
                    print("Errore: hai inserito un valore non valido, riprova")
                    continue
        case "2":
            nome=input("Inserisci nome del paziente: ")
            nome=inputStringaSenzaNumero(nome)
            cognome=input("Inserisci cognome del paziente: ")
            cognome=inputStringaSenzaNumero(cognome)

            Paziente().registrazionePaziente(nome,cognome)
        case "3":
            conn,cur=aperturaConnessione()
            #controllo richiasta della consegna se esistono pazienti che hanno bisogno e se ci sono medici disponibili per continuare
            cur.execute('''
                select * from paziente
                where id_medico is null
            ''')
            risultato_query1=cur.fetchall()
            if not risultato_query1:
                print("Non ci sono pazienti che hanno bisogno di un medico")
                continue
            cur.execute('''
                select * from medici    
                where numero_pazienti <3 and disponibilita=="si"
            ''')
            risultato_query2=cur.fetchall()
            if not risultato_query2:
                print("Non ci sono medici disponibili")
                continue
            #output dei medici e pazienti disponibili
            print("Pazienti disponibili: ")
            for row in risultato_query1:
                print(row[0],row[1],row[2])
            print("Medici disponibili: ")

            for row in risultato_query2:
                print(row[0],row[1],row[2],row[4]) 
            #da qui in poi ci saranno i controlli dell'input in cui si verifica se l'utente inserisce valori giusti come per esempio pazienti che esistono e che hanno bisogno di un medico, medici disponibili     
            while True:      
                id_paziente=input("Inserisci id del paziente: ")
                id_paziente=inputNumero(id_paziente)
                cur.execute('''
                    select * from paziente
                    where id_paziente=? 
                ''',(id_paziente,))
                risultato_query1=cur.fetchall()
                #controllo che il paziente non ha ancora un medico
                if not risultato_query1 or risultato_query1[0][3] is not None:
                    print("Il paziente non è disponibile")
                    continue
                elif risultato_query1[0][3] is not None:
                    print("Il paziente ha gia un medico")
                break
            while True:
                #controllo che il medico sia esista,non abbia superato 3 pazienti e che sia disponibile
                id_medico=input("Inserisci id del medico: ")
                id_medico=inputNumero(id_medico)
                cur.execute('''
                    select * from medici    
                    where id_medico= ? and numero_pazienti <3 and disponibilita=="si"
                ''',(id_medico,))
                risultato_query=cur.fetchall()
                if not risultato_query:
                    print("Il medico non è disponibile")
                    continue
                Visita().registrazioneVisita(id_paziente,id_medico)
                #quando viene registrato una visita faccio update della colonna id_medico nella tabella paziente
                cur.execute('''
                    update paziente
                    set id_medico=?
                    where id_paziente=?
                ''',(id_medico,id_paziente))
                #faccio update dei numeri di pazienti
                cur.execute('''
                    update medici
                    set numero_pazienti=numero_pazienti+1
                    where id_medico=?
                ''',(id_medico,))
                conn.commit()
                break
            chiusuraConnessione(conn,cur)

        case "4":
            print("Uscita dal programma")
            break
        case _:
            print("Valore inserito non valido")