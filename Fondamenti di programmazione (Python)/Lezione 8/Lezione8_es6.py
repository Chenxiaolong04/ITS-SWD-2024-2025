elenco = []
while True:
    numero = input("Inserisci un numero: ")    
    if numero == "done" or numero =="Done":
      print("Inserimento numeri concluso.")
      break  
    try:
      numero = float(numero)  
      elenco.append(numero)
    except:
      print("Inserisci un numero valido!")
print("Il numero più grande e': ", max(elenco),"e il numero piu piccolo e': ",min(elenco))