import sqlite3

# Connessione al database
conn = sqlite3.connect('statistiche.sqlite')
cur = conn.cursor()
while True : 
    nome = input('Come ti chiami : \n')
    nome = nome.strip().lower()
    if nome=="":
        print("Non puoi inserire un nome vuoto")
    else:

        break

while True : 
    try:
        eta = int(input('Immetti la età che tu pensi abbia: \n'))
        break
    except:
        print("Inserisci un'eta valida (numero intero)")

while True : 
    try:
        Altezza = float(input("Immetti l'altezza che tu pensi abbia: \n"))
        break
    except:
        print("Inserisci un'altezza valida")

Materie = ""

while True:
    sposato = input('Pensi che sia sposato?  (Inserisci si o no) \n').lower()
    if sposato == 'si' :
      Celibe = True
      break
    elif sposato == 'no' :
      Celibe = False
      break
    else :
        print('Inserisci si o no')
        continue
cur.execute('INSERT INTO persona (nome,altezza,anni,sposato) VALUES (?,?,?,?)', (nome,Altezza,eta,Celibe))
id_utente = cur.lastrowid


while True :
    Materie1 = (input('Quali altre Materie pensi insegni in SWD :  (per uscire scrivi "done") \n')).lower().strip()
    if Materie1 == 'done' :
        if len(Materie1)==0:
            print('Inserisci almeno una Materia')
            continue
        else:
            break
    elif Materie1 == '' :
        print('la stringa non puo essere vuota')
        continue
    else :
        #Materie+=(Materie1 + ",").lower()
        cur.execute('INSERT INTO materie(id_utente,materia)values(?,?)',(id_utente,Materie1))

conn.commit()

conn.close()
