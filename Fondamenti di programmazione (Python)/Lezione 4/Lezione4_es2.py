def computegrade(num):
        if(num>=0.9):
            voto="A"
        elif(num>=0.8):
            voto="B"
        elif(num>=0.7):
            voto="C"
        elif(num>=0.6):
            voto="D"
        elif(num<0.6):
            voto="F"    
        return voto
try:
    numero=float(input("Inserisci un valore compreso tra 0.0 e 1: "))
    if(numero>1 or numero <0):
        print("Inserisci un numero valido")
    else:
        voto_finale=computegrade(numero)
        print("Il tuo voto e':",voto_finale)
except:
    print("Inserisci un valore valido")

