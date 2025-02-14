'''
1 leggre riga per riga il file di testo
2 controllare come inizia la riga nel file di testo per sapere quale dato andare a prendere
3 dopo aver preso il dato che serve trasformarlo in un dato utilizzabile
4 effettuare tutti i calcoli per le statistiche
5 output
'''
#apertura di un file il modalita lettura e che lo chiuderà in automatico dopo aver eseguito il codice
with open("output.txt", "r") as file:
    #dichiarazione delle variabili
    righe = file.readlines()
    totale_persone = 0
    eta_totale = 0
    altezza_totale = 0
    sposato_si = 0
    sposato_no = 0
    materie = dict()
    nomi = dict()
    #lettura del file riga per riga
    for riga in righe:
        riga=riga.strip(" ")    # serve per rimuovere tutti i spazzi e non solo 1
        #controllo dell'utente
        if riga.startswith("Sondaggio di:"):
            totale_persone += 1
            nome = riga.split(":")[1].strip()#splitta la parte letta e prende la parte dopo il ':'
            if nome in nomi:
                nomi[nome] += 1
                continue
            else:
                nomi[nome] = 1
                continue
        #controllo età
        if riga.startswith("Eta:"):
            eta = int(riga.split(":")[1].strip())
            eta_totale += eta
            continue
        #controllo altezza    
        if riga.startswith("Altezza:"):
            altezza = float(riga.split(":")[1].strip())
            altezza_totale += altezza
            continue
        #controllo sposato o no    
        if riga.startswith("Sposato:"):
            sposato = riga.split(":")[1].strip()
            if sposato == "si":
                sposato_si += 1
                continue
            else:
                sposato_no += 1
                continue
        #controllo materie
        if riga.startswith("Lista delle Materie:"):
            materia_lista=riga.split(':')
            materia_lista=materia_lista[1].strip().strip('[').strip(']').split(', ')#dopo aver splittato prende la parte interessata 
            for materia in materia_lista:                                           #poi toglie tutte le cose non necessarie e la trasforma in una lista
                if materia in materie:
                    materie[materia] += 1
                    continue
                else:
                    materie[materia] = 1
                    continue
    #calcoli
    eta_media = eta_totale / totale_persone
    altezza_media = altezza_totale / totale_persone
    percentuale_sposato_si = (sposato_si / totale_persone) * 100
    percentuale_sposato_no = (sposato_no / totale_persone) * 100
    #output
    print("\n--- Statistiche del Sondaggio ---""\n")
    print("Numero totale di persone registrate: " + str(totale_persone)+"\n")
    print("Nomi e frequenze: ")
    for chiave in nomi:
        print("\t"+str(chiave) + ": " + str(nomi[chiave]) + " volte"+"\n")
    print("Età media inserita: " + str(int(eta_media)) + " anni"+"\n")
    print("Altezza media inserita: " + str(round(altezza_media, 2)) + " metri""\n")
    print("Percentuale sposato: " )
    print("Si: "+str(round(percentuale_sposato_si, 2)) + "%") 
    print("No: "+str(round(percentuale_sposato_no, 2)) + "%"+"\n")
    print("Materie menzionate e frequenze:")
    for chiave in materie:
        print("\t"+str(chiave) + ": " + str(materie[chiave]) + " volte")
