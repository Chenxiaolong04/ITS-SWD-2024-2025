"""
#1
stringa1=input("Inserisci la prima stringa: ")
stringa2=input("Inserisci la seconda stringa: ")
print(stringa1+stringa2)
#2
numero1=float(input("Inserisci il primo numero: "))
numero2=float(input("Inserisci il secondo numero: "))
print(numero1+numero2)

#3
numero1=float(input("Inserisci il primo numero: "))
numero2=float(input("Inserisci il secondo numero: "))
if(numero1+numero2==0):
    print("Il risultato e' uguale a 0")
elif(numero1+numero2>0):
    print("Il risultato e' positivo")
else:
    print("Il risultato e' negativo")
print(numero1+numero2)
"""

#5
"""
somma=0
while True:
    try:
        numero1=input("Inserisci un numero: ")
        if(numero1=="done"):
            print("Sei uscito dal ciclo")
            break
        somma+=float(numero1)
        numero2=input("Inserisci un numero: ")
        if(numero2=="done"):
            print("Sei uscito dal ciclo")
            break
        somma+=float(numero2)
    except:
        print("Inserisci un valore valido")
        continue
if(somma==0):
    print("Il risultato e' uguale a 0")
    print(somma)
elif(somma>0):
    print("Il risultato e' positivo")
    print(somma)
else:
    print("Il risultato e' negativo")
    print(somma)
"""  
#6
""" 
def inserimento():
    n=input("Inserisci un valore: ")
    if(n=="done"):
        return n
    else:
        return float(n)
def somma(somma,n):
    somma+=n
    return somma

addizione=0
while True:        
    n=inserimento()  
    if(n=="done"):
        print(n)
        break  
    addizione=somma(addizione,n)
if(addizione==0):
    print("Il risultato e' uguale a 0")
    print(addizione)
elif(addizione>0):
    print("Il risultato e' positivo")
    print(addizione)
else:
    print("Il risultato e' negativo")
    print(addizione)
 """ 
def inserimento():
    stringa=input("Inserisci un valore: ")
    if(stringa=="done"):
        return stringa
    else:
        return stringa
somma=0
file=open("numeri.txt","w")
while True:        
    stringa=inserimento()  
    if(stringa=="done"):
        print(stringa) #ctrl+h
        break 
    file.write(stringa+"\n") 

file=open("numeri.txt")#ricordarsi di cambiare tra la modalita di scrittura e lettura

for line in file:
    somma+=float(line)
output=open("risultato.txt","w")
output.write(str(somma))
print(somma)
output.close()
file.close()