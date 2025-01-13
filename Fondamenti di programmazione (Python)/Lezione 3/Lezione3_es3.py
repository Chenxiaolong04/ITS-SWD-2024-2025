try:
    num=float(input("Inserisci un valore compreso tra 0.0 e 1: "))
    if(num>1 or num<0):
        print("Bravo kiwi non puoi mettere questo numero")
    elif(num>=0.9):
        print("Il tuo grado e':","A")
    elif(num>=0.8):
        print("Il tuo grado e':","B")
    elif(num>=0.7):
        print("Il tuo grado e':","C")
    elif(num>=0.6):
        print("Il tuo grado e':","D")
    elif(num<0.6):
        print("Il tuo grado e':","F")    
except:
    print("Inserisci un numero kiwi")