'''
1 creazione del file e poi ogni volta fare append
2 fare un ciclo per ogni volta che un utente inserisce il dato con all'interno un try exept cosi se non valido torna indietro e lo fa eseguire nuovamene
3 dopo aver ottenuto tutti i dati inseriti scriverli sul file di testo un una piccola parte di desto davanti prima di salvare la variabile cosi è piu facile ritrovare il dato
'''
with open("output.txt", "a") as file:
    nome = input("Inserisci il tuo nome: ")
    while nome=='':
        nome = input("Inserisci il tuo nome nuovamente: ")
    while True:
        try:
            eta = int(input("Quanti anni pensi che abbia? "))
            if eta < 0:  
                print("Errore: l'età non può essere negativa.")
                continue
            break
        except:
            print("Errore: inserisci un numero intero valido per l'età.")
    while True:
        try:
            altezza = float(input("Quanto pensi che sia alto (in metri)? "))
            if altezza < 0:  
                print("Errore: l'altezza non può essere negativa.")
                continue
            break
        except:
            print("Errore: inserisci un numero decimale valido per l'altezza.")
    while True:
        sposato = input("Pensi che sia sposato? (si/no): ").strip().lower()
        if sposato == "si" or sposato == "no":
            break
        print("Errore: rispondi con 'si' per sì o 'no' per no.")
    materie = input("Quali materie pensi che insegni? (separate da virgola): ").lower().strip().split(",")
    file.write('Sondaggio di: '+nome.capitalize()+'\n')
    file.write('Eta: '+str(eta)+'\n')
    file.write('Altezza: ' +str(altezza)+'\n')
    file.write('Sposato: '+sposato +'\n')
    file.write('Lista delle Materie: '+str(materie)+'\n')
    print("Sondaggio completato")