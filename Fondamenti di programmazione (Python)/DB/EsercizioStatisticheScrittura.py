'''
Abbiamo un programma che chiede dati in scrittura in un file.
creazione di un file sondaggio.txt, se non esiste lo andiamo a creare altrimenti andiamo a fare append
andiamo a chiedere gli input all'utente, dove le mette in delle variabili apposite
'''

from classeProva import GestioneFile

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


while True :
    Materie1 = (input('Quali altre Materie pensi insegni in SWD :  (per uscire scrivi "done") \n')).lower().strip()
    if Materie1 == 'done' :
        if len(Materie)==0:
            print('Inserisci almeno una Materia')
            continue
        else:
            break
    elif Materie1 == '' :
        print('la stringa non puo essere vuota')
        continue
    else :
        Materie+=(Materie1 + ",").lower()

quiz=GestioneFile(nome,eta,Altezza,Celibe,Materie)
quiz.scrivi_quiz("sondaggio.txt")




'''
fout.write('Sondaggio di : '+nome.capitalize()+ '\n')
fout.write('Eta : '+str(eta) + '\n')
fout.write('Altezza : ' +str(Altezza) + '\n')
fout.write('Celibe : '+str(Celibe) + '\n')
fout.write('Materie : '+ Materie + '\n')
'''